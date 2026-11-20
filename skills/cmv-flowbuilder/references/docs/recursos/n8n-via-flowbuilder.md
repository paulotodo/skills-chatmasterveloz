# n8n via Flowbuilder

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/n8n-via-flowbuilder
- **Categoria:** Recursos
- **Menu:** Integrações › n8n via Flowbuilder

---

[![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/26653-n8n.jpg)]()

## Integração n8n via FlowBuilter

A integração com o N8N via Flowbuilder é feita com o bloco Http Request

🧩 **Integração n8n via Flowbuilder (HTTP Request)** permite que seu chatbot "converse" com o n8n em um momento **específico** do fluxo.

Enquanto o Webhook é "passivo" (escuta tudo o que acontece), a **Requisição HTTP no Flowbuilder** é "ativa" e acontece num momento específico da conversa e **aguarda uma resposta** para continuar.

☑️ **Consultas em Tempo Real:** enviar um CPF ou Número de Pedido para o n8n analisar em sua programação e devolver o status direto na conversa.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Crie um **Workflow** no n8n.
>
> ➡️ Nesse workflow adicione um node de **Webhook Trigger** definindo HTTP Method POST. ➡️ Realize uma chamada HTTP Request a essa **URL** dentro do Flowbuilder. Se necessário aguarde a resposta do fluxo n8n e salve em um bloco de **Variável**.

## Como integrar o n8n com nosso sistema

### ⚡ Passo 01 - Configurar um fluxo no n8n

Dentro do N8N, crie um Workflow e adicione o node **Webhook Trigger,** para definir uma URL que será ativado quando nossa plataforma enviar um webhook.

**➡️** Utilize o HTTP Method **Post**

**➡️ Em Path:** defina uma URL personalizada e única.

**➡️ Authentication:** opcional, mas o padrão é None.

![Formulário Webhook Trigger do n8n para configurar a integração](https://clihelper.chatmasterveloz.com/docs-imagem/26653-n8n-webhook-trigger.jpg)

### ⚡ Passo 02 - Chamar o fluxo do n8n utilizando o Flowbuilder

No FlowBuilder utilize o bloco HTTP Request com o seguinte código (alterando para a URL correspondente):

```
// definir
let endpoint = "https://enderecoWebhookTrigger";
let method = "POST";
let payload = {
  "number": "{{number}}",
  "contactId": "{{contact_id}}",
  "name": "{{name}}",
  "firstName": "{{firstName}}",
  "ticketId": "{{ticket_id}}",
  "protocol": "{{protocol}}",
  "queueId": "{{queue}}",
  "userName": "{{user}}",
  "connectionName": "{{connection}}",
  "companyName": "{{name_company}}",
  "backendURL": "{{backendURL}}",
  "token": "{{connection_token}}",
  "dataHora": "{{data_hora}}"
  // apague ou insira outros payloads desejados aqui
};
// estrutura
try {
    const response = await axios({
      url: endpoint,
      method: method,
      headers: {
        'Content-Type': 'application/json'
      },
      data: payload,
      maxBodyLength: Infinity
    });
    return JSON.stringify(response.data, null, 2);
} catch (error) {
    return "Algo deu errado: " + error.message;
}
```

### ⚡ Passo 03 - Aguardar Resposta (opcional)

Em seu n8n você pode configurar seu workflow para enviar uma resposta ao Flowbuilder.

Para isso, em seu node "**Webhook Trigger**" no campo **Respond**, escolha a opção **Using 'Respond to Webhook' Node**.

E no final do seu fluxo, adicione o node **Respond to Webhook** configurando os dados de resposta ao Flowbuilder.

Para salvar essa resposta, em seu Flowbuilder, após o bloco de HTTP Request que fez a requisição ao n8n, adicione um bloco de **Variável**.
