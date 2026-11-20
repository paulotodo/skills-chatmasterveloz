<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-30.141.0 -->

# Classes sem prefixo

Partes do Chat que já tinham nome antes da convenção `custom-css-`: o cartão do ticket, o cabeçalho do atendimento, a conversa e o painel do contato. Os nomes continuam os mesmos e valem como as outras âncoras — 69 classes, na ordem da tela:

| Classe | Onde | O quê |
|---|---|---|
| `.ticket-channel-icon` | todo ícone de canal | o ícone do canal (WhatsApp, Instagram…), com `data-channel`. É o mesmo no cartão do ticket, no cabeçalho do atendimento e nas outras telas que mostram o canal |
| `.ticket-name` | cartão do ticket | o nome do contato — ou o do grupo, no cartão de grupo |
| `.ticket-elapsed` | cartão do ticket | o tempo desde a última atualização, entre parênteses, ao lado do nome; a cor diz quanto tempo faz, e o estado está em `data-elapsed-status` e `data-elapsed-late` |
| `.ticket-datetime` | cartão do ticket | a hora da última atualização, à direita: de hoje, só a hora; de outro dia, a data e a hora |
| `.ticket-date` | cartão do ticket | a data, dentro do `.ticket-datetime` — só quando não é de hoje |
| `.ticket-time` | cartão do ticket | a hora, dentro do `.ticket-datetime` |
| `.ticket-waiting` | cartão do ticket | junto do `.ticket-datetime`, no atendimento ainda sem mensagem: o aviso que toma o lugar da hora |
| `.ticket-secondary` | cartão do ticket | a parte de baixo do cartão: a prévia, as faixas e o selo de não lidas |
| `.ticket-primary` | cartão do ticket | a parte de cima do cartão: os ícones, o nome e o tempo — como a `.ticket-secondary` é a de baixo |
| `.ticket-primary-line` | cartão do ticket | dentro da `.ticket-primary`, a linha: o ícone do grupo, o do canal, o olho do Espiar e o nome |
| `.ticket-primary-name` | cartão do ticket | dentro da linha, o nome e o tempo (`.ticket-name` e `.ticket-elapsed`) e o selo da busca na mensagem |
| `.ticket-avatar` | cartão do ticket | a coluna da foto, com a estrela de favoritar embaixo |
| `.ticket-divider` | cartão do ticket | o divisor entre um cartão e o próximo |
| `.ticket-preview` | cartão do ticket | o bloco da prévia da última mensagem, com as duas faixas (`.ticket-badges` e `.ticket-tags`) dentro dele |
| `.ticket-preview-text` | cartão do ticket | o texto da prévia: a última mensagem, cortada, ou `---` quando não há o que mostrar |
| `.ticket-badges` | cartão do ticket | a faixa das pílulas: a conexão, o atendente, os convidados e a fila |
| `.ticket-connection` | cartão do ticket | a pílula da conexão, com `data-connection-color` |
| `.ticket-user` | cartão do ticket | a pílula do atendente, com `data-user-color` |
| `.ticket-collaborators` | cartão do ticket | a pílula dos convidados ("+1"), com quantos em `data-count` e os nomes em `data-names` |
| `.ticket-queue` | cartão do ticket | a pílula da fila, com `data-queue-color` — `#7c7c7c` no atendimento sem fila |
| `.ticket-tags` | cartão do ticket | a faixa das etiquetas do contato |
| `.ticket-title` | cabeçalho do atendimento | o título: o nome, a presença, o número do atendimento e o protocolo, com `data-ticket-name`, `data-ticket-id` e `data-ticket-protocol` |
| `.ticket-title-name` | cabeçalho do atendimento | o nome do contato, com o nome inteiro em `data-full-name` (no celular, o texto é cortado) |
| `.ticket-presence` | cabeçalho do atendimento | a presença do contato, ao lado do nome, com `data-presence-state` — é o mesmo elemento da `.custom-css-ticket-presence` |
| `.ticket-title-id` | cabeçalho do atendimento | o número do atendimento, entre parênteses |
| `.ticket-title-protocol` | cabeçalho do atendimento | o protocolo (o `#123` do fim, com o separador antes dele), só no atendimento que tem um |
| `.ticket-operator-label` | cabeçalho do atendimento | o rótulo antes do nome do atendente |
| `.ticket-operator` | cabeçalho do atendimento | o nome do atendente, com `data-operator-id` |
| `.ticket-collaborator` | cabeçalho do atendimento | cada convidado, com `data-user-id` |
| `.ticket-collaborators-more` | cabeçalho do atendimento | o "+N" dos convidados que não couberam, com quantos em `data-count` |
| `.message-date-divider` | conversa | o divisor de data entre os dias da conversa |
| `.message-date-divider-label` | conversa | a data dentro do `.message-date-divider` |
| `.message-avatar` | conversa | a foto ao lado do balão, com `data-avatar`: `contact` (o contato) · `user` (o atendente) · `none` (mensagem sem atendente registrado, um círculo cinza) |
| `.message-quoted` | conversa | a mensagem citada (a resposta a outra mensagem), dentro do balão |
| `.message-quoted-body` | conversa | o conteúdo da citação |
| `.message-quoted-author` | conversa | o nome de quem escreveu a mensagem citada — só quando foi o contato |
| `.message-deleted` | conversa | o aviso de mensagem apagada, no balão do contato, com `data-apagada-por`; e o mesmo aviso na página do atendimento (`#custom-css-atendimento-report`), sem o atributo |
| `.message-meta` | conversa | a data e a hora dentro do balão; nas mensagens enviadas, também o nome do atendente e os checks de entrega |
| `.message-edited` | conversa | o "Editada" ao lado da hora, nas mensagens enviadas: a empresa editou a mensagem (pela plataforma ou pelo aparelho) e o texto do balão já é o novo, como o cliente vê; leva `data-edited="user"` |
| `.message-origin-app` | conversa | o celular ao lado da hora: a mensagem foi enviada pelo aparelho, e não pela plataforma |
| `.message-origin-hybrid` | conversa | o símbolo da rota híbrida ao lado da hora: a mensagem saiu pela plataforma e por fora da API oficial ao mesmo tempo (os dois símbolos podem aparecer juntos) |
| `.message-internal` | conversa | o balão da nota interna. Sozinha, é o recado do time; com uma das três abaixo, é outro assunto |
| `.message-internal-error` | conversa | junto da `.message-internal`: o retorno de erro (vermelho, sem título) |
| `.message-internal-action` | conversa | junto da `.message-internal`: o registro do atendimento (verde) |
| `.message-internal-info` | conversa | junto da `.message-internal`: o aviso informativo (sem título) |
| `.message-internal-title` | conversa | o título do balão da nota interna ("Comunicação interna" ou "Registro do atendimento") — o erro e o aviso não têm título |
| `.message-internal-text` | conversa | o texto do balão da nota interna |
| `.contact-drawer-header` | painel do contato | o topo do painel: a primeira linha e, quando a conexão tem integração, as abas |
| `.contact-drawer-topo` | painel do contato | a primeira linha: o X (`data-action="fechar"`) e o título |
| `.contact-drawer-titulo` | painel do contato | o título do painel |
| `.contact-drawer-body` | painel do contato | o corpo do painel, com os cartões |
| `.contact-drawer-iframe` | painel do contato | a caixa da aba de integração, com o iframe da conexão — o conteúdo é de outro site e não se estiliza; o quadro (altura, borda, fundo), sim |
| `.contact-card` | painel do contato | o cartão do contato: a foto, o nome, o número e o botão Editar |
| `.contact-card-foto` | painel do contato | a caixa da foto, no cartão do contato |
| `.contact-card-nome` | painel do contato | o nome do contato — o clique abre o formulário de edição |
| `.contact-card-telefone` | painel do contato | a linha do número: o link `tel:`, ou o número mascarado quando ele está oculto para quem vê |
| `.contact-card-email` | painel do contato | a linha do e-mail |
| `.contact-card-editar` | painel do contato | o botão Editar do cartão (`data-action="editar"`) |
| `.contact-lid` | painel do contato | a linha do LID — some quando o número está oculto para quem vê |
| `.contact-jid` | painel do contato | a linha do JID — some quando o número está oculto para quem vê |
| `.contact-lid-jid` | painel do contato | a linha LID => JID — some quando o número está oculto para quem vê |
| `.contact-permissao-chamada` | painel do contato | a linha da permissão de ligação, com `data-permissao` — é o mesmo elemento do `#custom-css-contact-permissao-chamada` |
| `.contact-pedidos-card` | painel do contato | o cartão dos pedidos do cliente (só com o PDV): os últimos pedidos, as contas e o "Repetir pedido" |
| `.contact-notes-card` | painel do contato | o cartão das anotações do contato |
| `.contact-note-field` | painel do contato | o campo de escrever a anotação |
| `.contact-note-input` | painel do contato | a caixa do campo (a borda e o fundo), dentro do `.contact-note-field` |
| `.contact-note-list` | painel do contato | a lista das anotações — só quando há alguma |
| `.contact-note-actions` | painel do contato | os botões do cartão das anotações |
| `.contact-extra-card` | painel do contato | o cartão das informações extras do contato |

```css
/* no cartão do ticket, o nome em negrito e o tempo menor */
.ticket-name { font-weight: 700; }
.ticket-elapsed { font-size: .75em; }

/* a citação com a borda na cor principal */
.message-quoted { border-left: 3px solid var(--app-primary); }
```
