# Recuperação de Senha

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/como-habilitar-recuperacao-de-senha
- **Categoria:** Recursos
- **Menu:** Como Habilitar › Recuperação de Senha

---

🧩 Ofereça a **recuperação de senha** pelo canal que preferir: o código de segurança chega ao usuário por e-mail, por WhatsApp ou pelos dois.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**, escolha em **Modo de Recuperação de Senha** entre **Somente E-Mail**, **Somente WhatsApp** ou **E-Mail & WhatsApp**.
>
> ➡️ Para WhatsApp: no menu **Conexões**, clique no lápis da conexão que vai enviar o código e ative a opção **Padrão**.
>
> ➡️ Para e-mail: no Resend, valide o domínio e crie a chave de API, como abaixo; depois cole a chave e o **Remetente de E-Mail** no menu **Configurações  ›  Plataforma**, seção **SMTP API (RESEND)**.
>
> ⚠️ Com **Somente WhatsApp** ou **E-Mail & WhatsApp**, é obrigatório ter uma Conexão conectada marcada como **Padrão**: sem ela, o sistema fica sem por onde enviar e o usuário não recebe o código.

## Configurar o envio por e-mail

A entrega usa a integração com o **Resend**. Faça o cadastro em [resend.com/signup](https://resend.com/signup) usando como login o próprio endereço que será remetente.

#### ⚡ Validar o domínio

🔘 No Resend, acesse **Domains** e clique em **+ Add Domain**.

🔘 Informe o domínio do e-mail e valide o DNS. Em provedores como a Cloudflare a validação é automática; nos demais, os registros são configurados um a um.

#### ⚡ Criar a chave de API

🔘 No Resend, acesse **Api Key** e clique em **+ Create Api Key**.

🔘 Dê um nome à chave — por exemplo, `Recuperar Senha Chat Master Veloz`.

🔘 Copie a chave e cole no menu **Configurações  ›  Plataforma**, seção **SMTP API (RESEND)**, campo **API RESEND**.

🔘 Preencha o **Remetente de E-Mail** com o mesmo endereço cadastrado no Resend, do domínio validado.

![image.png](https://revendedor.chatmasterveloz.com/docs-imagem/ed-6a9acef4ac77e.png)

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Como sei se o e-mail de recuperação de senha foi enviado?** Acompanhe pelo menu **Logs** dentro do painel do Resend. Ele mostra se a mensagem foi entregue ou rejeitada.
