# Comandos GPT Assistant

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/comandos-gpt-assistant
- **Categoria:** Recursos
- **Menu:** Inteligência Artificial › GPT Assistant › Comandos GPT Assistant

---

🧩 Quer que a IA faça mais do que conversar — passar o atendimento para quem resolve, registrar a venda, marcar a visita, encerrar quando o assunto acabou? Os **Comandos da IA** são as ações que a IA executa no atendimento, e a janela **Comandos da IA**, dentro do prompt, escreve a instrução de cada uma já pronta, com os ids da sua empresa.

Nas palavras da janela: *"A IA só executa um comando se o prompt mandar."* Cada comando entra no texto do prompt como uma instrução: diz em que momento agir e qual bloco a IA inclui na resposta para a plataforma executar a ação.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Prompts OPEN.AI** e abra o prompt pelo ícone **Editar** do card, ou clique em **ADICIONAR PROMPT**.
>
> ➡️ Clique em **COMANDOS DA IA**.
>
> ➡️ Escolha o comando em **O que a IA deve fazer**, escreva o momento certo em **Quando a IA deve fazer isso** e preencha os campos do comando.
>
> ➡️ Confira a prévia e clique em **INSERIR NO PROMPT**.
>
> ➡️ Repita para cada comando e clique em **Salvar** na janela do prompt (**Adicionar**, no prompt novo).

## Como usar a janela Comandos da IA

Acesse o menu **Prompts OPEN.AI  ›  editar o prompt  ›  COMANDOS DA IA**

🔘 **O que a IA deve fazer:** o comando. São seis: **Registrar oportunidade no CRM**, **Marcar ou desmarcar na agenda**, **Transferir para um setor**, **Transferir para um operador**, **Marcar com uma tag** e **Encerrar o atendimento**.

🔘 **Quando a IA deve fazer isso:** a situação que dispara o comando, com as suas palavras. Nas palavras da tela: *"Escreva com suas palavras — vai direto para a instrução."* Por exemplo: *o cliente pedir para falar com o financeiro*. O campo já vem com uma sugestão própria de cada comando, como *o assunto for de outro setor ou o cliente pedir para falar com ele*, no **Transferir para um setor**.

🔘 **Prévia:** nas palavras da janela, *é isto que vai para o prompt*. Mostra a instrução pronta, com o bloco do comando e os ids da sua empresa já preenchidos.

🔘 **INSERIR NO PROMPT:** acrescenta a instrução no fim do campo **Prompt**, numa seção com o nome do comando, e avisa *"Instrução adicionada ao prompt"*. Dá para inserir vários comandos no mesmo prompt, um depois do outro. Nos comandos que pedem um Setor, uma pessoa ou uma tag, o botão só fica ativo depois dessa escolha.

⚠️ O comando inserido passa a valer depois que você clica em **Salvar** na janela do prompt.

## O que cada comando faz

### Transferir para um setor

🔘 **Setor:** o Setor de destino.

Passa o atendimento para o Setor escolhido. Se o Setor de destino também tiver um prompt, a IA desse Setor continua a conversa.

### Transferir para um operador

🔘 **Setor** e **Operador:** o Setor e a pessoa que vai atender.

Passa o atendimento para o Setor e já atribui a pessoa: o atendimento fica aberto com ela.

### Marcar com uma tag

🔘 **Tag:** a tag que a IA aplica.

Aplica a tag no atendimento quando a situação descrita em **Quando a IA deve fazer isso** acontece.

⚠️ Nas palavras da prévia: *"Aplica a tag no atendimento. No turno do bloco, o cliente não recebe mensagem."*

### Encerrar o atendimento

Fecha o atendimento quando o assunto terminou. Descreva o sinal de fim em **Quando a IA deve fazer isso**, como *o cliente agradecer e dizer que era só isso*.

### Registrar oportunidade no CRM

🔘 **Produto do catálogo (opcional):** o produto da oportunidade.

🔘 **Funil** e **Etapa:** onde a oportunidade nasce. As listas começam em **Funil padrão da empresa** e **Primeira etapa do funil**; a **Etapa** se escolhe depois do funil.

🔘 **Transferir depois de registrar:** **Não transferir** ou o Setor que recebe o atendimento depois do registro.

🔘 **Respostas a gravar:** o que a IA precisa saber do cliente antes de registrar, uma por linha — a quantidade, o nome, a cidade. Nas palavras da tela: *"As quatro primeiras vão para os campos livres da oportunidade; todas ficam no resumo."*

A IA conversa até ter as respostas e cria a oportunidade na etapa escolhida, ligada ao atendimento, com o valor e um resumo. As respostas ficam na descrição da oportunidade, uma por linha, e as quatro primeiras também nos campos livres.

⚠️ Nas palavras da janela: *"Sem transferir, o cliente não recebe resposta no turno em que a IA registra a oportunidade."* Para a IA registrar e responder na mesma mensagem, escolha um Setor em **Transferir depois de registrar**.

### Marcar ou desmarcar na agenda

🔘 **Tipo do compromisso:** **Reunião**, **Ligação**, **Visita**, **Lembrete** ou **Tarefa**.

🔘 **Duração (minutos):** nas palavras da tela, usada para conferir se o horário está livre antes de marcar.

🔘 **Ensinar a IA a cancelar o compromisso:** com a opção ligada, a instrução também traz o bloco para a IA desmarcar o compromisso quando o cliente pedir.

A IA combina o dia e a hora com o cliente e confirma com ele antes de marcar. Nas palavras da instrução, a data vai ao cliente como DD/MM/AAAA, e a IA nunca marca nada antes da data de hoje. Com o sim, cria o compromisso como uma tarefa do tipo escolhido, com a duração definida, ligada ao atendimento, e avisa a equipe numa nota interna da conversa. Se o horário já estiver ocupado, a instrução diz que *o sistema recusa e avisa o operador*.

Nas palavras da janela, a IA *grava o compromisso e põe no Google Calendar*. Sem o Google Calendar conectado, o compromisso fica só na plataforma.

## Como o comando fica no prompt

Cada **INSERIR NO PROMPT** acrescenta ao fim do prompt uma seção com o nome do comando, a frase *"Quando [o que você escreveu], responda incluindo o bloco abaixo:"*, o bloco do comando e as instruções para a IA. O bloco é o que a plataforma lê para executar a ação:  
- **Transferir para um setor:** `#{"queueId": "10"}` — o id do Setor.
- **Transferir para um operador:** `#{"queueId": "9", "userId": "18"}` — o id do Setor e o do usuário.
- **Marcar com uma tag:** `#{"tagId": "16"}` — o id da tag.
- **Encerrar o atendimento:** `#{"closeTicket": "1"}`.
- **Registrar oportunidade no CRM** e **Marcar ou desmarcar na agenda:** os blocos `oportunidade` e `agenda`, que a IA completa com o que ouviu do cliente — o valor, o resumo e as respostas; a data, a hora e o tipo.

Os números acima são exemplos: a janela **Comandos da IA** põe os ids da sua empresa. Por isso vale inserir pela janela em vez de digitar o bloco à mão.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Inseri um comando da IA e ele não foi executado. O que confiro?** A IA só executa um comando se o prompt mandar: confira se a instrução está no fim do campo **Prompt** e se o prompt foi salvo depois do **INSERIR NO PROMPT**. Confira também o texto de **Quando a IA deve fazer isso**: é por ele que a IA reconhece o momento de agir.
>
> **A IA marcou a tag e o cliente não recebeu resposta naquela mensagem. É normal?** É. Nas palavras da prévia do comando **Marcar com uma tag**, *"No turno do bloco, o cliente não recebe mensagem."*
>
> **Posso usar mais de um comando da IA no mesmo prompt?** Pode. Cada **INSERIR NO PROMPT** acrescenta uma seção nova no fim do prompt.
>
> **O cliente ficou sem resposta depois que a IA registrou a oportunidade. Por quê?** Sem um Setor em **Transferir depois de registrar**, o cliente não recebe resposta no turno em que a IA registra a oportunidade. Escolha um Setor para a IA registrar e responder na mesma mensagem.
>
> **A IA marca o compromisso na agenda sem perguntar ao cliente?** Não. A instrução do comando **Marcar ou desmarcar na agenda** manda a IA confirmar o dia e a hora com o cliente antes de marcar.
