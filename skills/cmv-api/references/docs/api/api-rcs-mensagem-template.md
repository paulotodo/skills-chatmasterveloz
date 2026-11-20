# API RCS Mensagem Template

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-rcs-mensagem-template
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API RCS Mensagem Template

---

🧩 Envia uma **mensagem template** aprovada do agente RCS, pela conexão de RCS com o provedor Gupshup.

**API:** RCS

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendRcsTemplate
```

##### Método

```
POST
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "number": "5511955892164",
    "template": "pedido_confirmado",
    "variables": {
        "nome": "Maria",
        "pedido": "123"
    },
    "name": "Maria Souza",
    "ticketId": 700
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números). **Obrigatório**, mesmo quando o `ticketId` é informado.

➡️ **“template”:** o código do template aprovado na Gupshup para o agente RCS. **Obrigatório.**

◽ Só a conexão de RCS com o provedor **Gupshup** envia template. Com outro provedor, a chamada é recusada.

◽ Quando o gateway recusa o template, a chamada responde **400**, e o motivo fica registrado no atendimento.

◽ A resposta de sucesso quer dizer que o gateway aceitou o template, não que ele chegou: o aviso de entrega vem depois.

➡️ **“variables”:** as variáveis do template, pelo nome, como estão no template aprovado.

➡️ **“name”:** nome do contato, usado só quando ele ainda não existe.

➡️ **“ticketId”:** ID do Ticket. **Opcional** — não substitui o `number`: só escolhe em qual atendimento a mensagem fica gravada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendRcsTemplate',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "template": "pedido_confirmado",
    "variables": {
        "nome": "Maria",
        "pedido": "123"
    },
    "name": "Maria Souza",
    "ticketId": 700
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendRcsTemplate' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","template":"pedido_confirmado","variables":{"nome":"Maria","pedido":"123"},"name":"Maria Souza","ticketId":700}'
```
