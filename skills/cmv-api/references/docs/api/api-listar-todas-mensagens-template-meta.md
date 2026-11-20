# API Listar Todas Mensagens Template Meta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-todas-mensagens-template-meta
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Listar Todas Mensagens Template Meta

---

🧩 Listar **todas Mensagens Templates cadastradas na META**.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/whatsapptemplates
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

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/whatsapptemplates',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/whatsapptemplates' -H 'Authorization: Bearer {seutokenaqui}'
```
