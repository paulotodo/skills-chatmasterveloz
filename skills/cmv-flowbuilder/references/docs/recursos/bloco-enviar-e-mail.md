# Enviar e-mail

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-enviar-e-mail
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Enviar e-mail

---

🧩 O bloco **Enviar e-mail** envia um e-mail no meio do fluxo: a confirmação do que o cliente combinou na conversa, o material que ele pediu, o aviso à equipe de que um contato chegou. O e-mail vai por uma das contas de e-mail da empresa ou por um provedor de envio por API, e o fluxo segue por um de dois caminhos: **Enviado** ou **Não enviado**.

**🏷️ Categoria: Mensagem - Roteador**

Ideal para:

☑️ **Confirmação por e-mail:** Envia ao contato, por escrito, o que ele combinou na conversa.

☑️ **Aviso para a equipe:** Avisa um endereço da empresa de que o contato passou por aquela etapa do fluxo.

☑️ **Plano B sem e-mail:** Leva o fluxo para outro caminho quando o contato não tem e-mail ou o envio falha.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Confira se a empresa tem uma conta de e-mail ativa no menu **Contas de E-mail**, ou um provedor em **Provedores de envio por API**, na mesma tela.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo no editor, clique no **+** e escolha **Enviar e-mail**.
>
> ➡️ Escolha **Enviar por**, preencha **Para**, **Assunto** e **Mensagem** e clique em **Adicionar**.
>
> ➡️ Ligue as saídas **Enviado** e **Não enviado** aos próximos passos.

## Como configurar o bloco Enviar e-mail

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Enviar e-mail**

A janela **Adicionar bloco: Enviar e-mail** tem estes campos:

🔘 **Enviar por:** por onde o e-mail é enviado. A lista separa as opções em dois grupos: **Contas de E-mail**, as caixas da empresa cadastradas no menu **Contas de E-mail**, e **Provedores por API**, os provedores de envio cadastrados na mesma tela.

🔘 **Para:** o endereço que recebe o e-mail. Nas palavras da tela: *"Vazio: o e-mail do contato. Aceita variáveis, como {{email}}."*

🔘 **Assunto:** o assunto do e-mail. Sem ele, a janela não salva e avisa *"Escreva o assunto do e-mail."*

🔘 **Mensagem:** o texto do e-mail, com quantas linhas precisar.

Nas palavras da janela: *"O assunto e a mensagem aceitam as variáveis do contato e do fluxo. Sem e-mail no contato, ou se o envio falhar, o fluxo segue pela saída Não enviado."* No e-mail que chega, `{{name}}` e `{{ticket_id}}` aparecem trocados pelo nome do contato e pelo número do atendimento.

Depois de preencher, clique em **Adicionar**. No desenho, o bloco mostra o assunto, o destino — *Para: o e-mail do contato*, com o **Para** vazio — e as duas saídas.

## As saídas Enviado e Não enviado

🔘 **Enviado:** o caminho quando o e-mail foi enviado.

🔘 **Não enviado:** o caminho quando o e-mail não pôde ser enviado — o **Para** ficou vazio e o contato não tem e-mail, ou a conta de e-mail escolhida falhou no envio.

⚠️ Ligue as duas saídas, mesmo que uma delas seja só uma mensagem. Saída sem ligação faz o fluxo parar ali.

O e-mail enviado pelo bloco **Enviar e-mail** não fica registrado na conversa, nem o motivo do **Não enviado**, e não aparece na pasta **Enviadas** da conta de e-mail. Na conversa aparece só o que os blocos seguintes enviarem.

## Os provedores de envio por API

Os provedores ficam no menu **Contas de E-mail**, no painel **Provedores de envio por API**, embaixo das contas. Nas palavras da tela: *"Envie e-mails pelo FlowBuilder Nativo sem SMTP, usando a chave de API do seu provedor de disparo."* Só o administrador cadastra provedores, cada um com o serviço de disparo, a chave de API e o remetente. Os campos de cada provedor estão no artigo **Provedores de Envio de E-mail por API**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Para quem o bloco Enviar e-mail envia quando o campo Para fica vazio?** Para o e-mail do contato da conversa. Sem e-mail no cadastro do contato, o fluxo segue pela saída **Não enviado**.
>
> **O e-mail do bloco Enviar e-mail aparece na conversa?** Não. Nada fica registrado na conversa nem na pasta **Enviadas** da conta de e-mail. Para avisar o cliente pelo atendimento, ligue a saída **Enviado** a um bloco de mensagem.
>
> **Posso usar o nome do contato no e-mail do bloco Enviar e-mail?** Pode. O **Assunto** e a **Mensagem** aceitam as variáveis do contato e do fluxo, como `{{name}}`, que chega trocada pelo nome do contato.
>
> **Preciso de um servidor SMTP para usar o bloco Enviar e-mail?** Não necessariamente. O **Enviar por** aceita também um provedor de envio por API, cadastrado no menu **Contas de E-mail**, em **Provedores de envio por API**, só com a chave do provedor.

> **[ERROS]**
>
> #### Erros Comuns
>
> **A janela mostra "Escreva o assunto do e-mail.":** o **Assunto** ficou vazio. **Solução:** escreva o assunto e clique em **Adicionar**.
>
> **O fluxo sempre segue por Não enviado:** o contato não tem e-mail e o **Para** está vazio, ou a conta escolhida em **Enviar por** não consegue enviar. **Solução:** preencha o **Para** ou o e-mail do contato, e confira a conta no menu **Contas de E-mail**, com **Testar conexão**.
