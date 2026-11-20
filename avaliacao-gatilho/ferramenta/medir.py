#!/usr/bin/env python3
"""Mede o acionamento das skills: cada pedido roda N vezes num Claude Code isolado
(sem a configuração pessoal da máquina), com as outras cinco skills instaladas competindo.

Uso:
  python3 medir.py --modelo claude-opus-5-5 --conjunto validacao
  python3 medir.py --modelo claude-sonnet-5-5 --conjunto independentes --skill cmv-api --repeticoes 5

Grava resultados/<skill>__<modelo>__<conjunto>.json e imprime um resumo por skill.
Os scripts em scripts/ são cópias corrigidas do skill-creator (licença em scripts/LICENSE.txt).
"""
import argparse, json, os, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent                      # pasta do projeto (onde fica skills/)
SKILLS = sorted(p.name for p in (RAIZ / "skills").iterdir() if (p / "SKILL.md").exists())


def descricao(skill: str) -> str:
    pasta = RAIZ / "skills" / skill
    linha = next(l for l in (pasta / "SKILL.md").read_text().splitlines() if l.startswith("description:"))
    valor = linha.split(":", 1)[1].strip()
    if valor.startswith('"'):                  # string JSON numa linha só (aspas internas escapadas)
        return json.loads(valor)
    sys.path.insert(0, str(AQUI))
    from scripts.utils import parse_skill_md   # bloco YAML em várias linhas (>-) ou texto cru
    d = parse_skill_md(pasta)[1]
    assert len(d) > 100, f"{skill}: descrição lida com {len(d)} caracteres, formato não reconhecido"
    return d


def medir(skill: str, a) -> dict:
    # bancada: pasta vazia em que só as OUTRAS skills estão instaladas; a skill em teste entra pelo medidor
    bancada = Path(tempfile.mkdtemp(prefix=f"bancada-{skill}-"))
    (bancada / ".claude" / "skills").mkdir(parents=True)
    for outra in SKILLS:
        if outra != skill:
            (bancada / ".claude" / "skills" / outra).symlink_to(RAIZ / "skills" / outra)
    env = dict(os.environ, PYTHONPATH=str(AQUI), TRIGGER_ANY_STEP="0" if a.primeiro_passo else "1")
    saida = subprocess.run(
        [sys.executable, "-m", "scripts.run_eval",
         "--eval-set", str(AQUI.parent / a.conjunto / f"{skill}.json"),
         "--skill-path", str(RAIZ / "skills" / skill),
         "--description", a.descricao or descricao(skill),
         "--runs-per-query", str(a.repeticoes), "--num-workers", str(a.paralelo),
         "--timeout", "120", "--model", a.modelo],
        cwd=bancada, env=env, capture_output=True, text=True)
    shutil.rmtree(bancada, ignore_errors=True)   # só links e cópias temporárias; não toca nas skills
    if saida.returncode != 0:
        raise RuntimeError(f"{skill}: medidor falhou\n{saida.stderr[-2000:]}")
    r = json.loads(saida.stdout)
    r["modelo"], r["conjunto"], r["modo"] = a.modelo, a.conjunto, "primeiro passo" if a.primeiro_passo else "sessão inteira"
    destino = Path(a.saida) / f"{skill}__{a.modelo}__{a.conjunto}{a.sufixo}.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(r, ensure_ascii=False, indent=2))
    return r


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--modelo", required=True)
    p.add_argument("--conjunto", required=True, help="pasta com os pedidos: otimizacao, validacao ou independentes")
    p.add_argument("--skill", action="append", help="mede só esta skill (pode repetir); padrão: todas")
    p.add_argument("--repeticoes", type=int, default=3)
    p.add_argument("--paralelo", type=int, default=4, help="execuções simultâneas por skill")
    p.add_argument("--descricao", help="texto alternativo a testar no lugar da descrição do SKILL.md (use com --skill)")
    p.add_argument("--sufixo", default="", help="acrescentado ao nome do arquivo de resultado")
    p.add_argument("--saida", default=str(AQUI.parent / "resultados"))
    p.add_argument("--primeiro-passo", action="store_true",
                   help="conta só a primeira ação do modelo, como o medidor original (padrão: acompanha a sessão)")
    a = p.parse_args()
    alvo = a.skill or SKILLS
    assert not (a.descricao and len(alvo) != 1), "--descricao exige exatamente uma --skill"
    with ThreadPoolExecutor(len(alvo)) as ex:
        for skill, r in zip(alvo, ex.map(lambda s: medir(s, a), alvo)):
            certos = [x for x in r["results"] if x["should_trigger"]]
            indev = [x for x in r["results"] if not x["should_trigger"]]
            print(f'{skill:20} {a.modelo:18} {a.conjunto:14} acertos {r["summary"]["passed"]}/{r["summary"]["total"]}'
                  f' | acionou quando devia {sum(x["triggers"] for x in certos)}/{sum(x["runs"] for x in certos)}'
                  f' | acionou sem dever {sum(x["triggers"] for x in indev)}/{sum(x["runs"] for x in indev)}', flush=True)
            for x in r["results"]:
                if not x["pass"]:
                    print(f'    FALHA ({x["triggers"]}/{x["runs"]}, devia {"acionar" if x["should_trigger"] else "não acionar"}): {x["query"][:110]}', flush=True)


if __name__ == "__main__":
    main()
