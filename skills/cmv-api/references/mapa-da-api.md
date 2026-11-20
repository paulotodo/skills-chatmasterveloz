# Mapa da API do Chat Master Veloz: operação × tipo de conexão → artigo

Use este mapa para chegar ao artigo certo sem ler o índice inteiro. Ele só aponta: o payload, os campos e os avisos estão no artigo, que precisa ser aberto antes de escrever qualquer código.

- Todos os caminhos são relativos a `references/docs/` (por exemplo, `api/api-criar-ticket.md` é `references/docs/api/api-criar-ticket.md`).
- **❌** = a tabela de `api/bibliotecas.md` diz que o recurso não existe naquela biblioteca.
- **não documentado** = não há artigo para aquela variante. Diga isso à pessoa; não adapte o artigo de outra conexão.
- O que não estiver aqui: `python3 scripts/buscar_endpoint.py <palavras>` ou `INDICE-api.md`.

## Sumário

1. [Qual coluna é a da pessoa](#1-qual-coluna-é-a-da-pessoa)
2. [Envio pelo WhatsApp: Básica, Pro e Oficial](#2-envio-pelo-whatsapp-básica-pro-e-oficial)
3. [Envio pelos outros canais](#3-envio-pelos-outros-canais)
4. [Templates](#4-templates)
5. [Operações que não dependem da conexão (selo Todas)](#5-operações-que-não-dependem-da-conexão-selo-todas)
6. [Chamadas que só aceitam o Token da Empresa](#6-chamadas-que-só-aceitam-o-token-da-empresa)
7. [Webhooks](#7-webhooks)
8. [De onde vem cada identificador](#8-de-onde-vem-cada-identificador)

## 1. Qual coluna é a da pessoa

| A conexão é… | Coluna / selo | Fonte |
|---|---|---|
| WhatsApp por QR Code | **Básica** ou **Pro** (são duas bibliotecas diferentes; a documentação não descreve como ver na tela qual das duas é a da conexão) | `api/bibliotecas.md` |
| WhatsApp API Oficial da Meta | **Oficial** | `api/bibliotecas.md` |
| WhatsApp Oficial pelo Hub | **Oficial Hub**, só no artigo de template sem variável (seção 4). Texto, mídia, lista, botões e template com variáveis pelo Hub: não documentado | `api/bibliotecas.md`, `api/api-oficial-template-sem-variavel-hub.md` |
| Instagram Direct | **Instagram** | `api/api-instagram-mensagem-de-texto.md` |
| Facebook Messenger | **Facebook** | `api/api-facebook-mensagem-de-texto.md` |
| Widget Web Chat | **WebChat** | `api/api-webchat-mensagem-de-texto.md` |
| Página do Chat Externo | **Chat Externo** | `api/api-chat-externo-mensagem-de-texto.md` |
| WhatsApp Gupshup / RCS | **Gupshup** / **RCS** (só há artigo de template) | seção 4 |

## 2. Envio pelo WhatsApp: Básica, Pro e Oficial

Nas chamadas **Oficial** de texto, mídia, lista e botões, o artigo exige a Janela de Atendimento **aberta**; fora dela, o caminho é template (seção 4). Para consultar a janela: `api/api-janela-de-atendimento-pelo-numero.md`.

A coluna **Oficial** desta tabela é a conexão Oficial direta. Para a Oficial pelo **Hub** só existe o artigo de template sem variável da seção 4 (`api/bibliotecas.md` ainda fala em três chamadas de template pelo Hub, mas só esse artigo está na documentação), e não há artigo de Hub para nenhuma linha desta tabela. Se a pessoa usa o Hub e pede outra coisa, diga que não está documentado se as chamadas desta coluna valem para ela.

| Operação | Básica | Pro | Oficial |
|---|---|---|---|
| Mensagem de texto | `api/api-mensagem-de-texto.md` | `api/api-mensagem-de-texto.md` (por LID em vez de telefone: `api/api-mensagem-de-texto-via-lid.md`) | `api/api-oficial-mensagem.md` |
| Imagem por URL | `api/api-enviar-imagem-por-url.md` | `api/api-enviar-imagem-por-url-pro.md` | `api/api-oficial-enviar-imagem-por-url.md` |
| Áudio por URL | `api/api-enviar-audio-por-url.md` | `api/api-enviar-audio-por-url-pro.md` | `api/api-oficial-enviar-audio-por-url.md` |
| Vídeo por URL | `api/api-enviar-video-por-url.md` | `api/api-enviar-video-por-url-pro.md` | `api/api-oficial-enviar-video-por-url.md` |
| Documento por URL | `api/api-enviar-documento-por-url.md` | `api/api-enviar-documento-por-url-pro.md` | `api/api-oficial-enviar-documento-por-url.md` |
| Arquivo anexado à requisição (multipart) | `api/api-enviar-arquivo.md` | `api/api-enviar-arquivo.md` | ❌ |
| Áudio em Base64 | ❌ | `api/api-enviar-audio-base64-pro.md` | ❌ |
| Mensagem de lista | `api/api-mensagem-de-lista.md` | `api/api-mensagem-de-lista-pro.md` | `api/api-oficial-mensagem-de-lista.md` |
| Botão Quick Reply | `api/api-botao-quick-reply.md` | `api/api-botao-quick-reply-pro.md` | `api/api-oficial-botao-quick-reply.md` |
| Botão URL | `api/api-botao-url.md` | `api/api-botao-url-pro.md` | `api/api-oficial-botao-url.md` |
| Botão Copia e Cola | `api/api-botao-copia-e-cola.md` | `api/api-botao-copia-e-cola-pro.md` | ❌ |
| Botão Ligação | ❌ | `api/api-botao-ligacao-pro.md` | ❌ |
| Botão Pix | ❌ | `api/api-botao-pix-pro.md` | ❌ |
| Botão Carrossel | ❌ | `api/api-botao-carrossel.md` | ❌ |
| Texto para grupo | `api/api-mensagem-para-grupos.md` | `api/api-mensagem-para-grupos-pro.md` | ❌ |
| Mídia por URL para grupo | ❌ | `api/api-enviar-imagem-por-url-para-grupos-pro.md`, `api/api-enviar-audio-por-url-para-grupos-pro.md`, `api/api-enviar-video-por-url-para-grupos-pro.md`, `api/api-enviar-documento-por-url-para-grupos-pro.md`, `api/api-enviar-arquivo-por-url-para-grupos-pro.md` | ❌ |
| "Digitando…" | `api/api-digitando.md` | `api/api-digitando-pro.md` | `api/api-oficial-digitando.md` |
| "Gravando…" | `api/api-gravando.md` | `api/api-gravando-pro.md` | ❌ |
| Cartão de contato | `api/api-enviar-contato.md` (o selo do artigo diz Básica; `api/bibliotecas.md` e `api/api-mensagem.md` dizem Pro: confirme com o Suporte) | ❌ | ❌ |
| Figurinha | ❌ | `api/api-enviar-figurinha.md` | `api/api-enviar-figurinha.md` |
| Status (texto, imagem, vídeo) | ❌ | `api/api-enviar-status-de-texto.md`, `api/api-enviar-status-de-imagem.md`, `api/api-enviar-status-de-video.md` | ❌ |
| Modo Alternativo (chat externo por link) | ❌ | ❌ | `api/api-modo-alternativo-enviar-link.md`, `api/api-modo-alternativo-mensagem-de-texto.md`, `api/api-modo-alternativo-enviar-arquivo-por-url.md`, `api/api-modo-alternativo-enviar-arquivo.md` |

O que muda de uma coluna para a outra, além do endereço (leia o artigo, isto é só o alerta):

- **Mídia por URL.** Na Básica há um endereço por tipo de arquivo e o payload leva `mimeType`. Na Pro há um endereço só para todos os tipos (`sendUrlFilesWhatsmeowPRO`) e na Oficial outro só (`official/sendMediaByURL`); nas duas o payload leva `type`. Copiar o payload de uma para a outra não funciona.
- **Nomes de campo.** Lista na Básica usa `body`, `buttonLabel`, `options`; na Pro usa `Desc`, `ButtonText`, `TopText`, `List`; na Oficial usa `type`, `header`, `body`, `footer`, `action`. Botões Quick Reply, URL, Copia e Cola, Ligação e Pix na Pro usam `phone` no lugar de `number`; o Carrossel da Pro usa `number`.
- **Botões.** Dependem também da opção **Botões** habilitada no plano, separada da **API Externa** (`api/pre-requisitos-botoes.md`). Na Básica, os artigos avisam que a chamada não abre atendimento nem grava a mensagem no painel. Na Pro, avisam que resposta de sucesso não garante a entrega.
- **`openTicket` e `queueId`.** O efeito sobre o atendimento muda de artigo para artigo (até entre os dois artigos de template da Oficial). Explique à pessoa o que o artigo daquela chamada diz.

## 3. Envio pelos outros canais

| Operação | Instagram | Facebook | WebChat | Chat Externo |
|---|---|---|---|---|
| Mensagem de texto | `api/api-instagram-mensagem-de-texto.md` | `api/api-facebook-mensagem-de-texto.md` | `api/api-webchat-mensagem-de-texto.md` | `api/api-chat-externo-mensagem-de-texto.md` |
| Imagem por URL | `api/api-instagram-enviar-imagem-por-url.md` | `api/api-facebook-enviar-imagem-por-url.md` | não documentado | `api/api-chat-externo-enviar-arquivo-por-url.md` |
| Áudio por URL | `api/api-instagram-enviar-audio-por-url.md` | `api/api-facebook-enviar-audio-por-url.md` | não documentado | `api/api-chat-externo-enviar-arquivo-por-url.md` |
| Vídeo por URL | `api/api-instagram-enviar-video-por-url.md` | `api/api-facebook-enviar-video-por-url.md` | não documentado | `api/api-chat-externo-enviar-arquivo-por-url.md` |
| Documento por URL | `api/api-instagram-enviar-documento-por-url.md` | `api/api-facebook-enviar-documento-por-url.md` | não documentado | `api/api-chat-externo-enviar-arquivo-por-url.md` |
| Arquivo anexado (multipart) | não documentado | não documentado | `api/api-webchat-enviar-arquivo.md` | `api/api-chat-externo-enviar-arquivo.md` |
| Mensagem de lista | `api/api-instagram-mensagem-de-lista.md` | `api/api-facebook-mensagem-de-lista.md` | `api/api-webchat-mensagem-de-lista.md` | `api/api-chat-externo-mensagem-de-lista.md` |
| Botão Quick Reply | `api/api-instagram-botao-quick-reply.md` | `api/api-facebook-botao-quick-reply.md` | `api/api-webchat-botao-quick-reply.md` | `api/api-chat-externo-botao-quick-reply.md` |
| Template | não documentado | não documentado | não documentado | não documentado |
| Grupos | não documentado | não documentado | não documentado | não documentado |

- **Instagram e Facebook:** o campo `number` não é telefone; é o identificador do contato no canal, o `sender` que chega no webhook. O artigo exige a janela de atendimento aberta.
- **WebChat:** o destinatário é o `sessionId` do visitante, e o ticket precisa estar aberto ou pendente.
- **Chat Externo:** o destinatário é o `ticketId` (o `chamadoId` do webhook). Criar ticket por API nessa conexão é recusado (`api/api-criar-ticket.md`).

## 4. Templates

| Situação | Artigo | Selo |
|---|---|---|
| Template com variáveis, cabeçalho ou botões (Oficial direta) | `api/api-oficial-mensagem-template.md` | Oficial |
| Template sem variável (Oficial direta) | `api/api-oficial-mensagem-template-sem-variavel.md` | Oficial |
| Template sem variável pelo Hub | `api/api-oficial-template-sem-variavel-hub.md` | Oficial Hub |
| Template com variável ou customizado pelo Hub | não documentado | |
| Template pela conexão WhatsApp Gupshup | `api/api-gupshup-mensagem-template.md` | Gupshup |
| Template do agente RCS (provedor Gupshup) | `api/api-rcs-mensagem-template.md` | RCS |
| Listar os templates da conexão, com filtro | `api/api-listar-mensagens-template-meta.md` | Oficial |
| Listar todos os templates cadastrados na Meta | `api/api-listar-todas-mensagens-template-meta.md` | Oficial |
| Obter um template | `api/api-obter-uma-mensagem-template-meta.md` | Oficial |
| Criar um template | `api/api-criar-mensagens-template-meta.md` | Oficial |
| Básica e Pro | ❌ (não há template nas bibliotecas por QR Code) | `api/bibliotecas.md` |

O nome e o idioma do template têm de ser idênticos aos aprovados; os componentes do payload seguem o que existe no template aprovado, na ordem das variáveis. Redigir o texto do template é assunto da skill `cmv-mensagens`.

## 5. Operações que não dependem da conexão (selo Todas)

O artigo é o mesmo para Básica, Pro e Oficial. Ainda assim o token decide a empresa e, em várias chamadas, a conexão afetada.

### Tickets

| Operação | Artigo | Atenção (está no artigo) |
|---|---|---|
| Criar ticket | `api/api-criar-ticket.md` | Usa `contactId`; se o contato já tem ticket na conexão, devolve o existente. |
| Obter um ticket | `api/api-obter-um-ticket.md` | GET com o `ticketId` no endereço; só leitura, não muda nada no ticket. |
| Mudar status, Setor ou atendente de **um** ticket (transferir um atendimento) | `api/api-atualizar-ticket.md` | É por aqui que se transfere um ticket só. No encerramento, aceita o retorno ao mesmo atendente (`retornoAoAtendente`, `minutosDoRetorno`, `setorDeTransbordoId`). |
| Transferir **todos** os tickets da conexão para um Setor | `api/api-transferir-tickets-para-um-setor.md` | Move todos, inclusive encerrados; não há filtro. |
| Transferir todos os tickets de uma conexão para outra | `api/api-transferir-tickets-entre-conexoes.md` | Migração em bloco. |
| Entregar um atendimento a um operador pelo rodízio | `api/api-distribuir-atendimento-por-rodizio.md` | Ninguém disponível não é erro. |
| Encerrar um ticket | `api/api-encerrar-ticket.md` | |
| Encerrar vários tickets | `api/api-encerrar-ticket-em-massa.md` | Em bloco, por status e Setor. |
| Apagar ticket | `api/api-apagar-ticket.md` | Apaga as mensagens junto; não há como desfazer. |
| Listar tickets com os filtros do painel | `api/api-listar-tickets-do-painel.md` | GET com corpo; exige `queueIds` e mais um filtro. |
| Buscar tickets por tags, situação, Setor e tempo parado | `api/api-buscar-tickets-por-filtro.md` | |
| Listar tickets de um contato | `api/api-listar-tickets-do-contato.md` | |
| Listar tickets que têm uma tag | `api/api-listar-contatos-por-tag.md` | Sem `tagid`, devolve todos os tickets da empresa. |
| Mensagens de um ticket | `api/api-listar-mensagens-do-ticket.md` | Páginas andam para trás no tempo; notas internas vêm no meio. |
| Mensagens de um protocolo | `api/api-listar-mensagens-por-protocolo.md` | |
| Mensagem interna (só a equipe vê) | `api/api-mensagem-interna.md` | |
| Janela de atendimento | `api/api-janela-de-atendimento.md`, `api/api-janela-de-atendimento-pelo-numero.md` | |

### Contatos

| Operação | Artigo | Atenção (está no artigo) |
|---|---|---|
| Criar contato | `api/api-criar-contato.md` | Não confere o número no WhatsApp. |
| Criar contato validando o número | `api/api-criar-contato-com-validacao.md` | Selo **Básica, Pro**; na Oficial ❌. |
| Validar se um número existe no WhatsApp | `api/api-validar-contato.md` | Selo **Básica, Pro**; depende de duas configurações do painel. |
| Obter um contato pelo número | `api/api-obter-um-contato.md` | |
| Atualizar contato | `api/api-atualizar-contato.md` | Pelo `id`; `extraInfo` substitui o conjunto inteiro. |
| Listar contatos | `api/api-listar-contatos.md` | |
| Listar contatos de uma tag | `api/api-listar-contatos-de-uma-tag.md` | |
| Apagar **todos** os contatos | `api/api-deletar-todos-os-contatos.md` | Destrutivo. Nunca sugira sem a pessoa pedir exatamente isso. |

### Tags

| Operação | Artigo | Atenção (está no artigo) |
|---|---|---|
| Adicionar tags a um ticket, mantendo as que já estão | `api/api-adicionar-tags-ao-ticket.md` | Tag de raia do Kanban tira a raia anterior. |
| Remover tags de um ticket | `api/api-remover-tags-do-ticket.md` | |
| Definir as tags de um ticket (substitui todas) | `api/api-atualizar-tags-do-ticket.md` | As que não forem enviadas são removidas. |
| Listar tags da empresa | `api/api-listar-tags-da-empresa.md` | Filtros na URL. |
| Criar tag no cadastro | `api/api-criar-tag.md` | Criar não aplica a tag a nenhum ticket. |
| Apagar tag do cadastro | `api/api-deletar-tag.md` | Apaga da empresa inteira; não é "tirar do ticket". |

### CRM

A versão do CRM da empresa decide o conjunto de artigos: os de `/crm/v2/` exigem o CRM novo ativado, e os "V1" exigem o CRM antigo. A versão é escolhida em **Configurações › Opções › Vendas**, seção **CRM**, campo **Versão do CRM** (`recursos/vendas-em-configuracoes.md`).

| Operação | CRM novo | CRM antigo (V1) |
|---|---|---|
| Descobrir ids de funil e raia | `api/api-listar-funis.md` | não documentado |
| Criar oportunidade | `api/api-criar-oportunidade.md` | `api/api-criar-oportunidade-v1.md` |
| Atualizar oportunidade | `api/api-atualizar-oportunidade.md` | `api/api-atualizar-oportunidade-v1.md` |
| Mover de raia | `api/api-mover-oportunidade-de-raia.md` | não documentado |
| Listar oportunidades | `api/api-listar-oportunidades.md` | não documentado |
| Obter uma oportunidade | `api/api-obter-uma-oportunidade.md` | não documentado |
| Apagar oportunidade | `api/api-deletar-oportunidade.md` | `api/api-deletar-oportunidade-v1.md` |
| Origens de venda e motivos de perda | `api/api-listar-origens-de-venda.md`, `api/api-listar-motivos-de-perda.md` | não documentado |

### Produtos e estoque

| Operação | Artigo | Atenção (está no artigo) |
|---|---|---|
| Listar produtos; obter um pelo id ou pelo SKU | `api/api-listar-produtos.md`, `api/api-obter-um-produto.md`, `api/api-obter-um-produto-pelo-sku.md` | |
| Criar, atualizar e apagar produto | `api/api-criar-produto.md`, `api/api-atualizar-produto.md`, `api/api-deletar-produto.md` | |
| Lançar e listar movimentações do estoque | `api/api-lancar-movimentacao-no-estoque.md`, `api/api-listar-movimentacoes-do-estoque.md` | Exclusivas do PDV. |

### Agendamento, fluxos e apoio

| Operação | Artigo | Atenção (está no artigo) |
|---|---|---|
| Agendar mensagem | `api/api-criar-agendamento.md` | Exige `contactId`, `userId` e `whatsappId`; aceita template para canais oficiais. |
| Listar e obter agendamentos | `api/api-listar-agendamentos.md`, `api/api-obter-um-agendamento.md` | |
| Atualizar agendamento | `api/api-atualizar-agendamento.md` | Só o que ainda não foi enviado. |
| Apagar agendamento | `api/api-deletar-agendamento.md` | Só os criados pela API. |
| Iniciar um fluxo do FlowBuilder | `api/api-iniciar-um-fluxo-do-flowbuilder.md`, `recursos/gatilho-via-api.md` | O `queueId` é o do Setor vinculado ao fluxo; o ticket vai para Aguardando. |
| Iniciar um fluxo do Typebot | `api/api-iniciar-um-fluxo-do-typebot.md` | |
| Listar fluxos | `api/api-listar-fluxos.md` | |
| Testar token e listar conexões | `api/api-status-das-conexoes.md` | A resposta traz o token de cada conexão: não exibir nem guardar em log. |
| Listar Setores (ids para `queueId`) | `api/api-listar-setores-da-empresa.md` | |
| Listar usuários (ids para `userId`) | `api/api-listar-usuarios-da-empresa.md` | |

### Quadro de Atendimentos, Reservas, Consultório, Tarefas e Equipe

| Grupo | Artigos (a página da seção lista todos) | Atenção (está no artigo) |
|---|---|---|
| Quadro de Atendimentos: quadros, colunas, regras, atendimentos do quadro (mover de coluna, fixar no topo, trocar a tag) | `api/api-quadro-de-atendimentos.md`; por exemplo `api/api-listar-quadros.md`, `api/api-listar-atendimentos-do-quadro.md`, `api/api-mover-atendimento-de-coluna.md` | Selo Todas. |
| Reservas: reservas e séries, situação, horários e noites livres, ofertas, recursos, pacotes, relatório | `api/api-reservas.md`; por exemplo `api/api-criar-reserva.md`, `api/api-listar-horarios-livres-das-reservas.md`, `api/api-listar-reservas.md` | Selo Todas. |
| Consultório: pacientes, consultas (marcar, remarcar, status), horários livres, profissionais, salas, serviços, convênios | `api/api-consultorio.md`; por exemplo `api/api-marcar-consulta.md`, `api/api-listar-horarios-livres-do-consultorio.md`, `api/api-buscar-pacientes.md` | Selo Empresa: só o Token da Empresa (seção 6). |
| Tarefas: obter uma, comentários e anexos | `api/api-obter-uma-tarefa.md`, `api/api-listar-comentarios-da-tarefa.md`, `api/api-criar-comentario-na-tarefa.md`, `api/api-listar-anexos-da-tarefa.md`, `api/api-anexar-arquivo-na-tarefa.md`, `api/api-deletar-anexo-da-tarefa.md` | As outras chamadas de Tarefas estão em `api/api-tarefas.md`. |
| Link de login automático de uma pessoa da Equipe (abre o painel já logado, também em iframe) | `api/api-gerar-link-de-login-automatico.md` | Só o Token da Empresa; exige **Ligar o login automático** em **Configurações › Opções › Integrações e segurança**, seção **Segurança**; chamar do servidor, nunca do navegador. |

PDV, Projetos, Chat Interno, Gravações, Rodízios, E-mail, Respostas Rápidas, Campanhas e Extras: veja a seção correspondente em `INDICE-api.md`.

## 6. Chamadas que só aceitam o Token da Empresa

São os artigos com `**API:** Empresa` (Projetos, Chat Interno, Gravações, Consultório e o link de login automático). Liste com `python3 scripts/buscar_endpoint.py --conexao empresa`. Com o token de uma conexão, a resposta é 401 "Acesso não permitido" (`recursos/token-da-empresa-em-configuracoes.md`).

## 7. Webhooks

| Webhook | Sentido | Onde configurar (como está no artigo) | O que avisa | Artigo |
|---|---|---|---|---|
| Da Conexão | sai do CMV | **Conexões › editar a Conexão › aba Integrações**, campo **Webhook** (há um principal e um secundário: ver abaixo) | Mensagem recebida e enviada, atendimento aberto, encerrado, reaberto ou mexido (Setor, atendente, status) por qualquer caminho, retorno ao mesmo atendente, tags, mensagem interna e Registro do atendimento, resposta à avaliação, videochamada, operador convidado | `api/webhooks-da-conexao.md` |
| Do Setor | sai do CMV | **Setores & Chatbot › editar o Setor**, campo **URL do Webhook** | Mensagem recebida e enviada, atendimento que chega ao Setor, tag, mensagem interna e Registro do atendimento, só dos tickets daquele Setor; os valores de `acao` são outros (`queue_webhook`, `queue_webhook_from_internal`, `queue_webhook_update`) | `api/webhook-de-setor.md` |
| Eventos | sai do CMV | **Configurações › Opções › Integrações e segurança**, seção **Webhooks e integrações** | Mensagens internas, TAG, Usuários (status) e CRM, um campo para cada | `api/webhook-eventos.md`, `recursos/webhooks-e-integracoes-em-configuracoes.md` |
| Do funil (CRM) | sai do CMV | **CRM › Funis**, em **Novo funil** ou **Editar funil** | Movimentação de oportunidades daquele funil; o campo `evento` diz qual (`CREATED`, `LANE_CHANGED`, `WON`, `LOST`…). Com segredo gerado, cada aviso vem assinado (HMAC-SHA256, valor começando em `sha256=`) | `recursos/webhook-do-funil.md` |
| Do Chat Interno | sai do CMV | menu **Chat Interno**, ícone **Webhook do chat interno** | Conversas, mensagens, reações e chamadas da equipe | `api/webhook-do-chat-interno.md` |
| Do PDV | sai do CMV | **Configurações › Opções › Integrações e segurança**, seção **Webhooks e integrações**, **Webhook do PDV** | Pedidos, pagamentos, caixa, estoque, entrega, setores de produção. Assinado com o Token da Empresa (`X-Assinatura-Pdv`) | `api/webhook-do-pdv.md`, `recursos/webhooks-e-integracoes-em-configuracoes.md` |
| Do Cardápio Digital | sai do CMV | o mesmo **Webhook do PDV** | Loja, endereços, mesas, comandas, reservas | `api/webhook-do-cardapio-digital.md` |
| De Projetos | sai do CMV | **Configurações › Opções › Integrações e segurança**, seção **Webhooks e integrações**, **Webhook de Projetos** | Projetos, etapas, tarefas e modelos. Assinado com o Token da Empresa (`X-Assinatura-Projetos`) | `api/webhook-de-projetos.md` |
| De E-mail | sai do CMV | **Configurações › Opções › Integrações e segurança**, seção **Webhooks e integrações**, **Webhook de e-mail** | E-mail recebido e enviado (as campanhas em massa têm webhook próprio, o do Mail Marketing). Assinado com o Token da Empresa (`X-Assinatura-Email`) | `api/webhook-de-e-mail.md` |
| Da avaliação pela IA | sai do CMV | **Configurações › Opções › Integrações e segurança**, seção **Webhooks e integrações**, **Webhook da avaliação** | Atendimento avaliado, falha da avaliação, aula gerada, alerta da avaliação | `recursos/webhook-da-avaliacao-pela-ia.md` |
| Das Reservas | sai do CMV | menu **Reservas**, aba **Webhook** | Reservas feitas, confirmadas, remarcadas ou canceladas, pagamentos, pacotes. Assinado com o Token da Empresa (`X-Assinatura-Reservas`) | `api/webhook-das-reservas.md` |
| Do Consultório | sai do CMV | **Consultório › Cadastros do consultório**, aba **Webhook** | Consultas, recepção, pagamentos. Assinado com o Token da Empresa (`X-Assinatura-Consultorio`) | `api/webhook-do-consultorio.md` |
| Do Mail Marketing | sai do CMV | **Mail Marketing › Configurações**, campo **Webhook do Mail Marketing** | Envio de campanha, abertura, clique, descadastro. Nome do evento em `X-MailMarketing-Evento`, assinatura em `X-Assinatura-MailMarketing` | `api/webhook-do-mail-marketing.md` |
| Webhook Trigger | **entra** no CMV | menu **Webhooks \| Triggers**, **Novo Webhook \| Trigger** | Um sistema externo chama o endereço gerado e inicia um fluxo | `api/webhook-triggers.md`, `recursos/gatilho-via-webhooks-trigger.md` |

Apoio: como escolher (`api/qual-webhook-usar.md`), visão geral (`api/webhooks.md`), arquivos recebidos (`api/arquivos-no-webhook.md`), buscar de novo um aviso perdido da Conexão ou do Setor, por até 7 dias (`api/api-listar-entregas-do-webhook-da-conexao.md`), n8n (`recursos/n8n-via-webhook.md`, `recursos/n8n-via-flowbuilder.md`).

### Webhook principal e secundário da Conexão

- `api/webhooks-da-conexao.md` descreve um campo só, **Webhook**, na aba **Integrações** da Conexão.
- `recursos/n8n-via-webhook.md` manda colar a URL em **Conexões > editar > Integrações > Webhook Principal ou Secundário**.
- Pela API, a Conexão tem os campos `webhook` e `webhookb`: "os endereços do webhook principal e do secundário" (`api/api-atualizar-conexao.md`); em `api/api-criar-conexao.md`, `webhookb` é "a URL do seu webhook secundário".
- **Não documentado:** a diferença entre os dois (se recebem os mesmos avisos, se um é reserva do outro, em que ordem são chamados). Não afirme nada sobre isso. Se a pessoa preencheu os dois e recebe em dobro, apresente como hipótese a conferir, não como causa confirmada.

### O que os artigos avisam e costuma quebrar integrações

Esta é a lista completa; `SKILL.md` e `references/moldes-de-codigo.md` só apontam para cá. A receita de receber e responder, com a tabela sintoma → causa → artigo, está em `references/moldes-de-codigo.md`.

- **`acao` × `action`.** Tudo chega no mesmo endereço e o campo `acao` diz o que aconteceu; nos avisos de tag a chave é `action` (alguns trazem as duas). No Webhook Eventos, o `acao` vem dentro de `body`. No do Setor, os valores de `acao` não são os da Conexão. Artigos: `api/webhooks-da-conexao.md`, `api/webhook-de-setor.md`, `api/webhook-eventos.md`.
- **Dois avisos por mensagem recebida.** Na Conexão, primeiro `start`, com o conteúdo como veio; depois `from_internal` (canal Oficial) ou `fila-data` (canais por QR Code), com a mensagem gravada. No Setor, `queue_webhook` e depois `queue_webhook_from_internal`. O segundo é o que vale tratar. A mensagem enviada costuma gerar só o segundo.
- **`mensagem` muda de formato.** No `from_internal` é um objeto; no `start` é uma lista; nos canais por QR Code o texto está em `msg.message`.
- **Direção.** `fromMe` é `false` quando o cliente mandou e `true` quando a mensagem saiu daqui. `name` muda de conteúdo conforme a direção e não serve para isso. Com `fromMe` verdadeiro, `mensagem.userId` preenchido é um atendente pela tela e `mensagem.fromApp` é alguém pelo celular da conta.
- **Quem gerou o aviso.** Todo aviso da Conexão e do Setor traz `origemDoEvento` (`contato`, `painel`, `flowbuilder`, `chatbot`, `ia`, `agendamento`, `sistema` ou `api`); os artigos dizem que é o campo que separa o aviso de algo que a própria integração fez (`api`).
- **Resposta automática em laço (inferência).** Como a mensagem enviada também gera aviso, uma integração que responde a todo aviso responde às próprias respostas. Os artigos não falam em laço; a proteção que eles sustentam é tratar só `fromMe` igual a `false` e ignorar `origemDoEvento` igual a `api`.
- **Repetidos e perdidos.** Todo aviso da Conexão e do Setor traz `eventoId`, `sequencia` e `enviadoEm`. O repetido se descarta pelo `eventoId`, igual em todos os endereços que recebem o mesmo fato; o `mensagem.wid` não serve para isso, porque a mesma mensagem gera mais de um aviso. A `sequencia` sobe de 1 em 1 por endereço: um número pulado é um aviso perdido, que se busca de novo por até 7 dias em `api/api-listar-entregas-do-webhook-da-conexao.md`.
- **Conexão + Setor.** Ligados ao mesmo tempo, os dois disparam para o atendimento que está no Setor escolhido; fora dele, só o da Conexão (`api/qual-webhook-usar.md`). Os dois avisos da mesma mensagem chegam com o mesmo `eventoId` (`api/webhook-de-setor.md`).
- **Mídia recebida.** Chegam dois avisos e é o segundo que traz o arquivo; o jeito de buscá-lo muda por biblioteca: endereço em `body.mensagem.mediaUrl` na Oficial, base64 dentro do aviso na Pro, endereço montado com `backendURL`, `mediaFolder` e `mediaName` na Básica (`api/arquivos-no-webhook.md`).
- **Áudio transcrito.** Com a transcrição ligada, o texto transcrito aparece em `mensagem.body`.
- **Atendimento.** `chamadoId` é o identificador do atendimento (número do ticket); `ticketData` traz o retrato do atendimento (`status`, `protocolo`, `userId`, `contact.number`). Exceções: no `action_from_user`, `ticketData` traz só o que mudou e `ticketData_completo` o atendimento de antes; os avisos `avaliacao-resposta` e os de retorno ao atendente não trazem `ticketData`.
- **Segredo dentro do aviso.** Os avisos da Conexão e do Setor carregam o token da conexão (`token_origin`, `connection_token`, `ticketData.whatsapp.token`) e dados do contato; o de Usuários, e-mail, telefone e hash de senha; o de TAG, o token da conexão. O destino tem de ser um endereço da própria pessoa, em HTTPS, sem o corpo inteiro em log.
- **Exemplos incompletos.** Os artigos avisam que os campos mostrados não são a lista completa e mudam entre versões da plataforma.

### Não documentado sobre webhooks (diga isso à pessoa, não deduza)

| Pergunta | O que existe nos artigos |
|---|---|
| O endereço da mídia (`mediaUrl`, ou o montado na Básica) exige token ou outro cabeçalho? | Nada. `api/arquivos-no-webhook.md` só diz que o arquivo é baixado por GET. |
| Quais são os valores possíveis de `mensagem.mediaType`? | Nada. O exemplo do webhook traz `null`. O único valor citado é `internal`, e na listagem de mensagens por API (`api/api-listar-mensagens-do-ticket.md`), não no webhook. |
| Onde se liga a transcrição de áudio na tela? | Não está nos artigos desta skill. Pela API existe o campo `isTranscribe` do Setor ("`true` transcreve os áudios recebidos no Setor"): `api/api-criar-setor.md`, `api/api-atualizar-setor.md`. O caminho pela tela é assunto da skill `cmv-ajuda`. |
| Qual `acao` tem cada um dos dois avisos de mídia? | `api/arquivos-no-webhook.md` não diz; só descreve o conteúdo de cada um. |
| Onde fica o identificador da mensagem no aviso `fila-data` (QR Code)? | O exemplo com `mensagem.wid` é do `from_internal`; para QR Code o artigo só diz que o texto está em `msg.message`. |
| Como aparece no aviso uma mensagem enviada pela API (`userId`, `fromApp`)? | Os artigos só descrevem o atendente pela tela e o celular da conta. O que está documentado é o `origemDoEvento` igual a `api`. |
| Qual é o payload dos avisos de Webhook Eventos? | `api/webhook-eventos.md` não traz exemplo; só diz que o `acao` vem dentro de `body`. |
| Diferença entre webhook principal e secundário da Conexão | Ver acima. |

Para qualquer uma dessas, o caminho honesto é capturar um aviso real no receptor da pessoa (sem expor o token) e mapear a partir dele, ou perguntar ao Suporte.

## 8. De onde vem cada identificador

| Identificador | De onde vem | Artigo |
|---|---|---|
| `number` (WhatsApp) | Telefone com DDI, DDD e número, só dígitos (ex.: `5511955892164`) | `api/api-mensagem-de-texto.md` |
| `number` de grupo | ID do grupo, que fica no lugar do telefone no ticket do grupo | `api/api-mensagem-para-grupos.md` |
| `number` por LID | O LID do destinatário (ex.: `903280432480329@lid`) | `api/api-mensagem-de-texto-via-lid.md` |
| `number` no Instagram e no Facebook | O `sender` do webhook da mensagem do contato | `api/api-instagram-mensagem-de-texto.md`, `api/api-facebook-mensagem-de-texto.md` |
| `sessionId` (WebChat) | Gerado pelo widget; vem pelo webhook, pela mensagem-marcador do ticket ou pela página de visitantes ao vivo | `api/api-webchat-mensagem-de-texto.md` |
| `ticketId` | Número entre parênteses no cabeçalho da conversa (em **João da Silva (52) \| #25678** é o 52; 25678 é o protocolo); no webhook é o `chamadoId`; a partir do telefone do contato, a API Listar Tickets do Contato (`GET /api/contacts/alltickets`, com `number`) | `api/api-atualizar-ticket.md`, `api/webhooks-da-conexao.md`, `api/api-listar-tickets-do-contato.md` |
| `queueId` | ID do Setor; consulte com a chamada que lista os Setores (o artigo não descreve o formato da resposta) | `api/api-listar-setores-da-empresa.md` |
| `userId` | ID do usuário; aparece no card da pessoa no menu **Equipe**, e há uma chamada que lista os usuários | `recursos/incorporar-atendimento-em-outro-sistema.md`, `api/api-listar-usuarios-da-empresa.md` |
| `contactId` | ID do contato cadastrado na plataforma; há uma chamada que consulta o contato pelo número (o artigo não descreve o formato da resposta) | `api/api-criar-ticket.md`, `api/api-obter-um-contato.md` |
| `connectionId` / `whatsappId` / `whatsappName` | ID ou nome da conexão; lista em **Configurações › Token da Empresa** ou pela chamada de status | `recursos/token-da-empresa-em-configuracoes.md`, `api/api-status-das-conexoes.md` |
| `pipelineId`, `laneId` | Ids de funil e raia; o artigo manda começar por esta listagem, porque não há como adivinhá-los | `api/api-listar-funis.md` |
| `companyId` | Aparece no campo `companyId` das respostas das outras chamadas | `api/api-listar-configuracoes-da-empresa.md` |
