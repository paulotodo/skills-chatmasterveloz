# Webhook de E-mail

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-de-e-mail
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook de E-mail

---

🧩 Quer que o seu sistema saiba na hora que um e-mail chegou ou foi enviado pelas contas de e-mail da empresa? O **Webhook de E-mail** avisa o seu sistema a cada e-mail recebido e a cada e-mail enviado.

O **Webhook de E-mail** cobre só os e-mails. As conversas com os clientes são avisadas pelos webhooks da Conexão e do Setor.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções** e encontre o campo **Webhook de e-mail**.
>
> ➡️ Preencha o endereço do seu sistema e clique em **Salvar**.

## Onde ligar o Webhook de E-mail

🔘 **Webhook de e-mail:** o endereço que recebe os avisos dos e-mails de todas as contas de e-mail da empresa. Em branco, nada é enviado. O botão **Salvar**, ao lado do campo, grava o endereço, e a tela avisa *"Webhook de e-mail salvo."*

O endereço precisa começar com http:// ou https://, sem espaços, e não pode apontar para a rede interna.

## Os eventos do Webhook de E-mail

Tudo chega no mesmo endereço. Os eventos enviados são estes:                  

| Evento | O que aconteceu |
|---|---|
| `email-recebido` | um e-mail chegou a uma conta de e-mail da empresa |
| `email-enviado` | um e-mail foi enviado por uma conta de e-mail da empresa, pela tela ou pela API |

⚠️ Nas palavras da tela, o **Webhook de E-mail** *"Só avisa o e-mail recebido com até 48 horas (a caixa antiga não dispara a automação)."*

## O que chega em cada aviso

Cada aviso chega em JSON, com o mesmo formato nos dois eventos:

🔘 `acao`: o evento, como `email-recebido`.

🔘 `companyId`, `enviadoEm`, com a hora do envio do aviso, e `backendURL`, o endereço da plataforma.

🔘 `email`: o e-mail. Traz o `id`, a conta (`accountId` e `accountEmail`), a pasta (`folder`), o `tipo` (`recebido` ou `enviado`), `from`, `to` e `cc`, o assunto (`subject`), o começo do texto (`snippet`), o texto inteiro (`text`), `hasAttachments`, que diz se tem anexo, `isSeen`, que diz se foi lido, a data (`date`) e os identificadores da mensagem (`messageId`, `inReplyTo` e `threadId`).

Exemplo de `email-recebido`:

```json
{
  "acao": "email-recebido",
  "companyId": 2,
  "email": {
    "id": 981,
    "accountId": 2,
    "accountEmail": "contato@lojaexemplo.com.br",
    "folder": "INBOX",
    "tipo": "recebido",
    "messageId": "<a1b2c3@cliente.com>",
    "inReplyTo": null,
    "threadId": "<a1b2c3@cliente.com>",
    "from": { "address": "maria@cliente.com", "name": "Maria Souza" },
    "to": [{ "address": "contato@lojaexemplo.com.br", "name": null }],
    "cc": [],
    "subject": "Orçamento do pedido 120",
    "snippet": "Bom dia! Podem me mandar o orçamento do pedido 120?",
    "text": "Bom dia! Podem me mandar o orçamento do pedido 120?",
    "hasAttachments": false,
    "isSeen": false,
    "date": "2026-11-05T11:42:10.000Z"
  },
  "enviadoEm": "2026-11-05T11:42:17.844Z",
  "backendURL": "https://api.exemplo.com.br"
}
```

## Como saber que o aviso veio daqui

Nas palavras da tela, o aviso do **Webhook de E-mail** vai assinado com o **Token da Empresa**, no cabeçalho `X-Assinatura-Email`.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Webhook de E-mail avisa as mensagens das conversas com os clientes?** Não. O **Webhook de E-mail** cobre só os e-mails das contas de e-mail da empresa. As mensagens das conversas são avisadas pelos webhooks da Conexão e do Setor.
>
> **O e-mail enviado pela API dispara o Webhook de E-mail?** Dispara. O e-mail enviado pela API chega como `email-enviado`, igual ao enviado pela tela.
>
> **Os e-mails antigos da caixa disparam o Webhook de E-mail?** Não. O aviso de `email-recebido` vale para o e-mail recebido com até 48 horas: a caixa antiga não dispara a automação.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Webhook de e-mail inválido:** ao salvar, a tela avisa *"Webhook de e-mail inválido: use um endereço http:// ou https://, sem espaços, fora da rede interna."* **Solução:** use o endereço público do seu sistema, começando com http:// ou https://, sem espaço no meio.
