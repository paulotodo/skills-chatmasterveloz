# Endpoints da API (233)

Uma linha por artigo que declara um endpoint, em ordem de endereço. Os artigos da categoria APIs que não estão aqui são conceituais (webhooks, autenticação, exemplos).

| Método | Endpoint | Artigo |
|---|---|---|
| GET | `https://api2.chatmasterveloz.com/api/anuncios/leads?anuncioId={anuncioId}&dataInicio={dataInicio}&dataFim={dataFim}` | [API Listar Leads por Anúncio](api/api-listar-leads-por-anuncio.md) |
| GET | `https://api2.chatmasterveloz.com/api/anuncios?dataInicio={dataInicio}&dataFim={dataFim}` | [API Relatório de Anúncios](api/api-relatorio-de-anuncios.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-externo/enviar-link` | [API Modo Alternativo Enviar Link](api/api-modo-alternativo-enviar-link.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-externo/mensagem` | [API Modo Alternativo Mensagem de Texto](api/api-modo-alternativo-mensagem-de-texto.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-externo/mensagem` | [API Chat Externo Mensagem de Lista](api/api-chat-externo-mensagem-de-lista.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-externo/mensagem` | [API Chat Externo Mensagem de Texto](api/api-chat-externo-mensagem-de-texto.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-externo/mensagem` | [API Chat Externo Botão Quick Reply](api/api-chat-externo-botao-quick-reply.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-externo/midia` | [API Modo Alternativo Enviar Arquivo por URL](api/api-modo-alternativo-enviar-arquivo-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-externo/midia` | [API Chat Externo Enviar Arquivo por URL](api/api-chat-externo-enviar-arquivo-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-externo/midia` | [API Modo Alternativo Enviar Arquivo](api/api-modo-alternativo-enviar-arquivo.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-externo/midia` | [API Chat Externo Enviar Arquivo](api/api-chat-externo-enviar-arquivo.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-interno/chats` | [API Criar Conversa no Chat Interno](api/api-criar-conversa-no-chat-interno.md) |
| GET | `https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}` | [API Obter uma Conversa do Chat Interno](api/api-obter-uma-conversa-do-chat-interno.md) |
| PUT | `https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}` | [API Atualizar Conversa do Chat Interno](api/api-atualizar-conversa-do-chat-interno.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/audios` | [API Enviar Áudio no Chat Interno](api/api-enviar-audio-no-chat-interno.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/files` | [API Enviar Arquivo no Chat Interno](api/api-enviar-arquivo-no-chat-interno.md) |
| POST | `https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/messages` | [API Enviar Mensagem no Chat Interno](api/api-enviar-mensagem-no-chat-interno.md) |
| GET | `https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/messages?pageNumber={pageNumber}` | [API Listar Mensagens do Chat Interno](api/api-listar-mensagens-do-chat-interno.md) |
| GET | `https://api2.chatmasterveloz.com/api/chat-interno/chats?userId={userId}&pageNumber={pageNumber}` | [API Listar Conversas do Chat Interno](api/api-listar-conversas-do-chat-interno.md) |
| GET | `https://api2.chatmasterveloz.com/api/companies/{companyId}/campaign-settings` | [API Listar Configurações de Campanha](api/api-listar-configuracoes-de-campanha.md) |
| PUT | `https://api2.chatmasterveloz.com/api/companies/{companyId}/campaign-settings` | [API Atualizar Configurações de Campanha](api/api-atualizar-configuracoes-de-campanha.md) |
| GET | `https://api2.chatmasterveloz.com/api/companies/{companyId}/settings` | [API Listar Configurações da Empresa](api/api-listar-configuracoes-da-empresa.md) |
| PUT | `https://api2.chatmasterveloz.com/api/companies/{companyId}/settings` | [API Atualizar Configurações da Empresa](api/api-atualizar-configuracoes-da-empresa.md) |
| GET | `https://api2.chatmasterveloz.com/api/company/queues` | [API Listar Setores da Empresa](api/api-listar-setores-da-empresa.md) |
| GET | `https://api2.chatmasterveloz.com/api/company/users` | [API Listar Usuários da Empresa](api/api-listar-usuarios-da-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/contact/update` | [API Atualizar Contato](api/api-atualizar-contato.md) |
| POST | `https://api2.chatmasterveloz.com/api/contacts` | [API Criar Contato](api/api-criar-contato.md) |
| GET | `https://api2.chatmasterveloz.com/api/contacts/all` | [API Listar Contatos](api/api-listar-contatos.md) |
| GET | `https://api2.chatmasterveloz.com/api/contacts/alltickets` | [API Listar Tickets do Contato](api/api-listar-tickets-do-contato.md) |
| POST | `https://api2.chatmasterveloz.com/api/contacts/changecarteira` | [API Transferir Carteira de Clientes](api/api-transferir-carteira-de-clientes.md) |
| GET | `https://api2.chatmasterveloz.com/api/contacts/findbytag` | [API Listar Tickets por Tag](api/api-listar-contatos-por-tag.md) |
| GET | `https://api2.chatmasterveloz.com/api/contacts/single` | [API Obter um Contato](api/api-obter-um-contato.md) |
| POST | `https://api2.chatmasterveloz.com/api/contactswv` | [API Criar Contato (com validação)](api/api-criar-contato-com-validacao.md) |
| GET | `https://api2.chatmasterveloz.com/api/crm/v2/funis` | [API Listar Funis](api/api-listar-funis.md) |
| GET | `https://api2.chatmasterveloz.com/api/crm/v2/motivos-perda` | [API Listar Motivos de Perda](api/api-listar-motivos-de-perda.md) |
| POST | `https://api2.chatmasterveloz.com/api/crm/v2/oportunidades` | [API Criar Oportunidade](api/api-criar-oportunidade.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}` | [API Deletar Oportunidade](api/api-deletar-oportunidade.md) |
| GET | `https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}` | [API Obter uma Oportunidade](api/api-obter-uma-oportunidade.md) |
| PUT | `https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}` | [API Atualizar Oportunidade](api/api-atualizar-oportunidade.md) |
| PUT | `https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}/mover` | [API Mover Oportunidade de Raia](api/api-mover-oportunidade-de-raia.md) |
| GET | `https://api2.chatmasterveloz.com/api/crm/v2/oportunidades?status={statusDaOportunidade}&pageNumber={pageNumber}&pageSize={pageSize}` | [API Listar Oportunidades](api/api-listar-oportunidades.md) |
| GET | `https://api2.chatmasterveloz.com/api/crm/v2/origens` | [API Listar Origens de Venda](api/api-listar-origens-de-venda.md) |
| GET | `https://api2.chatmasterveloz.com/api/email/accounts` | [API Listar Contas de E-mail](api/api-listar-contas-de-e-mail.md) |
| GET | `https://api2.chatmasterveloz.com/api/email/messages/{emailId}` | [API Obter um E-mail](api/api-obter-um-e-mail.md) |
| GET | `https://api2.chatmasterveloz.com/api/email/messages?tipo={tipoDoEmail}&accountId={accountId}&desde={desde}&page={pageNumber}&pageSize={pageSize}` | [API Listar E-mails](api/api-listar-e-mails.md) |
| POST | `https://api2.chatmasterveloz.com/api/email/send` | [API Enviar E-mail](api/api-enviar-e-mail.md) |
| GET | `https://api2.chatmasterveloz.com/api/figurinhas` | [API Listar Figurinhas](api/api-listar-figurinhas.md) |
| POST | `https://api2.chatmasterveloz.com/api/figurinhas/enviar` | [API Enviar Figurinha](api/api-enviar-figurinha.md) |
| GET | `https://api2.chatmasterveloz.com/api/flowbuilder` | [API Listar Fluxos](api/api-listar-fluxos.md) |
| POST | `https://api2.chatmasterveloz.com/api/flowbuilder` | [API Criar Fluxo](api/api-criar-fluxo.md) |
| GET | `https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}` | [API Obter uma Gravação](api/api-obter-uma-gravacao.md) |
| POST | `https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}/transcrever` | [API Pedir a Transcrição de uma Gravação](api/api-pedir-a-transcricao-de-uma-gravacao.md) |
| GET | `https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}/transcricao?formato={formatoDaTranscricao}` | [API Obter a Transcrição de uma Gravação](api/api-obter-a-transcricao-de-uma-gravacao.md) |
| GET | `https://api2.chatmasterveloz.com/api/gravacoes?pageNumber={pageNumber}&de={dataInicio}&ate={dataFim}&origem={origemDaGravacao}&ticketId={ticketId}&chatId={chatId}&estado={estadoDaGravacao}&busca={busca}` | [API Listar Gravações](api/api-listar-gravacoes.md) |
| POST | `https://api2.chatmasterveloz.com/api/isValid` | [API Validar Contato](api/api-validar-contato.md) |
| GET | `https://api2.chatmasterveloz.com/api/janela?number=5511955892164` | [API Janela de Atendimento pelo Número](api/api-janela-de-atendimento-pelo-numero.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/edit` | [API Editar Mensagem no Painel](api/api-editar-mensagem-no-painel.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/finish` | [API Encerrar Ticket](api/api-encerrar-ticket.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/flowbuilderStart` | [API Iniciar um Fluxo do Flowbuilder](api/api-iniciar-um-fluxo-do-flowbuilder.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/internal/send` | [API Mensagem Interna](api/api-mensagem-interna.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/isRecording` | [API Gravando…](api/api-gravando.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/isTyping` | [API Digitando…](api/api-digitando.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/list` | [API Listar Mensagens do Ticket sem as Internas](api/api-listar-mensagens-do-ticket-sem-as-internas.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Oficial Enviar Imagem por URL](api/api-oficial-enviar-imagem-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Facebook Enviar Imagem por URL](api/api-facebook-enviar-imagem-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Instagram Enviar Imagem por URL](api/api-instagram-enviar-imagem-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Oficial Enviar Áudio por URL](api/api-oficial-enviar-audio-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Facebook Enviar Áudio por URL](api/api-facebook-enviar-audio-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Instagram Enviar Áudio por URL](api/api-instagram-enviar-audio-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Oficial Enviar Vídeo por URL](api/api-oficial-enviar-video-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Facebook Enviar Vídeo por URL](api/api-facebook-enviar-video-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Instagram Enviar Vídeo por URL](api/api-instagram-enviar-video-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Oficial Enviar Documento por URL](api/api-oficial-enviar-documento-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Facebook Enviar Documento por URL](api/api-facebook-enviar-documento-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL` | [API Instagram Enviar Documento por URL](api/api-instagram-enviar-documento-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/send` | [API Mensagem de Texto](api/api-mensagem-de-texto.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/send` | [API Enviar Arquivo](api/api-enviar-arquivo.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendBTN2` | [API Botão Quick Reply](api/botao-quick-reply-api.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendCTAURL` | [API Oficial Botão URL](api/api-oficial-botao-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendContact` | [API Enviar Contato](api/api-enviar-contato.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendCopyPaste` | [API Botão Copia e Cola](api/botao-copia-e-cola-api.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendGroup` | [API Mensagem para Grupos](api/api-mensagem-para-grupos.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendGupshupTemplate` | [API Gupshup Mensagem Template](api/api-gupshup-mensagem-template.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendInteractive` | [API Oficial Mensagem de Lista](api/api-oficial-mensagem-de-lista.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendInteractive` | [API Oficial Botão Quick Reply](api/api-oficial-botao-quick-reply.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendList` | [API Mensagem de Lista](api/api-mensagem-de-lista.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendMetaCustom` | [API Oficial Mensagem Template](api/api-oficial-mensagem-template.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendMetaCustom` | [API Oficial Mensagem Template sem variável](api/api-oficial-mensagem-template-sem-variavel.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendOfficial` | [API Oficial Template sem variável (Hub)](api/api-oficial-template-sem-variavel-hub.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendOfficial` | [API Oficial Template com variável (Hub)](api/api-oficial-template-com-variavel-hub.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendOfficialCustom` | [API Oficial Template Customizado (Hub)](api/api-oficial-template-customizado-hub.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendOfficialData` | [API Oficial Mensagem](api/api-oficial-mensagem.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendOfficialData` | [API Facebook Mensagem de Texto](api/api-facebook-mensagem-de-texto.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendOfficialData` | [API Instagram Mensagem de Texto](api/api-instagram-mensagem-de-texto.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendRcsTemplate` | [API RCS Mensagem Template](api/api-rcs-mensagem-template.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendURLAudio` | [API Enviar Áudio por URL](api/api-enviar-audio-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendURLBTN` | [API Botão URL](api/botao-url-api.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendURLDocument` | [API Enviar Documento por URL](api/api-enviar-documento-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendURLImage` | [API Enviar Imagem por URL](api/api-enviar-imagem-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/sendURLVideo` | [API Enviar Vídeo por URL](api/api-enviar-video-por-url.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/typebotStart` | [API Iniciar um Fluxo do Typebot](api/api-iniciar-um-fluxo-do-typebot.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/typing` | [API Oficial Digitando](api/api-oficial-digitando.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendBase64AudioWhatsmeowPRO` | [API Enviar Áudio Base64](api/api-enviar-audio-base64-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendButtonsPRO` | [API Botão Copia e Cola](api/api-botao-copia-e-cola-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendButtonsPRO` | [API Botão URL](api/api-botao-url-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendButtonsPRO` | [API Botão Quick Reply](api/api-botao-quick-reply-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendButtonsPRO` | [API Botão Ligação](api/api-botao-ligacao-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendButtonsPRO` | [API Botão Pix](api/api-botao-pix-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendCarousel` | [API Botão Carrossel](api/api-botao-carrossel.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendComposingPRO` | [API Digitando….](api/api-digitando-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendComposingPRO` | [API Gravando….](api/api-gravando-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendImageStatus` | [API Enviar Status de Imagem](api/api-enviar-status-de-imagem.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendListPRO` | [API Mensagem de Lista](api/api-mensagem-de-lista-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendTextGroupPRO` | [API Mensagem para Grupos](api/api-mensagem-para-grupos-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendTextPROLid` | [API Mensagem de Texto via LID](api/api-mensagem-de-texto-via-lid.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendTextStatus` | [API Enviar Status de Texto](api/api-enviar-status-de-texto.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowGroupPRO` | [API Enviar Imagem por URL para Grupos](api/api-enviar-imagem-por-url-para-grupos-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowGroupPRO` | [API Enviar Áudio por URL para Grupos](api/api-enviar-audio-por-url-para-grupos-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowGroupPRO` | [API Enviar Vídeo por URL para Grupos](api/api-enviar-video-por-url-para-grupos-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowGroupPRO` | [API Enviar Documento por URL para Grupos](api/api-enviar-documento-por-url-para-grupos-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowGroupPRO` | [API Enviar Arquivo por URL para Grupos](api/api-enviar-arquivo-por-url-para-grupos-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowPRO` | [API Enviar Imagem por URL](api/api-enviar-imagem-por-url-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowPRO` | [API Enviar Áudio por URL](api/api-enviar-audio-por-url-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowPRO` | [API Enviar Vídeo por URL](api/api-enviar-video-por-url-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowPRO` | [API Enviar Documento por URL](api/api-enviar-documento-por-url-pro.md) |
| POST | `https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendVideoStatus` | [API Enviar Status de Vídeo](api/api-enviar-status-de-video.md) |
| POST | `https://api2.chatmasterveloz.com/api/nova-conexao` | [API Criar Conexão](api/api-criar-conexao.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/oportunidade` | [API Deletar Oportunidade V1](api/api-deletar-oportunidade-v1.md) |
| POST | `https://api2.chatmasterveloz.com/api/oportunidade` | [API Criar Oportunidade V1](api/api-criar-oportunidade-v1.md) |
| PUT | `https://api2.chatmasterveloz.com/api/oportunidade` | [API Atualizar Oportunidade V1](api/api-atualizar-oportunidade-v1.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/categorias` | [API Listar Categorias de Produto](api/api-listar-categorias-de-produto.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/clientes/{contactId}` | [API Obter o Resumo do Cliente no PDV](api/api-obter-o-resumo-do-cliente-no-pdv.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/enderecos` | [API Criar Endereço do Cliente](api/api-criar-endereco-do-cliente.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/enderecos/importar` | [API Importar Endereços do Cliente](api/api-importar-enderecos-do-cliente.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/pdv/enderecos/{enderecoId}` | [API Deletar Endereço do Cliente](api/api-deletar-endereco-do-cliente.md) |
| PUT | `https://api2.chatmasterveloz.com/api/pdv/enderecos/{enderecoId}` | [API Atualizar Endereço do Cliente](api/api-atualizar-endereco-do-cliente.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/enderecos?number=5511955892164` | [API Listar Endereços do Cliente](api/api-listar-enderecos-do-cliente.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/formas-de-pagamento` | [API Listar Descontos e Taxas das Formas de Pagamento](api/api-listar-descontos-e-taxas-das-formas-de-pagamento.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/frete?cep={cep}&bairro={bairro}` | [API Cotar Frete](api/api-cotar-frete.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/mesas?tipo={tipoDaMesa}&ativa={mesaAtiva}` | [API Listar Mesas e Comandas](api/api-listar-mesas-e-comandas.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/pedidos` | [API Criar Pedido](api/api-criar-pedido.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}` | [API Obter um Pedido](api/api-obter-um-pedido.md) |
| PUT | `https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}` | [API Atualizar Pedido](api/api-atualizar-pedido.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/cancelar` | [API Cancelar Pedido](api/api-cancelar-pedido.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/confirmar` | [API Confirmar Pedido](api/api-confirmar-pedido.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/entregue` | [API Marcar Pedido como Entregue](api/api-marcar-pedido-como-entregue.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/pagamentos` | [API Registrar Pagamento do Pedido](api/api-registrar-pagamento-do-pedido.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/preparar` | [API Marcar Pedido em Preparo](api/api-marcar-pedido-em-preparo.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/pronto` | [API Marcar Pedido como Pronto](api/api-marcar-pedido-como-pronto.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/saiu` | [API Marcar Pedido como Saiu para Entrega](api/api-marcar-pedido-como-saiu-para-entrega.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/pedidos?situacao={situacaoDoPedido}&pagamento={pagamentoDoPedido}&de={dataInicio}&ate={dataFim}&busca={busca}&ticketId={ticketId}&pageNumber={pageNumber}` | [API Listar Pedidos](api/api-listar-pedidos.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/relatorio/lancamentos?de={dataInicio}&ate={dataFim}&tipo={tipoDoLancamento}&pageNumber={pageNumber}` | [API Listar Lançamentos do PDV](api/api-listar-lancamentos-do-pdv.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/relatorio?de={dataInicio}&ate={dataFim}&userId={userId}` | [API Obter Relatório do PDV](api/api-obter-relatorio-do-pdv.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/reservas` | [API Criar Reserva de Mesa](api/api-criar-reserva-de-mesa.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}` | [API Obter uma Reserva de Mesa](api/api-obter-uma-reserva-de-mesa.md) |
| PUT | `https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}` | [API Atualizar Reserva de Mesa](api/api-atualizar-reserva-de-mesa.md) |
| POST | `https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}/situacao` | [API Atualizar a Situação de uma Reserva de Mesa](api/api-atualizar-a-situacao-de-uma-reserva-de-mesa.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/reservas?de={dataInicio}&ate={dataFim}&situacao={situacaoDaReserva}&mesaId={mesaId}` | [API Listar Reservas de Mesa](api/api-listar-reservas-de-mesa.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/setores` | [API Listar Setores de Produção](api/api-listar-setores-de-producao.md) |
| GET | `https://api2.chatmasterveloz.com/api/pdv/taxas-de-entrega` | [API Listar Taxas de Entrega](api/api-listar-taxas-de-entrega.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/products` | [API Deletar Produto](api/api-deletar-produto.md) |
| POST | `https://api2.chatmasterveloz.com/api/products` | [API Criar Produto](api/api-criar-produto.md) |
| PUT | `https://api2.chatmasterveloz.com/api/products` | [API Atualizar Produto](api/api-atualizar-produto.md) |
| GET | `https://api2.chatmasterveloz.com/api/projeto-modelos` | [API Listar Modelos de Projeto](api/api-listar-modelos-de-projeto.md) |
| POST | `https://api2.chatmasterveloz.com/api/projetos` | [API Criar Projeto](api/api-criar-projeto.md) |
| GET | `https://api2.chatmasterveloz.com/api/projetos/situacoes` | [API Listar Situações dos Projetos](api/api-listar-situacoes-dos-projetos.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/projetos/{projetoId}` | [API Deletar Projeto](api/api-deletar-projeto.md) |
| GET | `https://api2.chatmasterveloz.com/api/projetos/{projetoId}` | [API Obter um Projeto](api/api-obter-um-projeto.md) |
| PUT | `https://api2.chatmasterveloz.com/api/projetos/{projetoId}` | [API Atualizar Projeto](api/api-atualizar-projeto.md) |
| POST | `https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas` | [API Criar Coluna do Projeto](api/api-criar-coluna-do-projeto.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas/{etapaId}` | [API Deletar Coluna do Projeto](api/api-deletar-coluna-do-projeto.md) |
| PUT | `https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas/{etapaId}` | [API Atualizar Coluna do Projeto](api/api-atualizar-coluna-do-projeto.md) |
| POST | `https://api2.chatmasterveloz.com/api/projetos/{projetoId}/tarefas` | [API Criar Tarefa no Projeto](api/api-criar-tarefa-no-projeto.md) |
| PUT | `https://api2.chatmasterveloz.com/api/projetos/{projetoId}/tarefas/{tarefaId}` | [API Atualizar Tarefa do Projeto](api/api-atualizar-tarefa-do-projeto.md) |
| GET | `https://api2.chatmasterveloz.com/api/projetos?situacao={situacaoDoProjeto}&contactId={contactId}&busca={busca}` | [API Listar Projetos](api/api-listar-projetos.md) |
| POST | `https://api2.chatmasterveloz.com/api/queue` | [API Horário de Expediente](api/api-horario-de-expediente.md) |
| POST | `https://api2.chatmasterveloz.com/api/queues` | [API Criar Setor](api/api-criar-setor.md) |
| POST | `https://api2.chatmasterveloz.com/api/queues/update` | [API Atualizar Setor](api/api-atualizar-setor.md) |
| POST | `https://api2.chatmasterveloz.com/api/queues/{queueId}/next-user` | [API Próximo Operador do Rodízio do Setor](api/api-proximo-operador-do-rodizio-do-setor.md) |
| POST | `https://api2.chatmasterveloz.com/api/quick-messages` | [API Criar Resposta Rápida](api/api-criar-resposta-rapida.md) |
| GET | `https://api2.chatmasterveloz.com/api/quick-messages?queueId={queueId}&userId={userId}&categoria={categoria}&searchParam={searchParam}&pageNumber={pageNumber}` | [API Listar Respostas Rápidas](api/api-listar-respostas-rapidas.md) |
| GET | `https://api2.chatmasterveloz.com/api/ratings?dateStart={dateStart}&dateEnd={dateEnd}&pageNumber={pageNumber}&pageSize={pageSize}` | [API Listar Avaliações](api/api-listar-avaliacoes.md) |
| GET | `https://api2.chatmasterveloz.com/api/rodizios` | [API Listar Rodízios](api/api-listar-rodizios.md) |
| POST | `https://api2.chatmasterveloz.com/api/rodizios/{rodizioId}/distribuir` | [API Distribuir Atendimento por Rodízio](api/api-distribuir-atendimento-por-rodizio.md) |
| GET | `https://api2.chatmasterveloz.com/api/rodizios/{rodizioId}/relatorio?dataInicio={dataInicio}&dataFim={dataFim}` | [API Obter o Relatório de um Rodízio](api/api-obter-o-relatorio-de-um-rodizio.md) |
| POST | `https://api2.chatmasterveloz.com/api/schedules` | [API Criar Agendamento](api/api-criar-agendamento.md) |
| POST | `https://api2.chatmasterveloz.com/api/schedules/delete` | [API Deletar Agendamento](api/api-deletar-agendamento.md) |
| POST | `https://api2.chatmasterveloz.com/api/tags` | [API Criar Tag](api/api-criar-tag.md) |
| POST | `https://api2.chatmasterveloz.com/api/tags/add` | [API Atualizar Tags do Ticket](api/api-atualizar-tags-do-ticket.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/tags/{tagId}` | [API Deletar Tag](api/api-deletar-tag.md) |
| GET | `https://api2.chatmasterveloz.com/api/tags/{tagId}/contacts?searchParam={searchParam}` | [API Listar Contatos de uma Tag](api/api-listar-contatos-de-uma-tag.md) |
| GET | `https://api2.chatmasterveloz.com/api/tags?todas={todas}&tipo={tipoDaTag}` | [API Listar Tags da Empresa](api/api-listar-tags-da-empresa.md) |
| POST | `https://api2.chatmasterveloz.com/api/tasks/create` | [API Criar Tarefa](api/api-criar-tarefa.md) |
| GET | `https://api2.chatmasterveloz.com/api/tasks/list?status={statusDaTarefa}&priority={priorityDaTarefa}&userId={userId}` | [API Listar Tarefas](api/api-listar-tarefas.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/tasks/{tarefaId}` | [API Deletar Tarefa](api/api-deletar-tarefa.md) |
| PUT | `https://api2.chatmasterveloz.com/api/tasks/{tarefaId}` | [API Atualizar Tarefa](api/api-atualizar-tarefa.md) |
| POST | `https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/complete` | [API Finalizar Tarefa](api/api-finalizar-tarefa.md) |
| GET | `https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/status` | [API Obter o Status de uma Tarefa](api/api-obter-o-status-de-uma-tarefa.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/changeconnection` | [API Transferir Tickets entre Conexões](api/api-transferir-tickets-entre-conexoes.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/changequeue` | [API Transferir Tickets para um Setor](api/api-transferir-tickets-para-um-setor.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/closeforced` | [API Encerrar Tickets da Conexão por "Dias de Inatividade"](api/api-encerrar-tickets-da-conexao-por-dias-de-inatividade.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/closeforcedAll` | [API Encerrar Tickets da Empresa por "Dias de Inatividade"](api/api-encerrar-tickets-da-empresa-por-dias-de-inatividade.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/closestatus` | [API Encerrar Ticket em Massa](api/api-encerrar-ticket-em-massa.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/createTicketAPI` | [API Criar Ticket](api/api-criar-ticket.md) |
| GET | `https://api2.chatmasterveloz.com/api/tickets/get` | [API Listar Tickets do Painel](api/api-listar-tickets-do-painel.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/getproto` | [API Listar Protocolos de um Ticket](api/api-listar-protocolos-de-um-ticket.md) |
| GET | `https://api2.chatmasterveloz.com/api/tickets/messages/{protocol}` | [API Listar Mensagens por Protocolo](api/api-listar-mensagens-por-protocolo.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/search` | [API Buscar Tickets por Filtro](api/api-buscar-tickets-por-filtro.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/updateAPI` | [API Obter um Ticket](api/api-obter-um-ticket.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/updateAPI` | [API Atualizar Ticket](api/api-atualizar-ticket.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/tickets/{ticketId}` | [API Apagar Ticket](api/api-apagar-ticket.md) |
| GET | `https://api2.chatmasterveloz.com/api/tickets/{ticketId}/janela` | [API Janela de Atendimento](api/api-janela-de-atendimento.md) |
| GET | `https://api2.chatmasterveloz.com/api/tickets/{ticketId}/messages?limit={limit}&pageNumber={pageNumber}` | [API Listar Mensagens do Ticket](api/api-listar-mensagens-do-ticket.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/{ticketId}/registro` | [API Mensagem Registro do Atendimento](api/api-mensagem-registro-do-atendimento.md) |
| DELETE | `https://api2.chatmasterveloz.com/api/tickets/{ticketId}/tags` | [API Remover Tags do Ticket](api/api-remover-tags-do-ticket.md) |
| POST | `https://api2.chatmasterveloz.com/api/tickets/{ticketId}/tags` | [API Adicionar Tags ao Ticket](api/api-adicionar-tags-ao-ticket.md) |
| POST | `https://api2.chatmasterveloz.com/api/users` | [API Criar Usuário](api/api-criar-usuario.md) |
| GET | `https://api2.chatmasterveloz.com/api/users/status?usuario={userId}` | [API Consultar o Status dos Usuários](api/api-consultar-o-status-dos-usuarios.md) |
| PUT | `https://api2.chatmasterveloz.com/api/users/{userId}` | [API Atualizar Usuário](api/api-atualizar-usuario.md) |
| POST | `https://api2.chatmasterveloz.com/api/users/{userId}/force-logout` | [API Derrubar a Sessão de um Usuário](api/api-derrubar-a-sessao-de-um-usuario.md) |
| PUT | `https://api2.chatmasterveloz.com/api/users/{userId}/status` | [API Atualizar o Status de um Usuário](api/api-atualizar-o-status-de-um-usuario.md) |
| POST | `https://api2.chatmasterveloz.com/api/waba-templates` | [API Criar Mensagens Template Meta](api/api-criar-mensagens-template-meta.md) |
| GET | `https://api2.chatmasterveloz.com/api/waba-templates/{id}` | [API Obter uma Mensagem Template Meta](api/api-obter-uma-mensagem-template-meta.md) |
| GET | `https://api2.chatmasterveloz.com/api/waba-templates?status={statusDoTemplate}&category={category}` | [API Listar Mensagens Template Meta](api/api-listar-mensagens-template-meta.md) |
| POST | `https://api2.chatmasterveloz.com/api/webchat/messages/send` | [API WebChat Mensagem de Texto](api/api-webchat-mensagem-de-texto.md) |
| POST | `https://api2.chatmasterveloz.com/api/webchat/messages/send` | [API WebChat Enviar Arquivo](api/api-webchat-enviar-arquivo.md) |
| POST | `https://api2.chatmasterveloz.com/api/whatsapp-restart` | [API Reiniciar Conexões](api/api-reiniciar-conexoes.md) |
| POST | `https://api2.chatmasterveloz.com/api/whatsapp-status` | [API Status das Conexões](api/api-status-das-conexoes.md) |
| POST | `https://api2.chatmasterveloz.com/api/whatsapp/importSession` | [API Importar Sessão](api/api-importar-sessao.md) |
| POST | `https://api2.chatmasterveloz.com/api/whatsapp/update` | [API Atualizar Conexão](api/api-atualizar-conexao.md) |
| POST | `https://api2.chatmasterveloz.com/api/whatsappqrcodepro` | [API Obter QR Code](api/api-obter-qr-code.md) |
| GET | `https://api2.chatmasterveloz.com/api/whatsapptemplates` | [API Listar Todas Mensagens Template Meta](api/api-listar-todas-mensagens-template-meta.md) |
| DELETE | `https://api2.chatmasterveloz.com/contacts-delete` | [API Deletar TODOS os Contatos](api/api-deletar-todos-os-contatos.md) |
