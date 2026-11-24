# API Contar Empresas

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-contar-empresas
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Empresas › API Contar Empresas

---

🧩 Contar as **empresas da instância**, ativas e inativas.

⚠️ Esta chamada exige o **Token da Empresa** da **empresa do Super Admin**.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/count
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
// sem payload
```

➡️ Esta chamada não tem payload.

◽ A resposta traz só números, sem nome nem dado de nenhuma empresa: `total` (todas as empresas da instância, contando a do Super Admin), `ativas`, `inativas` e `geradoEm` (data e hora do servidor, em UTC).

⚠️ O token de uma **conexão** não serve aqui, nem o de uma conexão da empresa do Super Admin: a resposta é `403`. O mesmo vale para o Token da Empresa de qualquer outra empresa.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/count',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token da Empresa do Super Admin
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X GET 'https://api2.chatmasterveloz.com/api/companies/count' -H 'Authorization: Bearer {seutokenaqui}'
```
