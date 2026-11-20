# API Obter um Ticket

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-um-ticket
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Obter um Ticket

---

🧩 Obter **um ticket específico**.

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
    "ticketId": "2003"
  }
```

➡️ **“ticketId”:** ID do Ticket.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

⚠️ Esta chamada usa o **mesmo endereço da atualização de ticket**. Enviando apenas o `ticketId`, nada é alterado: o ticket só é devolvido. Qualquer outro campo que você incluir no payload **será gravado** no ticket.

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
    "ticketId": "2003" // Informe o ID do Ticket
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/updateAPI' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":"2003"}'
```
