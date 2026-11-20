# Tipo Prompt

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/tipo-prompt
- **Categoria:** Recursos
- **Menu:** Inteligência Artificial › GPT Assistant › Tipo Prompt

---

🧩 O tipo **Prompt** monta a IA dentro da própria plataforma: você escreve as instruções, escolhe o modelo e liga o prompt a um **Setor**. A partir daí, a IA responde os clientes que aguardam nesse Setor e, quando o cliente pede uma pessoa, transfere o atendimento para o Setor de transbordo.

**Antes de começar:** a plataforma precisa da chave da OpenAI, colada no campo **Token OpenAI** do card **OPEN.AI**, no menu **Integrações**. Se o card avisar que a conta usa a chave da plataforma, não há chave a cadastrar.

## Como criar um GPT Assistant do tipo Prompt

Acesse o menu **Prompts OPEN.AI  ›  Adicionar Prompt**

![Janela do prompt com os campos Tipo, Nome, Prompt, GPT Model, transbordo, voz e parâmetros](https://clihelper.chatmasterveloz.com/docs-imagem/21242-gptAssistant-config-prompt-1024x862.jpg)

#### Tipo

Prompt. A outra opção da lista, **Agente OpenAI**, aparece desativada e não funciona mais.

#### Nome

Defina um rótulo para seu Assistente. O nome também assina as respostas da IA na conversa.

#### Gatilho para Acionar em Grupos

A palavra que chama o assistente num grupo de WhatsApp, no começo da mensagem. A tela orienta *"Exemplo: #meubot | Evite usar @"*, e a ajuda do campo resume quem responde: *"No grupo, responde o prompt do contato do grupo. Sem ele, responde o prompt do Setor do atendimento, só nas mensagens que começam com este gatilho."*

#### Prompt

Nesse campo, você define as **instruções, regras e direções** para o seu assistente, como:  
- **Tom de voz e estilo** das respostas.
- **Limites e restrições** sobre o que ele pode ou não fazer.
- **Objetivos, referências e formatos de resposta**, entre outros ajustes.

#### COMANDOS DA IA

O botão abre a janela que escreve, com os dados da sua empresa, a instrução de uma ação que a IA executa no atendimento, como transferir ou encerrar, e a acrescenta no fim do campo **Prompt**. A IA só executa a ação que o prompt manda.

#### Modelo da IA

Escolha o modelo de IA para o seu assistente, considerando desempenho e custo. A primeira opção, **Modelo do provedor**, mostra entre parênteses o modelo que vale para a empresa e segue esse modelo. Com a OpenAI, a lista traz também os modelos da conta dona da chave que a sua empresa usa, e uma ótima opção é o **“gpt-4o-mini”**, que oferece qualidade e agilidade com um custo baixíssimo.

#### Setor para Atendimento Humano (Transbordo)

Escolha um **Setor** para o GPT Assistant transferir a conversa quando solicitado um atendimento humano. O campo é obrigatório: sem ele, a janela avisa *"Informe o setor"*.

#### Mensagem de Transbordo

Mensagem personalizada que o GPT envia quando entende que deve transferir para um atendimento humano. Com o campo vazio, a plataforma envia *"Aguarde enquanto transfiro para um atendente..."*.

#### Base de conhecimento

O material que a IA consulta antes de responder: horários, políticas, preços, perguntas frequentes. As bases são cadastradas no menu **Prompts OPEN.AI  ›  Base de Conhecimento**. Com **Nenhuma**, a IA não consulta material além do prompt.

#### Voz

Modo que seu assistente enviará as respostas:

**➡️** via **Texto**

**➡️** ou por voz de uma IA: **Francisca (Feminino)**, **Antonio (Masculino)**, **Jenny (English)**, **Guy (English)**, **Elvira (Español)** ou **Alvaro (Español)**.

Tenha em mente que a opção por voz tem um custo extra, através da Microsoft Azure, e demanda a integração nos campos:  
- **Chave da API de Voz** (fornecida pela Azure)
- **Região de Voz**

Obs: deixe esses dois campos vazios se optar por “Texto”

#### Temperatura

Ajuste de **0 a 2**: quanto mais alto, mais criativo o assistente será; quanto mais perto de **0**, mais ele seguirá fielmente o prompt. A tela não aceita valor acima de 2.

#### Tokens

Determina o **limite máximo de texto gerado na resposta**. O campo aceita um número inteiro de 1 para cima: com **0**, a tela avisa *"Use um número inteiro de 1 para cima."* e o prompt não é salvo.

Um token pode representar uma palavra curta, um pedaço de palavra ou até um espaço, ou seja, a cada token representa em média de 3 a 4 caracteres.

**Sugestão**: entre 500 a 1000 tokens é um bom início. Mas faça testes para encontrar um ponto ideal para o seu negócio.

#### Máximo de mensagens no Histórico

Quantidade de últimas mensagens que o assistente guarda no histórico para entender o contexto da conversa.

**Sugestão**: entre 10 a 20 mensagens, mas depende também do seu negócio.

Os campos **Tokens** e **Máximo de mensagens no Histórico** impactam diretamente o custo do seu GPT.

Isso ocorre porque o custo é calculado com base na quantidade de **informações processadas**, incluindo todo o histórico da conversa (mensagens anteriores + última pergunta) e o **tamanho da resposta** gerada pelo seu assistente GPT.

Faça testes nesses dois campos para ir otimizando seus custos conforme a necessidade de seu negócio.

## Como ativar seu GPT Assistant do tipo Prompt

Com um GPT Assistant criado, acesse o menu **Setores & Chatbot**, edite o Setor e, no campo **Prompt OPEN.AI (ChatGPT)**, defina qual assistente será ativado nesse Setor. O card do Setor passa a mostrar o selo **Prompt GPT**.

![Cadastro do Setor com o campo Prompt OPEN.AI (ChatGPT) preenchido](https://clihelper.chatmasterveloz.com/docs-imagem/21242-gptAssistant-ativar-1024x810.jpg)

O jeito recomendado de levar o cliente até esse Setor é o bloco **GPT Assistant (OpenAI)** do **FlowBuilder**, que lista só os Setores com prompt e pode devolver o atendimento ao fluxo quando o cliente fica sem responder. O Setor também pode receber a conversa direto, pela Conexão ou por transferência.

> **[ATENCAO]**
>
> #### Importante
>
> O GPT Assistant responde nos Setores em que foi escolhido, e somente quando o atendimento estiver em **Aguardando**. Com o atendimento aceito por alguém da equipe, ele fica calado; se o atendimento voltar para **Aguardando**, ele volta a responder. O mesmo prompt pode ficar em mais de um Setor.

#### 💭 Tenha em mente

O seu assistente começa a agir somente depois que o atendimento passa para o Setor do GPT.

Sendo assim, estimule seu cliente a enviar uma mensagem após essa troca de Setor.

Mensagens enviadas antes da troca para o Setor do GPT não serão respondidas pelo seu assistente. Quando o cliente escreve de novo, a IA lê também o que veio antes e pode responder a pergunta antiga junto com a nova.

## Como a resposta da IA aparece na conversa

A resposta da IA chega em poucos segundos. Na conversa, a mensagem aparece assinada com o nome do prompt seguido de **(IA)**, por exemplo *"Assistente Virtual (IA)"*, e com o selo **IA**, para a equipe saber o que foi escrito pela IA. Quando o nome do prompt já termina em IA, como *"Bia IA"* ou *"Bia (IA)"*, a assinatura mostra o nome como está, sem repetir o **(IA)**.

Quando o cliente escreve aos pedaços, em várias mensagens curtas seguidas, a IA espera o cliente terminar e responde uma vez só, ao pedido inteiro. Se o cliente manda uma pergunta nova depois da resposta, a IA responde à pergunta nova.

## Transbordo: quando a IA passa para uma pessoa

Quando o cliente pede para falar com uma pessoa, a IA envia a **Mensagem de Transbordo** e passa o atendimento para o Setor escolhido em **Setor para Atendimento Humano (Transbordo)**.

⚠️ Para a conversa ficar com a equipe, escolha como transbordo um Setor **sem** prompt. Se o Setor de transbordo tiver prompt, inclusive o próprio Setor da IA, a IA desse Setor continua respondendo.

## Áudio do cliente

Com a opção **Ativar Transcrição de Áudio** ligada no cadastro do Setor, o áudio do cliente é transcrito e a IA responde ao conteúdo dele, no WhatsApp, no WebChat e no Chat Externo. No WhatsApp e no WebChat, o texto transcrito fica junto da mensagem de áudio, na conversa; no Chat Externo, chega numa mensagem à parte, marcada **Transcrição do áudio**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O que acontece com o Setor quando eu excluo um prompt em uso?** Ao clicar para excluir, a janela avisa em quais Setores o prompt está em uso: *"Este prompt está em uso no(s) setor(es):"*, seguido dos nomes, e *"Eles ficarão sem IA."* Com **OK**, o prompt é excluído e esses Setores ficam sem IA, sem responder os clientes que aguardam neles, até você escolher outro prompt no cadastro do Setor.
