#!/usr/bin/env python3
"""Roda tarefas completas (não só o acionamento) com as seis skills instaladas como cópias reais,
num Claude Code isolado, e guarda a resposta, as ferramentas usadas e os arquivos criados.
Serve para ver se a skill entrega nos modelos menores. A nota é dada depois, por leitura.

Uso: python3 ponta_a_ponta.py --modelo claude-haiku-5-5 --tarefas tarefas.json --saida pasta
tarefas.json: [{"id": "flowbuilder", "pedido": "...", "skill": "cmv-flowbuilder"}]
Campo opcional "contexto": texto gravado como CLAUDE.md da pasta (instruções fixas do projeto).
Campo opcional "arquivos": {"nome-na-pasta-de-trabalho": "caminho relativo ao tarefas.json"} põe arquivos do usuário na pasta.
"""
import argparse, json, os, shutil, subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent / "skills"
# só o que as skills precisam: ler, escrever na pasta de teste e rodar os scripts delas
PERMITIDAS = ["Skill", "Read", "Write", "Edit", "Glob", "Grep",
              "Bash(python3:*)", "Bash(ls:*)", "Bash(cat:*)", "Bash(grep:*)", "Bash(mkdir:*)", "Bash(cp:*)", "Bash(head:*)", "Bash(wc:*)"]


def rodar(tarefa, modelo, saida, limite, base):
    pasta = Path(saida) / modelo / tarefa["id"]
    if pasta.exists():
        shutil.rmtree(pasta)
    (pasta / ".claude").mkdir(parents=True)
    # cópia real, não link: num link para fora da pasta a sessão não consegue ler references/
    shutil.copytree(RAIZ, pasta / ".claude" / "skills", ignore=shutil.ignore_patterns("__pycache__", "fontes.txt"))
    dados = set()
    if tarefa.get("contexto"):   # instruções fixas do projeto, como a linha que o README recomenda
        (pasta / "CLAUDE.md").write_text(tarefa["contexto"] + "\n"); dados.add("CLAUDE.md")
    for nome, origem in tarefa.get("arquivos", {}).items():
        shutil.copyfile(base / origem, pasta / nome); dados.add(nome)
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        r = subprocess.run(["claude", "-p", tarefa["pedido"], "--model", modelo, "--output-format", "stream-json", "--verbose",
                            "--setting-sources", "project", "--strict-mcp-config", "--permission-mode", "acceptEdits",
                            "--allowedTools", *PERMITIDAS],
                           cwd=pasta, env=env, capture_output=True, text=True, timeout=limite)
        bruto, estourou = r.stdout, False
    except subprocess.TimeoutExpired as e:
        bruto, estourou = (e.stdout.decode() if isinstance(e.stdout, bytes) else e.stdout or ""), True
    passos, final, negadas, custo = [], "", 0, None
    for linha in bruto.splitlines():
        try:
            ev = json.loads(linha)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            for c in ev["message"].get("content", []):
                if c.get("type") == "tool_use":
                    passos.append(c["name"] + " " + json.dumps(c.get("input", {}), ensure_ascii=False)[:160])
        elif ev.get("type") == "user":
            for c in ev.get("message", {}).get("content", []) if isinstance(ev.get("message", {}).get("content"), list) else []:
                if c.get("type") == "tool_result" and c.get("is_error") and "permission" in json.dumps(c.get("content", "")).lower():
                    negadas += 1
        elif ev.get("type") == "result":
            final, custo = ev.get("result") or "", {"turnos": ev.get("num_turns"), "segundos": round((ev.get("duration_ms") or 0) / 1000)}
    (pasta / "resposta.md").write_text(final)
    carregadas = sorted({s for p in passos if p.startswith(("Skill", "Read")) for s in os.listdir(RAIZ) if s in p})
    resumo = {"id": tarefa["id"], "modelo": modelo, "pedido": tarefa["pedido"], "skill_esperada": tarefa["skill"],
              "skills_carregadas": carregadas, "tempo_esgotado": estourou, "comandos_negados": negadas, "custo": custo, "passos": passos,
              "arquivos_criados": sorted(str(f.relative_to(pasta)) for f in pasta.rglob("*")
                                         if f.is_file() and ".claude" not in f.parts and f.name not in ("resposta.md", "resumo.json") and f.name not in dados)}
    (pasta / "resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=1))
    return resumo


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--modelo", required=True); p.add_argument("--tarefas", required=True); p.add_argument("--saida", required=True)
    p.add_argument("--limite", type=int, default=900, help="segundos por tarefa")
    a = p.parse_args()
    tarefas = json.loads(Path(a.tarefas).read_text())
    with ThreadPoolExecutor(len(tarefas)) as ex:
        for r in ex.map(lambda t: rodar(t, a.modelo, a.saida, a.limite, Path(a.tarefas).resolve().parent), tarefas):
            print(f'{r["modelo"]} · {r["id"]}: carregou {r["skills_carregadas"] or "nenhuma"} · {len(r["passos"])} passos · '
                  f'{r["custo"]} · arquivos {r["arquivos_criados"]} · negados {r["comandos_negados"]}' + (" · TEMPO ESGOTADO" if r["tempo_esgotado"] else ""), flush=True)


if __name__ == "__main__":
    main()
