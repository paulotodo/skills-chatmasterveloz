# API Instagram Enviar Documento por URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-instagram-enviar-documento-por-url
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Instagram Enviar Documento por URL

---

🧩 Envia um **documento a partir de uma URL** pelo **Instagram Direct** (conexão nativa ou pelo portal), estando com a Janela de Atendimento ao Cliente **aberta**.

**API:** Instagram

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
    "number": "{instagramId}",
    "type": "document",
    "caption": "Aqui vai minha legenda",
    "fileName": "algumnome.pdf",
    "body": "https://suite.chatmasterveloz.com/api/document.pdf"
}
```

➡️ **“number”:** identificador do contato no Instagram — não é telefone.

◽ É o `sender` que chega no webhook da mensagem do contato, o mesmo número que fica gravado no contato (15 dígitos).

➡️ **“type”:** `document`.

➡️ **“caption”:** legenda. Chega ao contato como uma mensagem de texto, logo depois do arquivo.

➡️ **“fileName”:** nome do arquivo que o contato vê.

➡️ **“body”:** URL do arquivo.

◽ O Instagram aceita **PDF**. Outros documentos, como `.docx`, são recusados com **400** `ERR_IG_ANEXO_NAO_SUPORTADO`.

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
    "number": "{instagramId}",
    "type": "document",
    "caption": "Aqui vai minha legenda",
    "fileName": "algumnome.pdf",
    "body": "https://suite.chatmasterveloz.com/api/document.pdf"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/official/sendMediaByURL' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"{instagramId}","type":"document","caption":"Aqui vai minha legenda","fileName":"algumnome.pdf","body":"https://suite.chatmasterveloz.com/api/document.pdf"}'
```
