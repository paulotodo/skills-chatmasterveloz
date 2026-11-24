# Entrevista de briefing para o atendente de IA

O prompt só fica bom se quem escreve souber o que a empresa vende, o que a IA pode afirmar e quando deve passar a conversa para uma pessoa. Esta entrevista levanta isso. Ela é método de trabalho desta skill (boa prática de redação de prompt), não conteúdo da documentação do Chat Master Veloz; o que é mecânica da plataforma está em `references/comandos-e-capacidades.md`.

## Como conduzir

- **A primeira resposta é curta.** Quem escreveu duas linhas ("tenho uma clínica e quero o ChatGPT respondendo no WhatsApp") não quer um questionário nem um manual. Use a primeira rodada da seção seguinte: cinco ou seis perguntas, e a oferta de um rascunho.
- **Aproveite o que já foi dito.** Antes de perguntar, releia a conversa: se a pessoa colou o site, a tabela de preços ou um prompt antigo, tire dali o que der e pergunte só o que falta.
- **Peça material pronto.** "Pode colar aqui as respostas que sua equipe mais repete?" rende mais que dez perguntas, e traz o tom real da empresa.
- **Quando a pessoa não souber**, use a saída indicada em cada grupo: proponha um padrão, diga que é um padrão e registre como "a confirmar". O que continuar em aberto vira regra de cautela no prompt ("não informe X; transfira para a equipe") ou marcador `[[...]]`, nunca um dado inventado.
- **Se a pessoa preferir o rascunho** ("faz aí que depois eu ajusto"), escreva com o que há, deixe as lacunas como marcadores e liste o que falta preencher. Rascunho com lacunas marcadas é entrega válida; prompt com dado de exemplo no lugar do dado real, não.
- **Aprofunde só o que o caso pede.** Os grupos 1 a 9 são repertório para a segunda rodada, quando a primeira versão já existe e a pessoa quer melhorar um ponto. Não percorra todos.
- **Confirme o que entendeu** em poucas linhas no começo da entrega (modelo no fim deste arquivo), em vez de uma rodada só para aprovar o resumo.

## Primeira rodada: o mínimo para escrever

São as perguntas da primeira resposta. Adapte as palavras ao ramo da pessoa e corte as que ela já respondeu.

1. Qual é o nome da empresa e o que vocês oferecem, em uma ou duas frases?
2. O que a IA pode responder? Cole aqui o que tiver: serviços, preços que ela pode informar, horário, endereço, formas de pagamento.
3. O que ela não pode dizer nem prometer? (Se não souber, eu proponho uma lista padrão.)
4. Quando a conversa deve passar para uma pessoa, e para qual equipe ou Setor?
5. A pergunta do objetivo: para agendar, que dados a equipe precisa receber e quem confirma o horário; para qualificar, o que define um bom contato; para suporte, quais problemas ela pode orientar.
6. O que já está pronto: você é administrador do painel e vê o menu **Prompts OPEN.AI**? A chave da OpenAI já está no card **OPEN.AI** do menu **Integrações** (ou o card diz que a conta usa a chave da plataforma)? (Não me envie a chave.)

Com as respostas 1 a 5 já sai um prompt completo ou quase. O que faltar vira marcador.

## Grupo 0: ponto de partida

Perguntas:

- Você é administrador do painel? (Os menus **Prompts OPEN.AI** e **Sugestão de resposta IA** aparecem só para o perfil Administrador; o menu **Avaliação pela IA** aparece também para Supervisor e Atendente.)
- O menu **Prompts OPEN.AI** aparece para você, e o token da OpenAI já está no card **OPEN.AI** do menu **Integrações** (ou o card diz que a conta usa a chave da plataforma)?
- Já existe algum assistente em **Prompts OPEN.AI**? Se sim, pode colar o prompt atual e contar o que está dando errado?
- Hoje, como o cliente chega até vocês: direto em um Setor, por menu de Setores ou por um fluxo do FlowBuilder?

Por que perguntar: define se o trabalho começa pelos pré-requisitos, se é criação ou correção, e em que Setor a IA vai ser ligada. Evita entregar um prompt ótimo para quem ainda não consegue abrir o menu. Se o menu **Prompts OPEN.AI** não aparece para quem é Administrador, o que o libera é a opção de plano **GPT Assistant**, que precisa também da **AI**: quem liga é quem fornece a plataforma (o suporte), não a própria empresa (`references/docs/revendedor/recursos/configuracoes-planos.md`).

Se não souber: mostre onde olhar (`references/docs/recursos/pre-requisitos-ia.md`, `references/docs/recursos/token-openai.md`, `references/docs/recursos/visao-geral-setores-e-chatbot.md`) e siga com a entrevista; os pré-requisitos entram como passo 1 da entrega.

## Grupo 1: negócio e objetivo

Perguntas:

- Qual é o nome da empresa e o que ela vende ou faz, em uma ou duas frases?
- O que você quer que a IA resolva sozinha? (Tirar dúvidas, qualificar o interessado, agendar, vender, dar suporte.) Se for mais de uma coisa, qual vem primeiro?
- Como você vai saber que deu certo? (Menos mensagens repetidas para a equipe, mais agendamentos, lead chegando com os dados prontos.)
- A IA terá um nome? Ela deve se apresentar como assistente virtual?

Por que perguntar: o objetivo define o roteiro da conversa. Um agente que "faz tudo" responde mal a tudo; com uma prioridade clara, o prompt consegue dizer o que fazer primeiro e quando parar.

Se não souber: proponha começar pelo objetivo mais simples e de menor risco, que é tirar as dúvidas frequentes e transferir o resto. Sobre o nome: sugira um e recomende que a IA se apresente como assistente virtual, porque cliente que descobre depois se sente enganado.

## Grupo 2: público e canal

Perguntas:

- Quem escreve para vocês? (Pessoa física ou empresa, faixa de idade, já cliente ou primeiro contato.)
- O que essas pessoas mais perguntam? Quais são as cinco ou dez dúvidas mais comuns?
- Os clientes costumam mandar áudio?
- A IA vai atender em conversa privada, em grupo, ou nos dois?

Por que perguntar: o público define vocabulário e paciência; as dúvidas mais comuns viram a base de conhecimento; o áudio decide ligar **Ativar Transcrição de Áudio** no Setor da IA (com ela, a IA responde ao que foi falado); grupo pede o **Gatilho para Acionar em Grupos**, a escolha de quem responde no grupo e as travas de grupo liberadas (`references/configuracao-painel.md`, "Opcional: usar o assistente em um grupo").

Se não souber: peça que role as conversas dos últimos dias e copie as perguntas que mais se repetem, ou que pergunte a quem atende. Sem isso, escreva a base só com o que foi informado e deixe a transferência como saída para o resto.

## Grupo 3: o que a IA pode responder (base de conhecimento)

Perguntas:

- Horário de atendimento, endereço, formas de contato e de pagamento.
- Produtos ou serviços: lista, descrição curta, diferenciais.
- Preços: a IA pode informar? Quais, exatamente? Há preço que só a equipe passa?
- Prazos, entrega, garantia, troca, cancelamento: quais são as regras?
- Links que ela pode enviar (site, catálogo, localização).

Por que perguntar: o assistente sabe o que está escrito no campo **Prompt** e o que estiver na **Base de Conhecimento** ligada a ele (itens digitados ou lidos de arquivo .pdf, .docx, .txt, .md ou .csv; site não). Tudo que ele pode afirmar precisa estar num dos dois, com as palavras certas. Se a pessoa tem um material pronto (tabela de preços, perguntas frequentes), ele pode ir para a base.

Se não souber: o que a pessoa não souber informar agora fica fora da base, e o prompt manda dizer que a equipe confirma e transferir. Para preço, o padrão seguro é não informar e encaminhar. Nunca preencha com valores "de exemplo" na versão final.

## Grupo 4: o que a IA não pode responder (limites)

Perguntas:

- Há assunto proibido ou delicado? (Diagnóstico, orientação jurídica, desconto, negociação de dívida, reclamação, concorrente.)
- Há promessa que só uma pessoa pode fazer? (Prazo especial, exceção de política, reserva garantida.)
- Há dado que ela não deve pedir? (Senha, número de cartão, documento.)
- Se o cliente puxar assunto fora do negócio, ela responde ou volta ao tema?

Por que perguntar: o erro mais caro de um atendente de IA é prometer o que a empresa não cumpre. Limite escrito é limite respeitado; limite presumido não existe para o modelo.

Se não souber: proponha a lista padrão e peça confirmação. Padrão: não inventar preço, prazo, estoque ou política; não dar desconto nem negociar; não dar orientação profissional (saúde, jurídica, financeira); não pedir senha nem dados de cartão; não falar de concorrentes; fora do tema, recusar com educação e voltar ao atendimento.

## Grupo 5: tom e estilo

Perguntas:

- Como a empresa fala com o cliente: formal, próximo, descontraído? Trata por "você" ou "senhor/senhora"?
- Usa emoji? Tem expressão que é a cara da empresa, ou palavra que não usa?
- Pode colar duas ou três respostas reais de um bom atendente?

Por que perguntar: tom descrito por adjetivo ("simpático") vira texto genérico; tom mostrado por exemplo real é imitado com fidelidade.

Se não souber: padrão para WhatsApp: cordial e direto, "você", frases curtas, uma pergunta por mensagem, sem emoji. Avise que é um padrão e que os testes mostram se combina.

## Grupo 6: transferência para humano

Perguntas:

- Em que situações a conversa deve ir para uma pessoa? (Pedido do cliente, reclamação, fechamento de venda, assunto fora da base, cliente irritado.)
- Para qual Setor vai cada situação? É sempre o mesmo ou depende do assunto?
- Alguma situação vai para uma pessoa específica?
- O que a IA deve dizer na hora de transferir? Fora do horário da equipe, o que muda nessa mensagem?
- Esse Setor de destino tem algum robô ligado (fluxo ou outro assistente)?

Por que perguntar: a plataforma tem dois mecanismos de transferência (os campos de **Transbordo** e os comandos **Transferir para um setor** e **Transferir para um operador**), e ambos pedem Setor definido. O assistente só atua nos Setores em que foi escolhido, com o atendimento em **Aguardando**. A skill recomenda que o Setor da equipe seja outro, sem assistente ligado (`references/comandos-e-capacidades.md`, seção 6).

Se não souber: padrão mínimo: transferir quando o cliente pedir uma pessoa, quando reclamar, quando a resposta não estiver na base e quando a mesma dúvida voltar pela segunda vez; tudo para um único Setor humano. Se a empresa só tem um Setor, explique que a skill recomenda criar outro para a IA (ou para a equipe) e inclua isso no passo a passo.

## Grupo 7: dados a coletar

Perguntas:

- Que dados a equipe precisa receber prontos? (Nome, cidade, produto de interesse, orçamento, melhor dia e horário.)
- Em que ordem faz sentido perguntar? Algum é obrigatório para seguir?
- O que caracteriza um bom lead para vocês? E um que não vale encaminhar?
- Depois de coletar, o que acontece: transfere, marca com tag, agenda?

Por que perguntar: coleta sem ordem vira interrogatório. Com a lista fechada, o prompt manda perguntar um dado por vez, não repetir o que o cliente já disse e confirmar tudo no fim.

Se não souber: padrão: nome, o que procura e melhor horário para contato, nessa ordem; depois, transferir. Mais que quatro ou cinco dados costuma derrubar a conversa no WhatsApp; proponha cortar.

## Grupo 8: ações na plataforma

Perguntas:

- A IA deve marcar a conversa com alguma tag? Em que momento (no turno da tag o cliente não recebe mensagem)? A tag já existe no menu **Tags**?
- A IA deve registrar uma oportunidade no CRM? Em que funil e etapa, com quais respostas do cliente?
- Pode encerrar o atendimento sozinha quando o cliente disser que não precisa de mais nada?
- Para agendamento: a equipe confirma o horário ou a IA marca sozinha na agenda da plataforma? Nesse segundo caso, qual o tipo de compromisso (Reunião, Ligação, Visita, Lembrete ou Tarefa), a duração, e se a IA também desmarca?
- Para que Setor (ou pessoa) vai cada transferência? Basta o nome: a janela **COMANDOS DA IA** escolhe pelo nome.

Por que perguntar: só existem os seis comandos documentados (**Transferir para um setor**, **Transferir para um operador**, **Marcar com uma tag**, **Encerrar o atendimento**, **Registrar oportunidade no CRM** e **Marcar ou desmarcar na agenda**), e cada um pede os seus campos na janela **COMANDOS DA IA**.

Se não souber: entregue o prompt com os marcadores de comando e a tabela "o que falta preencher e onde achar"; como usar a janela **COMANDOS DA IA** está em `references/comandos-e-capacidades.md`, seção 4, e `references/configuracao-painel.md`, etapa 5. Para agendamento sem definição, use a variante A de `assets/modelo-prompt.md`: a IA coleta e a equipe confirma.

## Grupo 9: operação e custo

Perguntas:

- A resposta será só por texto ou também por voz? (A voz tem custo extra, pela Microsoft Azure.)
- As conversas costumam ser longas? (Ajuda a escolher o **Máximo de mensagens no Histórico**.)
- Há preocupação forte com custo?

Por que perguntar: **Tokens** e **Máximo de mensagens no Histórico** impactam diretamente o custo, e a cobrança vai para a conta da OpenAI dona da chave em uso: a da empresa ou, quando o card **OPEN.AI** avisa que a conta usa a chave da plataforma, a conta dona dessa chave.

Se não souber: use os valores para o caso comum de `references/configuracao-painel.md`, etapa 4, e ajuste depois dos testes.

## O que entendi (para abrir a entrega)

Use só as linhas que se aplicam; na primeira entrega, cinco ou seis bastam.

```text
O QUE ENTENDI — me corrija se algo estiver errado

Empresa: ...
Objetivo principal da IA: ...
Objetivos secundários: ...
Nome e apresentação da IA: ...
Público: ...
Pode responder sobre: ...
Não pode responder nem prometer: ...
Tom: ...
Dados a coletar, na ordem: ...
Transferir para uma pessoa quando: ...
Setor de destino: ...
Tags e momento de aplicar: ...
Pode encerrar o atendimento sozinha: sim / não
Agendamento: não se aplica / coleta e transfere / comando de agenda (tipo e duração)
Áudio dos clientes: frequente / raro
Resposta: texto / voz

A confirmar (presumi um padrão): ...
```
