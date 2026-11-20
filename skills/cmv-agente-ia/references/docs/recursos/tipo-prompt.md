# Tipo Prompt

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/tipo-prompt
- **Categoria:** Recursos
- **Menu:** Inteligência Artificial › GPT Assistant › Tipo Prompt

---

**Antes de continuar, é necessário integrar a Inteligência Artificial à nossa plataforma. Saiba como em “Pré-Requisitos de IA”**

## Como criar um GPT Assistant do tipo Prompt

Acesse o menu → Prompts Open.Ai > Adicionar Prompt

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/21242-gptAssistant-config-prompt-1024x862.jpg)

#### Tipo

Prompt

#### Nome

Defina um rótulo para seu Assistente

#### Prompt

Nesse campo, você define as **instruções, regras e direções** para o seu assistente, como:  
- **Tom de voz e estilo** das respostas.
- **Limites e restrições** sobre o que ele pode ou não fazer.
- **Objetivos, referências e formatos de resposta**, entre outros ajustes.

#### GPT Model

Escolha o modelo de IA para o seu assistente, considerando desempenho e custo. Uma ótima opção é o **“gpt-4o-mini”**, que oferece qualidade e agilidade com um custo baixíssimo.

#### Setor para Atendimento Humano (Transbordo)

Escolha um **Setor** para o GPT Assistant transferir a conversa quando solicitado um atendimento humano.

#### Mensagem de Transbordo

Mensagem personalizada que o GPT envia quando entende que deve transferir para um atendimento humano.

#### Voz

Modo que seu assistente enviará as respostas:

**➡️** via **Texto**

**➡️** ou por voz de uma IA.

Tenha em mente que a opção por voz tem um custo extra, através da Microsoft Azure, e demanda a integração nos campos:  
- **Chave da API de Voz** (fornecida pela Azure)
- **Região da Voz**

Obs: deixe esses dois campos vazios se optar por “Texto”

#### Temperatura

Ajuste de **0 a 2**: quanto mais alto, mais criativo o assistente será; quanto mais perto de **0**, mais ele seguirá fielmente o prompt.

**OBS:** Coloque temperatura “1” para o agente interpretar corretamente áudios enviados pelos clientes.

#### Tokens

Determina o **limite máximo de texto gerado na resposta**.

Um token pode representar uma palavra curta, um pedaço de palavra ou até um espaço, ou seja, a cada token representa em média de 3 a 4 caracteres.

**Sugestão**: entre 500 a 1000 tokens é um bom início. Mas faça testes para encontrar um ponto ideal para o seu negócio.

#### Máximo de Mensagens no Histórico

Quantidade de últimas mensagens que o assistente guarda no histórico para entender o contexto da conversa.

**Sugestão**: entre 10 a 20 mensagens, mas depende também do seu negócio.

Os campos **Tokens** e **Máximo de Mensagens no Histórico** impactam diretamente o custo do seu GPT.

Isso ocorre porque o custo é calculado com base na quantidade de **informações processadas**, incluindo todo o histórico da conversa (mensagens anteriores + última pergunta) e o t**amanho da resposta** gerada pelo seu assistente GPT.

Faça testes nesses dois campos para ir otimizando seus custos conforme a necessidade de seu negócio.

## Como ativar seu GPT Assistant do tipo Prompt

Com um GPT Assistant criado, acesse o menu **Setores & Chatbot**, edite o Setor e, no campo **Prompt OPEN.AI (ChatGPT)**, defina qual assistente será ativado nesse Setor.

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/21242-gptAssistant-ativar-1024x810.jpg)

> **[ATENCAO]**
>
> #### Importante
>
> Cada GPT Assistant funciona em **um Setor** e somente quando o atendimento estiver em **Aguardando**

#### 💭 Tenha em mente

O seu assistente começa a agir somente depois que o atendimento passa para o Setor do GPT.

Sendo assim, estimule seu cliente a enviar uma mensagem após essa troca de Setor.

Mensagens enviadas antes da troca para o Setor do GPT não serão respondidas pelo seu assistente.
