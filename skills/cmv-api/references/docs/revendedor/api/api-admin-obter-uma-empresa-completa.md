# API Obter uma Empresa (completa)

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-obter-uma-empresa-completa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Empresas › API Obter uma Empresa (completa)

---

🧩 Obter **uma empresa** específica, com o cadastro completo.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies
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
    "id":"9"
}
```

➡️ **“id”:** ID da empresa.

◽ Repare que é um `GET` que lê o alvo no **corpo**, e não na URL. Mande o corpo mesmo assim, com `Content-Type: application/json`.

⚠️ **A resposta traz a empresa inteira, incluindo o Token da Empresa** (`apiToken`), o CSS e o JavaScript personalizados e os dados do proxy. É credencial em trânsito: não guarde essa resposta em log nem a exiba em tela.

◽ Sem o `id`, ou com empresa que não existe, a resposta é não encontrada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_POSTFIELDS =>'{
    "id":"9"
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
curl -X GET 'https://api2.chatmasterveloz.com/api/companies' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"id":"9"}'
```
