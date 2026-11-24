# Mapa por objetivo: "quero fazer isto" → leia estes artigos

Atalho para os pedidos mais comuns. Os caminhos partem de `references/docs/`. A ordem dos artigos em cada linha é a ordem de leitura sugerida: o primeiro costuma bastar, os outros completam.

Como usar: ache a linha, abra o primeiro artigo, leia o bloco `[RESUMO]` e a seção que responde à pergunta. A coluna **Atenção** traz só o que foi conferido no próprio artigo; ela não substitui a leitura. Se o objetivo não estiver aqui, use `INDICE-recursos.md` e a busca descrita no `SKILL.md`.

Seções: [Começar](#começar) · [Meu perfil e acesso](#meu-perfil-e-acesso) · [Chats](#chats-atendimento-do-dia-a-dia) · [Atendimento automático](#atendimento-automático-e-distribuição) · [Conexões](#conexões-canais) · [Setores & Chatbot](#setores--chatbot) · [Equipe](#equipe-e-permissões) · [Contatos e Tags](#contatos-e-tags) · [Mensagens prontas](#respostas-rápidas-agendamentos-tarefas-e-campanhas) · [CRM](#crm) · [IA](#inteligência-artificial) · [FlowBuilder](#flowbuilder) · [PDV](#pdv) · [Outros módulos](#outros-módulos) · [Consultório e Reservas](#consultório-e-reservas) · [Integrações](#integrações-e-ajustes-técnicos) · [Liberação e revendedor](#liberação-de-recursos-e-revendedor) · [Novidades e suporte](#novidades-e-suporte)

## Começar

| Quero… | Leia | Atenção |
|---|---|---|
| Começar do zero: conectar o WhatsApp, criar setores, cadastrar a equipe | `trilhas/primeiros-passos.md`, `trilhas/visao-geral-do-sistema.md`, `trilhas/adicionar-a-primeira-conexao.md`, `trilhas/vincular-um-setor-a-conexao.md`, `trilhas/definir-equipe-e-permissoes.md` | A trilha pede para seguir nessa ordem. Ela chama o Setor de "Fila" e de "Departamento". |
| Entender ticket, protocolo e os estados Aguardando, Atendendo e Encerrado | `recursos/ticket-x-protocolo.md`, `recursos/aguardando-x-atendendo.md` | "Ticket aberto" quer dizer Aguardando ou Atendendo. Aguardando pode ter robô conversando. |

## Meu perfil e acesso

| Quero… | Leia | Atenção |
|---|---|---|
| Trocar a minha senha ou recuperar a senha esquecida | `recursos/editar-perfil-ou-alterar-senha.md`, `recursos/recuperar-senha.md` | Para trocar a senha de outra pessoa, o caminho é o card dela no menu Equipe: `recursos/acoes-sobre-um-usuario.md`. Quando a plataforma exige senha forte (opção **Exigir senha forte**, que é da instância), a senha nova precisa de no mínimo 8 caracteres, com maiúscula, minúscula, número e caractere especial (`recursos/aba-geral-em-equipe.md`); `recursos/recuperar-senha.md` ainda diz que não há requisito. |
| Achar uma tela do menu pelo nome | `recursos/busca-no-menu.md` | Campo **Buscar no menu…**, no topo do menu lateral. Só acha o que o menu da pessoa já tem: *"Nenhum item do menu com esse nome."* quer dizer que o item não existe para ela, pelo perfil ou pelo que está liberado. |
| Ficar ausente e deixar uma resposta automática | `recursos/status-do-perfil.md`, `recursos/mensagem-de-ausencia.md` | Ausente e Offline não recebem atendimentos do rodízio. |
| Descobrir por que alguém não consegue entrar | `recursos/usuario-nao-consegue-entrar-na-plataforma.md` | O artigo parte da mensagem que aparece na tela da pessoa; peça essa mensagem. Horário de trabalho só barra o perfil User. |

## Chats (atendimento do dia a dia)

| Quero… | Leia | Atenção |
|---|---|---|
| Transferir, devolver ao setor ou encerrar um atendimento | `recursos/transferir-ticket.md`, `recursos/devolver-ao-setor.md`, `recursos/encerrar-ticket.md`, `recursos/aguardando-x-atendendo.md`, `recursos/transferencias-em-configuracoes.md` | O botão de encerrar se chama **Resolver**. Devolver mantém o protocolo; encerrar fecha. |
| Iniciar uma conversa com um cliente | `recursos/novo-chat.md`, `recursos/iniciar-conversa-com-um-contato.md` | Em conexão oficial, fora da janela de 24 horas só sai template: veja `recursos/janela-de-atendimento.md`. |
| Achar um atendimento antigo ou baixar a lista em planilha | `recursos/pesquisar-atendimentos.md` | O menu do painel se chama **Pesquisar**. |
| Encerrar ou transferir muitos atendimentos de uma vez | `recursos/gestao-de-atendimentos.md` | Menu de administradores e supervisores; o atendente não tem o item. |
| Entender um recado vermelho dentro da conversa (erro ao enviar) | `recursos/alertas-vermelhos-no-chat.md`, `recursos/missing-body-in-payload.md` | É o aviso de erro que aparece no meio das mensagens. Os textos vêm em inglês: busque pelo texto exato que apareceu na tela. |
| Entender por que as conversas ficaram com fundo vermelho na lista | `recursos/conexao-desconectada.md`, `recursos/visao-geral-conexoes.md` | `recursos/conexao-desconectada.md` diz que, quando a conexão desconecta, os tickets ficam com fundo vermelho; os passos dele são os de QR Code. `recursos/visao-geral-conexoes.md` cita o "vermelho de conexão caída" sem dizer o canal, e diz que amarelo é conexão pausada. Os artigos da conexão oficial não falam em fundo vermelho. Confirme o canal e siga a linha "Resolver conexão que caiu", em Conexões. |
| Ver os atendimentos em colunas | `recursos/quadro-de-atendimentos.md`, `recursos/visao-geral-quadro-de-atendimentos.md`, `recursos/colunas-do-quadro-de-atendimentos.md`, `recursos/regras-do-quadro-de-atendimentos.md`, `recursos/permissoes-quadro-de-atendimentos.md` | O atendente só vê os quadros atribuídos a ele (causa comum de "tela vazia"). Não é o Kanban de Tags nem o Board do CRM. |
| Fazer videochamada com o cliente e achar as gravações | `recursos/videochamada-com-o-cliente.md`, `recursos/gravacoes-das-chamadas.md` | O artigo avisa que depende do plano da empresa. As gravações das ligações do PABX não ficam em **Gravações**: vão para o menu **Chamadas** (veja a linha das ligações, em Outros módulos). |
| Falar com colegas ou chamar um colega para a conversa | `recursos/chat-interno.md`, `recursos/chamadas-no-chat-interno.md`, `recursos/convidar-operadores-na-conversa.md` | No Chat Interno, só o administrador vê o ícone **Limpar conversas sem mensagens**, que apaga de uma vez as conversas sem nenhuma mensagem e não tem desfazer (`recursos/atualizacoes-2026-11-24.md`). |
| Corrigir uma mensagem já enviada ao cliente | `recursos/editar-mensagem-enviada-ao-cliente.md` | **Editar** fica no menu da mensagem e só aparece quando o canal da conversa permite editar. As versões anteriores ficam visíveis para a equipe. |

## Atendimento automático e distribuição

| Quero… | Leia | Atenção |
|---|---|---|
| Definir horário de atendimento e a mensagem de fora do expediente | `recursos/gerenciamento-de-expediente-em-configuracoes.md`, `recursos/aba-horarios-em-setores-e-chatbot.md`, `recursos/aba-mensagens-em-setores-e-chatbot.md` | A aba **Horários** do Setor só mostra os campos depois de escolher **Gerenciamento Por Setor** em **Gerenciamento de Expediente**, em Configurações › Opções › Geral. O fuso é da empresa inteira (**Fuso horário da empresa**, seção Empresa e região). |
| Encerrar sozinho quem parou de responder, ou mover quem ficou esperando | `recursos/encerrar-por-inatividade.md`, `recursos/mover-apos.md` | Inatividade age no Atendendo; Mover após age no Aguardando. Os dois ficam no cadastro da Conexão. |
| Enviar uma mensagem de despedida ao encerrar | `recursos/mensagem-de-encerramento.md` | Há três cadastros e vale o primeiro preenchido: o do atendente (**Mensagem de Despedida**, em Equipe), o do Setor (**Mensagem de despedida do setor**) e o da Conexão (**Mensagem de conclusão**). A do atendente só funciona se a da Conexão estiver preenchida. Se a despedida é obrigatória ou desligada, decide o campo **Despedida ao encerrar**. |
| Enviar pesquisa de satisfação ao cliente | `recursos/avaliacoes.md`, `recursos/avaliacoes-em-configuracoes.md`, `recursos/bloco-avaliacao-do-atendimento.md`, `recursos/gatilho-via-avaliacao.md` | Não é a `recursos/avaliacao-pela-ia.md`, em que quem dá a nota é a IA. |
| Colocar o nome do cliente, o protocolo e outros dados nas mensagens | `recursos/mustaches.md` | Sintaxe `{{nome_do_código}}`. Dentro do FlowBuilder, as variáveis criadas no fluxo usam `%nome%`: `recursos/bloco-variavel.md`. |
| Dividir os atendimentos entre os atendentes (rodízio) | `recursos/rodizios.md`, `recursos/visao-geral-rodizios.md`, `recursos/bloco-rodizio.md`, `recursos/relatorio-do-rodizio.md`, `recursos/rodizio-de-atendimento.md` | São dois modelos: o menu **Rodízios** com o bloco Rodízio do FlowBuilder, e o rodízio montado com dois Setores no menu do chatbot (último artigo). Pergunte qual a pessoa usa. Para o atendimento esperar a vez no mesmo Setor quando ninguém está disponível, em vez de ir para o transbordo: opção **Aguardar na mesma fila e redistribuir assim que um desocupa**, no cadastro do menu **Rodízios** (`recursos/atualizacoes-2026-11-21.md`; os artigos do rodízio ainda não trazem). |
| Fazer o cliente cair sempre com o mesmo atendente (carteira) | `recursos/carteira-de-clientes.md`, `recursos/contatos-em-configuracoes.md` (seção Carteiras de Clientes) | A carteira é ligada em Configurações › Opções › Contatos, opção **Carteira de Clientes**. |
| Ser avisado no WhatsApp pessoal quando chega cliente, ou responder por ele | `recursos/avise-me.md`, `recursos/siga-me.md` | Avise-me avisa os usuários de um Setor; Siga-me encaminha as conversas do próprio atendente. |

## Conexões (canais)

| Quero… | Leia | Atenção |
|---|---|---|
| Escolher entre WhatsApp oficial e por QR Code | `recursos/whatsapp-oficial-x-nao-oficial.md`, `recursos/entenda-a-api-oficial.md`, `recursos/whatsapp.md` | |
| Conectar um WhatsApp por QR Code | `recursos/adicionar-whatsapp-qrcode.md`, `recursos/adicionar-whatsapp-sem-aparelho-celular.md` | Só QR Code. O segundo artigo é para número sem celular (código por SMS ou ligação). |
| Conectar o WhatsApp Oficial | `recursos/portfolio-empresarial-bm.md`, `recursos/adicionar-whatsapp-oficial.md`, `recursos/trazer-um-numero-da-api-oficial-de-outra-plataforma.md` | Só Oficial. O terceiro artigo vale para número que já está na API Oficial em outra plataforma. |
| Resolver conexão que caiu ou QR Code que não lê | QR Code: `recursos/adicionar-whatsapp-qrcode.md` (seção "Quando a conexão cai"), `recursos/conexao-desconectada.md`, `recursos/conexao-nao-le-o-qr-code.md`. Oficial: `recursos/verificar-agora-e-reconectar.md`, `recursos/avisos-da-meta-na-conexao.md` | Cada canal tem o seu procedimento. No QR Code os dois primeiros artigos divergem: um manda **Reconectar**, depois **Novo QR**, e **Excluir Sessão** só se os dois não resolverem; o outro começa por **Excluir Sessão**, depois **Reiniciar Conexões** e **Ver QR Code**. Apresente os dois, começando pelo que não apaga a sessão. Na oficial o artigo pede para não excluir a conexão para "conectar de novo". |
| Entender por que o número foi bloqueado ou restrito | `recursos/numero-bloqueado-no-whatsapp.md` | O artigo separa canal não oficial e canal oficial: mantenha a separação. O artigo do revendedor (`revendedor/trilhas/bloqueio-whatsapp.md`) não separa e traz só o pedido feito pelo aplicativo, no aparelho do número. Sobre onde pedir o desbloqueio do número oficial, as duas documentações divergem: diga isso, sem afirmar um dos lados. |
| Entender a janela de 24 horas e os templates | `recursos/janela-de-atendimento.md`, `recursos/mensagem-template.md`, `recursos/whatsapp-oficial-gestao-de-templates.md` | Só Oficial. A tela Gestão de Templates abre pelo card da conexão, não pelo menu lateral. Redigir o template é da skill `cmv-mensagens`. |
| Criar um template ou entender por que foi recusado, pausado ou desabilitado | `recursos/criar-template-pela-plataforma.md`, `recursos/criar-template-no-gerenciador-do-whatsapp.md`, `recursos/template-recusado-pausado-ou-desabilitado.md` | Só Oficial. O botão **NOVO TEMPLATE** fica na **Gestão de Templates**. |
| Cadastrar o cartão da Meta, trocar o nome de exibição ou dar acesso à conta da Meta | `recursos/forma-de-pagamento-do-whatsapp-oficial.md`, `recursos/nome-de-exibicao-do-whatsapp-oficial.md`, `recursos/administradores-da-conta-na-meta.md` | Só Oficial. Os três são feitos na conta da empresa na Meta, não na plataforma. Sem forma de pagamento, o número não envia template. |
| Entender mensagem do Oficial não entregue, qualidade do número ou limite de envio | `recursos/erros-de-entrega-do-whatsapp-oficial.md`, `recursos/qualidade-do-numero-e-limite-de-envio.md` | Só Oficial. O botão **Erros de template**, no card da conexão, lista os templates recusados no envio, com o código da Meta. Responder quem escreveu primeiro não conta no limite de envio. |
| Gastar menos com a cobrança do WhatsApp Oficial | `trilhas/a-cobranca-do-whatsapp-oficial-mudou.md`, `recursos/limitador-de-mensagens.md`, `recursos/concatenador-de-mensagens.md`, `recursos/whatsapp-modo-hibrido-oficial-e-qrcode.md`, `recursos/modo-alternativo-chat-externo-por-link.md` | Valores e datas da cobrança são da Meta: repita só o que o artigo diz. O Limitador só informa, não bloqueia envio. |
| Atender o Instagram (Direct e comentários) | `recursos/instagram.md`, `recursos/direct.md`, `recursos/comentarios.md`, `recursos/automacao-eu-quero.md`, `recursos/posts-do-instagram.md`, `recursos/gatilho-via-comentario-do-instagram.md` | A conta precisa ser Instagram Business. |
| Conectar Facebook Messenger ou Telegram | `recursos/facebook-messenger.md`, `outros/telegram.md` | O artigo do Telegram fica em `outros/`, fora do índice de recursos. |
| Colocar um chat no meu site | `recursos/web-chat.md`, `recursos/chat-externo.md` | São coisas diferentes: Web Chat é um código colado no site; Chat Externo é uma página aberta por link. Nenhum dos dois é o Modo Alternativo. |
| Trocar de conexão ou de número sem perder o histórico | `recursos/como-migrar-conexoes.md` | Migre antes de excluir a conexão antiga. No WhatsApp por QR Code, o botão **Clonar conexão** do card cria a nova, leva os atendimentos e apaga a antiga numa ação só. |
| Receber (ou parar de receber) grupos do WhatsApp | `recursos/gerenciamento-de-grupos-em-configuracoes.md` | São até três travas, e basta uma bloqueando para o grupo não entrar. Duas são do administrador: a da empresa (**Ignorar Mensagens de Grupos**, em Configurações › Opções › Atendimento) e o **Bloquear Grupos** de cada Conexão. A terceira é o **Bloquear Grupos** do cadastro da empresa, que é do Super Admin (`revendedor/recursos/como-habilitar-grupos.md`, `revendedor/recursos/configuracoes-editar-empresa.md`). Cada documentação conta só duas: se as duas do administrador estão liberadas e o grupo não entra, a terceira se confere com quem fornece a plataforma. O Setor em que os grupos entram em Aguardando é o **Setor padrão para grupos**, na aba **Setores & Tempos** da Conexão, e cada pessoa só vê os grupos das Conexões que pode atender (`recursos/atualizacoes-2026-11-20.md`). Se todos do Setor veem o grupo atribuído a um colega, decide a opção **Operador vê os grupos do setor atribuídos a outros?**, em Configurações › Opções, filtro Atendimento (`recursos/atualizacoes-2026-11-24.md`). |

## Setores & Chatbot

| Quero… | Leia | Atenção |
|---|---|---|
| Criar e organizar setores | `recursos/setores-e-chatbot.md`, `recursos/visao-geral-setores-e-chatbot.md`, `recursos/aba-geral-em-setores-e-chatbot.md`, `recursos/categorias-de-setores.md` | Depois de criar, marque o Setor na Conexão (aba Setores & Tempos), senão a conversa não aparece para a equipe. |
| Mandar um menu inicial para o cliente escolher o setor | `recursos/chatbot-e-menu-de-setores-na-conexao.md` | O menu nasce de marcar vários Setores na mesma Conexão; a ordem vem da **Ordenação do BOT**. |
| Fazer um fluxo atender toda conversa que chega | `recursos/setor-unico-com-fluxo-automatico.md`, `recursos/gatilho-via-conexao.md` | Desenhar o fluxo é da skill `cmv-flowbuilder`. |

## Equipe e permissões

| Quero… | Leia | Atenção |
|---|---|---|
| Cadastrar um atendente e dizer em quais setores ele atende | `recursos/aba-geral-em-equipe.md`, `recursos/aba-setores-e-conexoes-em-equipe.md`, `recursos/atendimento-e-operador-em-configuracoes.md`, `recursos/tipos-de-perfil.md`, `recursos/aba-permissoes-em-equipe.md` | O menu Equipe é só do administrador. O cadastro novo já vem com o perfil **User**, que não tem Configurações, Equipe nem Conexões no menu. Sem Setor marcado a pessoa não vê conversa; mas marcar o Setor não define o que ela vê dentro dele: isso é a opção **Operador Acessa Todos os Atendimentos do Setor?**, em Configurações › Opções › Atendimento, seção Atendimento e operador, que vale para todos os atendentes da empresa (Sim: todos os do Setor; Não: só os dela). **Acesso Limitado** em SIM deixa o menu só com Chats, e a trilha `trilhas/controlar-o-que-o-atendente-enxerga.md` avisa que a pessoa perde também a capacidade de iniciar um atendimento. Para tirar só o início de atendimentos, sem cortar o menu: **Pode iniciar novos atendimentos** em **NÃO**, na aba **Permissões** do cadastro. |
| Saber o que cada perfil vê, ou esconder algo do atendente | `recursos/tipos-de-perfil.md`, `recursos/aba-permissoes-em-equipe.md`, `recursos/atendimento-e-operador-em-configuracoes.md`, `trilhas/controlar-o-que-o-atendente-enxerga.md` | Por pessoa: aba Permissões do cadastro. Para todos os atendentes: Configurações › Opções › Atendimento, seção Atendimento e operador (importar e exportar contatos fica na aba Contatos). |
| Limitar quantos atendimentos cada pessoa pega ao mesmo tempo | `recursos/limite-de-atendimentos-simultaneos.md` | |
| Desligar alguém da equipe sem perder os atendimentos | `recursos/acoes-sobre-um-usuario.md` | Ordem do artigo: transferir tickets e carteira, depois inativar; excluir é o último recurso. Essas ações não têm desfazer. |
| Auditar quem fez o quê e reforçar a segurança do acesso | `recursos/registro-de-atividades.md`, `recursos/logs-e-monitoramento-em-configuracoes.md`, `recursos/seguranca-em-configuracoes.md` | **Habilitar 2FA na empresa** só libera a autenticação em dois fatores; cada usuário configura a própria. |

## Contatos e Tags

| Quero… | Leia | Atenção |
|---|---|---|
| Importar ou exportar contatos | `recursos/importar-contatos-planilha.md`, `recursos/importar-contatos-telefone.md`, `recursos/exportar-contatos.md` | Número só com dígitos, no formato DDI DDD NÚMERO. Importar contatos novos e atualizar contatos são procedimentos diferentes. |
| Cadastrar, editar, bloquear contato ou criar campos extras | `recursos/adicionar-contato.md`, `recursos/editar-contato.md`, `recursos/bloquear-contato.md`, `recursos/contatos-em-configuracoes.md` | Não é permitido alterar o telefone do contato. Excluir o contato remove os atendimentos dele (`recursos/excluir-contato.md`). |
| Criar tags e entender os tipos | `outros/adicionar-tag.md`, `outros/tipos-de-tags.md`, `recursos/tags-de-atendimento.md`, `recursos/tags-de-encerramento.md`, `recursos/tags-de-crm.md` | Os dois primeiros ficam em `outros/`. Atendimento liga ao ticket, Encerramento ao protocolo, CRM à oportunidade. |
| Organizar atendimentos em um kanban de tags | `recursos/kanban-de-tags.md`, `recursos/quadro-de-atendimentos-por-tags.md` | Só tag do tipo Atendimento entra no Kanban de Tags. O segundo artigo é a visão por Tags do Quadro de atendimentos, outra tela. |
| Exigir o motivo do encerramento e registrar a venda | `recursos/tags-de-encerramento.md`, `recursos/encerrar-ticket.md` | O **Motivo de Encerramento Obrigatório** é ligado por Setor. |
| Disparar um fluxo ou um evento de Pixel quando uma tag é marcada | `recursos/remarketing-em-tags.md`, `recursos/gatilho-via-remarketing-de-tag.md`, `recursos/pixel-meta-em-tags.md` | |
| Medir no Pixel da Meta e no Google Analytics as visitas às páginas públicas da empresa (cardápio, loja, link na bio, reservas, link de agendamento, rastreio do pedido) | `recursos/pixel-da-meta-e-google-analytics-nas-paginas-externas.md` | Um ID do pixel e um ID de métricas valem para todas as páginas externas; cada página pode ficar de fora. |

## Respostas rápidas, agendamentos, tarefas e campanhas

| Quero… | Leia | Atenção |
|---|---|---|
| Criar respostas rápidas (texto, mídia, fluxo) | `recursos/visao-geral-respostas-rapidas.md`, `recursos/resposta-rapida-envio-de-texto.md`, `recursos/resposta-rapida-envio-de-midia.md`, `recursos/resposta-rapida-de-fluxo.md`, `recursos/gerenciador-de-arquivos.md` | A opção **Global** é só para Admin; a resposta rápida de fluxo só é cadastrada por administradores. O "/" da conversa acha a resposta pelo texto todo ou só pelo começo do atalho, conforme o campo **Busca das respostas rápidas** do cadastro da pessoa (Equipe › editar a pessoa › aba Permissões): com **Só pelo começo do atalho**, a lista fica vazia, sem aviso, quando o termo está no meio do atalho ou na mensagem. Redigir os textos é da skill `cmv-mensagens`. |
| Agendar uma mensagem para depois | `recursos/adicionar-agendamento.md`, `recursos/visao-geral-agendamentos.md` | Com conexão de API Oficial, o agendamento exige um template aprovado. |
| Deixar o cliente marcar uma reunião sozinho | `recursos/links-de-agendamento.md` | Não é o menu Agendamentos (mensagem programada). O menu **Links de agendamento** é do administrador; a reunião marcada entra nas **Tarefas** de quem atende. Cada faixa de horário pode ter o seu local, presencial com endereço ou online: seção **Locais de atendimento**, na janela **Editar link** (`recursos/atualizacoes-2026-11-24.md`; o artigo do recurso ainda não traz). |
| Criar e acompanhar tarefas | `recursos/adicionar-tarefa.md`, `recursos/adicionar-tarefa-ao-ticket.md`, `recursos/visao-geral-tarefas.md` | |
| Avisar o cliente pelo WhatsApp sobre uma tarefa ou um projeto | `recursos/avisos-ao-cliente-em-tarefas.md`, `recursos/avisos-ao-cliente-em-projetos.md` | Nas Tarefas, o administrador escreve os textos uma vez e cada tarefa escolhe se avisa o cliente. |
| Fazer uma campanha (envio em massa) por QR Code | `recursos/campanhas.md`, `recursos/configurar-campanhas.md`, `recursos/fontes-de-contatos-para-campanhas.md`, `recursos/nova-campanha.md` | O artigo avisa do risco de bloqueio do chip. A Lista de Contato da campanha não é o menu Contatos. |
| Fazer uma campanha pela API Oficial | `recursos/nova-campanha-api-oficial.md`, `recursos/mensagem-template.md` | Artigo próprio, de título quase igual ao anterior. Uma conexão só; não usar Gatilho, Caracteres Ocultos nem Mensagem de Descadastramento. |
| Enviar e-mail em massa (Mail Marketing) | `recursos/mail-marketing.md`, `recursos/visao-geral-mail-marketing.md`, `recursos/listas-de-envio-do-mail-marketing.md`, `recursos/campanhas-de-e-mail.md`, `recursos/configuracoes-do-mail-marketing.md`, `recursos/permissoes-mail-marketing.md` | É à parte das Campanhas. Envia por uma conta de e-mail da empresa (`recursos/contas-de-e-mail.md`). Menu do administrador e do supervisor; a aba **Configurações** do módulo, só o administrador altera. |

## CRM

| Quero… | Leia | Atenção |
|---|---|---|
| Montar o CRM (funis, etapas, cadastros, produtos) | `recursos/visao-geral-do-crm.md`, `recursos/criar-e-editar-funil.md`, `recursos/etapas-do-funil.md`, `recursos/quem-acessa-o-funil.md`, `recursos/cadastros-do-crm.md`, `recursos/produtos-do-crm.md` | Administrador e supervisor criam funis e cadastros; **Quem acessa** é só do administrador. |
| Criar e acompanhar uma oportunidade, e gerar proposta | `recursos/criar-oportunidade.md`, `recursos/nova-oportunidade.md`, `recursos/board-de-oportunidades.md`, `recursos/ganhar-perder-e-devolver-oportunidade-ao-funil.md`, `recursos/gerar-e-enviar-proposta.md` | `recursos/nova-oportunidade.md` é o botão dentro da conversa (ou o do card **Oportunidades**, no painel do contato); `recursos/criar-oportunidade.md` é pelo Board. |
| Descobrir por que o vendedor abre o Board e não vê nada | `recursos/quem-visualiza-o-que-no-crm.md`, `recursos/quem-acessa-o-funil.md` | Atendente e supervisor só veem os funis liberados para eles. |
| Ver relatórios, ranking e metas de vendas | `recursos/relatorio-de-vendas.md`, `recursos/ranking-de-vendas.md`, `recursos/minha-evolucao.md`, `recursos/leads-de-anuncio.md` | Leads de anúncio é de administrador e supervisor. O Ranking, para o atendente, depende de **Pode ver o Ranking (CRM)**, na aba Permissões do cadastro. |

## Inteligência Artificial

| Quero… | Leia | Atenção |
|---|---|---|
| Ligar a IA na plataforma | `recursos/pre-requisitos-ia.md`, `recursos/token-openai.md`, `recursos/provedor-de-ia.md`, `recursos/atualizacoes-2026-11-11.md` (seção "IA pelo provedor escolhido") | O pré-requisito é a chave da OpenAI, colada no campo **Token OpenAI** do card **OPEN.AI**, no menu **Integrações**; se o card avisar que a conta usa a chave da plataforma, não há chave a cadastrar. Outro serviço de IA se escolhe no card **Provedor de IA**. |
| Colocar um assistente de IA para responder clientes | `recursos/gpt-assistant.md`, `recursos/tipo-prompt.md`, `recursos/base-de-conhecimento-do-gpt-assistant.md`, `recursos/comandos-gpt-assistant.md`, `recursos/bloco-gpt-assistant-openai.md` | Escrever o prompt é da skill `cmv-agente-ia`. O tipo **Agente OpenAI** aparece desativado e não funciona mais; o tipo é **Prompt**. A **Base de Conhecimento** guarda horários, preços e políticas e é vinculada ao prompt. |
| Usar a IA para ajudar o atendente e avaliar atendimentos | `recursos/copiloto-de-mensagens.md`, `recursos/sugestao-de-resposta-ia.md`, `recursos/transcrever-audios.md`, `recursos/analise-de-atendimento.md`, `recursos/avaliacao-pela-ia.md` | A opção de Avaliação pela IA é só do administrador. |
| Ligar e acompanhar a Avaliação pela IA | `recursos/como-ligar-a-avaliacao-pela-ia.md`, `recursos/visao-geral-avaliacao-pela-ia.md`, `recursos/processos-de-atendimento-da-avaliacao-pela-ia.md`, `recursos/aba-hoje-da-avaliacao-pela-ia.md`, `recursos/aulas-da-avaliacao-pela-ia.md`, `recursos/relatorio-da-avaliacao-pela-ia.md`, `recursos/alertas-da-avaliacao-pela-ia.md`, `recursos/permissoes-avaliacao-pela-ia.md` | Liga em Configurações › Opções › Automação, seção Avaliações (**Avaliar os atendimentos pela IA**), só o administrador. O atendente vê só as próprias aulas. |
| Perguntar à IA sobre os números da plataforma | `recursos/assistente-de-ia.md`, `recursos/crm-no-assistente-de-ia.md`, `recursos/reservas-no-assistente-de-ia.md`, `recursos/vendas-perdidas-no-assistente-de-ia.md` | O **Assistente de IA** só consulta, não muda nada, e responde só com o que quem pergunta já tem acesso. Não é o GPT Assistant, que responde clientes. |

## FlowBuilder

| Quero… | Leia | Atenção |
|---|---|---|
| Criar o primeiro fluxo de chatbot | `recursos/flowbuilder.md`, `recursos/visao-geral-flowbuilder.md`, `recursos/como-usar-o-editor-de-fluxos.md`, `recursos/blocos.md`, `recursos/automacoes-rapidas.md` | No painel o menu se chama **FlowBuilder Nativo** e é do administrador. Para desenhar ou gerar o fluxo, use a skill `cmv-flowbuilder`. |
| Descobrir por que o fluxo não responde ou para no meio | `recursos/pontos-de-entrada.md`, `recursos/como-o-fluxo-roda.md`, `recursos/verificar-e-resumo-do-fluxo.md`, `recursos/erros-do-fluxo.md` | Fluxo que não está ligado a um ponto de entrada não atende ninguém. |

## PDV

| Quero… | Leia | Atenção |
|---|---|---|
| Começar a vender pelo PDV | `recursos/visao-geral-pdv.md`, `recursos/produtos-e-estoque-do-pdv.md`, `recursos/caixa-do-pdv.md`, `recursos/pedido-na-conversa.md`, `recursos/venda-no-balcao.md`, `recursos/permissoes-pdv.md` | As Opções do PDV ficam em Configurações › Opções › Vendas, seção PDV, que só o administrador abre (`recursos/opcoes-do-pdv.md`). |
| Montar cardápio digital, loja digital ou mesas | `recursos/cardapio-digital.md`, `recursos/loja-digital.md`, `recursos/mesas-e-comandas.md`, `recursos/painel-de-pedidos.md`, `recursos/entregas-e-entregadores.md` | Cardápio e Loja são montados só pelo administrador. |
| Dividir o preparo entre cozinha e bar, ou consultar o histórico de um cliente | `recursos/setores-de-producao-do-pdv.md`, `recursos/clientes-do-pdv.md` | Com setores de produção, cada tela do **Painel de Pedidos** mostra só os itens do seu setor. |
| Reservar mesa, fechar a conta da mesa ou cadastrar garçom | `recursos/reservas-de-mesa.md`, `recursos/conta-da-mesa.md`, `recursos/perfil-garcom-e-comissao.md` | Reservas de mesa são do PDV, não o módulo Reservas. |
| Receber pagamento online no pedido | `recursos/pagamentos-do-pedido.md`, `recursos/token-asaas.md`, `recursos/access-token-mercado-pago.md`, `recursos/token-pagseguro-pagbank.md`, `recursos/credenciais-paggpix.md` | Os campos das credenciais são só do administrador. |

## Outros módulos

| Quero… | Leia | Atenção |
|---|---|---|
| Acompanhar os números do atendimento (Dashboard) | `recursos/dashboard.md`, `recursos/visao-geral-dashboard.md`, `recursos/filtros-do-dashboard.md`, `recursos/metas-e-limites-do-dashboard.md`, `recursos/permissoes-dashboard.md`, `recursos/meus-numeros-do-atendente.md` | Tela do administrador e do supervisor. O atendente só tem **Meus números**, se o administrador ligar **Atendente vê os próprios números**, em Configurações › Opções › Atendimento. O filtro de conexão fica guardado no navegador. O **Dashboard (legado)** conta diferente: não compare um com o outro. |
| Receber os números ou os alertas do Dashboard por e-mail e WhatsApp | `recursos/resumo-automatico-do-dashboard.md`, `recursos/aviso-dos-alertas-do-dashboard.md` | |
| Atender e-mails dentro da plataforma | `recursos/e-mails.md`, `recursos/contas-de-e-mail.md`, `recursos/visao-geral-e-mails.md`, `recursos/permissoes-e-mails.md` | O menu Contas de E-mail é só do administrador. |
| Enviar e-mail de dentro de um fluxo (confirmação ao cliente, aviso à equipe) | `recursos/bloco-enviar-e-mail.md`, `recursos/provedores-de-envio-de-e-mail-por-api.md`, `recursos/contas-de-e-mail.md` | O bloco envia por uma conta de e-mail ou por um provedor de envio por API; o e-mail não aparece na conversa. |
| Fazer e receber ligações (VoIP, PABX) | `recursos/entendendo-voip.md`, `recursos/entendendo-pabx.md`, `recursos/pabx-ramais.md`, `recursos/pabx-ligacao-voip.md`, `recursos/pabx-ligacao-whatsapp-qr-code.md`, `recursos/pabx-whatsapp-oficial.md`, `recursos/aba-voip-chamadas-em-equipe.md` | Há um artigo de PABX para WhatsApp por QR Code e outro para WhatsApp Oficial. As gravações das ligações do PABX aparecem no menu **Chamadas**, não no **Gravações** (`recursos/gravacoes-das-chamadas.md` é outro recurso). O envio delas é configurado no sistema de PABX (`revendedor/recursos/como-habilitar-gravacoes-no-pabx.md`), e a Central não tem artigo de uso do menu **Chamadas**. |
| Organizar entregas depois da venda (Projetos) | `recursos/projetos.md`, `recursos/visao-geral-projetos.md`, `recursos/modelos-de-projeto.md`, `recursos/criar-um-projeto.md`, `recursos/projeto-criado-ao-ganhar-a-venda.md`, `recursos/permissoes-projetos.md` | |
| Criar links rastreáveis ou uma página de links | `recursos/adicionar-link.md`, `recursos/relatorio-do-link.md`, `recursos/link-na-bio.md` | O menu Link na Bio é só do administrador. |

## Consultório e Reservas

| Quero… | Leia | Atenção |
|---|---|---|
| Montar o Consultório (profissionais, serviços, salas) | `recursos/consultorio.md`, `recursos/visao-geral-consultorio.md`, `recursos/permissoes-consultorio.md`, `recursos/aba-profissionais-em-cadastros-do-consultorio.md`, `recursos/aba-servicos-em-cadastros-do-consultorio.md`, `recursos/aba-salas-em-cadastros-do-consultorio.md` | Só o administrador salva nos **Cadastros do consultório**. Só quem está cadastrado como profissional tem agenda e lê o prontuário. |
| Marcar, confirmar e receber consultas, inclusive por vídeo | `recursos/agenda-do-consultorio.md`, `recursos/aba-confirmacao-em-cadastros-do-consultorio.md`, `recursos/recepcao-do-consultorio.md`, `recursos/consultorio-no-atendimento.md`, `recursos/teleconsulta.md` | A agenda não deixa marcar dois pacientes no mesmo horário com o mesmo profissional. |
| Usar o prontuário, documentos e receitas | `recursos/prontuario-do-paciente.md`, `recursos/aba-prontuario-em-cadastros-do-consultorio.md`, `recursos/documentos-e-receitas-do-consultorio.md` | O prontuário usa uma chave criada uma vez, a partir de uma frase que a plataforma não guarda. Sem a chave, ninguém registra no prontuário. |
| Montar as Reservas (o que é reservado, horários, página) | `recursos/reservas.md`, `recursos/visao-geral-reservas.md`, `recursos/permissoes-reservas.md`, `recursos/aba-recursos-em-reservas.md`, `recursos/aba-ofertas-em-reservas.md`, `recursos/aba-horarios-em-reservas.md`, `recursos/aba-pagina-em-reservas.md` | Recurso é quem ou o que recebe a reserva; oferta é o que o cliente escolhe. Montar as Reservas é do administrador. Não é a Reserva de mesa do PDV. |
| Reservar pela agenda, pela página do cliente ou pelo fluxo | `recursos/agenda-de-reservas.md`, `recursos/pagina-de-reservas-do-cliente.md`, `recursos/reservas-agendar-no-fluxo.md`, `recursos/aba-avisos-em-reservas.md` | Os avisos ao cliente começam desligados. |
| Reservar por diária, em turma ou com repetição, lista de espera e pagamento | `recursos/reservas-por-diaria.md`, `recursos/reservas-em-turma.md`, `recursos/reservas-que-se-repetem.md`, `recursos/lista-de-espera-das-reservas.md`, `recursos/pagamento-da-reserva.md`, `recursos/pacotes-dos-clientes-nas-reservas.md` | |

## Integrações e ajustes técnicos

| Quero… | Leia | Atenção |
|---|---|---|
| Achar tokens, webhooks e a ligação com o n8n | `recursos/token-da-conexao.md`, `recursos/token-da-empresa-em-configuracoes.md`, `recursos/webhooks-e-integracoes-em-configuracoes.md`, `recursos/n8n-via-webhook.md`, `recursos/n8n-via-flowbuilder.md`, `recursos/api-nao-funciona.md` | Aqui só está onde cada coisa fica no painel. Endpoints, payloads e código são da skill `cmv-api`. |
| Mostrar o atendimento dentro de outro sistema | `recursos/incorporar-atendimento-em-outro-sistema.md` | |
| Guardar os arquivos num armazenamento próprio | `recursos/armazenamento-remoto-de-arquivos.md`, `recursos/cloudflare-r2-em-armazenamento-remoto.md`, `recursos/hetzner-object-storage-em-armazenamento-remoto.md` | |
| Usar no celular e receber notificações | `recursos/aplicativo.md`, `recursos/como-instalar-o-pwa.md`, `recursos/notificacoes-push.md` | É um PWA: instalado pelo navegador, sem loja de aplicativos. |
| Resolver tela desatualizada ou recurso novo que não aparece | `recursos/como-atualizar-o-cache.md` | |

## Liberação de recursos e revendedor

As três últimas linhas são para o revendedor (Super Admin, dono da instância): o cliente de uma empresa não tem essas telas. Veja "Cliente ou revendedor", no `SKILL.md`.

| Quero… | Leia | Atenção |
|---|---|---|
| Descobrir por que um menu ou recurso não aparece nem para o administrador | `references/liberar-recursos.md`, `recursos/tipos-de-perfil.md` | O que o plano não libera não aparece para ninguém. Diga ao cliente o nome da opção que libera o recurso e que quem liga é quem fornece a plataforma. Preços não estão documentados. |
| Liberar um recurso ou um canal para uma empresa (revendedor) | `references/liberar-recursos.md`, `revendedor/recursos/como-habilitar.md`, `revendedor/recursos/configuracoes-planos.md`, `revendedor/recursos/configuracoes-editar-empresa.md` | Há um artigo `revendedor/recursos/como-habilitar-*.md` por recurso. Depois de mudar o plano, quem estava com a plataforma aberta precisa recarregar a página. |
| Administrar a instância: empresas, planos, marca, cores, logotipos, créditos de IA (revendedor) | `revendedor/recursos/configuracoes.md`, `revendedor/recursos/plataforma-em-configuracoes.md`, `revendedor/recursos/configuracoes-empresas.md`, `revendedor/recursos/configuracoes-cores.md`, `revendedor/recursos/configuracoes-logotipos-icones.md`, `revendedor/recursos/configuracoes-tokens-de-ia.md` | O que está no card **Plataforma** vale para todas as empresas, sem versão por empresa. Logotipo é da instância. As APIs administrativas são da skill `cmv-api`; CSS e JS, da `cmv-painel-css-js`. |
| Oferecer a API Oficial com aplicativo próprio na Meta (revendedor) | `revendedor/trilhas/meta.md`, `revendedor/trilhas/api-oficial-nativa.md`, `revendedor/trilhas/tech-provider.md`, `revendedor/trilhas/publicar-o-app-e-ligar-na-plataforma.md`, `revendedor/recursos/como-habilitar-api-oficial-nativa-whitelabel.md` | No plano, o aplicativo próprio é **WABA WL** e o da plataforma é **WABA INC**; não se habilitam os dois na mesma instância. |

## Novidades e suporte

| Quero… | Leia | Atenção |
|---|---|---|
| Saber o que mudou na plataforma | `recursos/atualizacoes.md`, `recursos/atualizacoes-2026-11.md`, `recursos/atualizacoes-2026-10.md` | Cada dia é um arquivo `recursos/atualizacoes-AAAA-MM-DD.md`, que costuma trazer Novidades, Melhorias, Correções e "O que você precisa fazer". |
| Ver um vídeo tutorial | `videos.md` | Só há título, link e uma linha de descrição; o conteúdo dos vídeos não foi transcrito. |
| Falar com o suporte | `recursos/contato-para-suporte.md` | |
