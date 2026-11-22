# Provedores de Envio de E-mail por API

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/provedores-de-envio-de-e-mail-por-api
- **Categoria:** Recursos
- **Menu:** E-mails › Provedores de Envio de E-mail por API

---

🧩 O fluxo precisa enviar e-mail — a confirmação de um pedido, o material que o cliente pediu —, mas a empresa não quer usar uma caixa de e-mail com servidor SMTP para isso? Os **provedores de envio por API** são os serviços de disparo de e-mail ligados à plataforma pela chave de API: eles enviam os e-mails do bloco **Enviar e-mail** do FlowBuilder Nativo, sem SMTP.

O provedor de envio só envia, pela chave de API do serviço de disparo: ele não é uma caixa de e-mail. No bloco **Enviar e-mail**, o campo **Enviar por** mostra as contas de e-mail e os provedores, cada grupo com o seu nome.

Ideal para:

☑️ **Envio sem SMTP:** Envia os e-mails do fluxo pela chave de API do serviço de disparo, sem servidor de e-mail próprio.

☑️ **Remetente do domínio da empresa:** Envia com um endereço do domínio verificado no serviço de disparo.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Contas de E-mail** e, no painel **Provedores de envio por API**, clique em **Novo provedor**.
>
> ➡️ Escolha o **Provedor**, preencha **Nome**, **Chave de API** e **E-mail do remetente** e clique em **Salvar**.
>
> ➡️ No bloco **Enviar e-mail** do FlowBuilder Nativo, escolha o provedor em **Enviar por**.

## O painel Provedores de envio por API

Acesse o menu **Contas de E-mail**. Embaixo da lista de contas fica o painel **Provedores de envio por API**. Nas palavras da tela: *"Envie e-mails pelo FlowBuilder Nativo sem SMTP, usando a chave de API do seu provedor de disparo."* Sem nenhum provedor, o painel mostra *"Nenhum provedor cadastrado."*

O painel é do administrador, como o resto do menu **Contas de E-mail**: o supervisor não tem o menu, e a plataforma recusa a ele a lista dos provedores.

## Como cadastrar um provedor de envio por API

Acesse o menu **Contas de E-mail  ›  Novo provedor**

🔘 **Provedor:** o serviço de disparo, escolhido na lista — *SendGrid*, *Brevo*, *Resend*, *Mailgun* ou *Postmark*.

🔘 **Nome:** como o provedor aparece na lista do painel e no **Enviar por** do bloco **Enviar e-mail**.

🔘 **Chave de API:** a chave gerada na conta do serviço de disparo.

🔘 **E-mail do remetente:** nas palavras da tela, *"Use um endereço do domínio verificado no provedor."*

🔘 **Nome do remetente:** o nome de quem envia.

🔘 **Ativo:** liga e desliga o provedor. Desligado, ele aparece na lista com o selo **Inativo**.

🔘 **Domínio de envio** e **Região:** aparecem só para um dos serviços da lista, o *Mailgun*, com a **Região** *US* ou *EU*.

Ao salvar, a janela pede o que falta: *"Dê um nome ao provedor de envio."*, *"Informe um e-mail válido para o remetente."* e *"Informe a chave de API do provedor."*

## Os provedores cadastrados

Cada provedor de envio cadastrado ocupa uma linha do painel, com o nome, o serviço e o remetente, e três ações:

🔘 **Enviar teste:** pede o endereço em *Enviar o teste para* e, com **Enviar**, avisa *"Teste enviado para …"* ou o motivo de o teste não ter sido enviado.

🔘 **Editar:** o ícone abre a janela **Editar provedor**, com os mesmos campos. Nas palavras da tela, a chave pode ficar em branco: *"Deixe vazio para manter a chave gravada."*

🔘 **Excluir:** o ícone pede confirmação, em *Excluir provedor?*, e avisa *"Os blocos do fluxo que usam este provedor passam a seguir pela saída Não enviado."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual a diferença entre uma conta de e-mail e um provedor de envio por API?** A conta de e-mail é uma caixa do servidor: recebe por **IMAP**, envia por **SMTP** e é usada no menu **E-mails**. O provedor de envio por API só envia, pela chave de API do serviço de disparo, e serve aos e-mails do bloco **Enviar e-mail** do FlowBuilder Nativo.
>
> **O que acontece com o fluxo quando excluo um provedor de envio por API?** Nas palavras da tela, *"Os blocos do fluxo que usam este provedor passam a seguir pela saída Não enviado."* Troque o **Enviar por** desses blocos antes de excluir o provedor.
>
> **O supervisor pode cadastrar um provedor de envio por API?** Não. O painel **Provedores de envio por API** fica no menu **Contas de E-mail**, que é só do administrador.

> **[ERROS]**
>
> #### Erros Comuns
>
> **A janela Novo provedor não salva:** a tela avisa *"Dê um nome ao provedor de envio."*, *"Informe um e-mail válido para o remetente."* ou *"Informe a chave de API do provedor."* **Solução:** preencha o **Nome**, um **E-mail do remetente** válido e a **Chave de API** e clique em **Salvar**.
