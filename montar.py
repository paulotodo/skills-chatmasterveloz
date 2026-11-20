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


CITACAO = re.compile(r"(?:references|scripts|assets)/[\w./-]*\.(?:md|py|json)")


def conferir(pasta):
    """Acusa caminho citado nos arquivos escritos à mão que não existe (artigo renomeado ou removido)."""
    quebrados = set()
    for arq in pasta.rglob("*.md"):
        if "docs" in arq.relative_to(pasta).parts:
            continue
        for citado in CITACAO.findall(arq.read_text()):
            if not (pasta / citado).is_file():
                quebrados.add(f"  {arq.relative_to(pasta)} cita {citado}")
    if quebrados:
        sys.exit(f"{pasta.name}: caminhos citados que não existem:\n" + "\n".join(sorted(quebrados)))


def empacotar(skill):
    pasta = AQUI / "skills" / skill
    saida = AQUI / "dist" / f"{skill}.skill"
    saida.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(saida, "w", zipfile.ZIP_DEFLATED) as z:
        for arq in sorted(pasta.rglob("*")):
            if arq.is_file() and arq.name != "fontes.txt" and "__pycache__" not in arq.parts:
                z.write(arq, Path(skill) / arq.relative_to(pasta))
    # a ajuda do claude.ai só documenta o envio de .zip; o .skill é o mesmo arquivo com outro nome
    shutil.copyfile(saida, saida.with_suffix(".zip"))
    print(f"{saida.relative_to(AQUI)}: {saida.stat().st_size // 1024} KB")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--zip"]
    skills = args or sorted(p.parent.name for p in (AQUI / "skills").glob("*/fontes.txt"))
    for s in skills:
        montar(s)
        if "--zip" in sys.argv:
            empacotar(s)
