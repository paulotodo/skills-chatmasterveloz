<!-- escrito à mão · fonte: textos de ajuda e código do bundle WS-29.930.0 (não está no catálogo /css-docs) -->

# Onde o CSS e o JS personalizados entram

O catálogo diz **o que** selecionar. Este arquivo diz **em que campo** escrever, **quando** cada campo carrega e **quem consegue ler**. Tudo aqui foi lido dos textos de ajuda da própria plataforma e do código que injeta os campos.

## Os campos

| Campo | Onde fica no painel | Tipo | Quem recebe | Elemento injetado |
|---|---|---|---|---|
| CSS pré-login — público | Configurações → Cores | CSS | todo mundo, sem login (inclusive login e cadastro) | `<style id="custom-css-frontend">` no fim do `<head>` |
| CSS pós-login | Configurações → Cores | CSS | só quem fez login; some no logout | `<style id="custom-css-poslogin">` logo depois do anterior |
| CSS desta empresa | Configurações → Empresas → editar a empresa → aba Configurações | CSS | só os usuários daquela empresa, depois do login | `<style id="custom-css-company">` depois dos dois |
| CSS do Chat Externo (Modo Alternativo) | mesma aba da empresa | CSS | o cliente final, na página pública do chat | só naquela página — ver `12-chat-externo.md` |
| JS pré-login — público | Configurações → Cores | JS | todo mundo, sem login | `<script id="custom-js-frontend">` no fim do `<body>` |
| JS pós-login | Configurações → Cores | JS | só quem fez login | `<script id="custom-js-poslogin">` no fim do `<body>` |
| JS desta empresa | aba Configurações da empresa | JS | só os usuários daquela empresa, depois do login | `<script id="custom-js-company">` no fim do `<body>` |

## Ordem de carga

- **CSS:** pré-login → pós-login → empresa. Em empate de especificidade vence o da empresa.
- **JS:** pré-login → pós-login → empresa.
- O CSS personalizado entra depois do CSS da plataforma. Para vencer o Material-UI pode ser preciso `!important`.

## Regras do CSS

- O campo pré-login é servido por rota pública: qualquer pessoa lê. Deixe nele só o visual das telas públicas (cor, logo, fundo). O visual do painel (tickets, chat, menus) vai no pós-login.
- A chave "Usar a customização geral (CSS e JS)" no cadastro da empresa desliga, para aquela empresa, o CSS pré-login, o CSS pós-login e o JS geral. Não afeta as telas de login e cadastro. O CSS e o JS da própria empresa continuam valendo.
- Ao salvar, a página recarrega.
- Use as âncoras `custom-css-*` e os atributos `data-*` do catálogo. Classes do Material-UI (`.MuiPaper-root`, `.jss123`) mudam a cada atualização.

## Regras do JS

- **Roda uma vez por carregamento da página.** O painel é uma SPA: trocar de tela não recarrega nem roda o script de novo. O script precisa lidar sozinho com elementos que aparecem depois (delegação de evento no `document`, ou os eventos de `05-eventos-js.md`).
- **A sintaxe é validada** ao salvar (nos campos de Configurações → Cores) e, no pós-login e no da empresa, de novo antes de injetar. Código com erro de sintaxe não é injetado.
- **O código roda dentro de `try { … } catch`.** Um erro em execução não derruba a aplicação e aparece no console com o prefixo do campo:

| Campo | Prefixo no console |
|---|---|
| JS pré-login | `[custom-js]` |
| JS pós-login | `[custom-js-poslogin]` |
| JS da empresa | `[custom-js-empresa]` |

- Como o código vira o corpo de um `try`, um `return` solto no nível de cima é erro de sintaxe, e erro dentro de `setTimeout`, de ouvinte de evento ou de `Promise` não cai nesse `catch`.
- **Nada de segredo em nenhum campo de JS** (chave de API, token, senha). O pré-login é lido por qualquer pessoa sem login; o pós-login e o da empresa rodam no navegador de todo usuário autenticado, e ali qualquer um lê.
- No pré-login também não coloque lógica de operação (regra de bloqueio, limite de SLA, nome de chave de armazenamento): fica legível para quem só abriu a URL. Código que trata do painel vai no pós-login.
- **Remover o script não desfaz** evento, temporizador nem variável que ele criou. Só o recarregamento da página desliga. No logout a plataforma recarrega a página.
- O JS da empresa passa a valer no próximo carregamento da página.

## Para conferir se carregou

No console do navegador:

```js
["custom-css-frontend", "custom-css-poslogin", "custom-css-company",
 "custom-js-frontend", "custom-js-poslogin", "custom-js-company"]
  .map(id => [id, !!document.getElementById(id)]);
```

O `<style>` com `media="not all"` existe mas está desligado: é a customização geral desativada para a empresa.
