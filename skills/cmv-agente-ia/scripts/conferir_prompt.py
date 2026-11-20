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
o prompt pode ir ao painel levando só marcadores de ID de comando (e o do comando
de agenda), que se trocam lá, pela janela Comandos da IA; o --final roda na
versão definitiva, depois que os IDs entraram, antes dos testes.

O que confere nos dois modos (referência: references/docs/recursos/comandos-gpt-assistant.md):
  - cada comando #{...} tem a mesma forma dos blocos de código do artigo
    (#{ colado, aspas retas, pares "chave": "valor") e usa chaves documentadas;
  - os IDs são números entre aspas, como no artigo;
  - não há variável {{...}}, que não está documentada para o campo Prompt;
  - existe no texto a regra de manter o código (dica do artigo de comandos).

A documentação só mostra a forma #{"chave": "544"}. Ela não diz que o código é
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
    ("queueId",): "Transferir Fila",
    ("queueId", "userId"): "Transferir para Operador",
    ("tagId",): "Atribuir Tag",
    ("removeTag",): "Remover Tag",
    ("closeTicket",): "Encerrar Ticket",
}
EFEITO = "A documentação não diz o efeito; corrija para ficar igual ao artigo."
ASPAS_CURVAS = "“”„‟″‶‘’′"
COMANDO = re.compile(r"#\s?\{[^}\n]*\}")
MARCADOR = re.compile(r"\[\[[^\]\n]*\]\]")
VARIAVEL = re.compile(r"\{\{[^}\n]*\}\}")


def conferir(texto, final=False):
    """Devolve (erros, pendencias, avisos, resumo), cada um uma lista de frases."""
    erros, pendencias, avisos, resumo = [], [], [], []
    falta = erros if final else pendencias  # onde vai o marcador por preencher
    linha_de = lambda pos: texto.count("\n", 0, pos) + 1

    for m in COMANDO.finditer(texto):
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
            erros.append(f"{onde} -> difere da forma mostrada no artigo de comandos, #{{\"chave\": \"544\"}}. {EFEITO}")
            continue
        chaves = tuple(sorted(dados))
        nome = DOCUMENTADAS.get(chaves)
        if nome is None:
            avisos.append(
                f"{onde} -> chave(s) {', '.join(chaves) or '(nenhuma)'} fora do artigo Comandos GPT Assistant. "
                "Se veio da janela Comandos da IA do painel, mantenha como o painel inseriu; se foi digitado, remova."
            )
            continue
        for chave, valor in dados.items():
            if not (isinstance(valor, str) and valor.isdigit()):
                erros.append(f"{onde} -> o valor de {chave} difere do artigo de comandos, que mostra um número entre aspas, como \"544\". {EFEITO}")
        if chaves == ("closeTicket",) and dados["closeTicket"] != "1":
            avisos.append(f"{onde} -> o artigo mostra closeTicket com o valor \"1\".")
        if com_marcador:
            falta.append(f"{onde} -> trocar o marcador pelo ID real ({nome}).")
        if len(erros) == antes:
            resumo.append(f"linha {linha}: {nome} {bruto}" + (" (ID pendente)" if com_marcador else ""))

    for m in re.finditer(r"#\s?\{[^}\n]*$", texto, re.M):
        erros.append(
            f"linha {linha_de(m.start())}: comando aberto com #{{ e não fechado com }} na mesma linha: "
            f"difere da forma do artigo de comandos. {EFEITO}"
        )

    # Marcadores fora dos comandos; o texto mantém as quebras para a linha sair certa.
    sem_comandos = COMANDO.sub(lambda m: " " * len(m.group(0)), texto)
    for m in MARCADOR.finditer(sem_comandos):
        falta.append(f"linha {linha_de(m.start())}: preencher {m.group(0)}")
    for m in VARIAVEL.finditer(texto):
        avisos.append(
            f"linha {linha_de(m.start())}: {m.group(0)} -> a documentação não descreve variáveis para o campo Prompt."
        )
    if COMANDO.search(texto) and not re.search(r"c[óo]digo", texto, re.I):
        avisos.append(
            "o prompt tem comandos, mas não achei a regra de manter o código no texto enviado "
            "(dica do artigo Comandos GPT Assistant)."
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
            "marcador de ID de comando pode ir ao painel e ser trocado pela janela Comandos da IA. "
            "Rode com --final na versão definitiva, depois que os IDs entrarem, antes dos testes."
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
        'Diga: temos #{"tagId": "71"} Notebook. Diga: foi #{"removeTag": "71"} cancelada.\n'
        'Diga: encerrando #{"closeTicket": "1"} agora.\n'
        'Os trechos que começam com #{ e terminam com } são códigos.\n'
    )
    for final in (False, True):
        erros, pendencias, avisos, resumo = conferir(bom, final)
        assert not erros and not pendencias and not avisos and len(resumo) == 5, (final, erros, pendencias, avisos)

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
        "chave desconhecida": 'código: #{"agenda": "1"}',
        "variável": "Olá, {{name}}.",
        "sem regra do código": 'Diga: #{"tagId": "71"} ok.',
        "closeTicket diferente de 1": 'código: #{"closeTicket": "2"}',
    }
    for nome, texto in casos_de_aviso.items():
        erros, pendencias, avisos, _ = conferir(texto, final=True)
        assert avisos and not erros and not pendencias, f"deveria só avisar: {nome} {erros} {avisos}"
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
