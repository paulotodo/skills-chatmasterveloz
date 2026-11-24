# API Obter Faturas

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-obter-faturas
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Faturas › API Obter Faturas

---

🧩 Obter a **lista de faturas** da sua conta Super Admin.

⚠️ Esta chamada exige um token da **empresa do Super Admin**. Serve tanto o token de uma Conexão dela quanto o **Token da Empresa**, gerado em **Configurações → Token da Empresa**. Token de outra empresa não é aceito.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/invoices/listar
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

```json
{
    "status":"all"
}
```

➡️ **“status”:** filtra as faturas.

◽ `all` — todas.

◽ `open` — não pagas.

◽ `paid` — pagas.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/invoices/listar',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_POSTFIELDS =>'{
    "status":"all" // all: todos, open: não pago, paid: pago
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
curl -X GET 'https://api2.chatmasterveloz.com/api/invoices/listar' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"status":"all"}'
```
