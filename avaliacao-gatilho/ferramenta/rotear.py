#!/usr/bin/env python3
"""Mede o ROTEAMENTO: com as seis skills instaladas de verdade (o SKILL.md real, não uma cópia),
roda cada pedido N vezes num Claude Code isolado e registra QUAL skill foi carregada.
Uma execução responde pelas seis skills ao mesmo tempo.

Cada pedido do conjunto tem: id, pedido, destino (uma skill ou "nenhuma") e aceitavel (outros
destinos também corretos). Com destino "qualquer", o campo nao lista as skills que não podem carregar. Uma repetição acerta quando carrega o destino ou um aceitável (ou nada,
se o destino é "nenhuma"); o pedido passa quando acerta em mais da metade das repetições.

Uso:
  python3 rotear.py --modelo claude-opus-5-5 --conjunto ../roteamento/teste.json
  python3 rotear.py --autoteste
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile, threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
SKILLS = sorted(p.name for p in (RAIZ / "skills").iterdir() if (p / "SKILL.md").exists())
ACHA = re.compile("(" + "|".join(sorted(SKILLS, key=len, reverse=True)) + r")(?![a-z-])")


class Leitor:
    """Recebe os eventos do stream-json e devolve None enquanto não há veredito; depois, a lista de
    skills carregadas na primeira mensagem que carregou alguma ([] se o turno terminou sem carregar)."""

    def __init__(self):
        self.ferramenta, self.entrada, self.cargas, self.outras, self.motivo_parada = None, "", [], 0, None

    def evento(self, ev):
        if ev.get("type") == "result":
            return self.cargas
        if ev.get("type") != "stream_event" or ev.get("parent_tool_use_id"):
            return None
        se = ev.get("event", {}); t = se.get("type")
        if t == "content_block_start" and se.get("content_block", {}).get("type") == "tool_use":
            self.ferramenta, self.entrada = se["content_block"].get("name", ""), ""
        elif t == "content_block_delta" and se.get("delta", {}).get("type") == "input_json_delta":
            self.entrada += se["delta"].get("partial_json", "")
        elif t == "content_block_stop" and self.ferramenta:
            if self.ferramenta in ("Skill", "Read"):
                self.cargas += [s for s in ACHA.findall(self.entrada) if s not in self.cargas]
            else:
                self.outras += 1
            self.ferramenta = None
        elif t == "message_delta":
            self.motivo_parada = se.get("delta", {}).get("stop_reason") or self.motivo_parada
        elif t == "message_stop":
            # shortcut: desiste depois de 8 ferramentas sem carregar skill; aumente se as skills passarem a carregar mais tarde
            if self.cargas or self.motivo_parada != "tool_use" or self.outras > 8:
                return self.cargas
            self.motivo_parada = None
        return None


EXTRA = []   # opções a mais para o claude -p (--plugin-dir, no modo --plugin)


class FalhaDeExecucao(Exception):
    pass


def uma_execucao(pedido, modelo, bancada, limite=150, tentativas=3):
    # limite de uso ou erro da API terminam a sessão sem carregar nada; sem isto, contariam como "não carregou"
    for n in range(tentativas):
        try:
            return _uma_execucao(pedido, modelo, bancada, limite)
        except FalhaDeExecucao as e:
            if n == tentativas - 1:
                raise RuntimeError(f"sessão de teste falhou {tentativas} vezes: {e}") from None
            threading.Event().wait(20 * (n + 1))


def _uma_execucao(pedido, modelo, bancada, limite):
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    proc = subprocess.Popen(
        ["claude", "-p", pedido, "--output-format", "stream-json", "--verbose", "--include-partial-messages",
         "--setting-sources", "project", "--strict-mcp-config", "--model", modelo, *EXTRA],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd=bancada, env=env, text=True)
    relogio = threading.Timer(limite, proc.kill); relogio.start()
    leitor, veredito, instaladas = Leitor(), None, None
    try:
        for linha in proc.stdout:
            try:
                ev = json.loads(linha)
            except json.JSONDecodeError:
                continue
            if ev.get("type") == "system" and ev.get("subtype") == "init":
                instaladas = [s for s in SKILLS if s in json.dumps(ev)]
            if ev.get("type") == "result" and (ev.get("is_error") or ev.get("subtype") not in (None, "success")):
                raise FalhaDeExecucao(str(ev.get("result") or ev.get("subtype"))[:200])
            veredito = leitor.evento(ev)
            if veredito is not None:
                break
    finally:
        relogio.cancel(); proc.kill(); proc.wait()
    if instaladas is not None and len(instaladas) != len(SKILLS):
        raise RuntimeError(f"a sessão de teste só enxergou {instaladas}; esperava as {len(SKILLS)} skills")
    if veredito is None and instaladas is None:
        raise FalhaDeExecucao("a sessão terminou sem nenhum evento")
    return leitor.cargas if veredito is None else veredito   # None = tempo esgotado: vale o que carregou até ali


def acertou(cargas, destino, aceitavel, nao=()):
    if destino == "qualquer":   # pedido que só diz o que NÃO pode carregar (campo "nao")
        return not set(cargas) & set(nao)
    certos = {destino, *aceitavel}
    if not cargas:
        return "nenhuma" in certos
    return bool(set(cargas) & certos)


def autoteste():
    def roda(passos):
        l = Leitor()
        for ev in passos:
            r = l.evento({"type": "stream_event", "event": ev})
            if r is not None:
                return r
        return "sem veredito"
    ini = lambda n: {"type": "content_block_start", "content_block": {"type": "tool_use", "name": n}}
    arg = lambda s: {"type": "content_block_delta", "delta": {"type": "input_json_delta", "partial_json": s}}
    fim, para = {"type": "content_block_stop"}, {"type": "message_stop"}
    motivo = lambda m: {"type": "message_delta", "delta": {"stop_reason": m}}
    a, b = SKILLS[0], SKILLS[1]
    assert roda([ini("Skill"), arg('{"skill": "%s"}' % a), fim, motivo("tool_use"), para]) == [a]
    assert roda([ini("Bash"), arg('{"command": "ls"}'), fim, motivo("tool_use"), para,
                 ini("Skill"), arg('{"skill": "%s"}' % b), fim, motivo("tool_use"), para]) == [b], "olhar a pasta antes não pode esconder a carga"
    assert roda([ini("Skill"), arg('{"skill": "%s"}' % a), fim, ini("Skill"), arg('{"skill": "%s"}' % b), fim,
                 motivo("tool_use"), para]) == [a, b], "duas skills na mesma mensagem"
    assert roda([motivo("end_turn"), para]) == [], "respondeu sem carregar nada"
    assert roda([ini("Read"), arg('{"file_path": "/x/.claude/skills/%s/SKILL.md"}' % a), fim, motivo("tool_use"), para]) == [a]
    assert "cmv-api" not in ACHA.findall("cmv-apisemelhante") or "cmv-api" not in SKILLS
    assert acertou([], "nenhuma", []) and not acertou([a], "nenhuma", []) and acertou([a], b, [a]) and not acertou([], a, [])
    assert acertou([b], "qualquer", [], [a]) and acertou([], "qualquer", [], [a]) and not acertou([a, b], "qualquer", [], [a])
    print("autoteste ok")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--modelo"); p.add_argument("--conjunto")
    p.add_argument("--repeticoes", type=int, default=3)
    p.add_argument("--paralelo", type=int, default=16)
    p.add_argument("--saida", default=str(AQUI.parent / "resultados"))
    p.add_argument("--skills", default=str(RAIZ / "skills"), help="pasta com as seis skills (para testar uma versão candidata sem tocar nas oficiais)")
    p.add_argument("--plugin", action="store_true", help="instala como plugin (--plugin-dir na raiz do projeto) em vez de copiar as skills para o projeto de teste")
    p.add_argument("--contexto", help="texto gravado como CLAUDE.md do projeto de teste (simula instruções fixas do usuário)")
    p.add_argument("--sufixo", default="", help="acrescentado ao nome do arquivo de resultado")
    p.add_argument("--autoteste", action="store_true")
    a = p.parse_args()
    if a.autoteste:
        return autoteste()
    assert a.modelo and a.conjunto, "informe --modelo e --conjunto"
    itens = json.loads(Path(a.conjunto).read_text())
    bancada = Path(tempfile.mkdtemp(prefix="bancada-roteamento-"))
    (bancada / ".claude" / "skills").mkdir(parents=True)
    if a.plugin:
        EXTRA.extend(["--plugin-dir", str(RAIZ.parent)])
    else:
        for s in SKILLS:
            (bancada / ".claude" / "skills" / s).symlink_to(Path(a.skills).resolve() / s)
    if a.contexto:
        (bancada / "CLAUDE.md").write_text(a.contexto + "\n")
    try:
        with ThreadPoolExecutor(a.paralelo) as ex:
            futuros = [(q, [ex.submit(uma_execucao, q["pedido"], a.modelo, bancada) for _ in range(a.repeticoes)]) for q in itens]
            res = []
            for q, fs in futuros:
                cargas = [f.result() for f in fs]
                ok = sum(acertou(c, q["destino"], q.get("aceitavel", []), q.get("nao", [])) for c in cargas)
                res.append({**q, "cargas": cargas, "acertos": ok, "repeticoes": a.repeticoes, "passou": ok * 2 > a.repeticoes})
    finally:
        shutil.rmtree(bancada, ignore_errors=True)   # só links; não toca nas skills
    nome = Path(a.conjunto).stem
    destino = Path(a.saida) / f"roteamento__{a.modelo}__{nome}{a.sufixo}.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps({"modelo": a.modelo, "conjunto": nome, "resultados": res}, ensure_ascii=False, indent=2))

    print(f"{a.modelo} · {nome}: {sum(r['passou'] for r in res)}/{len(res)} pedidos certos")
    por = Counter(); tot = Counter()
    for r in res:
        tot[r["destino"]] += 1; por[r["destino"]] += r["passou"]
    print("  por destino: " + " · ".join(f"{d.replace('cmv-', '')} {por[d]}/{tot[d]}" for d in sorted(tot)))
    # carga a mais: a repetição acertou, mas carregou junto uma skill que não é destino nem aceitável
    certos = lambda r: {r["destino"], *r.get("aceitavel", [])}
    a_mais = [(r, sum(1 for c in r["cargas"] if r["destino"] != "qualquer" and set(c) - certos(r) and set(c) & certos(r))) for r in res]
    print(f"  cargas a mais: {sum(n for _, n in a_mais)} repetições em {sum(1 for _, n in a_mais if n)} pedidos"
          + "".join(f"\n    {r['id']} ({n}/{r['repeticoes']}): {sorted({x for c in r['cargas'] for x in c} - certos(r))}" for r, n in a_mais if n))
    for r in res:
        if not r["passou"]:
            vistos = Counter("+".join(c) or "nada" for c in r["cargas"])
            print(f"  ERRO {r['id']} devia {r['destino']}, carregou {dict(vistos)}: {r['pedido'][:100]!r}")


if __name__ == "__main__":
    main()
