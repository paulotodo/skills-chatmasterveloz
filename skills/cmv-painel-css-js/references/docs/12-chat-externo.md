<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-29.930.0 -->

# Chat Externo (página pública)

A página que o cliente final abre pelo link do Modo Alternativo é vestida por **outro campo**: o **CSS do Chat Externo (Modo Alternativo)**, em Configurações → Empresas → editar a empresa → aba Configurações. O CSS da plataforma não chega nela, porque ela tem marcação própria.

95 âncoras, lidas da página, na ordem da tela:

Formato: um título `###` por **Âncora** (95 itens), com os campos O quê abaixo.

### `.custom-css-chat-app`

- **O quê:** a tela inteira: a moldura das duas colunas (a lista à esquerda, a conversa à direita), com `data-tela` e `data-conversa`

### `.custom-css-chat-sidebar`

- **O quê:** a coluna da esquerda: a lista de conversas do visitante (os protocolos dele com a empresa, de qualquer conexão)

### `.custom-css-chat-sidebar-header`

- **O quê:** o topo da coluna da esquerda

### `.custom-css-chat-sidebar-avatar`

- **O quê:** a marca da empresa no topo da lista

### `.custom-css-chat-sidebar-title`

- **O quê:** o título da lista (Conversas)

### `.custom-css-chat-list`

- **O quê:** a lista de protocolos, a mais recente primeiro

### `.custom-css-chat-list-item`

- **O quê:** cada protocolo da lista — um botão, com `data-protocolo`, `data-atual`, `data-encerrado`, `data-ativo`, `data-canal` e, quando há mensagem nova, `data-nao-lidas`

### `.custom-css-chat-list-avatar`

- **O quê:** a marca da empresa em cada item

### `.custom-css-chat-list-title`

- **O quê:** o título do item (Protocolo 123; "Conversa atual" no ticket sem protocolo)

### `.custom-css-chat-list-channel`

- **O quê:** o canal ao lado do título (· WhatsApp, · Instagram…), dentro dele

### `.custom-css-chat-list-time`

- **O quê:** a hora da última mensagem (hh:mm hoje, Ontem, ou a data)

### `.custom-css-chat-list-preview`

- **O quê:** a prévia da última mensagem (Você: … / Atendente: …)

### `.custom-css-chat-list-badge`

- **O quê:** o selo do item: Atual (a conversa do link), Em andamento ou Encerrado

### `.custom-css-chat-list-unread`

- **O quê:** o contador de mensagens novas do atendente, no item atual, enquanto a conversa atual não está à vista

### `.custom-css-chat-conversation`

- **O quê:** a coluna da direita: a conversa aberta

### `.custom-css-chat-header`

- **O quê:** o topo da conversa

### `.custom-css-chat-back`

- **O quê:** a seta do topo que volta para a lista (só no celular)

### `.custom-css-chat-avatar`

- **O quê:** a foto no topo

### `.custom-css-chat-title`

- **O quê:** o nome no topo

### `.custom-css-chat-subtitle`

- **O quê:** a linha de status no topo (conectando… / online; com um protocolo antigo aberto, o número e o canal dele)

### `.custom-css-chat-canal-nova-conversa`

- **O quê:** só na página do canal Chat Externo (o link com `h=`), quando a conexão tem a página de entrada: o botão "Começar nova conversa" no fim do topo — esquece a conversa neste navegador e volta ao formulário de entrada. No celular, só o ícone. Some com a conversa bloqueada pelo atendimento (`.custom-css-chat-app` com `data-canal-estado="bloqueada"`), junto com o campo, que fica travado

### `.custom-css-chat-banner`

- **O quê:** a faixa de aviso (conversa encerrada; também é onde o botão de notificação aparece)

### `.custom-css-chat-messages`

- **O quê:** a área da conversa do link

### `.custom-css-chat-history`

- **O quê:** a área de um protocolo antigo, aberto pela lista: as mesmas linhas e balões, só para ler (sem o botão de ações)

### `.custom-css-chat-history-notice`

- **O quê:** o aviso no meio dessa área (Carregando…, Sem mensagens, ou a falha ao abrir)

### `.custom-css-chat-date-divider`

- **O quê:** o divisor de data (Hoje, Ontem, dd/mm)

### `.custom-css-chat-row`

- **O quê:** cada mensagem — a linha inteira, com o balão, as reações e o botão de ações

### `.custom-css-chat-bubble`

- **O quê:** o balão

### `.custom-css-chat-quote`

- **O quê:** a citação dentro do balão (resposta a outra mensagem) e a prévia na barra de resposta

### `.custom-css-chat-media`

- **O quê:** imagem, áudio ou vídeo dentro do balão

### `.custom-css-chat-doc`

- **O quê:** o anexo (link para o arquivo) dentro do balão

### `.custom-css-chat-caption`

- **O quê:** a legenda de uma imagem

### `.custom-css-chat-interactive`

- **O quê:** o conteúdo de uma mensagem com botões, lista ou cartão, dentro do balão — o fluxo conversando pela página (a chave "Continuar o fluxo no chat externo" do bloco do link), com `data-tipo`, `data-estilo` e `data-aberta`

### `.custom-css-chat-interactive-header`

- **O quê:** o cabeçalho dessa mensagem: um texto, ou a imagem, o vídeo ou o documento de um modelo

### `.custom-css-chat-interactive-text`

- **O quê:** o texto dessa mensagem

### `.custom-css-chat-contact-card`

- **O quê:** o cartão de um contato enviado pelo fluxo: o nome e o número

### `.custom-css-chat-location-card`

- **O quê:** o cartão de uma localização: o nome e o endereço

### `.custom-css-chat-catalog-section`

- **O quê:** o título de cada seção de um catálogo

### `.custom-css-chat-catalog`

- **O quê:** a fileira de produtos de uma seção, que rola para o lado

### `.custom-css-chat-product-card`

- **O quê:** cada produto do catálogo: a foto, o nome, o preço e o botão "Quero este", com `data-opcao`

### `.custom-css-chat-interactive-footer`

- **O quê:** o rodapé dessa mensagem

### `.custom-css-chat-interactive-buttons`

- **O quê:** a coluna de botões embaixo da hora, dentro do balão, com `data-aberta`

### `.custom-css-chat-interactive-button`

- **O quê:** cada botão dessa coluna (e o "Quero este" do produto), com `data-tipo`: responder, abrir um link, ligar ou copiar

### `.custom-css-chat-interactive-list-button`

- **O quê:** o botão que abre a lista de opções de um menu (a folha, abaixo)

### `.custom-css-chat-meta`

- **O quê:** hora e checks, dentro do balão

### `.custom-css-chat-reactions`

- **O quê:** a fileira de reações embaixo do balão

### `.custom-css-chat-reaction`

- **O quê:** cada reação da fileira (agrupada por emoji, com o contador quando há mais de uma)

### `.custom-css-chat-actions-btn`

- **O quê:** o botão ao lado do balão que abre "reagir / responder"

### `.custom-css-chat-actions`

- **O quê:** a barra de ações aberta

### `.custom-css-chat-action-react`

- **O quê:** cada emoji rápido da barra de ações

### `.custom-css-chat-action-reply`

- **O quê:** o botão de responder da barra de ações

### `.custom-css-chat-reply-bar`

- **O quê:** a barra "respondendo a…" sobre o campo de digitação

### `.custom-css-chat-reply-cancel`

- **O quê:** o × que fecha a barra de resposta

### `.custom-css-chat-canal-encerrado`

- **O quê:** só na página do canal Chat Externo (o link com `h=`): a faixa logo acima da barra de digitação com o atendimento encerrado — "Atendimento encerrado. Envie uma mensagem para começar outro." O campo continua livre: a mensagem retoma a conversa

### `.custom-css-chat-canal-bloqueada`

- **O quê:** só na página do canal Chat Externo: a faixa no mesmo lugar quando o atendente bloqueia a conversa — "Esta conversa foi encerrada pelo atendimento." O campo de digitação fica travado; a conversa continua legível

### `.custom-css-chat-composer`

- **O quê:** a barra de digitação

### `.custom-css-chat-emoji-btn`

- **O quê:** o botão dos emojis, na barra de digitação — com `aria-expanded` dizendo se a caixa dos emojis está aberta

### `.custom-css-chat-attach-btn`

- **O quê:** o botão de anexar (o clipe)

### `.custom-css-chat-input-wrap`

- **O quê:** a caixa arredondada em volta do campo de texto; o fundo lê `--wa-input` (branco, sem customização)

### `.custom-css-chat-input`

- **O quê:** o campo de texto

### `.custom-css-chat-mic`

- **O quê:** o botão do microfone

### `.custom-css-chat-send`

- **O quê:** o botão de enviar

### `.custom-css-chat-emoji-pop`

- **O quê:** a caixa dos emojis, que abre sobre a barra de digitação, com `data-aberto`; o fundo lê `--wa-popup` (branco, sem customização)

### `.custom-css-chat-recbar`

- **O quê:** a barra da gravação de áudio, no lugar da de digitação enquanto grava, com `data-gravando`

### `.custom-css-chat-rec-dot`

- **O quê:** a bolinha vermelha que pisca durante a gravação

### `.custom-css-chat-rec-time`

- **O quê:** o tempo da gravação (0:00)

### `.custom-css-chat-rec-cancel`

- **O quê:** o Cancelar da gravação (descarta o áudio)

### `.custom-css-chat-rec-send`

- **O quê:** o botão de enviar o áudio gravado

### `.custom-css-chat-readonly`

- **O quê:** a faixa "somente leitura" que toma o lugar do campo de digitação quando a direita mostra um protocolo antigo

### `.custom-css-chat-readonly-button`

- **O quê:** o botão "Voltar à conversa atual", nessa faixa

### `.custom-css-chat-aviso`

- **O quê:** o botão "avisar quando chegar mensagem" (pedido de permissão de notificação), dentro da faixa

### `.custom-css-chat-screen`

- **O quê:** a tela de erro e de senha, sobre as duas colunas

### `.custom-css-chat-pass`

- **O quê:** o formulário da senha (chat autenticado), dentro dessa tela

### `.custom-css-chat-entrada`

- **O quê:** só no link de entrada do canal Chat Externo (`e=`): o cartão da entrada, também dentro dessa tela — a marca e o nome da empresa, a pergunta da conversa lembrada e o formulário —, com `data-etapa`

### `.custom-css-chat-entrada-continuar`

- **O quê:** na volta ao link de entrada com uma conversa lembrada neste navegador (até 24 horas): o botão "Continuar a conversa anterior"

### `.custom-css-chat-entrada-comecar-nova`

- **O quê:** o botão "Começar nova", logo abaixo — mostra o formulário de entrada

### `.custom-css-chat-entrada-pais`

- **O quê:** o seletor do país no formulário de entrada (o rótulo e o `<select>`): o nome do país no idioma da página e o DDI — Brasil (+55)

### `.custom-css-chat-entrada-telefone`

- **O quê:** o campo do telefone (o rótulo e o `<input>`): o código de área e o número, sem o DDI. Com o número recusado, o `<input>` ganha `aria-invalid="true"`

### `.custom-css-chat-entrada-nome`

- **O quê:** o campo do nome (o rótulo e o `<input>`), só quando a conexão pede o nome

### `.custom-css-chat-entrada-sem-telefone`

- **O quê:** a caixa "Prefiro não informar meu telefone" (um `<label>` com a caixa de marcar), só quando a conexão deixa entrar sem telefone. Marcada, o país e o telefone ficam desligados

### `.custom-css-chat-entrada-consentimento`

- **O quê:** a caixa do aceite (um `<label>` com a caixa de marcar e o texto de consentimento da conexão), só quando a conexão tem o texto

### `.custom-css-chat-entrada-enviar`

- **O quê:** o botão Entrar do formulário de entrada

### `.custom-css-chat-loading`

- **O quê:** a tela de carregamento, no desenho da do WhatsApp Web; some quando a conversa está na tela

### `.custom-css-chat-loading-logo`

- **O quê:** a marca nela (o logo da conexão, ou o desenho padrão)

### `.custom-css-chat-loading-bar`

- **O quê:** a barra de progresso (o trilho; o preenchimento anda por etapa: configuração, mensagens, lista)

### `.custom-css-chat-loading-text`

- **O quê:** o texto Carregando…

### `.custom-css-chat-loading-footer`

- **O quê:** o rodapé, com o nome da empresa

### `.custom-css-chat-lightbox`

- **O quê:** a imagem ampliada

### `.custom-css-chat-sheet`

- **O quê:** a folha que sobe de baixo com as opções de uma lista

### `.custom-css-chat-sheet-box`

- **O quê:** a caixa branca da folha (o título e as opções); o fundo lê `--wa-popup` (branco, sem customização)

### `.custom-css-chat-sheet-title`

- **O quê:** o título da folha

### `.custom-css-chat-sheet-close`

- **O quê:** o × que fecha a folha

### `.custom-css-chat-sheet-options`

- **O quê:** a área das opções da folha, que rola

### `.custom-css-chat-sheet-section`

- **O quê:** o título de uma seção da lista, antes da primeira opção dela (as listas que a API manda têm seções)

### `.custom-css-chat-sheet-option`

- **O quê:** cada opção da folha — o título e, embaixo, a descrição —, com `data-opcao`

Atributos de estado da página:

Formato: um título `###` por **Atributo** (29 itens), com os campos Onde · Valores abaixo.

### `data-aberta`

- **Onde:** `.custom-css-chat-interactive` e `.custom-css-chat-interactive-buttons`
- **Valores:** `true` na mensagem que ainda aceita resposta: a última da conversa, sem resposta, com o atendimento aberto — ou encerrado com a avaliação esperando a nota · `false` nas outras, cujos botões de responder ficam desabilitados (os de link, ligar e copiar continuam valendo). Na página do canal Chat Externo, também `false` com a conversa bloqueada pelo atendimento e na mensagem de um atendimento anterior (`data-atendimento="anterior"`)

### `data-aberto`

- **Onde:** `.custom-css-chat-emoji-pop`
- **Valores:** `true` com a caixa dos emojis aberta · `false` fechada

### `data-atendimento`

- **Onde:** `.custom-css-chat-row`
- **Valores:** só na página do canal Chat Externo: `anterior` na mensagem de um atendimento que já acabou e continua na tela depois de a conversa ser retomada num atendimento novo — sem o botão de reagir e responder (`.custom-css-chat-actions-btn`) e, se for interativa, com os botões de responder desabilitados. Sem o atributo, a mensagem é do atendimento atual

### `data-ativo`

- **Onde:** `.custom-css-chat-list-item`
- **Valores:** `true` no item aberto à direita (o mesmo que leva `aria-current`) · `false`

### `data-atual`

- **Onde:** `.custom-css-chat-list-item`
- **Valores:** `true` no protocolo do link — a conversa viva, a única com campo de digitação · `false` nos outros

### `data-autor`

- **Onde:** `.custom-css-chat-row`, `.custom-css-chat-quote` e `.custom-css-chat-reaction`
- **Valores:** na linha e na citação: `contato` (o visitante) · `atendente`. Na reação: `contato` · `atendente` · `ambos` (os dois reagiram com o mesmo emoji). ⚠️ Use este, e não as classes `out`/`in` da página: ali `out` é a mensagem do VISITANTE — o inverso do `fromMe` do resto da plataforma

### `data-aviso`

- **Onde:** `.custom-css-chat-banner`
- **Valores:** `1` enquanto a faixa está mostrando o botão de pedir permissão de notificação; some quando o visitante responde ao pedido

### `data-body`

- **Onde:** `.custom-css-chat-row`
- **Valores:** o texto da mensagem. Uso interno da página (casa a bolha otimista com a confirmação) — não é um bom alvo de CSS

### `data-canal`

- **Onde:** `.custom-css-chat-list-item`
- **Valores:** o canal do protocolo (`whatsapp`, `instagram`, `facebook`, …) — a lista traz os protocolos de todas as conexões da empresa

### `data-canal-estado`

- **Onde:** `.custom-css-chat-app` (só na página do canal Chat Externo, o link com `h=`; sem o atributo, é a página do modo alternativo)
- **Valores:** `aberto` · `encerrado` (a faixa `.custom-css-chat-canal-encerrado`, com o campo livre — a próxima mensagem retoma a conversa) · `avaliacao` (encerrado com a avaliação esperando a nota: o campo travado, como no modo alternativo) · `bloqueada` (a faixa `.custom-css-chat-canal-bloqueada`, com o campo travado)

### `data-conversa`

- **Onde:** `.custom-css-chat-app`
- **Valores:** `atual` (a conversa do link, com o campo de digitação) · `historico` (um protocolo antigo aberto pela lista, só para ler)

### `data-emoji`

- **Onde:** `.custom-css-chat-reaction` e `.custom-css-chat-action-react`
- **Valores:** o próprio emoji

### `data-encerrado`

- **Onde:** `.custom-css-chat-list-item`
- **Valores:** `true` · `false`. No item atual é o estado de agora: acompanha o encerrar e o reabrir sem recarregar a página

### `data-estilo`

- **Onde:** `.custom-css-chat-interactive` (só quando `data-tipo` é `opcoes`)
- **Valores:** `botoes` · `lista` · `texto` — o estilo que o menu tem no fluxo. O menu de texto também vira botões na página

### `data-etapa`

- **Onde:** `.custom-css-chat-entrada`
- **Valores:** `formulario` (o formulário de entrada) · `pergunta` (há uma conversa lembrada neste navegador: continuar ou começar outra)

### `data-gravando`

- **Onde:** `.custom-css-chat-recbar`
- **Valores:** `true` enquanto o áudio é gravado (a barra está à vista) · `false`

### `data-id`

- **Onde:** `.custom-css-chat-row`
- **Valores:** o id da mensagem na plataforma. É o alvo do clique na citação; a bolha recém-enviada ganha o id quando o servidor responde

### `data-media-type`

- **Onde:** `.custom-css-chat-row`
- **Valores:** `text` · `image` · `audio` · `video` · `doc`

### `data-nao-lidas`

- **Onde:** `.custom-css-chat-list-item` (só o atual)
- **Valores:** quantas mensagens do atendente chegaram na conversa atual enquanto ela não estava à vista; o atributo some quando o visitante volta a ela

### `data-opcao`

- **Onde:** `.custom-css-chat-interactive-button` (os de responder), `.custom-css-chat-product-card` e `.custom-css-chat-sheet-option`
- **Valores:** o que o clique responde: o número da opção, o valor do botão, o código do produto

### `data-optimistic`

- **Onde:** `.custom-css-chat-row`
- **Valores:** `1` enquanto a mensagem do visitante ainda não foi confirmada pelo servidor; o atributo some na confirmação (o `data-status` vira `sent`)

### `data-protocolo`

- **Onde:** `.custom-css-chat-list-item`
- **Valores:** o número do protocolo. Vazio no item do ticket sem protocolo (anterior aos protocolos), que só aparece quando é o do link

### `data-quoted-id`

- **Onde:** `.custom-css-chat-quote`
- **Valores:** o id da mensagem citada

### `data-reacted`

- **Onde:** `.custom-css-chat-row`
- **Valores:** `true` quando o visitante reagiu a esta mensagem · `false`

### `data-reactions`

- **Onde:** `.custom-css-chat-row`
- **Valores:** as reações em JSON. Uso interno da página (é como o poll sabe se mudou); para estilizar use `data-reacted` e as `.custom-css-chat-reaction`

### `data-status`

- **Onde:** `.custom-css-chat-row`
- **Valores:** `sent` · `received` · `pending` (a mensagem do visitante ainda não confirmada pelo servidor) · `failed`

### `data-tela`

- **Onde:** `.custom-css-chat-app`
- **Valores:** `conversa` · `lista` — qual coluna está à vista no celular (a página abre na `conversa`; a seta do topo leva à `lista`). No computador as duas aparecem, e o valor guarda a última escolha

### `data-tipo`

- **Onde:** `.custom-css-chat-interactive`, `.custom-css-chat-interactive-button` e `.custom-css-chat-interactive-list-button`
- **Valores:** na mensagem: `opcoes` (um menu, a avaliação, as escolhas de um robô) · `botoes` · `contato` · `localizacao` · `modelo` · `catalogo`. No botão: `resposta` · `link` · `ligar` · `copiar` · `quero` (o "Quero este" do produto) · `lista` (o que abre a folha)

### `data-wid`

- **Onde:** `.custom-css-chat-row`
- **Valores:** o identificador da mensagem no canal (`ext_…` quando o visitante escreveu pela própria página)

> ⚠️ **`out`/`in`.** As classes originais da página continuam lá, mas ali `out` é a mensagem do **visitante** — o inverso do `fromMe` do resto da plataforma. Use `data-autor`, que não tem essa inversão.

```css
.custom-css-chat-header { background: #101014; }
.custom-css-chat-row[data-autor="atendente"] .custom-css-chat-bubble { background: #1f6feb; color: #fff; }
.custom-css-chat-row[data-reacted="true"] .custom-css-chat-bubble { outline: 1px solid #1f6feb; }
.custom-css-chat-row[data-status="failed"] .custom-css-chat-bubble { outline: 1px solid #d33; }
```
