# Webhook do Mail Marketing

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-do-mail-marketing
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook do Mail Marketing

---

🧩 Quer que o seu sistema saiba na hora que uma campanha de e-mail começou a ser enviada, que alguém abriu o e-mail ou clicou num link, ou que uma pessoa se descadastrou? O **Webhook do Mail Marketing** avisa o seu sistema a cada evento das listas, dos modelos e das campanhas do Mail Marketing.

O **Webhook do Mail Marketing** cobre só o Mail Marketing. As conversas com os clientes são avisadas pelos webhooks da Conexão e do Setor.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Mail Marketing  ›  Configurações**.
>
> ➡️ Preencha o campo **Webhook do Mail Marketing** com o endereço do seu sistema, começando com https://.
>
> ➡️ Clique em **Salvar**.

## Onde ligar o Webhook do Mail Marketing

🔘 **Webhook do Mail Marketing:** o endereço que recebe os avisos do Mail Marketing da empresa. Nas palavras da tela: *"Só https. Cada evento leva o nome em X-MailMarketing-Evento e a assinatura em X-Assinatura-MailMarketing."*

O botão **Salvar** da aba **Configurações** grava o webhook junto com as outras configurações do Mail Marketing, e a tela avisa *"Configuração salva."*

⚠️ Só o administrador da empresa altera o **Webhook do Mail Marketing**. Para o supervisor, a aba **Configurações** aparece com os campos desabilitados e sem o **Salvar**.

## Os eventos do Webhook do Mail Marketing

Tudo chega no mesmo endereço. A aba **Configurações** mostra os eventos que o webhook envia:                                              

| Evento | O que aconteceu |
|---|---|
| `lista-criada` · `lista-alterada` · `lista-removida` | uma lista de contatos foi criada, mudou ou foi apagada |
| `contatos-adicionados` · `contato-removido` | contatos entraram numa lista, ou um contato saiu dela |
| `modelo-criado` · `modelo-alterado` · `modelo-removido` | um modelo de e-mail foi criado, mudou ou foi apagado |
| `campanha-criada` · `campanha-alterada` · `campanha-removida` | uma campanha foi criada, mudou ou foi apagada |
| `campanha-agendada` · `campanha-iniciada` · `campanha-pausada` · `campanha-retomada` · `campanha-cancelada` · `campanha-concluida` | a campanha foi agendada, começou a ser enviada, foi pausada, retomada, cancelada ou terminou |
| `envio-falhou` | um e-mail da campanha não foi enviado |
| `email-aberto` | uma pessoa abriu o e-mail da campanha |
| `link-clicado` | uma pessoa clicou num link do e-mail da campanha |
| `descadastro` | uma pessoa se descadastrou e deixou de receber as campanhas da empresa |

## Como saber que o aviso veio daqui

Pela ajuda da tela, cada aviso do **Webhook do Mail Marketing** leva o nome do evento no cabeçalho `X-MailMarketing-Evento` e a assinatura no cabeçalho `X-Assinatura-MailMarketing`.

A assinatura depende do **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**. Sem ele, nas palavras da tela: *"Gere o token da empresa para o webhook funcionar: nada sai sem assinatura."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Quem pode cadastrar o Webhook do Mail Marketing?** Só o administrador da empresa, na aba **Configurações** do Mail Marketing. O supervisor vê a aba com os campos desabilitados, sem o **Salvar**.
>
> **Como sei qual evento do Webhook do Mail Marketing chegou?** Pelo cabeçalho `X-MailMarketing-Evento`, que leva o nome do evento, como `email-aberto` ou `descadastro`.
>
> **O Webhook do Mail Marketing avisa as mensagens das conversas com os clientes?** Não. O **Webhook do Mail Marketing** cobre só os eventos do Mail Marketing: listas, modelos, campanhas e os e-mails das campanhas. As mensagens das conversas são avisadas pelos webhooks da Conexão e do Setor.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Webhook do Mail Marketing com http://:** ao salvar, a tela avisa *"O webhook precisa começar com https:// e apontar para fora do servidor."* **Solução:** use o endereço público do seu sistema, começando com https://.
