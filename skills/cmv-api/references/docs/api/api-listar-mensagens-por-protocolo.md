# API Listar Mensagens por Protocolo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-mensagens-por-protocolo
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Listar Mensagens por Protocolo

---

🧩 Listar **todas as mensagens** de um protocolo.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/messages/{protocol}
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

```javascript
{
    "protocol":"6126"
}
```

➡️ **“protocol”:** ID do protocolo — o número entra no fim do endereço, como em `/api/tickets/messages/6126`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/messages/6126',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_POSTFIELDS =>'{
    "protocol":"6126"
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
curl -X GET 'https://api2.chatmasterveloz.com/api/tickets/messages/{protocol}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"protocol":"6126"}'
```
