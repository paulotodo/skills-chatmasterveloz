# API Atualizar Tags do Ticket

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-tags-do-ticket
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Atualizar Tags do Ticket

---

🧩 Define as **Tags de um ticket**.

⚠️ Esta chamada **substitui** as Tags do ticket: as que já estavam vinculadas são removidas e ficam valendo apenas as que você enviar no código. Para manter alguma, inclua o ID dela junto.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tags/add
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
    "ticketId": 383,
    "tags": [
      {
        "id": 100
      },
      {
        "id": 98
      }
    ]
}
```

➡️ **“ticketId”:** ID do Ticket.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

➡️ **“tags.id”:** ID de cada Tag que deve ficar no ticket.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tags/add',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": 383,
    "tags": [
      {
        "id": 100
      },
      {
        "id": 98
      }
    ]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tags/add' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":383,"tags":[{"id":100},{"id":98}]}'
```
