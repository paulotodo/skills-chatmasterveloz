# API Horário de Expediente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-horario-de-expediente
- **Categoria:** APIs
- **Menu:** APIs › Extras › API Horário de Expediente

---

🧩 Verifica o **horário de expediente de um Setor**. Dentro do horário a resposta traz `"isOpen": true`; fora dele, `"isOpen": false`.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/queue
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
    "queueId": 1
  }
```

➡️ **“queueId”:** ID do Setor.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/queue',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "queueId": 1
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
curl -X POST 'https://api2.chatmasterveloz.com/api/queue' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"queueId":1}'
```
