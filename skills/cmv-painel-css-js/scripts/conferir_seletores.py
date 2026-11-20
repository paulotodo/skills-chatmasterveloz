#!/usr/bin/env python3
"""Confere CSS e JS personalizados do painel Chat Master Veloz contra o catálogo de references/docs/.

Uso:
  python3 conferir_seletores.py meu.css [meu.js receitas.md ...]
  python3 conferir_seletores.py --tipo css < meu.css
  python3 conferir_seletores.py --historico antigo.css   # em que versões cada nome foi citado no histórico
  python3 conferir_seletores.py --teste

Confere, um a um: classes e ids `custom-css-*`, atributos `data-*`, variáveis `--*`, as classes sem
prefixo do chat (`.ticket-*`, `.message-*`, `.contact-*`) e os eventos com dois-pontos do addEventListener.
Confere o valor de `[data-x="valor"]` contra a linha Valores do atributo em 06 e 12: valor fora de uma lista
fechada é problema; quando o catálogo não lista os valores (ou a lista é aberta), avisa que não conferiu.
Acusa `.Mui*` e `.jss<número>`. No JS, acusa `return` no nível de cima e o que parece segredo (regras de
02-campos-css-js.md) e avisa, como precaução da skill, de innerHTML e de chamadas de rede.
Arquivo .md: confere cada bloco ```css e ```js.
Sai com 0 se não há problema, 1 se há, 2 se não conseguiu rodar. Passar aqui quer dizer que os nomes existem
no catálogo; não quer dizer que o seletor está no elemento certo nem que o efeito visual é o esperado.
"""
import argparse
import difflib
import re
import sys
from collections import defaultdict
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "references" / "docs"
# 00 é o mapa (tem exemplos de grep como `--nome`), 13 é o histórico (cita o que já mudou), 14 são rotas
ARQUIVOS_DO_CATALOGO = {f"{n:02d}" for n in range(1, 13)}

RE_CC = re.compile(r"(?<![\w-])([.#]?)(custom-css-[A-Za-z0-9_-]+)")
RE_DATA = re.compile(r"(?<![\w-])(data-[A-Za-z0-9_-]+)")
RE_VAR = re.compile(r"(?<![\w-])(--[A-Za-z_][A-Za-z0-9_-]*)")
RE_SOLTA = re.compile(r"(?<![\w-])\.((?:ticket|message|contact)-[A-Za-z0-9_-]+)")
RE_PROIBIDO = re.compile(r"(?<![\w-])\.(?:Mui[\w-]+|jss\d+)|\[class[~|^$*]?=\s*[\"']?(?:Mui|jss|makeStyles)[\w-]*")
RE_EVENTO = re.compile(r"addEventListener\(\s*[\"'`]([\w-]+:[\w:-]+)[\"'`]")

RE_COMENT_CSS = re.compile(r"/\*.*?\*/", re.S)
# shortcut: não entende regex literal do JS com aspas ou // dentro; se der alarme falso, tire a regex do trecho
RE_JS = re.compile(r"""//[^\n]*|/\*.*?\*/|"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*'|`(?:\\.|[^`\\])*`""", re.S)
RE_VALOR_ATTR = re.compile(r"(\[\s*[\w-]+\s*[~|^$*]?=)([^\]]*)")
RE_URL = re.compile(r"https?://[^\s\"'`)]+|url\([^)]*\)")
RE_STRING_CSS = re.compile(r""""[^"\n]*"|'[^'\n]*'""")
RE_ATTR_VALOR = re.compile(r"\[\s*(data-[\w-]+)\s*=\s*\\?[\"']?([^\"'\]\\]*)\\?[\"']?\s*(?:[is]\s*)?\]")
RE_ENTRADA_ATTR = re.compile(r"^### `(data-[\w-]+)`\n(.*?)(?=^### |\Z)", re.S | re.M)
# pistas de que a linha Valores descreve um valor livre (id, número, data…) em vez de enumerar todos
RE_VALOR_LIVRE = re.compile(r"…|\.\.\.|\bo id\b|\bos ids\b|o número|quant[ao]s|o caminho|os nomes|ISO 8601|JSON|"
                            r"percentual|hexadecimal|como está gravado|e outro|o motivo do registro|"
                            r"o nível do registro|o status do atendimento|o total|identificador|o nome d")
RE_SEGREDO = re.compile(r"(?<![\w-])\w*token\w*(?![\w-])|\bapi[_-]?key\b|\bBearer\b|\bAuthorization\b|"
                        r"\b\w*(?:senha|password|secret)\w*[\"']?\s*[:=]\s*[\"'`]", re.I)
RE_HTML = re.compile(r"\b(?:innerHTML|outerHTML|insertAdjacentHTML)\b|\bdocument\.write\b")
RE_REDE = re.compile(r"\bfetch\s*\(|\bXMLHttpRequest\b|\bsendBeacon\b|\bnew\s+WebSocket\b")
RE_BLOCO_MD = re.compile(r"^```(css|js|javascript)[ \t]*\n(.*?)^```", re.S | re.M)


def apagar(texto):
    """Troca por espaços sem mudar o tamanho nem as quebras de linha (os números de linha continuam valendo)."""
    return re.sub(r"[^\n]", " ", texto)


def carregar_catalogo():
    """Lê references/docs/ e devolve onde cada nome aparece, os tipos (classe/id), o histórico e os eventos."""
    if not DOCS.is_dir():
        sys.exit(f"Não achei o catálogo em {DOCS}. O script precisa ficar em scripts/, ao lado de references/docs/.")
    onde = defaultdict(set)       # nome -> {"09", "10", "13"...}
    tipos = defaultdict(set)      # custom-css-x -> {".", "#", ""}
    historico = defaultdict(list)  # nome -> [(versão, linha de 13-historico.md)]
    valores = {}                   # data-x -> {"lista": valores entre crases, "fechada": bool, "onde": ["06, linha 887"]}
    eventos, versao_catalogo = set(), "?"
    for arq in sorted(DOCS.glob("[0-9][0-9]-*.md")):
        n, texto = arq.name[:2], arq.read_text(encoding="utf-8")
        # o 00 é escrito à mão e pode ficar para trás; vale a versão do cabeçalho dos arquivos gerados
        m = re.match(r"<!-- gerado por _gerar\.py .*?versão (\S+) -->", texto)
        if m:
            versao_catalogo = m.group(1)
        if n == "00":  # lido primeiro (ordem do nome); os gerados, lidos depois, sobrepõem a versão
            m = re.search(r"Versão do catálogo:\*\*\s*(\S+)", texto)
            versao_catalogo = m.group(1) if m else "?"
            continue
        if n == "05":
            eventos |= set(re.findall(r"`([\w-]+:[\w:-]+)`", texto))
        if n in ("06", "12"):
            for m in RE_ENTRADA_ATTR.finditer(texto):
                v = re.search(r"^- \*\*Valores:\*\*(.*)$", m.group(2), re.M)
                txt = v.group(1) if v else ""
                lista = set(re.findall(r"`([^`]+)`", txt))
                # fechada: enumera no estilo do catálogo (`a` · `b`) e não tem pista de valor livre.
                # shortcut: é heurística sobre o texto; se acusar valor que a entrada admite, leia a entrada
                fechada = len(lista) >= 2 and " · `" in txt and not RE_VALOR_LIVRE.search(txt)
                info = valores.setdefault(m.group(1), {"lista": set(), "fechada": True, "onde": []})
                info["lista"] |= lista
                info["fechada"] = info["fechada"] and fechada
                info["onde"].append(f"{n}, linha {texto.count(chr(10), 0, m.start()) + 1}")
        versao = None
        for num, linha in enumerate(texto.splitlines(), 1):
            if n == "13" and linha.startswith("### "):
                versao = linha[4:].strip()
            nomes = []
            for m in RE_CC.finditer(linha):
                nomes.append(m.group(2))
                if n in ARQUIVOS_DO_CATALOGO and not m.group(2).endswith("-"):
                    tipos[m.group(2)].add(m.group(1))
            nomes += RE_DATA.findall(linha) + RE_VAR.findall(linha) + RE_SOLTA.findall(linha)
            for nome in nomes:
                if nome.endswith("-"):  # `.custom-css-modal-<nome>`, `--mui-*`: é padrão, não nome
                    continue
                onde[nome].add(n)
                if versao and (not historico[nome] or historico[nome][-1][0] != versao):
                    historico[nome].append((versao, num))
    return {"onde": onde, "tipos": tipos, "historico": historico, "eventos": eventos, "versao": versao_catalogo,
            "valores": valores}


def preparar(texto, tipo):
    """Devolve (codigo, bruto, seletores), todos do tamanho do original.

    codigo: sem comentários. bruto: onde procurar custom-css-* (no JS, só o conteúdo das strings).
    seletores: bruto sem URLs e sem valores de atributo, onde procurar data-*, --variáveis e o resto.
    """
    if tipo == "js":
        so_strings = list(apagar(texto))

        def troca(m):
            s = m.group(0)
            if s[0] in "\"'`":
                so_strings[m.start() + 1:m.end() - 1] = s[1:-1]
                return s
            return apagar(s)

        codigo = RE_JS.sub(troca, texto)
        bruto = "".join(so_strings)
    else:
        codigo = bruto = RE_COMENT_CSS.sub(lambda m: apagar(m.group(0)), texto)
    seletores = RE_URL.sub(lambda m: apagar(m.group(0)), bruto)
    seletores = RE_VALOR_ATTR.sub(lambda m: m.group(1) + apagar(m.group(2)), seletores)
    if tipo != "js":
        seletores = RE_STRING_CSS.sub(lambda m: apagar(m.group(0)), seletores)
    return codigo, bruto, seletores


def returns_soltos(estrutura):
    """Posições de `return` fora de qualquer função. estrutura: o JS sem comentários e sem o conteúdo das strings."""
    pilha, soltos = [], []   # pilha: uma entrada por `{` aberta; True se é corpo de função
    for m in re.finditer(r"[{}]|(?<![\w$.])return\b", estrutura):
        t = m.group(0)
        if t == "}":
            if pilha:
                pilha.pop()
        elif t == "return":
            if not any(pilha):
                soltos.append(m.start())
        else:
            antes = estrutura[:m.start()].rstrip()
            funcao = antes.endswith("=>")
            if antes.endswith(")"):   # acha o `(` que casa e olha a palavra antes dele
                nivel, i = 0, len(antes) - 1
                while i >= 0:
                    nivel += (antes[i] == ")") - (antes[i] == "(")
                    if nivel == 0:
                        break
                    i -= 1
                palavra = re.search(r"([\w$]+)\s*$", antes[:max(i, 0)])
                funcao = not palavra or palavra.group(1) not in ("if", "for", "while", "switch", "catch", "with")
            pilha.append(funcao)
    return soltos


def blocos_do_arquivo(nome, texto, tipo=None):
    """Um arquivo vira uma lista de blocos (tipo, texto, primeira linha, grupo). No .md, um grupo por seção `## `."""
    if nome.lower().endswith(".md"):
        blocos = []
        for m in RE_BLOCO_MD.finditer(texto):
            antes = texto[:m.start()]
            secao = len(re.findall(r"^## ", antes, re.M))
            blocos.append(("css" if m.group(1) == "css" else "js", m.group(2), antes.count("\n") + 2, (nome, secao)))
        return blocos
    if not tipo:
        if nome.lower().endswith((".js", ".mjs")):
            tipo = "js"
        elif nome.lower().endswith(".css"):
            tipo = "css"
        else:  # entrada padrão sem --tipo: adivinha
            tipo = "js" if re.search(r"\b(function|const|let|document\.|window\.)|=>", texto) else "css"
    return [(tipo, texto, 1, "arquivos")]


def conferir(arquivos, cat, tipo=None):
    """arquivos: [(nome, texto)]. Devolve (problemas, avisos, usados); cada item é (origem, linhas, mensagem)."""
    onde, usos = cat["onde"], defaultdict(list)   # (grupo, categoria, nome, prefixo) -> [(origem, linha)]
    definidos, lidos = defaultdict(set), defaultdict(set)   # grupo -> nomes que o próprio código cria / lê
    problemas, avisos = [], []

    for nome_arq, texto in arquivos:
        for tipo_bloco, corpo, linha0, grupo in blocos_do_arquivo(nome_arq, texto, tipo):
            codigo, bruto, seletores = preparar(corpo, tipo_bloco)

            def linha(pos):
                return corpo.count("\n", 0, pos) + linha0

            def usar(categoria, nome, pos, prefixo=""):
                usos[(grupo, categoria, nome, prefixo)].append((nome_arq, linha(pos)))

            for m in RE_CC.finditer(bruto):
                usar("cc", m.group(2), m.start(), m.group(1))
            for m in RE_SOLTA.finditer(seletores):
                usar("solta", m.group(1), m.start(), ".")
            for m in RE_PROIBIDO.finditer(bruto):
                problemas.append((nome_arq, [linha(m.start())], f"{m.group(0)}: seletor proibido. Classes do "
                                  "Material-UI (.Mui*, .jss123) mudam a cada atualização; use a âncora custom-css-* "
                                  "ou o data-* do catálogo, e se não houver, o alvo não existe."))

            for m in RE_ATTR_VALOR.finditer(bruto):
                usar("valor", m.group(1), m.start(), m.group(2).strip())

            criados_aqui = set()   # posições em que o JS cria (não lê) um atributo ou variável
            if tipo_bloco == "js":
                estrutura = "".join(" " if s not in " \n" else c for c, s in zip(codigo, bruto))
                for pos in returns_soltos(estrutura):
                    problemas.append((nome_arq, [linha(pos)], "return no nível de cima: o código do campo vira o "
                                      "corpo de um try, e um return solto ali é erro de sintaxe; código com erro de "
                                      "sintaxe não é injetado (02-campos-css-js.md). Envolva o script em "
                                      "(function () { … })();"))
                sem_valores = RE_VALOR_ATTR.sub(lambda m: m.group(1) + apagar(m.group(2)), codigo)
                vistos = set()
                for m in RE_SEGREDO.finditer(sem_valores):
                    trecho = m.group(0).strip()
                    if trecho.lower() in vistos:
                        continue
                    vistos.add(trecho.lower())
                    problemas.append((nome_arq, [linha(m.start())], f"{trecho}: parece segredo (token, chave de API, "
                                      "senha) em JS. Nenhum campo de JS guarda segredo: o pré-login é lido por qualquer "
                                      "pessoa sem login, e o pós-login e o da empresa rodam no navegador de todo "
                                      "usuário autenticado, onde qualquer um lê (02-campos-css-js.md). Se o segredo já "
                                      "foi colado em algum campo, troque-o. Chamada com token se faz num servidor, "
                                      "fora do painel (skill cmv-api)."))
                for regex, texto_aviso in (
                        (RE_HTML, "insere HTML na página. Use textContent e nunca monte HTML com texto que veio de "
                                  "mensagem de cliente"),
                        (RE_REDE, "faz chamada de rede. Confira que não envia dado de cliente a terceiros nem "
                                  "precisa de token")):
                    m = regex.search(estrutura)
                    if m:
                        avisos.append((nome_arq, [linha(m.start())], f"{m.group(0).strip(' (')}: {texto_aviso}. "
                                       "Precaução da skill, não regra de 02-campos-css-js.md."))
                for m in re.finditer(r"(?:set|toggle)Attribute\(\s*[\"'`](data-[\w-]+)", codigo):
                    definidos[grupo].add(m.group(1))
                    criados_aqui.add(m.start(1))
                for m in re.finditer(r"setProperty\(\s*[\"'`](--[\w-]+)", codigo):
                    definidos[grupo].add(m.group(1))
                    criados_aqui.add(m.start(1))
                    usos[(grupo, "var-def", m.group(1), "")].append((nome_arq, linha(m.start(1))))
                for m in re.finditer(r"\bdataset\.([A-Za-z_]\w*)(\s*=(?!=))?", codigo):
                    attr = "data-" + re.sub(r"[A-Z]", lambda c: "-" + c.group(0).lower(), m.group(1))
                    if m.group(2):
                        definidos[grupo].add(attr)
                    else:
                        usar("data", attr, m.start())
                for m in RE_EVENTO.finditer(codigo):
                    if m.group(1) not in cat["eventos"]:
                        problemas.append((nome_arq, [linha(m.start())], f'evento "{m.group(1)}": não está em '
                                          f"05-eventos-js.md (lá só há: {', '.join(sorted(cat['eventos'])) or 'nenhum'})."))
            for m in RE_DATA.finditer(seletores):
                if m.start() not in criados_aqui:
                    usar("data", m.group(1), m.start())
            for m in RE_VAR.finditer(seletores):
                if m.start() in criados_aqui:
                    continue
                if re.match(r"\s*:", seletores[m.end():]):
                    definidos[grupo].add(m.group(1))
                    usos[(grupo, "var-def", m.group(1), "")].append((nome_arq, linha(m.start())))
                else:
                    lidos[grupo].add(m.group(1))
                    usar("var", m.group(1), m.start())

    def no_catalogo(nome):
        return bool(onde.get(nome, set()) & ARQUIVOS_DO_CATALOGO)

    def parecidos(nome, categoria):
        def miolo(n):   # compara sem o prefixo comum, que sozinho já faria tudo parecer parecido
            return re.sub(r"^(custom-css-|data-|--)", "", n)
        mesma_familia = r"(ticket|message|contact)-" if categoria == "solta" else re.escape(nome[:6])
        candidatos = {miolo(n): n for n in onde if no_catalogo(n) and re.match(mesma_familia, n)}
        achados = difflib.get_close_matches(miolo(nome), list(candidatos), n=3, cutoff=0.75)
        return f" Parecidos no catálogo: {', '.join(candidatos[x] for x in achados)}." if achados else ""

    usados, externo, painel = [], defaultdict(set), defaultdict(set)
    for (grupo, categoria, nome, prefixo), ocorrencias in sorted(usos.items(), key=lambda kv: kv[1][0]):
        origem, linhas = ocorrencias[0][0], sorted({l for _, l in ocorrencias})
        rotulo = prefixo + nome

        def problema(msg):
            problemas.append((origem, linhas, f"{rotulo}: {msg}"))

        if categoria == "valor":   # nome = atributo, prefixo = valor
            rotulo = f'[{nome}="{prefixo}"]'
            info = cat["valores"].get(nome, {"lista": set(), "fechada": False, "onde": []})
            if not prefixo or not no_catalogo(nome) or nome in definidos[grupo] or prefixo in info["lista"]:
                continue   # atributo inexistente já é acusado em "data"; valor listado está certo
            ref = "; ".join(info["onde"]) or "sem entrada própria em 06 nem em 12"
            simples = sorted(v for v in info["lista"] if re.fullmatch(r"[\w.-]+", v))
            if info["fechada"]:
                perto = difflib.get_close_matches(prefixo, simples, n=3, cutoff=0.6)
                problema(f"valor que não está entre os listados para {nome} ({ref}): "
                         + ", ".join(simples[:15]) + ("…" if len(simples) > 15 else "") + "."
                         + (f" Parecidos: {', '.join(perto)}." if perto else ""))
            else:
                motivo = ("o catálogo não lista os valores deste atributo" if not simples else
                          "o valor não está entre os citados, e a lista do catálogo não é fechada")
                avisos.append((origem, linhas, f"{rotulo}: valor não conferido: {motivo} ({ref}). Confirme o valor "
                               "pelo Inspecionar antes de entregar."))
            continue
        if categoria == "var-def":
            if no_catalogo(nome):
                usados.append((rotulo, sorted(onde[nome] & ARQUIVOS_DO_CATALOGO)))
            elif nome not in lidos[grupo]:
                problema("variável definida mas nunca lida. A plataforma não lê variável com esse nome: "
                         "ela não existe no catálogo (03, 04, 12). Se é uma variável sua, lida em outro arquivo, "
                         "confira os arquivos juntos." + parecidos(nome, categoria))
            continue
        if categoria == "cc" and nome.endswith("-"):   # [class*="custom-css-modal-confirmation-"]
            if not any(n.startswith(nome) and no_catalogo(n) for n in onde):
                problema("nenhuma âncora do catálogo começa assim.")
            continue
        if categoria in ("var", "data") and nome in definidos[grupo] and not no_catalogo(nome):
            continue   # criado pelo próprio código: não é do catálogo, e tudo bem
        if no_catalogo(nome):
            usados.append((rotulo, sorted(onde[nome] & ARQUIVOS_DO_CATALOGO)))
            if categoria == "cc":
                (externo if onde[nome] <= {"12", "13"} else painel)[grupo].add(rotulo)
                conhecidos = cat["tipos"][nome]
                if prefixo and "" not in conhecidos and prefixo not in conhecidos:
                    certo = "id (#" if "#" in conhecidos else "classe (."
                    problema(f"no catálogo é {certo}{nome}), não {'classe' if prefixo == '.' else 'id'}.")
        elif nome in onde:   # só em 13-historico.md
            versao, num = cat["historico"][nome][0]
            avisos.append((origem, linhas, f"{rotulo}: só aparece no histórico (versão {versao}, linha {num} de "
                           "13-historico.md), não nas listas do catálogo. Leia a entrada e confirme que continua "
                           "existindo antes de entregar."))
        else:
            o_que = {"cc": "âncora", "data": "atributo", "var": "variável", "solta": "classe sem prefixo"}[categoria]
            extra = " (em 11-classes-sem-prefixo.md)" if categoria == "solta" else ""
            problema(f"{o_que} que não existe no catálogo{extra}. Não invente nome: o que não está no catálogo "
                     "não existe no painel." + parecidos(nome, categoria))
    for grupo in externo:
        if painel[grupo]:
            avisos.append((grupo if isinstance(grupo, str) else grupo[0], [], "mistura âncoras do Chat Externo ("
                           + ", ".join(sorted(externo[grupo])[:3]) + "…) com âncoras do painel ("
                           + ", ".join(sorted(painel[grupo])[:3]) + "…). São campos diferentes: o CSS do painel não "
                           "chega na página do Chat Externo, nem o contrário. Separe em dois blocos."))
    return problemas, avisos, usados


def relatorio(arquivos, cat, tipo=None, detalhe=False, historico=False):
    problemas, avisos, usados = conferir(arquivos, cat, tipo)
    nomes = sorted({r for r, _ in usados})
    print(f"Catálogo {cat['versao']}: {len(nomes)} nome(s) conferido(s) e encontrado(s).")
    if detalhe:
        for rotulo, arqs in sorted(set((r, tuple(a)) for r, a in usados)):
            print(f"  ok  {rotulo}  (em {', '.join(arqs)})")
    if historico:
        print("Histórico (13-historico.md), da versão mais nova para a mais antiga:")
        for rotulo in nomes:
            versoes = cat["historico"].get(rotulo.lstrip(".#"), [])
            if versoes:
                print(f"  {rotulo}: " + ", ".join(f"{v} (linha {n})" for v, n in versoes[:6])
                      + (" …" if len(versoes) > 6 else ""))
    for titulo, itens in (("PROBLEMA", problemas), ("AVISO", avisos)):
        for origem, linhas, msg in itens:
            local = f"{origem}, linha {', '.join(map(str, linhas[:5]))}" if linhas else origem
            print(f"{titulo} [{local}] {msg}")
    print(f"Resultado: {len(problemas)} problema(s), {len(avisos)} aviso(s).")
    if problemas:
        print("Corrija os problemas antes de entregar.")
    else:
        print("Os nomes usados existem no catálogo" + ("; leia cada aviso antes de entregar." if avisos else ".")
              + " Não foi conferido, e continua por conta de quem escreve: se cada seletor está no elemento certo, "
              "se o valor vale naquele elemento e qual é o efeito visual.")
    return 1 if problemas else 0


def autoteste(cat):
    def roda(texto, nome="t.css"):
        p, a, u = conferir([(nome, texto)], cat)
        return [m for _, _, m in p], [m for _, _, m in a], [r for r, _ in u]

    # CSS correto, com tudo o que não pode dar alarme falso
    p, a, u = roda("""
        /* comentário com .custom-css-inventada, [data-nada] e --nada não conta */
        .custom-css-ticket-item { border-radius: 12px !important; }
        .custom-css-msg-bubble[data-status="pending"] { opacity: .6; }
        body[data-theme="dark"] .custom-css-page-header { background: var(--mui-paper); }
        :root { --minha-cor: #0f766e; --mui-primary: var(--minha-cor); }
        #custom-css-contacts [data-menu="data-inventado"] { background: url(https://x.com/data-foo/--bar.png); }
        [class*="custom-css-modal-confirmation-"] .ticket-name::after { content: "--x data-y"; }
    """)
    assert not p and len(a) == 1 and '[data-menu="data-inventado"]: valor não conferido' in a[0], (p, a)
    assert {".custom-css-ticket-item", "#custom-css-contacts", "data-status", "data-theme", "data-menu",
            "--mui-paper", "--mui-primary", ".ticket-name"} <= set(u), u

    # CSS errado: cada linha tem de ser acusada
    p, a, u = roda("""
        .custom-css-inventada { color: red; }
        .custom-css-ticket-item[data-inventado] { color: var(--inventada); }
        .MuiPaper-root, .jss123, [class*="MuiButton"] { display: none; }
        #custom-css-ticket-item, .custom-css-contacts { color: red; }
        :root { --mui-inventada: red; }
        .ticket-inventada, [class^="custom-css-nadanada-"] { color: red; }
    """)
    for trecho in (".custom-css-inventada: âncora", "data-inventado: atributo", "--inventada: variável",
                   ".MuiPaper-root: seletor proibido", ".jss123: seletor proibido", '[class*="MuiButton',
                   "#custom-css-ticket-item: no catálogo é classe", ".custom-css-contacts: no catálogo é id",
                   "--mui-inventada: variável definida mas nunca lida", ".ticket-inventada: classe sem prefixo",
                   "custom-css-nadanada-: nenhuma âncora"):
        assert any(trecho in m for m in p), (trecho, p)
    assert len(p) == 11, p

    # JS correto: i-- não é variável, atributo e variável criados pelo código não são do catálogo
    p, a, u = roda("""
        // .custom-css-inventada em comentário não conta
        for (let i = 3; i > 0; i--) { --i; }
        window.addEventListener("sip:state", e => console.log(e.detail.call));
        document.addEventListener("click", ev => {
          const el = ev.target.closest('.custom-css-ticket-item[data-status="pending"]');
          if (!el || el.dataset.cmvVisto) return;
          el.dataset.cmvVisto = "1";
          el.setAttribute("data-cmv-hora", Date.now());
          document.documentElement.style.setProperty("--cmv-cor", "#123");
          document.documentElement.style.setProperty("--menu-ordem", "sistema");
          el.style.color = "var(--cmv-cor)";
          fetch("https://exemplo.com/data-coisa");
          if (document.getElementById("custom-css-contacts") && el.dataset.unreadCount > 0) {}
        });
    """, "t.js")
    assert not p and len(a) == 1 and "fetch: faz chamada de rede" in a[0] and "Precaução da skill" in a[0], (p, a)
    assert {".custom-css-ticket-item", "custom-css-contacts", "data-status", "data-unread-count"} <= set(u), u

    # JS errado
    p, a, u = roda("""
        window.addEventListener("ticket:aberto", () => {});
        document.querySelector(".custom-css-inventada .MuiButton-root [data-inventado]");
        if (el.dataset.naoExiste) el.style.setProperty("--x", getComputedStyle(el).getPropertyValue("--inventada"));
    """, "t.js")
    for trecho in ('evento "ticket:aberto"', ".custom-css-inventada: âncora", ".MuiButton-root: seletor proibido",
                   "data-inventado: atributo", "data-nao-existe: atributo", "--inventada: variável"):
        assert any(trecho in m for m in p), (trecho, p)

    # Markdown: só os blocos css/js, com a linha certa; atributo criado no JS vale no CSS da mesma seção
    md = ("## Receita\n\ntexto com .custom-css-inventada fora de bloco\n\n```js\nel.setAttribute('data-cmv-x', 1);\n```\n\n"
          "```css\n[data-cmv-x] { color: red; }\n.custom-css-inventada { color: red; }\n```\n\n"
          "## Outra\n\n```css\n[data-cmv-x] { color: red; }\n```\n")
    prob, _, _ = conferir([("r.md", md)], cat)
    assert [(l, m.split(":")[0]) for _, l, m in prob] == [([11], ".custom-css-inventada"), ([17], "data-cmv-x")], prob

    # Chat Externo misturado com painel vira aviso; sozinho, passa
    p, a, u = roda(".custom-css-chat-bubble { color: red; } .custom-css-ticket-item { color: red; }")
    assert not p and len(a) == 1 and "Chat Externo" in a[0], (p, a)
    p, a, u = roda('.custom-css-chat-row[data-autor="atendente"] .custom-css-chat-bubble { background: var(--wa-popup); }')
    assert not p and not a, (p, a)
    # Valores de atributo: lista fechada acusa, lista aberta ou ausente avisa, valor listado passa
    p, a, u = roda("""
        .custom-css-login-link[data-link="cadastro"], body[data-theme='dark'], [data-action=resolve] { color: red; }
        .custom-css-login-link[data-link="signup"], body[data-theme="escuro"] { color: red; }
        [data-menu="contacts"], [data-action="resolver"], [data-unread-count="3"] { color: red; }
    """)
    assert len(p) == 2 and len(a) == 3, (p, a)
    assert any('[data-link="signup"]: valor que não está entre os listados' in m and "cadastro" in m for m in p), p
    assert any('[data-theme="escuro"]: valor que não está' in m and "dark" in m for m in p), p
    for trecho in ('[data-menu="contacts"]: valor não conferido: o catálogo não lista',
                   '[data-action="resolver"]: valor não conferido: o valor não está entre os citados',
                   '[data-unread-count="3"]: valor não conferido'):
        assert any(trecho in m for m in a), (trecho, a)
    p, a, u = roda("""document.querySelector('.custom-css-login-link[data-link="signup"]');""", "t.js")
    assert len(p) == 1 and '[data-link="signup"]' in p[0], p

    # JS: return no nível de cima é erro de sintaxe (02); dentro de função, não
    p, a, u = roda("""
        var el = document.getElementById("custom-css-contacts");
        if (!el) { return; }
        return;
    """, "t.js")
    assert [m.split(":")[0] for m in p] == ["return no nível de cima"] * 2, p
    p, a, u = roda("""
        (function () { if (!window.x) return; })();
        (() => { for (;;) { return 1; } })();
        document.addEventListener("click", function (ev) { if (!ev.target) return; try { x(); } catch (e) { return; } });
        var o = { metodo() { return 1; }, outro: async function nome(a, b) { return a; } };
        var texto = "return { solto } numa string"; // return em comentário
    """, "t.js")
    assert not p and not a, (p, a)

    # JS: segredo é problema; nome do catálogo com "password"/"senha" não é
    p, a, u = roda("""
        (function () {
          var TOKEN = "abc123";
          fetch("https://api.exemplo.com/x", { headers: { Authorization: "Bearer " + TOKEN, apikey: "k" } });
          var cfg = { senha: "1234" };
          el.innerHTML = "<b>oi</b>";
        })();
    """, "t.js")
    for trecho in ("TOKEN: parece segredo", "Authorization: parece segredo", "Bearer: parece segredo",
                   "apikey: parece segredo", 'senha: ": parece segredo'):
        assert any(trecho in m for m in p), (trecho, p)
    assert len(p) == 5 and len(a) == 2 and all("Precaução da skill" in m for m in a), (p, a)
    p, a, u = roda("""
        (function () {
          var campo = document.querySelector(".custom-css-login-password-input");
          var item = document.querySelector('.custom-css-menu-usuario [data-menu-action="trocar-senha"]');
          if (campo && campo.type === "password") { campo.title = "Digite a sua senha"; }
        })();
    """, "t.js")
    assert not p and not a, (p, a)

    print(f"Autoteste: tudo certo (catálogo {cat['versao']}, {len(cat['onde'])} nomes lidos de {DOCS}).")


def main():
    ap = argparse.ArgumentParser(description="Confere seletores, atributos data-* e variáveis CSS contra o catálogo "
                                 "do painel Chat Master Veloz (references/docs/).")
    ap.add_argument("arquivos", nargs="*", help="arquivos .css, .js ou .md (blocos ```css/```js); sem arquivo, lê a entrada padrão")
    ap.add_argument("--tipo", choices=["css", "js"], help="trata a entrada como CSS ou JS (padrão: pela extensão)")
    ap.add_argument("--detalhe", action="store_true", help="lista cada nome conferido e em que arquivo do catálogo está")
    ap.add_argument("--historico", action="store_true", help="mostra em que versões de 13-historico.md cada nome foi citado")
    ap.add_argument("--teste", action="store_true", help="roda o autoteste")
    args = ap.parse_args()
    cat = carregar_catalogo()
    if args.teste:
        autoteste(cat)
        return 0
    entradas = []
    for nome in args.arquivos or ["-"]:
        try:
            entradas.append(("entrada padrão", sys.stdin.read()) if nome == "-"
                            else (nome, Path(nome).read_text(encoding="utf-8")))
        except OSError as e:
            print(f"Não consegui ler {nome}: {e}", file=sys.stderr)
            return 2
    return relatorio(entradas, cat, args.tipo, args.detalhe, args.historico)


if __name__ == "__main__":
    sys.exit(main())
