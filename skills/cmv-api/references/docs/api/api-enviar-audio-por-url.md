# API Enviar Áudio por URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-audio-por-url
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Enviar Áudio por URL

---

🧩 Envia um **áudio a partir de uma URL**.

**API:** Básica

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendURLAudio
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
    "body": "https://suite.chatmasterveloz.com/api/audio.mp3",
    "mimeType": "audio/mpeg",
    "fileName": "audio.mp3",
    "ptt": true
  }
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“body”:** URL do arquivo.

➡️ **“fileName”:** nome do arquivo que o cliente vê.

➡️ **“mimeType”:** tipo do arquivo no formato MIME — aqui `audio/mpeg`.

➡️ **“ptt”:** `true` para o áudio chegar como mensagem de voz.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendURLAudio',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "body": "https://suite.chatmasterveloz.com/api/audio.mp3",
    "mimeType": "audio/mpeg",
    "fileName": "audio.mp3",
    "ptt": true
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendURLAudio' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","body":"https://suite.chatmasterveloz.com/api/audio.mp3","mimeType":"audio/mpeg","fileName":"audio.mp3","ptt":true}'
```
