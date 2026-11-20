# API Gravando….

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-gravando-pro
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Gravando….

---

🧩 Altera o status para **Gravando...** até que mude para "pause" ou que envie uma mensagem.

**API:** Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendComposingPRO
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
    "body": "composing", //composing, paused
    "caption": "audio"
  }
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“body”:** `composing` para ficar gravando…, e `paused` para parar.

➡️ **“caption”:** `audio` para ficar gravando…, e **“”** para digitando…

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendComposingPRO',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
  "number": "5511955892164",
  "body": "composing",
  "caption": "audio"
}',
// "body": "composing" ou  "paused"
// "caption": "audio" para gravando
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendComposingPRO' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","body":"composing","caption":"audio"}'
```
