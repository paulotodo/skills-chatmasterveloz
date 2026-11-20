#!/usr/bin/env python3
"""Busca endpoints da API do Chat Master Veloz por palavra, método e tipo de conexão.

Lê references/docs/INDICE-api-endpoints.md e, para cada artigo, a linha **API:**
(o índice não traz o tipo de conexão; é isso que este script acrescenta a um grep).
Não faz nenhuma chamada de rede.

Uso:
  python3 scripts/buscar_endpoint.py texto                 # palavras no título, endereço ou arquivo
  python3 scripts/buscar_endpoint.py imagem url --conexao oficial
  python3 scripts/buscar_endpoint.py --metodo DELETE
  python3 scripts/buscar_endpoint.py ticket --conexao pro --exato   # não inclui os "Todas"
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
LINHA = re.compile(r"^\| (GET|POST|PUT|DELETE|PATCH) \| `([^`]+)` \| \[(.+)\]\(([^)]+)\) \|$")
BASE = "https://api2.chatmasterveloz.com"


def norm(texto):
    """Minúsculas e sem acento, para 'audio' achar 'Áudio'."""
    sem = unicodedata.normalize("NFD", texto)
    return "".join(c for c in sem if unicodedata.category(c) != "Mn").lower()


def carregar():
    itens = []
    for linha in (DOCS / "INDICE-api-endpoints.md").read_text(encoding="utf-8").splitlines():
        m = LINHA.match(linha)
        if not m:
            continue
        metodo, endereco, titulo, artigo = m.groups()
        api = ""
        caminho = DOCS / artigo
        if caminho.exists():
            achado = re.search(r"^\*\*API:\*\*\s*(.+)$", caminho.read_text(encoding="utf-8"), re.M)
            api = achado.group(1).strip() if achado else ""
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
            if norm(conexao) not in api and (exato or api != "todas"):
                continue
        saida.append(it)
    return saida


def autoteste():
    itens = carregar()
    assert len(itens) == 309, f"esperava 309 endpoints no índice, achei {len(itens)}"
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
    assert filtrar(itens, palavras=["palavraquenaoexiste"]) == []
    print(f"Autoteste OK: {len(itens)} endpoints lidos, todos com artigo e linha API.")


def main():
    ap = argparse.ArgumentParser(description="Busca endpoints da API do Chat Master Veloz no índice local.")
    ap.add_argument("palavras", nargs="*", help="palavras que devem aparecer no título, no endereço ou no nome do arquivo (todas)")
    ap.add_argument("--metodo", help="GET, POST, PUT ou DELETE")
    ap.add_argument("--conexao", help="valor da linha API: do artigo (pro, basica, oficial, webchat, instagram, facebook, empresa...)")
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
