# Revisão dos pedidos de roteamento

Estes pedidos medem se o Claude escolhe a skill certa. Para revisar, **responda pelo chat com o número do pedido**, só onde você discordar ou tiver algo a dizer. Exemplos de resposta: `3: deveria ser Mensagens`, `7: ninguém escreve assim`, `12: ok`. O que você não citar fica como está.

O mais útil que você pode mandar, além disso: **mensagens reais** que seus clientes ou sua equipe já escreveram pedindo ajuda, coladas no chat do jeito que foram escritas (sem nomes nem telefones).

## Quem atende o quê

- **Ajuda:** explica como usar ou configurar algo na tela
- **API:** entrega o código da integração
- **FlowBuilder:** monta ou conserta o fluxo do robô
- **Agente de IA:** prompt e configuração da IA
- **Mensagens:** escreve o texto pronto
- **CSS/JS:** muda o visual do painel com código
- **Nenhuma:** não é assunto do Chat Master Veloz

## Parte A: 15 pedidos em que duas respostas são aceitas

Os anotadores consideraram os dois destinos defensáveis. Se para você só um faz sentido, diga qual.

### 1
> quero mudar a cor e o arredondado dos botões da página do Link na Bio. vi que tem um campo de css lá, quais classes eu uso?

- **Aceito hoje:** Ajuda ou CSS/JS
- **Por quê:** Fala de CSS, mas a página do Link na Bio não é o painel: o bloco Aparência (CSS e JavaScript) e as classes .bio-* estão no artigo Link na Bio da Central de Ajuda, fora do catálogo da cmv-painel-css-js.

### 2
> tem extrato de tokens da IA? o saldo de créditos despencou essa semana

- **Aceito hoje:** Agente de IA ou Ajuda
- **Por quê:** 'Token' aqui não é o da API: é o Extrato de tokens da tela Sugestão de resposta IA, recurso da tabela 'Outros recursos de IA'; a cmv-ajuda também tem esse artigo (pasta outros), por isso é aceitável.

### 3
> Tem como as ligações gravadas do PABX já virem transcritas e com um resumo do que foi falado? Onde liga isso e o que precisa estar configurado antes?

- **Aceito hoje:** Agente de IA ou Ajuda
- **Por quê:** Fala de ligações e PABX, mas é o recurso 'IA nas gravações das chamadas' da tabela 'Outros recursos de IA' (usa o Token OpenAI); o artigo Gravações das Chamadas também está na cmv-ajuda, por isso é aceitável.

### 4
> dá pra sumir com o botão excluir da tela de Contatos pra todo mundo? o pessoal clica sem querer

- **Aceito hoje:** CSS/JS ou Ajuda
- **Por quê:** Fronteira com cmv-ajuda, que perde: o pedido é esconder um botão para todos (aparência, receita 12), não permissão por perfil; a skill entrega o CSS e avisa que esconder não bloqueia.

### 5
> Posso colar o token da conexão num javascript do painel do Chat Master Veloz pra ele buscar o status do pedido no meu sistema e mostrar do lado da conversa?

- **Aceito hoje:** CSS/JS ou API
- **Por quê:** Fronteira com cmv-api: a seção 'Quando pedem para pôr token, senha ou chave no JS' é da cmv-painel-css-js (recusa com o porquê); a integração que resolve a necessidade é da cmv-api, por isso aceitável.

### 6
> já tenho o texto do prompt pronto (um colega escreveu). só não acho em qual tela eu colo ele e como ligo no setor de Vendas. qual é o menu?

- **Aceito hoje:** Ajuda ou Agente de IA
- **Por quê:** 'Onde termina esta skill' diz que 'onde colar o prompt' continua na cmv-ajuda; a cmv-agente-ia perde porque o prompt já existe e não se pede escrever nem ajustar a IA, embora ela também traga o passo a passo do painel.

### 7
> Onde eu cadastro o token da conexão no CMV? O programador que está integrando nosso sistema pediu esse dado e eu não sei em que tela fica.

- **Aceito hoje:** Ajuda ou API
- **Por quê:** 'Onde termina esta skill' cita 'onde cadastrar o token da conexão' como uso do painel; a cmv-api perde porque não se pede código, payload nem chamada.

### 8
> entrei no FlowBuilder Nativo e só vejo os cards dos fluxos. onde clico pra abrir o editor e mexer num fluxo que já existe?

- **Aceito hoje:** Ajuda ou FlowBuilder
- **Por quê:** 'Onde termina esta skill' cita 'como abrir o editor de fluxos' como uso; a cmv-flowbuilder perde porque não se pede desenhar, gerar nem diagnosticar fluxo.

### 9
> quero aquele robô simples: cliente manda oi e já aparece 1-Vendas 2-Financeiro 3-Suporte e cai no setor que escolher. me falaram que nem precisa montar fluxo, é só colocar os setores na conexão. como configuro isso?

- **Aceito hoje:** Ajuda ou FlowBuilder
- **Por quê:** Tabela de sinônimos: 'robô, menu automático' pode ser o menu de Setores na conexão (artigo Chatbot e menu de Setores na Conexão), que é configuração de tela; a cmv-flowbuilder perde porque a pessoa descarta o fluxo, mas tem o mesmo artigo.

### 10
> quero um fluxo no CMV com menu inicial (1 comprar, 2 suporte, 3 financeiro) e, se a pessoa escolher suporte, cai numa IA que tira as dúvidas dela. monta pra mim?

- **Aceito hoje:** FlowBuilder ou Agente de IA
- **Por quê:** 'O que é de outra skill': o desenho do fluxo e o bloco que leva ao assistente ficam aqui e o prompt é da cmv-agente-ia, que no pedido misto também se declara apta a fazer a parte de IA.

### 11
> no bloco Typebot a lista de setores aparece vazia e não consigo escolher nada. meu robô no typebot existe e funciona. o que eu tenho que fazer antes pra ele aparecer ali?

- **Aceito hoje:** FlowBuilder ou Ajuda
- **Por quê:** Artigo Typebot (bloco): a lista só mostra Setores com um Typebot ligado; 'Typebot' aqui é um bloco do FlowBuilder, não um pedido sobre a outra plataforma.

### 12
> criei a chave lá na openai. e agora, onde eu colo ela? no menu Prompts OPEN.AI não achei campo nenhum pra isso. precisa pedir alguma liberação antes de funcionar?

- **Aceito hoje:** Agente de IA ou Ajuda
- **Por quê:** Etapa 1 e tabela 'Outros recursos de IA': Token OpenAI no menu Integrações, card OPEN.AI, mais os três pré-requisitos; a cmv-ajuda também cobre 'onde fica'.

### 13
> essa nota de 0 a 10 que aparece aqui no painel pros atendimentos encerrados é o cliente que dá ou é a máquina? tem atendimento com nota em que o cliente nem respondeu a pesquisa

- **Aceito hoje:** Agente de IA ou Ajuda
- **Por quê:** Tabela 'Outros recursos de IA': a Avaliação pela IA dá nota de 0 a 10 aos encerrados, diferente da pesquisa respondida pelo cliente; a cmv-ajuda também separa os dois em 'Títulos parecidos'.

### 14
> me escreve só os textos do fluxo de boas-vindas da barbearia: saudação, a pergunta do menu de serviços e o aviso de que vai passar pro barbeiro. a montagem no editor eu mesmo faço

- **Aceito hoje:** Mensagens ou FlowBuilder
- **Por quê:** 'Onde termina esta skill': os textos de dentro de um fluxo podem ser redigidos aqui e a montagem não; a cmv-flowbuilder perde porque a montagem foi dispensada, mas também diz que os textos dos blocos ficam nela.

### 15
> quero pôr um script no painel do CMV que, quando o atendente abre o ticket, busca na API o saldo devedor do cliente e mostra ao lado do nome. posso deixar o token da empresa direto no JS?

- **Aceito hoje:** CSS/JS ou API
- **Por quê:** Seção 'Quando pedem para pôr token, senha ou chave no JS': a skill recusa o token com o porquê e entrega o resto; a cmv-api perde como primeira parada, mas é dela a integração fora do painel.

## Parte B: 7 pedidos em que algum modelo não carregou a skill esperada

Aqui o destino não está em dúvida. Só diga se o pedido parece com o que seus usuários escrevem, ou se o destino está errado.

### 16
> coloquei limite de 5 atendimentos simultaneos pra cada atendente mas tem gente aceitando conversa acima disso. o q ta faltando?

- **Deveria atender:** Ajuda
- **Falhou em:** Haiku (Haiku: nenhuma skill 3/3)

### 17
> O QR Code da mesa 7 foi fotografado e tem gente fazendo pedido de casa pelo cardápio digital. Como invalido só o dessa mesa, sem ter que reimprimir o das outras?

- **Deveria atender:** Ajuda
- **Falhou em:** Haiku (Haiku: nenhuma skill 3/3)

### 18
> apareceu um recado vermelho escrito Missing Body in Payload embaixo de uma conversa. a gente nem usa api, q erro é esse??

- **Deveria atender:** Ajuda
- **Falhou em:** Haiku (Haiku: nenhuma skill 2/3, Ajuda 1/3)

### 19
> quanto custa colocar mais 3 usuários no meu plano do Chat Master Veloz? e tem fidelidade ou posso cancelar qdo quiser?

- **Deveria atender:** Ajuda
- **Falhou em:** Haiku (Haiku: nenhuma skill 2/3, Ajuda 1/3)

### 20
> tem como cadastrar respostas rápidas em lote no CMV? tenho 80 num csv (atalho;texto) e não quero digitar uma por uma. sei mexer com node

- **Deveria atender:** API
- **Falhou em:** Sonnet (Sonnet: Ajuda 2/3, Ajuda + API 1/3)

### 21
> Queria que a atendente digitasse /garantia e isso rodasse uma sequência sozinha: manda o PDF do termo, espera uns segundos, pergunta se ficou alguma dúvida e marca a tag "garantia enviada". Tem como montar?

- **Deveria atender:** FlowBuilder
- **Falhou em:** Opus, Sonnet (Opus: Ajuda 3/3; Sonnet: Ajuda 3/3)

### 22
> reescreve a mensagem de avaliação q vai no fim do atendimento? hj tá "Avalie nosso atendimento de 1 a 5" e quase ninguem responde. restaurante com delivery

- **Deveria atender:** Mensagens
- **Falhou em:** Haiku (Haiku: nenhuma skill 2/3, Mensagens 1/3)

## Parte C: os outros 146 pedidos

Leitura opcional: todos os modelos medidos carregaram o destino esperado.

### Ajuda

| # | Pedido |
|---|---|
| 23 | cadastrei a conta de email do comercial no painel só q ta puxando a caixa inteira, inclusive coisa pessoal do vendedor. da pra sincronizar só uma pasta? |
| 24 | sumiu uma coluna do kanban de tags, a tag ainda existe no cadastro. pq? |
| 25 | atendente novo nao recebe o aviso no whatsapp pessoal qdo chega conversa no aguardando do setor dele, os outros recebem normal. oq conferir? |
| 26 | Quero que atendente não consiga excluir contato de jeito nenhum no CMV, nem achando outro caminho pra tela. Supervisor e admin continuam podendo. Como travo isso? |
| 27 | como ativo aquele menu simples que a própria conexão manda com os setores (1 Comercial, 2 Financeiro, 3 Suporte)? criei os setores no chat master veloz mas o cliente não recebe opção nenhuma |
| 28 | Como eu crio uma campanha pelo WhatsApp de QR Code? Os textos o marketing já me passou prontos, o que eu não sei é onde monta a lista de contatos e onde marca o dia e a hora do disparo. |
| 29 | Trouxemos nosso número da API oficial de outra plataforma para o Chat Master Veloz. Os templates que já estavam aprovados lá aparecem sozinhos ou tenho que sincronizar em algum lugar? |
| 95 | fim do dia e a menina do balcão não sabe fechar o caixa no PDV. onde clica e o que ela tem que conferir antes de confirmar? |
| 96 | Quero atender o direct do Instagram da loja no mesmo painel onde já atendo o WhatsApp. Como adiciono essa conexão e o que a conta do Instagram precisa ter? |
| 97 | contratamos o pabx e preciso criar ramal pra 4 atendentes. onde cadastra os ramais e como cada um atende a ligação pelo painel? |
| 98 | Tem um menu E-mails aqui no painel mas pra mim aparece vazio. Como cadastro a conta contato@ da empresa pra equipe responder por ali, junto com os tickets? |
| 99 | desde ontem um monte de conversa ficou com fundo vermelho na lista de atendimentos e cliente reclamando que não recebe resposta. o que é isso e como resolve?? |
| 100 | dá pra trocar a cor do Web Chat? ele tá azul no site e a marca da clínica é verde, ficou destoando |
| 101 | O que é exatamente a tal API Oficial? Hoje uso o Chat Master Veloz com QR Code e o suporte comentou que eu deveria migrar. Muda o quê no meu dia a dia? |
| 102 | No Chat Master Veloz, consigo colocar a logo e a cor do meu restaurante no Cardápio Digital? Onde fica essa configuração? |

### API

| # | Pedido |
|---|---|
| 30 | preciso de um curl pra encerrar o ticket pelo ticketId quando o pedido sai como entregue no meu sistema de delivery. a conexão é whatsapp por QR code e o token já tá definido na aba Integrações dela |
| 31 | O webhook do Setor está mandando aviso até das mensagens que o próprio atendente envia. Como eu filtro só as que vêm do cliente no meu receptor em PHP? Qual campo do JSON diferencia? |
| 32 | como mando um botão de pix copia e cola por requisição http na conexão Pro? tentei aqui e a msg chegou só com o texto, sem botão nenhum |
| 33 | tenho uma planilha com umas 300 reservas do restaurante e queria um script em python que cria a reserva de mesa de cada uma no PDV. qual endpoint e quais campos vão no corpo? |
| 34 | Nosso ERP precisa mover a oportunidade de raia quando o boleto é compensado. Estamos no CRM novo, com vários funis, e vamos usar o Token da Empresa. Existe chamada para isso? Como fica o pedido? |
| 35 | qdo alguem preenche o formulário de matrícula no site da escola (wordpress) quero q o robô já chame a pessoa no whats levando nome e curso de interesse. o fluxo já tá pronto e testado no FlowBuilder, falta o site disparar ele. como faço essa chamada? |
| 36 | Minha chamada de enviar texto volta 401 "Acesso não permitido". Estou fazendo POST em https://api2.chatmasterveloz.com/api/messages/send com Authorization: Bearer e o token que copiei em Configurações > Token da Empresa, corpo {"number":"5541999990000","body":"teste"}. O que está errado? |
| 37 | Tenho um template de utilidade já aprovado, lembrete_consulta, com {{1}} = nome do paciente e {{2}} = horário. Preciso do JSON pra disparar ele a partir do sistema da clínica pela API oficial. |
| 38 | queria jogar no nosso BI a nota que a Avaliação pela IA dá pra cada atendimento encerrado. tem webhook disso? o q chega nele? |
| 39 | Quando a secretária marca uma consulta no nosso sistema, quero que ele já crie sozinho, lá em Agendamentos, a mensagem de lembrete pro paciente pra véspera às 18h. Tem endpoint pra isso? Se puder, exemplo em PHP. |
| 40 | Como recebo no meu servidor um aviso toda vez que um pedido do PDV do Chat Master Veloz muda de status (confirmado, em preparo, saiu pra entrega)? Preciso saber onde cadastro a URL e o formato do que chega. |
| 103 | tenho um sisteminha de agenda da clínica que meu sobrinho fez. queria que quando a secretária marcasse a consulta lá, o paciente já recebesse a confirmação no whats pelo número que a gente conectou por QR Code em Conexões. tem como ligar uma coisa na outra? não entendo nada de programação |
| 104 | meu ERP sabe o vencimento de cada boleto. quero que ele mesmo crie o lembrete lá em Agendamentos em vez de alguém cadastrar um por um na mão. o texto já está definido, preciso é saber como o ERP cria isso |
| 105 | preciso mandar pelo meu script em python uma mensagem com 3 botões de resposta (Confirmar / Remarcar / Cancelar) pela conexão oficial, usando o token da conexão. qual endpoint e como fica o json? |
| 106 | quando o pedido é marcado como entregue no nosso sistema eu queria encerrar o ticket do cliente sozinho, sem o atendente ter que clicar em Resolver. dá pra fazer isso por requisição? em php de preferência |
| 107 | to montando um workflow no n8n pra responder direct do instagram. o webhook que colei na aba Integrações da conexão já chega certinho, mas qual chamada eu uso pra devolver o texto pro instagram? a de whatsapp deu erro |
| 108 | meu CRM precisa iniciar um fluxo do FlowBuilder pra um número específico quando o lead muda de etapa. o fluxo já está pronto e testado, falta só a chamada do lado do CRM. como é? |
| 109 | Já tenho o template lembrete_consulta aprovado na Meta. Preciso do curl pra enviar ele pelo CMV preenchendo o nome do paciente e o horário nas variáveis. |
| 110 | Quero receber no meu sistema de RH a nota que a Avaliação pela IA dá pra cada atendimento do Chat Master Veloz. Tem webhook pra isso? Como configuro o recebimento? |
| 111 | fiz um robô em node que lê os pedidos novos da loja virtual e precisa abrir um ticket já no setor Expedição com uma nota interna dizendo o número do pedido. qual rota do CMV eu chamo? |
| 112 | tenho um agente de ia próprio rodando no meu servidor (langchain + banco vetorial). quero plugar ele no CMV: receber cada mensagem que o cliente manda e devolver a resposta dentro do mesmo atendimento. como faço essa ponte? |
| 113 | quero disparar um aviso pra uns 300 clientes direto da minha planilha do google com apps script, sem passar pela tela de Campanhas. como fica a requisição com o token da conexão? |
| 114 | No Chat Master Veloz dá pra enviar mensagem pro visitante do Web Chat pela API? Quero avisar quando o orçamento dele ficar pronto, a partir do nosso sistema de orçamentos. |

### FlowBuilder

| # | Pedido |
|---|---|
| 41 | preciso de um fluxo pro instagram da loja no flowbuilder: a pessoa comenta EU QUERO no post e recebe no direct o link do catálogo, mas só se já seguir o perfil. se não segue, pede pra seguir antes |
| 42 | Meu robô manda as boas-vindas duas vezes seguidas pra todo cliente novo. O fluxo só tem um bloco Conteúdo no começo, antes do Menu. O que pode ser? |
| 43 | quero testar duas abordagens no FlowBuilder Nativo: metade dos leads que entram recebe a oferta A e a outra metade a oferta B, e cada grupo ganha uma tag diferente pra eu comparar depois. como monto? |
| 44 | Sou coordenadora de uma escola de inglês. Quando o responsável dá nota 1 ou 2 na avaliação do atendimento, queria que entrasse um fluxo perguntando o motivo e deixando um recado interno pra coordenação. Nota 4 e 5 só agradece. Dá pra desenhar isso? |
| 45 | fluxo trava no bloco Pergunta qdo o cliente some, nunca encerra nem cai pro atendente. como arrumo |
| 46 | Quero um fluxo que começa com menu (1 agendar visita, 2 tirar dúvidas, 3 falar com corretor) e na opção 2 quem responde é o assistente que já está criado e testado em Prompts OPEN.AI. Se o cliente pedir humano, vai pro setor Corretores. Monta o desenho pra mim? |
| 47 | no meio do fluxo preciso consultar o status do pedido no meu sistema (já tenho a url, devolve um json com status e previsao) e responder pro cliente tipo 'seu pedido está X, previsão Y'. como encaixo isso nos blocos e uso o retorno na mensagem? |
| 48 | Uso a API oficial no Chat Master Veloz. No fluxo de recuperação, a primeira mensagem precisa ser um template que já está aprovado (voltamos_a_falar) e, se a pessoa responder, segue pro menu. Como configuro o bloco do template dentro do fluxo e preencho a variável do nome? |
| 49 | no bloco Execução de Código JS, como tiro ponto e traço do cpf que o cliente digitou antes de passar pro bloco do Asaas? e como guardo o resultado pra usar depois |
| 50 | vou disparar uma campanha de rematrícula e quero q quem responder caia num robô q pergunta a série do aluno e encaminha pra secretaria certa (fundamental ou médio). os textos da campanha já estão prontos, falta essa parte automática |
| 51 | Tenho um provedor de internet pequeno e uso o Chat Master Veloz com WhatsApp por QR Code. Queria um atendimento automático assim: fora do horário (seg a sex 8h-18h, sáb 8h-12h) avisa que voltamos no próximo dia útil; dentro do horário mostra um menu com 2ª via de boleto, suporte técnico e contratar plano. Suporte e contratar vão pros setores Suporte e Comercial; 2ª via por enquanto manda pro Financeiro. Consegue me entregar o arquivo pronto pra importar? |
| 115 | importei o fluxo ontem, salvei, ele aparece na lista do FlowBuilder Nativo, mas quando mando mensagem de teste não acontece nada, a conversa cai direto em Aguardando sem resposta. o que falta? |
| 116 | o cliente manda oi e recebe DUAS boas-vindas, uma atrás da outra, antes do menu. no meu fluxo só tem um bloco Conteúdo com a saudação. de onde tá vindo a outra? |
| 117 | tenho um fluxo de pós-venda pronto. o que é melhor pra começar ele: o atendente chamar por resposta rápida no fim da conversa, ou pendurar numa tag com remarketing pra disparar sozinho 2 dias depois? muda alguma coisa no desenho do fluxo? |
| 118 | Sou dona de uma oficina mecânica. Queria um atendimento automático no WhatsApp que pergunte se é orçamento, revisão ou acompanhar serviço, peça a placa do carro e só então passe pro setor certo. Uso conexão por QR Code e já tenho os setores Orçamento e Pátio criados. |
| 119 | meu Menu em Botões tem 5 opções e o cliente só vê 3. tem como mostrar as 5 sem ter que refazer tudo? é o bloco Menu do fluxo de entrada |
| 120 | no meio do fluxo eu preciso consultar o status do pedido no meu sistema (tenho uma url que devolve um json com o campo status) e mostrar isso pro cliente. em que ponto do fluxo entra essa consulta e como uso o retorno nas mensagens seguintes? |
| 121 | meu fluxo de remarketing roda 3 dias depois do orçamento, já fora das 24h, e uso a API oficial. como configuro o bloco Template pra ele abrir a conversa e preencher o nome do cliente? o template em si já está aprovado |
| 122 | em que parte do fluxo eu coloco o bloco GPT Assistant? quero que a IA só entre depois que o cliente informar o CPF e escolher o assunto no menu. o assistente já está criado e respondendo bem |
| 123 | preciso de um bloco de Execução de Código JS que pegue o que o cliente digitou no telefone e tire tudo que não é número antes de guardar na variável. como escrevo e onde ligo a Variável depois? |
| 124 | Me gera o arquivo pra importar no Chat Master Veloz: fluxo de uma escola de idiomas com menu Matrícula, Financeiro e Secretaria, e quem escrever fora do horário recebe aviso de que respondemos no próximo dia útil. |

### Agente de IA

| # | Pedido |
|---|---|
| 52 | tenho um pet shop com banho e tosa e queria uma IA respondendo no whats sobre preço e horário e anotando pedido de agendamento. vi no painel um menu Prompts OPEN.AI, é ali? por onde começo |
| 53 | o gpt assistant do setor Recepção ta inventando preço de procedimento q a gente nem faz. o prompt hj é só isso: "Você é a Lia, atendente virtual da clínica. Responda dúvidas sobre tratamentos e valores de forma simpática." como arrumo? |
| 54 | O assistente responde bem quando o cliente escreve, mas quando mandam áudio ele devolve coisa sem sentido. No cadastro do prompt a temperatura está 0.3 e o máximo de tokens 300. O que ajusto? |
| 55 | as sugestões daquele botão ✨ na conversa saem genéricas demais, sem o jeito da nossa imobiliária, e as vezes prometem prazo de visita q não existe. da pra ajustar isso? |
| 56 | Quero usar o assistente dentro do grupo de WhatsApp dos nossos revendedores, mas só quando alguém chamar, tipo !tabela. Vi que o prompt tem um campo Gatilho para Grupo. Como configuro e o que escrevo nas instruções pra ele responder só sobre a tabela de preços? |
| 57 | Já tenho o fluxo pronto com menu, e na opção 'dúvidas' entra o bloco GPT Assistant. O fluxo tá ok. O que falta é o texto de instruções desse assistente: escola de idiomas, tira dúvida de matrícula, horários e mensalidade, e devolve pra um humano se perguntarem de bolsa ou desconto. |
| 58 | A Avaliação pela IA do CMV tá dando nota baixa pra atendimento que foi bom, parece q ela não conhece nosso processo (a gente sempre pede o CPF antes de qualquer coisa, por ex). tem como ensinar pra ela como é o atendimento ideal aqui? |
| 59 | preciso da mensagem que o assistente manda quando passa a conversa pra um humano (campo Mensagem de Transbordo) e da regra no prompt dizendo quando ele deve transferir pro Financeiro. é uma contabilidade, tom formal |
| 60 | coloquei no prompt pra ele marcar a tag "lead quente" qdo o cliente pedir orçamento. na conversa ele até fala que anotou, mas a tag não aparece no ticket. o que tá errado? |
| 61 | a IA do Chat Master Veloz consegue olhar minha agenda do Google e já marcar o horário sozinha com o cliente, sem ninguém da equipe confirmar depois? |
| 125 | aquele botão Analisar Atendimento com IA nas ações do ticket: o resultado aparece pro cliente também ou só pra gente? e o que exatamente ele avalia? |
| 126 | colei o prompt no GPT Assistant e liguei num setor de teste. como testo direito antes de apontar a conexão principal pra ele? queria um roteiro de conversas pra tentar fazer ele errar |
| 127 | a ia do atendimento tá inventando preço de procedimento que não existe e às vezes responde textão enorme. a tabela de valores tá certinha no prompt lá em Prompts OPEN.AI, temperatura em 1. onde eu mexo? |
| 128 | Tenho um escritório de contabilidade e quero uma IA respondendo as dúvidas básicas de MEI no WhatsApp e passando pro contador quando o assunto for imposto de renda. Já temos o setor Fiscal criado e a conexão oficial funcionando. Por onde começo? |
| 129 | meu fluxo já termina no bloco GPT Assistant, essa parte tá ok. agora preciso do texto das instruções do assistente: escola de natação infantil, informa turmas e horários, nunca fala de valor e passa pra secretaria quando pedirem matrícula |
| 130 | quero deixar as sugestões do Copiloto com a cara da nossa imobiliária: tom formal, sem emoji, nunca prometer prazo de aprovação de financiamento. o que escrevo nas instruções dele? |
| 131 | os atendentes reclamam de ter que ouvir áudio de 3 minutos. no CMV tem como transformar o áudio do cliente em texto? onde clica e isso consome a conta da openai? |
| 132 | ativei o menu Assistente de IA achando que ele ia responder meus clientes de madrugada, mas ele só fica respondendo pergunta minha sobre os atendimentos. tô configurando errado? |
| 133 | quero um robô que converse de verdade com o paciente e entenda o que ele escreve, não aquele menu de digite 1, digite 2. no CMV como se faz isso? |
| 134 | No Chat Master Veloz, o GPT Assistant consegue responder dentro de um grupo de WhatsApp? Queria que ele só falasse quando alguém chamasse por um comando. |

### Mensagens

| # | Pedido |
|---|---|
| 62 | preciso de uns 6 atalhos prontos pras meninas do escritório de contabilidade usarem no menu Respostas Rápidas: pedir documento do IR, avisar que a guia foi enviada, cobrar honorário atrasado com jeitinho, essas coisas. atendemos por qr code |
| 63 | me ajuda a escrever o texto de ausência? sou advogada, fico em audiência a tarde toda e deixo o status como Ausente. o cliente manda 5 msg seguidas e não quero q pareça um robô repetindo a mesma coisa |
| 64 | Template de marketing pra Black Friday da loja de calçados, com o primeiro nome da pessoa e o cupom, e com opção de parar de receber. Vai em campanha pela conexão oficial pra uns 2 mil contatos; vou cadastrar em Gestão de Templates. |
| 65 | quero mandar parabéns automático no aniversário dos alunos da academia com um mimo (1 semana de personal grátis). escreve o texto pra eu colar em Mensagem de Aniversário? whats por qr code |
| 66 | Aviso de reajuste da mensalidade pra todos os pais da escola, uns 400 contatos, em Campanhas, pelo WhatsApp de QR Code. Preciso das variações do texto pra não tomar bloqueio e do texto de descadastro. |
| 67 | qual texto eu coloco na mensagem de fora do expediente do setor Suporte? aqui a opção de abrir ticket fora do expediente tá em Não. provedor de internet, horário seg a sáb 8h às 20h |
| 68 | Preciso do texto do template que vai no bloco Template do meu fluxo de remarketing: cliente pediu orçamento de energia solar e sumiu há 3 dias. O fluxo já está montado, só falta o que escrever pra mandar pra aprovação. |
| 69 | nosso sistema vai disparar por api o template de confirmação de agendamento da clínica, essa parte técnica o dev resolve. eu preciso é do texto do template: utilidade, com nome, data e hora, e q não seja reprovado pela meta |
| 70 | escreve a saudação com as opções que a conexão manda qdo o cliente chega? setores: 1 Vendas, 2 Assistência Técnica, 3 Financeiro. loja de eletrodomésticos, tom simpático mas sem exagero de emoji |
| 71 | Administradora de condomínios, campanha pela oficial no CMV. Quero um template avisando que o boleto do mês está disponível, com {{1}} nome, {{2}} mês e {{3}} link. Escreve o template e me diz como fica a planilha de contatos pra cada variável cair no lugar certo. |
| 72 | No Chat Master Veloz dá pra agendar uma mensagem que se repete todo mês pro mesmo cliente? Trabalho com purificadores de água e queria lembrar cada um da troca do refil. Se der, já escreve a mensagem. Conexão por QR Code. |
| 135 | preciso de uma msg pra mandar pros pais avisando q a rematrícula vence dia 10 e quem não renovar perde a vaga. escola infantil, uns 180 responsáveis, número conectado por qr code |
| 136 | escreve um texto pra Mensagem de Ausência do meu perfil? saio pro almoço 12h às 13h30 e não quero que o cliente ache que foi ignorado se mandar 3 mensagens seguidas |
| 137 | a mensagem que sai quando o atendente clica em Resolver tá assim: 'Atendimento finalizado. Posso ajudar em algo mais?' e toda vez o cliente responde 'não, obrigado' e abre ticket de novo. reescreve pra mim? |
| 138 | Preciso do texto da pesquisa de satisfação que vai no fim do atendimento pedindo a nota, aquela das Avaliações. Loja de móveis planejados, tom simpático e curto. |
| 139 | o cliente ficou de mandar os documentos e sumiu faz 3 dias. tentei escrever e não vai, fala que a janela de 24 horas fechou. o que eu posso mandar pra ele agora pra retomar? uso a conexão oficial |
| 140 | vou enviar por API um aviso de 'pedido saiu pra entrega', mas ainda não tenho o texto. cria o template de utilidade pra eu submeter na Gestão de Templates? a chamada meu dev já sabe fazer |
| 141 | Vou fazer minha primeira campanha no CMV pra avisar que a loja mudou de endereço. Escreve as variações do texto e a mensagem de descadastramento? É conexão por QR Code. |
| 142 | preciso de umas respostas rápidas pros atendentes usarem quando a IA passa o cliente pra eles, tipo 'oi, aqui é a Carla, vi que você já falou com nossa assistente virtual sobre...'. faz umas 5 variações com atalho |
| 143 | qual código eu uso pra aparecer o primeiro nome do cliente e o protocolo na saudação do setor? aproveita e já escreve a saudação, é uma ótica |
| 144 | a resposta automática de fora do horário do robô tá seca demais: 'Estamos fechados.' melhora ela? pet shop, atendemos seg a sáb das 8h às 18h |
| 145 | No CMV tenho este template aprovado e em uso: 'Olá {{1}}, sua consulta está confirmada para {{2}}.' Quero acrescentar o endereço da clínica e uma frase oferecendo check-up com 20% de desconto. Como fica o texto novo? |

### CSS/JS

| # | Pedido |
|---|---|
| 73 | quero trocar o fundo da tela de login do painel pelo degradê azul da nossa marca (#0A2A66 pro #1E66F5) e deixar o texto do rodapé branco. onde mexo? |
| 74 | no tema escuro queria os botões principais em laranja #F26B21. no claro fica como tá |
| 75 | qdo a atendente clicar em Resolver no ticket queria q aparecesse um lembrete tipo "conferiu se anexou o comprovante?" antes. tem como colocar isso no painel? |
| 76 | no Quadro de Atendimentos o tempo de espera atrasado e o de atenção têm cores muito fraquinhas, no telão da operação ninguém enxerga. queria vermelho forte no atrasado e amarelo vivo no atenção |
| 77 | Meu CSS que escondia a coluna de valor no Board do CRM parou de funcionar depois da última atualização do painel. O trecho é: .MuiGrid-root .jss412 { display: none !important; } O que houve? |
| 78 | na página de chat que o cliente abre pelo link (modo alternativo) queria os balões mais arredondados e a fonte maior. a foto e a cor do topo eu já ajustei em Aparência, o resto não achei onde muda |
| 79 | no editor do flowbuilder os blocos são muito parecidos entre si, no monitor grande da sala ninguém distingue. dá pra deixar a borda mais grossa e o fundo mais escuro neles? |
| 80 | Quando a atendente estiver em ligação no ramal, queria que a barra do topo do painel dela ficasse vermelha, pra supervisora ver de longe quem está em chamada. Tem como? |
| 81 | no board de oportunidades do CMV queria q cada cartão tivesse uma faixa na lateral com a cor da etapa do funil em q ele tá. hj é tudo branco |
| 82 | No Chat Master Veloz tem como rodar um JS meu na página do chat externo (a que abre pelo link) pra instalar o pixel do Facebook? Não achei campo de JS pra ela, só de CSS. |
| 146 | em qual campo eu colo o css pra mudar só a tela de login? vi que em Configurações > Cores tem pré-login e pós-login e não entendi a diferença |
| 147 | dá pra trocar o texto do botão Resolver pra 'Finalizar atendimento' na tela dos tickets? o pessoal aqui confunde |
| 148 | as janelinhas que abrem no painel (tipo a de novo contato e a de confirmar exclusão) ficam com um branco estourado no tema escuro. queria fundo cinza escuro e cantos arredondados em todas |
| 149 | quero reordenar o menu lateral: Tickets, Contatos e CRM lá em cima e o resto embaixo. tem como sem pedir pro suporte? |
| 150 | meu css parou de pegar depois da atualização de ontem. eu usava .MuiPaper-root pra arredondar os cartões da lista de atendimentos e agora não faz mais nada |
| 151 | queria que aparecesse um aviso amarelo no topo da tela de Contatos do painel lembrando o pessoal de não exportar a base sem autorização. dá pra fazer com um scriptzinho? |
| 152 | O painel do Chat Master Veloz vem todo no verde padrão. Preciso deixar a barra de cima e os botões em azul marinho (#0b1f3a), que é a cor da minha revenda, também no tema escuro. |
| 153 | tem como sumir com o botão de excluir na tela de Contatos? não quero mexer em permissão de ninguém, só tirar ele da vista pra evitar clique sem querer |
| 154 | na página que o cliente abre pelo link do Chat Externo eu já troquei a Cor principal, mas os balões continuam cinza e a letra é miúda. quero os balões da empresa em laranja e a fonte maior |
| 155 | dá pra criar um template visual pro painel? tipo um tema roxo com cinza, igual o site da empresa, valendo só pra minha empresa e não pras outras da revenda |
| 156 | quando toca ligação no ramal o pessoal tá em outra aba e perde a chamada. tem como fazer o título da aba do navegador mudar ou piscar enquanto o ramal toca? |

### Nenhuma

| # | Pedido |
|---|---|
| 83 | monta pra mim um fluxo de boas-vindas no ManyChat pro instagram da confeitaria: quem mandar a palavra CARDAPIO recebe o pdf e depois uma pergunta se quer encomendar |
| 84 | No Blip meu bot cai sempre na exceção de "não entendi" mesmo quando o usuário digita certinho o número da opção do menu. Onde eu olho pra descobrir o que tá quebrado? |
| 85 | preciso criar um zap no Zapier: entrou lead no Facebook Lead Ads, cria uma linha no Google Sheets e manda um email pro vendedor da vez. me passa o passo a passo |
| 86 | no chatwoot as mensagens do whatsapp cloud api estão chegando duplicadas na caixa de entrada desde ontem, cada msg do cliente aparece 2x. self-hosted em docker. como resolvo? |
| 87 | como configuro mensagem de ausência e respostas rápidas no app do WhatsApp Business? acabei de baixar no celular da loja |
| 88 | Meu workflow do n8n que lê os emails do Gmail e resume com a OpenAI dá erro 429 no nó da OpenAI quase toda execução. Como faço pra ele esperar e tentar de novo? |
| 89 | o menu do topo do meu site em wordpress quebra em duas linhas no celular. css atual: .navbar ul { display:flex; gap:24px } como arrumo? |
| 90 | Melhora esse prompt que eu uso no ChatGPT pra resumir as atas de reunião do condomínio: "Resuma a ata abaixo em tópicos, destacando decisões e valores aprovados." Ele tem deixado passar os prazos. |
| 91 | como faço a autenticação OAuth2 na API do Google Calendar em python pra listar os eventos da semana? fico tomando invalid_grant |
| 92 | me faz um template de contrato de locação residencial em word, com cláusula de reajuste pelo IPCA e multa por rescisão |
| 93 | monta um fluxo de caixa mensal em excel pra minha oficina |
| 94 | escreve uma msg curta de agradecimento pros padrinhos do meu casamento |
| 157 | monta um typebot de captação de lead pra corretora de seguros: pergunta nome, telefone e tipo de seguro, e no fim grava tudo numa planilha do google sheets |
| 158 | meu fluxo no manychat parou de responder comentário no instagram desde ontem. o gatilho por palavra-chave tá ativo e a conta tá conectada. o que pode ser? |
| 159 | No Chatwoot as conversas do WhatsApp estão caindo todas na caixa de entrada errada e a atribuição automática não distribui pros agentes. Como arrumo? |
| 160 | preciso de um workflow no n8n que receba o webhook da Evolution API e responda o cliente usando o gpt-4o-mini, guardando o histórico no redis. me passa os nós e as configs |
| 161 | a z-api devolve erro dizendo que a instância tá desconectada toda vez que tento enviar texto, mesmo com o qr code lido e o celular online. como resolvo? |
| 162 | Como crio no builder do Blip um bloco de atendimento humano que direciona pra fila de Cobrança do Blip Desk depois do menu? |
| 163 | preciso de um css pra esconder o rodapé do tema Astra no meu site em wordpress e trocar a cor do botão do formulário de contato pra laranja |
| 164 | Me ajuda a escrever as instruções de um GPT personalizado lá no ChatGPT pra ser meu consultor de produtos? Loja de suplementos, vou usar só eu mesma pra tirar dúvida de composição. |
| 165 | escreve um script python que usa a api da openai pra resumir transcrições de reunião em tópicos e salvar num .md |
| 166 | meu backend em express fala com a Cloud API do WhatsApp pela graph api da meta. como registro o webhook e respondo o desafio do verify_token? e como envio um template hello_world de teste |
| 167 | como configuro mensagem de ausência e resposta rápida no aplicativo WhatsApp Business do celular? é o app comum, o do B, uso sozinha no meu ateliê |
| 168 | Escreve uma sequência de 3 e-mails de campanha de reativação pra minha base no Mailchimp: loja de roupas femininas, clientes que não compram há 6 meses, cupom de 15%. |
