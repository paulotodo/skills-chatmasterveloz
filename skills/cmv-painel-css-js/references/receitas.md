# Receitas prontas de CSS e JS do painel

Todos os seletores, atributos e variáveis destas receitas foram conferidos com `scripts/conferir_seletores.py` contra o catálogo WS-30.141.0 (`references/docs/`): os nomes existem, e os valores de atributo estão entre os que o `06` e o `12` listam (o script deixa um aviso só para `data-menu="contacts"`, porque o catálogo não lista os valores de `data-menu`). O que **não** foi feito: testar o resultado visual num painel de verdade. Por isso, ao entregar uma receita, peça para a pessoa olhar o resultado depois de salvar e avisar se algo não mudou (o motivo mais comum é faltar `!important` para vencer o Material-UI).

Cores, tamanhos e textos são exemplos: troque pelos da pessoa. Se mudar ou acrescentar um seletor, rode o script de novo.

## Sumário

| # | Receita | Campo |
|---|---|---|
| 1 | Cor da marca no tema escuro | CSS pós-login |
| 2 | Fundos do tema escuro e regra que vale só no escuro | CSS pós-login |
| 3 | Barra do topo e faixas em gradiente | CSS pós-login |
| 4 | Esconder item, seção ou submenu do menu lateral | CSS pós-login ou da empresa |
| 5 | Reordenar o menu lateral | CSS pós-login ou da empresa |
| 6 | Fonte e cores dos balões da conversa | CSS pós-login |
| 7 | Cartão da lista de atendimentos | CSS pós-login |
| 8 | Barra de ações do atendimento | CSS pós-login |
| 9 | Campo de digitação | CSS pós-login |
| 10 | Tela de login e as outras telas de entrada | CSS pré-login |
| 11 | Uma janela (modal) específica, ou todas | CSS pós-login |
| 12 | Regra que vale só em uma página | CSS pós-login |
| 13 | Regra por estado, com `data-*` | CSS pós-login |
| 14 | Kanban e Quadro com a cor da etapa | CSS pós-login |
| 15 | Trocar o texto de um botão | CSS pós-login |
| 16 | JS: aviso quando abrir uma tela (espera o elemento aparecer) | JS pós-login |
| 17 | JS: lembrete ao clicar num botão (delegação de evento) | JS pós-login |
| 18 | JS: reagir ao evento `sip:state` | JS pós-login |
| 19 | Chat Externo | CSS do Chat Externo |
| 20 | Dashboard e Modo TV | CSS pós-login |

## Como aplicar e como desfazer (vale para todas)

Os campos e os caminhos estão em `references/docs/02-campos-css-js.md`:

| Campo | Caminho no painel |
|---|---|
| CSS pré-login, CSS pós-login, JS pré-login, JS pós-login | Configurações → Cores |
| CSS desta empresa, JS desta empresa, CSS do Chat Externo (Modo Alternativo) | Configurações → Empresas → editar a empresa → aba Configurações |

Os dois caminhos são telas de quem administra a instância (`revendedor/recursos/configuracoes.md`). O administrador de uma empresa cliente não chega nelas: para ele, entregue o bloco e diga que quem cola é quem fornece a plataforma.

Aplicar:

1. Abra o caminho do campo indicado na receita.
2. Copie antes o que já está no campo para um arquivo de texto (é a sua cópia de segurança).
3. Cole o bloco **no fim** do campo, sem apagar o que já existe. Cada bloco vem entre `CMV-INICIO` e `CMV-FIM` para ser fácil de achar depois.
4. Salve. A página recarrega e o resultado aparece. O JS da empresa passa a valer no próximo carregamento da página.

Desfazer:

1. Volte ao mesmo campo, apague tudo entre `CMV-INICIO` e `CMV-FIM` daquele bloco e salve.
2. Se era JS: quem estava com o painel aberto precisa recarregar a página (F5). Remover o script não desliga evento nem temporizador que ele já criou; só o recarregamento desliga.

Para usar uma receita só em uma empresa, cole no **CSS desta empresa** (ou **JS desta empresa**) em vez do pós-login: ele entra depois do geral e vence os empates.

---

## 1. Cor da marca no tema escuro

**Pedido típico:** "no tema escuro o painel fica cinza, quero a cor da minha marca."
**Campo:** CSS pós-login. **Fonte:** `04-tema-escuro.md`.

No escuro a plataforma usa cinza. A Cor Principal configurada pelo super admin fica em `--app-primary` nos dois temas; basta apontar as variáveis do escuro para ela. Estes blocos só usam `--mui-primary*`, `--mui-button-primary*` e `--mui-secondary*`, que o `04` dá como do tema escuro; nenhuma fonte diz que o tema claro as lê (o que o claro também lê são as quatro variáveis de fundo, ver a receita 2). Os blocos abaixo trocam tudo de uma vez: se o pedido é só os botões, o núcleo são as três `--mui-button-primary*`; as `--mui-primary*` e as `--mui-secondary*` ampliam o efeito para tudo o que o `04` lista em cada uma (nas `--mui-primary*`, o cabeçalho das janelas, os selos com número, o popup de notificações e outros). Entregue o núcleo e ofereça o resto como opcional, dizendo o que mais muda.

```css
/* CMV-INICIO cor da marca no tema escuro */
:root {
  /* cabeçalho das janelas, selos, destaques */
  --mui-primary: var(--app-primary);
  --mui-primary-dark: var(--app-primary-dark);
  --mui-primary-contrast: var(--app-primary-contrast);
  /* botão principal (Salvar, Adicionar, Confirmar): tem variável própria */
  --mui-button-primary: var(--app-primary);
  --mui-button-primary-hover: var(--app-primary-dark);
  --mui-button-primary-contrast: var(--app-primary-contrast);
}
/* CMV-FIM */
```

Variante, quando a pessoa quer no escuro uma cor diferente da Cor Principal (escolha um contraste legível: texto claro sobre cor escura, ou o contrário):

```css
/* CMV-INICIO cor fixa no tema escuro */
:root {
  --mui-primary: #0f766e;
  --mui-primary-dark: #134e4a;
  --mui-primary-contrast: #ffffff;
  --mui-button-primary: #0f766e;
  --mui-button-primary-hover: #134e4a;
  --mui-button-primary-contrast: #ffffff;
  /* interruptores, abas, chips, caixas de marcar: cor secundária */
  --mui-secondary: #5eead4;
  --mui-secondary-dark: #2dd4bf;
  --mui-secondary-contrast: #042f2e;
}
/* CMV-FIM */
```

Avise sempre: trocar `--mui-primary` não muda os botões (por isso as `--mui-button-primary*`), e o `04` lista o que as variáveis não alcançam. Para o tema **claro**, as únicas variáveis de cor documentadas são as quatro de fundo, `--mui-paper`, `--mui-background`, `--mui-paper-2` e `--mui-paper-3`, escritas em `body[data-theme="light"]` (receita 2); para a cor da marca no claro há só `--app-primary*`, a Cor Principal, que o super admin configura em Configurações → Cores, bloco **Cores Principais** (`revendedor/recursos/configuracoes-cores.md`).

## 2. Fundos do tema escuro e regra que vale só no escuro

**Pedido típico:** "o tema escuro está muito preto", "arruma tal parte que ficou ilegível no escuro."
**Campo:** CSS pós-login. **Fonte:** `04-tema-escuro.md`, `01-fundamentos.md`.

```css
/* CMV-INICIO fundos do tema escuro */
:root {
  --mui-background: #0f172a;      /* fundo da página */
  --mui-paper: #111827;           /* janelas, menus, cartões */
  --mui-paper-2: #0b1220;         /* conteúdo das janelas, seções, campos */
  --mui-paper-3: #1f2937;         /* bloco dentro de bloco, divisor de data */
  --mui-divider: #334155;         /* divisores */
  --mui-dashboard-card: #1e293b;  /* cartões do Dashboard */
}
/* CMV-FIM */
```

O `:root` acima não muda o tema claro. Desde a 29.923.0 (`13-historico.md`, "Tema claro com as variáveis do papel"), o claro também lê quatro dessas variáveis, `--mui-paper`, `--mui-background`, `--mui-paper-2` e `--mui-paper-3`, escritas em `body[data-theme="light"]`, sem `!important` (`revendedor/recursos/configuracoes-cores.md` confirma). O `04` ainda diz que as `--mui-*` só existem no escuro: a frase vem do site e, na divergência, valem o histórico e o artigo do revendedor. Só essas quatro: nenhuma fonte diz que o claro lê `--mui-divider`, `--mui-dashboard-card` ou as outras `--mui-*`. Vem da documentação, não de teste no painel.

```css
/* CMV-INICIO fundos do tema claro */
body[data-theme="light"] {
  --mui-background: #f4f6f8;      /* fundo da página */
  --mui-paper: #ffffff;           /* janelas, menus, popups, cartões */
  --mui-paper-2: #f8fafc;         /* seções e blocos das telas */
  --mui-paper-3: #eef2f6;         /* seções e blocos das telas */
}
/* CMV-FIM */
```

Quando o problema é um elemento que as variáveis não alcançam, escreva a regra só para o escuro com `body[data-theme="dark"]`:

```css
/* CMV-INICIO cabeçalho das páginas no tema escuro */
body[data-theme="dark"] .custom-css-page-header { background: var(--mui-paper-2) !important; }
body[data-theme="dark"] .custom-css-page-title { color: #f8fafc !important; }
/* CMV-FIM */
```

`.custom-css-page-header` e `.custom-css-page-title` são convenções (`01`): a regra vale em todas as páginas que as usam. Para uma página só, ponha o `#custom-css-<página>` na frente (receita 12).

No painel (CSS pós-login e da empresa), toda receita que fixa cor de fundo ou de texto precisa do par: a regra normal (tema claro) e a `body[data-theme="dark"] …` correspondente. Sem o par, um fundo claro fixo fica com texto claro por cima no escuro. Nas telas de entrada (receita 10) e no Chat Externo (receita 19) a referência não documenta tema escuro: lá, defina fundo e texto juntos, na mesma regra.

## 3. Barra do topo e faixas em gradiente

**Pedido típico:** "quero a barra de cima e os cabeçalhos coloridos com a cor da empresa."
**Campo:** CSS pós-login. **Fonte:** `03-propriedades-css.md`.

```css
/* CMV-INICIO barra do topo e faixas com a cor da marca */
:root {
  --appbar-fundo: #0f766e;                                         /* barra do topo e menu do "+" do celular */
  --section-header-fundo: linear-gradient(135deg, #0f766e, #134e4a); /* todas as faixas em gradiente */
}
/* a cor original de cada seção vira uma borda na faixa */
.custom-css-section-header { border-left: 6px solid; border-image: var(--section-header-gradiente) 1; }
/* CMV-FIM */
```

A plataforma nunca define essas duas variáveis (`03`). Em que tema elas valem o catálogo não informa: as entradas delas no `03` não falam de tema e o `04` não cita nenhuma das duas. Não afirme "vale nos dois temas" nem "só no claro": diga que isso não está documentado e peça para a pessoa conferir a barra e as faixas no claro e no escuro depois de salvar. `--appbar-cor` e `--section-header-gradiente` servem para **ler** a cor que a plataforma escolheu, não para trocar. A regra da borda não tem escopo de página: o `10` lista `.custom-css-section-header` nas áreas `Settings`, `TranslationManager`, `WABATemplates` e nas três janelas de novo ticket (`NewTicketModal…`), e ela pega todas. Para uma tela só, ponha o `#custom-css-<página>` ou o `.custom-css-modal-<nome>` na frente.

## 4. Esconder item, seção ou submenu do menu lateral

**Pedido típico:** "esconde o item X do menu."
**Campo:** CSS pós-login (todas as empresas) ou CSS desta empresa (só uma). **Fonte:** `06-atributos-data.md` (`data-menu`, `data-menu-section`, `data-menu-group-box`).

```css
/* CMV-INICIO esconder partes do menu lateral */
/* um item: o valor do data-menu é o identificador do item */
.custom-css-menu-lista [data-menu="contacts"] { display: none !important; }
/* uma seção inteira, com o título */
.custom-css-menu-secao[data-menu-section="ajuda"] { display: none !important; }
/* um submenu inteiro (Kanban, CRM, Campanhas…) */
.custom-css-menu-grupo-caixa[data-menu-group-box="campaigns"] { display: none !important; }
/* CMV-FIM */
```

- Seções documentadas: `favoritos`, `principal`, `atendimentos`, `ferramentas`, `modulos-externos`, `ajuda`, `campanhas`, `administracao`, `automacao`, `sistema`. Submenus documentados: `kanban`, `crm`, `pdv`, `consultorio`, `campaigns`.
- O catálogo **não lista** os valores de `data-menu` de cada item (só diz "o identificador do item"; `contacts` aparece num exemplo do `03`). Para outro item, peça à pessoa: botão direito no item → Inspecionar → copiar o valor de `data-menu`.
- **"Só para o atendente" não existe no catálogo.** Não há atributo com o perfil de quem está logado; os campos separam por público (todos, quem fez login, uma empresa), não por perfil. Diga isso com clareza em vez de inventar seletor.
- O menu tem um campo de busca no topo (`.custom-css-menu-busca`): com texto digitado, "o menu dá lugar aos resultados" em `.custom-css-menu-busca-resultados`. O catálogo não diz se um item escondido por estas regras aparece nos resultados: teste digitando o nome dele.
- Esconder não é bloquear: a tela continua abrindo pelo endereço. Controle de acesso é configuração do painel (assunto da `cmv-ajuda`).

## 5. Reordenar o menu lateral

**Pedido típico:** "coloca Contatos em primeiro no menu."
**Campo:** CSS pós-login ou da empresa. **Fonte:** `03-propriedades-css.md` (`--menu-ordem`).

```css
/* CMV-INICIO ordem do menu lateral */
/* nomes separados por vírgula: data-menu do item, data-menu-group-box do submenu ou data-menu-section da seção */
.custom-css-menu-lista { --menu-ordem: sistema, contacts, crm; }
/* ou só dentro de uma seção: troque pelos identificadores (data-menu) dos itens dela */
.custom-css-menu-secao[data-menu-section="administracao"] { --menu-ordem: identificador-um, identificador-dois; }
/* CMV-FIM */
```

Cada caixa (o menu, cada seção, cada submenu) põe primeiro os citados; os outros seguem na ordem de sempre. O catálogo não diz em que seção cada item fica nem lista os identificadores dos itens: se nada mudou, peça para a pessoa conferir o `data-menu` do item pelo Inspecionar.

O item citado sobe só **dentro da seção dele**: para ele ir ao topo do menu inteiro, cite também a seção, antes dos itens. Observado num painel em 22/11/2026 (não é lista oficial, confirme pelo Inspecionar): **Chats** é `tickets`, **Contatos** é `contacts`, **CRM** é o submenu `crm`, e os três ficam na seção `atendimentos`. Lá, `--menu-ordem: atendimentos, tickets, contacts, crm` levou os três ao topo; sem `atendimentos`, eles só passaram à frente dentro da seção, abaixo da seção Principal.

## 6. Fonte e cores dos balões da conversa

**Pedido típico:** "aumenta a letra das mensagens", "muda a cor do balão do atendente."
**Campo:** CSS pós-login. **Fonte:** `09-ancoras-por-area.md` (área `MessagesList`), `06-atributos-data.md` (`data-fromme`, `data-status`), `11-classes-sem-prefixo.md`.

```css
/* CMV-INICIO fonte e cores dos balões */
.custom-css-msg-bubble { font-size: 16px !important; line-height: 1.5 !important; }
.message-meta { font-size: 11px !important; }             /* a hora e os checks continuam pequenos */

/* enviada pela plataforma × recebida do contato */
.custom-css-msg-bubble[data-fromme="true"] { background: #d1fae5 !important; color: #064e3b !important; }
.custom-css-msg-bubble[data-fromme="false"] { background: #ffffff !important; color: #111827 !important; }
body[data-theme="dark"] .custom-css-msg-bubble[data-fromme="true"] { background: #064e3b !important; color: #ecfdf5 !important; }
body[data-theme="dark"] .custom-css-msg-bubble[data-fromme="false"] { background: #1f2937 !important; color: #f9fafb !important; }

/* mensagem que ainda não saiu */
.custom-css-msg-bubble[data-status="pending"] { opacity: .6; }
/* a citação com a borda na cor principal */
.message-quoted { border-left: 3px solid var(--app-primary); }
/* CMV-FIM */
```

As regras não têm escopo de página: o `10` lista `.custom-css-msg-bubble` nas áreas `MessagesList` e `BalaoDaConversa`, e o `11` descreve `.message-meta` e `.message-quoted` só como "conversa". A referência não diz em quais telas e janelas a conversa é desenhada, então conte que a regra vale em todas.

O catálogo não tem âncora só para o texto dentro do balão. Se a letra não mudar com a regra do balão, diga que o alvo específico não existe; não tente `.Mui*`. A nota interna (`.message-internal`) vem sem `data-fromme`, então as regras de cor acima não a alcançam.

## 7. Cartão da lista de atendimentos

**Pedido típico:** "deixa a lista de atendimentos mais compacta", "destaca quem está esperando."
**Campo:** CSS pós-login. **Fonte:** `03-propriedades-css.md` (`--ticket-min-height`, `--queue-color`), `11-classes-sem-prefixo.md`, `06-atributos-data.md`.

```css
/* CMV-INICIO cartão da lista de atendimentos */
:root { --ticket-min-height: 96px; }                       /* sem ela, 115px */
.custom-css-ticket-item { border-radius: 12px !important; }
.ticket-name { font-weight: 700; }
.ticket-preview-text { font-size: 13px; }
/* com mensagem não lida: contorno na cor da fila */
.custom-css-ticket-item[data-unread="true"] { box-shadow: inset 0 0 0 2px var(--queue-color); }
/* tempo atrasado (data-elapsed-status "late": acima de 60 minutos) */
.ticket-elapsed[data-elapsed-late="true"] { font-weight: 700; text-decoration: underline; }
/* CMV-FIM */
```

`--queue-color` serve para ler a cor da fila (cinza no atendimento sem fila). `data-unread` é sim/não; a quantidade está em `data-unread-count`. O `10` lista `.custom-css-ticket-item` em duas áreas, a lista de atendimentos e a de grupos (`TicketListItemCustom` e `TicketListItemCustomGroup`): as regras valem nas duas.

## 8. Barra de ações do atendimento

**Pedido típico:** "quero só três botões em cima da conversa", "tira o Excluir da frente."

O `06` lista os valores de `data-action` (`resolve`, `delete`…) sem o rótulo que aparece na tela: a ligação com "Resolver" e "Excluir" é dedução pelo nome. Peça para a pessoa confirmar pelo Inspecionar.
**Campo:** CSS pós-login. **Fonte:** `03-propriedades-css.md`, `06-atributos-data.md` (`data-action`, com a lista dos nomes).

```css
/* CMV-INICIO barra de ações do atendimento */
.custom-css-ticket-actions {
  --ticket-actions-visiveis: 3;                 /* quantas ficam à vista; o resto vai para o menu ⋯ */
  --ticket-actions-ordem: resolve, transfer;    /* quais vêm primeiro */
  --ticket-actions-no-menu: delete, schedule;   /* sempre dentro do menu ⋯ */
}
/* CMV-FIM */
```

Os nomes são os valores de `data-action` da barra (`resolve`, `return`, `transfer`, `schedule`, `task`, `delete`, `invite`, `call`, `files`, `flow`…): confira a lista inteira em `06` antes de usar outro. Isso muda o lugar do botão, não a permissão.

## 9. Campo de digitação

**Pedido típico:** "o campo de escrever cresce demais", "quero o campo sempre com duas linhas."
**Campo:** CSS pós-login. **Fonte:** `06-atributos-data.md` (aviso no fim do arquivo), `04-tema-escuro.md`.

```css
/* CMV-INICIO campo de digitação */
/* height não funciona aqui: o Material-UI grava a altura no próprio campo. max-height e min-height vencem */
.custom-css-composer-field textarea { max-height: 60px; overflow-y: auto !important; }
.custom-css-composer-field textarea { min-height: 40px; }
/* nota interna com fundo de destaque: o data-mode fica no próprio .custom-css-composer-field (06) */
.custom-css-composer-field[data-mode="internal"] textarea { background: #fffbe6; color: #1f2937; }
body[data-theme="dark"] .custom-css-composer-field[data-mode="internal"] textarea { background: #3f3a1d; color: #fef9c3; }
/* CMV-FIM */
```

O `10` lista `.custom-css-composer-field` nas áreas `MessageInputCustom` e `MessageInputCustomHub` (e em `helpers`): as regras valem no campo de digitação comum e no do Hub.

## 10. Tela de login e as outras telas de entrada

**Pedido típico:** "personaliza a tela de login com as cores da empresa."
**Campo:** **CSS pré-login** (é o único que chega em quem ainda não entrou). **Fonte:** `07-paginas.md`, `09-ancoras-por-area.md` (áreas `Login`, `Signup`, `ForgotPassword`), `06-atributos-data.md` (`data-link`).

```css
/* CMV-INICIO tela de login */
#custom-css-login { background: linear-gradient(135deg, #0f766e, #134e4a) !important; }
.custom-css-login-card { border-radius: 16px !important; box-shadow: 0 12px 40px rgba(0, 0, 0, .25) !important; }
.custom-css-login-logo { max-width: 220px; }
.custom-css-login-email-input, .custom-css-login-password-input { border-radius: 10px !important; }
/* esconder o link de cadastro (os outros valores do login: recuperar-senha, termos, privacidade) */
.custom-css-login-link[data-link="cadastro"] { display: none !important; }
/* o copyright, só no login: a mesma classe existe em outras três telas públicas */
#custom-css-login .custom-css-copyright { color: #e5e7eb !important; }
/* CMV-FIM */
```

Só se a pessoa pedir o mesmo visual nas outras telas de entrada:

```css
/* CMV-INICIO cadastro e recuperar a senha */
#custom-css-signup, #custom-css-forgotpassword { background: linear-gradient(135deg, #0f766e, #134e4a) !important; }
.custom-css-signup-card, .custom-css-forgotpassword-card { border-radius: 16px !important; }
#custom-css-signup .custom-css-copyright, #custom-css-forgotpassword .custom-css-copyright { color: #e5e7eb !important; }
/* CMV-FIM */
```

- **O campo é público:** qualquer pessoa lê o conteúdo sem login. Coloque aqui só o visual das telas públicas; regras do painel (atendimentos, menus) vão no pós-login. E o CSS pré-login chega a todas as telas (`01`), então todo seletor daqui precisa de escopo: sem o `#custom-css-login` na frente, a regra pega mais do que o pedido.
- **Copyright:** o `10` lista `.custom-css-copyright` em quatro áreas: `Login`, `Signup`, `ForgotPassword` e `Survey` (a pesquisa de satisfação). Sem escopo, a cor muda nas quatro.
- **O que o catálogo não diz:** se o `#custom-css-login` cobre a tela inteira (o fundo pode pintar só o contêiner), nem se o copyright e os links ficam dentro dele. Se a cor do copyright não mudar com a regra acima, ele está fora do contêiner, e não há como limitar a regra ao login só com o catálogo. Peça para a pessoa conferir pelo Inspecionar. O catálogo também dá só os nomes das âncoras do login, sem descrever cada uma (não diz, por exemplo, se `.custom-css-login-logo` é a imagem ou a caixa dela), e não documenta como trocar a imagem do logo por CSS. A imagem se troca em Configurações → Logotipos / Ícones, destino **Tela de Login**, em PNG; logotipo é da instância, não existe por empresa (`revendedor/recursos/configuracoes-logotipos-icones.md`).
- **Tema escuro: não documentado nestas telas.** O `04` só fala do painel, e o `06` diz que `data-theme` fica no `<body>` sem dizer em quais telas. Não escreva o par `body[data-theme="dark"]` aqui como se fosse garantido: defina fundo e texto juntos, com contraste próprio, e peça para a pessoa olhar o resultado.
- **Esconder o link não fecha o cadastro.** `/signup` é rota pública (`14-rotas.md`) e continua abrindo pelo endereço. O `06` diz, em `data-link`, que cada link do login "só aparece quando a configuração o liga": o jeito de tirar o link de verdade é desligar essa configuração. São duas opções em Configurações → Plataforma, grupo **Marca e acesso**, seção **Configurações Globais** (`revendedor/recursos/marca-e-acesso-em-plataforma.md`): **Registro (Inscrição) Visível?** mostra ou esconde o link de cadastro na tela de login; **Registro (Inscrição) Permitida?** em **Não** recusa o cadastro público mesmo com o link visível. Valem para todas as empresas da instância, e o card Plataforma só o super admin vê (`revendedor/recursos/configuracoes.md`): o administrador de uma empresa cliente pede a quem fornece a plataforma. O artigo não diz se a rota `/signup` deixa de abrir; diz que o cadastro é recusado.
- A chave "Usar a customização geral (CSS e JS)" da empresa não afeta as telas de login e cadastro (`02`).

## 11. Uma janela (modal) específica, ou todas

**Pedido típico:** "muda a janela de confirmação", "arredonda todas as janelas."
**Campo:** CSS pós-login. **Fonte:** `08-modais.md`, `01-fundamentos.md` (Convenções).

```css
/* CMV-INICIO janelas */
/* todas as janelas */
.custom-css-modal { border-radius: 16px !important; }

/* só as janelas de confirmação: o nome da janela na frente */
.custom-css-modal-confirmation .custom-css-dialog-header { background: #b91c1c !important; color: #ffffff !important; }
.custom-css-modal-confirmation .custom-css-dialog-body { font-size: 15px; }
.custom-css-modal-confirmation .custom-css-btn-confirm { background: #b91c1c !important; color: #ffffff !important; }
/* CMV-FIM */
```

Para achar o nome de outra janela, procure uma palavra em `08-modais.md` (um nome por linha; português e inglês se misturam: `ticket`, `usuario`, `user`…). Sem o nome da janela na frente, `.custom-css-dialog-header` vale em **todas** as janelas. O `08` só lista os nomes, sem descrição: o que cada janela é se deduz do nome (há também nomes por caso, como `.custom-css-modal-confirmation-atendimento-excluir`). Na dúvida, peça para a pessoa abrir a janela, inspecionar e dizer qual `custom-css-modal-…` aparece.

## 12. Regra que vale só em uma página

**Pedido típico:** "só na tela de Contatos, esconde o botão de excluir."
**Campo:** CSS pós-login. **Fonte:** `07-paginas.md`, `01-fundamentos.md` (Convenções), `06-atributos-data.md` (`data-acao`, `data-menu-action`).

```css
/* CMV-INICIO só na página de Contatos */
#custom-css-contacts .custom-css-page-title { font-size: 22px !important; }
#custom-css-contacts .custom-css-stat-card-valor { font-size: 28px !important; }
/* o botão Excluir da tabela */
#custom-css-contacts [data-acao="excluir"] { display: none !important; }
/* no celular, o mesmo botão fica no menu ⋮ da linha (06); a regra usa a âncora do próprio menu */
.custom-css-menu-contato-acoes [data-menu-action="excluir"] { display: none !important; }
/* CMV-FIM */
```

Toda página tem um `#custom-css-<página>` (é **id**, com `#`; as outras âncoras são classe, com `.`). Esconder o botão não tira a permissão de excluir.

## 13. Regra por estado, com `data-*`

**Pedido típico:** "pinta de outra cor quem está aguardando", "destaca quando o telefone tocar."
**Campo:** CSS pós-login. **Fonte:** `06-atributos-data.md` (`data-status`, `data-unread`, `data-sip-call`).

Classe diz **onde**; `data-*` diz **quando**. Confira em `06` os valores do atributo **naquele elemento**: `data-status` tem um vocabulário no balão, outro no cartão do atendimento, outro na tarefa.

```css
/* CMV-INICIO regras por estado */
/* atendimento aguardando, na lista */
.custom-css-ticket-item[data-status="pending"] { background: #fef3c7 !important; }
body[data-theme="dark"] .custom-css-ticket-item[data-status="pending"] { background: #422006 !important; }
/* conversa de grupo */
.custom-css-ticket-item[data-group="true"] .ticket-name { font-style: italic; }
/* chamada chegando no ramal: a barra do topo muda de cor */
body[data-sip-call="ringing"] .custom-css-appbar-toolbar { background: #b91c1c !important; }
/* CMV-FIM */
```

As duas primeiras regras valem na lista de atendimentos e na de grupos (as duas áreas de `.custom-css-ticket-item` no `10`).

## 14. Kanban e Quadro com a cor da etapa

**Pedido típico:** "quero a coluna do Kanban com a cor da etapa", "muda as cores do tempo no Quadro."
**Campo:** CSS pós-login. **Fonte:** `03-propriedades-css.md` (`--lane-color`, `--quadro-tempo-*`).

```css
/* CMV-INICIO Kanban e Quadro de Atendimentos */
/* --lane-color serve para ler a cor da etapa (ou da fila) */
.custom-css-kanban-col, .custom-css-quadro-coluna { border-top: 4px solid var(--lane-color); }
/* cores do tempo do card do Quadro, por faixa */
:root {
  --quadro-tempo-atrasado: #b91c1c;
  --quadro-tempo-atencao: #b45309;
  --quadro-tempo-em-dia: #15803d;
}
/* CMV-FIM */
```

Os outros Kanbans têm coluna própria: `.custom-css-kanban-team-col`, `.custom-css-kanban-filas-col`, `.custom-css-kanban-grupos-col`. As cores do tempo valem nos dois temas: escolha tons legíveis nos dois, ou redefina as três dentro de uma regra `body[data-theme="dark"] .custom-css-quadro-card`.

## 15. Trocar o texto de um botão

**Pedido típico:** "troca o texto do botão Enviar Template para Enviar modelo."
**Campo:** CSS pós-login. **Fonte:** `09-ancoras-por-area.md` (área `MessagesList`), `04-tema-escuro.md` (cita o botão "Enviar Template").

CSS resolve. Prefira-o ao JS aqui: o painel é uma SPA (`02`), e é de esperar que um texto trocado por JS se perca quando a tela é refeita (observação geral sobre SPAs, não um fato do catálogo).

```css
/* CMV-INICIO texto do botão Enviar Template */
.custom-css-conversation-bar-btn-template { font-size: 0 !important; }                     /* some com o texto original */
.custom-css-conversation-bar-btn-template::after { content: "Enviar modelo"; font-size: 14px; } /* escreve o novo */
/* CMV-FIM */
```

Limites, para dizer à pessoa: como é só CSS, o texto novo não acompanha o idioma do painel e leitores de tela tendem a continuar lendo o original (comportamento geral de CSS, não descrito no catálogo); só dá para fazer em botão que tem âncora no catálogo. Se o botão pedido não tem, o alvo não existe.

## 16. JS: aviso quando abrir uma tela (espera o elemento aparecer)

**Pedido típico:** "mostra um aviso quando o atendente abrir a tela de Contatos."
**Campo:** JS pós-login (ou JS desta empresa). **Fonte:** `02-campos-css-js.md` (regras do JS), `07-paginas.md`.

O JS roda uma vez, no carregamento. A tela de Contatos só existe quando a pessoa navega até ela, então o script vigia a página e reage quando o `#custom-css-contacts` aparece ou some.

```js
/* CMV-INICIO aviso na tela de Contatos */
(function () {
  var ID_DA_TELA = "custom-css-contacts";   // o id da página, de 07-paginas.md, sem o #
  var TEXTO = "Antes de importar contatos, confira a planilha com a supervisão.";

  function conferir() {
    var naTela = document.getElementById(ID_DA_TELA);
    var aviso = document.getElementById("cmv-aviso-tela");
    if (naTela && !aviso) {
      aviso = document.createElement("div");
      aviso.id = "cmv-aviso-tela";
      aviso.textContent = TEXTO;             // textContent, nunca innerHTML
      aviso.title = "Clique para fechar";
      aviso.style.cssText = "position:fixed;right:16px;bottom:16px;z-index:9999;max-width:320px;" +
        "padding:12px 16px;border-radius:8px;background:#0f766e;color:#fff;font:14px/1.4 sans-serif;cursor:pointer";
      aviso.onclick = function () { aviso.style.display = "none"; };
      document.body.appendChild(aviso);
    } else if (!naTela && aviso) {
      aviso.remove();                        // saiu da tela: o aviso volta na próxima visita
    }
  }

  new MutationObserver(conferir).observe(document.body, { childList: true, subtree: true });
  conferir();
})();
/* CMV-FIM */
```

O aviso é um elemento próprio, preso ao `<body>`: não mexe em nada que o painel desenha. Nada de dado de cliente nem de segredo no texto: todo usuário logado consegue ler o script.

## 17. JS: lembrete ao clicar num botão (delegação de evento)

**Pedido típico:** "quando o atendente clicar em Resolver, lembra ele de marcar a etiqueta."

A ligação entre o botão "Resolver" e `data-action="resolve"` é dedução pelo nome do valor (o `06` não traz o rótulo): confirme pelo Inspecionar.
**Campo:** JS pós-login (ou JS desta empresa). **Fonte:** `02-campos-css-js.md`, `06-atributos-data.md` (`data-action`).

O botão ainda não existe quando o script roda, então o clique é ouvido no `document` e filtrado pelo `data-action`.

```js
/* CMV-INICIO lembrete ao clicar em Resolver */
(function () {
  var TEXTO = "Lembrete: marque a etiqueta do atendimento antes de encerrar.";

  document.addEventListener("click", function (ev) {
    var alvo = ev.target instanceof Element ? ev.target.closest('[data-action="resolve"]') : null;
    if (!alvo) return;
    var lembrete = document.createElement("div");
    lembrete.textContent = TEXTO;
    lembrete.style.cssText = "position:fixed;left:50%;top:72px;transform:translateX(-50%);z-index:9999;" +
      "padding:10px 16px;border-radius:8px;background:#1f2937;color:#fff;font:14px/1.4 sans-serif";
    document.body.appendChild(lembrete);
    setTimeout(function () { lembrete.remove(); }, 5000);
  }, true);
})();
/* CMV-FIM */
```

O seletor não tem escopo de tela de propósito: o `06` cita o valor `resolve` só na barra do atendimento, e diz que a ação recolhida no menu `⋯` vira um item que leva só o `data-action`, fora da barra. O script só mostra o lembrete: não impede nem altera o encerramento. O `return` está dentro de uma função; solto no nível de cima seria erro de sintaxe, e o painel não injeta código com erro.

## 18. JS: reagir ao evento `sip:state`

**Pedido típico:** "quando chegar ligação, quero o título da aba piscando o número."
**Campo:** JS pós-login. **Fonte:** `05-eventos-js.md`, `06-atributos-data.md` (`data-sip-call`).

`sip:state` é um dos dois eventos do catálogo (o outro, `atendimentos:buscado`, avisa o fim de uma busca na Pesquisar). Antes de escrever JS, veja se CSS resolve: o `<body>` já traz `data-sip-call` e `data-sip-registration` (receita 13).

```js
/* CMV-INICIO título da aba durante a chamada */
(function () {
  var tituloAntes = null;

  window.addEventListener("sip:state", function (e) {
    var chamada = e.detail.call;   // valores documentados para o data-sip-call do body: idle, ringing, calling, active
    if (chamada === "ringing" && tituloAntes === null) {
      tituloAntes = document.title;
      document.title = "Chamada chegando: " + (e.detail.number || "");
    } else if (chamada !== "ringing" && tituloAntes !== null) {
      document.title = tituloAntes;
      tituloAntes = null;
    }
  });
})();
/* CMV-FIM */
```

O `05` lista os campos do `detail` (`registration`, `call`, `direction`, `muted`, `onHold`, `number`, `ticketId`), mas só dá os valores de `direction`. Os valores de `call` usados acima são os que o `06` documenta para o `data-sip-call`; peça para a pessoa confirmar no console com o exemplo do `05` antes de depender deles.

## 19. Chat Externo

**Pedido típico:** "personaliza a página de chat que o cliente abre pelo link."
**Campo:** **CSS do Chat Externo (Modo Alternativo)**, em Configurações → Empresas → editar a empresa → aba Configurações. **Fonte:** `12-chat-externo.md`.

É outra página, com âncoras próprias (`custom-css-chat-*`). O CSS do painel não chega nela (`12`): não misture os dois num mesmo bloco.

```css
/* CMV-INICIO Chat Externo */
.custom-css-chat-header { background: #0f766e; color: #ffffff; }
.custom-css-chat-sidebar-header { background: #134e4a; color: #ffffff; }
.custom-css-chat-messages { background: #f0fdfa; }

/* balões: use data-autor, e não as classes out/in da página (lá, out é o visitante) */
.custom-css-chat-row[data-autor="atendente"] .custom-css-chat-bubble { background: #ffffff; color: #111827; }
.custom-css-chat-row[data-autor="contato"] .custom-css-chat-bubble { background: #0f766e; color: #ffffff; }
.custom-css-chat-row[data-status="failed"] .custom-css-chat-bubble { outline: 1px solid #dc2626; }

/* barra de digitação e botão de enviar */
.custom-css-chat-input-wrap { border-radius: 20px; }
.custom-css-chat-send { background: #0f766e; color: #ffffff; }

/* tela de carregamento */
.custom-css-chat-loading-bar { background: #99f6e4; }
/* CMV-FIM */
```

- A referência não documenta campo de JS para o Chat Externo, nem tema escuro nessa página.
- O fundo da caixa do campo lê `--wa-input`, e o da caixa dos emojis e o da folha de opções, `--wa-popup` (branco, sem customização). O `12` não diz em que seletor defini-las.
- O visitante vê esta página: nada de informação interna em `content:` de CSS.

## 20. Dashboard e Modo TV

**Pedido típico:** "no Dashboard, esconde o bloco de aniversariantes e aumenta os números, para passar na TV."
**Campo:** CSS pós-login. **Fonte:** `07-paginas.md`, `06-atributos-data.md` (`data-dash-view`, `data-modo-tv`).

```css
/* CMV-INICIO Dashboard na TV */
/* números do topo maiores, só no Modo TV */
#custom-css-dashboard[data-modo-tv="ligado"] .custom-css-stat-card-valor { font-size: 48px !important; }
#custom-css-dashboard[data-modo-tv="ligado"] .custom-css-stat-card-rotulo { font-size: 18px !important; }
/* esconde a seção de aniversariantes e o cartão que a abre */
#custom-css-dashboard [data-dash-view="aniversariantes"] { display: none !important; }
/* CMV-FIM */
```

- O `data-dash-view` vale `estatisticas`, `linha-do-tempo`, `equipe`, `relatorios` ou `aniversariantes`, e está no cartão "O que você gostaria de ver?" e no bloco que ele abre (`.custom-css-dashboard-painel`). O seletor sem a classe do painel esconde os dois; com `.custom-css-dashboard-painel` na frente, só o bloco.
- Sem `[data-modo-tv="ligado"]`, a regra vale também fora do Modo TV.
- A área chamada só `Dashboard` no catálogo mistura duas telas: âncoras da Dashboard legada (`#custom-css-dashboard-legado`), como `.custom-css-aniversariantes`, e âncoras de blocos mais novos, como `.custom-css-dashboard-api-oficial` e `.custom-css-dashboard-ranking-linha`. O catálogo não diz em qual página cada âncora dessa área aparece: confirme pelo Inspecionar antes de prender a regra a um id de página. Não junte âncoras da legada, como `.custom-css-aniversariantes`, com o id da Dashboard nova: o seletor nunca casa. Se a pessoa usa a legada (endereço `/dashboard_legado`), as regras são `#custom-css-dashboard-legado .custom-css-aniversariantes` e `#custom-css-dashboard-legado .custom-css-stat-card-valor`, sem Modo TV: o `data-modo-tv` só existe na nova.
- O catálogo não diz em que posição da tela cada cartão de número fica: peça para a pessoa conferir no painel.
