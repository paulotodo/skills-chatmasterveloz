# Avisos ao Cliente em Tarefas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/avisos-ao-cliente-em-tarefas
- **Categoria:** Recursos
- **Menu:** Tarefas › Avisos ao Cliente em Tarefas

---

🧩 Seu cliente esquece a visita combinada, ou nem fica sabendo que ela foi marcada? Com os **avisos ao cliente** das **Tarefas**, a plataforma envia ao cliente uma mensagem pelo WhatsApp quando a tarefa é criada e um lembrete antes do horário, sem ninguém da equipe precisar escrever.

O administrador escreve os textos dos avisos uma vez, para a empresa toda, e cada tarefa escolhe se avisa o cliente e quais avisos usa. Nas palavras da tela, o aviso chega *"mesmo a quem ainda não tem cadastro nem conversa aberta"*: basta o nome e o WhatsApp do cliente.

Ideal para:

☑️ **Visita marcada:** Confirma ao cliente o dia e a hora no momento em que a tarefa é criada.

☑️ **Lembrete do compromisso:** Envia o lembrete antes do horário, no tempo que a tarefa escolhe.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Tarefas** e clique em **Avisos ao cliente**.
>
> ➡️ Escreva a mensagem de **Quando a tarefa é criada** e a de **Antes do horário** e clique em **Salvar**.
>
> ➡️ Na **Nova Tarefa**, ligue **Avisar o cliente pelo WhatsApp**, escolha o cliente e os avisos e clique em **Criar Tarefa**.

## Como configurar os avisos das tarefas

Acesse o menu **Tarefas  ›  Avisos ao cliente**

O botão **Avisos ao cliente** fica no topo da tela de **Tarefas** e é do administrador. A janela abre com o título *Avisos das tarefas ao cliente* e explica: *"As mensagens que o cliente recebe pelo WhatsApp quando a tarefa liga o aviso: ao ser criada e antes do horário. Cada tarefa escolhe os avisos dela."*

🔘 **Enviar pela conexão:** a Conexão de WhatsApp por onde os avisos são enviados. A lista traz só as conexões de WhatsApp. Nas palavras da tela, *"Vazio: pela conversa do cliente (ou pela conexão padrão)."*

🔘 **Quando a tarefa é criada:** a **Mensagem** enviada assim que a tarefa é criada, até 2.000 caracteres. O texto sugerido é `{{ms}}, {{cliente}}! Está marcado: {{tarefa}}, {{quando}}.`

🔘 **Antes do horário:** a **Mensagem** do lembrete, até 2.000 caracteres. O texto sugerido é `{{ms}}, {{cliente}}! Lembrete: {{tarefa}} começa {{quando}}.`

🔘 **Webhook dos avisos (opcional):** o endereço de outro sistema que acompanha os avisos. Nas palavras da tela, ele *"Recebe um POST quando um aviso sai e quando não sai, com o motivo."* O endereço precisa começar com `http://` ou `https://` e não pode apontar para a rede interna.

Clique em **Salvar**. A tela confirma *"Avisos salvos"*.

⚠️ Com uma das mensagens em branco, a tela avisa *"Preencha as duas mensagens (e o modelo completo, se escolheu um)."* e o **Salvar** fica desativado.

## As variáveis dos avisos das tarefas

A **Mensagem** de cada aviso troca as variáveis pelos dados da tarefa na hora do envio. A janela lista as variáveis, e cada uma vai entre chaves duplas:

➡️ `{{cliente}}`: o nome do cliente da tarefa.

➡️ `{{tarefa}}`: o título da tarefa.

➡️ `{{data}}` e `{{hora}}`: o dia e a hora de início da tarefa.

➡️ `{{quando}}`: o dia e a hora juntos, como *em 20/11/2026 às 14:00*.

➡️ `{{responsavel}}`: a pessoa responsável pela tarefa.

➡️ `{{link}}`: o link da videochamada, quando a tarefa tem uma sala de reunião.

Valem também as variáveis da conversa: `{{ms}}`, que vira a saudação do horário (*Bom dia*, *Boa tarde*…), e `{{firstName}}`, o primeiro nome do contato. Com o texto sugerido, o cliente recebe algo como *"Bom dia, Ana! Está marcado: Visita técnica, em 20/11/2026 às 14:00."*

## Como ligar o aviso numa tarefa

Na janela da **Nova Tarefa**, o bloco **Avisar o cliente pelo WhatsApp** começa desligado. Nas palavras da tela: *"Ligue para o cliente receber a mensagem quando a tarefa for criada e um lembrete antes do horário — mesmo quem ainda não tem cadastro nem conversa aberta."*

🔘 **Contato cadastrado:** busca o cliente entre os contatos; cada um aparece com o nome e o número. A lista traz também os contatos do Messenger e do Instagram, mas o aviso só vai para um contato de WhatsApp.

🔘 **Contato novo:** o **Nome** e o **WhatsApp** do cliente. Nas palavras da tela, o WhatsApp vai *"Com DDI e DDD, só números"*, como `5511999999999`. Quando o número informado já é de um contato, a tarefa usa esse contato.

🔘 **Avisar ao criar a tarefa:** envia a mensagem de **Quando a tarefa é criada** assim que você clica em **Criar Tarefa**.

🔘 **Avisar antes do horário:** envia o lembrete antes do início da tarefa, com **60 min antes (o lembrete)**, **15 minutos**, **30 minutos**, **1 h**, **2 h**, **3 h** ou **1 dia antes**.

O bloco lembra onde ficam os textos: *"Os textos das mensagens ficam em Tarefas → Avisos ao cliente."*

⚠️ **Tarefa sem horário:** sem os **Horários** preenchidos, **Avisar antes do horário** fica desmarcado e desativado, e a tela explica: *"O aviso antes do horário precisa da data e da hora de início."* A tarefa é criada só com o aviso ao criar.

## Como acompanhar os avisos da tarefa

Na tarefa já criada, aberta em **Editar**, o aviso de criação vira **Avisar ao salvar (se ainda não avisou)**, e cada aviso mostra a situação: *Enviado em* com a data e a hora, como *Enviado em 17/11/2026, 06:29:24*, ou *Não foi enviado* e o motivo.

Para tentar de novo um aviso que não foi enviado, abra a tarefa em **Editar**, deixe **Avisar ao salvar (se ainda não avisou)** marcado e clique em **Atualizar**. Quando o motivo é o contato, troque antes o cliente da tarefa por um contato de WhatsApp: com a troca, o aviso é enviado e a tarefa passa a mostrar *Enviado em* com a data e a hora. O aviso que já foi enviado não é enviado de novo.

## Por onde os avisos das tarefas são enviados

Os avisos ao cliente das **Tarefas** são enviados só pelo WhatsApp: a lista **Enviar pela conexão** traz só as conexões de WhatsApp. Com o campo vazio, o aviso vai pela conversa de WhatsApp do cliente.

O cliente da tarefa precisa ser um contato de WhatsApp. Um contato do Messenger ou do Instagram não recebe o aviso, mesmo que tenha conversa no WhatsApp, e a tarefa diz por quê: *"Não foi enviado: o cliente é um contato do Messenger e não tem número de WhatsApp — escolha na tarefa um contato de WhatsApp"* — ou *do Instagram*, conforme o contato. Ao criar a tarefa, a tela confirma só *"Tarefa criada com sucesso!"*; o motivo aparece ao abrir a tarefa em **Editar**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente ainda não tem cadastro. Ele recebe o aviso da tarefa?** Recebe. Em **Avisar o cliente pelo WhatsApp**, escolha **Contato novo** e informe o **Nome** e o **WhatsApp**, com DDI e DDD, só números.
>
> **Criei uma tarefa sem horário. Por que o Avisar antes do horário está desativado?** Porque o lembrete conta a partir do início da tarefa. Nas palavras da tela: *"O aviso antes do horário precisa da data e da hora de início."* A tarefa é criada com o aviso ao criar; para ter o lembrete, preencha os **Horários**.
>
> **Os avisos das tarefas podem ir por uma Conexão que não é de WhatsApp?** Não. Os avisos das tarefas são enviados só pelo WhatsApp, e **Enviar pela conexão** lista só as conexões de WhatsApp.
>
> **Onde mudo o texto dos avisos das tarefas?** No menu **Tarefas**, no botão **Avisos ao cliente**. O texto vale para todas as tarefas da empresa; cada tarefa só escolhe quais avisos usa.
>
> **Como sei se o aviso da tarefa foi enviado?** Abra a tarefa em **Editar**: em **Avisar o cliente pelo WhatsApp**, cada aviso mostra *Enviado em* com a data e a hora, ou *Não foi enviado* com o motivo.
>
> **O aviso não foi enviado. Como tento de novo?** Abra a tarefa em **Editar**, deixe **Avisar ao salvar (se ainda não avisou)** marcado e clique em **Atualizar**. Se o motivo for o contato — *"o cliente é um contato do Messenger"* ou *do Instagram* —, troque antes o cliente da tarefa por um contato de WhatsApp. O aviso que já foi enviado não é enviado de novo.
>
> **Escolhi um contato do Instagram ou do Messenger na tarefa. Por que o aviso não foi enviado?** Porque os avisos das tarefas vão só para um contato de WhatsApp. A busca **Contato cadastrado** lista também os contatos do Messenger e do Instagram, mas, com um deles, a tarefa mostra *Não foi enviado* com o motivo. Escolha o contato de WhatsApp do cliente.
>
> **O Notificar antes (minutos) da tarefa avisa o cliente?** Não. O **Notificar antes (minutos)** lembra a equipe; o lembrete do cliente é o **Avisar antes do horário**, no bloco **Avisar o cliente pelo WhatsApp**.
>
> **O atendente não encontra o botão Avisos ao cliente nas Tarefas.** O botão **Avisos ao cliente** é do administrador. O atendente liga os avisos em cada tarefa, no bloco **Avisar o cliente pelo WhatsApp**.
