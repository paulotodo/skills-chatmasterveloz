# Msg Interna

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-msg-interna
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Msg Interna

---

🧩 O bloco **Msg Interna** registra uma nota na conversa que só a equipe visualiza. O cliente não recebe nada; o atendente encontra a nota destacada no meio das mensagens, como um bilhete deixado pela automação.

**🏷️ Categoria: Dados**

☑️ **Passagem de bastão:** deixa um resumo, como *Cliente escolheu Financeiro*, antes de entregar a conversa a uma pessoa.

☑️ **Instrução ao atendente:** orienta o que conferir antes de responder.

☑️ **Rastro do fluxo:** marca os caminhos por onde o cliente passou.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Msg Interna**.
>
> ➡️ Escreva a nota em **Comentário Interno** e clique em **Adicionar**.

## Vídeo Tutorial

[Vídeo Voomly — id oWpEN8nREQjDvwdejAZGgt-BVL_cETrD6YYUT9lZa9ojB1VUc, tipo v]  

## Como configurar o bloco Msg Interna

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Msg Interna**

A janela **Adicionar bloco: Msg Interna** tem um campo:

🔘 **Comentário Interno:** o texto da nota que a equipe vai ler. Aceita variáveis do fluxo, escritas entre `%`, como `%nome%`: a nota mostra o valor guardado na variável.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco aparece como **Msg Interna**, com o texto da nota, e tem uma saída para o próximo passo.

## Como a nota aparece para a equipe

Para o atendente, a nota aparece com uma cor diferente, e título **Comunicação Interna**. Para o cliente, nada muda: a nota não é enviada a ele.

![Exemplo de mensagem interna na conversa](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ada1e496ef86.png)

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente recebe alguma notificação da Msg Interna?** Não. A nota não é enviada ao cliente, e o celular dele nem vibra.
>
> **Posso usar emojis na Msg Interna?** Pode. Um ⚠️ ajuda a chamar a atenção do atendente para uma situação crítica.
>
> **Posso usar uma variável do fluxo na Msg Interna?** Pode. Escreva o nome da variável entre `%`, como `%nome%`, no **Comentário Interno**: a equipe lê a nota com o valor que a variável guardou.
>
> **A Msg Interna fica no histórico?** Fica. Mesmo depois de encerrado o atendimento, a nota continua na conversa.
