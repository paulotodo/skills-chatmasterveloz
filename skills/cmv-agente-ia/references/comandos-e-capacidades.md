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
| [Base de Conhecimento] | `references/docs/recursos/base-de-conhecimento-do-gpt-assistant.md` | https://clihelper.chatmasterveloz.com/docs/base-de-conhecimento-do-gpt-assistant |
| [Provedor de IA] | `references/docs/recursos/provedor-de-ia.md` | https://clihelper.chatmasterveloz.com/docs/provedor-de-ia |
| [Assistente de IA] | `references/docs/recursos/assistente-de-ia.md` | https://clihelper.chatmasterveloz.com/docs/assistente-de-ia |
| [Atualização 15/10] | `references/docs/recursos/atualizacoes-2026-10-15.md` | https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-10-15 |
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
| **Agente OpenAi** | Usava um assistente configurado na plataforma da OpenAI. | Aparece **desativado** na janela do prompt e "não funciona mais"; a IA se cria com o tipo **Prompt**, "com as instruções escritas no próprio campo do prompt". | [GPT Assistant], [Tipo Prompt] |

Se a pessoa disser que tem ou quer um "Agente OpenAI", diga isso com a fonte e ofereça reescrever as instruções como prompt do tipo **Prompt**.

Não confunda com o menu **Assistente de IA**, que responde a perguntas da equipe sobre os dados da plataforma (atendimentos, contatos, tarefas e outros), só consulta e não atende cliente ([Assistente de IA]).

## 2. Campos da janela do prompt

Caminho: menu **Prompts OPEN.AI** › **Adicionar Prompt** ([Tipo Prompt]). O menu aparece só para o perfil **Administrador** ([Tipos de Perfil]). A janela grava com **Salvar** (**Adicionar**, no prompt novo) ([Comandos]).

| Campo | O que a documentação diz | Fonte |
|---|---|---|
| **Tipo** | **Prompt**. O tipo **Agente OpenAI** aparece desativado. | [Tipo Prompt] |
| **Nome** | Rótulo do assistente; também assina as respostas da IA na conversa. | [Tipo Prompt] |
| **Gatilho para Acionar em Grupos** | Palavra que chama o assistente num grupo de WhatsApp, no começo da mensagem. A tela orienta "Exemplo: #meubot \| Evite usar @". | [Tipo Prompt], [Grupos] |
| **Prompt** | Instruções, regras e direções: tom de voz e estilo, limites e restrições, objetivos, referências e formatos de resposta. | [Tipo Prompt] |
| **COMANDOS DA IA** | Botão que abre a janela que escreve a instrução de uma ação e a acrescenta no fim do campo **Prompt** (seção 4). | [Tipo Prompt], [Comandos] |
| **Modelo da IA** (antes **GPT Model**) | O modelo, pesando desempenho e custo. A primeira opção, **Modelo do provedor**, mostra entre parênteses o modelo que vale para a empresa. Com a OpenAI, a lista traz também os modelos da conta dona da chave, e o artigo sugere o "gpt-4o-mini". | [Tipo Prompt], [Provedor de IA] |
| **Setor para Atendimento Humano (Transbordo)** | Setor para onde o GPT Assistant transfere a conversa "quando solicitado um atendimento humano". Obrigatório: sem ele, a janela avisa "Informe o setor". | [Tipo Prompt] |
| **Mensagem de Transbordo** | Mensagem que o GPT envia "quando entende que deve transferir para um atendimento humano". Vazia, vai "Aguarde enquanto transfiro para um atendente...". | [Tipo Prompt] |
| **Base de conhecimento** | A base que o prompt consulta antes de responder, ou **Nenhuma** (seção 10). | [Tipo Prompt], [Base de Conhecimento] |
| **Voz** | Resposta por **Texto** ou por voz de uma IA. A voz tem custo extra, pela Microsoft Azure, e pede **Chave da API de Voz** e **Região de Voz**; com **Texto**, os dois ficam vazios. | [Tipo Prompt] |
| **Temperatura** | De 0 a 2. Mais alto, mais criativo; mais perto de 0, mais fiel ao prompt. A tela não aceita valor acima de 2. | [Tipo Prompt] |
| **Tokens** | Limite máximo de texto gerado na resposta; um token equivale em média a 3 ou 4 caracteres. Sugestão do artigo: entre 500 e 1000 para começar. Não aceita 0 ("Use um número inteiro de 1 para cima."), e o prompt não é salvo. | [Tipo Prompt] |
| **Máximo de mensagens no Histórico** | Quantas das últimas mensagens o assistente guarda para entender o contexto. Sugestão do artigo: entre 10 e 20. | [Tipo Prompt] |

Sobre custo, o artigo diz que **Tokens** e **Máximo de mensagens no Histórico** "impactam diretamente o custo", porque ele é calculado pelo que é processado (histórico mais a última pergunta) e pelo tamanho da resposta, e manda testar os dois campos para otimizar ([Tipo Prompt]). Repita isso; não transforme em regra de proporção.

Os valores que a skill recomenda para o caso comum estão em `references/configuracao-painel.md`, etapa 4.

## 3. Comandos

Os **Comandos da IA** são as ações que a IA executa no atendimento. Nas palavras da janela: "A IA só executa um comando se o prompt mandar." Cada comando entra no texto do prompt como uma instrução que diz em que momento agir e qual bloco a IA inclui na resposta para a plataforma executar a ação ([Comandos]). São seis:

| Comando (como na janela) | Campos | O que faz | Bloco que vai no prompt (ids de exemplo do artigo) |
|---|---|---|---|
| **Transferir para um setor** | **Setor** | Passa o atendimento para o Setor escolhido. Se o Setor de destino também tiver prompt, a IA desse Setor continua a conversa. | `#{"queueId": "10"}` |
| **Transferir para um operador** | **Setor** e **Operador** | Passa o atendimento para o Setor e já atribui a pessoa: o atendimento fica aberto com ela. | `#{"queueId": "9", "userId": "18"}` |
| **Marcar com uma tag** | **Tag** | Aplica a tag no atendimento. | `#{"tagId": "16"}` |
| **Encerrar o atendimento** | (nenhum além do momento) | Fecha o atendimento quando o assunto terminou. | `#{"closeTicket": "1"}` |
| **Registrar oportunidade no CRM** | **Produto do catálogo (opcional)**, **Funil**, **Etapa**, **Transferir depois de registrar**, **Respostas a gravar** | Cria a oportunidade na etapa escolhida, ligada ao atendimento, com o valor, um resumo e as respostas (as quatro primeiras também nos campos livres). | bloco `oportunidade`, que o artigo cita sem mostrar a forma (a observada está na seção 4) |
| **Marcar ou desmarcar na agenda** | **Tipo do compromisso**, **Duração (minutos)**, **Ensinar a IA a cancelar o compromisso** | Seção 4. | bloco `agenda`, que o artigo cita sem mostrar a forma (a observada está na seção 4) |

Os números são exemplos: a janela **COMANDOS DA IA** põe os ids da empresa, e o artigo recomenda inserir pela janela "em vez de digitar o bloco à mão" ([Comandos]). Por isso o prompt que esta skill entrega leva, no lugar de cada comando, um marcador com o que escolher na janela e o texto de **Quando a IA deve fazer isso** (`assets/modelo-prompt.md`).

Documentado sobre o uso ([Comandos]):

- Cada **INSERIR NO PROMPT** acrescenta ao fim do prompt uma seção com o nome do comando, a frase "Quando [o que você escreveu], responda incluindo o bloco abaixo:", o bloco e as instruções para a IA.
- Dá para usar vários comandos no mesmo prompt: cada inserção é uma seção nova no fim.
- O comando passa a valer depois do **Salvar** na janela do prompt.
- É pelo texto de **Quando a IA deve fazer isso** que a IA reconhece o momento de agir.
- O comando de remover tag (`removeTag`), que aparecia na versão anterior do artigo, não está mais documentado: não o use.

### Forma do código (precaução desta skill)

Nos blocos do artigo, a forma é sempre `#{"chave": "número"}`: `#` colado na chave de abertura, aspas retas, ID numérico entre aspas. O artigo não diz que o código é JSON nem o que acontece com outras formas (espaço depois do `#`, aspas curvas, ID sem aspas). Inserindo pela janela, a forma vem dela. Se a pessoa digitar ou editar um bloco à mão, a skill adota uma precaução, e deve apresentá-la como precaução: o código fica idêntico ao bloco do artigo. O `scripts/conferir_prompt.py` acusa o que difere dessa forma; sem terminal, confira código por código. Os blocos `agenda` e `oportunidade` ficam fora dessa conferência (seção 4).

### Turnos sem mensagem ao cliente

Documentado ([Comandos]):

- **Marcar com uma tag:** "Aplica a tag no atendimento. No turno do bloco, o cliente não recebe mensagem."
- **Registrar oportunidade no CRM:** "Sem transferir, o cliente não recebe resposta no turno em que a IA registra a oportunidade." Com um Setor em **Transferir depois de registrar**, a IA registra e responde na mesma mensagem.

Consequência prática (recomendação desta skill): não ponha na resposta da tag nenhuma pergunta de que a conversa dependa; prefira um momento da conversa em que o cliente pode ficar um turno sem resposta, e teste esse turno.

## 4. Janela "COMANDOS DA IA" e comando de agenda

Caminho: menu **Prompts OPEN.AI** › abrir o prompt pelo ícone **Editar** do card, ou **ADICIONAR PROMPT** › **COMANDOS DA IA** ([Comandos]).

- **O que a IA deve fazer:** o comando (os seis da seção 3).
- **Quando a IA deve fazer isso:** a situação que dispara o comando, com as palavras da empresa. Vem com uma sugestão própria de cada comando, como "o assunto for de outro setor ou o cliente pedir para falar com ele", no **Transferir para um setor**.
- **Prévia:** a instrução pronta, com o bloco e os ids da empresa.
- **INSERIR NO PROMPT:** acrescenta a instrução no fim do campo **Prompt** e avisa "Instrução adicionada ao prompt". Nos comandos que pedem Setor, pessoa ou tag, o botão só fica ativo depois dessa escolha.
- Depois, **Salvar** na janela do prompt (**Adicionar**, no prompt novo).

**Marcar ou desmarcar na agenda** ([Comandos]):

- **Tipo do compromisso:** **Reunião**, **Ligação**, **Visita**, **Lembrete** ou **Tarefa**. **Duração (minutos):** usada para conferir se o horário está livre antes de marcar. **Ensinar a IA a cancelar o compromisso:** ligada, a instrução traz também o bloco para desmarcar quando o cliente pedir.
- A IA combina o dia e a hora com o cliente e confirma com ele antes de marcar. A data vai ao cliente como DD/MM/AAAA, e a IA nunca marca nada antes da data de hoje.
- Com o sim, cria o compromisso como uma tarefa do tipo escolhido, com a duração definida, ligada ao atendimento, e avisa a equipe numa nota interna da conversa. Se o horário já estiver ocupado, a instrução diz que "o sistema recusa e avisa o operador".
- A IA "grava o compromisso e põe no Google Calendar"; sem o Google Calendar conectado, o compromisso fica só na plataforma.

Não documentado: a forma dos blocos `agenda` e `oportunidade` (o artigo só diz que "a IA completa com o que ouviu do cliente — o valor, o resumo e as respostas; a data, a hora e o tipo") e o texto exato das instruções que a janela insere. Nenhum artigo da Central mostra esses blocos (conferido em 21/11/2026 em toda a documentação, inclusive CRM, Consultório, Reservas e Links de agendamento).

**Forma observada, não oficial.** O que a janela inseriu num painel em 21/11/2026 (ids e nomes trocados aqui). Pode mudar com a versão da plataforma. Serve para explicar o que a seção faz e para reconhecer um bloco inteiro; não serve para escrever o bloco à mão, porque os ids vêm da conta e só a janela os põe.

A seção de agenda chega com o título **Marcar na agenda**, e a de oportunidade com **Registrar a oportunidade no CRM** (não com o nome do comando na janela):

```
#{"agenda": {"acao": "marcar", "titulo": "<assunto>", "data": "<AAAA-MM-DD>", "hora": "<HH:MM>", "duracao": 30, "tipo": "reuniao"}}
#{"agenda": {"acao": "desmarcar"}}
#{"oportunidade": {"productId": 7, "valor": "<valor combinado, ex: 1200,00>", "pipelineId": 5, "laneId": 9, "resumo": "<uma frase com o que o cliente quer>", "respostas": {"<pergunta>": "<resposta do cliente>"}}, "queueId": "6"}
```

- Os trechos entre `<` e `>` são para a IA completar na conversa. Não são marcadores para a pessoa trocar: ficam como a janela os pôs.
- Agenda: `duracao` e `tipo` vêm de **Duração (minutos)** e **Tipo do compromisso**. No bloco, a data vai como AAAA-MM-DD e a hora como HH:MM em 24 h; ao cliente, a data vai como DD/MM/AAAA. O bloco de desmarcar só vem com **Ensinar a IA a cancelar o compromisso** ligado.
- Agenda com horário ocupado: a instrução inserida diz à IA que "o sistema recusa e avisa o operador — você não recebe essa resposta" e manda oferecer outro horário se o cliente voltar ao assunto. Ou seja, a IA não fica sabendo da recusa no mesmo turno. O que o cliente recebe nesse turno não está na documentação; o que foi visto está no item de baixo.
- Visto numa conversa de teste em 22/11/2026 (um prompt só com esse comando, uma conversa): a IA confirmou data e hora, o cliente respondeu "sim" e a conversa ganhou a nota interna "📅 A IA marcou um compromisso: compromisso N marcado para AAAA-MM-DD HH:MM (na agenda do Google)". Na conversa vista no painel, o cliente não recebeu mensagem de confirmação depois do "sim". Três minutos depois, na mesma conversa, pediu o mesmo horário para outra pessoa e recebeu na hora "O horário de 10:00 já está ocupado. Que tal marcar para às 11:00?", sem nota interna de recusa. Essa resposta pode ter vindo do que a própria IA tinha marcado minutos antes.
- Recusa do sistema, vista em 22/11/2026 numa conversa nova (depois do **SAIR**), pedindo o mesmo dia e hora já ocupados: a IA não sabia do compromisso e pediu a confirmação normalmente. Com o "sim", nada foi marcado e a conversa ganhou uma nota interna em vermelho: "A IA tentou mexer na AGENDA e o sistema não conseguiu. Motivo: AAAA-MM-DD HH:MM já está ocupado na agenda (nome do compromisso) — nada foi marcado. ⚠️ O cliente pode ter sido informado de que estava agendado. Confira antes de encerrar." O cliente não recebeu nenhuma mensagem depois do "sim" (visto no painel e confirmado por quem testou, no WhatsApp). Na prática: o cliente fica achando que marcou, e só a equipe vê o aviso. Diga isso a quem for usar o comando de agenda, e escreva no prompt que a confirmação ao cliente não vale como agendamento garantido (por exemplo, a IA avisa que a equipe confirma em seguida). Uma conversa só, um prompt só com esse comando.
- Cancelamento, visto em 23/11/2026 (prompt de teste com os blocos de marcar e de desmarcar, uma conversa de cada caso, respostas limitadas a 100 tokens): o cliente pediu para cancelar a aula marcada minutos antes e recebeu "Aula experimental marcada para DD/MM às HH:MM cancelada com sucesso". Só que nada foi cancelado: a tarefa continuou **Pendente** em **Tarefas**, a conversa não ganhou nota interna e o evento continuou no Google Calendar. Não deu para saber se a IA deixou de mandar o bloco ou se o sistema não o executou. No teste do dia seguinte (item de baixo) o sistema executou o comando, mas em outro compromisso. Na prática: a resposta da IA ao cliente não prova o cancelamento. Diga isso a quem ligar **Ensinar a IA a cancelar o compromisso**, peça o teste de cancelamento conferido em **Tarefas** e sugira que o prompt mande a IA dizer que a equipe confirma o cancelamento.
- Cancelamento que atinge outro compromisso, visto em 24/11/2026 (mesmo prompt, conversa nova): o cliente marcou uma aula e, três minutos depois, pediu para cancelar "a aula que marquei". Não recebeu nenhuma mensagem, e a conversa ganhou a nota interna "📅 A IA marcou um compromisso: compromisso N ("título") cancelado" (a nota diz "marcou" mesmo no cancelamento). O compromisso cancelado foi outro, do mesmo contato e de meses antes, que passou a aparecer como **Concluída** em **Tarefas**; a aula recém-marcada continuou **Pendente**. O bloco de desmarcar não leva data nem identificador (`#{"agenda": {"acao": "desmarcar"}}`), então quem escolhe o compromisso é o sistema, e a regra dessa escolha não está documentada. Na prática: com mais de um compromisso ou tarefa em aberto no mesmo contato, o cancelamento pela IA pode atingir o errado, sem aviso ao cliente. Antes de ligar **Ensinar a IA a cancelar o compromisso**, avise disso; para quem tem clientes com mais de um compromisso, recomende deixar desligado e mandar o pedido de cancelamento para um atendente (comando **Transferir para um setor**). Uma conversa só.
- Mais três coisas vistas no mesmo teste de 23/11/2026. (1) Prompt que dizia que a IA "só marca" aulas: ao pedido de cancelamento, o atendimento foi para **Aguardando** no Setor de transbordo e o cliente ficou sem nenhuma mensagem; se a IA também cancela, o prompt precisa dizer que cancelar faz parte do trabalho dela. (2) Horário ocupado por um evento criado direto no Google Calendar: a IA respondeu duas vezes que o horário estava ocupado e não tentou marcar (nenhuma nota interna), e ofereceu como alternativa um horário que estava ocupado por outro compromisso. Não conte com a IA para dizer quais horários estão livres; se o sistema recusa horário ocupado só no Google Calendar ficou sem teste. (3) Recusa do sistema de novo, em conversa nova: o cliente aceitou o horário ocupado que a IA tinha oferecido, a IA mandou marcar sem nova confirmação, veio a mesma nota vermelha de recusa, o cliente ficou sem mensagem e o atendimento apareceu em **Aguardando** no Setor de transbordo. A marcação que dá certo não tira o atendimento da IA.
- Oportunidade: `productId`, `pipelineId` e `laneId` são números sem aspas, de **Produto do catálogo**, **Funil** e **Etapa**. O `queueId`, entre aspas e fora do objeto `oportunidade`, só aparece com um Setor em **Transferir depois de registrar**. As chaves de `respostas` são as perguntas de **Respostas a gravar**.
- Oportunidade sem os campos opcionais (visto na prévia da janela em 22/11/2026): sem **Produto do catálogo**, **Funil** e **Etapa**, o bloco vem sem `productId`, `pipelineId` e `laneId`. Sem Setor em **Transferir depois de registrar**, vem sem `queueId` e a instrução muda para "Responda APENAS com o bloco, sem texto junto: neste caso o cliente não recebe mensagem neste turno"; a própria janela avisa que, sem transferir, o cliente fica sem resposta no turno em que a IA registra a oportunidade. Para a IA registrar e responder na mesma mensagem, escolha um Setor.
- Oportunidade, instruções que vêm junto: escrever a mensagem ao cliente antes do bloco, que é removido antes do envio; usar o `productId` só se for esse o produto e nunca inventar um; se o produto for outro, usar `"produto": "<nome>"`.

Nunca escreva de cabeça esses blocos nem os corrija à mão. O que dizer à pessoa, e o que o `scripts/conferir_prompt.py` diz quando acha um deles (pelo nome no bloco, pelo nome do comando ou pelo título da seção): "insira pelo botão da janela COMANDOS DA IA e não edite o bloco à mão; a Central de Ajuda não mostra a forma dele". O script nunca acusa erro nesses dois blocos: compara com a forma observada e, se o bloco difere dela (aspas curvas, chave sem fechar), diz isso no mesmo aviso. Quem prova que funcionam é o teste do comando. O roteiro está em `references/configuracao-painel.md`, etapa 5; as duas variantes de agendamento, em `assets/modelo-prompt.md`.

O artigo não liga esse comando às agendas do **Consultório** nem das **Reservas**: o compromisso vira uma tarefa ([Comandos]). O Consultório tem outra via, a de um "atendente de IA que marca consultas pela conversa" por uma chave de API criada em **Consultório › Cadastros do consultório**, aba **Integrações** (Aba Integrações em Cadastros do Consultório, https://clihelper.chatmasterveloz.com/docs/aba-integracoes-em-cadastros-do-consultorio). É integração por API, com a `cmv-api`; a documentação não diz que o GPT Assistant usa essa chave.

## 5. Onde achar os IDs dos comandos

Pela janela **COMANDOS DA IA**, o Setor, o operador e a tag se escolhem pelo nome, e a janela põe os ids (seção 4). Os IDs só importam para conferir um bloco ou para quem edita à mão:

| ID | Onde aparece | Fonte |
|---|---|---|
| Tag (`tagId`) | Menu **Tags**: no lado direito de cada tag, o campo **ID** ("número ID da tag, utilizado para automações"). | [Visão Geral Tags] |
| Operador (`userId`) | Menu **Equipe**: o card de cada pessoa mostra o **ID**. | [Visão Geral Equipe] |
| Setor (`queueId`) | **Não documentado** em que tela do painel o ID do Setor aparece. O que existe: a janela **COMANDOS DA IA**, e o endpoint "API Listar Setores da Empresa", cujo artigo não mostra a resposta (`references/docs/api/api-listar-setores-da-empresa.md`; uso de API é da skill `cmv-api`). | [Comandos] |

## 6. Quando o assistente atua

Documentado:

- O assistente é ligado a um Setor: menu **Setores & Chatbot** › editar o Setor › aba **Geral** › campo **Prompt OPEN.AI (ChatGPT)**, "se disponível no seu plano". O card do Setor passa a mostrar o selo **Prompt GPT** ([Tipo Prompt], [Aba Geral do Setor]).
- "O GPT Assistant responde nos Setores em que foi escolhido, e somente quando o atendimento estiver em **Aguardando**. Com o atendimento aceito por alguém da equipe, ele fica calado; se o atendimento voltar para **Aguardando**, ele volta a responder. O mesmo prompt pode ficar em mais de um Setor." ([Tipo Prompt])
- O caminho recomendado para levar o cliente ao Setor é o bloco **GPT Assistant (OpenAI)** do FlowBuilder; o Setor também pode receber a conversa direto, pela Conexão ou por transferência ([Tipo Prompt], [GPT Assistant]).
- "O seu assistente começa a agir somente depois que o atendimento passa para o Setor do GPT." Mensagens enviadas antes da troca não são respondidas; quando o cliente escreve de novo, a IA lê também o que veio antes e pode responder a pergunta antiga junto com a nova. O artigo recomenda estimular o cliente a enviar uma mensagem depois da troca ([Tipo Prompt]).
- **Aguardando** é o atendimento sem atendente humano; um atendimento atendido por automação (chatbot, FlowBuilder, IA) continua em Aguardando. Quando alguém aceita, ele passa para **Atendendo**. Transferido para outro Setor sem ser aceito, continua em Aguardando ([Aguardando x Atendendo]).
- Quem tem a permissão **Pode responder sem aceitar** responde sem tirar o atendimento de Aguardando, e "o agente de IA do Setor continua atendendo" ([Atualização 15/10]).
- A resposta aparece assinada com o nome do prompt seguido de **(IA)** (sem repetir quando o nome já termina em IA) e com o selo **IA**. Quando o cliente escreve aos pedaços, a IA espera e responde uma vez só, ao pedido inteiro ([Tipo Prompt]).
- Para a conversa ficar com a equipe, o Setor de transbordo tem de ser um Setor **sem** prompt: se ele tiver prompt, inclusive o próprio Setor da IA, a IA desse Setor continua respondendo ([Tipo Prompt]). O mesmo vale para o comando **Transferir para um setor** ([Comandos]).
- Excluir um prompt em uso deixa os Setores dele sem IA; a janela de excluir avisa quais são ([Tipo Prompt]).
- A **Mensagem de saudação** do Setor (aba **Mensagens**) é o texto que o cliente recebe ao chegar ao Setor pela Conexão ([Aba Mensagens do Setor]).
- A tela aceita **FlowBuilder** e **Prompt GPT** no mesmo Setor sem avisar, mas o recomendado é um motor por Setor ([Visão Geral Setores], [Aba Geral do Setor]).

Recomendação desta skill (não é frase da documentação; apresente assim):

- **Dois Setores.** Um Setor para a IA e outro, sem prompt, para a equipe que recebe as transferências e o transbordo. É a aplicação direta do aviso acima.
- **Primeira mensagem do cliente.** O artigo não diz se a primeira mensagem de uma conversa que já nasce no Setor da IA (Conexão apontando só para ele) é respondida. Trate como ponto a observar no teste.

## 7. Transferência para humano: dois mecanismos

| Mecanismo | Como funciona | Fonte |
|---|---|---|
| **Transbordo** (campos da janela do prompt) | Quando o cliente pede para falar com uma pessoa, a IA envia a **Mensagem de Transbordo** e passa o atendimento para o Setor de **Setor para Atendimento Humano (Transbordo)**. | [Tipo Prompt] |
| **Comando** **Transferir para um setor** ou **Transferir para um operador** (inserido pela janela) | A instrução no prompt manda a IA incluir o bloco na situação descrita; a plataforma transfere. Permite Setores diferentes por assunto, ou um operador. | [Comandos] |

Não documentado: o que acontece quando os dois mecanismos valem para a mesma situação. Recomendação desta skill: preencher o transbordo com o Setor humano principal, inserir o comando para cada critério que precisa funcionar sempre (outro Setor, outro assunto), e testar um pedido de humano para ver qual mensagem chega e se a transferência acontece uma única vez.

## 8. Áudio e voz

- Com **Ativar Transcrição de Áudio** ligada no cadastro do Setor, o áudio do cliente é transcrito e a IA responde ao conteúdo dele, no WhatsApp, no WebChat e no Chat Externo ([Tipo Prompt], [Aba Geral do Setor]).
- Pode responder por voz de uma IA (**Francisca (Feminino)**, **Antonio (Masculino)** e outras), com custo extra pela Microsoft Azure e os campos **Chave da API de Voz** e **Região de Voz** ([Tipo Prompt]).

## 9. Grupos e FlowBuilder

**Grupos** ([Grupos]): o campo **Gatilho para Acionar em Grupos** do prompt guarda a palavra que chama a IA (a tela orienta "Exemplo: #meubot | Evite usar @"). Quem responde: o prompt escolhido no contato do grupo (menu **Contatos** › editar o grupo › **Prompt OPEN.AI (ChatGPT)**); sem ele, o prompt do Setor em que está o atendimento do grupo, que chega sem Setor e precisa ser transferido para um Setor com prompt. Com gatilho, a IA só responde à mensagem que **começa** com ele (exemplo: `#meubot quanto custa a entrega?`); com o gatilho vazio, o prompt do contato do grupo responde sem ser chamado. Pedido de pessoa no grupo: a IA envia a **Mensagem de Transbordo** e passa o atendimento ao Setor de transbordo. Antes de tudo isso, o grupo precisa entrar na plataforma: há até três travas de grupo, o **Bloquear Grupos** do cadastro da empresa (de quem administra a instância), o **Ignorar Mensagens de Grupos** e o **Bloquear Grupos** de cada Conexão; cada documentação cita duas, e nenhuma diz como as três se combinam (`references/configuracao-painel.md`, "Opcional: usar o assistente em um grupo").

**Bloco GPT Assistant (OpenAI)** do FlowBuilder ([Bloco]): não configura a IA; só leva a conversa ao **Setor com GPT Assistant** escolhido, e a lista mostra apenas Setores com assistente ligado. O campo **Sem resposta: seguir pela saída depois de (minutos)** cria a saída **Sem resposta**; vazio ou 0 desliga. Sem essa saída, a conversa fica com o assistente. O desenho do fluxo é da skill `cmv-flowbuilder`.

## 10. Base de conhecimento, provedor e o que a documentação não descreve

**Base de Conhecimento** ([Base de Conhecimento]): menu **Prompts OPEN.AI** › **BASE DE CONHECIMENTO** › **NOVA BASE**; cada informação é um item (**NOVO ITEM**, com **Título** e **Conteúdo**, ou **ENVIAR ARQUIVO**, que lê .pdf, .docx, .txt, .md ou .csv, um por vez; imagem não é lida). "O título pesa mais na busca que o conteúdo — use as palavras que o cliente usaria." A base se liga no campo **Base de conhecimento** do prompt; cada prompt consulta uma base, e a mesma base pode servir a vários prompts. Confira o texto extraído do arquivo antes de salvar: "o que estiver aqui é o que a IA vai afirmar ao cliente".

**Provedor de IA** ([Provedor de IA]): o card **Provedor de IA**, no menu **Integrações**, escolhe "qual serviço de IA responde os prompts de chat"; em **OpenAI**, vale a chave do card **OPEN.AI**. Fora da OpenAI, **Modelo** e **Chave de API do provedor** são obrigatórios, e a chave é uma só para todos os provedores. Quando a IA falha, o motivo fica no menu **Erros do Sistema**. O card aparece com a opção de plano **Provedores de IA** (`references/docs/revendedor/recursos/como-habilitar-provedores-de-ia.md`).

Não documentado. Diga "não documentado" e proponha um teste ou o suporte da plataforma. Não complete por dedução.

- **Variáveis dentro do prompt** (nome do cliente, data e hora, protocolo). O `{{name}}` está documentado para a Mensagem de saudação do Setor, não para o campo **Prompt**.
- **Consulta a sistemas externos** (estoque, pedido, agenda de terceiros). Quando for preciso, o caminho é fluxo (`cmv-flowbuilder`) ou API (`cmv-api`). A exceção documentada é o Google Calendar do comando de agenda (seção 4).
- **Como o cliente vê a mensagem que contém o bloco** e **mais de um bloco na mesma mensagem**.
- **Leitura de imagens, documentos e outros anexos enviados pelo cliente** (a Base de Conhecimento lê arquivos enviados pela empresa, não os do cliente).
- **Horário de funcionamento do assistente** e limite de tamanho do campo **Prompt**.
- **Preços.** Não há valores na documentação; só está dito que o consumo é cobrado pela OpenAI na conta dona da chave em uso. Os nomes das opções de plano que liberam cada recurso de IA estão documentados, nos artigos do revendedor (`references/configuracao-painel.md`, "O que libera cada recurso de IA").
- **Chave da plataforma e créditos:** se a chave da plataforma cobre a Avaliação pela IA e a transcrição automática do Setor, como ela se combina com um Provedor de IA que não seja a OpenAI, e por que o saldo do Copiloto aparece **Ilimitado** (as duas documentações explicam de forma diferente). Detalhe na mesma seção de `references/configuracao-painel.md`.
- Os pontos das seções 4 (forma dos blocos `agenda` e `oportunidade`), 5 (ID do Setor), 6 (primeira mensagem) e 7 (transbordo com comando).
