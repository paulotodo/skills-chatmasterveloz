#!/bin/bash
# Atualiza a cópia da documentação oficial dentro das skills, confere e registra no git.
# Feito para rodar pelo cron: não imprime nada; o que aconteceu fica em atualizacoes.log.
# Se qualquer etapa falhar, tudo volta ao estado anterior e o motivo vai para o log.
#
# Uso: ./atualizar.sh
set -u
cd "$(dirname "$(readlink -f "$0")")" || exit 1
RAIZ=$PWD
FONTES=("$RAIZ/../docs-plataforma-chatmasterveloz" "$RAIZ/../docs-css-chatmasterveloz")
LOG=$RAIZ/atualizacoes.log
diz() { echo "$(date '+%F %T') $*" >> "$LOG"; }

exec 9> "$RAIZ/.atualizar.lock"
flock -n 9 || exit 0                       # outra atualização em andamento

# alteração feita à mão e não registrada seria misturada (ou desfeita) pela atualização
if [ -n "$(git status --porcelain)" ]; then
  diz "PULADO: há alterações não registradas no git. Registre (git commit) ou desfaça, e rode de novo."
  exit 1
fi

COPIA=$(mktemp -d)
trap 'rm -rf "$COPIA"' EXIT
for f in "${FONTES[@]}"; do cp -a "$f" "$COPIA/" || { diz "FALHOU: não consegui copiar $f"; exit 1; }; done
antes=$(find "${FONTES[0]}" -name '*.md' | wc -l)

desfazer() {
  for f in "${FONTES[@]}"; do rm -rf "$f" && cp -a "$COPIA/$(basename "$f")" "$f"; done
  git checkout -q -- . && git clean -qfd skills
  diz "FALHOU: $1. Nada mudou. Fim da saída: $(tail -c 500 "$COPIA/saida.txt" 2>/dev/null | tr '\n' ' ')"
  exit 1
}
roda() { "$@" >> "$COPIA/saida.txt" 2>&1; }

roda python3 "${FONTES[0]}/_gerar.py" || desfazer "não consegui baixar a Central de Ajuda"
roda python3 "${FONTES[1]}/_gerar.py" || desfazer "não consegui baixar o catálogo de CSS"
depois=$(find "${FONTES[0]}" -name '*.md' | wc -l)
# os geradores apagam o que saiu do site; uma queda grande é sinal de download incompleto
[ "$depois" -ge $((antes * 9 / 10)) ] || desfazer "a Central de Ajuda baixada encolheu de $antes para $depois artigos"

roda python3 montar.py || desfazer "um arquivo escrito à mão cita um artigo que mudou de nome ou saiu do ar"
for teste in "skills/cmv-flowbuilder/scripts/gerar_fluxo.py --teste" \
             "skills/cmv-flowbuilder/scripts/validar_fluxo.py --teste" \
             "skills/cmv-agente-ia/scripts/conferir_prompt.py --autoteste" \
             "skills/cmv-api/scripts/buscar_endpoint.py --autoteste" \
             "skills/cmv-painel-css-js/scripts/conferir_seletores.py --teste" \
             "skills/cmv-painel-css-js/scripts/conferir_seletores.py skills/cmv-painel-css-js/references/receitas.md"; do
  # shellcheck disable=SC2086
  roda python3 $teste || desfazer "a conferência falhou com a documentação nova: $teste"
done

if [ -z "$(git status --porcelain)" ]; then
  diz "sem mudanças na documentação"
  exit 0
fi

roda python3 montar.py --zip || desfazer "não consegui refazer os pacotes"
git add -A
# a ajuda leva a Central inteira; conta os artigos por ela para não somar as cópias das outras skills
mudancas=$(git diff --cached --name-status -- skills/cmv-ajuda/references/docs skills/cmv-painel-css-js/references/docs)
novos=$(echo "$mudancas" | grep -c '^A'); alterados=$(echo "$mudancas" | grep -c '^M'); removidos=$(echo "$mudancas" | grep -c '^D')
nomes=$(echo "$mudancas" | grep '^[AD]' | sed 's#\t.*/#\t#; s#\.md$##' | tr '\t' ' ' | head -25 | paste -sd ';' -)
git commit -q -m "Atualização automática da documentação" \
  -m "$novos artigos novos, $alterados alterados, $removidos removidos (A = novo, D = removido): ${nomes:-nenhum novo ou removido}" \
  || desfazer "não consegui registrar no git"
diz "ATUALIZADO: $novos artigos novos, $alterados alterados, $removidos removidos. ${nomes:+Novos (A) e removidos (D): $nomes. }Pacotes refeitos em dist/. Artigo novo pode pedir revisão dos mapas escritos à mão (references/*.md de cada skill)."
# quem instalou pelo marketplace recebe pelo git; sem remoto configurado, não há o que publicar
if git remote | grep -q .; then
  git push -q 2>>"$LOG" || diz "AVISO: a documentação foi atualizada aqui, mas não consegui publicar (git push)."
fi
