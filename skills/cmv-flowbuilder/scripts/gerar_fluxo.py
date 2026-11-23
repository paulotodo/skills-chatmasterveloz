#!/usr/bin/env python3
"""Monta o .json de um fluxo do FlowBuilder a partir de uma descrição compacta e confere o resultado.

Uso:
  python3 gerar_fluxo.py descricao.json fluxo.json           gera o arquivo e roda o validador
  python3 gerar_fluxo.py descricao.json fluxo.json --final   valores a trocar contam como erro
  python3 gerar_fluxo.py --teste                             autoteste

A descrição compacta está explicada em references/descricao-compacta.md, com um exemplo em
assets/descricao-exemplo.json. Só entram os blocos cujo formato foi observado num arquivo exportado
(references/formato-json.md); os demais são montados no editor.

Código de saída: 0 gerado sem erros, 1 com erros do validador, 2 descrição inválida ou ilegível.
"""
import json
import random
import string
import sys
from collections import defaultdict
from pathlib import Path

sys.dont_write_bytecode = True  # não deixar __pycache__ dentro da pasta da skill
sys.path.insert(0, str(Path(__file__).resolve().parent))
import validar_fluxo  # noqa: E402

ESTILO = {"backgroundColor": "#13111C", "padding": 0, "borderRadius": 8}
LIGACAO = {"style": {"stroke": "#667eea", "strokeWidth": 3}, "animated": False, "type": "smoothstep"}
MARCADOR = validar_fluxo.MARCADOR
UMA = {"": "a"}  # bloco de uma saída só: a ligação não precisa dizer a saída
# Fatos dos artigos bloco-horario-de-expediente.md e aba-horarios-em-setores-e-chatbot.md (references/docs/recursos/).
HORARIO_NA_EMPRESA = [
    "O horário não vai no arquivo nem fica no bloco: vem da aba Horários do Setor escolhido no bloco (menu Setores & Chatbot › editar o Setor › aba Horários). Quem preenche é a pessoa, no painel: não ofereça arquivo “já com os horários” (no arquivo, horário só entra como texto de mensagem).",
    "A aba Horários só aparece com o Gerenciamento de Expediente em Gerenciamento Por Setor, no menu Configurações › Opções › Geral. Sem isso, não há horário para o bloco conferir.",
    "Ligar o Gerenciamento Por Setor vale para a empresa inteira: todos os Setores passam a seguir o horário que já está na aba Horários de cada um, inclusive os que ninguém nunca abriu. Mande conferir a aba de todos os Setores, não só a do Setor do bloco.",
]

# tipo da descrição: (campos obrigatórios, campos opcionais)
CAMPOS = {
    "conteudo": ({"itens"}, set()),
    "menu": ({"mensagem", "opcoes"}, {"botao", "cabecalho", "rodape", "resposta_invalida", "sem_resposta_minutos"}),
    "pergunta": ({"mensagem"}, set()),
    "variavel": ({"nome"}, set()),
    "condicao": ({"valor"}, {"compara"}),
    "switch": ({"regras"}, set()),
    "tag": ({"nome"}, {"id"}),
    "intervalo": ({"segundos"}, set()),
    "msg_interna": ({"mensagem"}, set()),
    "codigo_js": ({"codigo"}, set()),
    "enviar_email": ({"assunto", "mensagem"}, {"para", "conta_id"}),
    "horario": ({"nome"}, {"id"}),
    "setor": ({"nome"}, {"id"}),
    "encerrar": (set(), {"mensagem"}),
    "marcador": ({"instrucao"}, set()),
}


class Invalida(Exception):
    """Descrição compacta com problemas; args[0] é a lista deles."""


def novo_id(tamanho=30, letras=string.ascii_letters + string.digits):
    return "".join(random.choices(letras, k=tamanho))


def da_conta(bloco, o_que):
    """sec e secName de Setor ou tag; sem o ID da conta, deixa o marcador que o validador lista."""
    ident = bloco.get("id")
    if isinstance(ident, int) and not isinstance(ident, bool) and ident > 0:
        return {"sec": ident, "secName": bloco["nome"]}
    return {"sec": 0, "secName": f"{MARCADOR}: {o_que} {bloco['nome']}"}


def construir(b):
    """Devolve (type, data, largura, altura, saídas {nome na descrição: sourceHandle}, o que conferir)."""
    tipo = b["tipo"]
    if tipo == "conteudo":
        itens, conta = [], {"message": 0, "interval": 0}
        for item in b["itens"]:
            if isinstance(item, bool) or not isinstance(item, (str, int)) or item == "":
                raise ValueError("cada item é um texto (mensagem) ou um número inteiro (segundos de intervalo)")
            if isinstance(item, int) and not 1 <= item <= 120:
                raise ValueError("o intervalo dentro do Conteúdo vai de 1 a 120 segundos; para esperar mais, use o bloco Intervalo")
            especie = "message" if isinstance(item, str) else "interval"
            itens.append({"type": especie, "value": str(item), "number": f"{especie}{conta[especie]}"})
            conta[especie] += 1
        if not itens:
            raise ValueError("a lista itens está vazia")
        return "singleBlock", {"seq": [i["number"] for i in itens], "elements": itens}, 198, 95 + 54 * (len(itens) - 1), UMA, None
    if tipo == "menu":
        opcoes = []
        for numero, o in enumerate(b["opcoes"], 1):
            titulo, descricao = (o, "") if isinstance(o, str) else (o[0], o[1] if len(o) > 1 else "")
            opcoes.append({"number": numero, "value": titulo, "description": descricao})
        dados = {
            "message": b["mensagem"], "arrayOption": opcoes, "botfiles": "", "menuType": "list",
            "listButtonText": b.get("botao", "Ver opções"), "listHeaderText": b.get("cabecalho", ""),
            "listFooterText": b.get("rodape", ""), "buttonHeaderText": "", "buttonFooterText": "",
            "enableElse": bool(b.get("resposta_invalida")),
        }
        saidas = {str(o["number"]): f"a{o['number']}" for o in opcoes}
        if dados["enableElse"]:
            saidas["invalida"] = "else"
        if b.get("sem_resposta_minutos"):
            dados["semResposta"] = {"minutos": int(b["sem_resposta_minutos"])}
            saidas["sem_resposta"] = "semResposta"
        return "menu", dados, 155, 145 + 24 * max(len(saidas) - 2, 0), saidas, None
    if tipo == "pergunta":
        return "question", {"message": b["mensagem"], "arrayOption": []}, 198, 92, UMA, "preencha Sem resposta e Mover de setor por inatividade, se o fluxo precisar: o arquivo não leva esses campos"
    if tipo == "variavel":
        return "variable", {"message": "%" + str(b["nome"]).strip("%") + "%", "arrayOption": []}, 198, 92, UMA, None
    if tipo == "condicao":
        modos = {"resposta": (1, 1, "Tipo Resposta da Pergunta, Condição Igual"), "tags": (2, 3, "Tipo Tag, Condição Contém")}
        if b.get("compara", "resposta") not in modos:
            raise ValueError("compara aceita “resposta” ou “tags”; as outras condições não têm formato observado")
        chave, condicao, esperado = modos[b.get("compara", "resposta")]
        nota = f"deve estar com {esperado} e Valor “{b['valor']}”; confira também se a saída Verdadeiro leva ao caminho certo"
        return "condition", {"key": chave, "condition": condicao, "value": b["valor"]}, 198, 216, {"verdadeiro": "a", "falso": "b"}, nota
    if tipo == "switch":
        regras, saidas = [], {}
        for r in b["regras"]:
            tag = r.get("tag_id")
            regra = {"id": "r" + novo_id(12, string.ascii_lowercase + string.digits), "label": r["nome"], "operator": "possui",
                     "tagIds": [tag if isinstance(tag, int) and tag > 0 else 0]}
            regras.append(regra)
            saidas[r["nome"]] = f"regra-{regra['id']}"
        if len(saidas) != len(regras) or "nenhuma" in saidas:
            raise ValueError("cada regra precisa de um nome diferente, e nenhuma pode se chamar “nenhuma”")
        saidas["nenhuma"] = "fallback"
        return "switch", {"rules": regras}, 210, 150 + 29 * len(regras), saidas, "cada regra deve estar com a comparação “possui a tag” e a tag certa"
    if tipo == "tag":
        return "tag", da_conta(b, "tag"), 195, 92, UMA, None
    if tipo == "intervalo":
        if isinstance(b["segundos"], bool) or not isinstance(b["segundos"], int):
            raise ValueError("segundos é um número inteiro")
        if not 1 <= b["segundos"] <= 120:
            raise ValueError("segundos vai de 1 a 120: com mais de 2 minutos o bloco ganha a saída Janela expirada, que não tem formato observado; monte essa espera no editor")
        return "interval", {"label": f"Intervalo {b['segundos']} seg.", "sec": str(b["segundos"])}, 195, 92, UMA, None
    if tipo == "msg_interna":
        return "internal", {"message": b["mensagem"], "arrayOption": []}, 198, 92, UMA, None
    if tipo == "marcador":
        return "internal", {"message": f"{MARCADOR} NO EDITOR: {b['instrucao']}", "arrayOption": []}, 198, 92, UMA, None
    if tipo == "codigo_js":
        return "wbh", {"message": b["codigo"], "condition": 2, "arrayOption": []}, 208, 92, UMA, "confira o campo Tipo (MENU ou REQUISIÇÃO) e use Testar Código"
    if tipo == "enviar_email":
        conta = b.get("conta_id")
        conta = conta if isinstance(conta, int) and not isinstance(conta, bool) and conta > 0 else 0  # 0: o validador manda escolher em Enviar por
        dados = {"origem": "conta", "contaId": conta, "provedorId": None, "para": b.get("para", ""), "assunto": b["assunto"], "corpo": b["mensagem"]}
        return "email", dados, 178, 136, {"enviado": "a", "nao_enviado": "b"}, None
    if tipo == "horario":
        return "away", da_conta(b, "Setor"), 195, 169, {"dentro": "a", "fora": "b"}, "confira se a saída Dentro do Horário leva ao caminho de dentro do expediente; se estiver invertida, troque as duas ligações"
    if tipo == "setor":
        return "queue", da_conta(b, "Setor"), 195, 92, {}, None
    return "close", {"message": b.get("mensagem", ""), "arrayOption": []}, 197, 94, {}, None


def montar(descricao):
    """Devolve (fluxo, lista do que conferir no editor). Levanta Invalida com a lista de problemas."""
    problemas = []
    if not isinstance(descricao, dict) or not isinstance(descricao.get("blocos"), list) or not isinstance(descricao.get("ligacoes"), list):
        raise Invalida(["A descrição precisa ser um objeto com as listas “blocos” e “ligacoes”."])
    nos = {"inicio": {"id": "1", "type": "start", "data": {"label": "Início"}, "width": 155, "height": 58}}
    saidas, conferir, recusados = {"inicio": UMA}, [], set()
    for posicao, b in enumerate(descricao["blocos"], 1):
        onde = f"Bloco {posicao}"
        if not isinstance(b, dict) or not isinstance(b.get("apelido"), str) or not b["apelido"]:
            problemas.append(f"{onde}: falta o campo apelido.")
            continue
        onde = f"Bloco “{b['apelido']}”"
        tipo = b.get("tipo")
        recusados.add(b["apelido"])  # sai da lista se o bloco for aceito
        if b["apelido"] in nos:
            recusados.discard(b["apelido"])
            problemas.append(f"{onde}: apelido repetido (“inicio” já é o bloco Início).")
            continue
        if tipo not in CAMPOS:
            problemas.append(f"{onde}: tipo “{tipo}” não existe no gerador. Tipos aceitos: {', '.join(CAMPOS)}. Bloco fora dessa lista não tem formato observado: use o tipo marcador ou monte no editor.")
            continue
        obrigatorios, opcionais = CAMPOS[tipo]
        campos = set(b) - {"apelido", "tipo"}
        if obrigatorios - campos or campos - obrigatorios - opcionais:
            falta, sobra = sorted(obrigatorios - campos), sorted(campos - obrigatorios - opcionais)
            problemas.append(f"{onde}: " + "; ".join(t for t in (falta and f"faltam os campos {falta}", sobra and f"campos desconhecidos {sobra}") if t) + ".")
            continue
        try:
            tipo_json, dados, largura, altura, saidas[b["apelido"]], nota = construir(b)
        except (ValueError, TypeError, KeyError, IndexError, AttributeError) as e:
            problemas.append(f"{onde}: {e if isinstance(e, ValueError) else f'campo com formato inesperado ({type(e).__name__}: {e})'}.")
            continue
        recusados.discard(b["apelido"])
        nos[b["apelido"]] = {"id": novo_id(), "type": tipo_json, "data": dados, "width": largura, "height": altura}
        if nota:
            conferir.append(f"{validar_fluxo.NOMES[tipo_json]} “{b['apelido']}”: {nota}.")

    ligacoes, vizinhos = [], defaultdict(list)
    for posicao, lig in enumerate(descricao["ligacoes"], 1):
        if not isinstance(lig, list) or len(lig) not in (2, 3):
            problemas.append(f"Ligação {posicao}: use [origem, destino] ou [origem, saída, destino].")
            continue
        origem, saida, destino = (lig[0], "", lig[1]) if len(lig) == 2 else (lig[0], str(lig[1]), lig[2])
        desconhecidos = [a for a in (origem, destino) if a not in saidas]
        if desconhecidos:
            if not set(desconhecidos) <= recusados:  # bloco já recusado acima não gera segundo erro
                problemas.append(f"Ligação {posicao}: apelido desconhecido: {', '.join(map(str, desconhecidos))}.")
            continue
        if saida not in saidas[origem]:
            nomes = [n for n in saidas[origem] if n]
            motivo = "é um bloco final, sem saída" if not saidas[origem] else f"tem as saídas {nomes}; escreva [origem, saída, destino]" if nomes else "tem uma saída só; escreva [origem, destino]"
            problemas.append(f"Ligação {posicao}: “{origem}” {motivo}.")
            continue
        ligacoes.append((origem, saidas[origem][saida], destino))
        vizinhos[origem].append(destino)
    if problemas:
        raise Invalida(problemas)

    # posição: uma coluna por distância do Início; blocos da mesma coluna empilhados
    coluna, fila = {"inicio": 0}, ["inicio"]
    while fila:
        atual = fila.pop(0)
        for v in vizinhos[atual]:
            if v not in coluna:
                coluna[v] = coluna[atual] + 1
                fila.append(v)
    solta, altura_da_coluna = max(coluna.values()) + 1, defaultdict(int)
    fluxo = {"nodes": [], "connections": []}
    for apelido, no in nos.items():
        c = coluna.get(apelido, solta)
        fluxo["nodes"].append({"id": no["id"], "position": {"x": 300 * c, "y": altura_da_coluna[c]}, "data": no["data"],
                               "type": no["type"], "width": no["width"], "height": no["height"], "style": dict(ESTILO)})
        altura_da_coluna[c] += no["height"] + 60
    for origem, handle, destino in ligacoes:
        o, d = nos[origem]["id"], nos[destino]["id"]
        fluxo["connections"].append({**LIGACAO, "source": o, "sourceHandle": handle, "target": d, "targetHandle": None,
                                     "id": f"reactflow__edge-{o}{handle}-{d}"})
    return fluxo, conferir


def na_empresa(fluxo):
    """O que o arquivo não leva e a pessoa configura no painel; hoje, só o Horário de Expediente pede isso."""
    return HORARIO_NA_EMPRESA if any(n["type"] == "away" for n in fluxo["nodes"]) else []


def gerar_arquivo(entrada, saida, final=False):
    try:
        fluxo, conferir = montar(json.loads(Path(entrada).read_text(encoding="utf-8-sig")))
    except (OSError, ValueError) as e:
        print(f"Não foi possível ler {entrada}: {e}")
        return 2
    except Invalida as e:
        print(f"Descrição inválida ({len(e.args[0])} problema(s)); nada foi gerado:")
        for problema in e.args[0]:
            print(f"  - {problema}")
        return 2
    Path(saida).write_text(json.dumps(fluxo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    codigo = validar_fluxo.validar_arquivo(saida, final)
    if conferir:
        print(f"\nCONFERIR NO EDITOR ({len(conferir)}): formato observado, com significado não confirmado")
        for item in conferir:
            print(f"  - {item}")
    if na_empresa(fluxo):
        print(f"\nCONFIGURAR NA EMPRESA ({len(na_empresa(fluxo))}): o Horário de Expediente depende disto, e o arquivo não leva")
        for item in na_empresa(fluxo):
            print(f"  - {item}")
    return codigo


def autoteste():
    pasta = Path(__file__).resolve().parent.parent / "assets"
    exemplo = json.loads((pasta / "descricao-exemplo.json").read_text(encoding="utf-8"))
    fluxo, _ = montar(exemplo)
    erros = validar_fluxo.conferir(fluxo)[0]
    assert not erros, f"descricao-exemplo.json gerou fluxo com erros: {erros}"
    assert not na_empresa(fluxo), "fluxo sem Horário de Expediente não deve imprimir CONFIGURAR NA EMPRESA"
    molde = json.loads((pasta / "exemplo-minimo.json").read_text(encoding="utf-8"))
    assert {tuple(n) for n in fluxo["nodes"]} == {tuple(n) for n in molde["nodes"]}, "campos de topo diferentes do exemplo-minimo.json"
    assert {tuple(c) for c in fluxo["connections"]} == {tuple(c) for c in molde["connections"]}, "campos de ligação diferentes do exemplo"
    assert all(n["style"] == molde["nodes"][0]["style"] for n in fluxo["nodes"]), "estilo diferente do exemplo"
    assert sorted(n["type"] for n in fluxo["nodes"]) == sorted(n["type"] for n in molde["nodes"]), "exemplo-minimo.json não corresponde à descricao-exemplo.json"

    todos = {
        "blocos": [
            {"apelido": "ola", "tipo": "conteudo", "itens": ["Olá", 2, "Tudo bem?"]},
            {"apelido": "nome", "tipo": "pergunta", "mensagem": "Qual é o seu nome?"},
            {"apelido": "v_nome", "tipo": "variavel", "nome": "nome"},
            {"apelido": "limpa", "tipo": "codigo_js", "codigo": "return \"%nome%\".trim() ? \"ok\" : \"vazio\";"},
            {"apelido": "pausa", "tipo": "intervalo", "segundos": 1},
            {"apelido": "v_ok", "tipo": "variavel", "nome": "%nome_ok%"},
            {"apelido": "tem_nome", "tipo": "condicao", "valor": "ok"},
            {"apelido": "marca", "tipo": "tag", "nome": "Lead", "id": 7},
            {"apelido": "perfil", "tipo": "switch", "regras": [{"nome": "VIP", "tag_id": 8}, {"nome": "Novo"}]},
            {"apelido": "menu", "tipo": "menu", "mensagem": "Escolha", "opcoes": ["Comprar", ["Suporte", "Ajuda"]], "resposta_invalida": True, "sem_resposta_minutos": 30},
            {"apelido": "expediente", "tipo": "horario", "nome": "Comercial"},
            {"apelido": "nota", "tipo": "msg_interna", "mensagem": "Lead %nome%"},
            {"apelido": "botoes", "tipo": "marcador", "instrucao": "substituir por Botões"},
            {"apelido": "aviso_email", "tipo": "enviar_email", "assunto": "Novo lead", "mensagem": "Lead %nome%"},
            {"apelido": "comercial", "tipo": "setor", "nome": "Comercial", "id": 3},
            {"apelido": "fim", "tipo": "encerrar", "mensagem": "Até mais"},
        ],
        "ligacoes": [
            ["inicio", "ola"], ["ola", "nome"], ["nome", "v_nome"], ["v_nome", "limpa"], ["limpa", "pausa"], ["pausa", "v_ok"],
            ["v_ok", "tem_nome"], ["tem_nome", "verdadeiro", "marca"], ["tem_nome", "falso", "fim"], ["marca", "perfil"],
            ["perfil", "VIP", "menu"], ["perfil", "Novo", "menu"], ["perfil", "nenhuma", "menu"],
            ["menu", 1, "expediente"], ["menu", "2", "botoes"], ["menu", "invalida", "nota"], ["menu", "sem_resposta", "fim"],
            ["expediente", "dentro", "nota"], ["expediente", "fora", "fim"], ["nota", "aviso_email"], ["botoes", "comercial"],
            ["aviso_email", "enviado", "comercial"], ["aviso_email", "nao_enviado", "comercial"],
        ],
    }
    fluxo, conferir = montar(todos)
    erros, _, trocar, _ = validar_fluxo.conferir(fluxo)
    assert not erros, erros
    assert len(trocar) == 4, trocar  # regra Novo sem tag, Setor do horário sem ID, marcador, e-mail sem conta
    assert len(conferir) == 5 and len({n["id"] for n in fluxo["nodes"]}) == 17, conferir
    email = next(n for n in fluxo["nodes"] if n["type"] == "email")["data"]
    assert email == {"origem": "conta", "contaId": 0, "provedorId": None, "para": "", "assunto": "Novo lead", "corpo": "Lead %nome%"}, email
    assert {n["type"] for n in fluxo["nodes"]} == set(validar_fluxo.NOMES), "algum tipo observado ficou sem gerador"
    assert any("Gerenciamento Por Setor" in aviso for aviso in na_empresa(fluxo)), "fluxo com Horário de Expediente sem o aviso da configuração da empresa"

    def recusa(nome, mudar, trecho):
        d = json.loads(json.dumps(todos))
        mudar(d)
        try:
            montar(d)
        except Invalida as e:
            assert any(trecho in p for p in e.args[0]), f"{nome}: esperava “{trecho}”, veio {e.args[0]}"
        else:
            raise AssertionError(f"{nome}: a descrição deveria ter sido recusada")

    recusa("tipo desconhecido", lambda d: d["blocos"][0].update(tipo="botoes"), "não existe no gerador")
    recusa("apelido repetido", lambda d: d["blocos"][1].update(apelido="ola"), "apelido repetido")
    recusa("campo desconhecido", lambda d: d["blocos"][0].update(texto="x"), "campos desconhecidos")
    recusa("campo faltando", lambda d: d["blocos"][1].pop("mensagem"), "faltam os campos")
    recusa("destino desconhecido", lambda d: d["ligacoes"].append(["ola", "nada"]), "apelido desconhecido: nada")
    recusa("saída inexistente", lambda d: d["ligacoes"].append(["menu", "9", "fim"]), "tem as saídas")
    recusa("saída não informada", lambda d: d["ligacoes"].append(["menu", "fim"]), "escreva [origem, saída, destino]")
    recusa("saída de bloco final", lambda d: d["ligacoes"].append(["fim", "ola"]), "bloco final")
    recusa("condição sem formato", lambda d: d["blocos"][6].update(compara="horario"), "não têm formato observado")
    recusa("intervalo longo", lambda d: d["blocos"][4].update(segundos=300), "Janela expirada")
    recusa("intervalo longo no Conteúdo", lambda d: d["blocos"][0].update(itens=["Olá", 300]), "de 1 a 120 segundos")
    print("Autoteste do gerador: tudo certo (exemplo de assets, fluxo com os 15 tipos e 11 descrições recusadas).")
    return 0


if __name__ == "__main__":
    argumentos = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--teste" in sys.argv:
        sys.exit(autoteste())
    if len(argumentos) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(gerar_arquivo(argumentos[0], argumentos[1], final="--final" in sys.argv))
