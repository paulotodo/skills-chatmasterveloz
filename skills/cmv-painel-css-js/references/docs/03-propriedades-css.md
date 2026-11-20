<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-30.141.0 -->

# Propriedades que o CSS pode mandar

Quase tudo aqui é só alvo de estilo, mas há um ponto em que o CSS **decide**:

Formato: um título `###` por **Propriedade** (16 itens), com os campos Onde · O que faz abaixo.

### `--ticket-actions-visiveis`

- **Onde:** `.custom-css-ticket-actions`
- **O que faz:** quantas ações ficam na barra antes de o resto ir para o menu `⋯`. Sem ela, a barra mede o espaço sozinha

### `--ticket-actions-ordem`

- **Onde:** `.custom-css-ticket-actions`
- **O que faz:** QUAIS ações vêm primeiro, e em que ordem: os nomes do `data-action` delas, separados por vírgula. As que a lista não cita vêm depois, na ordem de sempre — e a `--ticket-actions-visiveis` conta nesta ordem

### `--ticket-actions-no-menu`

- **Onde:** `.custom-css-ticket-actions`
- **O que faz:** as ações que ficam SEMPRE no menu `⋯`, em qualquer largura: os nomes do `data-action`, separados por vírgula. Elas não ocupam vaga na `--ticket-actions-visiveis`

### `--menu-ordem`

- **Onde:** `.custom-css-menu-lista` (o menu inteiro) — ou uma `.custom-css-menu-secao`, ou um `.custom-css-menu-grupo-itens`, só para ela
- **O que faz:** a ORDEM do menu lateral, pelos nomes, separados por vírgula: o `data-menu` do item, o `data-menu-group-box` do submenu ou o `data-menu-section` da seção. Cada caixa (o menu, cada seção, cada submenu) põe primeiro os citados, na ordem citada; os outros seguem depois, na ordem de sempre. O título e o divisor do topo da seção ficam no topo dela. Sem ela, nada muda

### `--section-header-fundo`

- **Onde:** `.custom-css-section-header` (ou `:root`)
- **O que faz:** o fundo de TODAS as faixas em gradiente de uma vez, sem `!important`. A plataforma nunca a define: sem ela, cada faixa usa o próprio gradiente

### `--section-header-gradiente`

- **Onde:** `.custom-css-section-header`
- **O que faz:** o gradiente que a plataforma deu àquela faixa (cada seção de Configurações tem o seu). Serve para LER — reaproveitar a cor da seção numa borda, por exemplo

### `--lane-color`

- **Onde:** a coluna de cada Kanban (`.custom-css-kanban-col`, `-team-col`, `-filas-col`, `-grupos-col`) e a do Quadro de Atendimentos (`.custom-css-quadro-coluna`)
- **O que faz:** a cor da etapa (ou da fila), a mesma do cabeçalho — no Quadro, a da bolinha (`.custom-css-quadro-coluna-cor`). Serve para LER: a borda da coluna, o contador ou o cartão na cor da etapa, sem depender do `style` do cabeçalho

### `--queue-color`

- **Onde:** o cartão do ticket na lista (`.custom-css-ticket-item`) e o do Quadro (`.custom-css-quadro-card`); o chip de setor das janelas (`.custom-css-queue-select-chip`) e o do cartão de Usuários (`.custom-css-users-card-setor`)
- **O que faz:** a cor da fila, a mesma da borda e do selo — cinza `#7C7C7C` no atendimento sem fila. Serve para LER: o `data-queue-color` ao lado é texto, e o CSS não o usa como cor

### `--flow-node-cor`

- **Onde:** o cartão de cada bloco no desenho do fluxo (`.custom-css-flow-node`)
- **O que faz:** a cor do tipo do bloco — a do ícone, das ações e dos detalhes dele. Serve para LER, como a `--queue-color`; para trocar a cor de um tipo ela pede `!important` (vem no `style` do cartão), e o ícone e as ações acompanham

### `--flow-node-fundo` · `--flow-node-borda` · `--flow-node-sombra`

- **Onde:** o mesmo cartão (ou `:root`, para todos)
- **O que faz:** o fundo, a cor da borda e a sombra do cartão, sem `!important`. A plataforma nunca as define: sem elas, cada tipo usa as cores de sempre

### `--ticket-min-height`

- **Onde:** o cartão do ticket (`.custom-css-ticket-item`) ou `:root`
- **O que faz:** a altura mínima do cartão, sem `!important`. A plataforma nunca a define: sem ela, `115px`

### `--appbar-fundo`

- **Onde:** `:root`
- **O que faz:** o fundo da barra do topo (`.custom-css-appbar-toolbar`) e do menu do "+" do celular, sem `!important` — no `:root`, porque o menu abre fora da barra. A plataforma nunca a define: sem ela, a cor das Configurações

### `--appbar-cor`

- **Onde:** `.custom-css-appbar-toolbar`
- **O que faz:** a cor da barra escolhida nas Configurações. Serve para LER, como a `--queue-color`

### `--custom-css-favicon` · `--custom-css-favicon-256`

- **Onde:** `:root`
- **O que faz:** o ícone do servidor, o de 32×32 e o de 256×256, como `url(…)` — para usar em `background-image`. O CSS personalizado pode redefinir as duas

### `--chamada-fundo` · `--chamada-quadro-fundo` · `--chamada-falando`

- **Onde:** `:root` (ou `.custom-css-chamada`, `#custom-css-sala-convidado`)
- **O que faz:** o plano de fundo da área dos vídeos da chamada (`.custom-css-chamada-grade`) e da página do convidado — cor, gradiente ou `url(…)` —, o fundo de cada participante (`.custom-css-chamada-participante`) e a borda de quem está falando, sem `!important`. A plataforma nunca as define: sem elas, os escuros de sempre e a borda verde

### `--quadro-tempo-atrasado` · `--quadro-tempo-atencao` · `--quadro-tempo-em-dia`

- **Onde:** `:root` (ou o card do Quadro, `.custom-css-quadro-card`)
- **O que faz:** a cor do tempo do card do Quadro de Atendimentos (`.custom-css-quadro-tempo`), por faixa: atrasado (`data-elapsed-late="true"`), atenção e em dia — sem `!important`. A plataforma nunca as define: sem elas, o `#db1313` (no escuro, o `#ff7a7a`, legível sobre o card), o `#a5a51a` e o `#36a936`. A cor não vem mais no `style` do elemento: uma regra no `[data-elapsed-status]` também vale

```css
/* três ações na barra, o resto sempre no menu */
.custom-css-ticket-actions { --ticket-actions-visiveis: 3; }

/* resolver e transferir primeiro; excluir e agendar sempre no menu */
.custom-css-ticket-actions {
  --ticket-actions-ordem: resolve, transfer;
  --ticket-actions-no-menu: delete, schedule;
}

/* todas as faixas com a cor da marca; a cor original da seção vira a borda */
:root { --section-header-fundo: linear-gradient(135deg, #0f766e, #134e4a); }
.custom-css-section-header { border-left: 6px solid; border-image: var(--section-header-gradiente) 1; }

/* a chamada com a imagem da marca de fundo, na janela e na página do convidado */
:root { --chamada-fundo: url(https://exemplo.com/fundo.jpg) center / cover; --chamada-falando: #0f766e; }
```

```css
/* menu: a seção Sistema no topo; Contatos e o CRM primeiro dentro da seção deles */
.custom-css-menu-lista { --menu-ordem: sistema, contacts, crm; }

/* destacar uma seção inteira, título junto */
.custom-css-menu-secao[data-menu-section="administracao"] { background: rgba(15, 118, 110, .08); border-radius: 12px; }
```

Existe porque a medição automática roda **depois** de qualquer coisa que o CSS faça, então quando ela erra não há como corrigir por fora. Valor inválido ou ausente cai na medição normal.
