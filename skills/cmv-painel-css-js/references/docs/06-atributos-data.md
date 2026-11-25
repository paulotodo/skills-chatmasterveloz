<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-30.215.0 -->

# Atributos de estado

Formato: um título `###` por **Atributo** (623 itens), com os campos Onde · Valores abaixo.

### `data-a-cobrar`

- **Onde:** o "Falta" da venda de balcão — quanto cobrar agora na forma escolhida
- **Valores:** o valor em reais, já com o desconto ou a taxa da forma (`0`: quitada)

### `data-aba`

- **Onde:** cada aba da lista de atendimentos (`.custom-css-ticket-tabs .MuiTab-root`), na visão individual e na de grupos; e cada aba da faixa Ticket / Atendimentos do celular (`.custom-css-mobile-tab`)
- **Valores:** `open` (Atendendo) · `pending` (Aguardando) · `pending-meus` (Aguardando (MEUS), só com a configuração "Aguardando com dono" ligada) — o mesmo vocabulário do `data-status` do cartão. No celular: `ticket` (a conversa aberta) · `atendimentos` (a lista), com a escolhida em `aria-selected`

### `data-aberto`

- **Onde:** painel que o "+" abre no campo de digitação; e o botão de figurinhas do compositor do Hub; e o painel do contato (`.custom-css-contact-drawer`)
- **Valores:** `true` · `false` — antes o estado só existia como `display: none` inline. No botão de figurinhas: se o seletor está aberto. No painel do contato: se ele está aberto — antes, fechado só se via pelo `visibility: hidden` que o Material-UI põe no estilo

### `data-aberto`

- **Onde:** cada e-mail da lista de E-mail (`.custom-css-emails-item`), junto com `aria-selected`
- **Valores:** `true` no e-mail aberto no leitor; ausente nos outros

### `data-aberto`

- **Onde:** cada dia nos horários de atendimento da agenda (`.custom-css-servicos-agenda-dia`)
- **Valores:** `true` tem horário · `false` fechado

### `data-acao`

- **Onde:** os botões de ação dos cartões e das tabelas dos cadastros: Tags, Setores, Respostas Rápidas, Categorias (de setores e de fluxos), Usuários (o cartão e as janelas de encerrar e de transferir os tickets), Contatos, Webhooks, Templates WABA, Arquivos do Bot, Contas de e-mail e Avaliações; o ícone de conversar dos Aniversariantes da Dashboard; o botão de concluir e de reabrir da lista de Tarefas
- **Valores:** o verbo do botão, em português. Em toda tela: `editar` · `excluir`. E os de cada uma — Tags: `ver-contatos`. Respostas Rápidas: `favoritar` (a estrela, também `.custom-css-quickmessage-favorita`). Usuários, no cartão: `encerrar-tickets` · `transferir-tickets` · `transferir-carteira` · `trocar-senha` · `acessos` (o histórico de entradas e saídas, `.custom-css-user-btn-acessos`); nas janelas de encerrar e de transferir os tickets: `cancelar` · `confirmar`. Contatos, na tabela: `resumo` · `iniciar-conversa` · `mais-acoes` (os três pontinhos do celular, que abrem o menu com os mesmos nomes em `data-menu-action`). Webhooks: `configurar` (abre o fluxo do webhook). Templates WABA: `visualizar` · `ver-json` · `editar-midia-local` (o botão que troca a mídia de exemplo) · `enviar-para-aprovacao`. Arquivos do Bot: `copiar-url`. Contas de e-mail: `adicionar` Usuários, no cartão (29.521.0): `presenca` — a bolinha do status e da sessão da pessoa (`.custom-css-user-btn-presenca`), com o status em `data-status`. No atendimento do canal Chat Externo (29.524.0), o botão de bloquear a conversa: `bloquear-conversa` · `desbloquear-conversa` — o mesmo valor do `data-action` dele. Só no botão: recolhida no menu `⋯` da barra, a ação vira um item que leva só o `data-action`. Aniversariantes da Dashboard (29.972.0): `abrir-atendimento` (abre um atendimento com o contato). Tarefas, na lista e nos cartões (29.973.0): `concluir` · `reabrir`.

### `data-acao`

- **Onde:** os botões do detalhe da reserva (`.custom-css-reservas-reserva-acao`)
- **Valores:** `confirmada` · `concluida` · `nao_compareceu` · `cancelar`

### `data-acao`

- **Onde:** a confirmação na página da ordem para o cliente (`.custom-css-servicos-publica-confirmacao`)
- **Valores:** `aprovar` · `recusar`

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

### `data-acoes-agrupadas`

- **Onde:** a barra de ações do ticket (`.custom-css-ticket-actions`)
- **Valores:** `true` a opção Ações do topo do ticket está em Agrupadas · `false` todas à mostra

### `data-acoes-busca`

- **Onde:** o campo de busca do menu Mais agrupado do ticket (`.custom-css-ticket-actions-busca`), que aparece a partir de 7 ações
- **Valores:** sempre `true`

### `data-action`

- **Onde:** botões do atendimento, da lista de atendimentos, do popup de encerramento, do Chat Interno, do painel do contato, do editor de fluxo, do Quadro de Atendimentos, dos Kanbans e do CRM
- **Valores:** na barra: `mark-as-read` (o "Marcar como lido", só com mensagem não lida) · `mark-as-unread` (o "Marcar como não lido", no mesmo lugar, quando não há não lidas — fora do atendimento encerrado) · `accept` (o Aceitar, no atendimento aguardando) · `finish` (o Encerrar, ao lado dele — só para admin e supervisor) · `resolve` · `return` · `transfer` · `schedule` · `task` · `delete` · `invite` · `call` · `files` · `flow` · `opportunity` · `summary` · `analyzer` · `contact-summary` · `accept-audio` · `external-chat-link` · `video-call` (a videochamada com o cliente) · `pdv-order` (o pedido do PDV) · `pdv-consulta` (a consulta de preço e estoque) · `mais-acoes` — são esses os nomes que a `--ticket-actions-ordem` e a `--ticket-actions-no-menu` usam (ver Propriedades). No celular, as ações ficam no menu de Ações (`.custom-css-ticket-actions-mobile` é a caixa dos botões), e `mais-acoes` é o botão que abre esse menu. No popup de encerramento: `resolve-silent` (sem mensagem) · `resolve-message` (com mensagem) · `resolve-rating` (com avaliação) — os dois primeiros são idênticos no DOM, só o texto difere. Os mesmos três valores estão nas três saídas da Tela 3 do encerramento em 3 passos (`.custom-css-modal-encerramento`), onde `resolve-message` é o botão verde, principal. No campo de mensagem (os dois compositores): `send` — o botão de enviar, que vira `forward` enquanto o modo de selecionar mensagens está ligado (o mesmo botão encaminha as escolhidas); `upload` (anexar) · `record-audio` (gravar áudio) · `emoji` · `send-contact` (enviar contato); `external-only` — o "Somente chat externo", com `aria-pressed`, como `signature` e `internal` ao lado; `extras` — o "+" que abre o painel de extras, com `aria-expanded`; `fechar-extras` — o X desse painel. Nos dois: `ver-notas-internas` — o botão das notas internas, que abre o `.custom-css-popover-notas-internas`. Só no compositor do Hub: `figurinhas` (o botão que abre o seletor de figurinhas) · `quick-favorites` (as mensagens rápidas favoritas) · `contact-notes` (as notas do contato). No menu `⋯` da barra, o item de uma ação que é interruptor (`accept-audio`) é `role="menuitemcheckbox"` com `aria-checked` — o estado de verdade, e o clique nele liga e desliga. No Chat Interno, em cada conversa da lista (`.custom-css-chats-item`): `favorite` · `mark-unread` (só na conversa sem nada por ler) · `edit` (só para quem criou a conversa) · `delete` (para quem criou e para o admin) · `privada` (o cadeado: liga e desliga a conversa privada — quem participa decide; o administrador de fora não a vê); no campo de mensagem (`.custom-css-chats-composer`): `record-audio` · `upload` · `send` — os mesmos nomes do campo de mensagem do atendimento. No painel do contato (`.custom-css-contact-drawer`): `fechar` — o X do topo, que também ganhou `aria-label`; `editar` — o botão Editar do cartão (`.contact-card-editar`). Na lista de atendimentos (`#custom-css-tickets-page`): `new-ticket` (o Novo) · `sort` (o Ordenar) · `more-filters` (o "+" que abre os filtros) · `advanced-search` (a Busca Avançada); e, no cartão do ticket, `accept` (o Aceitar do aguardando) · `spy` (o olho do Espiar) · `finish` (o Encerrar do aguardando, só para admin e supervisor). No card do Quadro de Atendimentos: `pin` (a estrela de fixar, `.custom-css-quadro-fixar`) · `finish` (o Encerrar, `.custom-css-quadro-encerrar`, quando o encerrar está ligado na barra do quadro). No card dos quatro Kanbans: `spy` (o olho, que abre a conversa numa janela). No editor de fluxo, na barra de cima (`.custom-css-flow-barra`): `desfazer` · `refazer` · `buscar` · `resumo` · `organizar` · `verificar` · `versoes` · `salvar` — os três que abrem um painel (`buscar`, `resumo` e `versoes`) dizem em `aria-pressed` se ele está aberto; em cada bloco do desenho do fluxo (`.custom-css-flow-node-acoes`): `copiar` · `excluir`; e, na janela de escolher o bloco (`.custom-css-flow-escolher-item`), o tipo do bloco que o item cria (`menu`, `question`, `switch`…). Nas atividades da oportunidade (`.custom-css-atividades`): `criar-atividade` (criar, ou salvar a que está em edição) · `cancelar-edicao` · `editar-atividade` (o assunto, que abre a atividade para editar) · `concluir` / `reabrir` (o que o clique FAZ, conforme a atividade está aberta ou concluída) · `anexos` · `excluir` · `abrir-reuniao` (o link da reunião) · `copiar-link`. Na conexão do Google Calendar (`.custom-css-google-calendar-conexao`): `conectar-calendar` · `desconectar-calendar` · `escolher-agenda`. Na conciliação de conexões (`.custom-css-conciliacao-conexoes`): `filtrar-excedente` · `baixar-csv` · `detalhar-empresa` (abre e fecha a linha da empresa) · `limpar-conexoes` (apaga as conexões da empresa). Nas regras de encadeamento dos funis do CRM: `adicionar-regra` · `remover-regra`. No atendimento do canal Chat Externo, a barra (e o menu de Ações do celular) tem também `bloquear-conversa` · `desbloquear-conversa` — o que o clique faz, conforme a conversa está liberada ou bloqueada; o mesmo valor vai no `data-acao` do botão — recolhida no menu `⋯` da barra, o item leva só o `data-action`, como todo item desse menu · No Chat Interno, na conversa aberta: `buscar-na-conversa` (a lupa do cabeçalho, que abre a busca) e, na busca, `fechar-busca`; no campo de mensagem, `emoji` e `figurinhas` (os seletores); na barra da mensagem em edição, acima do campo (`.custom-css-chat-interno-editando`), `cancelar-edicao` — o X que desiste · No cartão do #protocolo do chat interno (`.custom-css-chats-protocolo`), `espiar-protocolo` — o olho, que abre a conversa do atendimento · no Cardápio Digital: `novo-cupom` (abre a janela do cupom novo) · `editar-cupom` · `remover-cupom` · `salvar-cupom` (o botão da janela) · na Avaliação pela IA: `salvar-avaliacao-ia` (o Salvar da configuração) · `salvar-webhook-avaliacao-ia` (o Salvar do webhook dela, em Webhooks e integrações) · `avaliar-agora` (roda a avaliação na hora) · `exportar-avaliacoes` (baixa a lista em CSV) · `abrir-conversa` (abre o atendimento avaliado) · `marcar-aula-vista` (marca a aula como lida) · no Consultório: `abrir-teleconsulta` (abre a sala da teleconsulta, na recepção) · `copiar-link-teleconsulta` (copia o link do paciente) · `enviar-link-teleconsulta` (manda o link no atendimento, no painel do contato) · no prontuário: `abrir-prontuario` (o botão na lista de pacientes) · `registrar-prontuario` (salva o registro, ou a retificação) · `retificar-prontuario` (escreve a correção de um registro) · `criar-chave-prontuario` e `restaurar-chave-prontuario` (o botão da chave, nas opções do Consultório) · `novo-modelo-documento` e `salvar-modelo-documento` (os modelos de documento, nas opções do Consultório) · `novo-documento`, `emitir-documento`, `pdf-documento`, `cancelar-documento` e `confirmar-cancelamento-documento` (os documentos do paciente, na janela do prontuário) · `enviar-documento` (enviar o documento, no painel do contato) · `nova-receita`, `adicionar-item-receita`, `remover-item-receita` e `emitir-receita` (a receita, nos documentos do paciente) · `cobranca-da-consulta` (abre a cobrança da consulta, no painel do contato) · nos E-mails: `buscar-anteriores-na-busca` (traz as mensagens anteriores quando a busca não acha nada nas já trazidas) · na Avaliação pela IA, o processo ideal nas Opções: `adicionar-etapa` · `subir-etapa` · `descer-etapa` · `remover-etapa` · `salvar-processo`; no relatório: `ver-quem-saiu` (filtra quem não seguiu a etapa) · `ver-etapas` (abre as etapas da avaliação) · na aba Hoje: `ver-atendimentos` (abre o relatório do vendedor, na etapa em que ele saiu) · `abrir-pior-conversa`; na janela da avaliação aberta pelo alerta do sino: `abrir-conversa-do-alerta` · `fechar-detalhe`; nas Opções: `salvar-alertas` (a nota do alerta) · nos Projetos: `salvar-avisos-do-projeto` (o Salvar da janela dos avisos ao cliente) · em Configurações → Opções: `limpar-busca-das-opcoes` (o X de "Pesquisar opção") · no aviso das filas sem expediente: `abrir-expediente` (o link para o Gerenciamento de Expediente) · no Painel de Pedidos: `cancelar-pedido-do-painel` (o Cancelar pedido do cartão) e, na janela do motivo (`.custom-css-modal-cancelar-pedido-do-painel`), `voltar-do-cancelamento` · `confirmar-cancelamento-do-pedido` · `confirmar-recusa-do-pedido` (o Recusar do pedido em Novo)

### `data-action-rotulo`

- **Onde:** o texto ao lado do ícone na barra agrupada (`.custom-css-ticket-acao-rotulo`)
- **Valores:** o `data-action` da ação do texto (`mais-acoes` no Mais)

### `data-active`

- **Onde:** item do menu lateral e cartão do menu da tela de Configurações
- **Valores:** `true` / `false` no item do menu lateral — `true` em **um item só**, o da tela aberta: quando um destino é prefixo de outro que também está no menu (`/ratings` e `/ratings/report`), só o mais específico acende; rota aninhada que não está no menu (`/tickets/<id>`) acende o item pai · `true` / `false` no cartão de Configurações, conforme a aba aberta

### `data-admin`

- **Onde:** a linha de um usuário em "Quem vê qual agenda" do Consultório (`.custom-css-consultorio-acesso`)
- **Valores:** `sim` (o administrador, que vê todas) · `nao`

### `data-agenda-google`

- **Onde:** a seção da agenda do Google na janela do recurso das reservas (`.custom-css-reservas-recurso-agenda-google`)
- **Valores:** `ligada` · `desligada`

### `data-agendamento`

- **Onde:** cada cartão da agenda do Consultório (`.custom-css-consultorio-agenda-cartao`), na página `/consultorio-agenda`
- **Valores:** o id da consulta ou do bloqueio do cartão — o mesmo cartão aparece com o mesmo valor no dia e na semana. O tipo e o status vão na classe (`custom-css-consultorio-agenda-bloqueio`, `-agendado`, `-confirmado`, `-atendido`, `-faltou`, `-cancelado`)

### `data-aguardando`

- **Onde:** aviso de coluna pausada no quadro de atendimentos
- **Valores:** quantas atualizações chegaram enquanto a coluna está pausada (`0` quando nada mudou) — dá para esconder o aviso quando não há nada esperando

### `data-aguardando-envio`

- **Onde:** selo na mensagem represada pelo concatenador
- **Valores:** `true` — a mensagem existe e ainda não saiu

### `data-ajuste-da-forma`

- **Onde:** a linha do desconto ou da taxa da forma de pagamento: no balcão (`.custom-css-balcao-ajuste-da-forma`), nos totais do pedido (`.custom-css-pedido-ajuste-da-forma`) e no valor do pagamento (`.custom-css-pedido-regra-da-forma`)
- **Valores:** o valor em reais: negativo é desconto, positivo é taxa (`0`: nenhum)

### `data-ajuste-do-pagamento`

- **Onde:** cada pagamento da janela do pedido que teve desconto ou taxa da forma
- **Valores:** o ajuste em reais: negativo é desconto, positivo é taxa

### `data-alterada`

- **Onde:** janela do editor de imagem (`.custom-css-modal-editor-de-imagem`)
- **Valores:** `true` quando já há alguma edição (e fechar pede confirmação) · `false` — concluir sem edição devolve a foto original, sem recomprimir

### `data-alvo-id`

- **Onde:** cada regra por funil ou por etiqueta da janela de Pontuação e níveis (`.custom-css-gamificacao-regra` com `data-regra="funil"` ou `data-regra="etiqueta"`)
- **Valores:** o id do funil ou da etiqueta da regra

### `data-amqp-vazio`

- **Onde:** aviso de monitor AMQP sem mensagem
- **Valores:** `sem-fila` (nenhuma conexão da empresa passa por RabbitMQ) · `sem-mensagem` (passa, mas nada chegou)

### `data-anexo`

- **Onde:** cada arquivo enviado junto de um comentário da tarefa (`.custom-css-tarefa-comentario-anexos`)
- **Valores:** o número do anexo

### `data-animada`

- **Onde:** a mesma figurinha
- **Valores:** `true` quando o WebP é animado · `false`

### `data-answer-from-ia`

- **Onde:** sugestão de resposta com IA (barra e cartão sobre o campo, e a aba de Tokens de IA)
- **Valores:** no bloco: `barra` · `cartao`. Dentro dele: `sugerir` · `melhorar` · `saldo` · `sugestao` · `texto` · `usar` · `nova` · `descartar`. Na aba do super: `ilimitado` · `abrir-recarga` · `recarga-pontos` · `recarga-observacao`

### `data-answer-from-ia-camada`

- **Onde:** painel flutuante da sugestão de IA
- **Valores:** `padrao` · `acima-do-dialogo` — quando a barra vive dentro de um diálogo, o painel precisa ficar acima dele

### `data-antes`

- **Onde:** cada lembrete da aba dos avisos das Reservas (`.custom-css-reservas-lembrete`)
- **Valores:** quantos minutos antes do horário o lembrete sai

### `data-ao-enviar`

- **Onde:** o "Ao enviar" do lembrete e da confirmação do Consultório (`.custom-css-consultorio-ao-enviar`)
- **Valores:** `nao-abrir` (a mensagem sai e nada entra na fila) · `abrir` (abre o atendimento no setor)

### `data-apagada`

- **Onde:** balão de mensagem do chat interno
- **Valores:** `true` · `false` — se a mensagem foi apagada

### `data-apagada-por`

- **Onde:** balão de mensagem apagada
- **Valores:** quem apagou (o nome), ou `desconhecido` quando o registro não diz

### `data-appbar`

- **Onde:** botões da barra do topo
- **Valores:** `menu` · `tickets` (o balão dos atendimentos) · `notifications` (o sino) · `push` (o sino das notificações push, com `aria-pressed`: ligadas ou não neste navegador) · `announcements` · `internal-chat` (o Chat Interno; antes era `msgs`) · `status` · `extension` (o ramal) · `dialer` (o discador) · `theme` · `lang` · `font` · `sound` · `ping` · `refresh` · `collapse` · `user` · `tarefas-em-execucao` (as tarefas que estão em execução agora, com o número em `data-quantas`) · `mais` (o "+" do celular, que abre o menu com o idioma, a latência, o atualizar e o tema — o atualizar e o tema, dentro dele, levam os mesmos `refresh` e `theme`)

### `data-atalho`

- **Onde:** botões de atalho do valor na Tela 2 do encerramento em 3 passos (`.custom-css-encerramento-atalho`)
- **Valores:** `50` · `100` · `500` (somam ao valor) · `limpar` (zera)

### `data-atendente`

- **Onde:** na Avaliação pela IA: cada vendedor de quem precisa de você (`.custom-css-avaliacao-ia-precisa`), cada um dos que estão em dia (dentro de `.custom-css-avaliacao-ia-em-dia`) e cada linha da Evolução (`[data-grafico="evolucao-semanal"]`)
- **Valores:** o id do vendedor; na linha do time inteiro, `time`

### `data-ativa`

- **Onde:** o botão Ativa de cada adicional e sabor no cadastro do produto (`.custom-css-produto-opcao-ativa`)
- **Valores:** `sim` a opção está à venda · `nao` desativada (some do Cardápio, do Balcão e da Mesa)

### `data-ativa`

- **Onde:** cada regra de lembrete na aba Confirmação do Consultório (`.custom-css-consultorio-lembrete`)
- **Valores:** `sim` a regra está ligada · `nao` desligada

### `data-ativa`

- **Onde:** cada chave da API na aba Integrações do Consultório (`.custom-css-consultorio-chave`)
- **Valores:** `sim` a chave vale · `nao` revogada (fica na lista, sem valer)

### `data-ativa`

- **Onde:** chip de pasta no seletor de figurinhas e item de pasta na tela de Figurinhas; e, no editor de imagem, cada botão de ferramenta (`.custom-css-editor-de-imagem-ferramenta`) e cada cor da paleta (`.custom-css-editor-de-imagem-cor`)
- **Valores:** `true` na pasta aberta · `false`. No editor: `true` na ferramenta em uso e na cor escolhida · `false`

### `data-atividade-mcp-aba`

- **Onde:** cada aba da página Atividade do MCP (a atividade e o que espera aprovação)
- **Valores:** `atividade` · `aprovacoes`

### `data-atividade-mcp-aprovacao`

- **Onde:** cada pedido de aprovação na página Atividade do MCP (`.custom-css-atividade-mcp-aprovacao`)
- **Valores:** `pendente` · `aprovada` · `recusada` · `falhou`

### `data-atividade-mcp-ok`

- **Onde:** cada linha da atividade do MCP (`.custom-css-atividade-mcp-item`)
- **Valores:** `true` (deu certo), `false` (recusado) ou vazio (registro sem resultado, como um token gerado)

### `data-ativo`

- **Onde:** o cartão de cada fluxo na lista de fluxos (`.custom-css-flow-card`) e a etiqueta de estado dele (`.custom-css-flow-card-status`)
- **Valores:** `true` no fluxo ativo · `false` no desativado — o mesmo que a etiqueta diz

### `data-ativo`

- **Onde:** a mensagem da vaga na aba dos avisos das Reservas (`.custom-css-reservas-aviso-vaga`)
- **Valores:** `1` ligada, `0` desligada

### `data-ativo`

- **Onde:** cada aviso da aba Avisos dos Serviços (`.custom-css-servicos-aviso`)
- **Valores:** `true` ligado (sai sozinho na etapa) · `false` desligado

### `data-atrasada`

- **Onde:** atividade do CRM (painel e cartão) e o cartão de tarefa (`.custom-css-task-card`)
- **Valores:** `true` quando o prazo passou — o único estado que pede ação agora. Ausente nos outros casos. Na tarefa: pendente, e o dia (o que a tela mostra) já passou, ou é hoje e já passou da hora marcada; tarefa concluída nunca está atrasada

### `data-atrasada`

- **Onde:** cada tarefa do quadro na página do projeto (`.custom-css-projeto-tarefa`)
- **Valores:** `true` quando o prazo passou e a tarefa não foi concluída; ausente nas outras

### `data-atrasada`

- **Onde:** cada ordem de serviço na lista (`.custom-css-servicos-ordem-na-lista`)
- **Valores:** `true` a previsão de entrega passou e a ordem ainda não ficou pronta · `false`

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

### `data-ausente`

- **Onde:** o atendente da coluna na visão por atendentes do Quadro (`.custom-css-quadro-coluna-atendente`)
- **Valores:** `true` (online, mas com o status Ausente — o ponto fica amarelo e ele não recebe pelo rodízio) · `false`

### `data-avaliacao`

- **Onde:** cada linha da tabela dos atendimentos avaliados (`[data-lista="avaliacoes"]`)
- **Valores:** o id da avaliação

### `data-avaliacao-detalhe`

- **Onde:** o conteúdo da janela de uma avaliação pela IA (`.custom-css-avaliacao-ia-detalhe`), aberta pelo alerta do sino
- **Valores:** o id da avaliação

### `data-avatar`

- **Onde:** avatar no balão
- **Valores:** `contact` · `user` · `ia` (a mensagem do assistente de IA, com o selo IA) · `none`

### `data-aviso-falta`

- **Onde:** cada aviso ao cliente na janela do link de agendamento (`.custom-css-link-de-agendamento-aviso`)
- **Valores:** `nenhuma` (pronto para salvar) · `tempoInvalido` · `horaInvalida` · `semTexto` · `modeloIncompleto`

### `data-aviso-momento`

- **Onde:** cada aviso ao cliente na janela do link de agendamento (`.custom-css-link-de-agendamento-aviso`)
- **Valores:** `confirmacao` (ao marcar) · `antes` (antes da reunião) · `nodia` (no dia, a uma hora) · `depois` (depois da reunião)

### `data-avisos`

- **Onde:** a seção Avisos e automações da janela do link de agendamento (`.custom-css-link-de-agendamento-automacao`)
- **Valores:** quantos avisos ao cliente o link tem (`0` a `10`)

### `data-avulsa`

- **Onde:** a janela da peça ou do serviço da ordem (`.custom-css-modal-servicos-linha`)
- **Valores:** `true` item lançado à mão, fora do catálogo · `false` veio do catálogo

### `data-badge`

- **Onde:** selo do modo da conta Meta no cartão da conexão (`.custom-css-connection-badge`)
- **Valores:** o evento, em minúsculas: `live` · `sandbox` · `pending`, ou o evento que a Meta mandou (`account_disconnected`…). O nível vai em `data-nivel`

### `data-baixada`

- **Onde:** cada peça ou serviço da ordem (`.custom-css-servicos-ordem-linha`)
- **Valores:** `true` a peça já saiu do estoque · `false` ainda não (ou é serviço)

### `data-barra`

- **Onde:** cada barra do gráfico da distribuição das notas (`[data-grafico="distribuicao"]`)
- **Valores:** a nota daquela barra, de `0` a `10`

### `data-barra-concatenacao`

- **Onde:** barra que avisa que a próxima mensagem será concatenada
- **Valores:** `true`

### `data-bloco`

- **Onde:** cada bloco do editor do modelo do Mail Marketing e cada tipo no menu Adicionar bloco (`.custom-css-mail-marketing-bloco`)
- **Valores:** `titulo`, `texto`, `imagem`, `botao`, `colunas`, `divisor`, `espaco` ou `html`

### `data-bloqueio`

- **Onde:** o aviso da URL parada no webhook do Consultório (`.custom-css-consultorio-webhook-bloqueado`)
- **Valores:** `http` a URL começa com http:// · `sem-token` a empresa não tem o token gerado

### `data-bloqueio`

- **Onde:** o aviso do webhook parado nas Reservas (`.custom-css-reservas-webhook-bloqueado`)
- **Valores:** `sem-token` a empresa não tem o token gerado (nada sai sem assinatura)

### `data-bloqueio`

- **Onde:** o aviso do webhook parado nos Serviços (`.custom-css-servicos-webhook-bloqueado`)
- **Valores:** `sem-token` a empresa não tem o token gerado (nada sai sem assinatura)

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

### `data-caminho`

- **Onde:** cada número do painel Quanto a automação resolve do Dashboard (`.custom-css-dashboard-automacao-numero`)
- **Valores:** `semPessoa` (resolvidos sem pessoa) · `passou` (passaram para uma pessoa) · `direto` (direto com uma pessoa) · `eficiencia` (a parte resolvida pela automação)

### `data-campanha`

- **Onde:** cada linha da lista de campanhas do Mail Marketing (`.custom-css-mail-marketing-campanhas`)
- **Valores:** o número da campanha

### `data-campanha-id`

- **Onde:** cada campanha da janela de Campanhas (`.custom-css-gamificacao-campanha`); cada campanha na lista do seletor de período (`.custom-css-seletor-periodo-campanha`); e a linha da contagem do nível em Minha Evolução (`.custom-css-minha-evolucao-contagem`), quando o nível conta numa campanha
- **Valores:** o id da campanha

### `data-campo`

- **Onde:** formulário de atividade do CRM, seletor de motivo por funil e liberação de agenda
- **Valores:** na atividade: `tipo` · `responsavel` · `assunto` · `descricao` · `data` · `hora` · `duracao`, e `descricao-lista` no texto já gravado. Nos cadastros do CRM: `funil-do-novo`. Nas regras de encadeamento: `produto-da-regra` · `destino-da-regra` · `responsavel-da-regra`. No cadastro de usuário: `agendas-visiveis`. Nas tarefas: `filtro-de-agenda`

### `data-campo`

- **Onde:** as quantidades do Monte seu plano (`.custom-css-monte-seu-plano-quantidade`) e os campos da tabela na tela de planos (`.custom-css-planos-monte-campo`)
- **Valores:** na página: `usuarios` · `conexoes` · `setores`. Na tabela: `base.valor` · `base.usuarios` · `base.conexoes` · `base.setores` · `extras.usuario` · `extras.conexao` · `extras.setor` · `maximos.usuarios` · `maximos.conexoes` · `maximos.setores` · `modulo.mensal` · `modulo.implantacao` · `implantacao`

### `data-campo-responsavel`

- **Onde:** campo de responsável no modal da oportunidade
- **Valores:** `true` — marca o campo que define de quem é a venda

### `data-canal`

- **Onde:** cada caixa de canal de uma regra em Desconto e taxa por forma de pagamento (`.custom-css-ajuste-da-forma-canal`)
- **Valores:** `balcao` (Mesas, Comandas e Balcão) · `delivery` (pedido online e entrega)

### `data-canal`

- **Onde:** linha de canal na conciliação de conexões e pílula do monitor AMQP
- **Valores:** a chave do grupo (`whatsapp`, `hub`, `instagramInc`, …)

### `data-cancelar`

- **Onde:** o que o botão Cancelar faz na confirmação do Consultório (`.custom-css-consultorio-acoes-dos-botoes`)
- **Valores:** `pergunta` (pergunta antes se o paciente tem certeza) · `direto` (cancela no toque)

### `data-carregados`

- **Onde:** o contador de cada aba da lista de atendimentos (`.custom-css-ticket-tabs-contador`, o `.MuiBadge-root` da aba), ao lado do `data-total`
- **Valores:** quantos atendimentos a lista já carregou

### `data-carregando`

- **Onde:** barra da sugestão de IA; o seletor de figurinhas do compositor; e a janela do editor de imagem (`.custom-css-modal-editor-de-imagem`)
- **Valores:** na IA: `true` enquanto a IA gera — é por ele que se estiliza o estado "Gerando sugestão…". No seletor: `true` enquanto as pastas carregam. No editor: `true` enquanto a foto abre · `false`

### `data-cartao`

- **Onde:** cada cartão da API Oficial no Dashboard (`.custom-css-dashboard-api-oficial-cartao`) e cada cartão da linha aberta do atendente no ranking (`.custom-css-dashboard-atendente-cartao`)
- **Valores:** na API Oficial: `economia` · `enviadas` · `custo` · `media`. No atendente: `resolvidos` · `atendimentosComMensagem` · `mensagensEnviadas` · `mensagensPorAtendimento` · `templatesEnviados` · `custoNoPeriodo`

### `data-categoria`

- **Onde:** cartão de categoria do Criar Template (WABA)
- **Valores:** o tipo de modelo, como a Meta o chama: `STANDARD` (Padrão) · `CATALOG` · `ORDER_DETAILS` · `CALL_PERMISSION`. Os que aparecem dependem da categoria escolhida nas abas (Marketing, Utilidade, Autenticação). O escolhido leva `data-selected="true"`

### `data-categoria-do-template`

- **Onde:** o aviso da prévia de exemplo do Criar Template (WABA), junto do `data-previa`
- **Valores:** a aba (categoria) escolhida, como a Meta a chama: `MARKETING` · `UTILITY` · `AUTHENTICATION`

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

### `data-chegadas`

- **Onde:** cada hora do mapa de horários de pico do Dashboard (`.custom-css-dashboard-pico-celula`)
- **Valores:** quantos atendimentos chegaram naquela hora no período (`0`, `1`, `2`...)

### `data-cliente`

- **Onde:** cada cliente achado na busca e o resumo aberto na página Clientes do PDV (`.custom-css-clientes-pdv-achados`, `.custom-css-clientes-pdv-resumo`)
- **Valores:** o id do contato

### `data-clone-estado`

- **Onde:** a janela do Clonar conexão (`.custom-css-modal-clonar-conexao`)
- **Valores:** `confirmar` (a explicação, antes de clonar) · `clonando` (esperando o servidor) · `pronto` (o resultado e o botão de ler o QR Code)

### `data-cobrancas`

- **Onde:** o valor da venda do projeto (`.custom-css-projeto-venda-cobranca`, ao lado de `.custom-css-projeto-venda-valor`)
- **Valores:** as cobranças da venda, separadas por espaço: `unica` · `mensal` · `anual` (só as que existem)

### `data-collapsed`

- **Onde:** menu lateral
- **Valores:** `true` quando recolhido

### `data-colocacao`

- **Onde:** cada linha do ranking entre as lojas (`.custom-css-crm-ranking-grupo`)
- **Valores:** a colocação, de `1` em diante: o maior valor vendido primeiro, depois a maior quantidade, e o nome desempata

### `data-coluna`

- **Onde:** as colunas novas do Ranking de Agentes no Dashboard (o cabeçalho que ordena e a célula de cada pessoa)
- **Valores:** `primeira-resposta` (a 1ª resposta média) · `no-sla` (a % dos resolvidos dentro do SLA)

### `data-coluna-pausada`

- **Onde:** coluna do quadro de atendimentos
- **Valores:** `true` na coluna com a atualização pausada, `false` nas demais

### `data-coluna-tipo`

- **Onde:** coluna do quadro de atendimentos (no quadro e na tela de configuração)
- **Valores:** `PENDENTES` · `ATENDENDO` (as duas fixas) · `LIVRE` (aberto, criada pelo admin) · `PENDENTE_LIVRE` (pendente, classificação manual) · `PENDENTE_FILA` (pendente, automática: recebe sozinha os pendentes das filas da regra). Na visão por tags ("Ver o quadro por: Tags"): `TAG` (cada tag marcada como Kanban) · `SEM_TAG` (os atendimentos sem nenhuma delas)

### `data-com-erro`

- **Onde:** o cartão da automação do Instagram (`.custom-css-ig-automacao-card`)
- **Valores:** `true` quando a última resposta falhou na Meta (o selo vermelho com o motivo) · `false`

### `data-com-imagem`

- **Onde:** o botão Enviar na conversa de cada linha da consulta de preço e estoque (`.custom-css-consulta-de-produtos-enviar`)
- **Valores:** `true` vai a foto do produto com o valor na legenda · `false` só o valor

### `data-comanda-id`

- **Onde:** cada conta aberta (e cada conta do Histórico) da página Mesas e Comandas (`.custom-css-comandas-aberta`)
- **Valores:** o id da conta (a comanda) — o mesmo do `comanda.id` do webhook

### `data-comentario-id`

- **Onde:** cada comentário da tarefa e da oportunidade (`.custom-css-comentarios`) e do diálogo de comentários da página de Tarefas
- **Valores:** o id do comentário — o que a notificação aponta ganha também `.custom-css-comentario-em-destaque`

### `data-compacta`

- **Onde:** cada oportunidade do modo lista no celular em pé (`.custom-css-oportunidades-linha` dentro de `.custom-css-oportunidades-lista-compacta`)
- **Valores:** `true` — a linha é o bloco do celular (na tabela, a linha não tem o atributo)

### `data-comprovante`

- **Onde:** cada opção do menu Imprimir da ordem de serviço (`.custom-css-servicos-ordem-comprovante`)
- **Valores:** `entrada` · `orcamento` · `entrega`

### `data-concat-example`

- **Onde:** prévia do texto concatenado, no modal do concatenador
- **Valores:** `true`

### `data-concat-field`

- **Onde:** campos do modal do concatenador
- **Valores:** `enabled` · `mode` · `timeout`

### `data-concat-indicator`

- **Onde:** selo de concatenação no cartão da conexão
- **Valores:** o id da conexão

### `data-concluida`

- **Onde:** cada etapa na página do convidado (`.custom-css-convidado-etapa`)
- **Valores:** `true` (a etapa foi concluída) · `false`

### `data-condicao-tipo`

- **Onde:** cada condição no editor de regra do quadro (`.custom-css-regra-editor-condicao`)
- **Valores:** `TEXTO` · `TEM_TAG` · `NAO_TEM_TAG` · `FILA` · `CONTATO` · `CONEXAO` · `CLIENTE_ESPERANDO` · `CLIENTE_SEM_RESPONDER`

### `data-conectado`

- **Onde:** bloco de conexão do Google Calendar
- **Valores:** `true` · `false`

### `data-conexao`

- **Onde:** escolha do tipo de conexão, ao criar uma nova
- **Valores:** `sem-aparelho` · `oficial-app-proprio` · `oficial-portal` · `chat-externo` · `gupshup`

### `data-conexoes`

- **Onde:** o aviso das conexões oficiais em que o modelo não existe (`.custom-css-consultorio-modelo-aviso`)
- **Valores:** os ids dessas conexões, separados por espaço

### `data-connected`

- **Onde:** botão do ramal na barra do topo (`[data-appbar="extension"]`) — o estado inteiro está no `data-status` do mesmo botão
- **Valores:** `true` · `false` — o estado do ramal. Sem ele, a única forma de saber se o ramal está conectado era ler a COR do ícone

### `data-connection`

- **Onde:** etiqueta verde da conexão no card do quadro de atendimentos
- **Valores:** o NOME da conexão ("Comercial", "Suporte"…) — dá para colorir o card por conexão, o que o `data-channel` não permite, porque ele só diz o canal

### `data-connection-action`

- **Onde:** botões do cartão de conexão
- **Valores:** `close-all` · `close-pending` · `templates` · `template-errors` (os templates que a Meta recusou) · `edit` · `delete` · `qrcode` · `profile` · `sip` · `sip-config` · `hybrid` · `proxy` · `rotate-ip` · `restart-pro` (reiniciar a conexão whatsmeow_pro) · `validate-code` (validar o código de registro) · `events` · `import-session` · `pair-code` · `passkey` · `reconnect` · `new-qr` · `disconnect` (Desconectar) · `delete-session` (Excluir Sessão: apaga a sessão, e o número precisa ler o QR de novo) · `send-limit` (o limitador de mensagens) · `concatenador` · `meta-recheck` (Verificar agora, na oficial nativa) · `meta-reconnect` (Reconectar, na oficial nativa) · `ig-check-subscription` (Verificar inscrição, no Instagram) · `copiar-link-entrada` (Copiar link de entrada, no canal Chat Externo) · `pause` · `resume` (pausar e retomar a conexão; só o admin vê, e o botão troca de valor conforme a conexão está pausada ou não). "Fechar Todos" e "Fechar Pendentes" são o mesmo botão no DOM — só o texto difere, e texto morre na troca de idioma. O "Conectando…", desabilitado, não tem ação No WhatsApp Gupshup: `copiar-url-gupshup` (copia a URL de recebimento para cadastrar no painel da Gupshup). No RCS: `copiar-url-rcs` (copia a URL do webhook para cadastrar no painel do provedor). E `clone` (Clonar conexão: a cópia com a configuração, os atendimentos passam para ela e a atual é apagada; só nas conexões de QR Code, e só o admin vê).

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

### `data-conta-meta`

- **Onde:** cada linha da conta Meta no cartão da conexão da API oficial, em Conexões (`.custom-css-connection-meta`)
- **Valores:** `nome-verificado` (o nome verificado do número) · `bm` (a empresa na Meta) · `waba` (a conta do WhatsApp Business)

### `data-conta-meta-lida`

- **Onde:** o bloco da conta Meta no cartão da conexão da API oficial, em Conexões (`.custom-css-conta-meta`)
- **Valores:** `sim` os dados já foram lidos na Meta · `nao` ainda não

### `data-contact-id`

- **Onde:** cartão do ticket, cabeçalho da conversa aberta, ficha lateral do contato e a linha da tabela de Contatos
- **Valores:** o id do contato. A ficha **não publicava identificador nenhum** — nome, telefone e e-mail existiam só como texto, e ligar uma anotação ou um registro de CRM ao contato certo dependia de casar texto, que se repete entre contatos e muda quando alguém corrige um cadastro

### `data-contagem`

- **Onde:** a linha acima do nível em Minha Evolução (`.custom-css-minha-evolucao-contagem`), que diz de onde o nível conta
- **Valores:** `campanha` (o nível soma só os pontos da campanha) · `livre` (fora de campanha: o tempo entre uma campanha e outra). Na empresa sem campanha a linha não aparece, e o nível conta desde sempre

### `data-contato`

- **Onde:** cada contato na janela Contatos da lista do Mail Marketing (`.custom-css-modal-mail-marketing-contatos`)
- **Valores:** o número do contato na lista

### `data-contato-id`

- **Onde:** cada cliente sugerido na busca do cliente da conta da mesa (`.custom-css-conta-da-mesa-cliente-sugerido`)
- **Valores:** o id do contato que a conta vai levar ao ser escolhido

### `data-convenio`

- **Onde:** cada convênio no cadastro do profissional do Consultório (`.custom-css-consultorio-profissional-convenio`)
- **Valores:** o id do convênio

### `data-convidado-id`

- **Onde:** cada linha da janela dos convidados externos (`.custom-css-convidados-externos-linha`)
- **Valores:** o id do convidado

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

### `data-da-equipe`

- **Onde:** cada reação de um arquivo na galeria (`.custom-css-ticket-files-reacao`, com o emoji em `data-emoji`)
- **Valores:** `true` (a reação é da equipe — clicar tira) · `false` (é do contato)

### `data-dash-view`

- **Onde:** cartões "O que você gostaria de ver?" do Dashboard; e os blocos da seção que cada um abre (`.custom-css-dashboard-painel`)
- **Valores:** `estatisticas` · `linha-do-tempo` · `equipe` · `relatorios` · `aniversariantes`. O cartão da seção aberta leva `aria-expanded="true"`; os outros, `false` — e o mesmo cartão fecha a seção. O bloco leva o MESMO valor do cartão que o abre (Linha do tempo, Equipe e Relatórios têm dois blocos cada)

### `data-data`

- **Onde:** cada data da prévia da série (`.custom-css-reservas-serie-data`)
- **Valores:** a data (`AAAA-MM-DD`)

### `data-de`

- **Onde:** o seletor da despedida no cadastro do usuário, do setor e da conexão (`.custom-css-regra-da-despedida`)
- **Valores:** de quem é a regra: `usuario` · `setor` · `conexao`

### `data-deleted`

- **Onde:** balão da mensagem
- **Valores:** `true` quando apagada

### `data-descadastrado`

- **Onde:** o selo descadastrado ao lado do e-mail na janela Contatos da lista do Mail Marketing
- **Valores:** `sim`

### `data-descadastro`

- **Onde:** cada linha da aba Descadastros do Mail Marketing (`.custom-css-mail-marketing-descadastros`)
- **Valores:** o número do descadastro

### `data-desligado`

- **Onde:** o aviso do agente desligado na janela do prompt (`.custom-css-prompt-agente-desligado`)
- **Valores:** `assistants` (a API de agentes da OpenAI, desligada)

### `data-destaque`

- **Onde:** cada linha do ranking de agentes no Dashboard (`.custom-css-dashboard-ranking-linha`)
- **Valores:** `true` quando as mensagens ou o custo por atendimento passam de 1,5 vez a média do time (com ao menos 5 atendimentos) · `false`

### `data-dia`

- **Onde:** coluna do gráfico de logs do Pixel; e cada dia do calendário de Agendamentos (`.custom-css-agenda-dia`)
- **Valores:** a data daquele dia (`YYYY-MM-DD` no calendário)

### `data-dia`

- **Onde:** cada dia da lista de espera na agenda das Reservas (`.custom-css-reservas-agenda-espera-dia`)
- **Valores:** o dia, no formato `AAAA-MM-DD`

### `data-dia`

- **Onde:** cada dia da página pública das reservas (`.custom-css-reservas-publica-dia`)
- **Valores:** o dia (`AAAA-MM-DD`, no fuso da empresa)

### `data-dia`

- **Onde:** cada coluna da agenda das reservas na semana (`.custom-css-reservas-agenda-coluna`)
- **Valores:** o dia da coluna (`AAAA-MM-DD`, no fuso da empresa)

### `data-dia`

- **Onde:** cada dia da grade de horários das Reservas (`.custom-css-reservas-horarios-dia`)
- **Valores:** o dia da semana: `0` domingo, `1` segunda ... `6` sábado

### `data-dia`

- **Onde:** a agenda dos Serviços (`.custom-css-servicos-agenda`) e cada dia nos horários de atendimento (`.custom-css-servicos-agenda-dia`)
- **Valores:** na agenda, a data `YYYY-MM-DD`; nos horários, o dia da semana de `0` (domingo) a `6` (sábado)

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

### `data-edicao-lugar`

- **Onde:** a caixa do texto de antes da edição (`.custom-css-edicao-versoes`)
- **Valores:** `atendimento` (a conversa com o cliente) · `chat` (o chat interno)

### `data-edicao-versao`

- **Onde:** cada versão de antes da edição (`.custom-css-edicao-versao`)
- **Valores:** `1` (o texto original), `2`, `3`… na ordem das edições

### `data-editando`

- **Onde:** o formulário da janela de Campanhas (`.custom-css-gamificacao-campanha-form`)
- **Valores:** `true` quando o formulário está mudando uma campanha que já existe · `false` quando está criando uma nova

### `data-editavel`

- **Onde:** o quadro das peças e serviços da ordem (`.custom-css-servicos-ordem-itens`)
- **Valores:** `true` ainda dá para mudar os itens · `false` a ordem já passou da execução

### `data-edited`

- **Onde:** balão da mensagem
- **Valores:** `contact` quando o contato editou (a mensagem nova, com o marcador) · `user` quando a empresa editou (a própria mensagem já tem o texto novo, com o `.message-edited` ao lado da hora)

### `data-elapsed-late`

- **Onde:** tempo relativo no cartão do ticket
- **Valores:** `true` · `false` — a regra simples de "está atrasado", para o CSS não precisar listar quais estados contam como atraso

### `data-elapsed-status`

- **Onde:** tempo relativo no cartão do ticket
- **Valores:** `fresh` (até 30 min) · `warning` (até 60) · `late` (acima). Vem junto do `data-elapsed-late`, que é o mesmo em forma de sim/não

### `data-em-execucao`

- **Onde:** o Iniciar/Pausar/Finalizar de cada tarefa, na lista de Tarefas e dentro da tarefa (`.custom-css-tarefa-execucao`)
- **Valores:** `minha` (você está executando esta tarefa agora) · `de-outro` (outra pessoa está) · `nao` (ninguém está)

### `data-em-outra-regra`

- **Onde:** a categoria já usada por outra regra, na lista de categorias de uma regra do cashback
- **Valores:** a posição da regra que já usa a categoria (a opção fica desabilitada)

### `data-em-uso`

- **Onde:** o aviso de prompt em uso na confirmação de apagar (`.custom-css-prompt-excluir-em-uso`)
- **Valores:** `setores` (os setores que usam o prompt) ou `atendimentos` (os atendimentos abertos com ele)

### `data-email-account`

- **Onde:** campos e botões do modal de conta de e-mail
- **Valores:** `carregar-pastas` · `nova-pasta` · `novo-endereco`

### `data-email-id`

- **Onde:** cada e-mail da lista da página E-mails (`.custom-css-emails-item`)
- **Valores:** o id do e-mail — com `.custom-css-emails-item-marcado` quando ele está selecionado para a ação em massa

### `data-email-isolado`

- **Onde:** o quadro do corpo do e-mail (`.custom-css-emails-corpo`)
- **Valores:** sempre `true`: o conteúdo mora num iframe isolado — o CSS da empresa estiliza o quadro (borda, altura mínima), não o e-mail

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

### `data-encaixe`

- **Onde:** a janela da chamada (`.custom-css-chamada`) e o contorno que mostra onde ela vai encaixar (`.custom-css-chamada-previa-do-encaixe`)
- **Valores:** `tudo` (maximizada) · `esquerda` · `direita` (a metade da tela); sem o atributo, a janela solta. A janela encaixada leva também as classes `.custom-css-chamada-encaixada` e `.custom-css-chamada-encaixada-tudo`, `-esquerda` ou `-direita`

### `data-encontrado`

- **Onde:** o cartão do #protocolo (`.custom-css-chats-protocolo`)
- **Valores:** `true` — o atendimento existe (o cartão mostra o contato e tem o olho de espiar) · `false` — nenhum atendimento da empresa com esse protocolo

### `data-endereco`

- **Onde:** pílula de endereço aceito no modal de conta de e-mail
- **Valores:** o endereço que a conta aceita (recebidos pelo destinatário, enviados pelo remetente)

### `data-entidade`

- **Onde:** cada tabela de resposta do Assistente de IA (`.custom-css-assistente-tabela`)
- **Valores:** `atendimentos` · `contatos` · `oportunidades` · `tarefas`

### `data-entregador-id`

- **Onde:** a regra própria de um entregador (`.custom-css-comissao-do-entregador-propria`) e a linha dele no Relatório do PDV (`.custom-css-relatorio-pdv-comissao-entregador-linha`)
- **Valores:** o id do usuário entregador (vazio enquanto não escolhido)

### `data-enviado`

- **Onde:** o que aconteceu com cada aviso ao cliente na janela da tarefa (`.custom-css-tarefa-aviso-situacao`)
- **Valores:** `true` (o aviso saiu) · `false` (não saiu; o motivo aparece no texto)

### `data-enviado`

- **Onde:** o link de pagamento recém-gerado da ordem de serviço (`.custom-css-servicos-cobranca-gerada`)
- **Valores:** `true` foi ao cliente pelo WhatsApp · `false` não foi (só copiar)

### `data-envio`

- **Onde:** cada e-mail na tabela do relatório da campanha do Mail Marketing (`.custom-css-mail-marketing-envios`)
- **Valores:** o número do envio

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

### `data-escolhida`

- **Onde:** cada post ou story na escolha do gatilho da automação do Instagram (`.custom-css-ig-automacao-midias`)
- **Valores:** `true` o escolhido · `false` os outros

### `data-escopo`

- **Onde:** cada escopo da chave nova na aba Integrações do Consultório (`.custom-css-consultorio-chaves-escopo`)
- **Valores:** `atendente` as ações do paciente · `clinica` tudo, sem pedir o contato · `pacientes` a ficha do paciente

### `data-escopo`

- **Onde:** bloco de conexão do Google Calendar
- **Valores:** `operador` (cada um conecta a própria agenda) · `empresa` (uma conta para todos)

### `data-escopo`

- **Onde:** o cancelar da reserva de uma série (`.custom-css-reservas-cancelar-escopo`)
- **Valores:** `esta` só ela · `proximas` ela e as seguintes · `todas` a série toda

### `data-escuta`

- **Onde:** o áudio escondido de quem fala na chamada espiada (o `<audio>` que o Espiar das Gravações põe na página)
- **Valores:** `sim`

### `data-estado`

- **Onde:** raiz da página de documentação da API (`#custom-css-documentacao-api`, a rota `/api-docs`) e da página das classes (`#custom-css-documentacao-css`, a rota `/css-docs`), cada etapa do indicador do encerramento em 3 passos (`.custom-css-encerramento-etapa`) e o cartão de PDF do chat interno (`.custom-css-chat-pdf`); e cada bolinha do Adicionar das Respostas Rápidas (`.custom-css-quick-message-etapa`)
- **Valores:** na documentação da API: `carregando` (o Swagger UI ainda não subiu) · `pronto` · `erro` (os arquivos de `/swagger-ui/` não carregaram). Na página das classes: `carregando` · `pronto` · `erro` (o catálogo do idioma não carregou). Na etapa do encerramento: `ativa` · `feita` · `pendente` · `pulada` (a etapa Valor, quando a tag escolhida não pede valor). No cartão de PDF: `carregando` (ainda sem a primeira página — também enquanto o balão não apareceu na tela) · `pronto` (a primeira página está no cartão) · `erro` (PDF com senha, corrompido ou fora do ar: fica o símbolo do PDF, e o clique continua baixando). Na bolinha das Respostas Rápidas: `ativa` · `feita` · `pendente`, como no encerramento

### `data-estoque-baixo`

- **Onde:** cada peça ou serviço do catálogo dos Serviços (`.custom-css-servicos-item`)
- **Valores:** `true` a peça chegou ao estoque mínimo · `false` não

### `data-estornado`

- **Onde:** cada pagamento da ordem de serviço (`.custom-css-servicos-ordem-pagamento`)
- **Valores:** `true` o pagamento foi estornado (não conta mais) · `false`

### `data-estorno`

- **Onde:** cada linha do extrato de Minha Evolução (`.custom-css-minha-evolucao-movimento`)
- **Valores:** `true` na linha de estorno: a venda deixou de contar e devolveu os pontos que tinha rendido (os pontos vêm negativos) · `false` no lançamento comum

### `data-etapa`

- **Onde:** janela do encerramento em 3 passos (`.custom-css-modal-encerramento`), cada etapa do indicador (`.custom-css-encerramento-etapa`) e cada etapa do Criar Template (`.custom-css-waba-template-form-etapa`); e cada bolinha do Adicionar das Respostas Rápidas (`.custom-css-quick-message-etapa`); na Avaliação pela IA, cada linha de Onde o time perde (`[data-ranking="etapa"]`) e cada etapa de uma avaliação (`.custom-css-avaliacao-ia-etapa-avaliada`)
- **Valores:** na janela, a tela aberta: `motivo` · `valor` · `confirmar` · `encerrado` (a tela de sucesso). Na etapa do indicador, o nome dela: `motivo` · `valor` · `confirmar` — o estado vai em `data-estado`. No Criar Template: `configurar` · `editar` · `enviar`, e a aberta leva `aria-current="step"`. Nas Respostas Rápidas: `tipo` (escolher Texto ou Arquivo) · `conteudo` (o formulário) — o estado vai em `data-estado`. Na Avaliação pela IA: o nome da etapa do processo ideal da empresa

### `data-etapa`

- **Onde:** cada coluna do quadro na página do projeto (`.custom-css-projeto-coluna`)
- **Valores:** o id da etapa

### `data-etapa`

- **Onde:** cada data na ficha da ordem de serviço (`.custom-css-servicos-ordem-datas`)
- **Valores:** `entradaEm` · `orcadoEm` · `aprovadoEm` · `recusadoEm` · `iniciadoEm` · `concluidoEm` · `entregueEm` · `canceladoEm` · `pagoEm`

### `data-etapa`

- **Onde:** a janela do link de pagamento da ordem de serviço (`.custom-css-modal-servicos-cobranca`)
- **Valores:** `escolha` (a conta e o envio) · `gerado` (o link pronto)

### `data-eventos`

- **Onde:** a lista de eventos do webhook na aba Configurações do Mail Marketing (`.custom-css-mail-marketing-configuracoes`)
- **Valores:** `mail-marketing`

### `data-excedente`

- **Onde:** linha da empresa na conciliação de conexões
- **Valores:** `true` quando ela usa mais conexões do que o plano permite

### `data-exemplo`

- **Onde:** o exemplo real dentro de uma aula da IA (`.custom-css-avaliacao-ia-aula`)
- **Valores:** o id da aula

### `data-exemplo-do-lote`

- **Onde:** a frase "Vai criar de … até …" da configuração das mesas e comandas (`.custom-css-comandas-configurar`)
- **Valores:** sem valor: só marca a frase (ela some quando os números não valem)

### `data-externo`

- **Onde:** cada horário bloqueado na agenda das reservas (`.custom-css-reservas-agenda-bloqueio`)
- **Valores:** `sim` (compromisso da agenda do Google do recurso) · `nao` (bloqueio feito aqui)

### `data-extrato`

- **Onde:** cada linha do extrato do cashback na página Clientes do PDV (`.custom-css-clientes-pdv-cashback`)
- **Valores:** `credito` · `uso` · `estorno` (o saldo devolvido) · `anulado` (o crédito do pedido cancelado) · `expirado`

### `data-faixa`

- **Onde:** a etiqueta da nota de um atendimento avaliado pela IA (junto do `data-nota`)
- **Valores:** `promotor` (9-10) · `neutro` (7-8) · `detrator` (0-6)

### `data-falta`

- **Onde:** cada produto da aba Vendas perdidas da Avaliação pela IA (`.custom-css-avaliacao-ia-falta`)
- **Valores:** o nome do produto sem acento, minúsculas e pontuação (o mesmo produto escrito de jeitos diferentes conta junto)

### `data-falta`

- **Onde:** o aviso do que falta escolher na janela Comandos da IA (`.custom-css-comandos-ia-falta`)
- **Valores:** `fila` (o setor), `usuario` (a pessoa) ou `tag`

### `data-faltando`

- **Onde:** o aviso do que falta para agendar, na janela da campanha do Mail Marketing (`.custom-css-modal-mail-marketing-campanha`)
- **Valores:** o que falta, separado por espaço: `conta`, `modelo`, `assunto`, `listas`

### `data-faltas`

- **Onde:** o modelo da API oficial no lembrete e na confirmação do Consultório (`.custom-css-consultorio-modelo`)
- **Valores:** o que falta para o modelo sair, separado por espaço: `modelo` · `variaveis` · `botoes` · `cabecalho` — ou `nenhuma`

### `data-fase`

- **Onde:** a janela do Espiar das Gravações (`.custom-css-gravacoes-espiar`)
- **Valores:** `conectando` · `ouvindo` · `encerrada` · `falhou`

### `data-favorita`

- **Onde:** estrela da mensagem rápida, na tela de Mensagens Rápidas
- **Valores:** `true` · `false` — se aquela mensagem está favoritada

### `data-favorita-id`

- **Onde:** item da lista de mensagens rápidas favoritas, no campo de digitação do HUB
- **Valores:** o id da mensagem rápida daquele item

### `data-favorite`

- **Onde:** cartão do ticket e a estrela dele; e o botão de favoritar de cada conversa do Chat Interno (`[data-action="favorite"]`)
- **Valores:** `true` · `false`

### `data-favorito-novo`

- **Onde:** o item da seção Favoritos do menu (`.custom-css-menu-favorito-novo`)
- **Valores:** `true` nos primeiros instantes depois de a página virar favorita; some sozinho

### `data-feito`

- **Onde:** cada item do checklist na página do convidado (`.custom-css-convidado-checklist-item`)
- **Valores:** `true` (feito) · `false`

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

### `data-filtros`

- **Onde:** a linha dos filtros em uso na janela "Mensagem a todos os atendimentos" do Quadro (`.custom-css-quadro-disparo-filtros`)
- **Valores:** quantos filtros da barra estão valendo (`1` em diante; sem filtro, a linha não aparece)

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

### `data-forma`

- **Onde:** cada forma de pagamento nas opções do desconto e da taxa por forma (`.custom-css-ajuste-da-forma`)
- **Valores:** `dinheiro` · `pix` · `cartao` · `boleto` · `outro`

### `data-forma`

- **Onde:** cada pagamento da reserva, o link gerado e cada forma de pagar na página pública (`.custom-css-reservas-reserva-pagamento-linha`, `.custom-css-reservas-reserva-pagamento-link`, `.custom-css-reservas-publica-sinal-forma`)
- **Valores:** `dinheiro` · `pix` · `cartao` · `boleto` · `outro` · `asaas` · `mercadopago` · `pagseguro` · `paggpix`

### `data-forma`

- **Onde:** a conta do link de pagamento da ordem de serviço (`.custom-css-servicos-cobranca-conta`, `.custom-css-servicos-cobranca-gerada`, `.custom-css-servicos-ordem-cobranca`, `.custom-css-servicos-publica-pagamento`)
- **Valores:** `asaas` · `mercadopago` · `pagseguro` · `paggpix`

### `data-frequencia`

- **Onde:** a marca da série no detalhe da reserva (`.custom-css-reservas-reserva-serie`)
- **Valores:** `diaria` · `semanal` · `quinzenal` · `mensal`

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

### `data-gateway`

- **Onde:** cada conta da lista "Link de pagamento depois de confirmar", na seção da IA que vende pelo PDV, em Configurações → Opções → Automação (`.custom-css-opcao-ia-link-de-pagamento`)
- **Valores:** `asaas` · `mercadopago` · `pagseguro` · `paggpix`

### `data-gerenciar-grupos`

- **Onde:** botão de gerenciar grupos de template, no cabeçalho de /waba-templates
- **Valores:** sem valor — marca o botão que abre o gerenciador

### `data-google-analytics`

- **Onde:** o script do Google Analytics (GA4) que as páginas públicas carregam (cardápio, loja, bio, reservas, agendamento, rastreio)
- **Valores:** sempre `script` — serve para achar ou esconder o script do Analytics

### `data-grafico`

- **Onde:** cada gráfico da página Avaliação pela IA (`.custom-css-page-avaliacao-ia`)
- **Valores:** `distribuicao` (as notas de 0 a 10) · `evolucao` (os dias do período) · `evolucao-semanal` (a tabela da aba Evolução, semana a semana)

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

- **Onde:** os títulos dos grupos e as ações do menu Mais agrupado (`.custom-css-ticket-actions-grupo`, `.custom-css-ticket-actions-item`)
- **Valores:** `atendimento` · `comunicacao` · `ia` · `organizacao` · `outras`

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

### `data-guia-mcp-acesso`

- **Onde:** cada tipo de acesso explicado no Guia do MCP (`.custom-css-guia-mcp-acesso`)
- **Valores:** `leitura` · `acao` · `plataforma` (só para o operador da plataforma)

### `data-guia-mcp-evento`

- **Onde:** cada aviso do webhook listado no Guia do MCP (`.custom-css-guia-mcp-evento`)
- **Valores:** o nome do evento que chega no webhook (`token-criado`, `acao-executada`…)

### `data-guia-mcp-ferramenta`

- **Onde:** cada ferramenta listada no Guia do MCP (`.custom-css-guia-mcp-ferramenta`)
- **Valores:** o nome da ferramenta no servidor (`buscar_atendimentos`, `enviar_mensagem`…)

### `data-guia-mcp-grupo`

- **Onde:** cada grupo de ferramentas no Guia do MCP (`.custom-css-guia-mcp-grupo`)
- **Valores:** `leitura` · `acao` · `plataforma` (só para o operador da plataforma)

### `data-guia-mcp-secao`

- **Onde:** cada seção da página Guia do MCP (`.custom-css-guia-mcp-secao`)
- **Valores:** `conectar` · `acessos` · `ferramentas` · `exemplos` · `fora` · `seguranca`

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

### `data-hora`

- **Onde:** cada horário livre da página pública das reservas (`.custom-css-reservas-publica-horario`)
- **Valores:** a hora do início no fuso da empresa (`HH:MM`)

### `data-hora`

- **Onde:** cada horário livre da janela da reserva (`.custom-css-reservas-reserva-horario`)
- **Valores:** a hora do início no fuso da empresa (`HH:MM`)

### `data-hora`

- **Onde:** cada horário livre para clicar (`.custom-css-servicos-agendamento-livre`, `.custom-css-servicos-agenda-publica-horario`)
- **Valores:** a hora, `HH:mm`

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

### `data-item`

- **Onde:** cada linha do resumo do Monte seu plano (`.custom-css-monte-seu-plano-item`) e do plano montado na página de cadastro (`.custom-css-signup-plano-montado-item`)
- **Valores:** `base` · `usuarios` · `conexoes` · `setores` · `implantacao`, ou a chave do módulo (`usePDV`...)

### `data-item-id`

- **Onde:** cada item de uma rodada (`.custom-css-salao-da-mesa-item`) e cada item tirado (`.custom-css-salao-da-mesa-tirado`) na janela da conta da mesa
- **Valores:** o id do item na rodada; no tirado, o id do registro do cancelamento

### `data-lane-type`

- **Onde:** raia do funil; e o cartão da tela de Oportunidades (`.custom-css-oportunidade-card`)
- **Valores:** `IN_PROGRESS` · `WON` · `LOST`. No cartão de Oportunidades, só com o CRM v2 — o v1 não traz a raia, e o cartão fica sem o atributo

### `data-largura`

- **Onde:** a prévia do editor do modelo do Mail Marketing (`.custom-css-mail-marketing-previa`)
- **Valores:** `computador` ou `celular`

### `data-ligada`

- **Onde:** o cartão da automação do Instagram (`.custom-css-ig-automacao-card`)
- **Valores:** `true` ligada · `false` desligada

### `data-ligada`

- **Onde:** a opção da despedida obrigatória em Configurações → Opções (`.custom-css-opcao-despedida-obrigatoria`)
- **Valores:** `sim` com a despedida obrigatória · `nao` sem

### `data-ligada`

- **Onde:** a repetição no agendar da reserva (`.custom-css-reservas-reserva-repetir`)
- **Valores:** `1` repetindo · `0` sem repetir

### `data-ligado`

- **Onde:** o contato do WhatsApp na ficha do paciente do Consultório (`.custom-css-consultorio-paciente-contato`)
- **Valores:** `true` com o contato ligado · `false` sem contato (ao salvar, o telefone o acha ou o cria)

### `data-limite`

- **Onde:** o campo Texto do botão do Criar Template (WABA)
- **Valores:** quantos caracteres o texto do botão aceita (`25`, o limite da Meta)

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

### `data-livre`

- **Onde:** cada noite do calendário da diária na página pública (`.custom-css-reservas-publica-noite`)
- **Valores:** `1` (há quem atenda naquela noite) · `0` (ocupada, bloqueada ou fora do prazo)

### `data-livre`

- **Onde:** cada data da prévia da série (`.custom-css-reservas-serie-data`)
- **Valores:** `1` livre · `0` não serve

### `data-livres`

- **Onde:** a prévia da série (`.custom-css-reservas-serie-datas`)
- **Valores:** quantas datas estão livres

### `data-local`

- **Onde:** cada local no filtro "Onde você prefere?" da página pública do link de agendamento (`.custom-css-agendar-publico-locais`)
- **Valores:** o id do local cadastrado no link (8 letras e números); o chip "Todos os locais" não tem o atributo

### `data-lugar`

- **Onde:** pódio de vendas
- **Valores:** `1` · `2` · `3`

### `data-mais-recente`

- **Onde:** cada versão da gaveta de Versões do editor de fluxo (`.custom-css-flow-versao`)
- **Valores:** `true` na primeira, a mais recente · `false` nas outras

### `data-marca-da-ficha`

- **Onde:** a marca no cartão do produto (`.custom-css-product-card-marca`)
- **Valores:** `true` quando a marca vem da linha "Marca" da ficha técnica (o campo Marca está vazio); `false` quando é a do campo

### `data-marcado`

- **Onde:** cada convênio no cadastro do profissional do Consultório (`.custom-css-consultorio-profissional-convenio`)
- **Valores:** `sim` (o profissional aceita o convênio) · `nao`

### `data-marcados`

- **Onde:** a barra de seleção acima da lista da página E-mails (`.custom-css-emails-selecao`)
- **Valores:** quantos e-mails estão selecionados (`0` sem nenhum) — dá para destacar a barra só quando há seleção

### `data-mcp-dia`

- **Onde:** cada dia da semana nos limites do token do MCP (`.custom-css-mcp-limites-dias`)
- **Valores:** `0` (domingo) a `6` (sábado)

### `data-mcp-externo-ativo`

- **Onde:** cada servidor MCP da empresa na seção do MCP (`.custom-css-mcp-externo-servidor`)
- **Valores:** `true` · `false`

### `data-mcp-token-novo`

- **Onde:** o quadro do token do MCP recém-gerado, em Configurações → Opções → Integrações e segurança (`.custom-css-mcp-token-novo`)
- **Valores:** `true` (o token aparece só agora, uma vez; some ao clicar em "Já copiei")

### `data-mcp-token-revogado`

- **Onde:** cada linha da lista de tokens do MCP (`.custom-css-mcp-token`)
- **Valores:** `true` (o token foi revogado e não vale mais) · `false` (ativo)

### `data-media`

- **Onde:** a média da semana dentro de cada célula da Evolução da Avaliação pela IA (`[data-semana]`), na cor da faixa da nota
- **Valores:** a média, com uma casa decimal

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

### `data-mensagem`

- **Onde:** a linha que diz se o cliente recebe a mensagem, na janela do cancelamento do Painel de Pedidos (`.custom-css-cancelar-pedido-cliente`)
- **Valores:** `sim` (pedido de entrega ou retirada: sai o aviso "Pedido cancelado", se estiver ligado) · `nao` (pedido de mesa ou comanda)

### `data-mensagens`

- **Onde:** cada célula do mapa de calor do atendente, na linha aberta do ranking (`.custom-css-dashboard-atendente-mapa-celula`)
- **Valores:** quantas mensagens ele enviou naquele dia e hora

### `data-menu`

- **Onde:** item do menu lateral
- **Valores:** o identificador do item

### `data-menu-action`

- **Onde:** cada item dos menus das páginas (`.custom-css-page-menu`) e dos menus da barra do topo
- **Valores:** no "Ações" de Conexões (`.custom-css-menu-conexoes-acoes`): `migrar` · `adicionar-whatsapp` · `adicionar-sem-aparelho` · `adicionar-webchat` · `adicionar-chat-externo` · `adicionar-oficial` · `adicionar-oficial-portal` · `adicionar-telegram` · `adicionar-facebook` · `adicionar-facebook-portal` · `adicionar-instagram` · `adicionar-instagram-portal` · `adicionar-tiktok` · `adicionar-rcs` · `adicionar-hub` · `fechar-removidas` · `fechar-todos` · `encerrar-com-filtros` · `reiniciar`. No ⋮ de cada fluxo (`.custom-css-menu-fluxo-acoes`): `editar-nome` · `editar-fluxo` · `exportar` · `duplicar` · `logs` · `excluir`. No Importar/Exportar de Contatos (`.custom-css-menu-contatos-importar-exportar`): `importar-agenda` · `importar-arquivo` · `exportar`. No ⋮ da linha de Contatos, no celular (`.custom-css-menu-contato-acoes`): `resumo` · `iniciar-conversa` · `editar` · `excluir`. No menu da mensagem do Chat Interno: `copiar` · `reagir` · `marcar-visto` / `desmarcar-visto` (o que o clique FAZ, conforme a mensagem já está marcada) · `apagar`. No "Recebe saltos de N" do editor de fluxo (`.custom-css-menu-saltos-do-fluxo`): `ir-para-origem`. No Ordenar da lista de atendimentos (`.custom-css-menu-ordenar-atendimentos`): `newest` (mais recentes primeiro) · `oldest` (mais antigos primeiro), com `role="menuitemradio"` e o escolhido em `aria-checked`. Na barra do topo: no menu da conta (`.custom-css-menu-usuario`), `perfil` · `trocar-senha` · `2fa` (só com o 2FA da empresa ligado) · `sair` · `versao`; no menu do status (`.custom-css-menu-status`), `online` · `away` · `offline`; no menu do idioma (`.custom-css-menu-idioma`), o código do idioma — `pt` · `pt-PT` · `es` · `en` · `de` · `fr`. Nos dois últimos, `role="menuitemradio"` e o atual em `aria-checked`. Os itens que só aparecem com o módulo no plano somem do DOM junto com o módulo No menu de status e sessão do cartão da tela de Usuários (`.custom-css-user-menu-presenca`): `online` · `away` · `offline` · `derrubar-sessao` (só para outra pessoa, com a confirmação `.custom-css-modal-confirmation-usuario-derrubar-sessao`). No "Ações" de Conexões, com o WhatsApp Gupshup no plano: `adicionar-gupshup`.

### `data-menu-busca`

- **Onde:** a caixa da busca no topo do menu lateral (`.custom-css-menu-busca`), só com o menu aberto
- **Valores:** `vazia` · `ativa` (com texto: o menu dá lugar aos resultados em `.custom-css-menu-busca-resultados`)

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

### `data-meus-numeros`

- **Onde:** cada número da página Meus números (`.custom-css-meus-numeros-numero`), os do próprio atendente
- **Valores:** `encerrados` · `primeira-resposta` · `resolucao` · `avaliacao` · `avaliacao-ia` (só quando há atendimentos avaliados pela IA)

### `data-meus-numeros-periodo`

- **Onde:** cada período da página Meus números (os botões acima dos números)
- **Valores:** `hoje` · `semana` (os últimos 7 dias) · `trinta` (os últimos 30 dias) · `esteMes`

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

### `data-modelo`

- **Onde:** a opção "Modelo do provedor" na escolha do modelo do prompt (`.custom-css-prompt-modelo-do-provedor`)
- **Valores:** o nome do modelo que o provedor usa (ex.: `llama-3.3-70b-versatile`); vazio sem IA configurada

### `data-modelo`

- **Onde:** o modelo da API oficial no lembrete e na confirmação do Consultório (`.custom-css-consultorio-modelo`)
- **Valores:** `sim` usa um modelo aprovado · `nao` só o texto

### `data-modo`

- **Onde:** o botão que troca os comentários entre aba e lateral direita (`.custom-css-comentarios-modo`, na tarefa, na oportunidade e no projeto)
- **Valores:** a escolha da pessoa: `aba` (o padrão) · `lateral`. O botão some na tela estreita, onde é sempre aba

### `data-modo`

- **Onde:** a duração de cada oferta na lista de ofertas (`.custom-css-reservas-oferta`)
- **Valores:** `horario` · `diaria`

### `data-modo`

- **Onde:** a janela de marcar ou remarcar um horário (`.custom-css-modal-servicos-agendamento`)
- **Valores:** `criar` · `editar`

### `data-modo`

- **Onde:** a linha de um usuário em "Quem vê qual agenda" do Consultório (`.custom-css-consultorio-acesso`)
- **Valores:** `todas` · `minha` (só a do profissional ligado ao usuário) · `estas` (os profissionais escolhidos) · `nenhuma`

### `data-modo`

- **Onde:** a janela do motivo do Painel de Pedidos (`.custom-css-modal-cancelar-pedido-do-painel`)
- **Valores:** `cancelar` (o Cancelar pedido) · `recusar` (o Recusar, do pedido em Novo)

### `data-modo-tv`

- **Onde:** a página do Dashboard (`#custom-css-dashboard`) no Modo TV (tela cheia, os painéis em rodízio)
- **Valores:** `ligado` (no Modo TV; fora dele, o atributo não aparece)

### `data-modulo`

- **Onde:** o Monte seu plano: cada módulo à venda na página pública (`.custom-css-monte-seu-plano-modulo`) e na tabela da tela de planos (`.custom-css-planos-monte-modulo`)
- **Valores:** a chave do módulo no plano (`useCampaigns`, `useKanban`, `usePDV`...)

### `data-momento`

- **Onde:** cada mensagem da janela Avisos ao cliente das Tarefas (`.custom-css-avisos-da-tarefa-momento`) e o que aconteceu com cada aviso na janela da tarefa (`.custom-css-tarefa-aviso-situacao`)
- **Valores:** `criacao` (o aviso de quando a tarefa é criada) · `lembrete` (o aviso antes do horário)

### `data-monitoravel`

- **Onde:** pílula de canal no monitor AMQP
- **Valores:** `true` no canal que passa por fila e portanto pode aparecer no monitor

### `data-mostra-encerrar`

- **Onde:** botão que liga e desliga o encerrar nos cards, na barra do quadro de atendimentos
- **Valores:** `true` · `false`

### `data-motivo`

- **Onde:** linha do histórico de remarketing; e cada linha do extrato de Minha Evolução (`.custom-css-minha-evolucao-movimento`); e cada motivo de quem precisa de você, na aba Hoje da Avaliação pela IA (dentro de `.custom-css-avaliacao-ia-precisa`)
- **Valores:** no remarketing, o motivo do registro. No extrato, o que rendeu o ponto: `venda` (venda fechada) · `valor` (valor vendido) · `meta` (meta do mês batida) · `funil` (venda no funil de uma regra) · `etiqueta` (venda com a etiqueta de uma regra) · `encerramento` (encerramento com venda) · `manual` — no estorno, o do lançamento que ele desfaz. Na aba Hoje: `nota-baixa` · `aderencia-baixa` · `caiu` · `saiu-do-processo`

### `data-motivo`

- **Onde:** a seção da agenda do Google na janela do recurso das reservas (`.custom-css-reservas-recurso-agenda-google`)
- **Valores:** por que a agenda não alcança o recurso: `sem-credencial` · `sem-usuario` · `sem-conta`; vazio quando alcança

### `data-motivo`

- **Onde:** o aviso de que o orçamento não pode ser aprovado pela página da ordem (`.custom-css-servicos-publica-sem-aprovacao`)
- **Valores:** `ERR_SERVICOS_APROVACAO_PELO_LINK_DESLIGADA` (a empresa aprova direto) · `ERR_SERVICOS_ORCAMENTO_VENCIDO` (passou da validade)

### `data-motivo`

- **Onde:** cada motivo da janela do cancelamento do Painel de Pedidos (`.custom-css-cancelar-pedido-motivo`)
- **Valores:** `clienteDesistiu` · `enderecoNaoAtendido` · `produtoEmFalta` · `pedidoDuplicado` · `outro` (abre o campo para escrever, `.custom-css-cancelar-pedido-outro`)

### `data-motivo`

- **Onde:** o motivo da falha de cada envio no relatório do Mail Marketing (`.custom-css-mail-marketing-motivo`), já na língua de quem usa (o texto técnico fica no passar do mouse)
- **Valores:** `servidor` (servidor de envio não encontrado) · `conexao` (sem conexão com o servidor) · `autenticacao` (usuário ou senha recusados) · `seguranca` (SSL/TLS) · `limite` (o servidor limitou os envios) · `destinatario` (endereço recusado) · `descadastrado` · `cancelada` · `interrompido` · `outro` (o texto do servidor como veio)

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

### `data-noites`

- **Onde:** o resumo da estadia (`.custom-css-reservas-publica-estadia`, `.custom-css-reservas-reserva-estadia`) e o cartão da diária na agenda (`.custom-css-reservas-agenda-reserva`)
- **Valores:** o número de noites da estadia (`1`, `2`, `3`...)

### `data-nota`

- **Onde:** a etiqueta da nota de um atendimento avaliado pela IA
- **Valores:** a nota, de `0` a `10`

### `data-nota-id`

- **Onde:** bloco de nota interna do atendimento
- **Valores:** o id da nota

### `data-notification-action`

- **Onde:** faixa de permissão de notificação
- **Valores:** `enable` · `dismiss`

### `data-nova`

- **Onde:** a janela da ordem de serviço (`.custom-css-modal-servicos-ordem`)
- **Valores:** `true` abrindo uma ordem nova · `false` editando uma que existe

### `data-novo`

- **Onde:** o aviso do rascunho no editor do fluxo (`.custom-css-flowbuilder-rascunho`), quando o assistente deixou um rascunho
- **Valores:** `true` no fluxo que o assistente criou (inativo, o desenho já está no editor) · `false` no ajuste de um fluxo em uso (o botão Abrir o rascunho aparece)

### `data-novo-grupo`

- **Onde:** campo de nome no gerenciador de grupos de template
- **Valores:** sem valor — marca o campo de criar grupo

### `data-numero`

- **Onde:** o número da empresa que recebe a ligação, no pop-up do ramal (`.custom-css-sip-numero-que-recebe`)
- **Valores:** o número que a central informou no convite (só aparece quando ela informa)

### `data-numero`

- **Onde:** cada número do relatório das reservas (`.custom-css-reservas-relatorio-numero`)
- **Valores:** `reservas` · `pessoas` · `comparecimento` · `cancelamento` · `previsto` · `recebido` · `aReceber` · `ticketMedio`

### `data-ocupacao`

- **Onde:** cada recurso no relatório das reservas (`.custom-css-reservas-relatorio-recurso`)
- **Valores:** a ocupação de 0 a 1 (`0.5` é metade); vazio sem grade no período

### `data-ocupadas`

- **Onde:** a prévia da série (`.custom-css-reservas-serie-datas`)
- **Valores:** quantas datas não servem

### `data-oferta`

- **Onde:** cada oferta da página pública das reservas (`.custom-css-reservas-publica-oferta`)
- **Valores:** o id da oferta

### `data-on-hold`

- **Onde:** a janela da chamada e o widget minimizado
- **Valores:** `true` · `false` — a chamada em espera

### `data-online`

- **Onde:** o avatar do atendente no cabeçalho da coluna, na visão Atendentes do Quadro de Atendimentos (`.custom-css-quadro-coluna-atendente`)
- **Valores:** `true` está online agora · `false` fora do ar

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

### `data-origem`

- **Onde:** a marca da reserva feita pela página no detalhe da agenda (`.custom-css-reservas-reserva-origem`)
- **Valores:** `pagina`

### `data-origem`

- **Onde:** cada horário na agenda dos Serviços (`.custom-css-servicos-agendamento`)
- **Valores:** `painel` · `pagina` · `api`

### `data-origem`

- **Onde:** a mensagem do chat interno (`.custom-css-chats-msg`)
- **Valores:** `sistema` na mensagem que o sistema escreve (a gravação, a transcrição e a análise da chamada), que ganha o balão `.custom-css-chats-msg-sistema`; sem o atributo nas outras

### `data-origem-do-envio`

- **Onde:** balão da mensagem da empresa (`.custom-css-msg-bubble`) e a marca `.custom-css-mensagem-enviada-automaticamente`
- **Valores:** `painel` · `celular` · `api` · `flowbuilder` · `chatbot` · `campanha` · `agendamento` · `ia` · `sistema` (o aviso que a plataforma manda sozinha); sem o atributo nas mensagens antigas

### `data-origin`

- **Onde:** balão da mensagem
- **Valores:** `contact` · `user` (operador) · `app` (celular pareado) · `api` (API) · `auto` (a plataforma, sozinha)

### `data-outro-mes`

- **Onde:** o mesmo dia
- **Valores:** `true` nos dias do mês anterior ou do seguinte, que completam as semanas da grade · `false`

### `data-pacote`

- **Onde:** a marca do pacote no detalhe da reserva (`.custom-css-reservas-reserva-pacote-usado`)
- **Valores:** o número do pacote do cliente que a reserva usou (`1`, `2`, `3`...)

### `data-padrao`

- **Onde:** a linha de um usuário em "Quem vê qual agenda" do Consultório (`.custom-css-consultorio-acesso`)
- **Valores:** `sim` (ainda sem escolha do administrador: vale o padrão) · `nao`

### `data-pagamento`

- **Onde:** o quadro dos pagamentos da ordem (`.custom-css-servicos-ordem-pagamentos`) e o selo dele (`.custom-css-servicos-ordem-pagamento-situacao`)
- **Valores:** `sem_valor` · `pendente` · `parcial` · `pago`

### `data-pagina`

- **Onde:** cada página com o pixel, na lista de páginas do Pixel da Meta (Opções → Integrações e segurança)
- **Valores:** `cardapio` · `loja` · `bio` · `reservas` · `agendamento` · `rastreio`

### `data-paginas`

- **Onde:** cartão de PDF do chat interno (`.custom-css-chat-pdf`)
- **Valores:** quantas páginas o PDF tem — só quando `data-estado` é `pronto`

### `data-papel`

- **Onde:** cada mensagem da conversa do Assistente de IA (`.custom-css-assistente-mensagem`)
- **Valores:** `usuario` (a pergunta) · `assistente` (a resposta)

### `data-para`

- **Onde:** cada botão de etapa da ordem de serviço (`.custom-css-servicos-ordem-acao`) e a janela do motivo (`.custom-css-modal-servicos-motivo`)
- **Valores:** a etapa para onde a ordem vai: `aberta` · `diagnostico` · `aguardando_aprovacao` · `aprovada` · `recusada` · `aguardando_peca` · `em_execucao` · `concluida` · `entregue` · `cancelada`

### `data-passo`

- **Onde:** cada passo do editor da automação do Instagram (`.custom-css-ig-automacao-passo`)
- **Valores:** `quando` · `faca` · `ajustes`

### `data-pasta`

- **Onde:** caixa de seleção de pasta no modal de conta de e-mail; e a pasta de figurinhas (chip do seletor no compositor e item da lista na tela de Figurinhas)
- **Valores:** no e-mail: o caminho IMAP da pasta (ex.: `INBOX`, `INBOX.Comercial`). Nas figurinhas: o id da pasta

### `data-pede-valor`

- **Onde:** cartão de cada tag na Tela 1 do encerramento em 3 passos
- **Valores:** `obrigatorio` (a tag pede valor e não aceita R$ 0,00) · `opcional` (pede, mas aceita em branco) · `nao` (a Tela 2 é pulada)

### `data-pedido`

- **Onde:** cada pedido do histórico do cliente na página Clientes do PDV (`.custom-css-clientes-pdv-pedidos`)
- **Valores:** o número do pedido

### `data-pedido`

- **Onde:** cada linha da lista "Cancelados" do Relatório do PDV (`.custom-css-relatorio-pdv-cancelado`)
- **Valores:** o id do pedido

### `data-pedido-id`

- **Onde:** cada rodada na janela da conta da mesa (`.custom-css-salao-da-mesa-rodada`)
- **Valores:** o id do pedido da rodada — o mesmo do `pedido.id` do webhook

### `data-percentual-da-meta`

- **Onde:** cartão da meta do mês, em Minha evolução
- **Valores:** o percentual do vendido sobre a meta, com uma casa (`41.7`, `150`) · vazio quando não há meta cadastrada

### `data-perfil`

- **Onde:** o perfil do vendedor ao lado do nome no Ranking do CRM e nas metas (`.custom-css-crm-ranking-perfil`)
- **Valores:** `admin` · `supervisor` · `user`

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

### `data-pixel-meta`

- **Onde:** o script do pixel da Meta que as páginas públicas carregam (cardápio, loja, bio, reservas, agendamento, rastreio)
- **Valores:** sempre `script` — serve para achar ou esconder o script do pixel

### `data-pixel-status`

- **Onde:** a situação de cada evento do formato de mensagens na tela de logs do Pixel (`.custom-css-pixel-logs-status`)
- **Valores:** `pendente` (na fila) · `enviando` · `enviado` (a Meta recebeu) · `ignorado` (não pôde sair — o porquê está em `.custom-css-pixel-logs-motivo`) · `falhou` (a Meta recusou ou não respondeu). Os eventos do formato site não levam o atributo

### `data-plano`

- **Onde:** o bloco do link de cadastro na tela de planos (`.custom-css-planos-link-de-cadastro`) e o plano escolhido pelo link na página de cadastro (`.custom-css-signup-plano-do-link`)
- **Valores:** o id do plano (`1`, `2`, `3`...)

### `data-plataforma`

- **Onde:** opções de plataforma no cadastro por app próprio
- **Valores:** o id da plataforma

### `data-pode-espiar`

- **Onde:** card do quadro de atendimentos
- **Valores:** `true` quando quem olha pode abrir a conversa com duplo clique · `false` quando "Operador Visualiza Prévias?" está desligada para ele

### `data-porcentagem`

- **Onde:** a barra de progresso na página do convidado (`.custom-css-convidado-progresso`)
- **Valores:** de `0` a `100`

### `data-porta`

- **Onde:** cada porta da aba Marcação do Consultório (`.custom-css-consultorio-marcacao-porta`)
- **Valores:** `painel` a regra da tela (recepção) · `api` a regra de quem marca de fora

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

### `data-previa`

- **Onde:** o aviso em cima da prévia do Criar Template (WABA) enquanto nenhum campo foi preenchido (`.custom-css-waba-template-previa-exemplo`)
- **Valores:** `exemplo` — a prévia mostra o exemplo da aba escolhida, e não o que foi digitado

### `data-prioridade`

- **Onde:** cartão de tarefa (`.custom-css-task-card`)
- **Valores:** `high` · `medium` · `low`

### `data-prioridade`

- **Onde:** cada ordem de serviço na lista (`.custom-css-servicos-ordem-na-lista`)
- **Valores:** `baixa` · `normal` · `alta` · `urgente`

### `data-privada`

- **Onde:** o cadeado de cada conversa na lista do chat interno (botão `[data-action=privada]`)
- **Valores:** `true` conversa privada (o administrador de fora não vê) · `false` visível para a gestão

### `data-problema`

- **Onde:** cada bloco listado no Verificar do editor de fluxo (`.custom-css-flow-verificar-item`); e a regra do cashback por categoria do Cardápio que impede salvar (`.custom-css-cardapio-cashback-regra`)
- **Valores:** `isolado` (não se chega a ele a partir do Início) · `sem-entrada` · `sem-saida` (o fluxo para nele) · `salto-quebrado` (um "Pular para" sem destino) · `ciclo-sem-espera` (aqui o item é o ciclo inteiro) No cashback do Cardápio: `percentual` (sem % válido) · `categorias` (sem categoria) · `repetida` (com a categoria de outra regra).

### `data-product-id`

- **Onde:** cartão da tela de Produtos (`.custom-css-product-card`)
- **Valores:** o id do produto

### `data-produto`

- **Onde:** cada produto achado pela busca da janela "Lançar na mesa" (tela Comandas)
- **Valores:** o id do produto no cadastro — tocar nele põe o produto no pedido do garçom

### `data-produto`

- **Onde:** cada produto da escolha "Só quando a venda tiver estes produtos" do modelo de projeto (`.custom-css-projeto-modelo-produtos`)
- **Valores:** o id do produto no cadastro

### `data-produtos`

- **Onde:** linha de produtos da oportunidade
- **Valores:** quantos itens são

### `data-progresso`

- **Onde:** a barra de progresso do relatório da campanha do Mail Marketing (`.custom-css-mail-marketing-progresso`)
- **Valores:** de `0` a `100`: quanto da campanha já saiu

### `data-prompt`

- **Onde:** o cartão de cada prompt na tela de Prompts (`.custom-css-prompts-cartao`)
- **Valores:** o id do prompt

### `data-protocolo`

- **Onde:** o cartão do #protocolo citado numa mensagem do chat interno (`.custom-css-chats-protocolo`)
- **Valores:** o número do protocolo, sem o `#`

### `data-provedor`

- **Onde:** o botão "Confirmar e enviar só o link" do pedido (`.custom-css-pedido-confirmar-so-o-link`)
- **Valores:** o provedor do link que vai ao cliente: `asaas` · `mercadopago` · `pagseguro` · `paggpix`

### `data-provedor`

- **Onde:** o botão "Fechar com link de pagamento" da venda de balcão (`.custom-css-balcao-fechar-com-link`)
- **Valores:** o provedor do link da venda: `asaas` · `mercadopago` · `pagseguro` · `paggpix`

### `data-quadro`

- **Onde:** aviso da página do Quadro de Atendimentos
- **Valores:** `fora-do-plano` — a empresa não tem o módulo `useQuadro` contratado. É o único valor emitido hoje; serve para esconder o aviso ou trocá-lo por um texto próprio

### `data-quantas`

- **Onde:** o botão das tarefas em execução, na barra do topo (`data-appbar="tarefas-em-execucao"`)
- **Valores:** quantas tarefas estão em execução agora (`0` quando nenhuma)

### `data-quantidade`

- **Onde:** cada pacote do cadastro (`.custom-css-reservas-pacote`)
- **Valores:** quantas reservas o pacote dá (`1` a `500`)

### `data-queue-chatbot`

- **Onde:** cartão do ticket, cartão de grupo, cabeçalho da conversa aberta e os cards do quadro de atendimentos e dos kanbans (`/kanban`, equipe, filas e grupos); o cartão da tela de Setores (`.custom-css-queue-card`); e as opções de setor do "Filtrar por Setores" da lista de atendimentos e das listas de escolher setor (transferir e novo atendimento)
- **Valores:** `true` · `false`. **Ausente quando o payload traz a fila sem dizer se ela é de chatbot** — é "não sei", e não "false"; quem customiza cai no critério seguinte dele

### `data-queue-color`

- **Onde:** cartão do ticket, cabeçalho da conversa aberta, o cartão da tela de Setores (`.custom-css-queue-card`) e o card do Quadro (`.custom-css-quadro-card`), também na pílula da fila (`.custom-css-quadro-fila`); o chip de cada setor no campo Setores das janelas (`.custom-css-queue-select-chip` — no Editar Usuário, nas conexões…) e no cartão de Usuários (`.custom-css-users-card-setor`)
- **Valores:** a cor da fila

### `data-queue-color`

- **Onde:** o chip de cada setor escolhido no filtro de Setores da Gestão de Atendimentos (`.custom-css-gestao-setor-chip`)
- **Valores:** a cor do setor (`#1976d2`...); ausente no "Sem setor"

### `data-queue-id`

- **Onde:** cartão do ticket, cartão de grupo, cabeçalho da conversa aberta, os cards do quadro de atendimentos e dos kanbans, e o cartão da tela de Setores; o chip de cada setor no campo Setores das janelas (`.custom-css-queue-select-chip` — no Editar Usuário, nas conexões…) e no cartão de Usuários (`.custom-css-users-card-setor`); e as opções de setor do "Filtrar por Setores" da lista de atendimentos e das listas de escolher setor (transferir e novo atendimento)
- **Valores:** o id da fila, ou vazio quando o atendimento não tem fila

### `data-queue-id`

- **Onde:** o chip de cada setor escolhido no filtro de Setores da Gestão de Atendimentos (`.custom-css-gestao-setor-chip`)
- **Valores:** o id do setor

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
- **Valores:** `atendente` · `setor` · `etapa`

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

### `data-recorte`

- **Onde:** cada seletor do recorte nos Filtros Avançados do Dashboard (`.custom-css-dashboard-recorte`)
- **Valores:** `queueIds` (os Setores) · `userIds` (os atendentes) · `tagIds` (as tags)

### `data-recurso`

- **Onde:** cada coluna da agenda das reservas no dia (`.custom-css-reservas-agenda-coluna`)
- **Valores:** o id do recurso da coluna (vazio na coluna das reservas sem recurso)

### `data-reenvio`

- **Onde:** o aviso "A Meta não confirmou" com o botão Enviar novamente, dentro do balão (`.custom-css-mensagem-reenvio`)
- **Valores:** `pendente` (esperando o clique) · `enviando` (o reenvio em andamento)

### `data-referencia`

- **Onde:** linha da tabela de logs de erro
- **Valores:** a referência daquele log — dá pra destacar por CSS os erros de uma origem só

### `data-regra`

- **Onde:** ícone de regra no cabeçalho da coluna automática do quadro de atendimentos; e cada regra da janela de Pontuação e níveis (`.custom-css-gamificacao-regra`); e cada regra do cashback por categoria do Cardápio (`.custom-css-cardapio-cashback-regra`)
- **Valores:** no quadro, `fila` — a coluna recebe sozinha os pendentes das filas da regra (é o único valor ali). As regras do quadro, as que cada um cria na tela de regras, usam `data-regra-id`. Na Pontuação e níveis, o que rende o ponto: `venda` · `valor` · `meta` · `encerramento` (cada encerramento com venda) · `funil` (cada venda no funil escolhido, uma linha por funil) · `etiqueta` (cada venda com a etiqueta escolhida, uma linha por etiqueta) No cashback do Cardápio, a posição da regra na lista, a partir de 0.

### `data-regra-ativa`

- **Onde:** cada linha da tela de regras do quadro (`.custom-css-regras-quadro-regra`)
- **Valores:** `true` · `false` — a regra desligada continua na lista, esmaecida, e não roda

### `data-regra-id`

- **Onde:** ícone de regra no card do quadro de atendimentos (`.custom-css-quadro-card-regra`) e cada linha da tela de regras do quadro (`.custom-css-regras-quadro-regra`)
- **Valores:** o id da regra do quadro. No card, é a regra que pôs o atendimento na coluna em que ele está — o ícone some quando alguém arrasta o card para outra coluna

### `data-regra-propria`

- **Onde:** cada linha da comissão dos entregadores no Relatório do PDV (`.custom-css-relatorio-pdv-comissao-entregador-linha`)
- **Valores:** `sim` o entregador tem regra própria · `nao` segue a regra geral

### `data-regra-travada`

- **Onde:** a mesma linha
- **Valores:** `true` na regra da equipe vista em Minhas regras (com cadeado e sem botões) · `false` nas que quem olha pode mudar

### `data-relatorio`

- **Onde:** cada relatório da seção Relatórios detalhados do dashboard (`.custom-css-dashboard-relatorio-secao`)
- **Valores:** `operador` (o relatório por operador) · `periodo` (o relatório por período)

### `data-remarcar`

- **Onde:** o que o botão Remarcar faz na confirmação do Consultório (`.custom-css-consultorio-acoes-dos-botoes`)
- **Valores:** `setor` (abre o atendimento no setor escolhido) · `nota` (só avisa a equipe com a nota)

### `data-remarketing`

- **Onde:** controles da tela de logs de remarketing
- **Valores:** `auto-atualizar` · `retencao`

### `data-repetida`

- **Onde:** a confirmação da lista de espera na página pública das Reservas (`.custom-css-reservas-publica-espera-feita`)
- **Valores:** `1` quando a pessoa já estava na lista, `0` quando entrou agora

### `data-reserva-id`

- **Onde:** cada reserva da aba Reservas das Comandas (`.custom-css-reservas-da-mesa-reserva`)
- **Valores:** o id da reserva — o mesmo do `reserva.id` do webhook e da API

### `data-reservas`

- **Onde:** cada barra (`.custom-css-reservas-relatorio-barra`) e cada cliente (`.custom-css-reservas-relatorio-cliente`) do relatório das reservas
- **Valores:** o número de reservas (`0`, `1`, `2`...)

### `data-resposta-na-volta`

- **Onde:** modal que oferece deixar pronta a retomada, ao enviar um template
- **Valores:** `pergunta` · `texto` · `prazo` · `nao`

### `data-resposta-na-volta-aviso`

- **Onde:** faixa sobre o campo, dizendo que há uma retomada guardada
- **Valores:** `true` na faixa · `cancelar` no botão que a descarta

### `data-respostas`

- **Onde:** o selo de respostas ao lado da nota, na tabela do Relatório de Avaliações (`.custom-css-ratings-report-respostas-selo`)
- **Valores:** quantas respostas o cliente deu nas perguntas do fluxo da nota

### `data-restantes`

- **Onde:** botão “ver mais” de uma raia do quadro do CRM
- **Valores:** quantos cartões ainda não foram carregados

### `data-resultado`

- **Onde:** o último envio do resumo automático do Dashboard (`.custom-css-dashboard-resumo-ultimo`)
- **Valores:** `ok` (saiu por todos os destinos) · `falha` (algum destino não recebeu; o motivo aparece embaixo)

### `data-resultados`

- **Onde:** a lista de resultados da busca do menu lateral (`.custom-css-menu-busca-resultados`)
- **Valores:** quantos itens do menu casaram com o texto (`0`: aparece `.custom-css-menu-busca-vazia`)

### `data-resumo`

- **Onde:** os blocos do topo da Pesquisar (`.custom-css-atendimentos-resumo`)
- **Valores:** `total` · `tempos` · `baixar` (o de baixar os resultados, só do admin, não é cartão de número)

### `data-rodada`

- **Onde:** cada linha do estado das rodadas na Avaliação pela IA, em Configurações → Opções, logo abaixo do "Avaliar agora" (dentro de `.custom-css-avaliacao-ia-rodadas`; a linha leva também `.custom-css-avaliacao-ia-rodada-<valor>`)
- **Valores:** `rodando` (há uma rodada agora) · `nenhuma` (ainda não houve) · `naoTerminou` (começou e não terminou) · `ultima` (a última: avaliados, ignorados, falhas e aulas) · `motivo` (por que falharam) · `proxima` (quando é a próxima)

### `data-rotulo-editar`

- **Onde:** no botão de editar do balão de link do editor de texto (`a.ql-action`)
- **Valores:** o texto de `textoRico.link.editar` nas Traduções

### `data-rotulo-link`

- **Onde:** no balão de link do editor de texto (`.ql-tooltip`), o rótulo de quando se digita o endereço do link
- **Valores:** o texto de `textoRico.link.digite` nas Traduções

### `data-rotulo-remover`

- **Onde:** no botão de remover do balão de link do editor de texto (`a.ql-remove`)
- **Valores:** o texto de `textoRico.link.remover` nas Traduções

### `data-rotulo-salvar`

- **Onde:** no botão de salvar do balão de link do editor de texto (`a.ql-action`, ao digitar o endereço)
- **Valores:** o texto de `textoRico.link.salvar` nas Traduções

### `data-rotulo-visitar`

- **Onde:** no balão de link do editor de texto (`.ql-tooltip`), o rótulo de quando o balão mostra um link já posto
- **Valores:** o texto de `textoRico.link.visitar` nas Traduções

### `data-rotulos`

- **Onde:** a barra de ações agrupada do ticket (`.custom-css-ticket-actions`)
- **Valores:** `todos` ícone e texto · `principal` só a ação principal com texto · `nenhum` só ícones

### `data-sala`

- **Onde:** o botão de entrar na reunião de cada tarefa do cartão Tarefas do painel do contato (`.custom-css-contato-tarefa-entrar`)
- **Valores:** `nossa` (a nossa videochamada, abre a janela da chamada) · `link` (um link colado — Meet, Zoom, Teams —, abre em outra aba)

### `data-saldo`

- **Onde:** o saldo de cashback do cliente na página Clientes do PDV (`.custom-css-clientes-pdv-cashback`)
- **Valores:** o saldo em centavos (`0`: sem saldo)

### `data-salvo`

- **Onde:** o status de salvo do editor de fluxo, acima do desenho (`.custom-css-flow-status`)
- **Valores:** `true` (fluxo salvo) · `false` (há alterações não salvas)

### `data-secao`

- **Onde:** cada seção da página das classes (`.custom-css-documentacao-css-secao`) e o link dela no sumário (`.custom-css-documentacao-css-sumario-item`); cada seção das janelas de Tag, de Categoria (de setores e de fluxos) e de Webhook (`.custom-css-dialog-secao`); e cada seção do corpo do Criar Template (`.custom-css-waba-template-form-secao`)
- **Valores:** o nome da seção: `como-usar` · `convencoes` · `propriedades` · `tema-escuro` · `eventos` · `atributos` · `paginas` · `modais` · `especificas` · `sem-prefixo` · `chat-externo` · `historico` · `nao-achou` — o mesmo que, depois do `#` no endereço, abre a página já na seção. Nas janelas: na de Tag, `informacoes-basicas` · `configuracoes-avancadas` · `pixel` · `automacao`; na de Categoria, `informacoes` · `cor`; na de Webhook, `informacoes-basicas` · `status`. No Criar Template: `cabecalho` · `corpo` · `rodape` · `botoes`

### `data-section`

- **Onde:** a faixa de seção do cadastro de Planos (`.custom-css-planos-secao`) e o título de seção da janela de contato (`.custom-css-contact-modal-secao`)
- **Valores:** Planos: `dados`, `limites`, `canais`, `recursos`, `ia`, `automacoes`, `gerais`. Janela de contato: `mainInfo`, `technicalInfo`, `contactInfo`, `personalData`, `location`, `specialSettings`, `extraInfo`

### `data-segmento`

- **Onde:** a janela da ordem de serviço (`.custom-css-modal-servicos-ordem`)
- **Valores:** `assistencia` (o equipamento, a marca, o modelo) · `grafica` (o pedido: o produto e as especificações). A página dos Serviços leva a classe `.custom-css-servicos-segmento-assistencia` ou `.custom-css-servicos-segmento-grafica`

### `data-selecionada`

- **Onde:** cartão de cada tag na Tela 1 do encerramento em 3 passos (`.custom-css-encerramento-tag`)
- **Valores:** `true` na tag escolhida · `false` nas outras

### `data-selecionadas`

- **Onde:** a barra da seleção em massa das Tarefas (`.custom-css-tarefas-selecao`)
- **Valores:** quantas tarefas estão marcadas (`0` quando nenhuma)

### `data-selecionando`

- **Onde:** campo de digitação
- **Valores:** `true` enquanto o modo de selecionar mensagens está ligado

### `data-selected`

- **Onde:** cartão do ticket; e o cartão de categoria do Criar Template (WABA)
- **Valores:** no ticket: `true` no ticket aberto. No cartão de categoria: `true` no escolhido · `false` nos outros. Ali não vai `aria-checked`: o cartão já tem um rádio de verdade dentro, e o leitor de tela anunciaria duas escolhas

### `data-sem-foto`

- **Onde:** o aviso "Sem foto: vai só o valor" na linha da consulta de preço e estoque (`.custom-css-consulta-de-produtos-sem-foto`), com "Enviar com a foto do produto" marcado
- **Valores:** `true`

### `data-sem-nome`

- **Onde:** a célula do nome na lista de Contatos (`.custom-css-contacts-nome`)
- **Valores:** `true` quando o contato não tem nome no cadastro (a célula mostra "Sem nome"); ausente quando tem

### `data-semana`

- **Onde:** cada célula da Evolução da Avaliação pela IA (`[data-grafico="evolucao-semanal"]`)
- **Valores:** a segunda-feira da semana, `AAAA-MM-DD`

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

### `data-sentido`

- **Onde:** a tendência de cada indicador do Dashboard (`.custom-css-kpi-tendencia`)
- **Valores:** `positiva` (melhorou) · `negativa` (piorou) · `neutra` (sem mudança). Nos tempos, subir é piorar: o tempo de resposta que aumentou leva `negativa`

### `data-serie`

- **Onde:** a marca da série no detalhe da reserva (`.custom-css-reservas-reserva-serie`)
- **Valores:** o número da série (`1`, `2`, `3`...)

### `data-setor`

- **Onde:** cada setor de produção — na lista da janela dos setores (`.custom-css-setor-do-pdv`), no nome do setor ao lado da categoria (`.custom-css-categoria-setor`) e no setor de cada item do Painel de Pedidos (`.custom-css-painel-item-setor`)
- **Valores:** o id do setor (o mesmo de `GET /pdv/setores`), para dar a cada setor — Cozinha, Bar, Caixa... — a sua própria aparência

### `data-setor-da-resposta`

- **Onde:** o setor onde cai a resposta do paciente ao lembrete (`.custom-css-consultorio-setor-da-resposta`)
- **Valores:** o id do setor escolhido — ou `sempre` (a fila padrão da conexão)

### `data-settings-aba`

- **Onde:** as abas de Configurações → Opções (`.custom-css-settings-aba`), o painel delas (`.custom-css-settings-aba-painel`), o índice dos subtítulos (`.custom-css-settings-indice-da-aba`) e cada resultado da busca (`.custom-css-settings-busca-resultado`)
- **Valores:** `geral` · `atendimento` · `contatos` · `automacao` · `chamadas` · `vendas` · `integracoes` — e `plataforma` no painel da aba Plataforma (só o super admin). No painel, é a aba aberta; na aba, o nome dela (a aberta também leva `data-active="true"` e `.custom-css-settings-aba-ativa`); no resultado da busca, a aba onde a opção mora. O endereço usa os mesmos nomes: `/settings?aba=atendimento&secao=transferencias`

### `data-settings-busca`

- **Onde:** o campo "Pesquisar opção" de Configurações → Opções (o `input` dentro de `.custom-css-settings-busca`)
- **Valores:** `campo`

### `data-settings-buscando`

- **Onde:** o painel das abas de Configurações → Opções (`.custom-css-settings-aba-painel`)
- **Valores:** `true` enquanto há texto em "Pesquisar opção" — o painel fica escondido e aparece a lista de resultados (`.custom-css-settings-busca-resultados`) · `false`

### `data-settings-campo`

- **Onde:** um campo dentro de uma seção de Configurações, que o endereço `?aba=…&secao=…&campo=…` destaca e traz para a tela
- **Valores:** `avaliacao-ia-faltas` (a chave "Registrar os produtos em falta", na Avaliação pela IA, dentro de `avaliacoes`)

### `data-settings-item`

- **Onde:** o que se procura pelo nome na busca de Configurações → Opções sem ser um campo (o botão "Adicionar processo" dos processos por setor ou conexão)
- **Valores:** o nome do item na busca

### `data-settings-item-ajuda`

- **Onde:** a ajuda do item de busca de `data-settings-item`
- **Valores:** o texto que a busca também lê

### `data-settings-plataforma-grupo`

- **Onde:** os subtítulos da aba Plataforma de Configurações (`.custom-css-settings-plataforma-grupo`, só o super admin)
- **Valores:** `marca` (Marca e acesso) · `cobranca` (Cobrança da plataforma) · `canais` (Canais e e-mail) · `monitoramento` (Monitoramento)

### `data-settings-secao`

- **Onde:** cada seção de Configurações (`.custom-css-settings-secao`) e a faixa dela (`.custom-css-section-header`)
- **Valores:** `empresa` · `expediente` · `permissoes` · `rodizio` · `transferencias` · `bot` · `ia-pdv` · `avaliacoes` · `chamadas` · `grupos` · `contatos-campos` · `mensagens` · `sons-notificacoes` · `carteiras` · `pdv` (só com o PDV) · `webhooks` · `pixel-meta` · `google-analytics-paginas` · `mcp` · `crm` · `armazenamento` · `seguranca` · `logs` · `sistema` (desde a WS-29.936.0; `aniversario` virou parte de `mensagens` e `2fa`, de `seguranca`); e, só para o super: `senha` · `global` · `smtp` · `pix-efi` · `mercado-pago` · `stripe` · `asaas` · `paypal` · `patibill` · `pwa` · `baileys` · `ajuda` · `nome-app` · `layout-v2` · `apps-externos` · `waba` · `google-analytics` · `infra` · `desempenho`

### `data-settings-secao`

- **Onde:** o nome antigo de uma seção de Configurações, em volta do campo que ela tinha (`.custom-css-settings-secao-antiga`, que também leva `.custom-css-settings-secao`)
- **Valores:** `aniversario` (a mensagem de aniversário, dentro de `mensagens`) · `2fa` (a verificação em duas etapas, dentro de `seguranca`) — sem caixa própria (`display: contents`): serve para o CSS, não muda o layout

### `data-settings-tab`

- **Onde:** cartão do menu da tela de Configurações
- **Valores:** o nome da aba (`options`, `schedules`, `tokenempresa`, `companies`…). O cartão também carrega `id="simple-tab-<nome>"`, `role="tab"`, `aria-selected` e `aria-controls="simple-tabpanel-<nome>"` — o painel já se apresentava com esse id e apontava para uma aba que não existia

### `data-sinal`

- **Onde:** cada oferta da aba Ofertas das Reservas (`.custom-css-reservas-oferta`)
- **Valores:** `nenhum` (sem sinal) · `percentual` (uma parte do preço) · `valor` (um valor fixo)

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

- **Onde:** cada campanha da janela de Campanhas (`.custom-css-gamificacao-campanha`); cada oportunidade (`.custom-css-contato-oportunidade`) e cada linha da tabela de Oportunidades (`.custom-css-oportunidades-linha`) e cada projeto (`.custom-css-contato-projeto`) nos cartões do painel do contato; a situação da tarefa ao lado do título da janela (`.custom-css-tarefa-situacao`); a situação de cada etapa de uma avaliação pela IA (dentro de `.custom-css-avaliacao-ia-etapa-avaliada`)
- **Valores:** na campanha: `agendada` (ainda não começou) · `andamento` (hoje está dentro dela) · `encerrada`; na oportunidade: `aberta` · `ganha` · `perdida`; no projeto: `planejamento` · `andamento` · `pausado` · `concluido`; na tarefa: `pendente` · `atrasada` · `realizada` (Concluída); na etapa avaliada pela IA: `seguiu` · `parcial` · `nao_seguiu` · `nao_se_aplica` · `sem` (a IA não respondeu)

### `data-situacao`

- **Onde:** o pagamento no detalhe da reserva (`.custom-css-reservas-reserva-pagamento`) e o sinal na página pública (`.custom-css-reservas-publica-sinal`)
- **Valores:** `pendente` · `parcial` · `paga`

### `data-situacao`

- **Onde:** cada pagamento da reserva (`.custom-css-reservas-reserva-pagamento-linha`)
- **Valores:** `pendente` · `confirmado` · `cancelado` · `estornado`

### `data-situacao`

- **Onde:** cada pessoa da lista de espera na agenda das Reservas (`.custom-css-reservas-agenda-espera-item`)
- **Valores:** `aguardando` · `avisado`

### `data-situacao`

- **Onde:** o Modo Secretária (Telegram Business) na conexão de Telegram (`.custom-css-telegram-business`)
- **Valores:** `aguardando` (nenhuma conta ligou o bot) · `respondendo` (responde pela conta) · `semPermissao` (ligado sem poder responder) · `desligado` (a conta desligou o bot)

### `data-situacao`

- **Onde:** cada mensagem no histórico do detalhe da reserva (`.custom-css-reservas-reserva-aviso`)
- **Valores:** `enviando` · `enviado` · `falhou`

### `data-situacao`

- **Onde:** a situação no "minha reserva" (`.custom-css-reservas-publica-situacao`) e a reserva feita pela página (`.custom-css-reservas-publica-feita`)
- **Valores:** `pendente` · `confirmada` · `concluida` · `nao_compareceu` · `cancelada`

### `data-situacao`

- **Onde:** cada reserva da agenda (`.custom-css-reservas-agenda-reserva`) e a situação no detalhe (`.custom-css-reservas-reserva-situacao`)
- **Valores:** `pendente` · `confirmada` · `concluida` · `nao_compareceu` · `cancelada`

### `data-situacao`

- **Onde:** cada ordem de serviço na lista (`.custom-css-servicos-ordem-na-lista`), o selo da etapa (`.custom-css-servicos-situacao`) e cada filtro de etapa (`.custom-css-servicos-ordens-filtro`, que também tem `em_andamento` e `todas`)
- **Valores:** `aberta` · `diagnostico` · `aguardando_aprovacao` · `aprovada` · `recusada` · `aguardando_peca` · `em_execucao` · `concluida` · `entregue` · `cancelada`

### `data-situacao`

- **Onde:** cada horário na agenda dos Serviços (`.custom-css-servicos-agendamento`) e o horário marcado na página do cliente (`.custom-css-servicos-agendamento-publico-cartao`, `.custom-css-servicos-agenda-publica-marcado`)
- **Valores:** `agendado` · `confirmado` · `concluido` · `faltou` · `cancelado`

### `data-situacao`

- **Onde:** cada link de pagamento na ficha da ordem de serviço (`.custom-css-servicos-ordem-cobranca`)
- **Valores:** `pendente` · `pago` · `cancelado`

### `data-situacao`

- **Onde:** a página da ordem para o cliente (`.custom-css-servicos-publica-ordem`) e o selo da etapa nela (`.custom-css-servicos-publica-situacao`)
- **Valores:** `aberta` · `diagnostico` · `aguardando_aprovacao` · `aprovada` · `recusada` · `aguardando_peca` · `em_execucao` · `concluida` · `entregue` · `cancelada`

### `data-situacao-na-tela`

- **Onde:** a situação escrita no cartão da agenda das Reservas (dentro de `.custom-css-reservas-agenda-reserva`)
- **Valores:** `pendente` · `aguardandoSinal` (pendente, esperando o sinal) · `confirmada` · `concluida` · `nao_compareceu` · `cancelada`

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

### `data-status`

- **Onde:** cada tarefa do quadro na página do projeto (`.custom-css-projeto-tarefa`)
- **Valores:** a situação da tarefa como o sistema grava (`pending`, `completed`...)

### `data-substituicao`

- **Onde:** o resultado da importação de produtos (`.custom-css-modal-product-import`)
- **Valores:** `nao_pedida` (a importação de sempre) · `feita` (os produtos fora da planilha foram apagados) · `cancelada` (havia linha com problema: nada foi apagado)

### `data-tag-color`

- **Onde:** etiqueta; o cartão da tela de Tags (`.custom-css-tag-card`); e a etiqueta do card do Kanban e do Kanban da equipe (`.custom-css-kanban-card-tag`)
- **Valores:** a cor dela

### `data-tag-id`

- **Onde:** etiqueta; o cartão da tela de Tags; e a etiqueta do card do Kanban e do Kanban da equipe
- **Valores:** o id dela

### `data-tamanho`

- **Onde:** o tamanho de cada gravação pronta na tela de Gravações (`.custom-css-gravacoes-tamanho`) e o botão Baixar da janela da gravação (`.custom-css-gravacoes-baixar`)
- **Valores:** o tamanho do arquivo em bytes (`2684354560`...); ausente quando o armazenamento não informou

### `data-tarefa`

- **Onde:** a faixa da tarefa no topo da janela de comentários (`.custom-css-tarefa-comentarios-faixa`)
- **Valores:** o id da tarefa dos comentários

### `data-tarefa`

- **Onde:** linha de tarefa no resumo do contato, dentro do atendimento
- **Valores:** o id da tarefa — a linha inteira abre a tarefa

### `data-tarefa`

- **Onde:** cada tarefa do quadro na página do projeto (`.custom-css-projeto-tarefa`)
- **Valores:** o id da tarefa

### `data-task-id`

- **Onde:** cada linha da janela das tarefas em execução (`.custom-css-tarefa-em-execucao-linha`)
- **Valores:** o número da tarefa

### `data-tem-ata`

- **Onde:** a ATA da reunião na janela da gravação (`.custom-css-gravacoes-ata`)
- **Valores:** `true` a ATA já foi gerada · `false` ainda não

### `data-tem-contato`

- **Onde:** bloco de identificação de quem liga, na janela de chamada recebida do webphone
- **Valores:** `true` quando o número casou com um contato (a linha do nome existe) · `false`

### `data-tem-fila`

- **Onde:** o campo "Fila de atendimento para grupos" no cadastro da conexão (`.custom-css-conexao-fila-dos-grupos`)
- **Valores:** `true` os grupos desta conexão chegam numa fila · `false` sem fila (como antes)

### `data-tem-sugestao`

- **Onde:** barra da sugestão de IA
- **Valores:** `true` quando já existe sugestão gerada — junto do `data-carregando`, cobre os três estados da barra

### `data-tem-token`

- **Onde:** o campo do token da API de Conversões, em Opções → Integrações e segurança → Pixel da Meta
- **Valores:** `true` já há um token guardado (ele nunca volta para a tela) · `false` sem token

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

### `data-ticket`

- **Onde:** cada linha da lista dos atendimentos de um número do Dashboard (`.custom-css-dashboard-lista-linha`)
- **Valores:** o id do atendimento

### `data-ticket-contexto`

- **Onde:** o cabeçalho do ticket (`.custom-css-ticket-header`), as ações (`.custom-css-ticket-actions`, `.custom-css-ticket-actions-mobile`), o menu Mais e a moldura do pop-up (`.custom-css-modal-ticket`)
- **Valores:** `chats` (a tela de atendimentos) · `quadro` (o pop-up do Quadro de Atendimentos e da Gestão) · `janela` (o pop-up aberto de outras telas) · `embed` (o ticket incorporado)

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

### `data-tipo`

- **Onde:** cada linha do resumo do Monte seu plano (`.custom-css-monte-seu-plano-item`) e do plano montado na página de cadastro (`.custom-css-signup-plano-montado-item`)
- **Valores:** `mensal` (entra na mensalidade) · `implantacao` (cobrado uma vez, na primeira fatura)

### `data-tipo`

- **Onde:** cada aviso da aba dos avisos das Reservas (`.custom-css-reservas-aviso`)
- **Valores:** `criada` · `pendente` · `confirmada` · `remarcada` · `cancelada`

### `data-tipo`

- **Onde:** cada recurso da aba Recursos das Reservas (`.custom-css-reservas-recurso`)
- **Valores:** `profissional` · `mesa` · `sala` · `quarto` · `equipamento` · `outro`

### `data-tipo`

- **Onde:** cada peça ou serviço do catálogo dos Serviços (`.custom-css-servicos-item`) e a janela do item (`.custom-css-modal-servicos-item`)
- **Valores:** `peca` · `servico`

### `data-tipo`

- **Onde:** cada peça ou serviço da ordem (`.custom-css-servicos-ordem-linha`) e a janela do item (`.custom-css-modal-servicos-linha`)
- **Valores:** `peca` · `servico`

### `data-tipo`

- **Onde:** cada linha do histórico da ordem de serviço (`.custom-css-servicos-ordem-evento`)
- **Valores:** `criada` · `alterada` · `situacao` · `item` · `pagamento` · `estorno` · `nota` · `anexo`

### `data-tipo`

- **Onde:** cada aviso da aba Avisos dos Serviços (`.custom-css-servicos-aviso`)
- **Valores:** a etapa do aviso: `aberta` · `diagnostico` · `aguardando_aprovacao` · `aprovada` · `recusada` · `aguardando_peca` · `em_execucao` · `concluida` · `entregue` · `cancelada`

### `data-tipo`

- **Onde:** cada aviso nas opções da agenda (`.custom-css-servicos-agenda-aviso`)
- **Valores:** `confirmacao` · `remarcacao` · `cancelamento` · `lembrete`

### `data-tipo`

- **Onde:** a regra geral da comissão do entregador (`.custom-css-comissao-do-entregador-geral`)
- **Valores:** `dia` · `percentual` · `entrega` · `dia-percentual` · `dia-entrega` · `nenhum` (sem comissão)

### `data-tipo-conexao`

- **Onde:** a conexão de cada regra de lembrete do Consultório (`.custom-css-consultorio-lembrete-conexao`)
- **Valores:** `antes` (a conexão das confirmações, como antes) · `atendimento` (a do atendimento do paciente) · `fixa`

### `data-tom`

- **Onde:** a variação de um cartão da API Oficial no Dashboard (`.custom-css-dashboard-api-oficial-variacao`)
- **Valores:** `bom` · `ruim` · `neutro` (o total enviado não é bom nem ruim; mais custo é ruim)

### `data-total`

- **Onde:** o mesmo dia; e o contador de cada aba da lista de atendimentos (`.custom-css-ticket-tabs-contador`, o `.MuiBadge-root` da aba); e a faixa das etiquetas do cartão do ticket (`.ticket-tags`)
- **Valores:** no dia, quantos agendamentos ele tem (já com a busca aplicada). Na aba, o total de atendimentos que o servidor informou — `0` até a primeira resposta; enquanto é `0`, o contador mostra só os carregados (`data-carregados`). Na faixa, quantas etiquetas o contato tem — cada uma com a posição em `data-posicao`

### `data-total-ajustado`

- **Onde:** o total grande da venda de balcão
- **Valores:** o total em reais com o desconto ou a taxa das formas de pagamento

### `data-total-chatbot`

- **Onde:** a aba AGUARDANDO da lista de atendimentos (o `.custom-css-ticket-tabs-contador` da aba), ao lado do `data-total`
- **Valores:** quantos atendimentos aguardando estão em setores marcados como "Agente de IA / Chatbot", com os mesmos filtros da aba — o servidor conta todos, e não só os já carregados. Ausente até a primeira resposta. A lista também pode vir só com esses setores: `queueChatbot=true` na busca da lista (`GET /tickets`); `queueChatbot=false` tira esses setores

### `data-total-servidor`

- **Onde:** subtítulo da raia do Kanban
- **Valores:** quantos cartões existem NO SERVIDOR naquela etapa — pode ser maior que os carregados na tela

### `data-transbordos`

- **Onde:** linha de transbordo do bloco, no relatório do rodízio
- **Valores:** quantos atendimentos o nó não conseguiu entregar no período — dá para destacar o bloco a partir de um patamar

### `data-transcricao`

- **Onde:** a marca "Transcrição do áudio" em cima do texto que transcreveu um áudio, na conversa do atendimento (`.custom-css-mensagem-transcricao`)
- **Valores:** `sim`

### `data-ultimo-login`

- **Onde:** linha do último login no card do operador, na tela de Usuários
- **Valores:** a data e hora no formato `dd/MM/yyyy HH:mm`, ou `nunca` para quem nunca entrou — dá para destacar quem está sumido

### `data-unidade`

- **Onde:** cada regra de lembrete na aba Confirmação do Consultório (`.custom-css-consultorio-lembrete`)
- **Valores:** `minutos` · `horas` · `dias` (o prazo da regra)

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

- **Onde:** cada convidado na linha do operador, no cabeçalho do atendimento (`.ticket-collaborator`); e o cartão da pessoa na tela de Usuários (`.custom-css-users-card`); e o avatar do atendente no cabeçalho da coluna, na visão Atendentes do Quadro de Atendimentos (`.custom-css-quadro-coluna-atendente`)
- **Valores:** o id do usuário convidado — o papel do `data-operator-id` do operador. No cartão de Usuários, o id da pessoa. No avatar da coluna do Quadro, o id do atendente

### `data-user-profile`

- **Onde:** cartão da pessoa na tela de Usuários (`.custom-css-users-card`), nas duas visões
- **Valores:** o perfil: `admin` · `supervisor` · `user` — o mesmo do chip `.custom-css-users-card-perfil`

### `data-user-section`

- **Onde:** blocos do modal de usuário
- **Valores:** `webphone-widget` · `webphone-nativo`

### `data-user-status`

- **Onde:** o chip de presença no cartão da pessoa, na tela de Usuários (`.custom-css-users-card-presenca`)
- **Valores:** `online` · `offline` · `inactive`

### `data-usuario`

- **Onde:** cada usuário das listas de responsável: o responsável padrão do modelo de projeto (`.custom-css-projeto-modelo-responsavel`), o da regra de projeto da etapa do funil (`.custom-css-crm-regra-projeto-responsavel`) e o da ação "Criar projeto" do Copilot (`.custom-css-copilot-acao-projeto-responsavel`)
- **Valores:** o id do usuário

### `data-usuario-id`

- **Onde:** caixa de seleção de cada pessoa no modal de compartilhar registro
- **Valores:** o id do usuário

### `data-vagas`

- **Onde:** os botões de horário da turma no agendar da equipe (`.custom-css-reservas-reserva-horario`) e na página pública (`.custom-css-reservas-publica-horario`)
- **Valores:** as vagas que sobram naquela sessão (`1`, `2`, `10`...); só na oferta do modo turma

### `data-vagas`

- **Onde:** as vagas da sessão da turma no cartão da agenda (`.custom-css-reservas-agenda-vagas`)
- **Valores:** as vagas que sobram na sessão (`0`, `1`, `2`...), contando as reservas da mesma oferta, do mesmo início e do mesmo recurso

### `data-variacao`

- **Onde:** a última coluna de cada linha da Evolução da Avaliação pela IA: quanto a média mudou entre as duas últimas semanas com avaliação
- **Valores:** a diferença (negativa quando caiu); vazio quando não há duas semanas

### `data-variavel`

- **Onde:** cada resposta nos detalhes da avaliação, no Relatório de Avaliações (`.custom-css-ratings-report-resposta`)
- **Valores:** o nome da variável do fluxo que guardou a resposta (sem os `%`)

### `data-vazia`

- **Onde:** coluna do quadro de atendimentos
- **Valores:** `true` quando a coluna não tem card nenhum · `false`. É o estado que `div:has(> .custom-css-quadro-card)` não consegue casar

### `data-vencido`

- **Onde:** o prazo de cada atendimento na lista do alerta de SLA do Dashboard (`.custom-css-dashboard-lista-sla`)
- **Valores:** `true` (o SLA já venceu) · `false` (ainda vai vencer)

### `data-versao`

- **Onde:** cada versão da prova da arte: no bloco "Prova da arte" da ordem de serviço (`.custom-css-servicos-ordem-prova-versao`) e na página do pedido para o cliente (`.custom-css-servicos-publica-prova`)
- **Valores:** o número da versão (1, 2, 3…): cada novo envio da gráfica é a versão seguinte

### `data-video`

- **Onde:** a janela da chamada
- **Valores:** `true` · `false` — ESTA chamada negociou vídeo (não basta o operador poder)

### `data-view`

- **Onde:** botões de visualização (`.custom-css-view-toggle`) em Tarefas, Oportunidades, Conexões, Equipe, Webhooks, Prompts e Agendamentos
- **Valores:** a visualização que o botão escolhe: `card` · `list` · `calendar` (Tarefas) · `card` · `list` (Oportunidades: cartões ou tabela) · `grid` · `list` (Conexões, Equipe, Webhooks, Prompts) · `month` · `day` · `history` (Agendamentos). Qual está escolhida vai em `aria-pressed="true"`

### `data-visao`

- **Onde:** os botões da visão no topo do Quadro de Atendimentos
- **Valores:** `colunas` (as colunas do quadro) · `tags` · `atendentes` (as de aguardando e uma por atendente)

### `data-visao`

- **Onde:** o ranking entre as lojas, no Ranking do CRM (`.custom-css-crm-ranking-grupos`)
- **Valores:** o que a lista compara: `equipes` · `unidades` · `funis` — o "Ranking por" escolhido (o ranking dos vendedores não usa esta caixa)

### `data-visao`

- **Onde:** o cartão do projeto na página de Projetos (`.custom-css-projetos-cartao`)
- **Valores:** `quadro` · `lista` — o modo em que a página está

### `data-vista`

- **Onde:** a etiqueta "Vista por" de uma aula da IA já vista
- **Valores:** `sim`

### `data-volume`

- **Onde:** botão do som na barra do topo (`[data-appbar="sound"]`)
- **Valores:** o volume das notificações, de `0` (mudo) a `1`, em passos de `0.1` — `[data-volume="0"]` é o som desligado. O mesmo botão diz em `aria-expanded` se o controle está aberto

### `data-webphone`

- **Onde:** botão de chamada na barra de ações
- **Valores:** o modo de webphone do operador

### `data-weekday`

- **Onde:** o cabeçalho de cada dia da semana na grade do mês da Agenda (`.custom-css-agenda-dia-da-semana`)
- **Valores:** a posição na linha: `0` (o primeiro dia mostrado) a `6`

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
