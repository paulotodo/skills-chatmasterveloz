# API Listar Tickets do Contato

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-tickets-do-contato
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Listar Tickets do Contato

---

🧩 Listar **todos os tickets de um contato**, em todas as conexões. Lembre-se de que um ticket é uma conversa entre um contato e uma conexão.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/contacts/alltickets
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
    "number":"5511955892164"
}
```

➡️ **“number”:** telefone do contato no formato ddi ddd numero (somente números).

◽ O número precisa ter a **mesma quantidade de dígitos** que está cadastrada na plataforma.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/contacts/alltickets',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_POSTFIELDS =>'{
    "number":"5511955892164"
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
curl -X GET 'https://api2.chatmasterveloz.com/api/contacts/alltickets' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164"}'
```
