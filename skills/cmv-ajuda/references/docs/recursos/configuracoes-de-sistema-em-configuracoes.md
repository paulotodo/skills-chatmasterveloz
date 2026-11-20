# Configurações de Sistema em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/configuracoes-de-sistema-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Configurações de Sistema em Configurações

---

🧩 A seção **Configurações de Sistema** é a maior da aba: reúne as mensagens automáticas que a plataforma envia em situações específicas, o comportamento de leitura e distribuição, a concatenação de entrada do construtor de fluxos e o limite de mensagens que o fluxo responde a um mesmo contato.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções** e localize **Configurações de Sistema**.
>
> ➡️ Os campos de texto são as mensagens automáticas; os de escolha mudam comportamento.

## Recuperação de senha e distribuição

🔘 **Modo de Recuperação de Senha:** por onde o usuário recebe o código ao esquecer a senha — **Somente E-Mail**, **Somente WhatsApp** ou **E-Mail & WhatsApp**. Para WhatsApp, precisa de uma Conexão marcada como **Padrão**.

🔘 **Modo de Randomização de Atendimento:** quem entra no sorteio da distribuição automática — **Somente Usuários Online** ou **Usuários Online e Offline**.

## Mensagens automáticas

🔘 **Mensagem de Recusa de Áudio:** enviada quando a empresa bloqueia áudio e o cliente manda um.

🔘 **Mensagem Saída Forçada:** enviada quando o atendimento é encerrado pelo sistema, não pelo atendente.

🔘 **Mensagem de Encaminhamento:** enviada ao cliente quando a conversa é encaminhada a um atendente — por exemplo, quando o rodízio de atendimento passa a conversa para o atendente sorteado. O texto aceita `{{ms}}`, que vira a saudação do horário (Bom dia, Boa tarde…), e `{{name}}`, o nome do cliente: com `{{ms}} *{{name}}*, em alguns instantes um atendente irá prosseguir com seu atendimento.`, a cliente Maria recebe pela manhã *"Bom dia Maria, em alguns instantes um atendente irá prosseguir com seu atendimento."*

🔘 **Mensagem de Notificação Externa:** o texto do aviso que o **atendente** recebe no WhatsApp pessoal quando o Setor tem **Notificar Operador no WhatsApp** ligado — por exemplo, quando o rodízio de atendimento entrega uma conversa a ele. Um exemplo de texto: *"Existe atendimento aguardando sua atenção na plataforma."* O aviso vai para o telefone cadastrado no usuário, em **Equipe**.

🔘 **Texto de Recuperação de Mensagem Perdida:** o texto usado quando uma mensagem precisa ser recuperada.

🔘 **Mensagem de Saudação para setor único?:** decide se o cliente recebe a **Mensagem de saudação** do Setor quando a Conexão aponta para um único Setor, sem menu de escolha. Com **Sim**, a saudação do Setor é enviada assim que o cliente escreve; com **Não**, ela não é enviada. Nos dois casos a saudação da Conexão fica de fora: com um Setor só, não há menu para ela abrir.

🔘 **Informar Posição na Fila?** e **Mensagem de Posição na fila:** com **Sim**, o cliente que entra num Setor e fica aguardando recebe, logo depois da saudação do Setor, a posição dele na espera — a contagem inclui todos os que aguardam naquele Setor, ele mesmo também. O texto vem de **Mensagem de Posição na fila** e é seguido do número da posição; com `{{ms}} *{{name}}*, sua posição na fila de atendimento é:`, a cliente Maria recebe pela manhã *"Bom dia Maria, sua posição na fila de atendimento é: 3"*. Quando o Setor escolhido tem **Opções do Chatbot**, a posição não é enviada enquanto o cliente escolhe a opção.

## Leitura, áudio e comentários

🔘 **Marcar Como Lida:** quando a mensagem do cliente é marcada como lida — **Ao Visualizar** ou **Ao Responder**. Com "Ao Responder", o cliente não vê o visto duplo azul até o atendente escrever.

🔘 **Ignorar Validação de Contatos?:** com **Sim**, a plataforma deixa de validar o número ao cadastrar um contato.

🔘 **[Mostrar Todos] Habilitado?:** liga ou desliga o filtro **Mostrar Todos** na lista de atendimentos.

🔘 **Bloquear Áudio de Todos os Contatos?:** com **Sim**, áudio recebido é recusado e o cliente recebe a **Mensagem de Recusa de Áudio**.

🔘 **Botão de Comentário Interno Disponível?:** mostra ou esconde, para o atendente, o botão de comentário que o cliente não vê.

🔘 **Quantidade de Mensagens ao Abrir uma Conversa:** quantas mensagens do histórico são carregadas ao abrir o atendimento — de **1** a **16** ou mais.

🔘 **Assinatura Genérica:** o texto de assinatura usado quando a mensagem é enviada sem o nome do atendente.

## Concatenação de entrada

🔘 **Concatenação no Flowbuilder?** e **Tempo de Concatenação:** com **Sim**, as mensagens que o **cliente** manda em sequência são juntadas antes de o fluxo responder — e o tempo de espera vai de **2** a **10 segundos**. Serve para o fluxo não responder cada fragmento de frase.

⚠️ Esta concatenação é de **entrada** — junta o que o cliente escreve. A que junta o que o **atendente** escreve, para ser enviado como uma mensagem só, é outra: fica no card da Conexão oficial, no botão **Concatenador**, e vai de 2 a 60 segundos. Os dois se chamam "concatenação" e não são a mesma coisa.

## Limite de mensagens do fluxo

🔘 **Limitar as mensagens que o fluxo responde ao mesmo contato?** Protege contra quem fica disparando o fluxo sem parar. Com **Sim**, defina o limite:

◽ **Máximo de mensagens do mesmo contato:** quantas mensagens o fluxo responde a um mesmo contato.

◽ **Contadas dentro de:** a janela de tempo, em minutos, em que essas mensagens são contadas.

◽ **Ao passar do limite, pausar o robô por:** por quantas horas o fluxo deixa de responder àquele contato.

Passou do limite, o fluxo deixa de responder a esse contato pelo tempo escolhido, e o atendimento fica em **Aguardando** para a equipe, com um aviso na conversa.

🔘 **Retomar antes do prazo:** no cadastro do contato aparece o aviso de que a automação está pausada para ele, com a data, e o botão **Retomar o robô agora**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente reclama que o visto azul demora.** É o **Marcar Como Lida** em **Ao Responder**. A leitura só é confirmada quando o atendente escreve.
>
> **O fluxo responde cada palavra que o cliente manda.** Ligue **Concatenação no Flowbuilder?** e dê um **Tempo de Concatenação** de alguns segundos.
>
> **Um contato fica mandando mensagem sem parar e o fluxo responde a todas.** Ligue **Limitar as mensagens que o fluxo responde ao mesmo contato?** e defina o máximo, a janela de tempo e a pausa.
>
> **Onde escolho se o código de recuperação vai por e-mail ou WhatsApp?** Em **Modo de Recuperação de Senha**, nesta seção. Para WhatsApp, marque uma Conexão como **Padrão** no menu **Conexões**.
>
> **O cliente deveria saber quantos estão na frente dele. Onde ligo isso?** Em **Informar Posição na Fila?**, nesta seção: com **Sim**, quem entra num Setor e aguarda recebe a posição logo depois da saudação do Setor. O texto do aviso fica em **Mensagem de Posição na fila**.
>
> **Minha Conexão tem um Setor só. O cliente recebe a saudação do Setor?** Depende de **Mensagem de Saudação para setor único?**, nesta seção: com **Sim**, recebe assim que escreve; com **Não**, não recebe.
>
> **Onde mudo a mensagem que o cliente recebe quando o rodízio passa a conversa para um atendente?** Em **Mensagem de Encaminhamento**, nesta seção. O texto vale para toda a empresa.
>
> **Onde mudo o texto do aviso que o atendente recebe no WhatsApp?** Em **Mensagem de Notificação Externa**, nesta seção. O aviso só é enviado quando o Setor tem **Notificar Operador no WhatsApp** ligado e o usuário tem telefone cadastrado em **Equipe**, no padrão DDI + DDD + número.
