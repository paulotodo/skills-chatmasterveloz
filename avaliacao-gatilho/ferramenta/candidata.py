#!/usr/bin/env python3
"""Monta uma cópia das seis skills com descrições candidatas, para medir com
`rotear.py --skills <pasta>` sem tocar nas skills oficiais.

Uso:
  python3 candidata.py descricoes.json pasta-de-saida          # monta a cópia
  python3 candidata.py descricoes.json --aplicar               # grava nas skills oficiais

descricoes.json: {"cmv-ajuda": "nova descrição", ...}; skill que não aparece fica como está.
A cópia tem o SKILL.md reescrito e links para o resto (references, scripts, assets).
"""
import json, re, shutil, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent / "skills"
LIMITE = 1024


def com_descricao(texto: str, descricao: str) -> str:
    """Troca o valor de `description` do frontmatter por uma string JSON numa linha só."""
    m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    saida, pulando = [], False
    for linha in m[1].split("\n"):
        if linha.startswith("description:"):
            saida.append("description: " + json.dumps(descricao, ensure_ascii=False)); pulando = True
        elif pulando and (linha.startswith(" ") or linha == ""):
            continue   # linhas de continuação de um bloco em várias linhas (>-)
        else:
            saida.append(linha); pulando = False
    return "---\n" + "\n".join(saida) + "\n---\n" + texto[m.end():]


def conferir(skill: str, d: str):
    assert (RAIZ / skill / "SKILL.md").exists(), f"skill desconhecida: {skill}"
    assert len(d.encode()) <= LIMITE, f"{skill}: {len(d)} caracteres / {len(d.encode())} bytes, limite {LIMITE}"
    assert "<" not in d and ">" not in d and "\n" not in d, f"{skill}: a descrição não pode ter < > nem quebra de linha"


def main():
    novas = json.loads(Path(sys.argv[1]).read_text())
    for skill, d in novas.items():
        conferir(skill, d)
    if sys.argv[2] == "--aplicar":
        for skill, d in novas.items():
            p = RAIZ / skill / "SKILL.md"
            p.write_text(com_descricao(p.read_text(), d))
            print(f"{skill}: gravada ({len(d)} caracteres)")
        return
    destino = Path(sys.argv[2])
    if destino.exists():
        shutil.rmtree(destino)
    for pasta in sorted(p for p in RAIZ.iterdir() if (p / "SKILL.md").exists()):
        nova = destino / pasta.name; nova.mkdir(parents=True)
        for item in pasta.iterdir():
            if item.name != "SKILL.md":
                (nova / item.name).symlink_to(item)
        texto = (pasta / "SKILL.md").read_text()
        (nova / "SKILL.md").write_text(com_descricao(texto, novas[pasta.name]) if pasta.name in novas else texto)
    print(f"{destino}: {len(novas)} descrições trocadas ({', '.join(f'{s} {len(d)}' for s, d in novas.items())})")


if __name__ == "__main__":
    # autoteste mínimo: a troca preserva o corpo e o nome, e o valor volta igual
    t = '---\nname: x\ndescription: >-\n  linha um\n  linha dois\n---\ncorpo: "a"\n'
    r = com_descricao(t, 'nova "com aspas": ok')
    assert r == '---\nname: x\ndescription: "nova \\"com aspas\\": ok"\n---\ncorpo: "a"\n', r
    main()
