<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-29.930.0 -->

# Atributos de estado

Formato: um título `###` por **Atributo** (341 itens), com os campos Onde · Valores abaixo.

### `data-aba`

- **Onde:** cada aba da lista de atendimentos (`.custom-css-ticket-tabs .MuiTab-root`), na visão individual e na de grupos; e cada aba da faixa Ticket / Atendimentos do celular (`.custom-css-mobile-tab`)
- **Valores:** `open` (Atendendo) · `pending` (Aguardando) · `pending-meus` (Aguardando (MEUS), só com a configuração "Aguardando com dono" ligada) — o mesmo vocabulário do `data-status` do cartão. No celular: `ticket` (a conversa aberta) · `atendimentos` (a lista), com a escolhida em `aria-selected`

### `data-aberto`

- **Onde:** painel que o "+" abre no campo de digitação; e o botão de figurinhas do compositor do Hub; e o painel do contato (`.custom-css-contact-drawer`)
- **Valores:** `true` · `false` — antes o estado só existia como `display: none` inline. No botão de figurinhas: se o seletor está aberto. No painel do contato: se ele está aberto — antes, fechado só se via pelo `visibility: hidden` que o Material-UI põe no estilo

### `data-acao`

- **Onde:** os botões de ação dos cartões e das tabelas dos cadastros: Tags, Setores, Respostas Rápidas, Categorias (de setores e de fluxos), Usuários (o cartão e as janelas de encerrar e de transferir os tickets), Contatos, Webhooks, Templates WABA, Arquivos do Bot, Contas de e-mail e Avaliações
- **Valores:** o verbo do botão, em português. Em toda tela: `editar` · `excluir`. E os de cada uma — Tags: `ver-contatos`. Respostas Rápidas: `favoritar` (a estrela, também `.custom-css-quickmessage-favorita`). Usuários, no cartão: `encerrar-tickets` · `transferir-tickets` · `transferir-carteira` · `trocar-senha` · `acessos` (o histórico de entradas e saídas, `.custom-css-user-btn-acessos`); nas janelas de encerrar e de transferir os tickets: `cancelar` · `confirmar`. Contatos, na tabela: `resumo` · `iniciar-conversa` · `mais-acoes` (os três pontinhos do celular, que abrem o menu com os mesmos nomes em `data-menu-action`). Webhooks: `configurar` (abre o fluxo do webhook). Templates WABA: `visualizar` · `ver-json` · `editar-midia-local` (o botão que troca a mídia de exemplo) · `enviar-para-aprovacao`. Arquivos do Bot: `copiar-url`. Contas de e-mail: `adicionar` Usuários, no cartão (29.521.0): `presenca` — a bolinha do status e da sessão da pessoa (`.custom-css-user-btn-presenca`), com o status em `data-status`. No atendimento do canal Chat Externo (29.524.0), o botão de bloquear a conversa: `bloquear-conversa` · `desbloquear-conversa` — o mesmo valor do `data-action` dele. Só no botão: recolhida no menu `⋯` da barra, a ação vira um item que leva só o `data-action`.

### `data-acao-funil`

- **Onde:** cartão do funil, no CRM v2
- **Valores:** `arquivar` · `reativar`

### `data-aceite`

- **Onde:** cada chave do aceite automático no topo do Painel de Pedidos (`.custom-css-painel-de-pedidos-aceite`)
- **Valores:** `fora` (os pedidos de fora: Cardápio, Loja, atendimento e balcão) · `mesa` (os pedidos das mesas — só aparece para quem tem mesas no salão)

### `data-acesso`

- **Onde:** cada linha do histórico de entradas e saídas do operador (botão "Acessos" no card da tela de Usuários)
- **Valores:** `LOGIN` · `LOGOUT` — dá para colorir a entrada e a saída de formas diferentes, ou esconder uma das duas

### `data-ack`

- **Onde:** balão da mensagem
- **Valores:** 0–5, o código bruto de entrega do WhatsApp

### `data-action`

- **Onde:** botões do atendimento, da lista de atendimentos, do popup de encerramento, do Chat Interno, do painel do contato, do editor de fluxo, do Quadro de Atendimentos, dos Kanbans e do CRM
- **Valores:** na barra: `mark-as-read` (o "Marcar como lido", só com mensagem não lida) · `mark-as-unread` (o "Marcar como não lido", no mesmo lugar, quando não há não lidas — fora do atendimento encerrado) · `accept` (o Aceitar, no atendimento aguardando) · `finish` (o Encerrar, ao lado dele — só para admin e supervisor) · `resolve` · `return` · `transfer` · `schedule` · `task` · `delete` · `invite` · `call` · `files` · `flow` · `opportunity` · `summary` · `analyzer` · `contact-summary` · `accept-audio` · `external-chat-link` · `video-call` (a videochamada com o cliente) · `pdv-order` (o pedido do PDV) · `pdv-consulta` (a consulta de preço e estoque) · `mais-acoes` — são esses os nomes que a `--ticket-actions-ordem` e a `--ticket-actions-no-menu` usam (ver Propriedades). No celular, as ações ficam no menu de Ações (`.custom-css-ticket-actions-mobile` é a caixa dos botões), e `mais-acoes` é o botão que abre esse menu. No popup de encerramento: `resolve-silent` (sem mensagem) · `resolve-message` (com mensagem) · `resolve-rating` (com avaliação) — os dois primeiros são idênticos no DOM, só o texto difere. Os mesmos três valores estão nas três saídas da Tela 3 do encerramento em 3 passos (`.custom-css-modal-encerramento`), onde `resolve-message` é o botão verde, principal. No campo de mensagem (os dois compositores): `send` — o botão de enviar, que vira `forward` enquanto o modo de selecionar mensagens está ligado (o mesmo botão encaminha as escolhidas); `upload` (anexar) · `record-audio` (gravar áudio) · `emoji` · `send-contact` (enviar contato); `external-only` — o "Somente chat externo", com `aria-pressed`, como `signature` e `internal` ao lado; `extras` — o "+" que abre o painel de extras, com `aria-expanded`; `fechar-extras` — o X desse painel. Nos dois: `ver-notas-internas` — o botão das notas internas, que abre o `.custom-css-popover-notas-internas`. Só no compositor do Hub: `figurinhas` (o botão que abre o seletor de figurinhas) · `quick-favorites` (as mensagens rápidas favoritas) · `contact-notes` (as notas do contato). No menu `⋯` da barra, o item de uma ação que é interruptor (`accept-audio`) é `role="menuitemcheckbox"` com `aria-checked` — o estado de verdade, e o clique nele liga e desliga. No Chat Interno, em cada conversa da lista (`.custom-css-chats-item`): `favorite` · `mark-unread` (só na conversa sem nada por ler) · `edit` (só para quem criou a conversa) · `delete` (para quem criou e para o admin); no campo de mensagem (`.custom-css-chats-composer`): `record-audio` · `upload` · `send` — os mesmos nomes do campo de mensagem do atendimento. No painel do contato (`.custom-css-contact-drawer`): `fechar` — o X do topo, que também ganhou `aria-label`; `editar` — o botão Editar do cartão (`.contact-card-editar`). Na lista de atendimentos (`#custom-css-tickets-page`): `new-ticket` (o Novo) · `sort` (o Ordenar) · `more-filters` (o "+" que abre os filtros) · `advanced-search` (a Busca Avançada); e, no cartão do ticket, `accept` (o Aceitar do aguardando) · `spy` (o olho do Espiar) · `finish` (o Encerrar do aguardando, só para admin e supervisor). No card do Quadro de Atendimentos: `pin` (a estrela de fixar, `.custom-css-quadro-fixar`) · `finish` (o Encerrar, `.custom-css-quadro-encerrar`, quando o encerrar está ligado na barra do quadro). No card dos quatro Kanbans: `spy` (o olho, que abre a conversa numa janela). No editor de fluxo, na barra de cima (`.custom-css-flow-barra`): `desfazer` · `refazer` · `buscar` · `resumo` · `organizar` · `verificar` · `versoes` · `salvar` — os três que abrem um painel (`buscar`, `resumo` e `versoes`) dizem em `aria-pressed` se ele está aberto; em cada bloco do desenho do fluxo (`.custom-css-flow-node-acoes`): `copiar` · `excluir`; e, na janela de escolher o bloco (`.custom-css-flow-escolher-item`), o tipo do bloco que o item cria (`menu`, `question`, `switch`…). Nas atividades da oportunidade (`.custom-css-atividades`): `criar-atividade` (criar, ou salvar a que está em edição) · `cancelar-edicao` · `editar-atividade` (o assunto, que abre a atividade para editar) · `concluir` / `reabrir` (o que o clique FAZ, conforme a atividade está aberta ou concluída) · `anexos` · `excluir` · `abrir-reuniao` (o link da reunião) · `copiar-link`. Na conexão do Google Calendar (`.custom-css-google-calendar-conexao`): `conectar-calendar` · `desconectar-calendar` · `escolher-agenda`. Na conciliação de conexões (`.custom-css-conciliacao-conexoes`): `filtrar-excedente` · `baixar-csv` · `detalhar-empresa` (abre e fecha a linha da empresa) · `limpar-conexoes` (apaga as conexões da empresa). Nas regras de encadeamento dos funis do CRM: `adicionar-regra` · `remover-regra`. No atendimento do canal Chat Externo, a barra (e o menu de Ações do celular) tem também `bloquear-conversa` · `desbloquear-conversa` — o que o clique faz, conforme a conversa está liberada ou bloqueada; o mesmo valor vai no `data-acao` do botão — recolhida no menu `⋯` da barra, o item leva só o `data-action`, como todo item desse menu · No Chat Interno, na conversa aberta: `buscar-na-conversa` (a lupa do cabeçalho, que abre a busca) e, na busca, `fechar-busca`; no campo de mensagem, `emoji` e `figurinhas` (os seletores); na barra da mensagem em edição, acima do campo (`.custom-css-chat-interno-editando`), `cancelar-edicao` — o X que desiste · No cartão do #protocolo do chat interno (`.custom-css-chats-protocolo`), `espiar-protocolo` — o olho, que abre a conversa do atendimento · no Cardápio Digital: `novo-cupom` (abre a janela do cupom novo) · `editar-cupom` · `remover-cupom` · `salvar-cupom` (o botão da janela) · na Avaliação pela IA: `salvar-avaliacao-ia` (o Salvar da configuração) · `avaliar-agora` (roda a avaliação na hora) · `exportar-avaliacoes` (baixa a lista em CSV) · `abrir-conversa` (abre o atendimento avaliado) · `marcar-aula-vista` (marca a aula como lida) · no Consultório: `abrir-teleconsulta` (abre a sala da teleconsulta, na recepção) · `copiar-link-teleconsulta` (copia o link do paciente) · `enviar-link-teleconsulta` (manda o link no atendimento, no painel do contato) · no prontuário: `abrir-prontuario` (o botão na lista de pacientes) · `registrar-prontuario` (salva o registro, ou a retificação) · `retificar-prontuario` (escreve a correção de um registro) · `criar-chave-prontuario` e `restaurar-chave-prontuario` (o botão da chave, nas opções do Consultório) · `novo-modelo-documento` e `salvar-modelo-documento` (os modelos de documento, nas opções do Consultório) · `novo-documento`, `emitir-documento`, `pdf-documento`, `cancelar-documento` e `confirmar-cancelamento-documento` (os documentos do paciente, na janela do prontuário) · `enviar-documento` (enviar o documento, no painel do contato) · `nova-receita`, `adicionar-item-receita`, `remover-item-receita` e `emitir-receita` (a receita, nos documentos do paciente) · `cobranca-da-consulta` (abre a cobrança da consulta, no painel do contato)

### `data-active`

- **Onde:** item do menu lateral e cartão do menu da tela de Configurações
- **Valores:** `true` / `false` no item do menu lateral — `true` em **um item só**, o da tela aberta: quando um destino é prefixo de outro que também está no menu (`/ratings` e `/ratings/report`), só o mais específico acende; rota aninhada que não está no menu (`/tickets/<id>`) acende o item pai · `true` / `false` no cartão de Configurações, conforme a aba aberta

### `data-agendamento`

- **Onde:** cada cartão da agenda do Consultório (`.custom-css-consultorio-agenda-cartao`), na página `/consultorio-agenda`
- **Valores:** o id da consulta ou do bloqueio do cartão — o mesmo cartão aparece com o mesmo valor no dia e na semana. O tipo e o status vão na classe (`custom-css-consultorio-agenda-bloqueio`, `-agendado`, `-confirmado`, `-atendido`, `-faltou`, `-cancelado`)

### `data-aguardando`

- **Onde:** aviso de coluna pausada no quadro de atendimentos
- **Valores:** quantas atualizações chegaram enquanto a coluna está pausada (`0` quando nada mudou) — dá para esconder o aviso quando não há nada esperando

### `data-aguardando-envio`

- **Onde:** selo na mensagem represada pelo concatenador
- **Valores:** `true` — a mensagem existe e ainda não saiu

### `data-alterada`

- **Onde:** janela do editor de imagem (`.custom-css-modal-editor-de-imagem`)
- **Valores:** `true` quando já há alguma edição (e fechar pede confirmação) · `false` — concluir sem edição devolve a foto original, sem recomprimir

### `data-alvo-id`

- **Onde:** cada regra por funil ou por etiqueta da janela de Pontuação e níveis (`.custom-css-gamificacao-regra` com `data-regra="funil"` ou `data-regra="etiqueta"`)
- **Valores:** o id do funil ou da etiqueta da regra

### `data-amqp-vazio`

- **Onde:** aviso de monitor AMQP sem mensagem
- **Valores:** `sem-fila` (nenhuma conexão da empresa passa por RabbitMQ) · `sem-mensagem` (passa, mas nada chegou)

### `data-animada`

- **Onde:** a mesma figurinha
- **Valores:** `true` quando o WebP é animado · `false`

### `data-answer-from-ia`

- **Onde:** sugestão de resposta com IA (barra e cartão sobre o campo, e a aba de Tokens de IA)
- **Valores:** no bloco: `barra` · `cartao`. Dentro dele: `sugerir` · `melhorar` · `saldo` · `sugestao` · `texto` · `usar` · `nova` · `descartar`. Na aba do super: `ilimitado` · `abrir-recarga` · `recarga-pontos` · `recarga-observacao`

### `data-answer-from-ia-camada`

- **Onde:** painel flutuante da sugestão de IA
- **Valores:** `padrao` · `acima-do-dialogo` — quando a barra vive dentro de um diálogo, o painel precisa ficar acima dele

### `data-apagada`

- **Onde:** balão de mensagem do chat interno
- **Valores:** `true` · `false` — se a mensagem foi apagada

### `data-apagada-por`

- **Onde:** balão de mensagem apagada
- **Valores:** quem apagou (o nome), ou `desconhecido` quando o registro não diz

### `data-appbar`

- **Onde:** botões da barra do topo
- **Valores:** `menu` · `tickets` (o balão dos atendimentos) · `notifications` (o sino) · `push` (o sino das notificações push, com `aria-pressed`: ligadas ou não neste navegador) · `announcements` · `internal-chat` (o Chat Interno; antes era `msgs`) · `status` · `extension` (o ramal) · `dialer` (o discador) · `theme` · `lang` · `font` · `sound` · `ping` · `refresh` · `collapse` · `user` · `mais` (o "+" do celular, que abre o menu com o idioma, a latência, o atualizar e o tema — o atualizar e o tema, dentro dele, levam os mesmos `refresh` e `theme`)

### `data-atalho`

- **Onde:** botões de atalho do valor na Tela 2 do encerramento em 3 passos (`.custom-css-encerramento-atalho`)
- **Valores:** `50` · `100` · `500` (somam ao valor) · `limpar` (zera)

### `data-ativa`

- **Onde:** chip de pasta no seletor de figurinhas e item de pasta na tela de Figurinhas; e, no editor de imagem, cada botão de ferramenta (`.custom-css-editor-de-imagem-ferramenta`) e cada cor da paleta (`.custom-css-editor-de-imagem-cor`)
- **Valores:** `true` na pasta aberta · `false`. No editor: `true` na ferramenta em uso e na cor escolhida · `false`

### `data-ativo`

- **Onde:** o cartão de cada fluxo na lista de fluxos (`.custom-css-flow-card`) e a etiqueta de estado dele (`.custom-css-flow-card-status`)
- **Valores:** `true` no fluxo ativo · `false` no desativado — o mesmo que a etiqueta diz

### `data-atrasada`

- **Onde:** atividade do CRM (painel e cartão) e o cartão de tarefa (`.custom-css-task-card`)
- **Valores:** `true` quando o prazo passou — o único estado que pede ação agora. Ausente nos outros casos. Na tarefa: pendente, e o dia (o que a tela mostra) já passou, ou é hoje e já passou da hora marcada; tarefa concluída nunca está atrasada

### `data-audio`

- **Onde:** gravador de áudio do campo de digitação
- **Valores:** no bloco: `gravando` · `pausado`. Dentro dele: `player` · `pausar` · `continuar`

### `data-auditoria`

- **Onde:** cartão da oportunidade no quadro do CRM v2
- **Valores:** o status da auditoria daquela venda

### `data-auditoria-acao`

- **Onde:** botões da fila do auditor
- **Valores:** `aprovar` · `reprovar`

### `data-auditoria-propria`

- **Onde:** cartão na fila do auditor
- **Valores:** `sim` quando a venda é do próprio auditor — é o cartão que aparece com os botões desligados

### `data-auditoria-status`

- **Onde:** linha do histórico de auditoria
- **Valores:** `APROVADA` · `REPROVADA`

### `data-aula`

- **Onde:** cada aula da IA (`.custom-css-avaliacao-ia-aula`)
- **Valores:** o id da aula

### `data-avaliacao`

- **Onde:** cada linha da tabela dos atendimentos avaliados (`[data-lista="avaliacoes"]`)
- **Valores:** o id da avaliação

### `data-avatar`

- **Onde:** avatar no balão
- **Valores:** `contact` · `user` · `ia` (a mensagem do assistente de IA, com o selo IA) · `none`

### `data-badge`

- **Onde:** selo do modo da conta Meta no cartão da conexão (`.custom-css-connection-badge`)
- **Valores:** o evento, em minúsculas: `live` · `sandbox` · `pending`, ou o evento que a Meta mandou (`account_disconnected`…). O nível vai em `data-nivel`

### `data-barra`

- **Onde:** cada barra do gráfico da distribuição das notas (`[data-grafico="distribuicao"]`)
- **Valores:** a nota daquela barra, de `0` a `10`

### `data-barra-concatenacao`

- **Onde:** barra que avisa que a próxima mensagem será concatenada
- **Valores:** `true`

### `data-bot-ativo`

- **Onde:** cartão do ticket (lista e grupos), cabeçalho da conversa aberta e os cards do quadro de atendimentos e dos kanbans
- **Valores:** `true` enquanto um nó do fluxo (flowbuilder) está rodando NESTE ticket — é o `flowStatus = executing`, a trava que impede duas execuções ao mesmo tempo; `false` nos demais estados. **Ausente quando o payload não traz `flowStatus`**: sem o campo, o card não afirma nada. Fluxo que morreu no meio pode deixar `true` para trás até a rotina de partida soltar a trava

### `data-botao`

- **Onde:** a caixa "Veio do Link na Bio" no painel do contato
- **Valores:** o id do botão da página do Link na Bio que abriu a conversa

### `data-busca`

- **Onde:** a busca na conversa do chat interno (`.custom-css-chats-busca-resultados`)
- **Valores:** `total` — a linha com quantas mensagens a busca achou · `vazia` — o aviso de que nenhuma mensagem tem o texto

### `data-cadastro-ativo`

- **Onde:** a mesma linha
- **Valores:** `true` · `false` — desativado continua na lista, não some

### `data-cadastro-funil`

- **Onde:** etiqueta do motivo de perda preso a um funil
- **Valores:** o id do funil. Motivo global não tem a etiqueta

### `data-cadastro-item`

- **Onde:** linha de origem de venda ou motivo de perda, nos Cadastros do CRM
- **Valores:** o id do item

### `data-call-direction`

- **Onde:** a janela da chamada
- **Valores:** `inbound` (a do receptor) · `outbound` (a do discador)

### `data-call-status`

- **Onde:** a janela da chamada (`.custom-css-modal-sip-receiver` e `.custom-css-modal-sip-dialer`) e o widget minimizado (`.custom-css-sip-widget`)
- **Valores:** na janela do receptor: `ringing` · `active` · `ended` · `failed` · `hungup` · `idle`. Na do discador: `idle` · `connecting` · `calling` · `active` · `ended` · `failed` · `disconnected`. No widget: `connecting` · `calling` (inclusive a chamada que chega e ainda não foi atendida) · `active`

### `data-campanha-id`

- **Onde:** cada campanha da janela de Campanhas (`.custom-css-gamificacao-campanha`); cada campanha na lista do seletor de período (`.custom-css-seletor-periodo-campanha`); e a linha da contagem do nível em Minha Evolução (`.custom-css-minha-evolucao-contagem`), quando o nível conta numa campanha
- **Valores:** o id da campanha

### `data-campo`

- **Onde:** formulário de atividade do CRM, seletor de motivo por funil e liberação de agenda
- **Valores:** na atividade: `tipo` · `responsavel` · `assunto` · `descricao` · `data` · `hora` · `duracao`, e `descricao-lista` no texto já gravado. Nos cadastros do CRM: `funil-do-novo`. Nas regras de encadeamento: `produto-da-regra` · `destino-da-regra` · `responsavel-da-regra`. No cadastro de usuário: `agendas-visiveis`. Nas tarefas: `filtro-de-agenda`

### `data-campo-responsavel`

- **Onde:** campo de responsável no modal da oportunidade
- **Valores:** `true` — marca o campo que define de quem é a venda

### `data-canal`

- **Onde:** linha de canal na conciliação de conexões e pílula do monitor AMQP
- **Valores:** a chave do grupo (`whatsapp`, `hub`, `instagramInc`, …)

### `data-carregados`

- **Onde:** o contador de cada aba da lista de atendimentos (`.custom-css-ticket-tabs-contador`, o `.MuiBadge-root` da aba), ao lado do `data-total`
- **Valores:** quantos atendimentos a lista já carregou

### `data-carregando`

- **Onde:** barra da sugestão de IA; o seletor de figurinhas do compositor; e a janela do editor de imagem (`.custom-css-modal-editor-de-imagem`)
- **Valores:** na IA: `true` enquanto a IA gera — é por ele que se estiliza o estado "Gerando sugestão…". No seletor: `true` enquanto as pastas carregam. No editor: `true` enquanto a foto abre · `false`

### `data-categoria`

- **Onde:** cartão de categoria do Criar Template (WABA)
- **Valores:** o tipo de modelo, como a Meta o chama: `STANDARD` (Padrão) · `CATALOG` · `ORDER_DETAILS` · `CALL_PERMISSION`. Os que aparecem dependem da categoria escolhida nas abas (Marketing, Utilidade, Autenticação). O escolhido leva `data-selected="true"`

### `data-causa`

- **Onde:** a linha de estorno do extrato de Minha Evolução (`.custom-css-minha-evolucao-movimento` com `data-estorno="true"`)
- **Valores:** por que a venda deixou de contar: `apagada` · `reaberta` · `perdida` · `emAuditoria` (voltou para a auditoria) · `reprovada` · `outroMes` (foi ganha de novo em outro mês) · `semDono` (ficou sem vendedor) · `metaDesfeita` (no bônus da meta, quando ela deixou de estar batida) · `outroFunil` (nos pontos por funil, quando a venda mudou de funil) · `semEtiqueta` (nos pontos por etiqueta, quando a etiqueta saiu da venda) · `encerramentoDesfeito` (nos pontos por encerramento, quando o encerramento com venda deixou de existir) · `outra`. Ausente fora do estorno

### `data-channel`

- **Onde:** cartão do ticket, CABEÇALHO da conversa aberta, ícone da conexão (`.ticket-channel-icon`, em toda tela) e cartão da conexão na tela de Conexões
- **Valores:** o canal da conexão, como está gravado nela — e `whatsapp` no atendimento antigo, sem canal. WhatsApp não oficial: `whatsapp` · `whatsapp_whatsmeow` · `whatsapp_whatsmeow_pro`. WhatsApp oficial: `whatsapp_meta` (direto com a Meta) · `whatsapp_business_account` (pelo HUB) · `whatsapp_gupshup` (pela Gupshup). Direto com a rede (`_inc`): `telegram_inc` · `facebook_inc` · `instagram_inc` · `tiktok_inc` · `webchat_inc` · `externalchat_inc` (o Chat Externo, com a página de entrada da própria conexão). Pelo portal, com o app da plataforma (`_portal`): `facebook_portal` · `instagram_portal`. Pelo HUB (sem sufixo): `telegram` · `instagram` · `facebook` · `messenger` · `mercado_livre` (ou `mercadolivre`) · `olx` · `sms` · `youtube` · `linkedin`. Outros: `webchat` · `rcs` · `email`

### `data-channel-filter`

- **Onde:** chips de filtro de canal, na página de Conexões
- **Valores:** `all` ou a chave do canal. Junto vai `aria-pressed`, que diz se o filtro está ligado

### `data-chat-externo`

- **Onde:** balão de mensagem vinda do chat externo
- **Valores:** `recebida` (veio de lá e está nas duas pontas) · `somenteExterno` (só existe no chat externo)

### `data-chat-id`

- **Onde:** cada conversa da lista do chat interno (`.custom-css-chats-item`) e os quatro botões dentro dela: favoritar, marcar como não lida, editar e excluir
- **Valores:** o id da conversa

### `data-collapsed`

- **Onde:** menu lateral
- **Valores:** `true` quando recolhido

### `data-colocacao`

- **Onde:** cada linha do ranking entre as lojas (`.custom-css-crm-ranking-grupo`)
- **Valores:** a colocação, de `1` em diante: o maior valor vendido primeiro, depois a maior quantidade, e o nome desempata

### `data-coluna-pausada`

- **Onde:** coluna do quadro de atendimentos
- **Valores:** `true` na coluna com a atualização pausada, `false` nas demais

### `data-coluna-tipo`

- **Onde:** coluna do quadro de atendimentos (no quadro e na tela de configuração)
- **Valores:** `PENDENTES` · `ATENDENDO` (as duas fixas) · `LIVRE` (aberto, criada pelo admin) · `PENDENTE_LIVRE` (pendente, classificação manual) · `PENDENTE_FILA` (pendente, automática: recebe sozinha os pendentes das filas da regra). Na visão por tags ("Ver o quadro por: Tags"): `TAG` (cada tag marcada como Kanban) · `SEM_TAG` (os atendimentos sem nenhuma delas)

### `data-comanda-id`

- **Onde:** cada conta aberta (e cada conta do Histórico) da página Mesas e Comandas (`.custom-css-comandas-aberta`)
- **Valores:** o id da conta (a comanda) — o mesmo do `comanda.id` do webhook

### `data-concat-example`

- **Onde:** prévia do texto concatenado, no modal do concatenador
- **Valores:** `true`

### `data-concat-field`

- **Onde:** campos do modal do concatenador
- **Valores:** `enabled` · `mode` · `timeout`

### `data-concat-indicator`

- **Onde:** selo de concatenação no cartão da conexão
- **Valores:** o id da conexão

### `data-condicao-tipo`

- **Onde:** cada condição no editor de regra do quadro (`.custom-css-regra-editor-condicao`)
- **Valores:** `TEXTO` · `TEM_TAG` · `NAO_TEM_TAG` · `FILA` · `CONTATO` · `CONEXAO` · `CLIENTE_ESPERANDO` · `CLIENTE_SEM_RESPONDER`

### `data-conectado`

- **Onde:** bloco de conexão do Google Calendar
- **Valores:** `true` · `false`

### `data-conexao`

- **Onde:** escolha do tipo de conexão, ao criar uma nova
- **Valores:** `sem-aparelho` · `oficial-app-proprio` · `oficial-portal` · `chat-externo` · `gupshup`

### `data-connected`

- **Onde:** botão do ramal na barra do topo (`[data-appbar="extension"]`) — o estado inteiro está no `data-status` do mesmo botão
- **Valores:** `true` · `false` — o estado do ramal. Sem ele, a única forma de saber se o ramal está conectado era ler a COR do ícone

### `data-connection`

- **Onde:** etiqueta verde da conexão no card do quadro de atendimentos
- **Valores:** o NOME da conexão ("Comercial", "Suporte"…) — dá para colorir o card por conexão, o que o `data-channel` não permite, porque ele só diz o canal

### `data-connection-action`

- **Onde:** botões do cartão de conexão
- **Valores:** `close-all` · `close-pending` · `templates` · `template-errors` (os templates que a Meta recusou) · `edit` · `delete` · `qrcode` · `profile` · `sip` · `sip-config` · `hybrid` · `proxy` · `rotate-ip` · `restart-pro` (reiniciar a conexão whatsmeow_pro) · `validate-code` (validar o código de registro) · `events` · `import-session` · `pair-code` · `passkey` · `reconnect` · `new-qr` · `disconnect` (Desconectar) · `delete-session` (Excluir Sessão: apaga a sessão, e o número precisa ler o QR de novo) · `send-limit` (o limitador de mensagens) · `concatenador` · `meta-recheck` (Verificar agora, na oficial nativa) · `meta-reconnect` (Reconectar, na oficial nativa) · `ig-check-subscription` (Verificar inscrição, no Instagram) · `copiar-link-entrada` (Copiar link de entrada, no canal Chat Externo) · `pause` · `resume` (pausar e retomar a conexão; só o admin vê, e o botão troca de valor conforme a conexão está pausada ou não). "Fechar Todos" e "Fechar Pendentes" são o mesmo botão no DOM — só o texto difere, e texto morre na troca de idioma. O "Conectando…", desabilitado, não tem ação No WhatsApp Gupshup: `copiar-url-gupshup` (copia a URL de recebimento para cadastrar no painel da Gupshup). No RCS: `copiar-url-rcs` (copia a URL do webhook para cadastrar no painel do provedor).

### `data-connection-color`

- **Onde:** etiqueta da conexão no cartão; e a pílula da conexão no card do Quadro (`.custom-css-quadro-conexao`)
- **Valores:** `green` (hoje é o único valor emitido)

### `data-connection-id`

- **Onde:** cartão da conexão e CABEÇALHO da conversa aberta
- **Valores:** o id da conexão. No cabeçalho é a conexão pela qual o atendimento entrou

### `data-connection-manual-review`

- **Onde:** aviso no cartão da conexão
- **Valores:** `true` quando o número está em revisão manual da Meta

### `data-connection-name`

- **Onde:** cartão do ticket e cabeçalho da conversa aberta
- **Valores:** o nome da conexão. Antes só existia como texto no cartão da lista (`.ticket-connection`), e a conversa aberta não dizia por onde tinha chegado

### `data-connection-status`

- **Onde:** cartão da conexão (e, com os mesmos valores, o cartão do ticket, o cabeçalho da conversa aberta, a faixa da conexão pausada acima do compositor, `.custom-css-ticket-conexao-pausada`, e os cards do Quadro e dos Kanban: `.custom-css-quadro-card`, `.custom-css-kanban-card`, `.custom-css-kanban-team-card` e `.custom-css-kanban-filas-card`)
- **Valores:** `connected` · `disconnected` · `qrcode` · `opening` · `error` · `paused` (pausada pelo admin: não recebe nem envia nada até ele retomar — não é queda). **É o estado como atributo**: antes ele existia só como cor do chip, e saber que uma conexão caiu exigia ler a cor computada ou o texto "Conectado" — cor muda com o tema e texto muda com o idioma. `PENDING` conta como `opening`; status desconhecido vira `error`

### `data-conta-como-venda`

- **Onde:** célula Valor da tabela da pesquisa de atendimentos (`.custom-css-atendimentos-valor`), para admin e supervisor
- **Valores:** `true` quando a tag do encerramento conta como venda (entra no total do rodapé) · `false` quando só registra o valor (a "Pesquisa de preço"). Ausente no atendimento que não passou pelos 3 passos

### `data-contact-id`

- **Onde:** cartão do ticket, cabeçalho da conversa aberta, ficha lateral do contato e a linha da tabela de Contatos
- **Valores:** o id do contato. A ficha **não publicava identificador nenhum** — nome, telefone e e-mail existiam só como texto, e ligar uma anotação ou um registro de CRM ao contato certo dependia de casar texto, que se repete entre contatos e muda quando alguém corrige um cadastro

### `data-contagem`

- **Onde:** a linha acima do nível em Minha Evolução (`.custom-css-minha-evolucao-contagem`), que diz de onde o nível conta
- **Valores:** `campanha` (o nível soma só os pontos da campanha) · `livre` (fora de campanha: o tempo entre uma campanha e outra). Na empresa sem campanha a linha não aparece, e o nível conta desde sempre

### `data-contato-id`

- **Onde:** cada cliente sugerido na busca do cliente da conta da mesa (`.custom-css-conta-da-mesa-cliente-sugerido`)
- **Valores:** o id do contato que a conta vai levar ao ser escolhido

### `data-copiado`

- **Onde:** botão de copiar de cada classe, atributo ou variável na página das classes (`.custom-css-documentacao-css-copiar`)
- **Valores:** `true` por dois segundos depois do clique, enquanto o aviso de copiado aparece · `false`

### `data-cor`

- **Onde:** cada cor da paleta do editor de imagem (`.custom-css-editor-de-imagem-cor`)
- **Valores:** a cor em hexadecimal: `#ffffff` · `#000000` · `#e53935` · `#fb8c00` · `#fdd835` · `#43a047` · `#1e88e5` · `#8e24aa`

### `data-count`

- **Onde:** o selo dos convidados no cartão do ticket (`.ticket-collaborators`); e o "+N" dos convidados que não couberam no cabeçalho do atendimento (`.ticket-collaborators-more`)
- **Valores:** no cartão, quantos convidados — o número do "+1". No cabeçalho, quantos ficaram de fora: os três primeiros aparecem pelo nome (`.ticket-collaborator`)

### `data-cupom`

- **Onde:** cada cupom na tela do Cardápio Digital (`.custom-css-cardapio-cupom`)
- **Valores:** o código do cupom

### `data-dash-view`

- **Onde:** cartões "O que você gostaria de ver?" do Dashboard; e os blocos da seção que cada um abre (`.custom-css-dashboard-painel`)
- **Valores:** `estatisticas` · `linha-do-tempo` · `equipe` · `relatorios` · `aniversariantes`. O cartão da seção aberta leva `aria-expanded="true"`; os outros, `false` — e o mesmo cartão fecha a seção. O bloco leva o MESMO valor do cartão que o abre (Linha do tempo, Equipe e Relatórios têm dois blocos cada)

### `data-deleted`

- **Onde:** balão da mensagem
- **Valores:** `true` quando apagada

### `data-dia`

- **Onde:** coluna do gráfico de logs do Pixel; e cada dia do calendário de Agendamentos (`.custom-css-agenda-dia`)
- **Valores:** a data daquele dia (`YYYY-MM-DD` no calendário)

### `data-dia-fechado`

- **Onde:** cada dia do editor de horário (`.horario-do-dia`) com a chave Aberto/Fechado — no Cardápio Digital (o horário da loja e o da mesa)
- **Valores:** `true` com a chave do dia desligada (o dia fechado) · `false` aberto

### `data-docker-aviso`

- **Onde:** avisos do cadastro por app próprio
- **Valores:** `numero-canonico` · `metodo-atendido`

### `data-docker-bloqueio`

- **Onde:** alerta de bloqueio no cadastro por app próprio
- **Valores:** o tipo do bloqueio devolvido pela Meta

### `data-docker-campo`

- **Onde:** campos de desafio no cadastro por app próprio
- **Valores:** `captcha` · `2fa`

### `data-docker-cooldown`

- **Onde:** alerta de espera no cadastro por app próprio
- **Valores:** o tipo da espera imposta pela Meta

### `data-docker-ddi`

- **Onde:** campo de DDI no cadastro por app próprio
- **Valores:** o DDI escolhido

### `data-docker-desafio`

- **Onde:** bloco do desafio no cadastro por app próprio
- **Valores:** `captcha` · `2fa`

### `data-docker-registro`

- **Onde:** etapas do cadastro por app próprio
- **Valores:** `numero` · `codigo`

### `data-editando`

- **Onde:** o formulário da janela de Campanhas (`.custom-css-gamificacao-campanha-form`)
- **Valores:** `true` quando o formulário está mudando uma campanha que já existe · `false` quando está criando uma nova

### `data-edited`

- **Onde:** balão da mensagem
- **Valores:** `contact` quando o contato editou

### `data-elapsed-late`

- **Onde:** tempo relativo no cartão do ticket
- **Valores:** `true` · `false` — a regra simples de "está atrasado", para o CSS não precisar listar quais estados contam como atraso

### `data-elapsed-status`

- **Onde:** tempo relativo no cartão do ticket
- **Valores:** `fresh` (até 30 min) · `warning` (até 60) · `late` (acima). Vem junto do `data-elapsed-late`, que é o mesmo em forma de sim/não

### `data-email-account`

- **Onde:** campos e botões do modal de conta de e-mail
- **Valores:** `carregar-pastas` · `nova-pasta` · `novo-endereco`

### `data-email-id`

- **Onde:** cada e-mail da lista da página E-mails (`.custom-css-emails-item`)
- **Valores:** o id do e-mail — com `.custom-css-emails-item-marcado` quando ele está selecionado para a ação em massa

### `data-embed-bloqueado`

- **Onde:** aviso do ticket incorporado quando ele não pode ser aberto
- **Valores:** `true` — marca o quadro que explica o motivo em vez da conversa

### `data-embed-motivo`

- **Onde:** aviso do ticket incorporado que não pôde abrir
- **Valores:** o motivo, para o CSS separar um do outro (o `data-embed-bloqueado` só diz QUE bloqueou)

### `data-emoji`

- **Onde:** botão de reação rápida no menu da mensagem do chat interno
- **Valores:** o próprio emoji

### `data-empresa`

- **Onde:** linha da empresa na aba de Tokens de IA
- **Valores:** o id dela

### `data-empty`

- **Onde:** bloco de estado vazio (`.custom-css-empty-state`)
- **Valores:** a tela, com o mesmo nome do `#custom-css-<página>`: `todolist` · `waba-templates` · `webhooks` · `audit-logs` · `pixel-logs` · `amqp-messages` · `tags` · `prompts` · `flowbuilders` · `services` · `products` · `quick-messages` · `queues` · `queue-categories` · `flow-categories` · `contact-lists` · `contact-list-items` · `campaigns` · `campaign-report` · `bot-files` · `kanban` · `kanban-team` · `kanban-grupos` · `oportunidades` · `pipeline` · `announcement-history` · `connections` · `propostas` · `contacts-duplicates` · `emails` · `thirdpart` · `documentacao-css` (a busca sem resultado, na página das classes). Telas com mais de um vazio levam o sufixo: `schedules-dia` · `schedules-historico` · `group-management-sem-conexao` · `group-management-sem-grupos` · `group-management-participantes` · `chats-conversa` (nenhuma conversa aberta, no computador e no celular) · `chats-lista` · `chats-popover` · `settings-empresas` (a lista de empresas em Configurações)

### `data-encontrado`

- **Onde:** o cartão do #protocolo (`.custom-css-chats-protocolo`)
- **Valores:** `true` — o atendimento existe (o cartão mostra o contato e tem o olho de espiar) · `false` — nenhum atendimento da empresa com esse protocolo

### `data-endereco`

- **Onde:** pílula de endereço aceito no modal de conta de e-mail
- **Valores:** o endereço que a conta aceita (recebidos pelo destinatário, enviados pelo remetente)

### `data-erro`

- **Onde:** diálogo de erro da Meta
- **Valores:** `mensagem` · `campos` · `alterna-bruto` (o botão que mostra a resposta crua da Meta)

### `data-erro-conexao`

- **Onde:** modal do Facebook nativo
- **Valores:** `true` no bloco que explica a falha de conexão

### `data-erro-da-api`

- **Onde:** balão da nota de erro (`.message-internal-error`), na conversa aberta e na espiada pelo olho
- **Valores:** o código que a API do canal devolveu, quando a tela mostra uma frase no lugar dele — hoje, `recipient_not_on_whatsapp` (a frase: Este número não está no WhatsApp). Só existe nos erros que a tela traduz; o texto do balão é a frase, no idioma de quem atende

### `data-error`

- **Onde:** balão da mensagem
- **Valores:** `true` no balão rosa (a plataforma não processou)

### `data-escopo`

- **Onde:** bloco de conexão do Google Calendar
- **Valores:** `operador` (cada um conecta a própria agenda) · `empresa` (uma conta para todos)

### `data-estado`

- **Onde:** raiz da página de documentação da API (`#custom-css-documentacao-api`, a rota `/api-docs`) e da página das classes (`#custom-css-documentacao-css`, a rota `/css-docs`), cada etapa do indicador do encerramento em 3 passos (`.custom-css-encerramento-etapa`) e o cartão de PDF do chat interno (`.custom-css-chat-pdf`); e cada bolinha do Adicionar das Respostas Rápidas (`.custom-css-quick-message-etapa`)
- **Valores:** na documentação da API: `carregando` (o Swagger UI ainda não subiu) · `pronto` · `erro` (os arquivos de `/swagger-ui/` não carregaram). Na página das classes: `carregando` · `pronto` · `erro` (o catálogo do idioma não carregou). Na etapa do encerramento: `ativa` · `feita` · `pendente` · `pulada` (a etapa Valor, quando a tag escolhida não pede valor). No cartão de PDF: `carregando` (ainda sem a primeira página — também enquanto o balão não apareceu na tela) · `pronto` (a primeira página está no cartão) · `erro` (PDF com senha, corrompido ou fora do ar: fica o símbolo do PDF, e o clique continua baixando). Na bolinha das Respostas Rápidas: `ativa` · `feita` · `pendente`, como no encerramento

### `data-estorno`

- **Onde:** cada linha do extrato de Minha Evolução (`.custom-css-minha-evolucao-movimento`)
- **Valores:** `true` na linha de estorno: a venda deixou de contar e devolveu os pontos que tinha rendido (os pontos vêm negativos) · `false` no lançamento comum

### `data-etapa`

- **Onde:** janela do encerramento em 3 passos (`.custom-css-modal-encerramento`), cada etapa do indicador (`.custom-css-encerramento-etapa`) e cada etapa do Criar Template (`.custom-css-waba-template-form-etapa`); e cada bolinha do Adicionar das Respostas Rápidas (`.custom-css-quick-message-etapa`)
- **Valores:** na janela, a tela aberta: `motivo` · `valor` · `confirmar` · `encerrado` (a tela de sucesso). Na etapa do indicador, o nome dela: `motivo` · `valor` · `confirmar` — o estado vai em `data-estado`. No Criar Template: `configurar` · `editar` · `enviar`, e a aberta leva `aria-current="step"`. Nas Respostas Rápidas: `tipo` (escolher Texto ou Arquivo) · `conteudo` (o formulário) — o estado vai em `data-estado`

### `data-excedente`

- **Onde:** linha da empresa na conciliação de conexões
- **Valores:** `true` quando ela usa mais conexões do que o plano permite

### `data-exemplo`

- **Onde:** o exemplo real dentro de uma aula da IA (`.custom-css-avaliacao-ia-aula`)
- **Valores:** o id da aula

### `data-exemplo-do-lote`

- **Onde:** a frase "Vai criar de … até …" da configuração das mesas e comandas (`.custom-css-comandas-configurar`)
- **Valores:** sem valor: só marca a frase (ela some quando os números não valem)

### `data-faixa`

- **Onde:** a etiqueta da nota de um atendimento avaliado pela IA (junto do `data-nota`)
- **Valores:** `promotor` (9-10) · `neutro` (7-8) · `detrator` (0-6)

### `data-favorita`

- **Onde:** estrela da mensagem rápida, na tela de Mensagens Rápidas
- **Valores:** `true` · `false` — se aquela mensagem está favoritada

### `data-favorita-id`

- **Onde:** item da lista de mensagens rápidas favoritas, no campo de digitação do HUB
- **Valores:** o id da mensagem rápida daquele item

### `data-favorite`

- **Onde:** cartão do ticket e a estrela dele; e o botão de favoritar de cada conversa do Chat Interno (`[data-action="favorite"]`)
- **Valores:** `true` · `false`

### `data-ferramenta`

- **Onde:** janela do editor de imagem (`.custom-css-modal-editor-de-imagem`) e cada botão de ferramenta dela (`.custom-css-editor-de-imagem-ferramenta`)
- **Valores:** no botão, a ferramenta dele: `recortar` · `desenhar` · `borrar` · `texto` · `emoji` · `figurinha`. Na janela, a que está em uso: `recortar` · `desenhar` · `borrar` · `texto` (a caixa de texto aberta) · `nenhuma` (tocar pega e arrasta textos, emojis e figurinhas)

### `data-figurinha`

- **Onde:** cada figurinha (botão no seletor do compositor; cartão na tela de Figurinhas)
- **Valores:** o id da figurinha

### `data-file-type`

- **Onde:** cada arquivo da janela Anexar Arquivos do Hub (`.custom-css-file-upload-hub-item`)
- **Valores:** `image` · `video` · `audio` · `document` — pelo tipo do arquivo; o que não é imagem, vídeo nem áudio (PDF, planilha, zip) é `document`

### `data-filter`

- **Onde:** filtros da lista de atendimento; e os botões de filtro do histórico de Agendamentos
- **Valores:** na lista: `scope` · `groups` · `closed` · `unread` · `queues` · `tags` · `users` · `connections`. No histórico de Agendamentos: `all` · `enviada` · `agendada` · `pendente` · `erro`. Nos dois, junto vai `aria-pressed`, que diz qual filtro está ligado

### `data-filtro`

- **Onde:** cada filtro da Pesquisar (`.custom-css-atendimentos-filtro`)
- **Valores:** `usuarios` · `conexao` · `status` · `origem` · `tags` · `contato` · `setores` · `transferencias` · `protocolo` · `data-inicial` · `data-final` · `data-por` · `valor-minimo` · `encerramento` · `texto`

### `data-filtro-operador`

- **Onde:** filtro de operador no quadro do CRM v2
- **Valores:** `true` — marca o campo

### `data-filtro-tag`

- **Onde:** filtro de etiqueta no quadro do CRM v2
- **Valores:** `true` — marca o campo

### `data-fixado`

- **Onde:** estrela de fixar no card do quadro de atendimentos
- **Valores:** `true` · `false`

### `data-flow-action`

- **Onde:** as ações do cartão de cada fluxo, na lista de fluxos (`.custom-css-flow-card-acoes`)
- **Valores:** `editar` — abre o fluxo no editor · `logs` — abre o histórico de execução do fluxo (só para o admin) · `mais` — abre o menu com as outras opções

### `data-flow-id`

- **Onde:** bloco de um nó de rodízio no relatório do rodízio; e o cartão de cada fluxo na lista de fluxos (`.custom-css-flow-card`)
- **Valores:** o id do fluxo, ou `legado` no grupo do que foi gravado antes da identificação por nó; vazio no grupo de um rodízio cadastrado. No cartão, sempre o id do fluxo

### `data-flow-log-detail`

- **Onde:** pilha de detalhe de uma falha do fluxo
- **Valores:** o id do registro

### `data-flow-log-row`

- **Onde:** linha de falha do fluxo
- **Valores:** o id do registro

### `data-flow-logs-empty`

- **Onde:** aviso de histórico de fluxo vazio
- **Valores:** `true`

### `data-flow-logs-level`

- **Onde:** filtro de nível no histórico do fluxo
- **Valores:** o nível (`warn`, `error`…) ou `all`

### `data-flow-logs-list`

- **Onde:** tabela de falhas do histórico do fluxo
- **Valores:** `true`

### `data-flow-logs-summary`

- **Onde:** tabela de resumo do histórico do fluxo
- **Valores:** `true`

### `data-flow-logs-window`

- **Onde:** filtro de janela de tempo no histórico do fluxo
- **Valores:** quantas horas

### `data-flow-status`

- **Onde:** os mesmos elementos do `data-bot-ativo`
- **Valores:** `executing` (um nó rodando agora) · `waiting_input` · `menu` · `pending` (fluxo parado, esperando o contato) · `idle` (nenhum fluxo em curso — também para quem nunca entrou num fluxo). Ausente quando o payload não traz o campo

### `data-fora-do-no`

- **Onde:** linha de operador no relatório do rodízio
- **Valores:** `true` quando o operador recebeu atendimentos mas não está mais na configuração do nó · `false`

### `data-fora-do-padrao`

- **Onde:** cartão da figurinha na tela de Figurinhas
- **Valores:** `true` quando não é 512×512 — a API oficial pode recusar; o wago costuma aceitar · `false`

### `data-forcar-hibrido`

- **Onde:** botão de forçar o envio pelo caminho híbrido, no compositor do Hub
- **Valores:** `true` quando o que for enviado a seguir — texto, arquivo ou figurinha — vai pela conexão whatsmeow_pro do modo híbrido · `false` no envio normal

### `data-fromme`

- **Onde:** balão e cartão; e o balão do chat interno (`.custom-css-chats-msg`)
- **Valores:** `true` quando saiu da plataforma · `false`. No chat interno: `true` na mensagem de quem está olhando (o balão da direita) · `false` na dos outros. A nota interna e o registro do atendimento (`.message-internal`) vêm SEM o atributo, na conversa aberta e no olho — até a 29.467.0 o olho os marcava com `true`

### `data-full-name`

- **Onde:** o nome do contato no cabeçalho do atendimento (`.ticket-title-name`)
- **Valores:** o nome INTEIRO. No celular o texto é cortado ("Dra. Karol..."); o mesmo valor vai no `title`

### `data-gamificacao-action`

- **Onde:** os botões da janela de Campanhas (`.custom-css-gamificacao-campanhas`) e os das regras por funil e por etiqueta, na janela de Pontuação e níveis (`.custom-css-gamificacao-config`)
- **Valores:** nas Campanhas: `salvar-campanha` (o Adicionar, que vira Salvar quando o formulário muda uma campanha que já existe) · `cancelar-edicao` · `editar-campanha` · `apagar-campanha` (abre a confirmação). Na Pontuação e níveis: `adicionar-funil` · `adicionar-etiqueta` (uma regra nova, já com o primeiro funil ou etiqueta que ainda não tem regra) · `remover-regra`

### `data-garcom-id`

- **Onde:** cada linha da comissão do garçom no Relatório do PDV (`.custom-css-relatorio-pdv-comissao-linha`)
- **Valores:** o id do garçom da linha; vazio na linha dos pedidos feitos pelo QR (sem garçom)

### `data-gerenciar-grupos`

- **Onde:** botão de gerenciar grupos de template, no cabeçalho de /waba-templates
- **Valores:** sem valor — marca o botão que abre o gerenciador

### `data-grafico`

- **Onde:** cada gráfico da página Avaliação pela IA (`.custom-css-page-avaliacao-ia`)
- **Valores:** `distribuicao` (as notas de 0 a 10) · `evolucao` (os dias do período)

### `data-gravando`

- **Onde:** campo de digitação
- **Valores:** `sim` enquanto grava áudio · `nao` fora disso

### `data-group`

- **Onde:** cartão do ticket e CABEÇALHO da conversa aberta
- **Valores:** `true` em conversa de grupo. No cabeçalho vale nos três lugares que usam a âncora `custom-css-ticket-header`: a conversa do frame da direita, o ticket em modal e o popup de espiar

### `data-group-filter`

- **Onde:** botão do filtro de grupos, na barra do quadro de atendimentos
- **Valores:** `todos` · `true` (só grupos) · `false` (sem grupos) — é o estado atual do filtro, e serve para destacar o botão quando ele está recortando a tela

### `data-group-option`

- **Onde:** cada opção dentro do filtro de grupos
- **Valores:** `todos` · `true` · `false`

### `data-grupo`

- **Onde:** linha de um grupo no gerenciador de grupos de template
- **Valores:** o id do grupo

### `data-grupo-id`

- **Onde:** cada linha do ranking entre as lojas (`.custom-css-crm-ranking-grupo`)
- **Valores:** o id da equipe, da unidade ou do funil da linha

### `data-grupos-do-template`

- **Onde:** seletor de grupos no cartão do template
- **Valores:** sem valor — marca o bloco que vincula o template aos grupos

### `data-grupos-nao-lidos`

- **Onde:** botão de trocar de visão
- **Valores:** quantos grupos têm mensagem não lida (ausente quando zero)

### `data-gupshup`

- **Onde:** os blocos da aba Geral da janela da conexão WhatsApp Gupshup (`.custom-css-modal-gupshup`)
- **Valores:** `instrucoes` (o quadro com o passo a passo, `.custom-css-gupshup-instrucoes`) · `url-do-webhook` (o quadro da URL para cadastrar na Gupshup, `.custom-css-gupshup-url`)

### `data-gupshup-acao`

- **Onde:** os botões da janela WhatsApp Gupshup
- **Valores:** `copiar-url` (copia a URL de recebimento) · `salvar` (Criar conexão ou Salvar)

### `data-gupshup-campo`

- **Onde:** os campos da janela WhatsApp Gupshup
- **Valores:** `nome` · `app` (nome da app na Gupshup) · `numero` (número de origem) · `chave` (API key) · `app-id` · `webhook` · `webhookb`

### `data-gupshup-passo`

- **Onde:** cada passo do quadro de instruções da janela WhatsApp Gupshup (`[data-gupshup="instrucoes"]`)
- **Valores:** o número do passo: `1` a `5`

### `data-gupshup-url`

- **Onde:** o conteúdo do quadro da URL na janela WhatsApp Gupshup (`[data-gupshup="url-do-webhook"]`)
- **Valores:** `depois-de-criar` (conexão ainda não criada: o aviso de que a URL aparece depois) · `pronta` (a URL, com o botão de copiar) · `sem-endereco` (a instalação ainda não tem o endereço de recebimento da Gupshup)

### `data-history-nav`

- **Onde:** paginação do histórico do limitador de envio
- **Valores:** `anterior` · `proximo`

### `data-hoje`

- **Onde:** cada dia do calendário de Agendamentos (`.custom-css-agenda-dia`)
- **Valores:** `true` no dia de hoje · `false`

### `data-icon`

- **Onde:** ícones do topo
- **Valores:** `theme` · `status` · `refresh` · `notifications` · `extension` · `dialer`

### `data-idioma`

- **Onde:** raiz da página de documentação da API e da página das classes
- **Valores:** o idioma da página: `pt` · `pt-PT` · `en` · `es` · `fr` · `de` — vem de `?lang=` na URL ou do idioma da plataforma. Na documentação da API, é o idioma em que a especificação foi pedida ao backend; na das classes, o do catálogo carregado

### `data-iframe-altura`

- **Onde:** moldura das páginas embutidas (Central de Ajuda, TypeBot, ChamaAi e os links do menu)
- **Valores:** a altura medida em pixels (`665px`, por exemplo) ou `padrao` no instante antes da primeira medição. Serve para conferir que a moldura ocupou a tela toda — se ficar em `padrao`, a medição não rodou

### `data-ilimitado`

- **Onde:** pílula de tokens da sugestão de IA (barra e cartão)
- **Valores:** `true` na empresa que usa credencial própria e não gasta tokens

### `data-import-state`

- **Onde:** barra de andamento da importação de contatos
- **Valores:** `enviando` (arquivo subindo, barra indeterminada) · `processando` (linhas sendo importadas)

### `data-in-call`

- **Onde:** botão do ramal na barra do topo (`[data-appbar="extension"]`)
- **Valores:** `true` com uma chamada atendida em curso — de entrada OU de saída · `false`

### `data-indicador`

- **Onde:** selo do card no Quadro de Atendimentos, dizendo o que já existe sobre aquele contato
- **Valores:** `oportunidade` · `agendamento` · `anotacao`. O selo só é desenhado quando o número é maior que zero, e a linha inteira some quando não há nenhum

### `data-indicador-total`

- **Onde:** o mesmo selo
- **Valores:** quantos — o número que aparece ao lado do ícone. Dá para destacar o card a partir de um patamar (por exemplo, três anotações ou mais)

### `data-item`

- **Onde:** cada linha do pedido na janela "Lançar na mesa" (tela Comandas)
- **Valores:** a chave do item: o produto, a variação e os adicionais escolhidos (o mesmo item, de novo, soma na mesma linha)

### `data-item-id`

- **Onde:** cada item de uma rodada (`.custom-css-salao-da-mesa-item`) e cada item tirado (`.custom-css-salao-da-mesa-tirado`) na janela da conta da mesa
- **Valores:** o id do item na rodada; no tirado, o id do registro do cancelamento

### `data-lane-type`

- **Onde:** raia do funil; e o cartão da tela de Oportunidades (`.custom-css-oportunidade-card`)
- **Valores:** `IN_PROGRESS` · `WON` · `LOST`. No cartão de Oportunidades, só com o CRM v2 — o v1 não traz a raia, e o cartão fica sem o atributo

### `data-linha`

- **Onde:** cada linha de um ranking da página Avaliação pela IA (`[data-ranking]`)
- **Valores:** o id do atendente ou do Setor

### `data-link`

- **Onde:** os links das telas de entrada: na de login (`.custom-css-login-link`) e na de recuperar a senha (`.custom-css-forgotpassword-link`)
- **Valores:** no login: `cadastro` · `recuperar-senha` · `termos` · `privacidade` (cada um só aparece quando a configuração o liga). No recuperar a senha: `login` (o voltar para o login)

### `data-lista`

- **Onde:** a tabela dos atendimentos avaliados da página Avaliação pela IA
- **Valores:** `avaliacoes`

### `data-lista-de-grupos`

- **Onde:** lista do gerenciador de grupos de template
- **Valores:** sem valor — marca a lista inteira

### `data-lugar`

- **Onde:** pódio de vendas
- **Valores:** `1` · `2` · `3`

### `data-mais-recente`

- **Onde:** cada versão da gaveta de Versões do editor de fluxo (`.custom-css-flow-versao`)
- **Valores:** `true` na primeira, a mais recente · `false` nas outras

### `data-marcados`

- **Onde:** a barra de seleção acima da lista da página E-mails (`.custom-css-emails-selecao`)
- **Valores:** quantos e-mails estão selecionados (`0` sem nenhum) — dá para destacar a barra só quando há seleção

### `data-media-type`

- **Onde:** balão da mensagem; a miniatura de cada arquivo em Arquivos da Conversa (`.custom-css-ticket-files-miniatura`); e a prévia de cada arquivo no Gerenciador de Arquivos (`.custom-css-bot-files-previa`, só `image` e `video`)
- **Valores:** `conversation` · `image` · `audio` · `video` · `document` · …

### `data-mencao`

- **Onde:** nome de quem foi marcado com @
- **Valores:** o identificador original (o número que aparecia antes)

### `data-mencao-contato`

- **Onde:** nome de quem foi marcado com @
- **Valores:** o id do contato. **Só existe quando o clique abre conversa privada** — some em grupo e no preview do ticket, então `[data-mencao-contato]` seleciona exatamente os clicáveis

### `data-mensagem`

- **Onde:** cada resultado da busca na conversa do chat interno (`.custom-css-chats-busca-resultados`)
- **Valores:** o id da mensagem que o resultado abre (o clique leva até ela na conversa)

### `data-menu`

- **Onde:** item do menu lateral
- **Valores:** o identificador do item

### `data-menu-action`

- **Onde:** cada item dos menus das páginas (`.custom-css-page-menu`) e dos menus da barra do topo
- **Valores:** no "Ações" de Conexões (`.custom-css-menu-conexoes-acoes`): `migrar` · `adicionar-whatsapp` · `adicionar-sem-aparelho` · `adicionar-webchat` · `adicionar-chat-externo` · `adicionar-oficial` · `adicionar-oficial-portal` · `adicionar-telegram` · `adicionar-facebook` · `adicionar-facebook-portal` · `adicionar-instagram` · `adicionar-instagram-portal` · `adicionar-tiktok` · `adicionar-rcs` · `adicionar-hub` · `fechar-removidas` · `fechar-todos` · `encerrar-com-filtros` · `reiniciar`. No ⋮ de cada fluxo (`.custom-css-menu-fluxo-acoes`): `editar-nome` · `editar-fluxo` · `exportar` · `duplicar` · `logs` · `excluir`. No Importar/Exportar de Contatos (`.custom-css-menu-contatos-importar-exportar`): `importar-agenda` · `importar-arquivo` · `exportar`. No ⋮ da linha de Contatos, no celular (`.custom-css-menu-contato-acoes`): `resumo` · `iniciar-conversa` · `editar` · `excluir`. No menu da mensagem do Chat Interno: `copiar` · `reagir` · `marcar-visto` / `desmarcar-visto` (o que o clique FAZ, conforme a mensagem já está marcada) · `apagar`. No "Recebe saltos de N" do editor de fluxo (`.custom-css-menu-saltos-do-fluxo`): `ir-para-origem`. No Ordenar da lista de atendimentos (`.custom-css-menu-ordenar-atendimentos`): `newest` (mais recentes primeiro) · `oldest` (mais antigos primeiro), com `role="menuitemradio"` e o escolhido em `aria-checked`. Na barra do topo: no menu da conta (`.custom-css-menu-usuario`), `perfil` · `trocar-senha` · `2fa` (só com o 2FA da empresa ligado) · `sair` · `versao`; no menu do status (`.custom-css-menu-status`), `online` · `away` · `offline`; no menu do idioma (`.custom-css-menu-idioma`), o código do idioma — `pt` · `pt-PT` · `es` · `en` · `de` · `fr`. Nos dois últimos, `role="menuitemradio"` e o atual em `aria-checked`. Os itens que só aparecem com o módulo no plano somem do DOM junto com o módulo No menu de status e sessão do cartão da tela de Usuários (`.custom-css-user-menu-presenca`): `online` · `away` · `offline` · `derrubar-sessao` (só para outra pessoa, com a confirmação `.custom-css-modal-confirmation-usuario-derrubar-sessao`). No "Ações" de Conexões, com o WhatsApp Gupshup no plano: `adicionar-gupshup`.

### `data-menu-group`

- **Onde:** grupo do menu lateral
- **Valores:** o identificador do grupo

### `data-menu-group-box`

- **Onde:** a caixa de cada submenu do menu lateral (`.custom-css-menu-grupo-caixa`): o divisor, o cabeçalho `[data-menu-group]` e a lista `.custom-css-menu-grupo-itens`
- **Valores:** o mesmo nome do `data-menu-group` do cabeçalho: `kanban` · `crm` · `pdv` · `consultorio` · `campaigns` — é o nome do submenu na `--menu-ordem`

### `data-menu-section`

- **Onde:** cada seção do menu lateral (`.custom-css-menu-secao`) e o título dela (`.custom-css-menu-secao-titulo`)
- **Valores:** `favoritos` · `principal` · `atendimentos` · `ferramentas` · `modulos-externos` · `ajuda` · `campanhas` · `administracao` · `automacao` · `sistema` — o mesmo nome no contêiner e no título; são esses os nomes de seção que a `--menu-ordem` usa

### `data-mesa-id`

- **Onde:** cada mesa (ou comanda) fechada da página Mesas e Comandas (`.custom-css-comandas-fechada`)
- **Valores:** o id da mesa ou da comanda no cadastro — tocar nela abre a conta

### `data-message-id`

- **Onde:** balão da mensagem — na conversa aberta e no olho (`.custom-css-modal-espiar-conversa`), onde faltava até a 29.467.0
- **Valores:** o id da mensagem

### `data-meta-batida`

- **Onde:** cartão da meta do mês, em Minha evolução
- **Valores:** `true` quando o vendido do mês alcançou a meta · `false` (também quando não há meta cadastrada)

### `data-meta-plataforma`

- **Onde:** cartão da conexão oficial nativa
- **Valores:** `cloud_api` · `coex`. Ausente quando a conexão não é oficial nativa ou quando ainda não se sabe — a pergunta não se aplica

### `data-metodo`

- **Onde:** opções de método de cadastro do número
- **Valores:** a chave do método

### `data-midia`

- **Onde:** prévia de mídia do template WABA
- **Valores:** `local` (a que está sendo trocada) · `atual` (a que o template já tem)

### `data-migracao-destino`

- **Onde:** campo de empresa de destino, no modal de migração
- **Valores:** sem valor — marca o campo que escolhe para onde migrar

### `data-migracao-empresa`

- **Onde:** linha da empresa no gerenciador
- **Valores:** o id da empresa a migrar

### `data-migracao-inventario`

- **Onde:** conteúdo do modal de migração
- **Valores:** o id da empresa

### `data-migracao-tabela`

- **Onde:** linha de tabela no inventário da migração
- **Valores:** o nome da tabela

### `data-migracao-teste`

- **Onde:** resultado do teste antes de migrar
- **Valores:** `ok` · `barrado`

### `data-minha`

- **Onde:** pílula de reação numa mensagem do chat interno
- **Valores:** `true` quando quem está olhando reagiu com aquele emoji · `false`

### `data-mode`

- **Onde:** campo de digitação (na caixa externa **e** em `.custom-css-composer-field`)
- **Valores:** `normal` · `signature` (assinar) · `internal` (nota interna — vence os outros modos, também no atendimento que está no chat externo, onde o globo começa ligado: a nota não vai para a página) · `external` (só canal externo)

### `data-modo`

- **Onde:** o botão que troca os comentários entre aba e lateral direita (`.custom-css-comentarios-modo`, na tarefa, na oportunidade e no projeto)
- **Valores:** a escolha da pessoa: `aba` (o padrão) · `lateral`. O botão some na tela estreita, onde é sempre aba

### `data-monitoravel`

- **Onde:** pílula de canal no monitor AMQP
- **Valores:** `true` no canal que passa por fila e portanto pode aparecer no monitor

### `data-mostra-encerrar`

- **Onde:** botão que liga e desliga o encerrar nos cards, na barra do quadro de atendimentos
- **Valores:** `true` · `false`

### `data-motivo`

- **Onde:** linha do histórico de remarketing; e cada linha do extrato de Minha Evolução (`.custom-css-minha-evolucao-movimento`)
- **Valores:** no remarketing, o motivo do registro. No extrato, o que rendeu o ponto: `venda` (venda fechada) · `valor` (valor vendido) · `meta` (meta do mês batida) · `funil` (venda no funil de uma regra) · `etiqueta` (venda com a etiqueta de uma regra) · `encerramento` (encerramento com venda) · `manual` — no estorno, o do lançamento que ele desfaz

### `data-muted`

- **Onde:** a janela da chamada e o widget minimizado
- **Valores:** `true` · `false` — o microfone mudo

### `data-names`

- **Onde:** o mesmo selo
- **Valores:** os nomes dos convidados, separados por vírgula e espaço (`Ana, Bruno`), como estão no cadastro — antes só existiam no balão do :hover. Dá para mostrá-los com `content: attr(data-names)`

### `data-nivel`

- **Onde:** linha do histórico de remarketing; o selo do modo da conta Meta no cartão da conexão (`.custom-css-connection-badge`); e o chip do tamanho do fluxo, no editor (`.custom-css-flow-tamanho`)
- **Valores:** no remarketing, o nível do registro. No selo: `erro` · `aviso` · `info` — a mesma regra que escolhe a cor dele. No chip do tamanho: `ok` (até 70% do limite) · `aviso` (acima de 70%) · `critico` (acima de 90%) — a mesma regra que escolhe a cor dele

### `data-node-id`

- **Onde:** o mesmo bloco do relatório do rodízio; e cada resultado da busca do editor de fluxo (`.custom-css-flow-busca-resultado`)
- **Valores:** o id do nó dentro do fluxo (vazio no grupo legado). Na busca, o id do bloco que o clique leva ao centro da tela

### `data-nota`

- **Onde:** a etiqueta da nota de um atendimento avaliado pela IA
- **Valores:** a nota, de `0` a `10`

### `data-nota-id`

- **Onde:** bloco de nota interna do atendimento
- **Valores:** o id da nota

### `data-notification-action`

- **Onde:** faixa de permissão de notificação
- **Valores:** `enable` · `dismiss`

### `data-novo-grupo`

- **Onde:** campo de nome no gerenciador de grupos de template
- **Valores:** sem valor — marca o campo de criar grupo

### `data-on-hold`

- **Onde:** a janela da chamada e o widget minimizado
- **Valores:** `true` · `false` — a chamada em espera

### `data-operador`

- **Onde:** foto do operador
- **Valores:** o nome dele

### `data-operator-id`

- **Onde:** cards de atendimento: o do Quadro (`.custom-css-quadro-card`), o cartão da lista (`.custom-css-ticket-item`, também o de grupo) e os dos quatro Kanban (`.custom-css-kanban-card`, `-kanban-team-card`, `-kanban-filas-card` e `-kanban-grupos-card`); e o nome do atendente no cabeçalho (`.ticket-operator`), a linha do ranking e a linha de operador no relatório do rodízio
- **Valores:** o id do operador, o mesmo em todas as telas. Nos cards só existe quando o atendimento tem operador: `:not([data-operator-id])` é o card sem operador. Como o atributo está em vários lugares, mire junto com a classe: `.custom-css-quadro-card[data-operator-id="3"]`

### `data-operator-name`

- **Onde:** os mesmos cards do `data-operator-id` (Quadro, lista e os quatro Kanban)
- **Valores:** o nome do operador como está no cadastro: a pílula mostra em caixa alta, o atributo não. Muda quando alguém corrige o nome; para uma regra que dure, use o `data-operator-id`

### `data-ordem`

- **Onde:** botão de ordenação no cabeçalho de cada coluna do Quadro de Atendimentos
- **Valores:** `recentes` (os mais novos em cima, o padrão) · `antigos`. Cada coluna tem a sua, e a escolha fica guardada no navegador

### `data-origem`

- **Onde:** cartão do template WABA
- **Valores:** quem criou (`bm`, `wsw`, `desconhecida`)

### `data-origin`

- **Onde:** balão da mensagem
- **Valores:** `contact` · `user` (operador) · `app` (celular pareado) · `api` (bot/API)

### `data-outro-mes`

- **Onde:** o mesmo dia
- **Valores:** `true` nos dias do mês anterior ou do seguinte, que completam as semanas da grade · `false`

### `data-paginas`

- **Onde:** cartão de PDF do chat interno (`.custom-css-chat-pdf`)
- **Valores:** quantas páginas o PDF tem — só quando `data-estado` é `pronto`

### `data-pasta`

- **Onde:** caixa de seleção de pasta no modal de conta de e-mail; e a pasta de figurinhas (chip do seletor no compositor e item da lista na tela de Figurinhas)
- **Valores:** no e-mail: o caminho IMAP da pasta (ex.: `INBOX`, `INBOX.Comercial`). Nas figurinhas: o id da pasta

### `data-pede-valor`

- **Onde:** cartão de cada tag na Tela 1 do encerramento em 3 passos
- **Valores:** `obrigatorio` (a tag pede valor e não aceita R$ 0,00) · `opcional` (pede, mas aceita em branco) · `nao` (a Tela 2 é pulada)

### `data-pedido-id`

- **Onde:** cada rodada na janela da conta da mesa (`.custom-css-salao-da-mesa-rodada`)
- **Valores:** o id do pedido da rodada — o mesmo do `pedido.id` do webhook

### `data-percentual-da-meta`

- **Onde:** cartão da meta do mês, em Minha evolução
- **Valores:** o percentual do vendido sobre a meta, com uma casa (`41.7`, `150`) · vazio quando não há meta cadastrada

### `data-perfil-erro`

- **Onde:** alerta do modal de perfil do número
- **Valores:** sem valor — marca o aviso de falha ao carregar ou salvar o perfil

### `data-periodo`

- **Onde:** o seletor de período das telas de desempenho (`.custom-css-seletor-periodo`): Minha Evolução, Ranking de Vendas e Ranking do CRM
- **Valores:** `mes` (o mês, nos campos de mês de cada tela) · `personalizado` (de um dia a outro, nos campos `.custom-css-seletor-periodo-de` e `.custom-css-seletor-periodo-ate`) · `campanha` (uma campanha da gamificação, escolhida na lista)

### `data-permissao`

- **Onde:** botões que dependem de permissão (painel do contato e barra de ações)
- **Valores:** o estado da permissão daquele botão

### `data-ping-ms`

- **Onde:** o medidor de latência da barra do topo (`[data-appbar="ping"]`)
- **Valores:** a latência medida, em milissegundos. Ausente enquanto não há medida

### `data-ping-status`

- **Onde:** o mesmo medidor
- **Valores:** `bom` (abaixo de 300ms) · `medio` (até 500ms) · `ruim` · `desconhecido` (sem medida ainda) — a mesma régua da cor da bolinha

### `data-pisca`

- **Onde:** brilho sobre o card do quadro que acabou de receber mensagem
- **Valores:** `mensagem-nova` (o único valor). O elemento só existe enquanto pisca

### `data-pixel-formato`

- **Onde:** a seção do Pixel na janela da tag (`.custom-css-tag-pixel`), a janela do bloco Pixel do fluxo (`.custom-css-flow-pixel`) e o bloco Pixel no desenho do fluxo (`.custom-css-flow-node-pixel`)
- **Valores:** `website` (o Pixel de sempre; no desenho do fluxo, uma saída) · `mensagens` (o Pixel no formato de mensagens do WhatsApp; no desenho do fluxo, duas saídas: Elegível e Não elegível). Muda na hora em que se troca o campo "Formato do evento"

### `data-pixel-logs-day`

- **Onde:** campo de dia na tela de logs do Pixel
- **Valores:** `true` — marca o campo

### `data-pixel-status`

- **Onde:** a situação de cada evento do formato de mensagens na tela de logs do Pixel (`.custom-css-pixel-logs-status`)
- **Valores:** `pendente` (na fila) · `enviando` · `enviado` (a Meta recebeu) · `ignorado` (não pôde sair — o porquê está em `.custom-css-pixel-logs-motivo`) · `falhou` (a Meta recusou ou não respondeu). Os eventos do formato site não levam o atributo

### `data-plataforma`

- **Onde:** opções de plataforma no cadastro por app próprio
- **Valores:** o id da plataforma

### `data-pode-espiar`

- **Onde:** card do quadro de atendimentos
- **Valores:** `true` quando quem olha pode abrir a conversa com duplo clique · `false` quando "Operador Visualiza Prévias?" está desligada para ele

### `data-posicao`

- **Onde:** cada etiqueta na faixa do cartão do ticket (`.ticket-tags .custom-css-contact-tag`), na lista e nos grupos
- **Valores:** a posição da etiqueta na faixa, de `1` em diante, na ordem da tela. Nas etiquetas de outros lugares, o atributo não sai

### `data-preenchido`

- **Onde:** todo seletor (o campo de escolher): na raiz (`.custom-css-select`), no rótulo (`.custom-css-select-label`) e na caixa do campo (`.custom-css-select-input`)
- **Valores:** `true` com um valor escolhido (também o que chega depois de a janela abrir) · `false` sem valor (vazio, `""` ou nenhum item no de vários) — o mesmo estado que faz o rótulo subir

### `data-prefixo`

- **Onde:** linha de conexão na lista de prefixos do discador SIP
- **Valores:** o prefixo de discagem daquela conexão

### `data-prefixos`

- **Onde:** botão que abre e recolhe a lista de prefixos do discador SIP
- **Valores:** `aberto` · `recolhido`

### `data-presence-state`

- **Onde:** selo de presença no cabeçalho do atendimento
- **Valores:** `online` · `away` · `offline`, ou vazio quando a conexão não informa

### `data-prioridade`

- **Onde:** cartão de tarefa (`.custom-css-task-card`)
- **Valores:** `high` · `medium` · `low`

### `data-problema`

- **Onde:** cada bloco listado no Verificar do editor de fluxo (`.custom-css-flow-verificar-item`)
- **Valores:** `isolado` (não se chega a ele a partir do Início) · `sem-entrada` · `sem-saida` (o fluxo para nele) · `salto-quebrado` (um "Pular para" sem destino) · `ciclo-sem-espera` (aqui o item é o ciclo inteiro)

### `data-product-id`

- **Onde:** cartão da tela de Produtos (`.custom-css-product-card`)
- **Valores:** o id do produto

### `data-produto`

- **Onde:** cada produto achado pela busca da janela "Lançar na mesa" (tela Comandas)
- **Valores:** o id do produto no cadastro — tocar nele põe o produto no pedido do garçom

### `data-produtos`

- **Onde:** linha de produtos da oportunidade
- **Valores:** quantos itens são

### `data-protocolo`

- **Onde:** o cartão do #protocolo citado numa mensagem do chat interno (`.custom-css-chats-protocolo`)
- **Valores:** o número do protocolo, sem o `#`

### `data-quadro`

- **Onde:** aviso da página do Quadro de Atendimentos
- **Valores:** `fora-do-plano` — a empresa não tem o módulo `useQuadro` contratado. É o único valor emitido hoje; serve para esconder o aviso ou trocá-lo por um texto próprio

### `data-queue-chatbot`

- **Onde:** cartão do ticket, cartão de grupo, cabeçalho da conversa aberta e os cards do quadro de atendimentos e dos kanbans (`/kanban`, equipe, filas e grupos); o cartão da tela de Setores (`.custom-css-queue-card`); e as opções de setor do "Filtrar por Setores" da lista de atendimentos e das listas de escolher setor (transferir e novo atendimento)
- **Valores:** `true` · `false`. **Ausente quando o payload traz a fila sem dizer se ela é de chatbot** — é "não sei", e não "false"; quem customiza cai no critério seguinte dele

### `data-queue-color`

- **Onde:** cartão do ticket, cabeçalho da conversa aberta, o cartão da tela de Setores (`.custom-css-queue-card`) e o card do Quadro (`.custom-css-quadro-card`), também na pílula da fila (`.custom-css-quadro-fila`); o chip de cada setor no campo Setores das janelas (`.custom-css-queue-select-chip` — no Editar Usuário, nas conexões…) e no cartão de Usuários (`.custom-css-users-card-setor`)
- **Valores:** a cor da fila

### `data-queue-id`

- **Onde:** cartão do ticket, cartão de grupo, cabeçalho da conversa aberta, os cards do quadro de atendimentos e dos kanbans, e o cartão da tela de Setores; o chip de cada setor no campo Setores das janelas (`.custom-css-queue-select-chip` — no Editar Usuário, nas conexões…) e no cartão de Usuários (`.custom-css-users-card-setor`); e as opções de setor do "Filtrar por Setores" da lista de atendimentos e das listas de escolher setor (transferir e novo atendimento)
- **Valores:** o id da fila, ou vazio quando o atendimento não tem fila

### `data-queue-name`

- **Onde:** cartão do ticket e cabeçalho da conversa aberta
- **Valores:** o nome do setor. No cartão o nome só existe como texto do badge (`.ticket-queue`), que muda com o idioma

### `data-quick-message`

- **Onde:** a mesma opção
- **Valores:** a mensagem INTEIRA da resposta — na lista ela vem cortada em 35 caracteres (`.custom-css-quick-reply-mensagem`)

### `data-quick-message-id`

- **Onde:** cada opção da lista de respostas rápidas do campo de mensagem (`.custom-css-quick-reply`, dentro do `li` da opção; a lista é `.custom-css-quick-replies`)
- **Valores:** o id da resposta rápida

### `data-quickmessage-id`

- **Onde:** cartão da tela de Respostas Rápidas (`.custom-css-quickmessage-card`)
- **Valores:** o id da mensagem rápida

### `data-quoted`

- **Onde:** balão da mensagem
- **Valores:** `true` quando é resposta a outra

### `data-ramal`

- **Onde:** linha do ramal no card do operador, na tela de Usuários
- **Valores:** o número do ramal. Sai do campo `webphoneRamal` do cadastro e, quando ele está vazio, do trecho do `sipuri` antes do `@`. O card só desenha a linha quando existe um dos dois

### `data-ranking`

- **Onde:** cada tabela de ranking da página Avaliação pela IA
- **Valores:** `atendente` · `setor`

### `data-rascunho`

- **Onde:** campo de digitação
- **Valores:** `true` quando há texto não enviado — dá para avisar quem sai da conversa com resposta pela metade

### `data-recibo`

- **Onde:** os tiques do balão de quem mandou, no chat interno (`.custom-css-chats-msg-recibo`)
- **Valores:** `enviada` (✓: alguém ainda não recebeu) · `entregue` (✓✓: chegou ao painel de todos) · `lida` (✓✓ colorido: todos abriram a conversa)

### `data-recibo-de`

- **Onde:** cada pessoa na janela das horas de entrega e leitura (`.custom-css-modal-recibos-chat-interno`)
- **Valores:** o id da pessoa

### `data-reconnect-path`

- **Onde:** escolha de caminho de reconexão, na página de Conexões
- **Valores:** `own` (app próprio) · `aini`

### `data-reconnect-path-dialog`

- **Onde:** diálogo que pergunta o caminho de reconexão
- **Valores:** `true`

### `data-referencia`

- **Onde:** linha da tabela de logs de erro
- **Valores:** a referência daquele log — dá pra destacar por CSS os erros de uma origem só

### `data-regra`

- **Onde:** ícone de regra no cabeçalho da coluna automática do quadro de atendimentos; e cada regra da janela de Pontuação e níveis (`.custom-css-gamificacao-regra`)
- **Valores:** no quadro, `fila` — a coluna recebe sozinha os pendentes das filas da regra (é o único valor ali). As regras do quadro, as que cada um cria na tela de regras, usam `data-regra-id`. Na Pontuação e níveis, o que rende o ponto: `venda` · `valor` · `meta` · `encerramento` (cada encerramento com venda) · `funil` (cada venda no funil escolhido, uma linha por funil) · `etiqueta` (cada venda com a etiqueta escolhida, uma linha por etiqueta)

### `data-regra-ativa`

- **Onde:** cada linha da tela de regras do quadro (`.custom-css-regras-quadro-regra`)
- **Valores:** `true` · `false` — a regra desligada continua na lista, esmaecida, e não roda

### `data-regra-id`

- **Onde:** ícone de regra no card do quadro de atendimentos (`.custom-css-quadro-card-regra`) e cada linha da tela de regras do quadro (`.custom-css-regras-quadro-regra`)
- **Valores:** o id da regra do quadro. No card, é a regra que pôs o atendimento na coluna em que ele está — o ícone some quando alguém arrasta o card para outra coluna

### `data-regra-travada`

- **Onde:** a mesma linha
- **Valores:** `true` na regra da equipe vista em Minhas regras (com cadeado e sem botões) · `false` nas que quem olha pode mudar

### `data-remarketing`

- **Onde:** controles da tela de logs de remarketing
- **Valores:** `auto-atualizar` · `retencao`

### `data-reserva-id`

- **Onde:** cada reserva da aba Reservas das Comandas (`.custom-css-reservas-da-mesa-reserva`)
- **Valores:** o id da reserva — o mesmo do `reserva.id` do webhook e da API

### `data-resposta-na-volta`

- **Onde:** modal que oferece deixar pronta a retomada, ao enviar um template
- **Valores:** `pergunta` · `texto` · `prazo` · `nao`

### `data-resposta-na-volta-aviso`

- **Onde:** faixa sobre o campo, dizendo que há uma retomada guardada
- **Valores:** `true` na faixa · `cancelar` no botão que a descarta

### `data-restantes`

- **Onde:** botão “ver mais” de uma raia do quadro do CRM
- **Valores:** quantos cartões ainda não foram carregados

### `data-resumo`

- **Onde:** os blocos do topo da Pesquisar (`.custom-css-atendimentos-resumo`)
- **Valores:** `total` · `tempos` · `baixar` (o de baixar os resultados, só do admin, não é cartão de número)

### `data-salvo`

- **Onde:** o status de salvo do editor de fluxo, acima do desenho (`.custom-css-flow-status`)
- **Valores:** `true` (fluxo salvo) · `false` (há alterações não salvas)

### `data-secao`

- **Onde:** cada seção da página das classes (`.custom-css-documentacao-css-secao`) e o link dela no sumário (`.custom-css-documentacao-css-sumario-item`); cada seção das janelas de Tag, de Categoria (de setores e de fluxos) e de Webhook (`.custom-css-dialog-secao`); e cada seção do corpo do Criar Template (`.custom-css-waba-template-form-secao`)
- **Valores:** o nome da seção: `como-usar` · `convencoes` · `propriedades` · `tema-escuro` · `eventos` · `atributos` · `paginas` · `modais` · `especificas` · `sem-prefixo` · `chat-externo` · `historico` · `nao-achou` — o mesmo que, depois do `#` no endereço, abre a página já na seção. Nas janelas: na de Tag, `informacoes-basicas` · `configuracoes-avancadas` · `pixel` · `automacao`; na de Categoria, `informacoes` · `cor`; na de Webhook, `informacoes-basicas` · `status`. No Criar Template: `cabecalho` · `corpo` · `rodape` · `botoes`

### `data-selecionada`

- **Onde:** cartão de cada tag na Tela 1 do encerramento em 3 passos (`.custom-css-encerramento-tag`)
- **Valores:** `true` na tag escolhida · `false` nas outras

### `data-selecionando`

- **Onde:** campo de digitação
- **Valores:** `true` enquanto o modo de selecionar mensagens está ligado

### `data-selected`

- **Onde:** cartão do ticket; e o cartão de categoria do Criar Template (WABA)
- **Valores:** no ticket: `true` no ticket aberto. No cartão de categoria: `true` no escolhido · `false` nos outros. Ali não vai `aria-checked`: o cartão já tem um rádio de verdade dentro, e o leitor de tela anunciaria duas escolhas

### `data-send-limit-action`

- **Onde:** botões do modal do limitador
- **Valores:** `history`

### `data-send-limit-counter`

- **Onde:** contador de envios no cartão da conexão
- **Valores:** o id da conexão

### `data-send-limit-field`

- **Onde:** campos do modal do limitador de envio
- **Valores:** `enabled` · `amount` · `cutoffDay`

### `data-send-limit-history`

- **Onde:** bloco do histórico de limites
- **Valores:** `true`

### `data-send-limit-summary`

- **Onde:** resumo do limite, no mesmo modal
- **Valores:** `true`

### `data-settings-secao`

- **Onde:** cada seção de Configurações (`.custom-css-settings-secao`) e a faixa dela (`.custom-css-section-header`)
- **Valores:** `avaliacoes` · `expediente` · `grupos` · `chamadas` · `bot` · `permissoes` · `sistema` · `sons-notificacoes` · `transferencias` · `carteiras` · `logs` · `contatos-campos` · `armazenamento` · `aniversario` · `webhooks` · `2fa`; e, só para o super: `senha` · `global` · `smtp` · `pix-efi` · `mercado-pago` · `stripe` · `asaas` · `paypal` · `patibill` · `pwa` · `baileys` · `ajuda` · `nome-app` · `layout-v2` · `apps-externos` · `waba` · `google-analytics` · `infra` · `desempenho`

### `data-settings-tab`

- **Onde:** cartão do menu da tela de Configurações
- **Valores:** o nome da aba (`options`, `schedules`, `tokenempresa`, `companies`…). O cartão também carrega `id="simple-tab-<nome>"`, `role="tab"`, `aria-selected` e `aria-controls="simple-tabpanel-<nome>"` — o painel já se apresentava com esse id e apontava para uma aba que não existia

### `data-sincroniza-agenda`

- **Onde:** opção de sincronizar com o Google Agenda (atividade do CRM e tarefa)
- **Valores:** `true` · `false`

### `data-sip`

- **Onde:** os botões da chamada: na janela do receptor (`.custom-css-modal-sip-receiver`), na do discador (`.custom-css-modal-sip-dialer`) e no widget minimizado (`.custom-css-sip-widget`)
- **Valores:** `answer` · `answer-video` · `call` · `call-video` · `hangup` (também o Cancelar enquanto chama) · `mute` · `hold` · `video` (a câmera) · `keypad` · `transfer` · `transfer-blind` · `transfer-attended` · `transfer-cancel` · `minimize` · `maximize` · `close` (o X da janela — no receptor ele também encerra a chamada) · `abrir-teclado` (no widget: volta para a janela JÁ com o teclado aberto)

### `data-sip-call`

- **Onde:** o `<body>`
- **Valores:** a chamada: `idle` · `ringing` (chegando) · `calling` (saindo, ainda sem resposta) · `active`. Com duas ao mesmo tempo, vale a mais viva (atendida > tocando > chamando)

### `data-sip-registration`

- **Onde:** o `<body>`
- **Valores:** o registro do ramal: `registered` · `connecting` · `unregistered` · `failed`. O mesmo valor sai no evento `sip:state` (ver Eventos)

### `data-situacao`

- **Onde:** cada campanha da janela de Campanhas (`.custom-css-gamificacao-campanha`); cada oportunidade (`.custom-css-contato-oportunidade`) e cada linha da tabela de Oportunidades (`.custom-css-oportunidades-linha`) e cada projeto (`.custom-css-contato-projeto`) nos cartões do painel do contato
- **Valores:** na campanha: `agendada` (ainda não começou) · `andamento` (hoje está dentro dela) · `encerrada`; na oportunidade: `aberta` · `ganha` · `perdida`; no projeto: `planejamento` · `andamento` · `pausado` · `concluido`

### `data-so-os-meus`

- **Onde:** botão "só os meus" na barra do quadro de atendimentos
- **Valores:** `true` · `false` — se o filtro por mim mesmo está ligado

### `data-so-sem-resposta`

- **Onde:** botão "sem resposta" na barra do quadro de atendimentos
- **Valores:** `true` · `false` — se o filtro de sem resposta está ligado

### `data-stat`

- **Onde:** cartão de número (`.custom-css-stat-card`)
- **Valores:** qual número o cartão mostra — em Contatos: `hoje` · `semana` · `mes` · `total`; Tarefas: `total` · `concluidas` · `pendentes` · `prioridade-alta` · `prioridade-media` · `prioridade-baixa`; Pesquisar: `total` · `tempos`; Monitor AMQP: `total` · `processadas` · `com-erro` · `pendentes`; os quatro Kanban e o Dashboard: `total` · `abertos` · `pendentes` · `fechados` (o Dashboard, sem o total); Pipeline: `em-andamento` · `vendas-ganhas` · `vendas-perdidas` · `valor-ganho` · `valor-perdido` · `taxa-de-conversao` · `ticket-medio`; Dashboard legado: `em-atendimento` · `aguardando` · `atendentes-ativos` · `finalizados` · `novos-contatos` · `recebidas` · `enviadas` · `tempo-medio-atendimento` · `tempo-medio-espera` · `empresas` · `conexoes` · `vencimento`; Logs de Auditoria: `total` · `acoes-bloqueadas` · `usuarios`; Relatório de Avaliações: `total` · `nota-media` · `opcao-mais-comum` · `periodo`; Ranking de Vendas: `vendas-do-time` · `meta` · `melhor-vendedor` · `ticket-medio`; Relatório de Vendas: `vendas` · `valor` · `ticket-medio`; Leads de anúncio: `leads` · `conversoes` · `taxa` · `receita`; Distribuição do rodízio: `atendimentos` · `transbordos` · `operadores` · `nos`; Ranking do CRM: `vendas` · `conversao` ou `meta` · `melhor-vendedor` · `ticket-medio`; Relatório da Campanha: `total` · `enviados` · `nao-enviados` · `repetidos` · `offline` · `com-retry`; Relatório de Ligações: `total` · `realizadas` · `recebidas` · `taxa-de-atendimento` · `nao-atendidas` · `tempo-medio`; Relatório da Empresa: `id` · `cadastro` · `vencimento` · `gestor-de-chaves` · `ultima-mensagem` · `mensagens` · `mensagens-no-mes` · `audios` · `videos` · `imagens` · `arquivos` · `usuarios` · `setores` · `mensagens-de-grupo` · `percentual-de-grupo` · `campanhas` · `agendamentos`; Grupos: `total` · `sou-admin` · `membros` · `bloqueados`; Consumo de Voz: `saldo` · `franquia` · `consumido` · `custo`; Minha Evolução: `pontos` · `pontos-no-mes` (no período que não é o mês, o mesmo cartão traz os pontos do período) · `meta` (no mês) ou `vendido` (no período personalizado e na campanha, em `.custom-css-minha-evolucao-vendido-periodo`); Estatísticas das Tags: `tag-mais-usada` · `aplicacoes` · `tags-usadas`; Estatísticas dos Contatos: `protocolos` · `contatos-ativos` · `novos-contatos` · `horario-de-pico`

### `data-status`

- **Onde:** balão, cartão do ticket e CABEÇALHO da conversa aberta; e, com valores próprios, o cartão de tarefa, o agendamento, o chip de status de Contatos, os cartões de status do Dashboard, o botão do ramal, o seletor de status da tela de login e o botão do status na barra do topo
- **Valores:** no balão: `pending` (ack 0) · `sent` (1 e 2) · `delivered` (3, entregue) · `read` (4 e 5, lida ou ouvida) · `unknown` (sem ack). No cartão e no cabeçalho: o status do atendimento. **Mesmo nome nos dois**, de propósito — a regra escrita para o cartão vale no cabeçalho sem `if`. No cartão de tarefa: `pending` · `completed`. No agendamento (`.custom-css-agenda-evento`): `pendente` · `agendada` · `enviada` · `erro`. No chip de Contatos (`.custom-css-contact-status`): `active` · `inactive`. Nos três cartões de status do Dashboard: `open` · `pending` · `closed`. No botão do ramal (`[data-appbar="extension"]`): `connecting` · `connected` · `failed` (o registro falhou) · `disconnected`. No seletor de status da tela de login (`.custom-css-login-status`) e em cada opção dele (`.custom-css-login-status-opcao`): `online` · `away` (Ausente) · `offline` — no seletor, o status escolhido; na opção, o dela. No botão do status na barra do topo (`[data-appbar="status"]`): `online` · `away` · `offline` — o de quem está logado No botão de status e sessão do cartão da tela de Usuários (`.custom-css-user-btn-presenca`): `online` · `away` · `offline`.

### `data-tag-color`

- **Onde:** etiqueta; o cartão da tela de Tags (`.custom-css-tag-card`); e a etiqueta do card do Kanban e do Kanban da equipe (`.custom-css-kanban-card-tag`)
- **Valores:** a cor dela

### `data-tag-id`

- **Onde:** etiqueta; o cartão da tela de Tags; e a etiqueta do card do Kanban e do Kanban da equipe
- **Valores:** o id dela

### `data-tarefa`

- **Onde:** linha de tarefa no resumo do contato, dentro do atendimento
- **Valores:** o id da tarefa — a linha inteira abre a tarefa

### `data-tem-contato`

- **Onde:** bloco de identificação de quem liga, na janela de chamada recebida do webphone
- **Valores:** `true` quando o número casou com um contato (a linha do nome existe) · `false`

### `data-tem-sugestao`

- **Onde:** barra da sugestão de IA
- **Valores:** `true` quando já existe sugestão gerada — junto do `data-carregando`, cobre os três estados da barra

### `data-template-groups`

- **Onde:** seletor de grupos de template no modal da fila
- **Valores:** sem valor — marca o campo que define quais grupos a fila usa

### `data-template-id`

- **Onde:** cartão do template na tela de Templates WABA (`.custom-css-waba-template-card`)
- **Valores:** o id do template na plataforma

### `data-template-status`

- **Onde:** cartão do template na tela de Templates WABA (`.custom-css-waba-template-card`)
- **Valores:** o estado do template na Meta, o valor cru: `APPROVED` · `PENDING` · `REJECTED` · `SUBMITTED` (e outro que a Meta mandar, como veio) — o chip `.custom-css-waba-template-status` mostra o mesmo em texto

### `data-testid`

- **Onde:** prévias de mídia do template WABA
- **Valores:** `previa-video` · `previa-documento`

### `data-theme`

- **Onde:** `<body>`
- **Valores:** `dark` · `light`

### `data-ticket-created`

- **Onde:** cartão do ticket e cabeçalho da conversa aberta
- **Valores:** quando o atendimento foi aberto, em ISO 8601. Existe para o cálculo de tempo ser aritmética de data: o único horário publicado antes era o TEXTO do `.ticket-datetime`, que sai como `20:50`, `ontem` ou `12/08` conforme a idade da mensagem

### `data-ticket-id`

- **Onde:** cartão do ticket, cabeçalho e ficha do contato; e a linha (e o cartão, no celular) da Pesquisar
- **Valores:** o id. Na Pesquisar é o id do ATENDIMENTO, e não o número da linha (o protocolo)

### `data-ticket-name`

- **Onde:** cartão do ticket
- **Valores:** o nome do contato

### `data-ticket-pending-since`

- **Onde:** cartão do ticket
- **Valores:** desde quando o atendimento aguarda na fila (a ordem de chegada do Aguardando), em ISO 8601 — não muda com mensagem nova nem com troca de setor; ausente fora do Aguardando

### `data-ticket-protocol`

- **Onde:** cartão do ticket
- **Valores:** o protocolo

### `data-ticket-status`

- **Onde:** cartão do quadro de atendimentos; e o cartão e o chip de status (`.custom-css-kanban-card-status`) dos quatro Kanban
- **Valores:** o status do atendimento naquele card: `pending` · `open` (no quadro); nos Kanban também `closed`

### `data-ticket-updated`

- **Onde:** cartão do ticket e cabeçalho da conversa aberta
- **Valores:** última alteração do atendimento, em ISO 8601. ⚠️ **Não é o horário da última mensagem**: `updatedAt` também anda quando o atendimento muda de fila, é transferido, atribuído ou resolvido. Para "há quanto tempo sem resposta" ele erra numa transferência — não existe hoje coluna do horário da última mensagem

### `data-ticket-uuid`

- **Onde:** cartão do ticket e cabeçalho da conversa aberta
- **Valores:** o uuid. É o que a rota `/tickets/<uuid>` usa, então é com ele que se monta link direto para um atendimento a partir de outra tela

### `data-tipo`

- **Onde:** atividade do CRM (painel e cartão); o item de cada bloco no desenho do fluxo (`.custom-css-flow-node-item`) e o da janela do Conteúdo (`.custom-css-flow-conteudo-item`); e as fileiras de ações do cartão da conexão (`.custom-css-connection-acoes`); os cartões de tipo do Adicionar das Respostas Rápidas (`.custom-css-quick-message-tipo`); e as caixas de explicação da aba de rastreio dos Links Curtos (`.custom-css-short-link-info`); e cada botão da mensagem interativa no atendimento (`.custom-css-msg-botao`)
- **Valores:** na atividade do CRM: `lembrete` · `reuniao` · `ligacao` · `email` · `visita` · `tarefa`. No item do bloco: `texto` · `imagem` · `audio` · `video` · `documento` · `intervalo` (os itens do Conteúdo, os mesmos na janela dele) · `opcao` e `senao` (cada opção do Menu e a "Resposta inválida" dele) · `botao` (Botões Interativos e Webview) · `saida` (cada saída: Randomizador, Condição, Switch, Horário Escolhido, Asaas, IXC, HTTP Request, É Seguidor? e Pixel) · `operador` (Rodízio) · `variavel` (Template). Na fileira de ações da conexão: `texto` (os botões com texto) · `icone` (os de ícone: editar, excluir…). No cartão de tipo das Respostas Rápidas: `texto` · `arquivo` — o escolhido em `aria-pressed`. Na caixa dos Links Curtos: `pixel` · `google`. No botão da mensagem interativa: `url` · `telefone` · `resposta` · `copiar` · `lista` (o que abre a lista)

### `data-total`

- **Onde:** o mesmo dia; e o contador de cada aba da lista de atendimentos (`.custom-css-ticket-tabs-contador`, o `.MuiBadge-root` da aba); e a faixa das etiquetas do cartão do ticket (`.ticket-tags`)
- **Valores:** no dia, quantos agendamentos ele tem (já com a busca aplicada). Na aba, o total de atendimentos que o servidor informou — `0` até a primeira resposta; enquanto é `0`, o contador mostra só os carregados (`data-carregados`). Na faixa, quantas etiquetas o contato tem — cada uma com a posição em `data-posicao`

### `data-total-chatbot`

- **Onde:** a aba AGUARDANDO da lista de atendimentos (o `.custom-css-ticket-tabs-contador` da aba), ao lado do `data-total`
- **Valores:** quantos atendimentos aguardando estão em setores marcados como "Agente de IA / Chatbot", com os mesmos filtros da aba — o servidor conta todos, e não só os já carregados. Ausente até a primeira resposta. A lista também pode vir só com esses setores: `queueChatbot=true` na busca da lista (`GET /tickets`); `queueChatbot=false` tira esses setores

### `data-total-servidor`

- **Onde:** subtítulo da raia do Kanban
- **Valores:** quantos cartões existem NO SERVIDOR naquela etapa — pode ser maior que os carregados na tela

### `data-transbordos`

- **Onde:** linha de transbordo do bloco, no relatório do rodízio
- **Valores:** quantos atendimentos o nó não conseguiu entregar no período — dá para destacar o bloco a partir de um patamar

### `data-ultimo-login`

- **Onde:** linha do último login no card do operador, na tela de Usuários
- **Valores:** a data e hora no formato `dd/MM/yyyy HH:mm`, ou `nunca` para quem nunca entrou — dá para destacar quem está sumido

### `data-unread`

- **Onde:** cartão do ticket; e cada conversa da lista do chat interno
- **Valores:** `true` · `false` — SE há mensagem não lida. (A descrição anterior aqui dizia "quantas", e estava errada: sempre foi booleano.)

### `data-unread-count`

- **Onde:** cartão do ticket; cada conversa da lista do chat interno; e o botão `mark-as-read` do cabeçalho do atendimento
- **Valores:** QUANTAS mensagens não lidas, como número. O valor já era desenhado no badge, mas só como texto dentro do MUI

### `data-user-color`

- **Onde:** cartão do ticket; e a pílula do operador no card do Quadro (`.custom-css-quadro-operador`)
- **Valores:** a cor do operador

### `data-user-field`

- **Onde:** campos do modal de usuário
- **Valores:** o nome do campo (`webphoneTipo`, `webphoneAcaoDoBotao`…)

### `data-user-id`

- **Onde:** cada convidado na linha do operador, no cabeçalho do atendimento (`.ticket-collaborator`); e o cartão da pessoa na tela de Usuários (`.custom-css-users-card`)
- **Valores:** o id do usuário convidado — o papel do `data-operator-id` do operador. No cartão de Usuários, o id da pessoa

### `data-user-profile`

- **Onde:** cartão da pessoa na tela de Usuários (`.custom-css-users-card`), nas duas visões
- **Valores:** o perfil: `admin` · `supervisor` · `user` — o mesmo do chip `.custom-css-users-card-perfil`

### `data-user-section`

- **Onde:** blocos do modal de usuário
- **Valores:** `webphone-widget` · `webphone-nativo`

### `data-user-status`

- **Onde:** o chip de presença no cartão da pessoa, na tela de Usuários (`.custom-css-users-card-presenca`)
- **Valores:** `online` · `offline` · `inactive`

### `data-usuario-id`

- **Onde:** caixa de seleção de cada pessoa no modal de compartilhar registro
- **Valores:** o id do usuário

### `data-vazia`

- **Onde:** coluna do quadro de atendimentos
- **Valores:** `true` quando a coluna não tem card nenhum · `false`. É o estado que `div:has(> .custom-css-quadro-card)` não consegue casar

### `data-video`

- **Onde:** a janela da chamada
- **Valores:** `true` · `false` — ESTA chamada negociou vídeo (não basta o operador poder)

### `data-view`

- **Onde:** botões de visualização (`.custom-css-view-toggle`) em Tarefas, Oportunidades, Conexões, Equipe, Webhooks, Prompts e Agendamentos
- **Valores:** a visualização que o botão escolhe: `card` · `list` · `calendar` (Tarefas) · `card` · `list` (Oportunidades: cartões ou tabela) · `grid` · `list` (Conexões, Equipe, Webhooks, Prompts) · `month` · `day` · `history` (Agendamentos). Qual está escolhida vai em `aria-pressed="true"`

### `data-visao`

- **Onde:** o ranking entre as lojas, no Ranking do CRM (`.custom-css-crm-ranking-grupos`)
- **Valores:** o que a lista compara: `equipes` · `unidades` · `funis` — o "Ranking por" escolhido (o ranking dos vendedores não usa esta caixa)

### `data-vista`

- **Onde:** a etiqueta "Vista por" de uma aula da IA já vista
- **Valores:** `sim`

### `data-volume`

- **Onde:** botão do som na barra do topo (`[data-appbar="sound"]`)
- **Valores:** o volume das notificações, de `0` (mudo) a `1`, em passos de `0.1` — `[data-volume="0"]` é o som desligado. O mesmo botão diz em `aria-expanded` se o controle está aberto

### `data-webphone`

- **Onde:** botão de chamada na barra de ações
- **Valores:** o modo de webphone do operador

### `data-window`

- **Onde:** faixa da conversa (Meta)
- **Valores:** estado da janela de 24h

### `data-zoom`

- **Onde:** a área da tela compartilhada na chamada (`.custom-css-chamada-tela-area`, na janela da chamada e na página do convidado)
- **Valores:** o zoom de agora, em porcentagem: `100` com a tela inteira, até `400` — dá para mostrar algo diferente quando a pessoa está aproximada

Exemplo — destacar mensagem não entregue e nota interna:

```css
.custom-css-msg-bubble[data-status="pending"] { opacity: .6; }
.custom-css-msg-bubble[data-origin="api"]     { border-left: 2px solid #888; }
[data-mode="internal"] textarea               { background: #fffbe6; }
```

⚠️ A altura do campo de digitação do atendimento: quem a calcula é o Material-UI, a cada letra, e ele a grava no próprio campo (`style="height: …px"`) — cresce até 5 linhas e para. Um `height` no CSS não vence o que está gravado no campo; `max-height` e `min-height` vencem, porque limitam essa altura em vez de disputar com ela. O `overflow` também vem gravado no campo: para a rolagem aparecer no campo mais baixo, ele leva `!important`. Para um campo mais baixo, com rolagem, ou que nunca encolha abaixo de duas linhas:

```css
.custom-css-composer-field textarea { max-height: 60px; overflow-y: auto !important; }
.custom-css-composer-field textarea { min-height: 40px; }
```
