#!/usr/bin/env python3
"""Copia a documentação-fonte para references/docs de cada skill, conforme skills/<skill>/fontes.txt.

Uso:
  python3 montar.py [skill ...]   monta as skills citadas (sem argumento: todas)
  python3 montar.py --zip         monta todas e gera dist/<skill>.skill e dist/<skill>.zip (para subir no claude.ai)

references/docs é sempre apagada e recriada: não escreva nada à mão ali.

Linhas de fontes.txt (o que vem depois de # é comentário):
  plataforma:recursos/               todos os .md da pasta
  plataforma:INDICE-api.md           um arquivo (aceita glob)
  plataforma:recursos/token-openai.md
  css:*.md
  subarvore:FlowBuilder              o item de menu com esse título, nos índices, e tudo abaixo dele
"""
import io
import re
import shutil
import sys
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZES = {
    "plataforma": AQUI.parent / "docs-plataforma-chatmasterveloz",
    "css": AQUI.parent / "docs-css-chatmasterveloz",
}
ITEM = re.compile(r"^(\s*)- \[(.+?)\]\((.+?\.md)\)")


def subarvore(titulo):
    for indice in ("INDICE-recursos.md", "INDICE-api.md", "INDICE-trilhas.md"):
        achados, nivel = [], None
        for linha in (RAIZES["plataforma"] / indice).read_text().splitlines():
            m = ITEM.match(linha)
            if not m:
                continue
            recuo = len(m[1])
            if nivel is None:
                if m[2] == titulo:
                    nivel = recuo
                    achados.append(m[3])
            elif recuo > nivel:
                achados.append(m[3])
            else:
                break
        if achados:
            return achados
    sys.exit(f"subarvore não encontrada nos índices: {titulo!r}")


def montar(skill):
    pasta = AQUI / "skills" / skill
    destino = pasta / "references" / "docs"
    shutil.rmtree(destino, ignore_errors=True)
    for bruta in (pasta / "fontes.txt").read_text().splitlines():
        linha = bruta.split("#")[0].strip()
        if not linha:
            continue
        raiz, _, alvo = linha.partition(":")
        if raiz == "subarvore":
            base = RAIZES["plataforma"]
            caminhos = [base / c for c in subarvore(alvo)]
        else:
            base = RAIZES[raiz]
            caminhos = sorted(base.glob(alvo + "*.md" if alvo.endswith("/") else alvo))
        if not caminhos or not all(c.is_file() for c in caminhos):
            sys.exit(f"{skill}/fontes.txt: nada encontrado para {linha!r}")
        for origem in caminhos:
            copia = destino / origem.relative_to(base)
            copia.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(origem, copia)
    arquivos = sorted(destino.rglob("*.md"))
    linhas = [f"# Artigos incluídos nesta skill ({len(arquivos)})", ""]
    for arq in arquivos:
        # primeira linha "# Título": os arquivos de CSS começam por um comentário HTML
        titulo = next((l[2:].strip() for l in arq.read_text().splitlines() if l.startswith("# ")), arq.stem)
        fonte = re.search(r"^- \*\*Fonte:\*\* <?(https?://[^\s>]+)", arq.read_text(), re.M)
        linhas.append(f"- [{titulo}]({arq.relative_to(destino)})" + (f" · Fonte: <{fonte[1]}>" if fonte else ""))
    (destino / "INDICE.md").write_text("\n".join(linhas) + "\n")
    print(f"{skill}: {len(arquivos)} arquivos em references/docs")
    conferir(pasta)


CITACAO = re.compile(r"(?<![\w/.-])((?:[\w-]+/)*[\w.-]+\.(?:md|py|json))\b")
PASTAS_DOCS = ("api/", "recursos/", "trilhas/", "outros/")


def conferir(pasta):
    """Acusa arquivo citado nos textos escritos à mão que não existe (artigo renomeado ou removido).

    Três jeitos de citar: caminho a partir da skill (references/…, scripts/…, assets/…), caminho a partir
    da cópia da documentação (recursos/x.md, api/x.md) e só o nome do artigo (bloco-menu.md).
    """
    nomes = {f.name for f in pasta.rglob("*") if f.is_file()}
    quebrados = set()
    for arq in pasta.rglob("*.md"):
        if "docs" in arq.relative_to(pasta).parts:
            continue
        for citado in CITACAO.findall(arq.read_text()):
            nome = citado.rsplit("/", 1)[-1]
            if citado.startswith(("references/", "scripts/", "assets/")):
                existe = (pasta / citado).is_file()
            elif citado.startswith(PASTAS_DOCS):
                # nome com maiúscula é marcador de exemplo (recursos/ARTIGO.md), não citação
                existe = nome != nome.lower() or (pasta / "references" / "docs" / citado).is_file()
            elif "/" not in citado and nome.endswith(".md") and nome == nome.lower() and ("-" in nome or nome[0].isdigit()):
                existe = nome in nomes          # só o nome do artigo, como bloco-menu.md
            else:
                continue                        # exemplo, marcador (ARTIGO.md) ou caminho de fora da skill
            if not existe:
                quebrados.add(f"  {arq.relative_to(pasta)} cita {citado}")
    if quebrados:
        sys.exit(f"{pasta.name}: caminhos citados que não existem:\n" + "\n".join(sorted(quebrados)))


LIMITE_CLAUDE_AI = 200  # o claude.ai recusa o envio: "Zip contains too many files (maximum 200)"
NOTA_COMPACTADA = """> **Nesta instalação os artigos vêm compactados.** A pasta `references/docs/` não existe aqui: os artigos estão em `references/docs.zip`, porque o claude.ai aceita no máximo 200 arquivos por skill. Antes de ler ou buscar qualquer artigo, rode uma vez, trocando `PASTA` pela pasta desta skill (a que contém este SKILL.md):
>
> ```bash
> python3 -c "import zipfile,tempfile,os; d=os.path.join(tempfile.gettempdir(),'{skill}','docs'); zipfile.ZipFile('PASTA/references/docs.zip').extractall(d); print(d)"
> ```
>
> O comando imprime a pasta onde os artigos ficaram. Daí em diante, todo caminho `references/docs/...` citado nesta skill fica nessa pasta: leia, liste e busque ali.{scripts} Na resposta, continue citando o título do artigo e o link, nunca esses caminhos.

"""


def empacotar(skill):
    pasta = AQUI / "skills" / skill
    saida = AQUI / "dist" / f"{skill}.skill"
    saida.parent.mkdir(exist_ok=True)
    arquivos = [a for a in sorted(pasta.rglob("*")) if a.is_file() and a.name != "fontes.txt" and "__pycache__" not in a.parts]
    docs = pasta / "references" / "docs"
    compactar = len(arquivos) > LIMITE_CLAUDE_AI
    with zipfile.ZipFile(saida, "w", zipfile.ZIP_DEFLATED) as z:
        if compactar:
            # Os artigos viram um arquivo só, e o SKILL.md do pacote ganha a nota que manda abri-lo.
            # A pasta skills/ não muda: no Claude Code os artigos continuam soltos.
            dentro = io.BytesIO()
            with zipfile.ZipFile(dentro, "w", zipfile.ZIP_DEFLATED) as zd:
                for arq in arquivos:
                    if docs in arq.parents:
                        zd.write(arq, arq.relative_to(docs))
            z.writestr(f"{skill}/references/docs.zip", dentro.getvalue(), zipfile.ZIP_STORED)
        for arq in arquivos:
            destino = str(Path(skill) / arq.relative_to(pasta))
            if compactar and docs in arq.parents:
                continue
            if compactar and arq == pasta / "SKILL.md":
                _, frente, corpo = arq.read_text().split("---\n", 2)
                scripts = " Os scripts desta skill já acham os artigos sozinhos." if (pasta / "scripts").is_dir() else ""
                z.writestr(destino, f"---\n{frente}---\n\n{NOTA_COMPACTADA.format(skill=skill, scripts=scripts)}{corpo.lstrip()}")
            else:
                z.write(arq, destino)
        total = len(z.namelist())
    assert total <= LIMITE_CLAUDE_AI, f"{skill}: {total} arquivos no pacote, o claude.ai aceita {LIMITE_CLAUDE_AI}"
    # a ajuda do claude.ai só documenta o envio de .zip; o .skill é o mesmo arquivo com outro nome
    shutil.copyfile(saida, saida.with_suffix(".zip"))
    print(f"{saida.relative_to(AQUI)}: {saida.stat().st_size // 1024} KB, {total} arquivos" + (", artigos em references/docs.zip" if compactar else ""))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--zip"]
    skills = args or sorted(p.parent.name for p in (AQUI / "skills").glob("*/fontes.txt"))
    for s in skills:
        montar(s)
        if "--zip" in sys.argv:
            empacotar(s)
