# API Encerrar Ticket em Massa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-encerrar-ticket-em-massa
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Encerrar Ticket em Massa

---

🧩 Encerra **um grupo de tickets** de uma vez, a partir do status e do Setor.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/closestatus
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
    "status": "open",
    "all": false,
    "queueId": null
  }
```

➡️ **“status”:** status dos tickets a encerrar — `open`, `pending` ou `both`.

➡️ **“all”:** define o alcance entre as conexões.

◽ `false` — somente a conexão do token usado na chamada.

◽ `true` — todas as conexões.

➡️ **“queueId”:** ID do Setor cujos tickets serão encerrados. Deixe `null` para encerrar os de todos os Setores.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/closestatus',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "status": "open",
    "all": false,
    "queueId": null
  }',
  // "status": use open, pending ou both
  // "all": true qualquer conexão. Se false, obedece a conexão do token
  // "queueId": ID do Setor
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/closestatus' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"status":"open","all":false,"queueId":null}'
```
