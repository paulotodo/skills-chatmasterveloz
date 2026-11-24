# Firebase Push em Configurações

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/configuracoes-firebase-push
- **Categoria:** Recursos
- **Menu:** Configurações › Firebase Push em Configurações

---

🧩 O card **Firebase Push** recebe as credenciais que permitem à plataforma enviar notificações push para o aplicativo instalado — um arquivo para Android, outro para iOS. Na tela, o título é **Notificações push (Firebase)**.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No console do Firebase, no projeto da sua plataforma, gere o arquivo de **conta de serviço** (JSON).
>
> ➡️ Acesse o menu **Configurações  ›  Firebase Push**.
>
> ➡️ Em **Android**, clique em **Escolher arquivo JSON**, escolha o arquivo da conta de serviço e clique em **ENVIAR ANDROID**. Repita em **iOS** com **ENVIAR IOS**.

## Os dois blocos

🔘 **Android:** o arquivo `.json` da conta de serviço, escolhido em **Escolher arquivo JSON** e enviado em **ENVIAR ANDROID**.

🔘 **iOS:** idem, para iOS, com **ENVIAR IOS**.

Cada bloco mostra o nome com que o arquivo fica guardado — *firebase-service-account.json* no Android e *firebase-service-account-ios.json* no iOS — e avisa: *"O arquivo fica guardado com segurança no servidor, só para esta empresa."* O arquivo enviado é salvo com esse nome fixo, qualquer que seja o nome original.

⚠️ Para a notificação chegar, a empresa ainda precisa da chave **PUSH** no plano e o usuário precisa aceitar notificações no aparelho.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Enviei os arquivos e ninguém recebe notificação.** Confira, nesta ordem: a chave **PUSH** no plano da empresa; se o usuário instalou o aplicativo e aceitou as notificações; se o arquivo é da conta de serviço (não a configuração do app web).
>
> **Onde pego o arquivo da conta de serviço do Firebase?** No Firebase Console, como a própria tela orienta: *"Firebase Console › Configurações do projeto › Contas de serviço › Gerar nova chave privada"*.
