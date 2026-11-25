# Glossário do Chat Master Veloz

Termos que aparecem o tempo todo nas perguntas. Cada definição é um resumo do artigo indicado, em `references/docs/`: abra o artigo antes de dar detalhes, porque aqui só está o suficiente para entender a pergunta e escolher onde ler.

## Estrutura do atendimento

| Termo | O que é | Artigo |
|---|---|---|
| Conexão | Um canal de atendimento ligado à plataforma: cada número de WhatsApp, conta de Instagram, bot de Telegram ou chat de site é uma conexão. | `recursos/conexoes.md` |
| Conexão Padrão | A conexão que a plataforma usa quando precisa escolher um canal sem indicação de qual. | `recursos/visao-geral-conexoes.md` |
| Setor (Fila, Departamento) | Divisão do atendimento por assunto (vendas, suporte, financeiro), com pessoas e horário próprios. Os artigos usam os três nomes para a mesma coisa. | `recursos/setores-e-chatbot.md`, `trilhas/visao-geral-do-sistema.md` |
| Equipe | Cadastro das pessoas que entram na plataforma: perfil, permissões e por onde cada uma atende. | `recursos/equipe.md` |
| Perfil | Admin, Supervisor ou User (o atendente). Decide o tamanho do menu. Entregador e Garçom são perfis de uma tela só. | `recursos/tipos-de-perfil.md` |
| Acesso Limitado | Opção do cadastro que deixa o menu da pessoa só com Chats, em qualquer perfil. | `recursos/tipos-de-perfil.md` |
| Ticket | A conversa de um contato com uma conexão. Um ticket por par contato + conexão; o número não muda. | `recursos/ticket-x-protocolo.md` |
| Protocolo | Cada ciclo de abertura e fechamento dentro do ticket. Avaliação e tag de encerramento ficam no protocolo. | `recursos/ticket-x-protocolo.md` |
| Aguardando | Ticket aberto sem atendente humano (pode ter robô conversando). | `recursos/aguardando-x-atendendo.md` |
| Atendendo | Ticket aberto com atendente humano. | `recursos/aguardando-x-atendendo.md` |
| Encerrado | Ticket fechado. Mensagem nova do cliente reabre em Aguardando, com protocolo novo. Exceção: com **Retornar ao mesmo atendente** ligado no Setor, a resposta dentro de **Minutos para o retorno** volta em Atendendo, com o mesmo atendente. | `recursos/aguardando-x-atendendo.md`, `recursos/aba-geral-em-setores-e-chatbot.md` |
| Carteira de Clientes | Contatos exclusivos de um atendente, o "Proprietário do Lead". | `recursos/carteira-de-clientes.md` |
| Rodízio | Divisão dos atendimentos entre os atendentes. Quando ninguém pode receber, o atendimento vai para o Setor de transbordo ou, com **Aguardar na mesma fila e redistribuir assim que um desocupa** escolhido no cadastro do rodízio, espera a vez no mesmo Setor. | `recursos/rodizios.md`, `recursos/atualizacoes-2026-11-21.md` |
| Mustaches | Variáveis do sistema entre chaves duplas, como `{{firstName}}`, trocadas pelo dado real na mensagem. | `recursos/mustaches.md` |

## WhatsApp e canais

| Termo | O que é | Artigo |
|---|---|---|
| Canal oficial (API Oficial, WhatsApp Oficial) | WhatsApp pela API autorizada pela Meta: tem janela de atendimento, templates e cobrança por mensagem enviada. | `recursos/whatsapp-oficial-x-nao-oficial.md` |
| Canal não oficial (QR Code) | WhatsApp ligado por leitura de QR Code, como o WhatsApp Web; sem templates e sem janela, com risco de bloqueio. | `recursos/whatsapp-oficial-x-nao-oficial.md` |
| Canal não oficial: Básica (Baileys) × Pro (APIdoZap Pro) | As duas bibliotecas do WhatsApp por QR Code; os nomes entre parênteses são os que o Super Admin vê no campo **API Não Oficial** do cadastro da empresa. A Básica foi descontinuada na plataforma: quem a usa deve migrar para a Pro (confirmado pelo dono das skills em 24/11/2026). | `revendedor/api/pre-requisitos-apis.md`, `revendedor/recursos/canais-e-e-mail-em-plataforma.md` |
| Janela de atendimento | Prazo que a Meta abre quando o cliente escreve (24 horas depois da última mensagem dele; 72 horas quando ele chega por anúncio de clique para o WhatsApp). Fora dele, só template. No Instagram e no Messenger, depois de 24 horas só a resposta digitada pelo atendente é enviada, por até 7 dias. | `recursos/janela-de-atendimento.md`, `recursos/whatsapp-oficial-x-nao-oficial.md`, `recursos/atualizacoes-2026-10-31.md` |
| Template | Modelo de mensagem aprovado antes pela Meta; único formato permitido com a janela fechada. | `recursos/mensagem-template.md` |
| Portfólio Empresarial (BM) | O cadastro da empresa dentro da Meta, onde nasce o número da API Oficial e se faz a verificação. | `recursos/portfolio-empresarial-bm.md` |
| Cloud API × Coexistência | Na Cloud API o número vive só na nuvem; na Coexistência continua também no aplicativo WhatsApp Business. | `recursos/adicionar-whatsapp-oficial.md` |
| WABA (Conta do WhatsApp Business) | A conta que guarda os números de WhatsApp Oficial da empresa. Não é sinônimo de API Oficial: é a conta em que os números ficam. | `revendedor/trilhas/meta.md`, `recursos/bloco-carrossel-de-produtos.md` |
| Modo Híbrido | Reparte os envios entre a conexão oficial (Coexistência) e uma por QR Code do mesmo número. | `recursos/whatsapp-modo-hibrido-oficial-e-qrcode.md` |
| "Híbrido" (três sentidos) | Na Central, é o Modo Híbrido da linha acima. Na documentação do revendedor, a palavra aparece em mais dois sentidos: a Coexistência é chamada de "modo híbrido", e o sistema é chamado de híbrido porque um cliente pode usar a integração Nativa e outro o NotificameHub. Se a pessoa disser só "híbrido", pergunte de qual fala. | `revendedor/recursos/como-habilitar-coexistencia.md`, `revendedor/trilhas/meta.md` |
| Modo Alternativo | Leva para uma página, por um botão, uma conversa que começou no WhatsApp Oficial. | `recursos/modo-alternativo-chat-externo-por-link.md` |
| Chat Externo | Conexão própria: uma página de conversa aberta por link, onde a conversa já começa. | `recursos/chat-externo.md` |
| Web Chat | Chat dentro do site do cliente, instalado colando um código. | `recursos/web-chat.md` |
| Concatenador | Junta numa só as mensagens que o atendente envia em sequência. | `recursos/concatenador-de-mensagens.md` |
| Limitador de Mensagens | Contador de envios da conexão oficial; informa, não bloqueia. | `recursos/limitador-de-mensagens.md` |

## Organização, vendas e automação

| Termo | O que é | Artigo |
|---|---|---|
| Tag de Atendimento / Encerramento / CRM | Etiquetas ligadas, nessa ordem, ao ticket, ao protocolo e à oportunidade. | `outros/tipos-de-tags.md` |
| Kanban de Tags | Quadro em que cada tag de atendimento vira uma coluna. | `recursos/kanban-de-tags.md` |
| Quadro de atendimentos | Os mesmos atendimentos da lista de conversas, vistos em colunas. | `recursos/quadro-de-atendimentos.md` |
| Resposta Rápida | Mensagem pronta, chamada no chat digitando `/` e um pedaço do atalho, do texto ou da categoria (ou só o começo do atalho, conforme a **Busca das respostas rápidas** do cadastro de cada pessoa). | `recursos/visao-geral-respostas-rapidas.md`, `recursos/resposta-rapida-envio-de-texto.md` |
| Funil, Etapa, Oportunidade | O funil é o caminho da venda; a oportunidade é o card de cada negociação, que anda pelas etapas. | `recursos/funis-do-crm.md`, `recursos/oportunidade-no-crm.md` |
| Board | O quadro do funil no CRM: cada etapa é uma coluna. | `recursos/board-de-oportunidades.md` |
| FlowBuilder | Construtor de fluxos de conversa; cada etapa é um bloco. No painel, menu FlowBuilder Nativo. | `recursos/flowbuilder.md`, `recursos/blocos.md` |
| Ponto de entrada (gatilho) | O que faz um fluxo começar a rodar numa conversa. | `recursos/pontos-de-entrada.md` |
| Variável de fluxo | Dado guardado pelo fluxo, escrito entre `%`, como `%nome%`. | `recursos/bloco-variavel.md` |
| Token da Conexão / Token da Empresa | Chaves para usar a API: uma por conexão, ou uma só para a empresa inteira. | `recursos/token-da-conexao.md`, `recursos/token-da-empresa-em-configuracoes.md` |
| PWA | A forma de usar a plataforma como aplicativo no celular, instalada pelo navegador. | `recursos/aplicativo.md` |

## Módulos com nomes parecidos

| Termo | O que é | Artigo |
|---|---|---|
| Dashboard / Dashboard (legado) / Meus números | O Dashboard é a tela de números da gestão (administrador e supervisor). O legado é a versão anterior, com outras regras de contagem. Meus números é a página do atendente, só com os números dele. | `recursos/dashboard.md`, `recursos/meus-numeros-do-atendente.md` |
| Agendamentos × Links de agendamento | Agendamento é a mensagem programada para sair depois. Link de agendamento é a página em que o cliente marca uma reunião sozinho; a reunião entra nas Tarefas. | `recursos/agendamentos.md`, `recursos/links-de-agendamento.md` |
| Reservas (recurso, oferta) × Reserva de mesa | Reservas é o módulo de hora marcada ou diária: o recurso recebe a reserva (profissional, mesa, sala, quarto), a oferta é o que o cliente escolhe. Reserva de mesa é do PDV, na página do salão. | `recursos/reservas.md`, `recursos/reservas-de-mesa.md` |
| Campanhas × Mail Marketing | Campanhas são envios em massa pela conexão. Mail Marketing envia e-mails em massa pelas contas de e-mail da empresa, com listas, modelos e relatório próprios. | `recursos/campanhas.md`, `recursos/mail-marketing.md` |
| GPT Assistant × Assistente de IA | O GPT Assistant é o prompt de IA que responde clientes num Setor. O Assistente de IA responde perguntas da equipe sobre os dados da plataforma e não muda nada. | `recursos/gpt-assistant.md`, `recursos/assistente-de-ia.md` |
| Base de Conhecimento | Material da empresa (horários, preços, políticas) que a IA consulta antes de responder; é vinculada a um prompt. | `recursos/base-de-conhecimento-do-gpt-assistant.md` |
| Consultório | Módulo de clínica: agenda das consultas, recepção, pacientes e prontuário, ligados às conversas. | `recursos/consultorio.md` |
| Gravações × Chamadas | **Gravações** é a página das chamadas gravadas dentro da plataforma: videochamadas dos atendimentos, chamadas do Chat Interno e reuniões das tarefas. As gravações das ligações do PABX vão para outro menu, **Chamadas**. | `recursos/gravacoes-das-chamadas.md`, `revendedor/recursos/como-habilitar-gravacoes-no-pabx.md` |

## Revendedor e instância

Termos da documentação do revendedor, em `references/docs/revendedor/`. O cliente de uma empresa não tem essas telas: veja "Cliente ou revendedor", no `SKILL.md`.

| Termo | O que é | Artigo |
|---|---|---|
| Instância | O conjunto das empresas que um revendedor administra. O que é da instância vale para todas as empresas ao mesmo tempo. | `revendedor/recursos/configuracoes.md` |
| Super Admin (revendedor) | Quem administra a instância: as empresas, os planos que elas assinam, a identidade visual e os meios de pagamento. Só ele vê o card **Plataforma**. | `revendedor/recursos/configuracoes.md`, `revendedor/recursos/plataforma-em-configuracoes.md` |
| Plano | O pacote que a empresa assina: decide quantos usuários, conexões e Setores ela pode ter e quais recursos aparecem no menu dela. Qual opção libera cada recurso está em `references/liberar-recursos.md`. | `revendedor/recursos/configuracoes-planos.md` |
| Aplicativo próprio × aplicativo da plataforma (Portal) | Os dois caminhos dos canais oficiais da Meta: pelo aplicativo do próprio revendedor, aprovado na Meta, ou pelo aplicativo da plataforma, sem aprovar aplicativo nenhum. No plano, o aplicativo próprio é **WABA WL** no WhatsApp e **INC** no Facebook e no Instagram. | `revendedor/recursos/configuracoes-planos.md`, `revendedor/trilhas/api-oficial-nativa.md` |
