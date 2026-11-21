#!/usr/bin/env python3
"""Confere um prompt do GPT Assistant do Chat Master Veloz.

Uso:
  python3 conferir_prompt.py prompt.txt            modo rascunho (padrão)
  python3 conferir_prompt.py --final prompt.txt    modo final, na versão definitiva
  python3 conferir_prompt.py [--final] -           lê o prompt da entrada padrão
  python3 conferir_prompt.py --autoteste           roda o autoteste

Dois modos, porque a skill permite entregar um rascunho com lacunas:
  rascunho  marcador [[...]] vira PENDÊNCIA a preencher e não reprova; o comando
            com marcador no lugar do ID tem a forma conferida do mesmo jeito.
  --final   qualquer marcador reprova.

Ordem de uso: os marcadores de dados do negócio são preenchidos antes de colar;
o prompt pode ir ao painel levando só os marcadores de comando, que se trocam lá,
pela janela COMANDOS DA IA; o --final roda na versão definitiva, depois do
INSERIR NO PROMPT, antes dos testes.

O que confere nos dois modos (referência: references/docs/recursos/comandos-gpt-assistant.md):
  - cada comando #{...} tem a mesma forma dos blocos do artigo
    (#{ colado, aspas retas, pares "chave": "valor") e usa chaves documentadas;
  - os IDs são números entre aspas, como no artigo;
  - não há variável {{...}}, que não está documentada para o campo Prompt;
  - existe no texto a regra dos códigos (precaução desta skill);
  - os blocos "agenda" e "oportunidade" (comandos Marcar ou desmarcar na agenda e
    Registrar oportunidade no CRM), que o artigo cita sem mostrar a forma, são
    reconhecidos e comparados só com a forma observada num painel em 21/11/2026
    (references/comandos-e-capacidades.md, seção 4): nunca viram erro, viram um
    aviso para inserir pela janela, que diz também quando o bloco difere dela.

A documentação só mostra a forma #{"chave": "10"}. Ela não diz que o código é
JSON nem o que acontece com outras formas (espaço depois do #, aspas curvas, ID
sem aspas). As verificações de forma são precaução desta skill: o script acusa o
que difere do artigo, não o que "não funciona".

Sai com código 1 quando há erro; pendências e avisos não mudam o código de saída.
"""
import json
import re
import sys

# Combinações de chaves que o artigo "Comandos GPT Assistant" mostra.
DOCUMENTADAS = {
    ("queueId",): "Transferir para um setor",
    ("queueId", "userId"): "Transferir para um operador",
    ("tagId",): "Marcar com uma tag",
    ("closeTicket",): "Encerrar o atendimento",
}
# Blocos que o mesmo artigo cita pelo nome sem mostrar a forma: o script os reconhece, compara
# com a forma observada e só avisa. Chave: nome do bloco no artigo; valor: nome do comando na janela.
SEM_FORMA = {"agenda": "Marcar ou desmarcar na agenda", "oportunidade": "Registrar oportunidade no CRM"}
# Título que a janela pôs na seção em 21/11/2026; só vale em linha de título, porque em prosa a frase é comum.
TITULO_OBSERVADO = {
    "agenda": re.compile(r"^#+[ \t]*Marcar na agenda[ \t]*$", re.I | re.M),
    "oportunidade": re.compile(r"^#+[ \t]*Registrar a oportunidade no CRM[ \t]*$", re.I | re.M),
}
AVISO_SEM_FORMA = (
    "insira pelo botão INSERIR NO PROMPT da janela COMANDOS DA IA e não edite o bloco à mão; "
    "a Central de Ajuda não mostra a forma dele, então este script só o compara com a forma observada num painel em 21/11/2026. "
    "Se foi digitado ou alterado, apague a seção e insira de novo pela janela; o teste do comando é que mostra se funciona."
)
DIFERE = (
    ' Na(s) linha(s) {linhas} o bloco difere da forma observada, #{{"{chave}": {{...}}}} com aspas retas e todas as chaves fechadas: '
    "é sinal de bloco digitado ou alterado."
)
EFEITO = "A documentação não diz o efeito; corrija para ficar igual ao artigo."
ASPAS_CURVAS = "“”„‟″‶‘’′"
COMANDO = re.compile(r"#\s?\{[^}\n]*\}")
INICIO = re.compile(r"#\s?\{")
MARCADOR = re.compile(r"\[\[[^\]\n]*\]\]")
VARIAVEL = re.compile(r"\{\{[^}\n]*\}\}")
LINHA_EM_BRANCO = re.compile(r"[ \t]*(?:\n|$)")


def fim_do_bloco(texto, inicio):
    """Fim de um bloco aberto em `inicio`: onde as chaves se fecham, ou antes da primeira linha em branco.

    shortcut: a forma dos blocos agenda e oportunidade é só a observada num painel; se a Central mostrar, trocar por ela.
    """
    nivel = 0
    for i in range(inicio, len(texto)):
        if texto[i] == "{":
            nivel += 1
        elif texto[i] == "}":
            nivel -= 1
            if nivel == 0:
                return i + 1
        elif texto[i] == "\n" and LINHA_EM_BRANCO.match(texto, i + 1):
            return i
    return len(texto)


def conferir(texto, final=False):
    """Devolve (erros, pendencias, avisos, resumo), cada um uma lista de frases."""
    erros, pendencias, avisos, resumo = [], [], [], []
    falta = erros if final else pendencias  # onde vai o marcador por preencher
    linha_de = lambda pos: texto.count("\n", 0, pos) + 1

    # Blocos agenda e oportunidade: reconhecidos pelo nome dentro do bloco, pelo nome do comando
    # ou pelo título que a janela põe na seção. São apagados (com as quebras de linha mantidas)
    # antes das outras conferências, para a forma não documentada não virar erro.
    achados = {chave: set() for chave in SEM_FORMA}
    diferem = {chave: set() for chave in SEM_FORMA}
    partes, pos = [], 0
    for m in INICIO.finditer(texto):
        if m.start() < pos:
            continue
        fim = fim_do_bloco(texto, m.start())
        bloco = texto[m.start():fim]
        chave = next((c for c in SEM_FORMA if re.search(c[:6], bloco, re.I)), None)  # "agenda", "agendar"...
        if chave is None:
            continue
        achados[chave].add(linha_de(m.start()))
        try:
            igual = isinstance(json.loads(MARCADOR.sub("0", bloco[bloco.index("{"):])).get(chave), dict)
        except ValueError:
            igual = False
        if not igual:
            diferem[chave].add(linha_de(m.start()))
        for mk in MARCADOR.finditer(bloco):
            falta.append(f"linha {linha_de(m.start() + mk.start())}: preencher {mk.group(0)}")
        partes += [texto[pos:m.start()], re.sub(r"[^\n]", " ", bloco)]
        pos = fim
    mascarado = "".join(partes) + texto[pos:]
    fora_de_marcador = MARCADOR.sub(lambda m: " " * len(m.group(0)), texto)  # o marcador do rascunho não conta
    for chave, nome in SEM_FORMA.items():
        achados[chave].update(linha_de(m.start()) for m in re.finditer(re.escape(nome), fora_de_marcador, re.I))
        achados[chave].update(linha_de(m.start()) for m in TITULO_OBSERVADO[chave].finditer(fora_de_marcador))
        if achados[chave]:
            junta = lambda numeros: ", ".join(map(str, sorted(numeros)))
            difere = DIFERE.format(linhas=junta(diferem[chave]), chave=chave) if diferem[chave] else ""
            avisos.append(f"linha(s) {junta(achados[chave])}: comando {nome} (bloco \"{chave}\") -> {AVISO_SEM_FORMA}{difere}")

    for m in COMANDO.finditer(mascarado):
        bruto, linha = m.group(0), linha_de(m.start())
        corpo = bruto[bruto.index("{"):]
        if not any(c in corpo for c in '"' + ASPAS_CURVAS):
            continue  # menção em prosa, como "começam com #{ e terminam com }"
        onde = f"linha {linha}: {bruto}"
        antes = len(erros)
        if not bruto.startswith("#{"):
            erros.append(f"{onde} -> há espaço entre # e {{: difere do artigo de comandos, que mostra #{{ colado. {EFEITO}")
        if any(c in corpo for c in ASPAS_CURVAS):
            erros.append(f"{onde} -> aspas curvas: difere dos blocos de código do artigo de comandos, que usam aspas retas (\"). {EFEITO}")
            continue
        com_marcador = bool(MARCADOR.search(corpo))
        try:
            # json.loads é só o jeito prático de comparar com a forma do artigo;
            # a documentação não diz que o código é JSON. O marcador vira "0"
            # para a forma ser conferida mesmo antes de o ID existir.
            dados = json.loads(MARCADOR.sub("0", corpo))
        except ValueError:
            erros.append(f"{onde} -> difere da forma mostrada no artigo de comandos, #{{\"chave\": \"10\"}}. {EFEITO}")
            continue
        chaves = tuple(sorted(dados))
        nome = DOCUMENTADAS.get(chaves)
        if nome is None:
            avisos.append(
                f"{onde} -> chave(s) {', '.join(chaves) or '(nenhuma)'} fora do artigo Comandos GPT Assistant. "
                "Se veio da janela COMANDOS DA IA do painel, mantenha como o painel inseriu; se foi digitado, remova "
                "e insira o comando pela janela."
            )
            continue
        for chave, valor in dados.items():
            if not (isinstance(valor, str) and valor.isdigit()):
                erros.append(f"{onde} -> o valor de {chave} difere do artigo de comandos, que mostra um número entre aspas, como \"10\". {EFEITO}")
        if chaves == ("closeTicket",) and dados["closeTicket"] != "1":
            avisos.append(f"{onde} -> o artigo mostra closeTicket com o valor \"1\".")
        if com_marcador:
            falta.append(f"{onde} -> trocar o marcador pelo ID real ({nome}).")
        if len(erros) == antes:
            resumo.append(f"linha {linha}: {nome} {bruto}" + (" (ID pendente)" if com_marcador else ""))

    for m in re.finditer(r"#\s?\{[^}\n]*$", mascarado, re.M):
        erros.append(
            f"linha {linha_de(m.start())}: comando aberto com #{{ e não fechado com }} na mesma linha: "
            f"difere da forma do artigo de comandos. {EFEITO}"
        )

    # Marcadores fora dos comandos; o texto mantém as quebras para a linha sair certa.
    sem_comandos = COMANDO.sub(lambda m: " " * len(m.group(0)), mascarado)
    for m in MARCADOR.finditer(sem_comandos):
        falta.append(f"linha {linha_de(m.start())}: preencher {m.group(0)}")
    for m in VARIAVEL.finditer(mascarado):
        avisos.append(
            f"linha {linha_de(m.start())}: {m.group(0)} -> a documentação não descreve variáveis para o campo Prompt."
        )
    if (COMANDO.search(mascarado) or mascarado != texto) and not re.search(r"c[óo]digo", texto, re.I):
        avisos.append(
            "o prompt tem comandos, mas não achei a regra dos códigos (precaução desta skill: "
            "incluir o código só na situação da instrução, sem alterar nenhum caractere)."
        )
    return erros, pendencias, avisos, resumo


def relatorio(texto, final=False):
    erros, pendencias, avisos, resumo = conferir(texto, final)
    print(f"Modo: {'final' if final else 'rascunho'}.")
    print(f"Tamanho do prompt: {len(texto)} caracteres, {len(texto.split())} palavras.")
    print(f"Comandos com a forma do artigo: {len(resumo)}")
    for item in resumo:
        print(f"  - {item}")
    for titulo, itens in (("ERROS", erros), ("PENDÊNCIAS A PREENCHER", pendencias), ("AVISOS", avisos)):
        if itens:
            print(f"\n{titulo} ({len(itens)}):")
            for item in itens:
                print(f"  - {item}")
    if erros:
        print("\nHá diferenças em relação à forma do artigo de comandos" + (" ou marcadores por trocar" if final else "") + ": corrija antes de " + ("testar." if final else "colar no painel."))
    elif pendencias:
        print(
            f"\nRascunho conferido: {len(pendencias)} pendência(s) a preencher. Preencha os dados do negócio antes de colar no painel; "
            "marcador de comando pode ir ao painel e ser trocado pela janela COMANDOS DA IA. "
            "Rode com --final na versão definitiva, depois do INSERIR NO PROMPT, antes dos testes."
        )
    elif not final:
        print("\nSem erros e sem pendências: o resultado é o mesmo do modo --final. Falta o teste: o script não prova que os IDs existem.")
    else:
        print("\nVersão definitiva conferida" + (" (leia os avisos)" if avisos else "") + ". Falta o teste: o script não prova que os IDs existem.")
    return 1 if erros else 0


def autoteste():
    bom = (
        'REGRA: mantenha o código. Diga: Transferindo para o #{"queueId": "544"} Suporte.\n'
        'Diga: Transferindo para o #{"queueId": "544", "userId":"3"} João.\n'
        'Diga: temos #{"tagId": "71"} Notebook.\n'
        'Diga: encerrando #{"closeTicket": "1"} agora.\n'
        'Os trechos que começam com #{ e terminam com } são códigos.\n'
    )
    for final in (False, True):
        erros, pendencias, avisos, resumo = conferir(bom, final)
        assert not erros and not pendencias and not avisos and len(resumo) == 4, (final, erros, pendencias, avisos)

    # Rascunho: marcador é pendência, e a forma do comando com marcador é conferida.
    rascunho = 'código. Você é [[NOME_DA_IA]]. Diga: indo para o #{"queueId": "[[ID_DO_SETOR]]"} setor.'
    erros, pendencias, _, resumo = conferir(rascunho)
    assert not erros and len(pendencias) == 2 and len(resumo) == 1, (erros, pendencias, resumo)
    erros, pendencias, _, _ = conferir(rascunho, final=True)
    assert len(erros) == 2 and not pendencias, (erros, pendencias)
    # Forma errada reprova mesmo no rascunho, com marcador ou sem.
    assert conferir('código: #{“queueId”: “[[ID_DO_SETOR]]”}')[0]
    assert conferir('código: #{"queueId" "[[ID_DO_SETOR]]"}')[0]

    casos_de_erro = {
        "aspas curvas": "código: #{“queueId”: “544”}",
        "ID não numérico": 'código: #{"tagId": "abc"}',
        "ID sem aspas": 'código: #{"tagId": 71}',
        "forma diferente": 'código: #{"tagId" "71"}',
        "espaço depois do #": 'código: # {"tagId": "71"}',
        "comando não fechado": 'código: #{"tagId": "71"',
    }
    for nome, texto in casos_de_erro.items():
        for final in (False, True):
            erros, _, _, resumo = conferir(texto, final)
            assert erros and not resumo, f"deveria acusar erro e não contar o comando: {nome}"

    casos_de_aviso = {
        "chave desconhecida": 'código: #{"priority": "1"}',
        "removeTag, que saiu do artigo": 'código: #{"removeTag": "71"}',
        "variável": "Olá, {{name}}.",
        "sem regra do código": 'Diga: #{"tagId": "71"} ok.',
        "closeTicket diferente de 1": 'código: #{"closeTicket": "2"}',
    }
    for nome, texto in casos_de_aviso.items():
        erros, pendencias, avisos, _ = conferir(texto, final=True)
        assert avisos and not erros and not pendencias, f"deveria só avisar: {nome} {erros} {avisos}"

    # Blocos agenda e oportunidade: a forma não está na Central. Qualquer forma (uma linha,
    # aninhada, várias linhas, aspas curvas) é reconhecida, nunca vira erro e sempre avisa.
    # O aviso diz "difere" quando o bloco não bate com a forma observada num painel em 21/11/2026
    # (os dois primeiros textos de cada lista são seções inseridas pela janela, com ids e nomes trocados).
    seco = lambda frase: "COMANDOS DA IA" in frase and "não edite" in frase and "Central de Ajuda não mostra" in frase
    sem_forma = {
        "agenda": [
            (False, '## Marcar na agenda\n\nQuando o cliente já tiver confirmado o dia e a hora, responda incluindo o bloco abaixo:\n\n'
                    '#{"agenda": {"acao": "marcar", "titulo": "<assunto>", "data": "<AAAA-MM-DD>", "hora": "<HH:MM>", "duracao": 30, "tipo": "reuniao"}}\n\n'
                    'Para CANCELAR o compromisso já marcado, use:\n\n#{"agenda": {"acao": "desmarcar"}}\n\nSe o horário já estiver ocupado, o sistema recusa.'),
            (False, '## Marcar na agenda\n\nQuando o cliente confirmar, responda incluindo o bloco abaixo:'),
            (False, 'código: #{"agenda": {"data": "25/12/2026", "hora": "14:00", "tipo": "Visita"}}'),
            (True, 'código: #{"agenda": "1"}'),
            (True, 'código: #{“agendar”: “1”}'),
            (True, 'código: #{"agenda": {"acao": "marcar", "titulo": "<assunto>"}'),
            (False, '### Marcar ou desmarcar na agenda\nQuando o cliente confirmar, responda incluindo o bloco abaixo:\n(bloco)'),
        ],
        "oportunidade": [
            (False, '## Registrar a oportunidade no CRM\n\nQuando o cliente demonstrar interesse, inclua na sua resposta o bloco abaixo,\nexatamente neste formato:\n\n'
                    '#{"oportunidade": {"productId": 7, "valor": "<valor combinado, ex: 1200,00>", "pipelineId": 5, "laneId": 9, '
                    '"resumo": "<uma frase com o que o cliente quer>", "respostas": {"Necessidade": "<resposta do cliente>", "Prazo": "<resposta do cliente>"}}, "queueId": "6"}\n\n'
                    'Use productId 7 (Plano Exemplo) só se for esse o produto.\nDepois de registrar, o atendimento vai para Comercial.'),
            (False, '## Registrar a oportunidade no CRM\n\nQuando o cliente pedir orçamento, inclua o bloco abaixo:'),
            (True, 'código: #{"oportunidade": "1"}'),
            (True, 'código:\n#{\n  "acao": "oportunidade",\n  "valor": {"total": "0"}\n}\nDepois siga.'),
            (False, '### Registrar oportunidade no CRM\nQuando o cliente pedir orçamento, responda incluindo o bloco abaixo:'),
        ],
    }
    for chave, textos in sem_forma.items():
        for difere, texto in textos:
            for final in (False, True):
                erros, pendencias, avisos, resumo = conferir(texto, final)
                assert not erros and not pendencias and not resumo, (texto, erros, pendencias)
                dele = [frase for frase in avisos if seco(frase)]  # a seção inteira da janela traz também o aviso da regra dos códigos
                assert len(dele) == 1 and f'"{chave}"' in dele[0] and len(avisos) <= 2, (texto, avisos)
                assert ("difere da forma observada" in dele[0]) == difere, (texto, avisos)
    # Em prosa, a frase do título observado não é o comando.
    assert not conferir("Você não enxerga a agenda. Não diga que vai marcar na agenda nem registrar a oportunidade no CRM.")[2]
    # Junto com os comandos documentados: os quatro continuam contados, e um erro fora do bloco continua erro.
    erros, _, avisos, resumo = conferir(bom + '\n#{"agenda": {"data": "x"}}\nDiga: #{"tagId": "abc"}', final=True)
    assert len(resumo) == 4 and len(erros) == 1 and "tagId" in erros[0] and len(avisos) == 1, (erros, avisos, resumo)
    # O marcador do rascunho que só cita o nome do comando não gera o aviso.
    erros, pendencias, avisos, _ = conferir("código. [[OPCIONAL: Registrar oportunidade no CRM, pela janela]]")
    assert not erros and len(pendencias) == 1 and not avisos, (erros, pendencias, avisos)
    # Marcador dentro do bloco continua contando: pendência no rascunho, erro no --final.
    assert len(conferir('código: #{"agenda": "[[DATA]]"}')[1]) == 1
    assert len(conferir('código: #{"agenda": "[[DATA]]"}', final=True)[0]) == 1
    print("Autoteste: tudo certo.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--final"]
    if len(args) != 1:
        sys.exit(__doc__)
    if args[0] == "--autoteste":
        autoteste()
    else:
        try:
            origem = sys.stdin if args[0] == "-" else open(args[0], encoding="utf-8")
        except OSError as erro:
            sys.exit(f"Não consegui abrir o arquivo do prompt: {erro}")
        with origem:
            sys.exit(relatorio(origem.read(), final="--final" in sys.argv))
