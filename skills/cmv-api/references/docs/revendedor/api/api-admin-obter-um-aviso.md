# API Obter um Aviso

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-obter-um-aviso
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Avisos › API Obter um Aviso

---

🧩 Obter **um aviso** pelo id.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/announcements/show?id={avisoId}
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
// sem payload — o id vai na própria URL
```

➡️ **“id”:** ID do aviso, na query da URL. **Obrigatório.**

◽ Vale para aviso de qualquer empresa.

◽ Para clientes que mandam corpo em GET, o `id` também é aceito no corpo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/announcements/show?id={avisoId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/announcements/show?id={avisoId}' -H 'Authorization: Bearer {seutokenaqui}'
```
