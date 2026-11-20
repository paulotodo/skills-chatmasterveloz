<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-30.141.0 -->

# As cores do tema escuro

O tema escuro pinta com as cores abaixo, e cada uma está numa variável no `:root`. Trocar a variável troca a cor em todos os lugares que a leem, sem `!important`: o CSS personalizado entra depois do da plataforma. As `--mui-*` existem só no tema escuro.

Formato: um título `###` por **Variável** (15 itens), com os campos Hoje · O que pinta, no tema escuro abaixo.

### `--mui-background`

- **Hoje:** `#1C1C1C`
- **O que pinta, no tema escuro:** o fundo da página (`<body>`), e o das telas que o usam (Traduções, Chat Interno)

### `--mui-paper`

- **Hoje:** `#1C1C1C`
- **O que pinta, no tema escuro:** o papel do Material-UI (`.MuiPaper-root`): janelas, menus, cartões e contêineres de página — e os que escrevem o papel à mão e já leem a variável: Configurações, o Quadro, o Chat Interno (a moldura, o cabeçalho e o campo), o item do Anexar Arquivos e o painel "Selecionar ticket" do celular

### `--mui-paper-2`

- **Hoje:** `#1a1a1a`
- **O que pinta, no tema escuro:** o conteúdo das janelas (abaixo do título) e as seções das telas; a prévia do Criar Template e a barra do editor do Novo Informativo

### `--mui-paper-3`

- **Hoje:** `#2b2b2b`
- **O que pinta, no tema escuro:** o bloco dentro de outro bloco (o "Neste ciclo" do limitador, o do concatenador) e o divisor de data da conversa

### `--mui-divider`

- **Hoje:** `#363636`
- **O que pinta, no tema escuro:** os divisores (`.MuiDivider-root`), em toda parte

### `--mui-dashboard-card`

- **Hoje:** `#1e293b`
- **O que pinta, no tema escuro:** os cartões do Dashboard

### `--mui-primary`

- **Hoje:** `#DCDCDC`
- **O que pinta, no tema escuro:** a cor principal do escuro onde ela é FUNDO com texto por cima: o cabeçalho das janelas (no gradiente, com `--mui-primary-dark`), os selos com número (os filtros de atendimento, o Chat Interno), os botões e os destaques escolhidos (o botão de visualização, o "Não lidas", o calendário de Tarefas), o balão próprio e o selo "admin" do Chat Interno, o popup de notificações, a janelinha da chamada, o cabeçalho da tabela da Pesquisa de Satisfação e os painéis do editor de fluxo

### `--mui-primary-dark`

- **Hoje:** `#9A9A9A`
- **O que pinta, no tema escuro:** a variação escura: o fim do gradiente dos cabeçalhos de janela, e o fundo ao passar o mouse nos botões na cor principal

### `--mui-primary-contrast`

- **Hoje:** `rgba(0, 0, 0, 0.87)`
- **O que pinta, no tema escuro:** o texto e o ícone em cima de `--mui-primary` e de `--mui-primary-dark`

### `--mui-button-primary`

- **Hoje:** `#DCDCDC`
- **O que pinta, no tema escuro:** o fundo do botão principal do Material-UI (o "contained" na cor principal: Salvar, Adicionar, Confirmar…), em todas as telas e janelas — variável própria, de propósito: trocar a `--mui-primary` não muda os botões

### `--mui-button-primary-hover`

- **Hoje:** `#9A9A9A`
- **O que pinta, no tema escuro:** o fundo dele com o mouse em cima

### `--mui-button-primary-contrast`

- **Hoje:** `rgba(0, 0, 0, 0.87)`
- **O que pinta, no tema escuro:** o texto e o ícone dele

### `--mui-secondary`

- **Hoje:** `#eee`
- **O que pinta, no tema escuro:** a cor secundária do escuro nos componentes do Material-UI que a usam: o botão "Enviar Template" da faixa da janela de 24h e os outros botões na cor secundária (cheio, contornado, de texto, de ícone e o redondo), os chips e selos, os interruptores, as caixas de marcar e os rádios (que são da cor secundária por padrão), as abas, as barras e os círculos de progresso, os ícones e os textos

### `--mui-secondary-dark`

- **Hoje:** `#A6A6A6`
- **O que pinta, no tema escuro:** a variação escura dela: o fundo do botão cheio na cor secundária com o mouse em cima, e o avatar do chip

### `--mui-secondary-contrast`

- **Hoje:** `rgba(0, 0, 0, 0.87)`
- **O que pinta, no tema escuro:** o texto e o ícone em cima de `--mui-secondary` e de `--mui-secondary-dark`

Desde a 29.508.0, também leem as variáveis os lugares que tinham a cor do escuro escrita fixa. A cor de antes continua como reserva no `var()`:

| Onde | O que | Variável |
|---|---|---|
| ticket aberto | `.custom-css-ticket`, `.custom-css-ticket-header` e o `div` filho de `.custom-css-composer` | `--mui-background` |
| ticket aberto | `.custom-css-composer` | `--mui-paper` |
| ticket aberto | `.custom-css-composer-field` | `--mui-paper-2` |
| painel do contato | `.contact-drawer-header` | `--mui-background` |
| painel do contato | `.contact-drawer-body` e a lista de `.contact-note-list` | `--mui-paper` |
| lista de tickets | `.ticket-datetime` | `--mui-paper-3` |
| Kanban (o comum, por equipe, por filas e por grupos) | o quadro (`-board`) | `--mui-background` |
| Kanban (o comum, por equipe, por filas e por grupos) | os cartões de número (`-stat-card`), as colunas (`-col`) e os cards | `--mui-paper` |
| CRM — quadro | `.custom-css-crm-board-raia` | `--mui-paper-3` |
| Pesquisar | `.custom-css-atendimentos-resumo` (e o cartão da versão de celular) | `--mui-paper` |
| Pesquisar | a célula fixa do cabeçalho da tabela | `--mui-paper-3` |
| Pesquisar | a célula fixa do corpo da tabela | `--mui-paper-2` |
| Contatos e Registro de Atividades | `.custom-css-stat-card` (e, em Contatos, o botão que mostra os números) | `--mui-paper` |
| Contatos e Registro de Atividades | os campos de busca e de filtro; em Contatos, também a coluna fixa das ações (no celular) | `--mui-paper-2` |
| Tarefas | `.custom-css-todolist-filtros` | `--mui-paper-3` |
| Agendamentos | `.custom-css-agenda-dia` e o calendário | `--mui-paper` |
| Agendamentos, Webhooks e Conexões | o campo de busca | `--mui-paper-2` |
| Webhooks | `.custom-css-webhooks-visualizacao` | `--mui-paper` |
| Configurações | `.custom-css-settings-menu-item` | `--mui-paper` |
| Configurações | `.custom-css-settings-secao` | `--mui-paper-2` |
| Traduções | `.MuiTableHead-root` | `--mui-paper` |
| toda tabela com cabeçalho fixo | as células `stickyHeader` | `--mui-background` |
| FlowBuilder (editor) | o papel em volta do `.react-flow`, o próprio canvas, os painéis e o `.MuiDrawer-paper` das Versões | `--mui-paper` |
| FlowBuilder (editor) | `.custom-css-flow-busca-campo` | `--mui-paper-2` |
| Dashboard (legado) | o botão `.buttonHover`, no hover | `--mui-paper-3` |
| janelas | o rodapé (`.MuiDialogActions-root`) e os campos (`.MuiOutlinedInput-root`) | `--mui-paper-2` |
| janelas | o `.MuiDialog-paper` do agendamento, as abas (`.MuiTabs-root`), os cartões (`.MuiCard-root`), as seções e caixas de dentro, `.custom-css-tarefa-contato` e `.custom-css-ticket-files-resumo` | `--mui-paper` |
| janelas | o conteúdo de `.custom-css-modal-ticket-files` | `--mui-paper-2` |
| em toda parte | `.MuiDivider-root` | `--mui-divider` |

E, nos DOIS temas, a Cor Principal configurada pelo super admin:

| Variável | O que é |
|---|---|
| `--app-primary` | a Cor Principal |
| `--app-primary-dark` | a variação escura dela, a que o Material-UI calcula |
| `--app-primary-contrast` | o texto que o Material-UI põe em cima dela |

No escuro a plataforma continua com o cinza de sempre. Para usar a cor da marca, basta apontar as variáveis do escuro para ela:

```css
:root {
  --mui-primary: var(--app-primary);
  --mui-primary-dark: var(--app-primary-dark);
  --mui-primary-contrast: var(--app-primary-contrast);
  --mui-button-primary: var(--app-primary);
  --mui-button-primary-hover: var(--app-primary-dark);
  --mui-button-primary-contrast: var(--app-primary-contrast);
}
```

⚠️ O que as variáveis NÃO alcançam: os componentes do Material-UI que usam a cor da paleta (interruptores, abas e os botões que não são o principal) continuam com o cinza, e as telas que escrevem a cor do papel no próprio estilo continuam com o cinza fixo — as que a 29.470.0 e a 29.471.0 tocaram já leem as variáveis (as da tabela). O botão principal lê as dele, as `--mui-button-primary*`.
