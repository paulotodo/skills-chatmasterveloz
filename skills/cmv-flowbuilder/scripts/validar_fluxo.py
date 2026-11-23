#!/usr/bin/env python3
"""Confere a estrutura de um fluxo do FlowBuilder (.json exportado ou gerado) antes de importar.

Uso:
  python3 validar_fluxo.py fluxo.json           lista erros, avisos e valores a trocar
  python3 validar_fluxo.py fluxo.json --final   valores a trocar também contam como erro
  python3 validar_fluxo.py --teste              autoteste

Código de saída: 0 sem erros, 1 com erros, 2 quando o arquivo não pôde ser lido.

O formato conferido é o observado em um arquivo exportado (references/formato-json.md), não um
formato oficial. Por isso, tipo de bloco que não foi observado vira aviso, e não erro.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

MARCADOR = "TROCAR"  # qualquer texto do fluxo com esta palavra é um valor a trocar
NOMES = {
    "start": "Início", "singleBlock": "Conteúdo", "menu": "Menu", "question": "Pergunta",
    "variable": "Variável", "condition": "Condição", "switch": "Switch (tags)", "tag": "Tag",
    "interval": "Intervalo", "internal": "Msg Interna", "wbh": "Execução de Código JS",
    "away": "Horário de Expediente", "queue": "Setor", "close": "Encerrar", "email": "Enviar e-mail",
}
UMA_SAIDA = {"start", "singleBlock", "tag", "variable", "interval", "internal", "wbh", "question"}
ESPERAM = {"menu", "question"}  # blocos observados que esperam a resposta do cliente
FONTES_DE_VARIAVEL = {"question", "menu", "wbh", "start"}
ITENS_CONTEUDO = {"message", "interval", "img"}
CONDICOES_VISTAS = {(1, 1), (2, 3), (12, 11)}  # pares (key, condition) do arquivo observado
LIMITES_LISTA = {"listButtonText": 20, "listHeaderText": 60, "listFooterText": 60, "message": 1024}


def minutos_sem_resposta(dados):
    sem = dados.get("semResposta")
    valor = sem.get("minutos") if isinstance(sem, dict) else None
    return valor if isinstance(valor, (int, float)) and valor > 0 else 0


def saidas(no):
    """Saídas que o bloco tem, pelo tipo e pelos dados: {handle: rótulo}. None = tipo não observado."""
    tipo, dados = no.get("type"), no.get("data") or {}
    if tipo == "interval" and str(dados.get("sec", "")).isdigit() and int(dados["sec"]) > 120:
        return None  # mais de 2 minutos: ganha a saída Janela expirada, sem formato observado
    if tipo in UMA_SAIDA:
        return {"a": "saída"}
    if tipo in ("queue", "close"):
        return {}
    if tipo == "condition":
        return {"a": "saída a (hipótese: Verdadeiro)", "b": "saída b (hipótese: Falso)"}
    if tipo == "away":
        return {"a": "saída a", "b": "saída b"}
    if tipo == "email":
        return {"a": "Enviado", "b": "Não enviado"}
    if tipo == "menu":
        s = {f"a{o.get('number')}": f"opção {o.get('number')}" for o in dados.get("arrayOption") or []}
        if dados.get("enableElse"):
            s["else"] = "Resposta inválida"
        if minutos_sem_resposta(dados):
            s["semResposta"] = "Sem resposta"
        return s
    if tipo == "switch":
        s = {f"regra-{r.get('id')}": f"regra “{r.get('label')}”" for r in dados.get("rules") or []}
        s["fallback"] = "Nenhuma condição atendida"
        return s
    return None


def trecho(no):
    dados = no.get("data") or {}
    texto = dados.get("message") or dados.get("secName") or dados.get("assunto") or ""
    if no.get("type") == "singleBlock":
        texto = next((e.get("value", "") for e in dados.get("elements") or [] if e.get("type") == "message"), "")
    texto = " ".join(str(texto).split())
    return f" “{texto[:40]}{'…' if len(texto) > 40 else ''}”" if texto else ""


def rotulo(no):
    return f"{NOMES.get(no.get('type'), no.get('type'))}{trecho(no)} [id {no.get('id')}]"


def textos(valor, caminho=""):
    """Todos os textos dentro de data, com o caminho de cada um."""
    if isinstance(valor, str):
        yield caminho, valor
    elif isinstance(valor, dict):
        for chave, v in valor.items():
            yield from textos(v, f"{caminho}.{chave}" if caminho else chave)
    elif isinstance(valor, list):
        for i, v in enumerate(valor):
            yield from textos(v, f"{caminho}[{i}]")


def conferir_dados(no, erros, avisos, trocar):
    tipo, dados, nome = no["type"], no["data"], rotulo(no)
    for caminho, texto in textos(dados):
        if MARCADOR in texto:
            trocar.append(f"{nome}: campo {caminho} = “{texto[:60]}”")
    if tipo in ("tag", "queue", "away"):
        sec = dados.get("sec")
        sem_id = not (isinstance(sec, int) and not isinstance(sec, bool) and sec > 0)
        if sem_id and MARCADOR not in str(dados.get("secName", "")):  # com marcador, o bloco já foi listado
            trocar.append(f"{nome}: campo sec = {sec!r} (falta o ID da conta; no arquivo observado é um número inteiro)")
    elif tipo == "email":
        conta = dados.get("contaId")
        if dados.get("origem") == "conta" and not (isinstance(conta, int) and not isinstance(conta, bool) and conta > 0):
            trocar.append(f"{nome}: campo contaId = {conta!r} (falta a conta de e-mail; abra o bloco e escolha em Enviar por)")
    elif tipo == "singleBlock":
        itens = dados.get("elements") or []
        if not itens:
            erros.append(f"{nome}: bloco Conteúdo sem nenhum item.")
        numeros = [e.get("number") for e in itens]
        if sorted(map(str, numeros)) != sorted(map(str, dados.get("seq") or [])):
            erros.append(f"{nome}: a lista seq não tem os mesmos itens de elements (campo number).")
        for e in itens:
            if e.get("type") not in ITENS_CONTEUDO:
                avisos.append(f"{nome}: item do tipo “{e.get('type')}” não foi observado; confira no editor.")
            elif e.get("type") == "interval" and not str(e.get("value", "")).isdigit():
                erros.append(f"{nome}: intervalo com valor “{e.get('value')}”; o esperado é um número de segundos.")
            elif e.get("type") == "message" and not str(e.get("value", "")).strip():
                avisos.append(f"{nome}: item de texto vazio.")
    elif tipo == "interval":
        seg = str(dados.get("sec", ""))
        if not seg.isdigit():
            erros.append(f"{nome}: Intervalo de “{seg}” segundos; o esperado é um número de segundos.")
        elif int(seg) > 120:
            avisos.append(f"{nome}: Intervalo de {seg} segundos; com mais de 2 minutos o bloco ganha a saída Janela expirada, que não foi observada no arquivo: as saídas dele não foram conferidas, confira no editor se a Janela expirada está ligada.")
    elif tipo == "variable":
        if not re.fullmatch(r"%[^%\s]+%", str(dados.get("message", ""))):
            erros.append(f"{nome}: o nome da variável precisa vir entre porcentagens e sem espaços, como %nome%.")
    elif tipo == "condition":
        par = (dados.get("key"), dados.get("condition"))
        if par not in CONDICOES_VISTAS:
            avisos.append(f"{nome}: combinação key={par[0]}, condition={par[1]} não foi observada; abra o bloco no editor e confira Tipo, Condição e Valor.")
    elif tipo == "menu":
        opcoes = dados.get("arrayOption") or []
        if not opcoes:
            erros.append(f"{nome}: menu sem opções.")
        numeros = [o.get("number") for o in opcoes]
        if len(set(numeros)) != len(numeros):
            erros.append(f"{nome}: opções com número repetido.")
        elif numeros != list(range(1, len(numeros) + 1)):
            avisos.append(f"{nome}: as opções não estão numeradas de 1 a {len(numeros)} em ordem.")
        if dados.get("menuType") == "list":
            for o in opcoes:
                if len(str(o.get("value", ""))) > 20:
                    erros.append(f"{nome}: opção {o.get('number')} tem mais de 20 caracteres (limite do Menu em Lista).")
                if len(str(o.get("description", ""))) > 72:
                    erros.append(f"{nome}: descrição da opção {o.get('number')} tem mais de 72 caracteres.")
            for campo, limite in LIMITES_LISTA.items():
                if len(str(dados.get(campo, ""))) > limite:
                    erros.append(f"{nome}: campo {campo} passa de {limite} caracteres.")
        else:
            avisos.append(f"{nome}: menuType “{dados.get('menuType')}” não foi observado (só “list”); confira o Tipo de Menu no editor.")
        if not minutos_sem_resposta(dados):
            avisos.append(f"{nome}: menu sem “Sem resposta”; quem não responder deixa o fluxo esperando.")
    elif tipo == "switch":
        regras = dados.get("rules") or []
        ids = [r.get("id") for r in regras]
        if len(set(ids)) != len(ids):
            erros.append(f"{nome}: regras com id repetido.")
        for r in regras:
            if r.get("operator") != "possui":
                avisos.append(f"{nome}: operador “{r.get('operator')}” não foi observado (só “possui”); confira a Comparação no editor.")
            tags = r.get("tagIds") or []
            if not tags:
                avisos.append(f"{nome}: regra “{r.get('label')}” sem tag; ela nunca é atendida.")
            elif not all(isinstance(t, int) and t > 0 for t in tags):
                trocar.append(f"{nome}: regra “{r.get('label')}” com tagIds = {tags!r} (falta o ID da tag)")


def ciclo_sem_espera(nos, vizinhos):
    """Um bloco de um ciclo em que nenhum bloco espera o cliente, ou None."""
    livres = {i for i, n in nos.items() if n["type"] in NOMES and n["type"] not in ESPERAM}
    cor = {}
    for inicio in livres:
        if inicio in cor:
            continue
        pilha = [(inicio, iter(vizinhos[inicio]))]
        cor[inicio] = 1
        while pilha:
            atual, resto = pilha[-1]
            proximo = next((v for v in resto if v in livres), None)
            if proximo is None:
                cor[atual] = 2
                pilha.pop()
            elif cor.get(proximo) == 1:
                return proximo
            elif proximo not in cor:
                cor[proximo] = 1
                pilha.append((proximo, iter(vizinhos[proximo])))
    return None


def conferir(fluxo, final=False):
    """Devolve (erros, avisos, trocar, resumo). Com final=True, valores a trocar viram erros."""
    erros, avisos, trocar = [], [], []
    if not isinstance(fluxo, dict) or not isinstance(fluxo.get("nodes"), list) or not isinstance(fluxo.get("connections"), list):
        return ["O arquivo precisa ser um objeto com as listas “nodes” e “connections”."], avisos, trocar, ""
    nos = {}
    for posicao, no in enumerate(fluxo["nodes"]):
        if not isinstance(no, dict) or not isinstance(no.get("id"), str) or not isinstance(no.get("type"), str) or not isinstance(no.get("data"), dict):
            erros.append(f"Bloco na posição {posicao} da lista nodes sem id, type ou data válidos.")
            continue
        if no["id"] in nos:
            erros.append(f"ID de bloco repetido: {no['id']}.")
            continue
        nos[no["id"]] = no
        pos = no.get("position")
        if not (isinstance(pos, dict) and all(isinstance(pos.get(k), (int, float)) for k in "xy")):
            erros.append(f"{rotulo(no)}: falta position com x e y numéricos.")
        if no["type"] in NOMES:
            conferir_dados(no, erros, avisos, trocar)
    tipos = Counter(n["type"] for n in nos.values())
    desconhecidos = sorted(t for t in tipos if t not in NOMES)
    for t in desconhecidos:
        avisos.append(f"Tipo de bloco “{t}” ({tipos[t]}) não foi observado: as saídas e os dados dele não foram conferidos.")
    inicios = [i for i, n in nos.items() if n["type"] == "start"]
    if len(inicios) != 1:
        erros.append(f"O fluxo precisa de exatamente um bloco Início (type start); este tem {len(inicios)}.")

    vizinhos, entradas, usadas = defaultdict(list), defaultdict(list), defaultdict(list)
    ids_ligacao, fora_do_padrao = Counter(), 0
    for posicao, c in enumerate(fluxo["connections"]):
        if not isinstance(c, dict):
            erros.append(f"Ligação na posição {posicao} não é um objeto.")
            continue
        origem, destino, handle = c.get("source"), c.get("target"), c.get("sourceHandle")
        ids_ligacao[c.get("id")] += 1
        if c.get("id") != f"reactflow__edge-{origem}{handle or ''}-{destino}{c.get('targetHandle') or ''}":
            fora_do_padrao += 1
        if origem not in nos or destino not in nos:
            falta = origem if origem not in nos else destino
            erros.append(f"Ligação {c.get('id')} aponta para um bloco que não existe: {falta}.")
            continue
        vizinhos[origem].append(destino)
        entradas[destino].append(origem)
        usadas[origem].append(handle)
        if nos[destino]["type"] == "start":
            avisos.append(f"Ligação chegando ao Início a partir de {rotulo(nos[origem])}: isso não foi observado.")
        previstas = saidas(nos[origem])
        if previstas is None or handle in previstas:
            continue
        if not previstas:
            erros.append(f"{rotulo(nos[origem])}: este bloco não tem saída, mas há uma ligação saindo dele.")
        elif nos[origem]["type"] == "question":
            avisos.append(f"{rotulo(nos[origem])}: saída “{handle}” não foi observada na Pergunta; confira no editor.")
        else:
            erros.append(f"{rotulo(nos[origem])}: a saída “{handle}” não existe neste bloco (saídas: {', '.join(previstas)}).")
    for ident, vezes in ids_ligacao.items():
        if vezes > 1:
            erros.append(f"ID de ligação repetido: {ident}.")
    if fora_do_padrao:
        avisos.append(f"{fora_do_padrao} ligação(ões) com id fora do padrão reactflow__edge-<origem><saída>-<destino>.")

    for ident, no in nos.items():
        previstas = saidas(no)
        for handle, nome in (previstas or {}).items():
            vezes = usadas[ident].count(handle)
            if vezes == 0:
                erros.append(f"{rotulo(no)}: {nome} (“{handle}”) sem ligação; o cliente que cair aqui fica sem resposta.")
            elif vezes > 1:
                avisos.append(f"{rotulo(no)}: {vezes} ligações saindo da mesma saída “{handle}”.")
        if no["type"] == "variable":
            fila, vistos = list(entradas[ident]), set()
            while fila:
                anterior = fila.pop()
                if anterior in vistos:
                    continue
                vistos.add(anterior)
                tipo = nos[anterior]["type"]
                if tipo == "interval":
                    fila.extend(entradas[anterior])
                elif tipo in NOMES and tipo not in FONTES_DE_VARIAVEL:
                    avisos.append(f"{rotulo(no)}: vem depois de {NOMES[tipo]}; a Variável precisa vir logo depois da fonte do dado (Pergunta, Menu, Execução de Código JS ou Início), só com Intervalo no meio.")

    if len(inicios) == 1:
        alcancados, fila = {inicios[0]}, [inicios[0]]
        while fila:
            for v in vizinhos[fila.pop()]:
                if v not in alcancados:
                    alcancados.add(v)
                    fila.append(v)
        for ident, no in nos.items():
            if ident not in alcancados:
                if desconhecidos:  # um bloco não observado, como o Pular para, pode chegar até aqui sem ligação
                    avisos.append(f"{rotulo(no)}: nenhuma ligação chega a este bloco a partir do Início.")
                else:
                    erros.append(f"{rotulo(no)}: bloco não alcançável a partir do Início.")
    preso = ciclo_sem_espera(nos, vizinhos)
    if preso:
        erros.append(f"Ciclo sem espera passando por {rotulo(nos[preso])}: o caminho volta ao mesmo bloco sem Menu nem Pergunta no meio, e o fluxo é interrompido.")
    if any(e.get("type") == "img" for n in nos.values() if n["type"] == "singleBlock" for e in n["data"].get("elements") or []):
        avisos.append("Há itens de imagem: o JSON guarda só o nome do arquivo. Confira no editor se as imagens aparecem depois de importar.")
    if final:
        erros.extend(f"Valor a trocar ainda presente: {t}" for t in trocar)
    resumo = f"Blocos: {len(nos)} | Ligações: {len(fluxo['connections'])} | " + ", ".join(f"{NOMES.get(t, t)} {q}" for t, q in tipos.most_common())
    return erros, avisos, trocar, resumo


def validar_arquivo(caminho, final=False):
    try:
        fluxo = json.loads(Path(caminho).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as e:
        print(f"Não foi possível ler {caminho}: {e}")
        return 2
    try:
        erros, avisos, trocar, resumo = conferir(fluxo, final)
    except (AttributeError, TypeError, KeyError) as e:  # campo com formato diferente do observado
        print(f"Fluxo: {caminho}\nEstrutura inesperada em algum bloco ({type(e).__name__}: {e}). Compare com references/formato-json.md.")
        return 1
    print(f"Fluxo: {caminho}\n{resumo}")
    for titulo, itens in (("ERROS", erros), ("AVISOS", avisos), ("VALORES A TROCAR", [] if final else trocar)):
        if itens:
            print(f"\n{titulo} ({len(itens)})")
            for item in itens:
                print(f"  - {item}")
    if erros:
        print(f"\nResultado: REPROVADO, com {len(erros)} erro(s). Corrija antes de importar.")
        return 1
    pendente = f" Há {len(trocar)} valor(es) a trocar: liste-os para quem vai importar." if trocar else ""
    print(f"\nResultado: estrutura sem erros, com {len(avisos)} aviso(s).{pendente}")
    print("Depois de importar, use Verificar e Resumo do fluxo no editor e teste antes de ligar o fluxo a uma conexão.")
    return 0


def autoteste():
    def no(ident, tipo, **dados):
        return {"id": ident, "type": tipo, "position": {"x": 0, "y": 0}, "data": dados}

    def lig(origem, handle, destino):
        return {"id": f"reactflow__edge-{origem}{handle}-{destino}", "source": origem, "sourceHandle": handle, "target": destino, "targetHandle": None}

    def base():
        opcoes = [{"number": 1, "value": "Vendas", "description": ""}, {"number": 2, "value": "Sair", "description": ""}]
        return {
            "nodes": [
                no("1", "start", label="Início"),
                no("msg", "singleBlock", seq=["message0"], elements=[{"type": "message", "value": "Olá", "number": "message0"}]),
                no("menu", "menu", message="Escolha", arrayOption=opcoes, menuType="list", listButtonText="Ver opções", enableElse=False, semResposta={"minutos": 30}),
                no("setor", "queue", sec=7, secName="Vendas"),
                no("fim", "close", message="Até mais", arrayOption=[]),
            ],
            "connections": [lig("1", "a", "msg"), lig("msg", "a", "menu"), lig("menu", "a1", "setor"), lig("menu", "a2", "fim"), lig("menu", "semResposta", "fim")],
        }

    def espera(nome, mudar, trecho_do_erro, final=False):
        fluxo = base()
        mudar(fluxo)
        erros = conferir(fluxo, final)[0]
        assert any(trecho_do_erro in e for e in erros), f"{nome}: esperava erro com “{trecho_do_erro}”, veio {erros}"

    erros, avisos, trocar, _ = conferir(base())
    assert not erros and not avisos and not trocar, (erros, avisos, trocar)
    espera("dois inícios", lambda f: f["nodes"].append(no("2", "start")), "exatamente um bloco Início")
    espera("id repetido", lambda f: f["nodes"].append(no("msg", "close", message="")), "ID de bloco repetido")
    espera("destino inexistente", lambda f: f["connections"].append(lig("msg", "a", "nada")), "não existe: nada")
    espera("saída inexistente", lambda f: f["connections"].append(lig("menu", "a9", "fim")), "a saída “a9” não existe")
    espera("saída sem ligação", lambda f: f["connections"].pop(3), "opção 2 (“a2”) sem ligação")
    espera("bloco solto", lambda f: f["nodes"].append(no("solto", "close", message="")), "não alcançável")
    espera("saída em bloco final", lambda f: f["connections"].append(lig("setor", "a", "fim")), "não tem saída")
    espera("opção longa", lambda f: f["nodes"][2]["data"]["arrayOption"][0].update(value="x" * 21), "mais de 20 caracteres")
    espera("marcador no modo final", lambda f: f["nodes"][3]["data"].update(sec=0, secName="TROCAR: Setor Vendas"), "Valor a trocar", final=True)

    def laco(f):
        f["nodes"] += [no("t1", "tag", sec=3, secName="A"), no("t2", "tag", sec=4, secName="B")]
        f["connections"][3] = lig("menu", "a2", "t1")
        f["connections"] += [lig("t1", "a", "t2"), lig("t2", "a", "t1")]
    espera("ciclo sem espera", laco, "Ciclo sem espera")

    fluxo = base()
    fluxo["nodes"][3]["data"].update(sec=0, secName="TROCAR: Setor Vendas")
    erros, _, trocar, _ = conferir(fluxo)
    assert not erros and len(trocar) == 1, (erros, trocar)
    fluxo = base()
    fluxo["nodes"].append(no("pulo", "tipoNovo"))
    fluxo["connections"][3] = lig("menu", "a2", "pulo")
    erros, avisos, _, _ = conferir(fluxo)
    assert not erros and any("não foi observado" in a for a in avisos), (erros, avisos)
    fluxo = base()
    fluxo["nodes"].append(no("espera", "interval", sec="300"))
    fluxo["connections"][3] = lig("menu", "a2", "espera")
    fluxo["connections"] += [lig("espera", "a", "fim"), lig("espera", "janela", "fim")]
    erros, avisos, _, _ = conferir(fluxo)
    assert not erros and any("Janela expirada" in a for a in avisos), (erros, avisos)

    exemplo = Path(__file__).resolve().parent.parent / "assets" / "exemplo-minimo.json"
    if exemplo.exists():
        erros = conferir(json.loads(exemplo.read_text(encoding="utf-8")))[0]
        assert not erros, f"assets/exemplo-minimo.json com erros: {erros}"
    print("Autoteste: tudo certo (14 verificações" + (", mais o exemplo de assets" if exemplo.exists() else "") + ").")
    return 0


if __name__ == "__main__":
    argumentos = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--teste" in sys.argv:
        sys.exit(autoteste())
    if len(argumentos) != 1:
        print(__doc__)
        sys.exit(2)
    sys.exit(validar_arquivo(argumentos[0], final="--final" in sys.argv))
