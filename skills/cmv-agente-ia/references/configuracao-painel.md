# Receita: colocar o GPT Assistant no ar pelo painel

Sequência que junta, na ordem de execução, o que está espalhado por vários artigos. Use-a para montar o passo a passo da entrega, pulando o que a pessoa já fez. Os nomes de menu, de campo e de botão que aparecem aqui foram conferidos nos artigos e podem ser usados sem reabri-los. Abra o artigo da etapa quando a pessoa perguntar algo que este resumo não cobre, quando a tela dela for diferente do descrito, ou para copiar o link da linha **Fonte** (o índice `references/docs/INDICE.md` traz o link de cada artigo).

O que é fato documentado, recomendação da skill ou ponto não documentado está explicado em `references/comandos-e-capacidades.md`; aqui fica o procedimento.

Quem executa: o perfil **Administrador**. Os menus **Prompts OPEN.AI**, **Setores & Chatbot**, **Conexões** e **Integrações** só aparecem para ele (`references/docs/recursos/tipos-de-perfil.md`).

## Etapa 1: pré-requisitos

Artigos: `references/docs/recursos/pre-requisitos-ia.md`, `references/docs/recursos/token-openai.md`.

1. No painel, menu **Integrações**, olhar o card **OPEN.AI**. Se ele avisar "A inteligência artificial desta conta usa a chave da plataforma. Não é preciso cadastrar uma chave aqui.", não há token a criar nem a colar: pule os passos 2 e 3.
2. Criar o token na OpenAI: em https://platform.openai.com, entrar, ir em Dashboard > API Keys, criar uma nova chave (Create New Secret Key), dar um nome, copiar o token e guardar em local seguro.
3. No card **OPEN.AI**, colar a chave no campo **Token OpenAI**. Cada campo grava sozinho, sem botão Salvar; o campo esconde a chave, com o botão **Mostrar a chave**. **Model OpenAI** e **Idioma OpenAI** ficam vazios para manter o padrão.

Se um recurso de IA não aparecer para a pessoa, o artigo Pré-Requisitos IA manda falar com o suporte do Chat Master Veloz: cada recurso aparece por uma condição própria da conta, e alguns ficam só com o administrador.

A chave é da empresa: é na conta dona dela que a OpenAI cobra o consumo, e ela dá acesso à parte financeira. Não peça a chave; se a pessoa colar no chat, recomende gerar outra.

No mesmo menu, o card **Provedor de IA** escolhe "qual serviço de IA responde os prompts de chat" (`references/docs/recursos/provedor-de-ia.md`). Para usar a OpenAI, ele fica em **OpenAI**, que "mantém o comportamento atual", e o **Modelo** e a **Chave de API do provedor** não são obrigatórios: "Na OpenAI vale o modelo padrão e a chave da seção OpenAI, acima." Com outro provedor, o **Modelo** e a **Chave de API do provedor** são obrigatórios, e o card guarda uma chave só: ao trocar de provedor, cole a chave do novo.

## Etapa 2: Setores

Artigos: `references/docs/recursos/aba-geral-em-setores-e-chatbot.md`, `references/docs/recursos/visao-geral-setores-e-chatbot.md`, `references/docs/recursos/aguardando-x-atendendo.md`.

A skill recomenda dois Setores, o da IA e o da equipe, sem prompt: o artigo Tipo Prompt avisa que, se o Setor de transbordo tiver prompt, a IA continua respondendo (`references/comandos-e-capacidades.md`, seção 6).

1. Menu **Setores & Chatbot** › **ADICIONAR SETOR** (ou o lápis de um Setor existente).
2. Preencher **Nome**, **Ordenação do BOT** e **Cor**, que são obrigatórios, e clicar em **Adicionar** (Setor novo) ou **Salvar** (Setor existente).
3. No card do Setor da IA, conferir os selos: ele não deve ter outro motor de automação (**FlowBuilder**, **Chatbot**). A tela aceita dois sem avisar, e aí fica difícil prever qual responde.
4. No Setor da equipe, conferir duas coisas: que não tem o selo **Prompt GPT** e que há atendentes nele. O artigo da aba Geral indica como próximo passo "Cadastrar quem atende este Setor, no menu **Equipe › editar o usuário**", e o artigo Aguardando x Atendendo avisa que o atendente só vê em Aguardando os atendimentos dos Setores em que tem permissão. Sem ninguém no Setor, a transferência da IA cai em uma fila que ninguém enxerga.

## Etapa 3: tags (se o prompt usa tag)

Artigo: `references/docs/recursos/visao-geral-tags.md`.

1. Menu **Tags** › **+ NOVA TAG** para criar a que faltar.
2. A janela **COMANDOS DA IA** escolhe a tag pelo nome (etapa 5). O **ID** que aparece no lado direito de cada tag só serve para conferir o bloco inserido.

## Etapa 4: criar o assistente

Artigos: `references/docs/recursos/tipo-prompt.md`, `references/docs/recursos/base-de-conhecimento-do-gpt-assistant.md`.

Menu **Prompts OPEN.AI** › **Adicionar Prompt**. A coluna "valor para o caso comum" é recomendação desta skill, sempre dentro do que o artigo permite; diga isso à pessoa e ajuste depois dos testes.

| Campo | O que o artigo diz | Valor para o caso comum e a razão |
|---|---|---|
| **Tipo** | **Prompt** (o tipo Agente OpenAI aparece desativado) | **Prompt** |
| **Nome** | Rótulo do assistente; assina as respostas da IA na conversa | Um nome que o cliente possa ler, como "Lia" ou "Assistente Virtual": a conversa mostra "Lia (IA)" |
| **Gatilho para Acionar em Grupos** | Só para uso em grupo | Vazio, salvo uso em grupo (fim deste arquivo) |
| **Prompt** | Recebe as instruções | O texto entregue, colado inteiro |
| **Modelo da IA** (antes **GPT Model**) | A primeira opção, **Modelo do provedor**, mostra entre parênteses o modelo que vale para a empresa; com a OpenAI, a lista traz os modelos da conta dona da chave e sugere o "gpt-4o-mini": qualidade e agilidade com custo baixíssimo | "gpt-4o-mini", por ser a sugestão do artigo. Se ele não aparecer na lista, peça à pessoa que diga quais opções aparecem, em vez de indicar um nome que pode não existir na tela dela |
| **Setor para Atendimento Humano (Transbordo)** | Setor para onde o GPT transfere quando solicitado um atendimento humano; obrigatório ("Informe o setor") | O Setor da equipe, sem prompt |
| **Mensagem de Transbordo** | Mensagem enviada quando o GPT entende que deve transferir; vazia, vai "Aguarde enquanto transfiro para um atendente..." | Uma frase curta que diga quem continua a conversa e o horário da equipe |
| **Base de conhecimento** | A base que o prompt consulta antes de responder, ou **Nenhuma** | **Nenhuma** quando as informações cabem no prompt; uma base quando há material longo (tabela de preços, perguntas frequentes). Como criar: logo abaixo |
| **Voz** | **Texto** ou voz de uma IA (custo extra, Microsoft Azure) | **Texto**, com **Chave da API de Voz** e **Região de Voz** vazias |
| **Temperatura** | De 0 a 2; perto de 0, mais fiel ao prompt; não aceita acima de 2 | **0,5**. O artigo não dá um número; mais perto de 0 a IA segue mais o prompt e as instruções dos comandos. Se as respostas saírem duras ou repetitivas nos testes, suba um pouco |
| **Tokens** | Limite máximo de texto gerado na resposta; entre 500 e 1000 para começar; não aceita 0 | **500**. O prompt pede mensagens curtas, e esse é o piso da faixa do artigo. Se alguma resposta vier cortada, suba |
| **Máximo de mensagens no Histórico** | Últimas mensagens guardadas para o contexto; entre 10 e 20 | **20** quando há coleta de dados (a IA precisa lembrar o que o cliente disse no começo até a confirmação); **10** quando é só tirar dúvidas |

A janela grava com **Salvar** (**Adicionar**, no prompt novo).

**Base de Conhecimento (opcional).** Menu **Prompts OPEN.AI** › **BASE DE CONHECIMENTO** › **NOVA BASE**: preencher **Nome da base** e clicar em **SALVAR**; abrir a base e acrescentar cada informação em **NOVO ITEM** (**Título** e **Conteúdo**; o título pesa mais na busca, então use as palavras que o cliente usaria) ou em **ENVIAR ARQUIVO** (.pdf, .docx, .txt, .md ou .csv, um por vez; confira o texto extraído antes de salvar). Depois, escolher a base no campo **Base de conhecimento** do prompt e salvar. Com base, o prompt ainda precisa da regra de não inventar e de transferir o que não estiver escrito.

## Etapa 5: inserir os comandos pela janela COMANDOS DA IA

Artigo: `references/docs/recursos/comandos-gpt-assistant.md`. O que está e o que não está documentado sobre a janela: `references/comandos-e-capacidades.md`, seções 3 a 5.

Ordem única: os marcadores de dados do negócio são preenchidos antes de colar; o prompt pode ir ao painel levando só os marcadores de comando, que se trocam lá, pela janela **COMANDOS DA IA**; o `--final` roda na versão definitiva, que é a que a pessoa devolve depois do **INSERIR NO PROMPT**, antes dos testes.

Cada marcador de comando do prompt entregue diz o que escolher na janela e o texto de **Quando a IA deve fazer isso**. Roteiro para passar à pessoa (documentado no artigo):

1. Cole o prompt no campo **Prompt**, com os dados do negócio já preenchidos e ainda com os marcadores de comando.
2. Na janela do prompt, clique em **COMANDOS DA IA**.
3. Em **O que a IA deve fazer**, escolha o comando do marcador; em **Quando a IA deve fazer isso**, cole o texto do marcador; preencha os campos do comando (o Setor, o operador ou a tag pelo nome; no de agenda, **Tipo do compromisso** e **Duração (minutos)**). Nos comandos que pedem Setor, pessoa ou tag, o **INSERIR NO PROMPT** só fica ativo depois dessa escolha.
4. Confira a prévia e clique em **INSERIR NO PROMPT**: a instrução entra no fim do campo **Prompt**, numa seção com o nome do comando, e a tela avisa "Instrução adicionada ao prompt".
5. Apague do texto a linha do marcador que acabou de inserir. A lista de situações em que transferir continua no prompt.
6. Repita para cada marcador de comando. No fim, não pode sobrar nenhum `[[` no texto.
7. Clique em **Salvar** na janela do prompt (**Adicionar**, no prompt novo): o comando só vale depois disso.
8. Copie o texto final do campo **Prompt** e cole aqui, para a conferência final (`--final`) antes dos testes.

Quem preferir não editar o texto pode, depois do passo 4, colar aqui o trecho que o painel inseriu, e você devolve o prompt final sem os marcadores.

## Etapa 6: ligar o assistente ao Setor

Artigos: `references/docs/recursos/tipo-prompt.md`, `references/docs/recursos/aba-geral-em-setores-e-chatbot.md`.

1. Menu **Setores & Chatbot** › editar o Setor da IA › aba **Geral**.
2. No campo **Prompt OPEN.AI (ChatGPT)**, escolher o assistente criado.
3. Se os clientes mandam áudio, ligar **Ativar Transcrição de Áudio**: com prompt no Setor, a IA responde ao que foi falado.
4. Clicar em **Salvar**. O card do Setor passa a mostrar o selo **Prompt GPT**.

## Etapa 7: saudação do Setor da IA

Artigos: `references/docs/recursos/aba-mensagens-em-setores-e-chatbot.md`, `references/docs/recursos/tipo-prompt.md`.

O artigo Tipo Prompt recomenda estimular o cliente a escrever depois que a conversa chega ao Setor do assistente. A **Mensagem de saudação** do Setor é o texto que o cliente recebe ao chegar pela Conexão.

1. No mesmo cadastro do Setor, aba **Mensagens**, campo **Mensagem de saudação**.
2. Escrever uma saudação curta que termine pedindo ao cliente que conte o que precisa, e clicar em **Salvar**.

## Etapa 8: testar antes de abrir ao público

Use `assets/plano-de-testes.md`. A seção "Como levar a conversa de teste ao Setor da IA" dá a rota que não mexe na Conexão.

## Etapa 9: fazer as conversas chegarem ao Setor da IA

| Caminho | Como | Artigo |
|---|---|---|
| A Conexão aponta só para o Setor da IA | Menu **Conexões** › editar a Conexão › aba **Setores & Tempos** › em **Setores**, marcar apenas o Setor da IA › **Salvar**. O artigo diz que, com um único Setor, a conversa vai direto para ele. | `references/docs/recursos/setor-unico-com-fluxo-automatico.md` |
| Menu de Setores | Na mesma aba, marcar dois ou mais Setores: o cliente recebe o menu e escolhe. A **Mensagem de saudação** da Conexão passa a ser obrigatória. | `references/docs/recursos/chatbot-e-menu-de-setores-na-conexao.md` |
| Fluxo do FlowBuilder | O bloco **GPT Assistant (OpenAI)** leva a conversa ao Setor com assistente; é o caminho que os artigos GPT Assistant e Tipo Prompt recomendam. O desenho do fluxo é da skill `cmv-flowbuilder`. | `references/docs/recursos/bloco-gpt-assistant-openai.md` |

Recomendação desta skill ao mudar a Conexão: anotar antes quais Setores estavam marcados em **Setores & Tempos**, para poder voltar atrás, e fazer a troca em horário de pouco movimento.

## Opcional: usar o assistente em um grupo

Artigo: `references/docs/recursos/gpt-assistant-em-grupos.md`.

1. Menu **Prompts OPEN.AI**, ao criar ou editar o prompt, preencher **Gatilho para Acionar em Grupos** (a tela orienta "Exemplo: #meubot | Evite usar @"). Vazio, o prompt escolhido no contato do grupo responde sem ser chamado.
2. Escolher quem responde: menu **Contatos** › editar o contato do grupo › campo **Prompt OPEN.AI (ChatGPT)**; ou deixar o contato sem prompt e transferir o atendimento do grupo, que chega sem Setor, para um Setor com prompt (aí a IA só responde às mensagens que começam com o gatilho).
3. No grupo, começar a mensagem com o gatilho: `#meubot quanto custa a entrega?`. Gatilho no fim da frase não chama a IA.

## Limites e custos: o que dá para afirmar

- O consumo é cobrado pela OpenAI, na conta dona da chave; tarifas e limites de uso são consultados na conta da OpenAI (`references/docs/recursos/token-openai.md`). Se o card **OPEN.AI** avisar que a conta usa a chave da plataforma, não há chave a cadastrar.
- **Tokens** e **Máximo de mensagens no Histórico** "impactam diretamente o custo", que é calculado pelo que é processado (histórico mais a última pergunta) e pelo tamanho da resposta; o artigo manda testar os dois campos para otimizar (`references/docs/recursos/tipo-prompt.md`).
- O artigo descreve o "gpt-4o-mini" como opção de custo baixíssimo, e a voz como custo extra, pela Microsoft Azure (`references/docs/recursos/tipo-prompt.md`).
- O assistente responde nos Setores em que foi escolhido e só com o atendimento em **Aguardando**; o mesmo prompt pode ficar em mais de um Setor (`references/docs/recursos/tipo-prompt.md`).
- Cada recurso de IA aparece por uma condição própria da conta (se não aparecer, o caminho é o suporte), e o campo **Prompt OPEN.AI (ChatGPT)** existe "se disponível no seu plano" (`references/docs/recursos/pre-requisitos-ia.md`, `references/docs/recursos/aba-geral-em-setores-e-chatbot.md`).

Valores em dinheiro, preço de plano e limite de mensagens não estão documentados: não cite.

## Quando algo não funciona

| Sintoma | O que conferir | Artigo |
|---|---|---|
| Não aparece o menu **Prompts OPEN.AI** | Perfil Administrador (documentado). Se a pessoa já é Administradora, falar com o suporte: cada recurso de IA aparece por uma condição própria da conta, e as telas de IA que não fazem parte do plano deixam de aparecer | `references/docs/recursos/tipos-de-perfil.md`, `references/docs/recursos/pre-requisitos-ia.md`, `references/docs/recursos/atualizacoes-2026-11-12.md` |
| A IA não responde | A conversa está no Setor da IA? Está em **Aguardando**? O cliente escreveu depois de a conversa chegar ao Setor? O token está no card **OPEN.AI** (ou o card avisa chave da plataforma)? O card **Provedor de IA** está completo? O Setor tem dois motores? | `references/docs/recursos/tipo-prompt.md`, `references/docs/recursos/provedor-de-ia.md`, `references/docs/recursos/visao-geral-setores-e-chatbot.md` |
| A IA falha e não se sabe por quê | O menu **Erros do Sistema** (só o Administrador o vê) registra o motivo das falhas da IA, com o recurso e o atendimento, como "o provedor recusou a chave de acesso" | `references/docs/recursos/provedor-de-ia.md`, `references/docs/recursos/tipos-de-perfil.md` |
| A janela do prompt não salva | **Tokens** com 0 ("Use um número inteiro de 1 para cima.") ou **Setor para Atendimento Humano (Transbordo)** vazio ("Informe o setor") | `references/docs/recursos/tipo-prompt.md` |
| A lista do bloco GPT Assistant está vazia | Nenhum Setor tem assistente ligado | `references/docs/recursos/bloco-gpt-assistant-openai.md` |
| O comando não executa | A instrução está no fim do campo **Prompt** e o prompt foi salvo depois do **INSERIR NO PROMPT**? O texto de **Quando a IA deve fazer isso** descreve bem o momento? Bloco editado à mão difere da forma do artigo (`references/comandos-e-capacidades.md`, seção 3)? | `references/docs/recursos/comandos-gpt-assistant.md` |
| A IA não usa a Base de Conhecimento | A base está escolhida no campo **Base de conhecimento** e o prompt foi salvo? O **Título** dos itens usa as palavras do cliente? | `references/docs/recursos/base-de-conhecimento-do-gpt-assistant.md` |
| Transferiu e ninguém atende | Há atendentes no Setor de destino? (etapa 2, passo 4) | `references/docs/recursos/aguardando-x-atendendo.md` |
| Transferiu e a IA continua respondendo | O Setor de destino (ou o de transbordo) tem prompt? Nesse caso, a IA desse Setor continua respondendo | `references/docs/recursos/tipo-prompt.md`, `references/docs/recursos/comandos-gpt-assistant.md` |
| O assistente não responde no grupo | A mensagem **começa** com o gatilho, escrito igual ao do campo **Gatilho para Acionar em Grupos**? O contato do grupo tem prompt em **Prompt OPEN.AI (ChatGPT)** ou, sem ele, o atendimento do grupo está num Setor com prompt? | `references/docs/recursos/gpt-assistant-em-grupos.md` |

Problemas gerais do painel que não são de IA (conexão caiu, usuário sem acesso) são da skill `cmv-ajuda`.
