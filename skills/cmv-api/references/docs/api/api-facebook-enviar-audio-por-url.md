# API Facebook Enviar Áudio por URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-facebook-enviar-audio-por-url
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Facebook Enviar Áudio por URL

---

🧩 Envia um **áudio a partir de uma URL** pelo **Facebook Messenger** (conexão nativa ou pelo portal), estando com a Janela de Atendimento ao Cliente **aberta**.

**API:** Facebook

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL
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
    "number": "{facebookId}",
    "type": "audio",
    "body": "https://suite.chatmasterveloz.com/api/audio.mp3"
}
```

➡️ **“number”:** identificador do contato no Facebook — não é telefone.

◽ É o `sender` que chega no webhook da mensagem do contato, o mesmo número que fica gravado no contato (17 dígitos).

➡️ **“type”:** `audio`.

➡️ **“body”:** URL do arquivo.

◽ Aceita áudio **mp3** e **ogg**.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "{facebookId}",
    "type": "audio",
    "body": "https://suite.chatmasterveloz.com/api/audio.mp3"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"{facebookId}","type":"audio","body":"https://suite.chatmasterveloz.com/api/audio.mp3"}'
```
