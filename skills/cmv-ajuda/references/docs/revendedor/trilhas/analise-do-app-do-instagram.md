# Análise do App do Instagram

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/analise-do-app-do-instagram
- **Categoria:** Trilhas
- **Menu:** Meta › Análise do App do Instagram

---

🧩 **A Análise do Aplicativo Meta** é a chave mestra que liga a plataforma aos servidores do Instagram. Sem ele, a integração não funciona.

☑️ **Liberação Final:** Tirar seu app do modo de rascunho e deixá-lo pronto para qualquer cliente usar.

☑️ **Uso Público:** Permitir que pessoas de fora da sua BM (seus clientes) façam login.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o portal **Meta for Developers** para editar seu **Aplicativo de Negócios** com **Instagram.**
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

🔲 No menu **Instagram** acesse o menu **Configurações da API do Instagram  ›  Faça a análise do app.**

### `instagram_business_basic`

☑️ Permite a plataforma acessar os dados básicos da conta (nome de usuário, foto e ID do perfil).

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
Our platform is a customer-service inbox that lets businesses manage their Instagram conversations from a single dashboard. We use instagram_business_basic to retrieve the connected Instagram professional account's basic metadata (account ID, username and profile picture), so we can display the correct account in the agent dashboard and associate conversations with the right business account.
```

🔘 **Faça o upload** de um vídeo gravado de sua tela, mostrando a plataforma enviando uma mensagem para seu instagram, que ao receber, enviar uma resposta e chega na plataforma.

🔘 Marque o **check** e clique em **Salvar**.

### `instagram_business_manage_messages`

☑️ Permite a plataforma receber e responder mensagens diretas (DMs) da conta.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
Our platform provides a unified customer-support inbox. We use instagram_business_manage_messages to receive direct messages that users send to the connected Instagram professional account and to send replies from our agent dashboard, enabling businesses to provide real-time customer support over Instagram Direct. We respect the 24-hour standard messaging window and Meta's message tag policies.
```

🔘 **Faça o upload** do vídeo.

🔘 Marque o **check** e clique em **Salvar**.

### `Human Agent`

☑️ Permite que um atendente humano responda fora da janela de 24h, por até 7 dias.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
Human Agent is not yet approved for our app, so the screencast shows the complete agent workflow and the error Meta returns today ("To use 'Human Agent', your use of this endpoint must be reviewed and approved"). The platform already sends the HUMAN_AGENT tag; once the feature is approved, these replies will be delivered.

Our platform is a human-operated customer-support platform. We use the Human Agent tag so human support agents can reply to a user's inquiry beyond the standard 24-hour window (up to 7 days) when a human response is needed to resolve the issue, for example when the answer depends on a check with another team or the message arrived outside business hours, in line with Meta's Human Agent policy. The tag is applied only to replies that an agent types and sends manually. Automated messages (flows, scheduled messages, satisfaction surveys and AI assistants) are never sent with this tag; after 24 hours the platform does not send them at all.

The screencast shows an agent manually replying to a conversation whose last customer message is more than 24 hours old, and the error above. For reference, it then shows a new customer message reopening the 24-hour window and the agent's reply being delivered to the customer's Instagram Direct.

== HUMAN AGENT ==

1. In the "Chats" menu, open an Instagram conversation where the customer's last message is older than 24 hours (see the timestamp on the last received message). The conversation bar shows the extended window ("Janela Estendida (Atendimento Humano)").
2. Type and send a reply as a human agent. The platform adds the HUMAN_AGENT message tag to this reply, allowing it within the 7-day window.
3. Until Human Agent is approved for our app, Meta returns the error shown in the screencast.
```

🔘 **Faça o upload** do vídeo.

🔘 Marque o **check** e clique em **Salvar**.

## Extras + 1 vídeo por permissão

### `instagram_business_manage_comments`

☑️ Permite a plataforma ler, responder e moderar comentários em posts e reels.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
We use instagram_business_manage_comments to read and reply to comments left on the connected Instagram professional account's posts and reels from our agent dashboard, allowing businesses to manage public engagement alongside their direct messages:
1. Read: comments arrive in the platform as a conversation with the customer, and the "Posts Instagram" screen lists the business's posts with their comments.
2. Reply manually: an agent writes a public reply from the "Posts Instagram" screen, and it is published under the customer's comment.
3. Reply automatically (optional, set up by the business): the business routes comments to a queue and chooses a keyword and a flow. When a comment contains the keyword, the flow publishes the business's reply under the comment and sends a private reply to the customer's Instagram Direct. Comments without the keyword get no automatic reply.

The screencast shows the setup (connection, queue, keyword "pricelist" and flow), a customer comment with the keyword receiving the automatic public and private replies, a second comment without the keyword, and an agent replying to it manually from the "Posts Instagram" screen. The replies are shown on Instagram.
```

🔘 **Faça o upload** do vídeo mostrando a plataforma lendo um comentário de post/reel e respondendo pelo painel.

🔘 Marque o **check** e clique em **Salvar**.

### `instagram_business_content_publish 🚫`

☑️ Permite a plataforma publicar conteúdo (posts e reels) na conta.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
We use instagram_business_content_publish to publish content (feed posts and reels) to the connected Instagram professional account directly from our platform, enabling businesses to manage their content alongside their conversations.
```

🔘 **Faça o upload** do vídeo com a plataforma criando um post/reel.

🔘 Marque o **check** e clique em **Salvar**.

### `instagram_business_manage_insights 🚫`

☑️ Permite a plataforma acessar métricas e estatísticas da conta (alcance, impressões, engajamento).

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
We use instagram_business_manage_insights to retrieve metrics and analytics for the connected Instagram professional account (such as reach, impressions and engagement) and display them as reports in our platform, helping businesses understand their performance.
```

🔘 **Faça o upload** do vídeo com a plataforma exibindo métricas/relatórios da conta do instagram.

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
