# API Enviar Imagem por URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-imagem-por-url
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Enviar Imagem por URL

---

🧩 Envia uma **imagem a partir de uma URL**, com opção de legenda.

**API:** Básica

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendURLImage
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
    "body": "https://suite.chatmasterveloz.com/api/image.jpg",
    "mimeType": "image/jpeg",
    "caption": "teste de caption"
  }
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“body”:** URL do arquivo.

➡️ **“mimeType”:** tipo do arquivo no formato MIME — aqui `image/jpeg`.

➡️ **“caption”:** legenda exibida junto do arquivo.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendURLImage',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "body": "https://suite.chatmasterveloz.com/api/image.jpg",
    "mimeType": "image/jpeg",
    "caption": "teste de caption"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendURLImage' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","body":"https://suite.chatmasterveloz.com/api/image.jpg","mimeType":"image/jpeg","caption":"teste de caption"}'
```
