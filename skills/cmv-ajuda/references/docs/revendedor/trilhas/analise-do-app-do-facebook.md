# Análise do App do Facebook

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/analise-do-app-do-facebook
- **Categoria:** Trilhas
- **Menu:** Meta › Análise do App do Facebook

---

🧩 **A Análise do Aplicativo Meta** é a chave mestra que liga a plataforma aos servidores do Facebook. Sem ele, a integração não funciona.

☑️ **Liberação Final:** Tirar seu app do modo de rascunho e deixá-lo pronto para qualquer cliente usar.

☑️ **Uso Público:** Permitir que pessoas de fora da sua BM (seus clientes) façam login.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o portal **Meta for Developers** para editar seu **Aplicativo de Negócios** com **Facebook.**
>
> ➡️ Enviar **vídeos e informação** em Análise do App.

> **[PREREQUISITO]**
>
> ## **Pré-requisitos Obrigatórios**
>
> Antes de começar, você **precisa** ter:
>
> ◽ Uma **BM (Portfólio Empresarial)** devidamente **Verificada** na Meta e aprovada com o status de **Tech Provider**. Sem isso, o App não sai do modo de desenvolvimento.

## ☁️ Acessando as Permissões

Acesse **Meus Aplicativos** em [https://developers.facebook.com](https://developers.facebook.com) usando a mesma conta de facebook utilizada para logar em sua BM.

🔲 No menu **Messenger** acesse o menu **Configurações da API do Messenger  ›  Faça a análise do app.**

### `pages_messaging`

☑️ Permite a plataforma receber e responder mensagens da Página no Messenger.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
Our platform is a customer-service inbox that lets businesses manage their Facebook Page conversations from a single dashboard. We use pages_messaging to receive messages that users send to the connected Facebook Page and to send replies from our agent dashboard, enabling real-time customer support over Messenger. We respect the 24-hour standard messaging window and Meta's messaging policies.
```

🔘 **Faça o upload** de um vídeo gravado de sua tela, mostrando a plataforma enviando uma mensagem para seu facebook, que ao receber, enviar uma resposta e chega na plataforma.

🔘 Marque o **check** e clique em **Salvar**.

🔘 **Testar e reproduzir a funcionalidade da sua integração:**

```
To test the pages_messaging integration with our platform:

1. Open [LOGIN_URL] and log in with the test account below.
2. The Facebook Page "[PAGE_NAME]" is already connected as a channel in the dashboard.
3. From a real Facebook account, open the "[PAGE_NAME]" Page via [MME_LINK] on Messenger and send a message.
4. The message appears in real time in the agent inbox of our platform.
5. Type a reply in the dashboard and send it; confirm it is delivered to the user on Messenger.

Test login:
- URL: [LOGIN_URL]
- User: [TEST_USER]
- Password: [TEST_PASSWORD]

The reviewer may also use their own Facebook account to message the Page.
```

### `pages_manage_metadata`

☑️ Permite a plataforma assinar a Página nos webhooks, para receber as mensagens em tempo real.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
We use pages_manage_metadata to subscribe the connected Facebook Page to our app's webhooks, so messages and messaging events sent to the Page are delivered to our platform in real time. Without this subscription, incoming Messenger messages would not reach the agent inbox.
```

🔘 **Faça o upload** do vídeo.

🔘 Marque o **check** e clique em **Salvar**.

### `pages_show_list`

☑️ Permite a plataforma listar as Páginas que o usuário administra, para ele escolher qual conectar.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
We use pages_show_list during onboarding so the business can see the list of Facebook Pages they manage and select which Page to connect. This ensures we only connect the Page the user explicitly chooses.
```

🔘 **Faça o upload** do vídeo.

🔘 Marque o **check** e clique em **Salvar**.

### `pages_read_engagement`

☑️ Permite a plataforma ler dados e informações da Página (nome, detalhes do perfil).

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
We use pages_read_engagement to read basic information about the connected Page (such as its name and profile details) so we can display the correct Page in the agent dashboard and associate conversations with the right business account.
```

🔘 **Faça o upload** do vídeo.

🔘 Marque o **check** e clique em **Salvar**.

### `business_management`

☑️ Permite a plataforma acessar e verificar os ativos do Business do usuário. Também é dependência do `pages_messaging` e do `pages_show_list`.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
We use business_management to access and verify the business assets the user manages, confirming the connected Page belongs to the user's Business before linking it to our platform. Note: business_management is also a dependency for pages_messaging and pages_show_list.
```

🔘 **Faça o upload** do vídeo.

🔘 Marque o **check** e clique em **Salvar**.

## Extras + 1 vídeo por permissão

### `pages_utility_messaging 🚫`

☑️ Permite enviar mensagens de utilidade fora da janela de 24h.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
We use pages_utility_messaging to send utility message templates (such as order confirmations, shipping updates and appointment reminders) to users outside the standard 24-hour window. These messages are non-promotional and tied to a specific transaction or request from the user.
```

🔘 **Faça o upload** do vídeo mostrando o envio de um template de utilidade fora da janela de 24h e ele chegando no Messenger.

🔘 Marque o **check** e clique em **Salvar**.

## Tratamento de Dados

Seguindo para o próximo passo: vamos informar a Meta como nossos dados são tratados.

🔘 **Você tem operador de dados ou provedores de serviço:** selecione a opção **Sim.**

🔘 **Em adicionar operador de dados ou provedor de serviço:** informe o nome da **EVEO,** categoria **Soluções e Serviços de TI,** localizada no **Brasil.**

🔘 Siga preenchendo as **informações da empresa.**

🔲 Finalize com o botão **Enviar para análise**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Por que preciso enviar vídeo se já sou Tech Provider?** O Tech Provider valida a *Empresa*. O App Review valida o *Software*.
>
> **Preciso de um aplicativo para cada canal?** Como você preferir. Dá para usar o **mesmo aplicativo** para WhatsApp, Messenger e Instagram, adicionando os produtos que faltarem, ou criar **um aplicativo por canal**. O processo de análise é o mesmo nos dois casos.
>
> **Onde vejo se foi aprovado?** Você receberá um e-mail e uma notificação no sininho do painel Developers. Geralmente leva de 24h a 48h.
