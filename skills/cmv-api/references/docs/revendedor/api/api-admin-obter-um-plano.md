# API Obter um Plano

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-obter-um-plano
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Planos › API Obter um Plano

---

🧩 Obter **um plano específico**, com todos os campos dele.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/plans/{planId}
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
// sem payload — o plano vai no endereço
```

➡️ **“planId”:** ID do plano — vai no próprio endereço, no lugar de `{planId}`. **Obrigatório.**

➡️ Esta chamada não tem payload.

◽ A resposta traz os mesmos campos da lista de planos: limites, teto por grupo de canal, valor e módulos.

◽ Plano que não existe responde `404`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/plans/{planId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/plans/{planId}' -H 'Authorization: Bearer {seutokenaqui}'
```
