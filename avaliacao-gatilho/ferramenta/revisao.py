#!/usr/bin/env python3
"""Gera ../REVISAO.md: todos os pedidos de teste, o rótulo esperado e quantas vezes cada
modelo acionou a skill, para uma pessoa revisar os pedidos e os rótulos.
Lê os resultados gravados pelo medir.py (resultados/<skill>__<modelo>__<conjunto>.json)."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CONJUNTOS = [("otimizacao", "usados para otimizar a descrição"),
             ("validacao", "nunca vistos pelo otimizador"),
             ("independentes", "escritos por um agente que não viu os outros pedidos nem as descrições")]
NOMES = {"claude-opus-5-5": "Opus 5.5", "claude-fable-5-2": "Fable 5.2",
         "claude-sonnet-5-5": "Sonnet 5.5", "claude-haiku-5-5": "Haiku 5.5"}

res = {}  # (skill, conjunto, pedido) -> {modelo: resultado}
for arq in (BASE / "resultados").glob("cmv-*__claude-*__*.json"):
    skill, modelo, conjunto = arq.stem.split("__")
    for r in json.loads(arq.read_text())["results"]:
        res.setdefault((skill, conjunto, r["query"]), {})[modelo] = r
modelos = [m for m in NOMES if any(m in v for v in res.values())]

L = ["# Revisão dos pedidos de teste", "",
     "Cada linha é um pedido usado para medir o acionamento. **Esperado** diz se a skill da seção deve ser "
     "carregada. As colunas dos modelos mostram em quantas das repetições ela foi carregada; ❌ marca o "
     "resultado que contraria o esperado (acionou em menos da metade quando devia, ou na metade ou mais "
     "quando não devia). Um traço significa que o conjunto não foi medido naquele modelo.", "",
     "O que revisar: (1) o rótulo **Esperado** está certo? (2) o pedido parece com o que seus usuários "
     "escrevem? (3) falta algum tipo de pedido? Para corrigir, edite o arquivo `.json` do conjunto e rode "
     "`ferramenta/medir.py` de novo.", ""]
for skill in sorted({k[0] for k in res}):
    L += [f"## {skill}", ""]
    for conjunto, nota in CONJUNTOS:
        arq = BASE / conjunto / f"{skill}.json"
        if not arq.exists():
            continue
        L += [f"### `{conjunto}/{skill}.json` ({nota})", "",
              "| # | Pedido | Esperado | " + " | ".join(NOMES[m] for m in modelos) + " |",
              "|---|---|---|" + "---|" * len(modelos)]
        for i, q in enumerate(json.loads(arq.read_text()), 1):
            cel = []
            for m in modelos:
                r = res.get((skill, conjunto, q["query"]), {}).get(m)
                cel.append("–" if not r else f'{r["triggers"]}/{r["runs"]}' + ("" if r["pass"] else " ❌"))
            pedido = q["query"].replace("|", "\\|").replace("\n", " ")
            L.append(f'| {i} | {pedido} | {"aciona" if q["should_trigger"] else "não aciona"} | ' + " | ".join(cel) + " |")
        L.append("")
(BASE / "REVISAO.md").write_text("\n".join(L))
print(f"REVISAO.md: {len(res)} pedidos, modelos: {', '.join(NOMES[m] for m in modelos)}")
