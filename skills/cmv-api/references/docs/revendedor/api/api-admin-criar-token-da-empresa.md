# API Criar Token da Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-criar-token-da-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Empresas › API Criar Token da Empresa

---

🧩 Gera o **Token da Empresa** de uma empresa — a credencial única com que ela fala com a API por qualquer conexão dela.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}/api-token
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
    "trocar": true
}
```

➡️ **“companyId”:** ID da empresa — vai no próprio endereço, no lugar de `{companyId}`. **Obrigatório.**

➡️ **“trocar”:** `true` substitui o token que a empresa já tem.

⚠️ **O token volta inteiro, e só desta vez.** Guarde-o na hora: nenhuma outra chamada mostra o token completo depois.

⚠️ **Empresa que já tem token é recusada**, de propósito, para ninguém trocar sem querer. É aí que entra o `trocar`.

⚠️ **Trocar derruba o token antigo na hora**, em toda integração que estiver usando ele.

◽ Com esse token a empresa precisa dizer a conexão em cada chamada — pelo `whatsappId`, `connectionId` ou `whatsappName` —, menos nas que só aceitam este token, que vão sem conexão.

◽ O Super Admin alcança qualquer empresa, inclusive a dele. Empresa que não existe responde `404`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}/api-token',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "trocar": true
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
curl -X POST 'https://api2.chatmasterveloz.com/api/companies/{companyId}/api-token' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"trocar":true}'
```
