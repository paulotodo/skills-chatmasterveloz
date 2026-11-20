#!/usr/bin/env python3
"""Gera ../REVISAO-ROTEAMENTO.md: os pedidos de roteamento numerados, para uma pessoa revisar
respondendo pelo chat com o número do pedido. Texto puro, sem botões: abre em qualquer leitor.
Lê roteamento/{teste,desenvolvimento}.json e resultados/roteamento__<modelo>__<conjunto>-depois.json."""
import json
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
NOMES = {"claude-opus-5-5": "Opus", "claude-fable-5-2": "Fable", "claude-sonnet-5-5": "Sonnet", "claude-haiku-5-5": "Haiku"}
QUEM = {  # o que cada destino entrega, em palavras de quem usa
    "cmv-ajuda": "Ajuda (explica como usar ou configurar algo na tela)",
    "cmv-api": "API (entrega o código da integração)",
    "cmv-flowbuilder": "FlowBuilder (monta ou conserta o fluxo do robô)",
    "cmv-agente-ia": "Agente de IA (prompt e configuração da IA)",
    "cmv-mensagens": "Mensagens (escreve o texto pronto)",
    "cmv-painel-css-js": "CSS/JS (muda o visual do painel com código)",
    "nenhuma": "Nenhuma (não é assunto do Chat Master Veloz)",
}
curto = lambda d: QUEM[d].split(" (")[0]

itens = []
for conjunto in ["teste", "desenvolvimento"]:
    for q in json.loads((BASE / "roteamento" / f"{conjunto}.json").read_text()):
        falhou, visto = [], []
        for mid, nome in NOMES.items():
            arq = BASE / "resultados" / f"roteamento__{mid}__{conjunto}-depois.json"
            if not arq.exists():
                continue
            r = next(x for x in json.loads(arq.read_text())["resultados"] if x["id"] == q["id"])
            c = Counter(" + ".join(curto(s) for s in g) or "nenhuma skill" for g in r["cargas"])
            visto.append(f"{nome}: " + ", ".join(f"{k} {v}/{r['repeticoes']}" for k, v in c.most_common()))
            if not r["passou"]:
                falhou.append(nome)
        itens.append({**q, "falhou": falhou, "visto": visto})

parte_a = [q for q in itens if q["aceitavel"]]
parte_b = [q for q in itens if q["falhou"] and not q["aceitavel"]]
resto = [q for q in itens if not q["aceitavel"] and not q["falhou"]]
num = {q["id"]: i for i, q in enumerate(parte_a + parte_b + resto, 1)}
cita = lambda q: "> " + q["pedido"].replace("\n", "\n> ")

L = ["# Revisão dos pedidos de roteamento", "",
     "Estes pedidos medem se o Claude escolhe a skill certa. Para revisar, **responda pelo chat com o número do pedido**, "
     "só onde você discordar ou tiver algo a dizer. Exemplos de resposta: `3: deveria ser Mensagens`, "
     "`7: ninguém escreve assim`, `12: ok`. O que você não citar fica como está.", "",
     "O mais útil que você pode mandar, além disso: **mensagens reais** que seus clientes ou sua equipe já escreveram "
     "pedindo ajuda, coladas no chat do jeito que foram escritas (sem nomes nem telefones).", "",
     "## Quem atende o quê", ""] + [f"- **{v.split(' (')[0]}:** {v.split(' (')[1][:-1]}" for v in QUEM.values()] + [""]

L += [f"## Parte A: {len(parte_a)} pedidos em que duas respostas são aceitas", "",
      "Os anotadores consideraram os dois destinos defensáveis. Se para você só um faz sentido, diga qual.", ""]
for q in parte_a:
    L += [f"### {num[q['id']]}", cita(q), "",
          f"- **Aceito hoje:** {curto(q['destino'])} ou {' ou '.join(curto(a) for a in q['aceitavel'])}",
          f"- **Por quê:** {q['motivo']}", ""]

L += [f"## Parte B: {len(parte_b)} pedidos em que algum modelo não carregou a skill esperada", "",
      "Aqui o destino não está em dúvida. Só diga se o pedido parece com o que seus usuários escrevem, "
      "ou se o destino está errado.", ""]
for q in parte_b:
    L += [f"### {num[q['id']]}", cita(q), "",
          f"- **Deveria atender:** {curto(q['destino'])}",
          f"- **Falhou em:** {', '.join(q['falhou'])} ({'; '.join(v for v in q['visto'] if v.split(':')[0] in q['falhou'])})", ""]

L += [f"## Parte C: os outros {len(resto)} pedidos", "",
      "Leitura opcional: todos os modelos medidos carregaram o destino esperado.", ""]
for d in QUEM:
    grupo = [q for q in resto if q["destino"] == d]
    if grupo:
        L += [f"### {curto(d)}", "", "| # | Pedido |", "|---|---|"]
        L += [f"| {num[q['id']]} | {q['pedido'].replace('|', '/').replace(chr(10), ' ')} |" for q in grupo] + [""]

(BASE / "REVISAO-ROTEAMENTO.md").write_text("\n".join(L))
json.dump({str(n): i for i, n in num.items()}, open(BASE / "roteamento" / "numeros-da-revisao.json", "w"), indent=0)
print(f"REVISAO-ROTEAMENTO.md: {len(itens)} pedidos (A {len(parte_a)}, B {len(parte_b)}, C {len(resto)})")
