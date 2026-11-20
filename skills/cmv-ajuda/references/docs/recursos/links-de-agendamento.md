# Links de Agendamento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/links-de-agendamento
- **Categoria:** Recursos
- **Menu:** Links de Agendamento

---

🧩 Quantas mensagens a sua equipe troca com o cliente só para achar um horário de reunião? "Pode às 10h?", "Às 10h não, só depois do almoço", e a reunião que levaria um minuto para marcar vira um dia de conversa.

Os **Links de agendamento** criam uma página em que o cliente marca a reunião sozinho, nos horários livres de quem atende. Cada link é um tipo de reunião, como a apresentação de 30 minutos ou a consultoria de 1 hora, e a reunião marcada entra nas **Tarefas** de quem atende, com o link da videochamada.

Nas palavras da tela: *"A página mostra só o que está livre, nunca o que ocupa a agenda."*

Ideal para:

☑️ **Reunião de apresentação:** o cliente que pediu uma demonstração escolhe o dia e a hora pelo link, sem esperar resposta.

☑️ **Agenda no site:** a página de agendamento aparece dentro do site da empresa, pelo código para o site.

☑️ **Equipe que divide a agenda:** com mais de uma pessoa em **Quem atende**, a reunião fica com a primeira livre naquele horário.

☑️ **Lembrete da reunião:** o cliente recebe pelo WhatsApp a confirmação ao marcar, o lembrete antes da reunião e a mensagem de depois, sem ninguém digitar.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Links de agendamento** e clique em **Novo link**.
>
> ➡️ Preencha o **Nome** e a **Duração (min)**, escolha **Quem atende** e monte os **Dias e horários de atendimento**.
>
> ➡️ Em **Avisos e automações**, escolha os avisos ao cliente e o Setor e as tags da conversa dele.
>
> ➡️ Clique em **Salvar** e, na lista, em **Copiar o link**, para mandar ao cliente.

## Como criar um link de agendamento

Acesse o menu **Links de agendamento**, clique em **Novo link** e preencha:

🔘 **Nome:** como o cliente vê o link, como *Reunião de apresentação*. Até 120 caracteres.

🔘 **Ativo (a página aceita marcação):** ligado, a página recebe marcações. Desligado, o link fica **Pausado**.

🔘 **Descrição:** o texto que aparece na página, acima dos horários. Até 2.000 caracteres.

🔘 **Duração (min):** quanto tempo dura cada reunião, de 5 a 480 minutos.

🔘 **Folga entre reuniões (min):** de 0 a 240 minutos. Nas palavras da tela, *"Livre antes e depois de cada compromisso."*

🔘 **Antecedência mínima (min):** de 0 a 43.200 minutos (30 dias). Nas palavras da tela, *"O cliente não marca em cima da hora."* Com 30 minutos de antecedência e reuniões de 30 minutos, quem abre a página às 9h14 vê o primeiro horário às 10:00.

🔘 **Até quantos dias à frente:** de 1 a 365 dias. Nas palavras da tela, *"Depois disso a página não oferece horário."*

🔘 **Quem atende:** as pessoas da equipe que recebem a reunião. Nas palavras da tela, *"Com mais de um, a reunião fica com o primeiro livre naquele horário."*

🔘 **O que ocupa o horário:** os tipos de tarefa que tiram o horário da página — **Reunião**, **Ligação**, **Visita**, **Tarefa**, **Lembrete** e **E-mail**. Nas palavras da tela, *"As tarefas destes tipos, com hora marcada, tiram o horário da página."*

🔘 **Dias e horários de atendimento:** de segunda a domingo, a **Hora Inicial** e a **Hora Final** de cada dia. Nas palavras da tela, *"Dia em branco: não oferece horário. A página divide cada faixa pela duração."* Com reuniões de 30 minutos e a segunda das 09:00 às 18:00, a página oferece 09:00, 09:30, 10:00 e assim por diante, até 17:30.

O **Salvar** só libera com o **Nome**, ao menos uma pessoa em **Quem atende** e a **Duração** de 5 minutos ou mais. Ao salvar, a tela avisa *"Link salvo."*

## Avisos e automações do link de agendamento

Na janela do link, depois dos **Dias e horários de atendimento**, a seção **Avisos e automações** diz o que acontece quando o cliente marca a reunião: os avisos que ele recebe pelo WhatsApp e o Setor e as tags que a conversa dele ganha.

🔘 **Conexão dos avisos:** por onde os avisos são enviados. Nas palavras da tela, *"Vazia: a conversa do cliente, ou a conexão padrão."* A lista traz só as conexões de WhatsApp: os avisos ao cliente são enviados pelo WhatsApp. Vazia, os avisos vão pela conversa de WhatsApp do cliente, mesmo quando ele tem um atendimento mais novo por outro canal.

🔘 **Setor da conversa:** o Setor da conversa do cliente. Nas palavras da tela, *"A resposta do cliente cai neste setor. Não tira a conversa de quem já a atende."* **Sem setor** deixa a conversa como está.

🔘 **Tags da conversa:** as tags postas na conversa do cliente quando ele marca.

🔘 **Oportunidade no CRM:** aparece quando o **CRM** faz parte do seu plano. Escolhido um funil, a marcação cria a oportunidade nele, na **Etapa** escolhida, com o cliente e quem atende, e a reunião vira uma atividade da oportunidade. **Não criar oportunidade** deixa a marcação sem oportunidade.

🔘 **Avisos ao cliente:** as mensagens que o cliente recebe pelo WhatsApp. **Adicionar aviso** cria um aviso, até 10 por link de agendamento. Sem nenhum, a tela avisa *"Nenhum aviso. O cliente só vê a confirmação na página."*

Cada aviso ao cliente tem três partes:

➡️ **Quando:** **Ao marcar**, **Antes da reunião**, **No dia, a uma hora** ou **Depois da reunião**.

➡️ **Quanto antes** ou **Quanto depois do fim:** o tempo, em minutos, horas ou dias, de 5 minutos a 30 dias. No aviso **No dia, a uma hora**, o lugar do tempo é a **Hora** do aviso.

➡️ **Texto:** a mensagem, até 2.000 caracteres, com as variáveis da reunião — `{{cliente}}`, `{{tarefa}}`, `{{data}}`, `{{hora}}`, `{{quando}}`, `{{responsavel}}` e `{{link}}`, o link da videochamada — e as da conversa, `{{ms}}` e `{{firstName}}`. Por exemplo, *"{{ms}}, {{cliente}}! Lembrete: {{tarefa}} começa {{quando}}."*

Quando o **Texto** do aviso não tem `{{link}}`, o link da videochamada entra sozinho, numa linha nova no fim da mensagem.

Quando a reunião é remarcada na tarefa, os avisos **Antes da reunião**, **No dia, a uma hora** e **Depois da reunião** acompanham o horário novo.

## Os links da lista

Cada link aparece na lista com o nome, a duração e a situação, **Ativo** ou **Pausado**, como *Reunião de apresentação · 30 min · Ativo*.

🔘 **Copiar o link:** copia o endereço da página, para mandar ao cliente pela conversa ou pôr nas redes da empresa. A tela avisa *"Link copiado."*

🔘 **Copiar o código para o site:** copia um código pronto, um *iframe*, que mostra a página de agendamento dentro do site da empresa. A tela avisa *"Código copiado. Cole no site onde a agenda deve aparecer."*

🔘 **Editar link:** abre o link para trocar qualquer campo, inclusive o **Ativo**.

🔘 **Remover link:** nas palavras da tela, *"O endereço deixa de funcionar. As reuniões já marcadas continuam na agenda."*

Para parar de receber marcações sem perder o link, desligue **Ativo (a página aceita marcação)**: a lista mostra **Pausado**, e quem abre o link lê *"Este link de agendamento não existe ou está pausado."*

## O que o cliente vê

A página do link de agendamento abre sem login, com o nome da empresa, o nome do link, a duração, como *30 minutos · videochamada*, e a **Descrição**.

➡️ **Escolha o dia:** os dias com horário, com os botões **Mais dias** e **Dias anteriores**.

➡️ **Escolha o horário:** só os horários livres de quem atende, já com a **Antecedência mínima** contada.

➡️ **Os dados:** **Seu nome**, **WhatsApp (com DDD)**, **E-mail (opcional)** e **Quer adiantar algo? (opcional)**.

➡️ **Marcar:** o botão traz o dia e a hora, como *Marcar 16/11/2026 às 10:00*, e só libera com o nome e o WhatsApp com DDD.

Depois de marcar, a página mostra *"Reunião marcada!"*, o dia e a hora e o **Link da videochamada**, com o recado *"Guarde este link: é por ele que você entra na reunião, no dia e na hora marcados."* O horário marcado some da página para os próximos clientes. Se outra pessoa pega o horário antes, a página avisa *"Este horário acabou de ser ocupado. Escolha outro."*

Antes da hora, o link da videochamada abre uma página que diz quando a reunião começa e quantos minutos antes o link abre.

## Onde a reunião marcada aparece

A reunião marcada pelo link de agendamento vira uma tarefa do tipo **Reunião** de quem atende, no menu **Tarefas**. O título junta o nome do link e o nome do cliente, como *Reunião de apresentação · Maria*. A tarefa traz o dia e a hora da reunião, o link da videochamada e, na descrição, o nome e o telefone do cliente e o que ele escreveu em **Quer adiantar algo?**.

Quando o WhatsApp informado na página já é de um contato, a tarefa da reunião fica ligada a esse contato. Se esse contato tinha só o número como nome, ele passa a ter o nome digitado em **Seu nome**, e os avisos chamam o cliente por esse nome.

Com a seção **Avisos e automações** preenchida, a marcação também faz o que o link pede: a conversa do cliente ganha o Setor e as tags escolhidos, sem tirar a conversa de quem já a atende, e os avisos são enviados nos momentos escolhidos. Sem nenhum aviso, nenhuma mensagem é enviada ao cliente: o link da videochamada é o que ele vê na tela de confirmação.

## Webhook do agendamento

O bloco **Webhook do agendamento** fica na mesma tela, abaixo dos links, com o botão **Salvar**. É um endereço só, para todos os links da empresa. Nas palavras da tela: *"Recebe link-criado, link-alterado, link-removido e agendamento-criado (o cliente marcou), assinados com o token da empresa."*

O endereço precisa ser um endereço `http://` ou `https://` válido. Fora disso, a tela avisa *"Use um endereço http(s):// válido para o webhook."*

## Quando o Salvar é recusado

➡️ *"A duração vai de 5 a 480 minutos."*

➡️ *"A folga vai de 0 a 240 minutos."*

➡️ *"A antecedência vai de 0 a 43200 minutos (30 dias)."*

➡️ *"O horizonte vai de 1 a 365 dias."*

➡️ *"Uma faixa de horário termina antes de começar."* — na grade, o próprio dia avisa *"O fim vem antes do início"*.

➡️ *"Cada link pode ter até 10 avisos ao cliente."*

➡️ *"Confira o momento e o tempo de cada aviso: de 5 minutos a 30 dias, ou a hora do aviso do dia."*

➡️ *"O texto do aviso passou de 2000 caracteres."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O menu Links de agendamento não aparece para mim.** O menu **Links de agendamento** é do administrador.
>
> **Links de agendamento é a mesma coisa que Agendamentos?** Não. Os **Links de agendamento** deixam o cliente marcar uma reunião com a equipe, pela página do link. O **Agendamentos** programa mensagens para o cliente.
>
> **O cliente marcou uma reunião pelo link de agendamento. Onde ela aparece?** No menu **Tarefas**, como uma tarefa do tipo **Reunião** de quem atende, com o nome do link e o do cliente no título e o link da videochamada.
>
> **O cliente recebe uma mensagem de confirmação da reunião marcada pelo link de agendamento?** Recebe, quando o link tem um aviso **Ao marcar** em **Avisos e automações**: a mensagem é enviada pelo WhatsApp logo depois da marcação. Sem nenhum aviso, o cliente vê só a confirmação na página, *"Reunião marcada!"*, com o **Link da videochamada**.
>
> **O cliente também conversa com a empresa por outro canal. Por onde vão os avisos do link de agendamento?** Pelo WhatsApp. A **Conexão dos avisos** só oferece conexões de WhatsApp e, vazia, os avisos vão pela conversa de WhatsApp do cliente, mesmo que ele tenha um atendimento mais novo em outro canal.
>
> **Como lembro o cliente da reunião marcada pelo link de agendamento?** Em **Editar link**, na seção **Avisos e automações**, clique em **Adicionar aviso**, escolha **Antes da reunião** e quanto tempo antes, escreva o **Texto** e salve.
>
> **Remarquei a reunião marcada pelo link de agendamento. Os lembretes mudam de horário?** Mudam. Os avisos de antes, do dia e de depois da reunião acompanham o horário novo da tarefa.
>
> **Como pauso um link de agendamento sem apagá-lo?** Em **Editar link**, desligue **Ativo (a página aceita marcação)** e salve. O link fica **Pausado**, e quem abre lê *"Este link de agendamento não existe ou está pausado."*
>
> **Uma tarefa que já está na agenda tira o horário da página do link de agendamento?** Tira, quando o tipo dela está marcado em **O que ocupa o horário** e ela tem hora marcada.
>
> **Dá para pôr a página do link de agendamento no site da empresa?** Dá. Na lista, clique em **Copiar o código para o site** e cole o código na página do site onde a agenda deve aparecer.

> **[ERROS]**
>
> #### Erros Comuns
>
> **"Este link de agendamento não existe ou está pausado":** o cliente abriu um link pausado ou com o endereço errado. **Solução:** no menu **Links de agendamento**, confira se o link está **Ativo** e mande de novo o endereço pelo **Copiar o link**.
>
> **O Salvar do Novo link não libera:** falta o **Nome**, uma pessoa em **Quem atende** ou a **Duração** está abaixo de 5 minutos. **Solução:** preencha os três e clique em **Salvar**.
>
> **A página mostra "Nenhum horário livre nestes dias.":** os dias na tela não têm horário livre. **Solução:** em **Editar link**, confira os **Dias e horários de atendimento** e o **Até quantos dias à frente**, e veja se as tarefas de quem atende ocupam esses horários.
