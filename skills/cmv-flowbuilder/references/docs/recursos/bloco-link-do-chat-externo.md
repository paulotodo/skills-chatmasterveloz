# Link do Chat Externo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-link-do-chat-externo
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Link do Chat Externo

---

🧩 O bloco **Link do Chat Externo** envia ao cliente o link da página do **Modo alternativo (chat externo por link)**, onde a conversa continua sem passar pela cobrança da API Oficial. É o mesmo link que o atendente envia pelo ícone de corrente, só que mandado pelo fluxo, sem depender de alguém lembrar.

Com a opção **Continuar o fluxo no chat externo** ligada, o fluxo inteiro passa a correr na página a partir dali.

**🏷️ Categoria: Mensagem**

Ideal para:

☑️ **Economia no canal oficial:** leva para a página a parte da conversa que teria muitas mensagens.

☑️ **Fluxo longo:** move menus e perguntas para a página, onde viram botões clicáveis.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No menu **Conexões**, confira se a conexão está com o **Modo alternativo (chat externo por link)** ligado.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo, clique no **+** e escolha **Link do Chat Externo**.
>
> ➡️ Escreva a mensagem, decida se o fluxo continua na página e clique em **Adicionar**.

## Como configurar o bloco Link do Chat Externo

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Link do Chat Externo**

🔘 **Mensagem (opcional):** o texto que acompanha o link. Use `{link}` onde o link deve entrar, como em *Prefere pelo navegador? Fale com a gente aqui: {link}*. Em branco, o bloco envia só o link.

🔘 **Continuar o fluxo no chat externo:** ligado, depois do link a conversa muda para a página. Os próximos blocos do fluxo, os robôs e as respostas do atendente vão só para lá, e menus e botões viram botões clicáveis na página. Vale até o atendimento ser encerrado.

🔲 Para finalizar, clique em **Adicionar**.

No WhatsApp Oficial, o link vai como botão. O texto desse botão não fica no bloco: ele é o **Texto do botão do chat externo**, configurado na conexão, e vale para todos os links dela.

No desenho, o bloco mostra a mensagem e, com a opção ligada, o aviso **O fluxo continua no chat externo**. Ele tem uma saída para o próximo passo.

⚠️ Com **Continuar o fluxo no chat externo** ligado, o que o cliente escrever no WhatsApp fica registrado na conversa, mas não faz o fluxo andar. A resposta que o fluxo espera é a que ele der na página.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O que muda quando ligo Continuar o fluxo no chat externo?** Os blocos seguintes, os robôs e as respostas do atendente vão para a página, até o atendimento ser encerrado. Desligada, o bloco só envia o link e o fluxo continua pelo WhatsApp.
>
> **Onde mudo o texto do botão que o bloco Link do Chat Externo envia?** Na conexão, no campo **Texto do botão do chat externo**. O bloco cuida só da mensagem que acompanha o link.
>
> **O envio do link é cobrado?** Sim. O link é uma mensagem de WhatsApp como outra qualquer. A economia vem depois, com a conversa acontecendo na página.
