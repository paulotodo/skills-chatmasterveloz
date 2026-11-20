# Chat Externo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/chat-externo
- **Categoria:** Recursos
- **Menu:** Conexões › Chat Externo

---

🧩 O **Chat Externo** é um chat para o seu site. Você publica um link — no site, nas redes ou num QR Code — e quem entra conversa com a sua equipe numa página do navegador, sem instalar nada. Pense numa **porta de entrada própria**: a conversa não começa no WhatsApp, começa na página, e chega à plataforma como qualquer outro atendimento.

Ao entrar, a pessoa informa o telefone, e é por ele que a conversa se liga ao cadastro do contato. Não é o **Modo Alternativo (chat externo por link)**, que leva para uma página uma conversa que já começou no WhatsApp.

Ideal para:

☑️ **Atender quem visita o site:** um botão ou link de contato que abre a conversa na hora.

☑️ **Campanhas e QR Code:** o mesmo link vai num anúncio, numa embalagem ou num material impresso.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões**, abra **Ações** e escolha **Adicionar Chat Externo**.
>
> ➡️ Preencha o **Nome da conexão**, escolha os **Setores** e salve.
>
> ➡️ No card da conexão, clique em **Copiar link de entrada** e publique o link no seu site.
>
> ➡️ As conversas chegam como atendimentos em **Aguardando**, no Setor escolhido.

## Como criar a conexão

Acesse o menu **Conexões  ›  Ações  ›  Adicionar Chat Externo**. A janela **Novo Chat Externo** tem cinco abas.

### ⚡ Geral

🔘 **Nome da conexão:** nome interno para identificar esta conexão. **Obrigatório.**

🔘 **Setores:** para onde vão as conversas que entram pela página.

### ⚡ Mensagens

🔘 **Mensagem de saudação:** enviada ao cliente quando a conversa começa.

🔘 **Mensagem de conclusão:** enviada quando o atendimento é encerrado.

🔘 **Mensagem de fora do expediente:** enviada quando o cliente chama fora do horário de atendimento.

🔘 **Mensagem de avaliação:** enviada para pedir que o cliente avalie o atendimento.

🔘 **Mensagem de despedida:** enviada quando o atendimento é encerrado por inatividade.

### ⚡ Comportamento

🔘 **Novo ticket ao reabrir:** decide o que acontece quando o cliente volta a escrever depois de um atendimento encerrado. Desligado, a mensagem reabre o mesmo atendimento, com um protocolo novo.

🔘 **Após** e **Mover:** depois do tempo escolhido, o atendimento que está esperando é movido para o Setor indicado.

🔘 **Inatividade** e **Inatividade Sem Setor:** encerram o atendimento quando o cliente não responde.

### ⚡ Integrações

🔘 **URL de Webhook** e **URL de Webhook Secundário:** endereços que recebem os eventos desta conexão, como as mensagens recebidas.

🔘 **Token da conexão:** usado na autorização das chamadas à API desta conexão. Precisa ser único.

### ⚡ Página de entrada

Esta aba só abre depois que a conexão é salva. Para chegar a ela, clique no lápis do card da conexão.

🔘 **Aparência:** a foto, a cor e o nome do topo da página que o cliente abre. Vale para o link de atendimento e para o canal Chat Externo.

◽ **Enviar foto:** JPG, PNG ou WEBP, até 1,5 MB. A foto é recortada em quadrado e salva na hora; **Remover foto** tira.

◽ **Cor principal:** a cor da página. Sem escolha, fica o **Padrão (verde)**.

◽ **Nome no topo:** em branco, usa o nome da empresa.

◽ **Frase abaixo do nome:** em branco, mostra "online" ou o nome do cliente.

🔘 **Link da página de entrada:** o endereço que você publica. **Copiar link** copia o endereço; **Gerar novo link** cria um endereço novo.

🔘 **País padrão:** o país que já vem escolhido no formulário da página.

🔘 **Oferecer todos os países:** ligado, a pessoa escolhe qualquer país da lista. Desligado, aparece o campo **Países oferecidos**, para você escolher quais entram.

🔘 **Permitir entrar sem telefone:** mostra no formulário a opção *"Prefiro não informar meu telefone"*.

🔘 **Pedir o nome:** o nome passa a ser obrigatório para entrar.

🔘 **Texto de consentimento:** com texto, a pessoa precisa marcar que aceita antes de entrar. Vazio, a página não pede o aceite. Até 1.000 caracteres.

## O que o cliente visualiza

A página mostra no topo o nome da sua empresa — ou o **Nome no topo**, quando preenchido — e pede *"Para começar, informe o seu telefone."*, com os campos **País** e **Telefone** e o botão **Entrar**. Entrando, a conversa abre ali mesmo, e a caixa de mensagem tem emoji, anexo e áudio. Sem o nome pedido no formulário, a página trata a pessoa como **Visitante**.

📌 **A página lembra a conversa no mesmo navegador.** Ao abrir o link de novo, ela avisa *"Você tem uma conversa recente neste navegador."* e oferece **Continuar a conversa anterior** ou **Começar nova**.

## Como a conversa chega à equipe

O atendimento entra em **Aguardando**, no Setor da conexão, e a equipe aceita e responde como em qualquer outro. O cliente visualiza, na página, o nome de quem respondeu junto da mensagem.

🔘 **Telefone de um contato que já existe:** a conversa entra **nesse mesmo contato**, com o nome que está no cadastro.

🔘 **Sem telefone:** a conversa entra num contato novo, com um nome gerado automaticamente.

Todo atendimento que vem pela página traz três sinais:

◽ o selo **Telefone informado, não verificado**, no cabeçalho;

◽ uma nota interna com o telefone que a pessoa digitou na entrada;

◽ a marca **Chat externo** nas mensagens do cliente.

⚠️ **O telefone não é verificado.** Qualquer pessoa pode digitar o número de outra, e a conversa entra no cadastro de quem tem aquele número. Antes de passar dado pessoal, de pedido ou de pagamento, confirme com quem você está falando.

📌 **Cada entrada por um navegador novo abre um atendimento novo**, com protocolo próprio, mesmo que o telefone seja o mesmo.

## Bloquear e encerrar

🔘 **Bloquear conversa:** fica nas ações do atendimento. A plataforma pergunta *"Bloquear esta conversa?"* e explica que o cliente não consegue mais escrever nem reagir pela página, mas continua vendo a conversa. Para ele, a página mostra *"Esta conversa foi encerrada pelo atendimento."* e a caixa de mensagem fica travada.

🔘 **Desbloquear conversa:** o mesmo botão, depois do bloqueio. Libera na hora, sem pedir confirmação.

🔘 **Encerrar:** pelo **Resolver**, com ou sem mensagem de encerramento. O cliente visualiza *"Atendimento encerrado. Envie uma mensagem para começar outro."* e, se escrever, o atendimento volta para **Aguardando** com um protocolo novo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **É o mesmo que o Modo Alternativo?** Não. O Modo Alternativo leva para uma página uma conversa que já começou no WhatsApp. O Chat Externo é uma porta de entrada própria: a conversa começa na página do seu site.
>
> **A conversa se junta com o histórico do WhatsApp?** Não por enquanto. O que liga as duas coisas é o cadastro do contato: o telefone digitado leva a conversa para o contato que tem aquele número.
>
> **O cliente precisa instalar alguma coisa?** Não. A página abre no navegador, no computador ou no celular.
>
> **Onde pego o link para colocar no site?** No card da conexão, em **Copiar link de entrada**, ou na aba **Página de entrada**, editando a conexão.
>
> **Dá para entrar sem informar o telefone?** Sim, com **Permitir entrar sem telefone** ligado: o formulário mostra *"Prefiro não informar meu telefone"*, e a conversa entra num contato novo, com nome gerado.
>
> **Por que apareceu um atendimento novo se o cliente é o mesmo?** Cada entrada por um navegador novo abre um atendimento novo. No mesmo navegador, a página oferece continuar a conversa anterior.
>
> **Bloqueei a conversa. O cliente ainda visualiza as mensagens?** Sim. Ele continua vendo a conversa, mas não consegue escrever nem reagir até você desbloquear.
>
> **O cliente pode voltar depois que o atendimento foi encerrado?** Pode. Ele escreve na mesma página e o atendimento volta para Aguardando, com protocolo novo.

> **[ERROS]**
>
> #### Erros Comuns
>
> **A conversa chegou, mas não aparece na tela de Chats:** quem não faz parte do Setor da conexão não visualiza o atendimento. **Solução:** confira os **Setores** da conexão e se o usuário está neles, ou filtre a lista de Chats pelo Setor.
>
> **A aba Página de entrada está apagada:** a conexão ainda não foi salva. **Solução:** salve e clique no lápis do card para voltar à aba.
>
> **Tratar o telefone como confirmado:** a conversa entra no cadastro de quem tem o número digitado, que pode não ser quem está escrevendo. **Solução:** confirme a identidade antes de passar dado pessoal ou fechar pedido.
