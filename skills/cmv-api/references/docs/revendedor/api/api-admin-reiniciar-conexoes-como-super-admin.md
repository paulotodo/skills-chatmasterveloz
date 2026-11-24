# API Reiniciar Conexões como Super Admin

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-reiniciar-conexoes-como-super-admin
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Conexões › API Reiniciar Conexões como Super Admin

---

🧩 Reiniciar as **conexões de toda a instância** da sua conta Super Admin.

⚠️ Esta chamada exige um token da **empresa do Super Admin**. Serve tanto o token de uma Conexão dela quanto o **Token da Empresa**, gerado em **Configurações → Token da Empresa**. Token de outra empresa não é aceito.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/application/restart
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

```
// sem payload
```

➡️ Esta chamada não tem payload.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/application/restart',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/application/restart' -H 'Authorization: Bearer {seutokenaqui}'
```
