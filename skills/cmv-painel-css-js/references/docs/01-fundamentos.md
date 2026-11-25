<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-30.215.0 -->

# Fundamentos

## Como usar

Cada tela e cada janela da plataforma, e boa parte do que há dentro delas, têm uma classe que começa com `custom-css-`. É nelas que o CSS personalizado deve se apoiar: elas continuam as mesmas quando a plataforma é atualizada — as classes do Material-UI (`.MuiPaper-root`, `.jss123`) não.

| Campo | Onde fica | Vale para |
|---|---|---|
| **CSS pré-login — público** | Configurações → Cores | todas as telas, inclusive login e cadastro. É servido sem login, e qualquer pessoa consegue ler: deixe aqui só o visual das telas públicas |
| **CSS pós-login — só para quem entrou** | Configurações → Cores | o painel, depois do login: os atendimentos, os menus, as janelas |
| **CSS desta empresa** | Configurações → Empresas → editar a empresa → aba Configurações | só aquela empresa, depois do login. Entra depois do CSS geral e vence os empates |
| **CSS do Chat Externo (Modo Alternativo)** | Configurações → Empresas → editar a empresa → aba Configurações | só a página de chat que o cliente final abre pelo link (veja a seção Chat Externo, mais abaixo) |

1. Abra a tela que você quer mudar e inspecione o elemento no navegador (botão direito → Inspecionar).
2. No elemento, ou num dos que estão em volta dele, procure uma classe `custom-css-*` — ou busque aqui pelo nome da tela.
3. Escreva a regra no campo certo e salve. A página recarrega e o resultado aparece.

Classe diz **onde**; atributo `data-*` diz **quando**. `body[data-theme="dark"]` vale só no tema escuro. Para vencer o estilo do Material-UI, às vezes é preciso `!important`.

```css
/* o cartão de cada atendimento na lista */
.custom-css-ticket-item { border-radius: 12px !important; }

/* só o balão da mensagem que ainda não saiu */
.custom-css-msg-bubble[data-status="pending"] { opacity: .6; }

/* o cabeçalho de todas as páginas, só no tema escuro */
body[data-theme="dark"] .custom-css-page-header { background: #111; }
```

## Convenções

Três regras cobrem quase tudo — saber elas evita procurar no catálogo:

| Onde | Padrão |
|---|---|
| Página | `#custom-css-<nome-da-página>` no container |
| Cabeçalho e título da página | `.custom-css-page-header` · `.custom-css-page-title` |
| Painel da página (o que vem abaixo do cabeçalho) | `.custom-css-page-panel` |
| Modal | `.custom-css-modal` (todos) **+** `.custom-css-modal-<nome>` (aquele) |
| Cabeçalho, rodapé e corpo de toda janela | `.custom-css-dialog-header` · `.custom-css-dialog-footer` · `.custom-css-dialog-body` |
| Seletor (o campo de escolher, em toda tela e janela) | `.custom-css-select[data-preenchido]` na raiz · `-label` no rótulo · `-input` na caixa · `-border` na borda |
| Abas e seções dentro de janela | `.custom-css-dialog-tabs` · `.custom-css-dialog-secao[data-secao]` · `.custom-css-dialog-secao-titulo` |
| Botão de ação dos cadastros (cartões e tabelas) | `[data-acao]`: `editar` · `excluir` · `ver-contatos` · `trocar-senha` · `copiar-url`… |
| Cartão de número ("Total 89", "Pendentes 11"…) | `.custom-css-stat-card[data-stat]` · `-icone` · `-rotulo` · `-valor` · `-detalhe` |
| Estado vazio ("Nenhum … encontrado") | `.custom-css-empty-state[data-empty="<página>"]` · `-icone` · `-titulo` · `-texto` · `-acao` |
| Faixa em gradiente | `.custom-css-section-header` · `-icone` · `-titulo` · `-subtitulo` |
| Menu aberto por uma página | `.custom-css-page-menu` (todos) **+** `.custom-css-menu-<nome>` (aquele) · `[data-menu-action]` nos itens |
| Menu da barra do topo | `.custom-css-menu-<nome>` no papel (`-usuario`, `-status`, `-idioma`; o do "+" do celular é `.custom-css-appbar-menu`) · `[data-menu-action]` nos itens |
| Popover (a caixa que abre ao lado de um botão) | `.custom-css-popover` (todos) **+** `.custom-css-popover-<nome>` (aquele) na raiz · `.custom-css-popover-paper` na caixa que se vê |
| Escolhido | `aria-pressed` (botão de alternância e cartão que filtra) · `aria-expanded` (cartão que abre seção) · `aria-selected` (aba) · `aria-checked` (item de menu que liga e desliga) |
| Tema | `body[data-theme="dark"]` / `[data-theme="light"]` |

Classe diz **onde**; atributo `data-*` diz **quando**. Para pintar só a mensagem que falhou, não existe classe — existe `[data-status="pending"]`.

Para vencer o Material-UI às vezes é preciso `!important`, igual no CSS geral.

## Não achou o que queria

Inspecione o elemento no navegador: se ele tiver uma classe `custom-css-*` (ou uma das classes sem prefixo), ela está aqui. Se não tiver, o alvo ainda não existe — peça, porque depender das classes do Material-UI (`.MuiPaper-root`, `.jss123`) quebra na próxima atualização da biblioteca.

Totais: 162 páginas · 378 modais · 2818 específicas · 69 sem prefixo · 623 atributos · Chat Externo: 95 âncoras e 29 atributos.
