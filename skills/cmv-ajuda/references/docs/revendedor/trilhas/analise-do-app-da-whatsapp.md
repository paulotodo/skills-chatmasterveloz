# Análise do App do WhatsApp

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/analise-do-app-da-whatsapp
- **Categoria:** Trilhas
- **Menu:** Meta › Análise do App do WhatsApp

---

🧩 **A Análise do Aplicativo Meta** é a chave mestra que liga a plataforma aos servidores do WhatsApp. Sem ele, a integração com a API Oficial não funciona.

Ao aprovar este App, você obtém as credenciais (ID e Secret) que permitem ao nosso sistema criar contas, gerar tokens e gerenciar números de WhatsApp em nome dos seus clientes.

☑️ **Liberação Final:** Tirar seu app do modo de rascunho e deixá-lo pronto para qualquer cliente usar.

☑️ **Uso Público:** Permitir que pessoas de fora da sua BM (seus clientes) façam login.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o portal **Meta for Developers** para editar seu **Aplicativo de Negócios** com **WhatsApp.**
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

🔲 Em seu **Aplicativo** acesse o menu **Analisar  ›  Análise do app** e em seguida no botão **Avançar.**

🔲 Expanda o box **Uso Permitido** e clique em **Ir para o uso permitido.**

Vamos solicitar aprovação um a um para cada permissão. Para isso clique em seus respectivos botões **Começar**.

### `public_profile`

☑️ Permite a plataforma acessar o perfil da conta.

🔘 Apenas marque o **check** e clique em **Salvar**.

### `whatsapp_business_messaging`

☑️ Permite a plataforma enviar e receber mensagens.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
Our application is a multi-agent customer support platform designed to help businesses manage their WhatsApp conversations efficiently. We use the whatsapp_business_messaging permission to: Receive incoming customer messages via webhooks and display them in our centralized dashboard. Allow support agents to send text and media replies directly from our interface to the end-user. This permission is critical for the core functionality of the app, as it enables multiple agents to collaborate and respond to customer inquiries from a single WhatsApp Business phone number, improving response times and customer satisfaction.
```

🔘 **Faça o upload** de um vídeo gravado de sua tela, mostrando a plataforma enviando uma mensagem para um whatsapp, que ao receber, enviar uma resposta e chega na plataforma.

🔘 Marque o **check** e clique em **Salvar**.

### `whatsapp_business_management`

☑️ Permite a plataforma criar e gerenciar contas WABA.

🔘 Preencha a **descrição** de uso dessa permissão. Sugestão:

```
We require the whatsapp_business_management permission to streamline the onboarding process for our clients (Tech Provider flow). This permission allows our application to: Read the WhatsApp Business Account (WABA) details and phone numbers after the user completes the Embedded Signup. This adds value by automating the setup process, ensuring that the business can connect their account and start supporting their customers immediately without manual configuration.
```

🔘 **Faça o upload** de um vídeo gravado de sua tela, mostrando a plataforma conectando via **Login do Facebook** no menu **Conexões.** Após isso demonstre a criação de um template na **Gestão de Templates** e sua visualização em seu App da Meta.

🔘 Marque o **check** e clique em **Salvar**.

## Tratamento de Dados

Seguindo para o próximo passo: vamos informar a Meta como nossos dados são tratados.

🔘 **Você tem operador de dados ou provedores de serviço:** selecione a opção **Sim.**

🔘 **Em adicionar operador de dados ou provedor de serviço:** informe o nome da **EVEO,** categoria **Soluções e Serviços de TI,** localizada no **Brasil.**

🔘 Siga preenchendo as **informações da empresa.**

## Instruções de Análise

🔘 **URL do site:** [LOGIN_URL]

🔘 **Forneça uma explicação sobre como acessar o app para que possamos concluir nossa análise:**

```
You can access our platform as the account administrator:

Web: [LOGIN_URL]
Email: [TEST_USER]
Password: [TEST_PASSWORD]

1. Go to the Conexões menu.
1.1. In the top right corner, click the 3-dot button, then select:
- "Adicionar WhatsApp Oficial" or
- "Adicionar Facebook Messenger" or
- "Adicionar Instagram DM"
to start syncing a Meta account with our system.
1.2. In the new pop-up window, click:
"Entrar com Facebook", or "Login com Facebook" or "Conectar com Instagram".
1.3. Complete the Meta sign-up process and connect the desired account/page.

2. In the Chats menu on the left, you can chat naturally with a WhatsApp, Facebook or Instagram lead.
2.1. The list of conversations is located on the left;
2.2. clicking on an item opens that conversation for exchanging messages.
```

🔲 Finalize com o botão **Enviar para análise**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Por que preciso enviar vídeo se já sou Tech Provider?** O Tech Provider valida a *Empresa*. O App Review valida o *Software*. O avaliador precisa garantir que, ao clicar no botão do seu site, ele realmente abre o WhatsApp e não um site malicioso.
>
> **Preciso de um aplicativo para cada canal?** Como você preferir. Dá para usar o **mesmo aplicativo** para WhatsApp, Messenger e Instagram, adicionando os produtos que faltarem, ou criar **um aplicativo por canal**. O processo de análise é o mesmo nos dois casos.
>
> **Onde vejo se foi aprovado?** Você receberá um e-mail e uma notificação no sininho do painel Developers. Geralmente leva de 24h a 48h.
