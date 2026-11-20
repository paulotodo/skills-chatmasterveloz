# Chat Master Veloz — referência de CSS e JS personalizados

Referência para agentes que escrevem CSS e JS de customização do painel `app.chatmasterveloz.com`.

- **Fonte:** <https://app.chatmasterveloz.com/css-docs>, que lê tudo de <https://app.chatmasterveloz.com/catalogo-css/pt.json>
- **Versão do catálogo:** a que aparece no cabeçalho de cada arquivo gerado (`versão WS-…`); muda a cada atualização da plataforma
- **Conteúdo:** páginas, modais, âncoras específicas, classes sem prefixo, atributos `data-*` e o Chat Externo; as contagens atuais estão no `01-fundamentos.md`
- **Cópia bruta do catálogo:** `catalogo-css.pt.json`
- **Para atualizar:** `python3 _gerar.py` baixa a versão atual e regenera os arquivos numerados (menos este e o `02`).

## Não leia tudo: busque

São cerca de 460 KB. Leia `01` e `02` inteiros (são curtos) e use `grep` nos demais.

| Preciso de… | Arquivo | Como achar |
|---|---|---|
| regras básicas e convenções de nome | `01-fundamentos.md` | ler inteiro |
| em que campo escrever, ordem de carga, regras do JS | `02-campos-css-js.md` | ler inteiro |
| variáveis CSS que mudam comportamento (ordem do menu, ações do ticket…) | `03-propriedades-css.md` | `grep -n -- '--nome'` |
| cores e variáveis do tema escuro (`--mui-*`) | `04-tema-escuro.md` | ler inteiro |
| eventos que o JS pode ouvir | `05-eventos-js.md` | ler inteiro |
| um atributo de estado `data-*`: onde existe e que valores tem | `06-atributos-data.md` | `grep -n -A3 '^### .data-status.'` |
| o id de uma tela (`#custom-css-<página>`) | `07-paginas.md` | `grep -n palavra` |
| a classe de uma janela (`.custom-css-modal-<nome>`) | `08-modais.md` | `grep -n palavra` |
| as âncoras de uma área/componente | `09-ancoras-por-area.md` | `grep -n -A2 '^### .Nome'` |
| em que área uma classe aparece, ou classes por palavra | `10-ancoras-indice-az.md` | `grep -n palavra` (uma classe por linha) |
| classes antigas do chat sem `custom-css-` (`.ticket-name`, `.message-quoted`…) | `11-classes-sem-prefixo.md` | ler inteiro |
| a página pública do Chat Externo (Modo Alternativo) | `12-chat-externo.md` | ler inteiro |
| o que mudou em cada versão (um seletor parou de funcionar?) | `13-historico.md` | `grep -n seletor` |
| as URLs do painel, para `location.pathname` | `14-rotas.md` | `grep -n palavra` |

Buscar em tudo de uma vez: `grep -rn 'termo' --include='*.md' .`

Os nomes misturam português e inglês (`ticket`, `quadro`, `funil`, `kanban`, `contact`, `contato`). Se a primeira busca não achar, tente o outro idioma.

## As regras que valem sempre

1. Selecione por `custom-css-*` e por `data-*`. Nunca por `.Mui*` ou `.jss123`: mudam a cada atualização.
2. Página: `#custom-css-<página>`. Modal: `.custom-css-modal` (todos) mais `.custom-css-modal-<nome>` (aquele).
3. Classe diz **onde**; atributo `data-*` diz **quando** (estado). Tema escuro: `body[data-theme="dark"]`.
4. Para vencer o Material-UI às vezes é preciso `!important`.
5. CSS do painel vai no campo pós-login; o pré-login é público. Nenhum segredo em campo de JS.
6. O JS roda uma vez por carregamento, numa SPA: as telas e os elementos aparecem depois.
7. Se o elemento não tem âncora no catálogo, o alvo não existe. Não invente nome de classe: confira com `grep` antes de usar.

## Formato dos arquivos

- Tabelas curtas são tabelas Markdown.
- Listas longas (`06`, `09`, parte de `03`, `04`, `12`) usam um título `###` por item, com os campos em marcadores logo abaixo.
- `07`, `08` e `10` têm um seletor por linha.
- O texto é o do catálogo, sem resumo e sem corte. `02` e `14` não vêm do catálogo: foram lidos do código do frontend, e cada um diz isso no topo.
