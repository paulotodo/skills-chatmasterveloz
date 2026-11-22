# Modo Alternativo (chat externo por link)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/modo-alternativo-chat-externo-por-link
- **Categoria:** Recursos
- **Menu:** Conexões › WhatsApp › Modo Alternativo (chat externo por link)

---

🧩 Toda resposta enviada pelo WhatsApp Oficial é cobrada pela Meta desde 1º de outubro de 2026. O **Modo Alternativo (chat externo por link)** existe para tirar parte da conversa dessa conta: o cliente toca num botão e a conversa continua numa página, sem sair do WhatsApp — e essa conversa não passa pela API Oficial.

Não é o **Chat Externo**, que é uma conexão própria, com página de entrada para o seu site: aqui a conversa começa no WhatsApp e só continua numa página.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões**, clique no lápis da conexão oficial e abra a aba **Geral**.
>
> ➡️ Ligue **Modo alternativo (chat externo por link)**, preencha os textos e salve.
>
> ➡️ Na conversa, clique no ícone de **corrente** na barra superior para enviar o botão ao cliente, ou utilize o bloco em fluxos de automação.
>
> ➡️ Depois que o cliente abrir a página, ligue o **globo** ao lado do **+** antes de escrever: com ele ligado, a sua mensagem vai para a página em vez do WhatsApp.

#### ![Ilustração do Modo Alternativo: o cliente recebe um botão no WhatsApp, a conversa continua numa página aberta dentro do próprio WhatsApp, e na plataforma as mensagens pela página aparecem como grátis enquanto a resposta pelo WhatsApp é cobrada.](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6aa4425f62432.png)

## Os dois botões que decidem o custo

🔘 **A corrente 🔗, na barra superior ou o bloco no fluxo de automação:** envia ao cliente o botão que abre a página. É uma mensagem de WhatsApp como qualquer outra — ela é cobrada. Você faz isso uma vez por conversa.

🔘 **O globo 🌐, no seu atendimento, ao lado da caixa de mensagem:** decide por onde sua mensagem é enviada:

**Ligado**, a mensagem aparece só na página e não passa pela Meta.

**Desligado**, ela é enviada pelo WhatsApp normalmente e entra na cobrança. (aparece também na página externa, que sempre mostra tudo)

⚠️ O globo é a parte que economiza. Mandar o botão e continuar respondendo com o globo desligado gasta tudo igual.

## O que o cliente vê na página

A página abre direto na **conversa atual**, com o nome da sua empresa no topo e uma saudação com o nome dele. É nessa tela que a conversa acontece.

📌 A conversa atual **traz o histórico recente junto**.

![Tela Atual e de Protocolos do Modo Alternativo](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6abced2ff345c.png)

### O botão de voltar, à esquerda do topo

A seta no canto esquerdo leva a uma **lista de conversas**. Cada linha é um **protocolo**, com:

◽ o **número do protocolo** e o canal por onde aquele atendimento entrou;

◽ a **data**, ou a hora quando é de hoje;

◽ uma **prévia da última mensagem**, dizendo quem falou;

◽ um selo: **Atual** para o atendimento em andamento, **Encerrado** para os que já terminaram.

### Os protocolos encerrados são só de leitura

Abrindo um protocolo antigo, o topo mostra o número dele e o cliente tem acesso ao histórico. No rodapé a página avisa **Somente leitura**, e oferece um botão **Voltar à conversa atual**.

➡️ Ou seja: ele consulta o que quiser do passado, mas só consegue escrever no atendimento em andamento.

Dentro da conversa ele pode **reagir com emoji** e **responder citando** uma mensagem, e tudo aparece na hora dos dois lados.

## Como enviar por automação

Além da corrente, o link pode ser enviado por um fluxo: o **FlowBuilder Nativo** tem o bloco **Link do Chat Externo**. Serve para quando a conversa precisa mudar de caminho sem depender de o atendente lembrar de clicar.

Dentro do bloco **Link do Chat Externo** existe a opção **Continuar o fluxo no chat externo**:

🔘 **Os próximos blocos do fluxo e os robôs passam a ir só para a página.** Menus e botões deixam de ser lista de opções no WhatsApp e viram **botões clicáveis** na página.

🔘 **As respostas do atendente também vão para a página, mas ele pode escolher o WhatsApp.** Com o atendimento na página, o **globo** já aparece ligado e o aviso dele diz que o envio é para a página. Para mandar uma resposta pelo WhatsApp, desligue o globo antes de escrever — a mensagem é enviada pelo WhatsApp e entra na cobrança. Para voltar a mandar pela página, ligue o globo de novo.

🔘 **O que o cliente escrever no WhatsApp continua registrado na conversa, mas não faz o fluxo andar.** A resposta que o fluxo espera é a que ele der na página.

🔘 **Vale até o atendimento ser encerrado — e o encerramento também acontece pela página.** A **avaliação do atendimento** é enviada na página, com as notas em botões, e não pelo WhatsApp.

⚠️ **Avaliação pela página não é cobrada, mas só é vista por quem abrir a página.** Se a resposta às avaliações for importante na sua operação, leve isso em conta antes de ligar a opção.

⚠️ No canva do fluxo, o bloco com a opção ligada mostra o aviso **O fluxo continua no chat externo**, então dá para conferir sem abrir o bloco.

## Como fica a conversa na plataforma

A plataforma marca cada mensagem pela origem, e a leitura é direta:

▫️ **Sem etiqueta, no balão comum:** mensagem que foi enviada pelo WhatsApp. Essa foi cobrada.

▫️ **🌐 Só no chat externo:** mensagem que você enviou com o globo ligado. Para o cliente, só aparece na página. É por essa marcação que você confere se a economia está acontecendo de verdade.

▫️ **🌐 Chat externo:** mensagem recebida que o cliente escreveu na página.

## As configurações dos campos na conexão

No menu **Conexões** configure:

🔘 **Modo alternativo (chat externo por link):** liga a função nesta conexão.

🔘 **Texto do botão do chat externo:** o que o cliente lê no botão, com até 20 caracteres. Em branco, a plataforma usa *"Abrir chat"*.

🔘 **Mensagem que acompanha o link:** o texto que vai junto com o botão. Em branco, a plataforma usa o texto padrão. Fora do botão, use `{link}` para escolher onde o endereço entra.

🔘 **Chat externo autenticado:** para abrir a conversa, o cliente digita os **quatro últimos dígitos do próprio telefone**. Nada é enviado a ele — a conferência é com o número que ele já tem.

⚠️ Enviar o botão não transfere nem encerra o atendimento, e o cliente continua podendo responder pelo WhatsApp. As duas origens caem na mesma conversa.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente precisa instalar alguma coisa?** Não. A página abre dentro do próprio WhatsApp.
>
> **O atendente vai atender em outro lugar?** Não. As mensagens da página entram na mesma conversa, marcadas pela origem.
>
> **Como envio o botão do Modo Alternativo?** Pelo ícone de corrente na barra superior do atendimento. Ou por automação, com o bloco **Link do Chat Externo** no FlowBuilder Nativo.
>
> **O que a opção Continuar o fluxo no chat externo muda?** Depois que o link é enviado, os próximos blocos do fluxo passam a correr na página. Sem ela, o link é enviado e o fluxo segue pelo WhatsApp.
>
> **Até quando a conversa fica na página?** Até o atendimento ser encerrado — e a avaliação do encerramento também vai pela página.
>
> **Com o atendimento na página, consigo mandar uma mensagem pelo WhatsApp?** Sim. Desligue o **globo**, ao lado do **+**, antes de escrever: a mensagem é enviada pelo WhatsApp e entra na cobrança. Para voltar a mandar pela página, ligue o globo de novo.
>
> **Encerrei o atendimento e a avaliação não foi pelo WhatsApp.** É assim mesmo com a opção **Continuar o fluxo no chat externo** ligada: a avaliação é enviada na página, com as notas em botões. O cliente responde abrindo a página.
>
> **Escrevi e a mensagem foi pelo WhatsApp mesmo com a página aberta.** O globo estava desligado. Ele fica ao lado do **+**, na caixa de mensagem, e precisa estar ligado a cada vez que você quiser mandar pela página.
>
> **Preciso mandar um link novo a cada atendimento?** Não. Pelo mesmo endereço o cliente chega à conversa atual, e pela seta do topo encontra os atendimentos anteriores.
>
> **O cliente pode escrever num atendimento antigo?** Não. Protocolo encerrado abre em **somente leitura**, com um botão para voltar à conversa atual. Escrever, só no atendimento em andamento.
>
> **O que o Chat externo autenticado pede?** Os quatro últimos dígitos do telefone do próprio cliente. É uma conferência local, sem código enviado e sem mensagem extra.
>
> **Existe na conexão por QR Code?** Não. O Modo Alternativo só aparece nas conexões de WhatsApp Oficial, que é onde existe cobrança por mensagem.
