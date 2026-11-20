# API Enviar Status de Texto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-status-de-texto
- **Categoria:** APIs
- **Menu:** APIs › Extras › API Enviar Status de Texto

---

🧩 Envia um **status de texto**.

**API:** Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendTextStatus
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
    "body": "Testando",
    "color": 4294967295,
    "backgroundcolor": 4285408638,
    "font": 10
  }
```

➡️ **“body”:** a mensagem de texto do status.

➡️ **“color”:** cor do texto.

➡️ **“backgroundcolor”:** cor do fundo.

➡️ **“font”:** tamanho da fonte.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendTextStatus',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "body": "Testando",
    "color": 4294967295,
    "backgroundcolor": 4285408638,
    "font": 10
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendTextStatus' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"body":"Testando","color":4294967295,"backgroundcolor":4285408638,"font":10}'
```
