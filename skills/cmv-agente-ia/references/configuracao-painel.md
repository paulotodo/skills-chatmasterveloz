# Receita: colocar o GPT Assistant no ar pelo painel

Sequência que junta, na ordem de execução, o que está espalhado por vários artigos. Use-a para montar o passo a passo da entrega, pulando o que a pessoa já fez. Os nomes de menu, de campo e de botão que aparecem aqui foram conferidos nos artigos e podem ser usados sem reabri-los. Abra o artigo da etapa quando a pessoa perguntar algo que este resumo não cobre, quando a tela dela for diferente do descrito, ou para copiar o link da linha **Fonte** (o índice `references/docs/INDICE.md` traz o link de cada artigo).

O que é fato documentado, recomendação da skill ou ponto não documentado está explicado em `references/comandos-e-capacidades.md`; aqui fica o procedimento.

Quem executa: o perfil **Administrador**. Os menus **Prompts OPEN.AI**, **Setores & Chatbot**, **Conexões** e **Integrações** só aparecem para ele (`references/docs/recursos/tipos-de-perfil.md`).

## Etapa 1: pré-requisitos

Artigos: `references/docs/recursos/pre-requisitos-ia.md`, `references/docs/recursos/token-openai.md`.

1. Pedir ao suporte do Chat Master Veloz a ativação da opção **AI** (o artigo diz que esse passo é feito pela equipe da plataforma, no menu Configurações Planos).
2. Criar o token na OpenAI: em https://platform.openai.com, entrar, ir em Dashboard > API Keys, criar uma nova chave, dar um nome, copiar o token e guardar em local seguro.
3. No painel, menu **Integrações**, card **OPEN.AI**, colar a chave no campo **Token OpenAI**. O artigo Token OpenAI e a atualização de 10/11/2026 dizem "card **OPEN.AI**"; o artigo Pré-Requisitos IA chama o mesmo lugar de "seção **OPEN.AI**". Use "card" e, se a pessoa não achar, mencione o outro nome. Cada campo grava sozinho, sem botão Salvar; depois de gravado, o token aparece escondido, com o olho **Mostrar a chave** (`references/docs/recursos/atualizacoes-2026-11-10.md`). **Model OpenAI** e **Idioma OpenAI** ficam vazios para manter o padrão.

A chave é da empresa: é na conta dona dela que a OpenAI cobra o consumo, e ela dá acesso à parte financeira. Não peça a chave; se a pessoa colar no chat, recomende gerar outra.

A atualização de 11/11/2026 cita, no mesmo menu, o card **Provedor de IA**, com **Provedor** e **Chave de API do provedor**. Os artigos não explicam como ele se relaciona com o card **OPEN.AI**. Se a tela da pessoa for diferente do artigo, peça que descreva o que vê.

## Etapa 2: Setores

Artigos: `references/docs/recursos/aba-geral-em-setores-e-chatbot.md`, `references/docs/recursos/visao-geral-setores-e-chatbot.md`, `references/docs/recursos/aguardando-x-atendendo.md`.

A skill recomenda dois Setores, o da IA e o da equipe (por quê, e por que é recomendação e não exigência: `references/comandos-e-capacidades.md`, seção 6).

1. Menu **Setores & Chatbot** › **ADICIONAR SETOR** (ou o lápis de um Setor existente).
2. Preencher **Nome**, **Ordenação do BOT** e **Cor**, que são obrigatórios, e clicar em **Adicionar** (Setor novo) ou **Salvar** (Setor existente).
3. No card do Setor da IA, conferir os selos: ele não deve ter outro motor de automação (**FlowBuilder**, **Chatbot**). A tela aceita dois sem avisar, e aí fica difícil prever qual responde.
4. No Setor da equipe, conferir duas coisas: que não tem o selo **Prompt GPT** e que há atendentes nele. O artigo da aba Geral indica como próximo passo "Cadastrar quem atende este Setor, no menu **Equipe › editar o usuário**", e o artigo Aguardando x Atendendo avisa que o atendente só vê em Aguardando os atendimentos dos Setores em que tem permissão. Sem ninguém no Setor, a transferência da IA cai em uma fila que ninguém enxerga.

## Etapa 3: tags (se o prompt usa tag)

Artigo: `references/docs/recursos/visao-geral-tags.md`.

1. Menu **Tags** › **+ NOVA TAG** para criar a que faltar.
2. Anotar o **ID** que aparece no lado direito de cada tag.

## Etapa 4: criar o assistente

Artigos: `references/docs/recursos/tipo-prompt.md`, `references/docs/recursos/atualizacoes-2026-11-11.md`.

Menu **Prompts OPEN.AI** › **Adicionar Prompt**. A coluna "valor para o caso comum" é recomendação desta skill, sempre dentro do que o artigo permite; diga isso à pessoa e ajuste depois dos testes.

| Campo | O que o artigo diz | Valor para o caso comum e a razão |
|---|---|---|
| **Tipo** | **Prompt** (o tipo Agente OpenAI aparece desligado) | **Prompt** |
| **Nome** | Rótulo do assistente | Algo que identifique, como "Atendente IA - Recepção" |
| **Prompt** | Recebe as instruções | O texto entregue, colado inteiro |
| **Modelo da IA** (antes **GPT Model**) | Sugere o "gpt-4o-mini": qualidade e agilidade com custo baixíssimo | "gpt-4o-mini", por ser a sugestão do artigo. Se ele não aparecer na lista: a atualização de 11/11 diz que o campo traz primeiro a opção **Modelo do provedor**, com o nome do modelo do provedor escolhido, e não lista as demais opções. Peça à pessoa que diga quais opções aparecem, em vez de indicar um nome que pode não existir na tela dela |
| **Setor para Atendimento Humano (Transbordo)** | Setor para onde o GPT transfere quando solicitado um atendimento humano | O Setor da equipe |
| **Mensagem de Transbordo** | Mensagem enviada quando o GPT entende que deve transferir | Uma frase curta, igual em sentido à frase de transferência do prompt |
| **Voz** | **Texto** ou voz de uma IA (custo extra, Microsoft Azure) | **Texto**, com **Chave da API de Voz** e **Região da Voz** vazias |
| **Temperatura** | De 0 a 2; perto de 0, mais fiel ao prompt; "1" para interpretar áudios dos clientes | **1**. É o único número que o artigo dá, e ele o liga ao áudio, comum no WhatsApp. Se a empresa quase não recebe áudio e os testes mostrarem a IA alterando o texto exato dos comandos, baixe (por exemplo, 0,5) e repita os testes |
| **Tokens** | Limite máximo de texto gerado na resposta; entre 500 e 1000 para começar; não aceita 0 | **500**. O prompt pede mensagens curtas, e esse é o piso da faixa do artigo. Se alguma resposta vier cortada, suba |
| **Máximo de Mensagens no Histórico** | Últimas mensagens guardadas para o contexto; entre 10 e 20 | **20** quando há coleta de dados (a IA precisa lembrar o que o cliente disse no começo até a confirmação); **10** quando é só tirar dúvidas |
| **Gatilho para Grupo** | Só para uso em grupo | Vazio, salvo uso em grupo (fim deste arquivo) |

O artigo não cita o nome do botão que grava a janela do prompt: escreva "salve", sem inventar o rótulo.

## Etapa 5: trocar os marcadores de ID pela janela Comandos da IA

Artigo: `references/docs/recursos/atualizacoes-2026-11-11.md`, seção "Comandos da IA". O que está e o que não está documentado sobre a janela: `references/comandos-e-capacidades.md`, seções 4 e 5.

Ordem única: os marcadores de dados do negócio são preenchidos antes de colar; o prompt pode ir ao painel levando só marcadores de ID de comando (e o do comando de agenda), que se trocam lá, pela janela **Comandos da IA**; o `--final` roda na versão definitiva, que é a que a pessoa devolve depois do **Inserir no prompt** ou a que você monta quando ela informa os IDs, antes dos testes.

Use quando o prompt foi entregue com marcador no lugar de um ID (em especial o do Setor, cuja tela não está documentada) ou com o marcador do comando de agenda. Quem já tem o ID da tag (menu **Tags**) ou do operador (menu **Equipe**) pode simplesmente trocar o marcador pelo número.

Roteiro para passar à pessoa. Os passos 1 a 4 são documentados; os passos 5 e 6 supõem que a janela escreve um trecho visível dentro do campo **Prompt**, o que a atualização não descreve. Diga isso e peça: "se a sua tela for diferente, me diga o que apareceu".

1. Cole o prompt no campo **Prompt**, com os dados do negócio já preenchidos e ainda com os marcadores de ID de comando.
2. Na janela do prompt, abra a janela **Comandos da IA** (a atualização não diz onde fica o botão que a abre).
3. Escolha o comando (por exemplo, transferir para um Setor) e o item pelo nome: o Setor, a tag ou o operador. Enquanto faltar o item, o **Inserir no prompt** fica desabilitado e a prévia avisa o que falta.
4. Clique em **Inserir no prompt**.
5. Procure no texto do prompt o trecho que entrou e compare o código com a forma do artigo de comandos, por exemplo `#{"queueId": "12"}`.
6. Fique com uma só regra para cada ação:
   - **O código inserido tem a forma do artigo:** mantenha a regra que o painel inseriu e apague a linha equivalente que veio com marcador (a que começa com "Para transferir, você deve dizer exatamente esse texto"). A lista de situações em que transferir continua no prompt.
   - **O que entrou é diferente, ou você não achou nada novo no texto:** não altere o que o painel escreveu, apague a linha com marcador e cole aqui o que apareceu, para a revisão.
7. Repita para cada marcador de ID. No fim, não pode sobrar nenhum `[[` no texto.
8. Copie o texto final do campo **Prompt** e cole aqui, para a conferência final (`--final`) antes dos testes.

Alternativa mais simples para quem não quer editar: depois do passo 4, a pessoa cola de volta o trecho que o painel inseriu, e você devolve o prompt final com uma regra só.

## Etapa 6: ligar o assistente ao Setor

Artigos: `references/docs/recursos/tipo-prompt.md`, `references/docs/recursos/aba-geral-em-setores-e-chatbot.md`.

1. Menu **Setores & Chatbot** › editar o Setor da IA › aba **Geral**.
2. No campo **Prompt OPEN.AI (ChatGPT)**, escolher o assistente criado.
3. Clicar em **Salvar**. O card do Setor passa a mostrar o selo **Prompt GPT**.

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
| Fluxo do FlowBuilder | O bloco **GPT Assistant (OpenAI)** leva a conversa ao Setor com assistente. O desenho do fluxo é da skill `cmv-flowbuilder`. | `references/docs/recursos/bloco-gpt-assistant-openai.md` |

Recomendação desta skill ao mudar a Conexão: anotar antes quais Setores estavam marcados em **Setores & Tempos**, para poder voltar atrás, e fazer a troca em horário de pouco movimento.

## Opcional: usar o assistente em um grupo

Artigo: `references/docs/recursos/gpt-assistant-em-grupos.md`.

1. Menu **Prompts OPEN.AI**, ao criar ou editar o prompt, preencher **Gatilho para Grupo**, começando com `!` (exemplo do artigo: `!alfred`).
2. Em **Editar Contato do Grupo**, adicionar o Prompt ao grupo desejado.
3. Conferir que o grupo está com status "aguardando" e na fila a que o assistente está vinculado.
4. No grupo, chamar com o gatilho: `!alfred como você pode me ajudar?`

## Limites e custos: o que dá para afirmar

- O consumo é cobrado pela OpenAI, na conta dona da chave; tarifas e limites de uso são consultados na conta da OpenAI (`references/docs/recursos/token-openai.md`).
- **Tokens** e **Máximo de Mensagens no Histórico** "impactam diretamente o custo", que é calculado pelo que é processado (histórico mais a última pergunta) e pelo tamanho da resposta; o artigo manda testar os dois campos para otimizar (`references/docs/recursos/tipo-prompt.md`).
- O artigo descreve o "gpt-4o-mini" como opção de custo baixíssimo, e a voz como custo extra, pela Microsoft Azure (`references/docs/recursos/tipo-prompt.md`).
- Cada assistente funciona em um Setor e só com o atendimento em **Aguardando** (`references/docs/recursos/tipo-prompt.md`).
- A opção de IA é ativada pelo suporte, e o campo **Prompt OPEN.AI (ChatGPT)** existe "se disponível no seu plano" (`references/docs/recursos/pre-requisitos-ia.md`, `references/docs/recursos/aba-geral-em-setores-e-chatbot.md`).

Valores em dinheiro, preço de plano e limite de mensagens não estão documentados: não cite.

## Quando algo não funciona

| Sintoma | O que conferir | Artigo |
|---|---|---|
| Não aparece o menu **Prompts OPEN.AI** | Perfil Administrador (documentado). Causa provável, não documentada: a opção AI ainda não ativada pelo suporte; o artigo a lista como pré-requisito, mas não diz que ela controla a aparição do menu | `references/docs/recursos/tipos-de-perfil.md`, `references/docs/recursos/pre-requisitos-ia.md` |
| A IA não responde | A conversa está no Setor da IA? Está em **Aguardando**? O cliente escreveu depois de a conversa chegar ao Setor? O token está no menu **Integrações**? O Setor tem dois motores? | `references/docs/recursos/tipo-prompt.md`, `references/docs/recursos/visao-geral-setores-e-chatbot.md` |
| A IA falha e não se sabe por quê | A atualização de 11/11, na seção "IA pelo provedor escolhido", que trata da sugestão de resposta e do card **Provedor de IA**, diz: "Quando a IA falha, o motivo aparece em **Erros do Sistema**". A nota não diz se isso vale para o GPT Assistant; vale olhar a página (só o Administrador a vê), sem prometer que o erro estará lá | `references/docs/recursos/atualizacoes-2026-11-11.md`, `references/docs/recursos/tipos-de-perfil.md` |
| A janela do prompt não salva | **Tokens** com 0: "Use um número inteiro de 1 para cima." | `references/docs/recursos/atualizacoes-2026-11-11.md` |
| A lista do bloco GPT Assistant está vazia | Nenhum Setor tem assistente ligado | `references/docs/recursos/bloco-gpt-assistant-openai.md` |
| O comando não executa | Código igual ao do artigo, ID certo, regra "dizer exatamente esse texto" e regra de manter o código (`references/comandos-e-capacidades.md`, seção 3) | `references/docs/recursos/comandos-gpt-assistant.md` |
| Transferiu e ninguém atende | Há atendentes no Setor de destino? (etapa 2, passo 4) | `references/docs/recursos/aguardando-x-atendendo.md` |
| Transferiu e a IA continua respondendo | O Setor de destino tem o selo **Prompt GPT**? | `references/docs/recursos/visao-geral-setores-e-chatbot.md` |
| O assistente não responde no grupo | Gatilho com `!`, Prompt em **Editar Contato do Grupo**, status "aguardando", fila do assistente | `references/docs/recursos/gpt-assistant-em-grupos.md` |

Problemas gerais do painel que não são de IA (conexão caiu, usuário sem acesso) são da skill `cmv-ajuda`.
