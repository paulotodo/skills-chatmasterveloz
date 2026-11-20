# API Enviar Status de Vídeo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-status-de-video
- **Categoria:** APIs
- **Menu:** APIs › Extras › API Enviar Status de Vídeo

---

🧩 Envia um **status de vídeo**.

**API:** Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendVideoStatus
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
    "body": "data:video/mp4;base64,Akd9300...",
    "caption": "Teste"
  }
```

➡️ **“body”:** o vídeo em `base64`.

➡️ **“caption”:** legenda do status.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendVideoStatus',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "body": "data:video/mp4;base64,Akd9300...",
    "caption": "Teste"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendVideoStatus' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"body":"data:video/mp4;base64,Akd9300...","caption":"Teste"}'
```
