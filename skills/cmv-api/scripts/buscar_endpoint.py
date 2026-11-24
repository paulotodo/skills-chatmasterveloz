#!/usr/bin/env python3
"""Busca endpoints da API do Chat Master Veloz por palavra, método e tipo de conexão.

Lê references/docs/INDICE-api-endpoints.md e, para cada artigo, a linha **API:**
(o índice não traz o tipo de conexão; é isso que este script acrescenta a um grep).
Lê também references/docs/revendedor/INDICE-api-endpoints.md, as APIs administrativas do
revendedor: aparecem marcadas como "Super Admin" e só entram num filtro por conexão com --conexao admin.
Não faz nenhuma chamada de rede.

Uso:
  python3 scripts/buscar_endpoint.py texto                 # palavras no título, endereço ou arquivo
  python3 scripts/buscar_endpoint.py imagem url --conexao oficial
  python3 scripts/buscar_endpoint.py --metodo DELETE
  python3 scripts/buscar_endpoint.py ticket --conexao pro --exato   # não inclui os "Todas"
  python3 scripts/buscar_endpoint.py --conexao admin       # as APIs administrativas (token do Super Admin)
  python3 scripts/buscar_endpoint.py --conexoes            # lista os valores da linha API:
  python3 scripts/buscar_endpoint.py --autoteste
"""
import argparse
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "references" / "docs"
if not DOCS.is_dir() and DOCS.with_suffix(".json").is_file():
    # Pacote do claude.ai (máximo de 200 arquivos, sem zip dentro): os artigos vêm em references/docs.json.
    import json
    import tempfile
    compactado, DOCS = DOCS.with_suffix(".json"), Path(tempfile.gettempdir()) / "cmv-api" / "docs"
    # shortcut: não reextrai se a pasta já existe; no claude.ai cada conversa começa vazia. Se o pacote for trocado na mesma máquina, apagar a pasta.
    if not (DOCS / "INDICE-api-endpoints.md").is_file():
        for caminho, texto in json.loads(compactado.read_text(encoding="utf-8")).items():
            (DOCS / caminho).parent.mkdir(parents=True, exist_ok=True)
            (DOCS / caminho).write_text(texto, encoding="utf-8")
LINHA = re.compile(r"^\| (GET|POST|PUT|DELETE|PATCH) \| `([^`]+)` \| \[(.+)\]\(([^)]+)\) \|$")
BASE = "https://api2.chatmasterveloz.com"


def norm(texto):
    """Minúsculas e sem acento, para 'audio' achar 'Áudio'."""
    sem = unicodedata.normalize("NFD", texto)
    return "".join(c for c in sem if unicodedata.category(c) != "Mn").lower()


def carregar():
    itens = []
    # "" é a API do cliente (Central de Ajuda); "revendedor/" são as APIs administrativas
    for pasta in ("", "revendedor/"):
        indice = DOCS / pasta / "INDICE-api-endpoints.md"
        if not indice.is_file():
            continue
        for linha in indice.read_text(encoding="utf-8").splitlines():
            m = LINHA.match(linha)
            if not m:
                continue
            metodo, endereco, titulo, artigo = m.groups()
            artigo = pasta + artigo
            api = ""
            caminho = DOCS / artigo
            if caminho.exists():
                achado = re.search(r"^\*\*API:\*\*\s*(.+)$", caminho.read_text(encoding="utf-8"), re.M)
                api = achado.group(1).strip() if achado else ""
            if pasta and api:
                api = f"Super Admin ({api})"   # o selo "Todas" delas não quer dizer "qualquer token"
            itens.append({"metodo": metodo, "endereco": endereco, "titulo": titulo,
                          "artigo": artigo, "api": api or "?"})
    return itens


def filtrar(itens, palavras=(), metodo=None, conexao=None, exato=False):
    saida = []
    for it in itens:
        alvo = norm(f"{it['titulo']} {it['endereco']} {it['artigo']}")
        if any(norm(p) not in alvo for p in palavras):
            continue
        if metodo and it["metodo"] != metodo.upper():
            continue
        if conexao:
            api = norm(it["api"])
            # "Todas" vale para qualquer conexão segundo o selo do artigo; --exato tira esses.
            # Quem pede as administrativas (--conexao admin) não quer as "Todas" do cliente junto.
            if norm(conexao) not in api and (exato or api != "todas" or norm(conexao) in "super admin"):
                continue
        saida.append(it)
    return saida


def autoteste():
    itens = carregar()
    admin = [it for it in itens if it["artigo"].startswith("revendedor/")]
    assert len(itens) - len(admin) == 309, f"esperava 309 endpoints no índice, achei {len(itens) - len(admin)}"
    assert admin, "não achei as APIs administrativas (references/docs/revendedor/INDICE-api-endpoints.md)"
    faltando = [it["artigo"] for it in itens if not (DOCS / it["artigo"]).exists()]
    assert not faltando, f"artigos do índice que não existem: {faltando}"
    sem_api = [it["artigo"] for it in itens if it["api"] == "?"]
    assert not sem_api, f"artigos sem a linha **API:**: {sem_api}"

    def arquivos(**kw):
        return {it["artigo"] for it in filtrar(itens, **kw)}

    assert "api/api-oficial-mensagem.md" in arquivos(palavras=["mensagem"], conexao="oficial", exato=True)
    assert "api/api-mensagem-de-texto.md" not in arquivos(palavras=["mensagem"], conexao="oficial")
    assert "api/api-enviar-audio-por-url-pro.md" in arquivos(palavras=["audio", "URL"], conexao="pro")
    assert "api/api-criar-ticket.md" in arquivos(palavras=["criar", "ticket"], conexao="pro")
    assert "api/api-criar-ticket.md" not in arquivos(palavras=["criar", "ticket"], conexao="pro", exato=True)
    assert all(it["metodo"] == "DELETE" for it in filtrar(itens, metodo="delete"))
    criar_empresa = "revendedor/api/api-admin-criar-empresa.md"
    assert criar_empresa in arquivos(palavras=["criar", "empresa"])
    assert criar_empresa in arquivos(conexao="admin")
    assert criar_empresa not in arquivos(palavras=["criar", "empresa"], conexao="pro")   # não se mistura às do cliente
    assert "api/api-criar-tag.md" not in arquivos(conexao="admin")
    assert filtrar(itens, palavras=["palavraquenaoexiste"]) == []
    print(f"Autoteste OK: {len(itens) - len(admin)} endpoints do cliente e {len(admin)} administrativos, todos com artigo e linha API.")


def main():
    ap = argparse.ArgumentParser(description="Busca endpoints da API do Chat Master Veloz no índice local.")
    ap.add_argument("palavras", nargs="*", help="palavras que devem aparecer no título, no endereço ou no nome do arquivo (todas)")
    ap.add_argument("--metodo", help="GET, POST, PUT ou DELETE")
    ap.add_argument("--conexao", help="valor da linha API: do artigo (pro, basica, oficial, webchat, instagram, facebook, empresa...); admin lista as APIs administrativas do revendedor")
    ap.add_argument("--exato", action="store_true", help="com --conexao, não inclui os artigos marcados como Todas")
    ap.add_argument("--conexoes", action="store_true", help="lista os valores da linha API: e quantos artigos há de cada")
    ap.add_argument("--autoteste", action="store_true", help="confere o script contra o índice e sai")
    args = ap.parse_args()

    if not (DOCS / "INDICE-api-endpoints.md").exists():
        sys.exit(f"Não achei {DOCS / 'INDICE-api-endpoints.md'}. Rode o script de dentro da pasta da skill.")
    if args.autoteste:
        return autoteste()
    itens = carregar()
    if args.conexoes:
        for api, n in Counter(it["api"] for it in itens).most_common():
            print(f"{n:4d}  {api}")
        return
    if not (args.palavras or args.metodo or args.conexao):
        ap.print_help()
        return
    achados = filtrar(itens, args.palavras, args.metodo, args.conexao, args.exato)
    for it in achados:
        print(f"{it['metodo']:6} [{it['api']}] {it['endereco'].replace(BASE, '')}\n"
              f"       {it['titulo']} -> references/docs/{it['artigo']}")
    if achados:
        print(f"\n{len(achados)} endpoint(s). Abra o artigo e confira o selo **API:** antes de montar o pedido.")
    else:
        print("Nada encontrado: tente outra palavra (sem acento serve) ou veja references/docs/INDICE-api.md.")


if __name__ == "__main__":
    main()
