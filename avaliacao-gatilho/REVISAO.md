# Revisão dos pedidos de teste (medição de 18/11)

> Medição de 18/11, com as descrições daquela data e o medidor por skill. A revisão atual é `REVISAO-ROTEAMENTO.md`.

Cada linha é um pedido usado para medir o acionamento. **Esperado** diz se a skill da seção deve ser carregada. As colunas dos modelos mostram em quantas das repetições ela foi carregada; ❌ marca o resultado que contraria o esperado (acionou em menos da metade quando devia, ou na metade ou mais quando não devia). Um traço significa que o conjunto não foi medido naquele modelo.

O que revisar: (1) o rótulo **Esperado** está certo? (2) o pedido parece com o que seus usuários escrevem? (3) falta algum tipo de pedido? Para corrigir, edite o arquivo `.json` do conjunto e rode `ferramenta/medir.py` de novo.

## cmv-agente-ia

### `otimizacao/cmv-agente-ia.json` (usados para otimizar a descrição)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | oi, tenho uma clínica de estética e queria colocar o chatgpt pra responder o whatsapp no chat master veloz, tirar duvida de preço e já deixar a avaliação agendada. como faço? | aciona | 3/3 | – | – | – |
| 2 | minha IA do CMV fala que vai transferir pro atendente e não transfere. o prompt é esse: 'quando pedir humano diga que vai transferir #{"queueId": "12"}' | aciona | 3/3 | – | – | – |
| 3 | apareceu um botão de estrelinha do lado do campo de mensagem no chat master veloz, é sugestão de resposta da IA? gasta crédito? | aciona | 3/3 | – | – | – |
| 4 | como ligo a transcrição de áudio no chat master veloz? os clientes mandam muito áudio e a equipe não consegue ouvir tudo | aciona | 3/3 | – | – | – |
| 5 | escreve um prompt de atendente virtual pra minha loja de pneus no chatmasterveloz, que responda medida e preço e passe pro vendedor | aciona | 3/3 | – | – | – |
| 6 | a avaliação pela IA do chat master veloz deu nota baixa pros meus atendimentos, como ela calcula essa nota? | aciona | 3/3 | – | – | – |
| 7 | qual temperatura e quantos tokens eu coloco no prompt do GPT Assistant do cmv? | aciona | 3/3 | – | – | – |
| 8 | o tipo Agente OpenAI sumiu do chat master veloz, como migro meu assistente antigo? | aciona | 3/3 | – | – | – |
| 9 | quero um robô inteligente no chat master veloz que não invente preço e passe pra humano quando não souber responder | aciona | 3/3 | – | – | – |
| 10 | dá pra usar o GPT assistant do chat master veloz dentro de um grupo de whatsapp? | aciona | 3/3 | – | – | – |
| 11 | monta um fluxo no flowbuilder do chat master veloz com menu de 3 opções que manda pro setor certo | não aciona | 0/3 | – | – | – |
| 12 | escreve 5 respostas rápidas de pós-venda pra minha loja no chat master veloz | não aciona | 0/3 | – | – | – |
| 13 | como crio um GPT personalizado no ChatGPT pra responder os clientes da minha loja? | não aciona | 0/3 | – | – | – |
| 14 | escreve um system prompt pra um bot de atendimento no Botpress | não aciona | 0/3 | – | – | – |
| 15 | como envio uma mensagem pela API do chat master veloz a partir do meu sistema em node? | não aciona | 0/3 | – | – | – |
| 16 | onde vejo o relatório de atendimentos por atendente no chat master veloz? | não aciona | 0/3 | – | – | – |
| 17 | quero trocar a fonte e as cores do painel do CMV pras da minha marca | não aciona | 0/3 | – | – | – |
| 18 | integrar a API da OpenAI no meu app python pra resumir textos longos | não aciona | 0/3 | – | – | – |
| 19 | como cadastro um atendente novo e defino os setores dele no chat master veloz? | não aciona | 0/3 | – | – | – |
| 20 | escreve uma mensagem de campanha pra divulgar a black friday no chat master veloz | não aciona | 0/3 | – | – | – |

### `validacao/cmv-agente-ia.json` (nunca vistos pelo otimizador)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | dá pra IA do chat master veloz marcar uma tag de 'lead quente' quando o cliente pede orçamento? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | meu assistente de IA do CMV tá gastando muito token, o que eu ajusto? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | quero que a IA do chatmasterveloz resuma a conversa antes de passar pro atendente humano, tem como? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | o copiloto de mensagens do chat master veloz serve pra quê? como uso? | aciona | 3/3 | 3/3 | 3/3 | 1/3 ❌ |
| 5 | cria a IA de atendimento da minha pizzaria no chat master veloz pra tirar pedido e passar pro balcão | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | como treino um agente no Dialogflow pra responder dúvidas da minha loja? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | escreve um prompt pro ChatGPT me ajudar a responder email de cliente | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | monta um fluxo no flowbuilder do chat master veloz que pergunta o pedido da pizza e manda pro setor balcão | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | quero colocar a chave da API do Asaas no chat master veloz, onde fica? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | melhora o texto da minha resposta rápida de cardápio no chat master veloz | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

### `independentes/cmv-agente-ia.json` (escritos por um agente que não viu os outros pedidos nem as descrições)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | Quero colocar uma IA pra responder os clientes da minha imobiliária no Chat Master Veloz. Ela precisa perguntar se é compra ou aluguel, o bairro e a faixa de preço, e só depois passar pro corretor. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | minha ia do cmv ta inventando preço q nao existe e nao transfere pro humano qdo o cliente pede. como arrumo isso no prompt? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | No menu Prompts OPEN.AI, além do texto do prompt, o que mais eu preciso preencher? E como faço o assistente responder só no setor Suporte e não nos outros? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | Quero ajustar as instruções da Sugestão de resposta IA (aquele botão do copiloto na conversa) pra ele sugerir respostas mais curtas, sem emoji e sempre chamando o cliente pelo nome. O que escrevo lá? uso o chatmasterveloz | aciona | 3/3 | 3/3 | 3/3 | 2/3 |
| 5 | Sou dona de uma escola de inglês com 3 unidades e atendo pelo CMV. Quero uma atendente virtual chamada Bia no GPT Assistant: ela informa as mensalidades (R$ 389 kids e R$ 429 adultos), os horários das turmas, marca aula experimental anotando nome, idade e unidade, nunca promete desconto e transfere para o setor Secretaria quando perguntarem de boleto ou rematrícula. Tom simpático e sem textão. Escreve o prompt completo e me diz onde colar e como testar. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | Cria um GPT personalizado no ChatGPT (pelo GPT Builder) pra tirar dúvidas dos pacientes da minha clínica: quero as instruções e os conversation starters. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | Escreve o system prompt do meu agente de atendimento que roda no n8n, com o nó AI Agent ligado na Evolution API, pra uma barbearia. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | Monta um fluxo no FlowBuilder com um menu de 3 opções: na opção 'Dúvidas' a conversa vai pro bloco GPT Assistant, nas outras duas vai direto pro setor. Quero o roteiro de montagem. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | Preciso receber no meu sistema, por webhook, o resultado da Avaliação pela IA de cada atendimento encerrado no CMV. Como é o payload e como cadastro a URL? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | Redige o template de confirmação de consulta pra API Oficial, com nome do paciente, data e hora nas variáveis, pra eu cadastrar no Chat Master Veloz. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

## cmv-ajuda

### `otimizacao/cmv-ajuda.json` (usados para otimizar a descrição)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | como eu faço pra uma atendente só ver as conversas do setor financeiro no chat master veloz? ela não pode mexer em configuração nenhuma | aciona | 3/3 | – | – | – |
| 2 | meu whatsapp desconectou no CMV e as conversas ficaram tudo vermelhas, como reconecto sem perder nada? | aciona | 3/3 | – | – | – |
| 3 | Onde fica a opção de encerrar sozinho o atendimento quando o cliente para de responder? uso o chatmasterveloz | aciona | 3/3 | – | – | – |
| 4 | qual a diferença entre ticket e protocolo no chat master veloz? meu supervisor ficou confuso no relatório de ontem | aciona | 3/3 | – | – | – |
| 5 | o que mudou no sistema essa semana? apareceu um menu novo 'Assistente de IA' no painel do chat master veloz e ninguém avisou | aciona | 3/3 | – | – | – |
| 6 | Como importo minha lista de contatos de uma planilha pro chat master veloz? tenho uns 3 mil contatos num excel com nome e telefone | aciona | 3/3 | – | – | – |
| 7 | no painel do cmv, como transfiro um atendimento pra outro atendente sem ele perder o histórico da conversa? | aciona | 3/3 | – | – | – |
| 8 | como funciona o rodízio no chat master veloz? quero distribuir os leads igual entre 4 vendedores | aciona | 3/3 | – | – | – |
| 9 | acabamos de contratar o chat master veloz, por onde eu começo? já tenho o número da empresa e 3 atendentes | aciona | 3/3 | – | – | – |
| 10 | a mensagem do cliente não aparece no Aguardando do chat master veloz, só chega no celular. o que pode ser? | aciona | 3/3 | – | – | – |
| 11 | preciso de um curl pra mandar mensagem de texto pela API do chat master veloz pro cliente quando o pedido for aprovado no meu sistema | não aciona | 0/3 | – | – | – |
| 12 | monta um fluxo no flowbuilder do cmv com menu de 3 opções e horário de expediente, quero o json pra importar | não aciona | 0/3 | – | – | – |
| 13 | escreve o prompt do GPT Assistant do chat master veloz pra minha imobiliária responder dúvidas de aluguel | não aciona | 0/3 | – | – | – |
| 14 | cria 10 respostas rápidas pra recepção da minha clínica no chat master veloz: saudação, pix, endereço e confirmação | não aciona | 0/3 | – | – | – |
| 15 | quero mudar a cor do menu lateral do painel do chat master veloz pro verde da minha marca usando css personalizado | não aciona | 0/3 | – | – | – |
| 16 | como configuro o chatbot no Blip pra transferir pro atendente humano quando o cliente pedir? | não aciona | 0/3 | – | – | – |
| 17 | no WhatsApp Business do celular, como crio etiquetas e a mensagem de ausência? | não aciona | 0/3 | – | – | – |
| 18 | escreve um template de cobrança pra API oficial do WhatsApp no chat master veloz, categoria utilidade, com nome e valor | não aciona | 0/3 | – | – | – |
| 19 | o webhook da conexão do CMV manda tudo duplicado pro meu n8n, como filtro isso no workflow? | não aciona | 0/3 | – | – | – |
| 20 | no Chatwoot, como faço pra um agente ver só a caixa de entrada do financeiro? | não aciona | 0/3 | – | – | – |

### `validacao/cmv-ajuda.json` (nunca vistos pelo otimizador)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | no chat master veloz, como faço pra um contato ficar sempre com o mesmo atendente quando volta a chamar? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | por que aparece 'Missing Body in Payload' quando a gente tenta responder um cliente no CMV? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | como ativo a autenticação em dois fatores pra equipe no chat master veloz? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | dá pra instalar o chat master veloz como aplicativo no celular dos atendentes? como recebe notificação? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 5 | Como crio um funil no CRM do chatmasterveloz e movo a oportunidade de etapa? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | no Zenvia, como faço pra transferir a conversa pra outro departamento? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | como crio uma lista de transmissão no whatsapp business do meu celular? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | escreve o texto da mensagem de encerramento do atendimento do chat master veloz, curtinho e simpático | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | me dá um exemplo em node pra criar contato pela API do chat master veloz | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | a IA do chat master veloz responde em inglês às vezes, como arrumo no prompt? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

### `independentes/cmv-ajuda.json` (escritos por um agente que não viu os outros pedidos nem as descrições)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | Como faço pra ativar o rodízio de atendimento num setor do Chat Master Veloz? Tenho 4 vendedores e quero que os leads novos sejam distribuídos por igual entre eles. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | meu whatsapp desconectou no cmv e agora nao le mais o qr code, fica carregando.. o q eu faço?? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | Sou supervisora de uma clínica odontológica e a gente usa o chatmasterveloz. Os tickets que estão em Atendendo voltam sozinhos para Aguardando depois de um tempo. Isso é alguma configuração? Onde eu desligo? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | o que entrou de novidade no CMV agora em novembro? queria saber principalmente o que mudou no CRM | aciona | 3/3 | 3/3 | 3/3 | 2/3 |
| 5 | Tenho uma imobiliária com 6 corretores usando o painel do Master Veloz. Quero que cada cliente caia sempre com o mesmo corretor que atendeu da primeira vez (acho que o nome disso é carteira de clientes) e que, quando o corretor estiver de férias, a conversa vá para o setor em vez de ficar parada. Como configuro isso, quem precisa ser administrador e o que acontece com os clientes que já estão cadastrados? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | Escreve pra mim 8 respostas rápidas pro setor financeiro da minha escola no CMV: segunda via de boleto, negociação de atraso, confirmação de pagamento, nota fiscal e por aí vai. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | Monta um fluxo no FlowBuilder que pergunta o CPF do cliente, marca a tag 'inadimplente' e transfere para o setor Cobrança. Se ele não responder em 20 minutos, encerra. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | Preciso do código em PHP para criar um contato e abrir um ticket no Chat Master Veloz pela API toda vez que alguém preencher o formulário de orçamento do meu site. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | Como cadastro um agente novo no Chatwoot e deixo ele restrito a uma única caixa de entrada? Uso a versão self-hosted. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | No aplicativo WhatsApp Business do celular, onde configuro a mensagem de ausência e o horário de funcionamento da empresa? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

## cmv-api

### `otimizacao/cmv-api.json` (usados para otimizar a descrição)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | Preciso que meu sistema em PHP mande um WhatsApp pelo Chat Master Veloz quando o pagamento for aprovado. Qual endpoint e payload? | aciona | 3/3 | – | – | – |
| 2 | no n8n eu recebo as mensagens do CMV pelo webhook da conexão mas chega tudo duplicado e áudio vem vazio. conexão é API oficial. como arrumo? | aciona | 3/3 | – | – | – |
| 3 | me passa um curl pra transferir o ticket 4521 pro setor financeiro e adicionar a tag Cobrança sem apagar as outras, chat master veloz | aciona | 3/3 | – | – | – |
| 4 | onde pego o token pra usar a API do chat master veloz? e qual a diferença entre token da empresa e token da conexão? | aciona | 3/3 | – | – | – |
| 5 | quero que o formulário do meu site crie o contato no chatmasterveloz e já dispare um fluxo, como faço isso sem expor o token? | aciona | 3/3 | – | – | – |
| 6 | a chamada de enviar imagem por url do CMV tá voltando 401, minha conexão é a pro. o que eu confiro? | aciona | 3/3 | – | – | – |
| 7 | como recebo no meu servidor um aviso toda vez que um ticket é encerrado no chat master veloz? | aciona | 3/3 | – | – | – |
| 8 | script python pra puxar as oportunidades de um funil do CRM do chat master veloz e jogar numa planilha | aciona | 3/3 | – | – | – |
| 9 | integrar o Make com o chat master veloz pra mandar template da API oficial quando entrar lead novo no RD Station | aciona | 3/3 | – | – | – |
| 10 | Qual o payload pra mandar mensagem de lista pela API do CMV numa conexão básica de qr code? | aciona | 3/3 | – | – | – |
| 11 | como um atendente transfere um atendimento pra outro setor pelo painel do chat master veloz? | não aciona | 0/3 | – | – | – |
| 12 | monta um fluxo no flowbuilder do cmv que pergunta o CPF e consulta meu sistema pelo bloco HTTP Request antes de responder | não aciona | 0/3 | – | – | – |
| 13 | escreve o texto de um template de confirmação de consulta pra API oficial no chat master veloz | não aciona | 0/3 | – | – | – |
| 14 | onde coloco a chave da OpenAI no chat master veloz pra ligar o GPT Assistant? | não aciona | 0/3 | – | – | – |
| 15 | dá pra colocar um script no JS personalizado do painel do CMV que mostra um aviso quando abre a tela de contatos? | não aciona | 0/3 | – | – | – |
| 16 | como integrar a Z-API com meu sistema em PHP pra mandar mensagem no whatsapp? | não aciona | 0/3 | – | – | – |
| 17 | na Cloud API da Meta, como envio um template com variável chamando a graph api direto, sem plataforma no meio? | não aciona | 0/3 | – | – | – |
| 18 | no painel do chat master veloz, como tiro um relatório dos atendimentos encerrados por atendente no mês? | não aciona | 0/3 | – | – | – |
| 19 | quero fazer uma campanha de disparo pra 800 clientes inativos no chat master veloz, me ajuda com o texto | não aciona | 0/3 | – | – | – |
| 20 | configurar o nó HTTP Request do n8n pra chamar a API do Pipedrive com OAuth2 | não aciona | 0/3 | – | – | – |

### `validacao/cmv-api.json` (nunca vistos pelo otimizador)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | tem endpoint no chat master veloz pra listar as mensagens de um ticket? quero salvar o histórico no meu banco | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | como mando um pdf por url pela api da conexão oficial no chat master veloz? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | quero que o CMV avise meu ERP quando uma tag 'Venda fechada' for aplicada no ticket, dá pra fazer por webhook? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | no zapier, como chamo o chatmasterveloz pra mandar mensagem quando chegar um pedido novo no shopify? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 5 | erro 400 pedindo whatsappId quando uso o token da empresa na api do chat master veloz, o que falta? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | como gero o QR code pra conectar um número novo no chat master veloz? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | escreve o prompt do assistente de IA do chat master veloz pra vender planos de internet | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | como uso a API do Twilio pra mandar SMS em python? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | monta um fluxo no flowbuilder do chat master veloz que chama um webhook do n8n e responde com o resultado | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | texto de template de rastreio de pedido pra API oficial no chat master veloz | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

### `independentes/cmv-api.json` (escritos por um agente que não viu os outros pedidos nem as descrições)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | O sistema de agendamento da minha clínica é próprio, feito em Laravel. Quero que ele mande um lembrete pelo WhatsApp um dia antes da consulta usando o Chat Master Veloz, com o nome do paciente e o horário. A conexão é WhatsApp por QR Code. Me passa o código da chamada e onde pego o token. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | como configuro o webhook do cmv pra receber no n8n toda msg que chega? e qual o formato do json q ele manda | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | qual é o endpoint e o corpo do POST pra mandar um pdf pelo whatsapp via api do chatmasterveloz? manda um exemplo em curl pfv | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | Preciso manter meu ERP sincronizado com o CRM do CMV: sempre que uma oportunidade mudar de etapa no funil, quero receber um aviso no meu servidor e atualizar o registro do meu lado. Existe webhook do funil? Como recebo e trato isso em Node? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 5 | Meu sistema de notas fiscais precisa disparar, pelo Master Veloz, um template já aprovado na API Oficial assim que a nota é emitida, preenchendo nome do cliente e número da nota nas variáveis. Como fica a requisição em Python? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | Como envio uma mensagem de texto pela Z-API usando Node? Preciso do endpoint send-text e de como passar o client-token no header. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | Quero mandar um template de WhatsApp direto pela Cloud API da Meta, sem plataforma nenhuma no meio, chamando o Graph API em Python. Qual é o endpoint e o payload? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | No FlowBuilder do CMV, quero um fluxo que pergunta o número do pedido, guarda numa variável e depois mostra um menu com 'Acompanhar entrega' e 'Falar com atendente'. Monta pra mim? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | Escreve o texto de um template de utilidade avisando que o pedido saiu para entrega, com variável para o nome e para o código de rastreio, pra eu cadastrar na Gestão de Templates do CMV. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | Como conecto um número na API Oficial do WhatsApp dentro do Chat Master Veloz? Já tenho a BM verificada, só não sei por onde começo no painel. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

## cmv-flowbuilder

### `otimizacao/cmv-flowbuilder.json` (usados para otimizar a descrição)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | tenho uma clínica de estética e quero um robozinho no whats do chat master veloz que pergunte se a pessoa quer agendar, saber preço ou falar com alguém, e mande pro setor certo. dá pra me mandar o arquivo pronto pra importar? | aciona | 3/3 | – | – | – |
| 2 | meu fluxo do flowbuilder trava depois que o cliente digita o cpf, não responde mais nada. segue o json que exportei | aciona | 3/3 | – | – | – |
| 3 | quero mandar uma mensagem automática 1 dia depois pra quem pediu orçamento e sumiu. uso a API oficial no CMV. como monto isso? | aciona | 3/3 | – | – | – |
| 4 | qual bloco do flowbuilder eu uso pra checar se tá no horário de expediente antes de mandar pro setor? | aciona | 3/3 | – | – | – |
| 5 | monta um fluxo de qualificação de lead no chat master veloz: pergunta nome, cidade e orçamento e manda pro vendedor por rodízio | aciona | 3/3 | – | – | – |
| 6 | no chatmasterveloz quero que quem comentar 'eu quero' no meu post do instagram receba o link no direct automático | aciona | 3/3 | – | – | – |
| 7 | como faço o fluxo do chat master veloz consultar meu sistema pelo número do cliente e responder o status do pedido? | aciona | 3/3 | – | – | – |
| 8 | revisa esse fluxo de cobrança que montei no flowbuilder do cmv, acho que tem alguma saída sem ligação | aciona | 3/3 | – | – | – |
| 9 | dá pra fazer um menu automático no cmv que manda o boleto do Asaas quando o cliente escolhe a opção 2? | aciona | 3/3 | – | – | – |
| 10 | preciso de um chatbot de pós-venda no chat master veloz que pergunta a nota de 1 a 5 e marca tag de insatisfeito quando dá menos de 3 | aciona | 3/3 | – | – | – |
| 11 | escreve o prompt do agente de IA do chat master veloz pra qualificar leads de energia solar | não aciona | 0/3 | – | – | – |
| 12 | preciso de um curl pra iniciar um fluxo do chat master veloz a partir do meu sistema quando entra um lead novo | não aciona | 0/3 | – | – | – |
| 13 | cria as mensagens de saudação e de fora do horário do setor de vendas no chat master veloz, tom simpático | não aciona | 0/3 | – | – | – |
| 14 | como vejo quais atendentes estão online agora no painel do chat master veloz? | não aciona | 0/3 | – | – | – |
| 15 | monta um fluxo no Typebot com captura de email e integração com o google sheets | não aciona | 0/3 | – | – | – |
| 16 | como faço um fluxo no ManyChat pra responder comentário do instagram com link no direct? | não aciona | 0/3 | – | – | – |
| 17 | quero esconder o botão de excluir conversa pros atendentes no painel do CMV | não aciona | 0/3 | – | – | – |
| 18 | workflow no n8n que lê os emails do gmail e salva no notion | não aciona | 0/3 | – | – | – |
| 19 | escreve um template de reengajamento pra API oficial do chat master veloz, pra quem não responde há 3 dias | não aciona | 0/3 | – | – | – |
| 20 | a IA do chat master veloz não transfere pro setor quando o cliente pede pra falar com humano, o prompt tá abaixo | não aciona | 0/3 | – | – | – |

### `validacao/cmv-flowbuilder.json` (nunca vistos pelo otimizador)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | o robô do chat master veloz fica repetindo o menu toda hora mesmo quando o cliente escolhe a opção, o que tá errado? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | olha esse json do meu fluxo do cmv e me diz por que ele não manda pro setor de vendas | aciona | 1/3 ❌ | 3/3 | 3/3 | 3/3 |
| 3 | quero que no chat master veloz o cliente que mandar mensagem de madrugada receba aviso de fora do horário e caia num menu de manhã | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | como faço um fluxo do chatmasterveloz que pergunta o nome, guarda numa variável e usa depois na mensagem? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 5 | monta um robô de agendamento pra barbearia no chat master veloz com escolha de serviço e dia | aciona | 3/3 | 3/3 | 3/3 | 2/3 |
| 6 | monta um bot no Botpress que agenda horário de barbearia | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | cria a resposta rápida de 'fora do horário' pra recepção usar no chat master veloz | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | quero que o atendente do chat master veloz veja só os atendimentos dele, como configuro? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | a IA do chat master veloz não usa o nome do cliente quando responde, como faço ela usar? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | como crio um fluxo no zapier que manda email quando entra linha nova no google sheets? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

### `independentes/cmv-flowbuilder.json` (escritos por um agente que não viu os outros pedidos nem as descrições)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | Preciso de um chatbot pra minha pizzaria no Chat Master Veloz: saudação, opções Cardápio / Fazer pedido / Falar com atendente, e quando a gente está fechado (abrimos de terça a domingo, 18h às 23h30) avisa o horário. Dá pra me entregar o arquivo pra importar? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | meu fluxo no flowbuilder trava no bloco de pergunta, o cliente responde e nao acontece mais nada. como eu descubro onde ta o erro? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | Quero uma automação no CMV que, 2 dias depois de eu colocar a tag 'orçamento enviado' no contato, mande uma mensagem perguntando se ele ainda tem interesse. Se responder que sim, vai pro setor Vendas; se não responder, tira a tag e encerra. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | no fluxo do cmv, como uso o bloco Condição ou o Switch de tags pra separar cliente novo de quem ja é cliente e mandar cada um pra um menu diferente? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 5 | Tenho um escritório de advocacia e uso o chatmasterveloz com WhatsApp por QR Code. Quero uma triagem automática: pergunta o nome, a área (trabalhista, família ou previdenciário) e se a pessoa já é cliente. Se for previdenciário, pede também idade e tempo de contribuição. No fim, deixa um resumo em mensagem interna para a equipe e transfere para o setor da área escolhida. Fora do horário comercial, avisa que retornamos no próximo dia útil. Me dá o roteiro bloco a bloco para eu montar no editor. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | Como monto no Typebot um bot com botões de escolha e uma condição de horário comercial? Vou hospedar na minha VPS e ligar na Evolution API. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | No ManyChat, como faço um flow que dispara quando comentam 'quero' no meu post do Instagram e manda o link por DM? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | Cria o prompt do GPT Assistant pra fazer a triagem dos clientes da minha loja de pneus no CMV: ele pergunta a medida do pneu e a cidade antes de passar pro vendedor. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | Já tenho o fluxo pronto no FlowBuilder. Agora só preciso da chamada HTTP (um curl serve) pro meu ERP disparar esse fluxo para um número pelo Gatilho via API. Qual o endpoint, o token e o corpo? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | Como crio uma tag de atendimento nova e faço ela aparecer como coluna no Kanban de Tags do Chat Master Veloz? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

## cmv-mensagens

### `otimizacao/cmv-mensagens.json` (usados para otimizar a descrição)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | migrei pra API oficial no chat master veloz e preciso de um template de cobrança de mensalidade que não seja reprovado. tem como mandar automático todo dia 5? | aciona | 3/3 | – | – | – |
| 2 | cria respostas rápidas pra recepção da minha clínica odontológica no CMV: saudação, confirmar consulta, localização, pix e pós-atendimento | aciona | 3/3 | – | – | – |
| 3 | quero fazer uma campanha pra reativar uns 800 clientes que não compram há 6 meses no chat master veloz, me ajuda com o texto | aciona | 3/3 | – | – | – |
| 4 | escreve a mensagem de aniversário automática do chat master veloz pra minha academia | aciona | 3/3 | – | – | – |
| 5 | meu template de marketing foi reprovado pela meta no chatmasterveloz, como eu reescrevo pra passar? | aciona | 3/3 | – | – | – |
| 6 | qual variável eu uso pra colocar o primeiro nome do cliente na resposta rápida do chat master veloz? | aciona | 3/3 | – | – | – |
| 7 | faz a mensagem de fora do horário e a de saudação do setor de vendas no CMV, tom descontraído | aciona | 3/3 | – | – | – |
| 8 | texto pra lembrete de consulta 1 dia antes, vou usar o agendamento de mensagem do chat master veloz | aciona | 3/3 | – | – | – |
| 9 | quanto custa mandar template de utilidade pelo chat master veloz depois que a meta mudou a cobrança? | aciona | 3/3 | – | – | – |
| 10 | melhora esse texto de carrinho abandonado que eu mando pelo chat master veloz: 'oi, vi que vc nao finalizou a compra' | aciona | 3/3 | – | – | – |
| 11 | como envio template com variáveis pela API do chat master veloz a partir do meu sistema? qual payload? | não aciona | 0/3 | – | – | – |
| 12 | monta um fluxo no flowbuilder do chat master veloz de pesquisa de satisfação com nota de 1 a 5 | não aciona | 0/3 | – | – | – |
| 13 | escreve o prompt da IA do chat master veloz pra responder dúvidas de matrícula da minha escola | não aciona | 0/3 | – | – | – |
| 14 | como conecto o whatsapp oficial no chat master veloz? já tenho a BM verificada | não aciona | 0/3 | – | – | – |
| 15 | escreve um email marketing de black friday pra mandar pelo mailchimp | não aciona | 0/3 | – | – | – |
| 16 | cria um template de mensagem no gerenciador do WhatsApp da Meta pra minha empresa, eu uso a Zenvia | não aciona | 0/3 | – | – | – |
| 17 | deixa o balão das mensagens enviadas no painel do chat master veloz com outra cor | não aciona | 0/3 | – | – | – |
| 18 | as mensagens do cliente não aparecem no Aguardando do chat master veloz, o que pode ser? | não aciona | 0/3 | – | – | – |
| 19 | escreve uma legenda de instagram pra divulgar meu restaurante japonês | não aciona | 0/3 | – | – | – |
| 20 | meu webhook do CMV não recebe as mensagens de áudio, só texto | não aciona | 0/3 | – | – | – |

### `validacao/cmv-mensagens.json` (nunca vistos pelo otimizador)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | preciso de um template de confirmação de entrega pra API oficial no chat master veloz, com o número do pedido | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | escreve 3 variações de mensagem pra campanha de reabertura da loja no CMV pelo qr code sem risco de bloqueio | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | a mensagem de boas-vindas do meu setor no chat master veloz tá muito seca, reescreve mais acolhedora | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | qual categoria escolho pro template de código de verificação no chatmasterveloz, utilidade ou autenticação? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 5 | monta respostas rápidas pra equipe de suporte técnico no chat master veloz: pedir print, pedir número de série e encerrar | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | como envio a resposta rápida pelo atalho dentro da conversa no chat master veloz? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | escreve um roteiro de ligação de cobrança pra minha equipe de telemarketing | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | monta um fluxo no flowbuilder do chat master veloz que manda a segunda via do boleto | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | como faço pra mandar template pela API do chat master veloz com botão de url? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | cria uma sequência de emails de boas-vindas pro meu curso online no hotmart | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

### `independentes/cmv-mensagens.json` (escritos por um agente que não viu os outros pedidos nem as descrições)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | Cria umas 10 respostas rápidas pra minha loja de roupas no Chat Master Veloz: prazo de entrega, troca e devolução, tabela de medidas, formas de pagamento, chave pix e agradecimento pós-compra. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | Meu template foi reprovado pela Meta duas vezes. O texto era: 'Olá {{1}}, aproveite 30% OFF só hoje!!! Clique já e garanta'. Cadastrei como utilidade. Reescreve de um jeito que passe, me diz a categoria certa e o que preencher na Gestão de Templates. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | Vou fazer uma campanha de Black Friday no CMV pelo WhatsApp de QR Code para uns 1.200 contatos da minha loja de suplementos. Escreve as variações da mensagem e me diz como reduzir o risco de o número ser bloqueado. | aciona | 3/3 | 3/3 | 3/3 | 2/3 |
| 4 | quero agendar no chatmasterveloz uma msg todo dia 5 lembrando os alunos da mensalidade da academia. como escrevo isso e coloco o nome de cada um? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 5 | texto pra mensagem de aniversário e pra msg de fora do expediente do setor comercial, tom descontraido, é uma barbearia (uso o master veloz) | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | Como cadastro a mensagem de saudação e as respostas rápidas no aplicativo WhatsApp Business? Aproveita e me sugere os textos, é pra um salão de beleza. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | Escreve um template de marketing pra eu cadastrar direto no Gerenciador do WhatsApp da Meta; quem dispara pra mim é a Zenvia. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | Me passa o JSON do POST pra enviar um template aprovado com duas variáveis pela API do Chat Master Veloz, de preferência com exemplo em Node. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | No FlowBuilder, como configuro o bloco Template pra mandar meu template já aprovado no começo do fluxo e seguir por caminhos diferentes conforme o botão que o cliente clicar? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | Escreve o prompt da IA do CMV pra ela responder dúvidas de troca e devolução no tom da minha marca, que é jovem e direto. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

## cmv-painel-css-js

### `otimizacao/cmv-painel-css-js.json` (usados para otimizar a descrição)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | oi, queria deixar o painel do chat master veloz com as cores da minha empresa (verde #0f766e), e no modo escuro ele fica todo cinza, dá pra arrumar? | aciona | 3/3 | – | – | – |
| 2 | coloquei um css no CMV pra mudar a lista de atendimentos e depois da última atualização parou de funcionar: .MuiListItem-root.jss412 { border-radius: 12px } | aciona | 3/3 | – | – | – |
| 3 | preciso que apareça um aviso pro pessoal quando abrir a tela de contatos do chat master veloz lembrando de não importar planilha sem falar com a supervisão | aciona | 3/3 | – | – | – |
| 4 | dá pra esconder o menu de campanhas pros atendentes no painel do chatmasterveloz com css? | aciona | 3/3 | – | – | – |
| 5 | trocar o fundo da tela de login do chat master veloz pela cor da marca e tirar o link de cadastro | aciona | 3/3 | – | – | – |
| 6 | aumentar a fonte das mensagens no chat do painel do cmv, a equipe reclama que tá pequena | aciona | 3/3 | – | – | – |
| 7 | qual seletor eu uso pra mudar a cor do balão de nota interna no chat master veloz? | aciona | 3/3 | – | – | – |
| 8 | JS personalizado no chat master veloz que toca um som quando chega ticket novo no aguardando | aciona | 3/3 | – | – | – |
| 9 | mudar a ordem dos itens do menu lateral do painel do CMV, quero contatos em primeiro | aciona | 3/3 | – | – | – |
| 10 | personalizar o visual do chat externo do chat master veloz que eu mando por link pros clientes | aciona | 3/3 | – | – | – |
| 11 | como mudo a foto de perfil do número de whatsapp no chat master veloz? | não aciona | 0/3 | – | – | – |
| 12 | quero que meu site chame a API do chat master veloz pra mandar mensagem quando alguém preencher o formulário | não aciona | 0/3 | – | – | – |
| 13 | como instalo o web chat do chat master veloz no meu site wordpress? | não aciona | 0/3 | – | – | – |
| 14 | css pra deixar o botão do meu site wordpress verde com efeito hover | não aciona | 0/3 | – | – | – |
| 15 | como alterar o tema do Chatwoot pra dark mode? | não aciona | 0/3 | – | – | – |
| 16 | como restrinjo o que o atendente pode ver nas permissões do chat master veloz? | não aciona | 0/3 | – | – | – |
| 17 | escreve a mensagem de saudação do setor de suporte no chat master veloz | não aciona | 0/3 | – | – | – |
| 18 | monta um fluxo no flowbuilder que manda o cliente pra um webview com formulário | não aciona | 0/3 | – | – | – |
| 19 | extensão do chrome que muda a cor do whatsapp web | não aciona | 0/3 | – | – | – |
| 20 | a IA do chat master veloz pode responder com emoji? como configuro isso no prompt? | não aciona | 0/3 | – | – | – |

### `validacao/cmv-painel-css-js.json` (nunca vistos pelo otimizador)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | como escondo o botão de nova conversa pros atendentes no painel do chat master veloz com css? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | o modo escuro do painel do CMV deixa o texto do campo de digitação ilegível, dá pra corrigir com css? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | quero um script no painel do chatmasterveloz que mostre o tempo de espera do cliente em vermelho quando passar de 10 minutos | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | mudar a logo e as cores da tela de login do painel do chat master veloz | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 5 | deixar o quadro de atendimentos do chat master veloz mais compacto, os cards são muito altos | aciona | 3/3 | 3/3 | 3/3 | 2/3 |
| 6 | como troco a logo da empresa nas configurações do chat master veloz? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 7 | javascript pra validar CPF num formulário do meu site | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | personaliza a cor do botão do web chat que fica no meu site, é do chat master veloz | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | como tiro a permissão do atendente de excluir contatos no chat master veloz? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | tema escuro no VS Code com fonte maior, como configuro? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |

### `independentes/cmv-painel-css-js.json` (escritos por um agente que não viu os outros pedidos nem as descrições)

| # | Pedido | Esperado | Opus 5.5 | Fable 5.2 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|---|
| 1 | Quero deixar a tela de login do Chat Master Veloz com fundo azul-marinho e o logo da minha empresa maior. Me passa o CSS e me diz onde colar. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | da pra esconder o item Campanhas do menu lateral no cmv usando css? e mudar a ordem dos outros itens | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | No tema escuro do painel CMV os balões da conversa ficam com pouco contraste. Quero o balão do cliente em cinza-escuro, o do atendente em verde #1f8a4c e a fonte em 15px. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | Preciso de um JS personalizado no painel do chatmasterveloz que mostre o lembrete 'confira a tag antes de encerrar' quando o atendente clicar no botão de encerrar o ticket. | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 5 | meu css customizado parou de funcionar depois da ultima atualizaçao do master veloz. eu usava .MuiButton-root e umas classes tipo .jss123 pra mudar os botoes e o cabeçalho. qual seletor eu uso agora pra nao quebrar de novo? | aciona | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | Como mudo as cores e a fonte do widget do Chatwoot no meu site? Queria também um CSS customizado no dashboard dos agentes. | não aciona | 0/3 | 0/3 | 0/3 | 1/3 |
| 7 | Preciso de um CSS adicional no WordPress (uso Elementor) pra deixar o botão flutuante de WhatsApp com a cor da minha marca e esconder ele no mobile. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 8 | Como tiro do perfil atendente a permissão de ver o menu Contatos e de exportar contatos no CMV? Quero fazer pelas permissões do usuário mesmo, sem código. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 9 | Escreve um script em JavaScript (Node) que recebe o webhook do Chat Master Veloz e responde a mensagem do cliente pela API. | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
| 10 | No bloco Execução de Código JS do FlowBuilder, como escrevo um código que tira pontos e traço do CPF que o cliente digitou e salva numa variável do fluxo? | não aciona | 0/3 | 0/3 | 0/3 | 0/3 |
