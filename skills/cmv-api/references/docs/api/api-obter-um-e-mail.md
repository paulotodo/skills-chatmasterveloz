# API Obter um E-mail

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-um-e-mail
- **Categoria:** APIs
- **Menu:** APIs › E-mail › API Obter um E-mail

---

🧩 Obter **um e-mail específico**, com o texto, o HTML e os dados dos anexos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/email/messages/{emailId}
```

##### Método

```
GET
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```
// sem payload
```

➡️ Esta chamada não tem payload.

➡️ **“emailId”:** ID do e-mail — vai no próprio endereço, no lugar de `{emailId}`. **Obrigatório.**

◽ O ID vem na lista de e-mails, no campo `id`.

◽ A resposta traz o `id`, a conta, a pasta, o `tipo` (`recebido` ou `enviado`), quem enviou, para quem, o assunto, se tem anexo, se foi lido e a data, e mais o `text`, o `html` e os `attachments`.

◽ **“html”:** vem nulo quando o e-mail é só texto.

◽ **“attachments”:** os dados de cada anexo: `filename`, `contentType` e `size`. O arquivo não vem na resposta.

◽ E-mail inexistente responde `ERR_EMAIL_MESSAGE_NOT_FOUND`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/email/messages/{emailId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/email/messages/{emailId}' -H 'Authorization: Bearer {seutokenaqui}'
```
