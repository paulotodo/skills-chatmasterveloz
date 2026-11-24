# API Desbloquear Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-desbloquear-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Empresas › API Desbloquear Empresa

---

🧩 Reativa **uma empresa bloqueada**.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}/unblock
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
// sem payload — a empresa vai no endereço
```

➡️ **“companyId”:** ID da empresa — vai no próprio endereço, no lugar de `{companyId}`. **Obrigatório.**

◽ A empresa volta a ser processada pela fila de atendimentos, e as sessões de WhatsApp voltam a subir.

◽ **Não mexe em fatura nem em plano.**

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}/unblock',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/companies/{companyId}/unblock' -H 'Authorization: Bearer {seutokenaqui}'
```
