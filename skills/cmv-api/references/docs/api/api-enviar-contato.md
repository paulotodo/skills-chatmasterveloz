# API Enviar Contato

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-contato
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Enviar Contato

---

🧩 Envia **um cartão de contato** para adicionar ou iniciar uma conversa.

**API:** Básica

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendContact
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
  "body": "Nome do contato",
  "optionList": {
    "phone": "5511888888888",
    "company": "Empresa do contato",
    "address": "Endereço do contato, 999"
  }
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“body”:** nome do contato.

➡️ **“optionList”:** dados extras sobre o contato, sendo que:

◽ `phone`: telefone.

◽ `company`: empresa.

◽ `address`: endereço.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendContact',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
  "number": "5511955892164",
  "body": "Nome do contato",
  "optionList": {
    "phone": "5511888888888",
    "company": "Empresa do contato",
    "address": "Endereço do contato, 999"
  }
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendContact' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","body":"Nome do contato","optionList":{"phone":"5511888888888","company":"Empresa do contato","address":"Endereço do contato, 999"}}'
```
