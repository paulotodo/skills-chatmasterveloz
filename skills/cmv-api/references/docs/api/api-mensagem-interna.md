# API Mensagem Interna

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-mensagem-interna
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Mensagem Interna

---

🧩 Envia uma **mensagem de comunicação interna (whisper)**, sendo visível somente dentro do sistema.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/internal/send
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
    "ticketId": "33461",
    "body": "Lead precisa de retorno no pedido"
  }
```

➡️ **“ticketId”:** ID do Ticket — o número entre parênteses no cabeçalho da conversa.

◽ Em **João da Silva (52) | #25678**, o `ticketId` é **52**.

◽ O número depois do **#** é o protocolo (25678, no exemplo) e não serve nesta API.

➡️ **“body”:** mensagem interna.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/internal/send',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": "33461",
    "body": "Lead precisa de retorno no pedido"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/internal/send' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":"33461","body":"Lead precisa de retorno no pedido"}'
```
