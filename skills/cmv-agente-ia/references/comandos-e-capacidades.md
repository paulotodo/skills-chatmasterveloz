# GPT Assistant: comandos e capacidades documentados

Resumo fiel do que a documentação do Chat Master Veloz diz que o GPT Assistant faz. Cada item aponta o artigo de onde saiu. É aqui que ficam, completos, os avisos sobre a forma dos comandos, o turno da tag, os dois Setores e a janela **Comandos da IA**; os outros arquivos da skill só apontam para cá.

Três tipos de afirmação aparecem, sempre identificados:

- **Documentado:** está no artigo citado.
- **Recomendação ou inferência desta skill:** raciocínio a partir do que está documentado; apresente assim e confirme no teste.
- **Não documentado:** diga isso com essas palavras (seção 10).

Antes de afirmar algo ao usuário, abra o artigo citado e confira. Onde o artigo do recurso e uma atualização (`references/docs/recursos/atualizacoes-2026-*.md`) divergem, este arquivo traz as duas versões e trata a atualização como a mais recente.

## Artigos citados

| Sigla | Arquivo | Link (linha **Fonte**) |
|---|---|---|
| [GPT Assistant] | `references/docs/recursos/gpt-assistant.md` | https://clihelper.chatmasterveloz.com/docs/gpt-assistant |
| [Tipo Prompt] | `references/docs/recursos/tipo-prompt.md` | https://clihelper.chatmasterveloz.com/docs/tipo-prompt |
| [Comandos] | `references/docs/recursos/comandos-gpt-assistant.md` | https://clihelper.chatmasterveloz.com/docs/comandos-gpt-assistant |
| [Grupos] | `references/docs/recursos/gpt-assistant-em-grupos.md` | https://clihelper.chatmasterveloz.com/docs/gpt-assistant-em-grupos |
| [Bloco] | `references/docs/recursos/bloco-gpt-assistant-openai.md` | https://clihelper.chatmasterveloz.com/docs/bloco-gpt-assistant-openai |
| [Atualização 11/11] | `references/docs/recursos/atualizacoes-2026-11-11.md` | https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-11-11 |
| [Atualização 15/10] | `references/docs/recursos/atualizacoes-2026-10-15.md` | https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-10-15 |
| [Atualização 20/10] | `references/docs/recursos/atualizacoes-2026-10-20.md` | https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-10-20 |
| [Atualização 22/10] | `references/docs/recursos/atualizacoes-2026-10-22.md` | https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-10-22 |
| [Aba Geral do Setor] | `references/docs/recursos/aba-geral-em-setores-e-chatbot.md` | https://clihelper.chatmasterveloz.com/docs/aba-geral-em-setores-e-chatbot |
| [Aba Mensagens do Setor] | `references/docs/recursos/aba-mensagens-em-setores-e-chatbot.md` | https://clihelper.chatmasterveloz.com/docs/aba-mensagens-em-setores-e-chatbot |
| [Visão Geral Setores] | `references/docs/recursos/visao-geral-setores-e-chatbot.md` | https://clihelper.chatmasterveloz.com/docs/visao-geral-setores-e-chatbot |
| [Aguardando x Atendendo] | `references/docs/recursos/aguardando-x-atendendo.md` | https://clihelper.chatmasterveloz.com/docs/aguardando-x-atendendo |
| [Visão Geral Tags] | `references/docs/recursos/visao-geral-tags.md` | https://clihelper.chatmasterveloz.com/docs/visao-geral-tags |
| [Visão Geral Equipe] | `references/docs/recursos/visao-geral-equipe.md` | https://clihelper.chatmasterveloz.com/docs/visao-geral-equipe |
| [Tipos de Perfil] | `references/docs/recursos/tipos-de-perfil.md` | https://clihelper.chatmasterveloz.com/docs/tipos-de-perfil |

## 1. Tipos de assistente

| Tipo | O que é | Situação | Fonte |
|---|---|---|---|
| **Prompt** | O assistente é configurado direto na plataforma: as instruções vão no campo **Prompt**. | É o tipo a usar. Tudo nesta skill trata dele. | [GPT Assistant], [Tipo Prompt] |
| **Agente OpenAi** | Usa um assistente configurado na plataforma da OpenAI. | O artigo ainda o apresenta como opção. A atualização diz que ele aparece **desligado** na janela do prompt, que a OpenAI desligou esse tipo e que as instruções devem ir "no próprio campo do prompt". Não há artigo que ensine a configurá-lo. | [GPT Assistant], [Atualização 11/11] |

Se a pessoa disser que tem ou quer um "Agente OpenAI", diga as duas coisas com as fontes e ofereça reescrever as instruções como prompt do tipo **Prompt**.

Não confunda com o menu **Assistente de IA**, que responde a perguntas da equipe sobre atendimentos, contatos, oportunidades e tarefas, só consulta e não atende cliente ([Atualização 11/11]).

## 2. Campos da janela do prompt

Caminho: menu **Prompts OPEN.AI** › **Adicionar Prompt** ([Tipo Prompt]; esse artigo escreve "Prompts Open.Ai", os demais "Prompts OPEN.AI"). O menu aparece só para o perfil **Administrador** ([Tipos de Perfil]).

| Campo | O que a documentação diz | Fonte |
|---|---|---|
| **Tipo** | **Prompt**. O tipo **Agente OpenAI** aparece desligado. | [Tipo Prompt], [Atualização 11/11] |
| **Nome** | Rótulo do assistente. | [Tipo Prompt] |
| **Prompt** | Instruções, regras e direções: tom de voz e estilo, limites e restrições, objetivos, referências e formatos de resposta. | [Tipo Prompt] |
| **Modelo da IA** (antes **GPT Model**) | O modelo, pesando desempenho e custo; o artigo sugere o "gpt-4o-mini". A atualização diz que o campo traz primeiro a opção **Modelo do provedor**, com o nome do modelo do provedor escolhido. | [Tipo Prompt], [Atualização 11/11] |
| **Setor para Atendimento Humano (Transbordo)** | Setor para onde o GPT Assistant transfere a conversa "quando solicitado um atendimento humano". | [Tipo Prompt] |
| **Mensagem de Transbordo** | Mensagem que o GPT envia "quando entende que deve transferir para um atendimento humano". | [Tipo Prompt] |
| **Voz** | Resposta por **Texto** ou por voz de uma IA. A voz tem custo extra, pela Microsoft Azure, e pede **Chave da API de Voz** e **Região da Voz**; com **Texto**, os dois ficam vazios. | [Tipo Prompt] |
| **Temperatura** | De 0 a 2. Mais alto, mais criativo; mais perto de 0, mais fiel ao prompt. Observação do artigo: "1" para o agente interpretar corretamente áudios enviados pelos clientes. | [Tipo Prompt] |
| **Tokens** | Limite máximo de texto gerado na resposta; um token equivale em média a 3 ou 4 caracteres. Sugestão do artigo: entre 500 e 1000 para começar. O campo começa em 1 e não aceita 0 ("Use um número inteiro de 1 para cima."). | [Tipo Prompt], [Atualização 11/11] |
| **Máximo de Mensagens no Histórico** | Quantas das últimas mensagens o assistente guarda para entender o contexto. Sugestão do artigo: entre 10 e 20. | [Tipo Prompt] |
| **Gatilho para Grupo** | Palavra que chama o assistente em um grupo; começa com `!`. | [Grupos] |

Sobre custo, o artigo diz que **Tokens** e **Máximo de Mensagens no Histórico** "impactam diretamente o custo", porque ele é calculado pelo que é processado (histórico mais a última pergunta) e pelo tamanho da resposta, e manda testar os dois campos para otimizar ([Tipo Prompt]). Repita isso; não transforme em regra de proporção.

Os valores que a skill recomenda para o caso comum estão em `references/configuracao-painel.md`, etapa 4.

## 3. Comandos

Os comandos ativam ações da plataforma a partir do texto que a IA diz ([Comandos]). São cinco no artigo:

| Ação | Código | Exemplo de instrução dado pelo artigo |
|---|---|---|
| Transferir Fila (Setor) | `#{"queueId": "544"}` | Se a pessoa quiser sobre suporte técnico ou qualquer tema relacionado a suporte, você deve dizer exatamente esse texto: Transferindo para o `#{"queueId": "544"}` setor de Suporte. |
| Transferir para Operador | `#{"queueId": "544", "userId":"3"}` | Se a pessoa disser "quero falar com o João", você deve dizer exatamente esse texto: Transferindo para o `#{"queueId": "544", "userId":"3"}` João. |
| Atribuir Tag | `#{"tagId": "71"}` | Se a pessoa disser "gostaria de saber sobre notebook", ou qualquer tema relacionado ao interesse em notebook, você deve dizer exatamente esse texto: Legal, temos diversas opções de `#{"tagId": "71"}` Notebook. |
| Remover Tag | `#{"removeTag": "71"}` | Se a pessoa disser "pode cancelar minha consulta", ou algo que demonstre o interesse em cancelar um agendamento, você deve dizer exatamente esse texto: ok, sua consulta foi `#{"removeTag": "71"}` cancelada. |
| Encerrar Ticket | `#{"closeTicket": "1"}` | Se você entender que todas as pendências foram finalizadas, que não há dúvidas, e que o cliente não deseja mais conversar, você deve dizer exatamente esse texto: Estou encerrando nosso `#{"closeTicket": "1"}` ticket agora, mas fico a disposição se precisar de algo no futuro. |

Os números `544`, `3` e `71` são exemplos do artigo: troque pelos IDs da empresa (seção 5).

Documentado sobre o uso:

- O padrão é uma regra no prompt do tipo "se [situação], você deve dizer exatamente esse texto: [frase com o código dentro]".
- Dica do artigo: escrever no prompt uma recomendação para a IA **manter o código no texto enviado**.

### Forma do código (precaução desta skill)

Nos blocos de código do artigo, a forma é sempre `#{"chave": "número"}`: `#` colado na chave de abertura, aspas retas, ID numérico entre aspas. Nos exemplos em prosa do mesmo artigo as aspas saem curvas (“ ”), efeito da formatação do site. O artigo não diz que o código é JSON nem o que acontece com outras formas (espaço depois do `#`, aspas curvas, ID sem aspas). Por isso a skill adota uma precaução, e deve apresentá-la como precaução: o código vai no prompt idêntico ao bloco de código do artigo. O `scripts/conferir_prompt.py` acusa o que difere dessa forma; sem terminal, confira código por código.

### Turno da tag (ponto em aberto)

O artigo de comandos mostra a tag dentro de uma frase dita ao cliente. A atualização de 11/11 diz, sobre os comandos da IA: "A tag é aplicada à conversa, e o cliente não recebe mensagem naquele turno" e "A transferência para outro Setor não envia texto interno ao cliente" ([Atualização 11/11]). A documentação não concilia as duas coisas. Consequências práticas:

- Todo plano de testes inclui o turno da tag: a tag apareceu na conversa? O cliente recebeu a frase?
- Se o cliente ficar sem a mensagem, tire da frase da tag qualquer pergunta de que a conversa dependa e reescreva o roteiro para a IA fazer essa pergunta na resposta seguinte.

## 4. Janela "Comandos da IA" e comando de agenda

Documentado ([Atualização 11/11], seção "Comandos da IA"):

- Existe, na janela do prompt, a janela **Comandos da IA**.
- Ela tem o texto **Quando a IA deve fazer isso**, que muda conforme o comando (exemplo citado: "o cliente quiser marcar um horário e já tiver confirmado o dia e a hora"), uma prévia e o botão **Inserir no prompt**.
- Sem a tag, o Setor ou o operador escolhido, o **Inserir no prompt** fica desabilitado, e a prévia avisa o que falta.
- Há um **comando de agenda**, com **Tipo do compromisso** (**Reunião**, **Ligação**, **Visita**, **Lembrete** ou **Tarefa**) e **Duração (minutos)**.
- "A agenda marca o compromisso a partir da data de hoje, nunca antes dela, e escreve a data para o cliente como dia/mês/ano."

Não documentado:

- onde fica o botão que abre a janela;
- o texto que ela insere, em que ponto do prompt o insere e se o código inserido tem a mesma forma do artigo de comandos;
- a sintaxe do comando de agenda;
- se a agenda consulta horários livres, o que faz quando dois clientes pedem o mesmo horário, onde o compromisso aparece e quem é avisado.

O que fazer com isso: o roteiro executável, que não depende de adivinhar a tela, está em `references/configuracao-painel.md`, etapa 5. Para agendamento, as duas variantes de roteiro estão em `assets/modelo-prompt.md`. Nunca escreva de cabeça o comando de agenda.

## 5. Onde achar os IDs dos comandos

| ID | Onde aparece | Fonte |
|---|---|---|
| Tag (`tagId`, `removeTag`) | Menu **Tags**: no lado direito de cada tag, o campo **ID** ("número ID da tag, utilizado para automações"). | [Visão Geral Tags] |
| Operador (`userId`) | Menu **Equipe**: o card de cada pessoa mostra o **ID**. | [Visão Geral Equipe] |
| Setor (`queueId`) | **Não documentado** em que tela do painel o ID do Setor aparece. O que existe: a janela **Comandos da IA**, em que se escolhe o Setor pelo nome (seção 4), e o endpoint "API Listar Setores da Empresa", cujo artigo não mostra a resposta (`references/docs/api/api-listar-setores-da-empresa.md`; uso de API é da skill `cmv-api`). | [Atualização 11/11] |

## 6. Quando o assistente atua

Documentado:

- O assistente é ligado a um Setor: menu **Setores & Chatbot** › editar o Setor › aba **Geral** › campo **Prompt OPEN.AI (ChatGPT)**, "se disponível no seu plano" ([Tipo Prompt], [Aba Geral do Setor]).
- "Cada GPT Assistant funciona em **um Setor** e somente quando o atendimento estiver em **Aguardando**" ([Tipo Prompt]).
- "O seu assistente começa a agir somente depois que o atendimento passa para o Setor do GPT." Mensagens enviadas antes da troca para o Setor do GPT não são respondidas, e o artigo recomenda estimular o cliente a enviar uma mensagem depois da troca ([Tipo Prompt]).
- **Aguardando** é o atendimento sem atendente humano; um atendimento atendido por automação (chatbot, FlowBuilder, IA) continua em Aguardando. Quando alguém aceita, ele passa para **Atendendo**. Transferido para outro Setor sem ser aceito, continua em Aguardando ([Aguardando x Atendendo]).
- Quem tem a permissão **Pode responder sem aceitar** responde sem tirar o atendimento de Aguardando, e "o agente de IA do Setor continua atendendo" ([Atualização 15/10]).
- A **Mensagem de saudação** do Setor (aba **Mensagens**) é o texto que o cliente recebe ao chegar ao Setor pela Conexão ([Aba Mensagens do Setor]).
- A tela aceita **FlowBuilder** e **Prompt GPT** no mesmo Setor sem avisar, mas o recomendado é um motor por Setor ([Visão Geral Setores], [Aba Geral do Setor]).
- Duas notas falam de identificação das respostas na conversa, sem dizer a qual recurso se referem: "Assistente de IA: as respostas vêm com o nome do assistente e um selo." ([Atualização 20/10]) e "Selo IA: na conversa, as respostas dos robôs integrados aparecem com o selo IA." ([Atualização 22/10]). Cite as frases; não afirme que valem para o GPT Assistant.

Recomendações e inferências desta skill (não são frases da documentação; apresente assim):

- **Dois Setores.** Recomendação: um Setor para a IA e outro, sem assistente ligado, para a equipe que recebe as transferências. Motivo: como o assistente atua no Setor dele em Aguardando, uma conversa transferida para um Setor com assistente ficaria, por inferência, sujeita à IA de novo. A documentação não exige dois Setores.
- **A IA para quando alguém aceita a conversa.** Inferência a partir de dois artigos: o assistente só atua em Aguardando ([Tipo Prompt]) e aceitar leva o atendimento para Atendendo ([Aguardando x Atendendo]). Nenhum artigo diz isso com essas palavras; confirme no teste.
- **Primeira mensagem do cliente.** O artigo não diz se a primeira mensagem de uma conversa que já nasce no Setor da IA (Conexão apontando só para ele) é respondida. Trate como ponto a observar no teste.

## 7. Transferência para humano: dois mecanismos

| Mecanismo | Como funciona | Fonte |
|---|---|---|
| **Transbordo** (campos da janela do prompt) | Escolhe-se um Setor e uma mensagem; o GPT transfere "quando solicitado um atendimento humano" e envia a mensagem "quando entende que deve transferir". | [Tipo Prompt] |
| **Comando** Transferir Fila ou Transferir para Operador (dentro do prompt) | Uma regra no prompt manda a IA dizer um texto exato com o código; a plataforma transfere. Permite Setores diferentes por assunto, ou um operador. | [Comandos] |

Não documentado: como o texto do prompt influencia a decisão do transbordo e o que acontece quando os dois mecanismos valem para a mesma situação. Recomendação desta skill: preencher o transbordo com o Setor humano principal, escrever a regra com o comando para cada critério que precisa funcionar sempre, e testar um pedido de humano para ver qual mensagem chega e se a transferência acontece uma única vez.

## 8. Áudio e voz

- Para o agente "interpretar corretamente áudios enviados pelos clientes", o artigo manda usar **Temperatura** "1" ([Tipo Prompt]).
- Pode responder por voz de uma IA, com custo extra pela Microsoft Azure e os campos **Chave da API de Voz** e **Região da Voz** ([Tipo Prompt]).

## 9. Grupos e FlowBuilder

**Grupos** ([Grupos]): define-se o **Gatilho para Grupo** no prompt (começa com `!`; exemplo do artigo: `!alfred`); o grupo precisa estar com status "aguardando" e na fila a que o assistente está vinculado; e é preciso adicionar o Prompt em **Editar Contato do Grupo**. No grupo, chama-se com o gatilho: `!alfred como você pode me ajudar?`.

**Bloco GPT Assistant (OpenAI)** do FlowBuilder ([Bloco]): não configura a IA; só leva a conversa ao **Setor com GPT Assistant** escolhido, e a lista mostra apenas Setores com assistente ligado. O campo **Sem resposta: seguir pela saída depois de (minutos)** cria a saída **Sem resposta**; vazio ou 0 desliga. Sem essa saída, a conversa fica com o assistente. O desenho do fluxo é da skill `cmv-flowbuilder`.

## 10. O que a documentação não descreve

Diga "não documentado" e proponha um teste ou o suporte da plataforma. Não complete por dedução.

- **Variáveis dentro do prompt** (nome do cliente, data e hora, protocolo). O `{{name}}` está documentado para a Mensagem de saudação do Setor, não para o campo **Prompt**.
- **Base de conhecimento por arquivo, site ou planilha.** O que o assistente sabe é o que está escrito no campo **Prompt**.
- **Consulta a sistemas externos** (estoque, pedido, agenda de terceiros). Quando for preciso, o caminho é fluxo (`cmv-flowbuilder`) ou API (`cmv-api`).
- **Como o cliente vê a mensagem que contém o código** e **mais de um código na mesma mensagem**.
- **Leitura de imagens, documentos e outros anexos.**
- **Horário de funcionamento do assistente** e limite de tamanho do campo **Prompt**.
- **Quais provedores** existem no card **Provedor de IA** e se o GPT Assistant usa o provedor escolhido (a atualização afirma isso para a sugestão de resposta e descreve a opção **Modelo do provedor** no campo **Modelo da IA**).
- **Preços e planos.** Só está dito que há recursos que dependem do plano e que o consumo é cobrado pela OpenAI na conta dona da chave.
- Os pontos das seções 4 (janela e agenda), 5 (ID do Setor), 6 (primeira mensagem) e 7 (transbordo com comando).
