# API Atualizar Ticket

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-ticket
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Atualizar Ticket

---

🧩 Atualiza **um ticket**, alterando seu status, Setor, atendente ou campos personalizados.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/updateAPI
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
    "ticketId": "1067",
    "status": "pending",
    "userId": "13",
    "queueId": "34",
    "typebot_sessionId": "CAMPO LIVRE LETRAS E NÚMEROS",
    "customA": "CAMPO LIVRE LETRAS E NÚMEROS",
    "customB": "CAMPO LIVRE LETRAS E NÚMEROS",
    "customC": {"origem": "site"},
    "customD": {"pedido": 4471}
}
```

➡️ **“ticketId”:** ID do Ticket.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

➡️ **“status”:** `open`, `pending` ou `closed`.

➡️ **“userId”:** ID do atendente, ou `null`.

➡️ **“queueId”:** ID do Setor, ou `null`.

➡️ **“typebot_sessionId”:** ID da sessão do Typebot. Campo livre, letras e números.

➡️ **“customA”:** informação livre A.

➡️ **“customB”:** informação livre B.

➡️ **“customC”:** informação livre C, em JSON.

➡️ **“customD”:** informação livre D, em JSON.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/updateAPI',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": "1067",
    "status": "pending",
    "userId": "13",
    "queueId": "34",
    "typebot_sessionId": "",
    "customA": "",
    "customB": "",
    "customC": {"origem": "site"},
    "customD": {"pedido": 4471}
}',
  // "status": open, pending ou closed
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/updateAPI' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":"1067","status":"pending","userId":"13","queueId":"34","typebot_sessionId":"CAMPO LIVRE LETRAS E NÚMEROS","customA":"CAMPO LIVRE LETRAS E NÚMEROS","customB":"CAMPO LIVRE LETRAS E NÚMEROS","customC":{"origem":"site"},"customD":{"pedido":4471}}'
```
