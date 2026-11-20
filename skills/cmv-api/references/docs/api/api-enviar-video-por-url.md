# API Enviar Vídeo por URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-video-por-url
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Enviar Vídeo por URL

---

🧩 Envia um **vídeo a partir de uma URL**, com opção de legenda.

**API:** Básica

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendURLVideo
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
    "body": "https://suite.chatmasterveloz.com/api/video.mp4",
    "caption": "Teste de Caption"
  }
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“body”:** URL do arquivo.

➡️ **“caption”:** legenda exibida junto do arquivo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendURLVideo',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "body": "https://suite.chatmasterveloz.com/api/video.mp4",
    "caption": "Teste de Caption"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendURLVideo' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","body":"https://suite.chatmasterveloz.com/api/video.mp4","caption":"Teste de Caption"}'
```
