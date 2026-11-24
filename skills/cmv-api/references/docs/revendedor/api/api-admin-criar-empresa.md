# API Criar Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-criar-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Empresas › API Criar Empresa

---

🧩 Criar **uma empresa** na sua instância.

⚠️ Esta chamada exige um token da **empresa do Super Admin**. Serve tanto o token de uma Conexão dela quanto o **Token da Empresa**, gerado em **Configurações → Token da Empresa**. Token de outra empresa não é aceito.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/add
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

```json
{
      "name": "EMPRESA DE TESTE API33",
      "namecomplete": "NOME DO CONTATO",
      "email": "EMAIL33@EMAIL.COM",
      "phone": "5511999999999",
      "pais": "BR",
      "indicator": "INDICADOR DA EMPRESA",
      "planId": "1",
      "status": true,
      "dueDate": "2025/12/20",
      "recurrence": "MENSAL",
      "password": "SENHA DE ACESSO"
}
```

➡️ **“name”:** nome da empresa.

➡️ **“namecomplete”:** nome do contato.

➡️ **“email”:** e-mail de acesso do contato.

➡️ **“phone”:** telefone do contato.

➡️ **“pais”:** sigla do país.

➡️ **“indicator”:** quem indicou a empresa (afiliação).

➡️ **“planId”:** ID do plano.

➡️ **“status”:** `true` ou `false`.

➡️ **“dueDate”:** data de vencimento no formato AAAA/MM/DD.

➡️ **“recurrence”:** período da recorrência.

➡️ **“password”:** senha de acesso.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/add',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
      "name": "EMPRESA DE TESTE API33",
      "namecomplete": "NOME DO CONTATO",
      "email": "EMAIL33@EMAIL.COM",
      "phone": "5511999999999",
      "pais": "BR",
      "indicator": "INDICADOR DA EMPRESA",
      "planId": "1",
      "status": true,
      "dueDate": "2025/12/20",
      "recurrence": "MENSAL",
      "password": "SENHA DE ACESSO"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/companies/add' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"EMPRESA DE TESTE API33","namecomplete":"NOME DO CONTATO","email":"EMAIL33@EMAIL.COM","phone":"5511999999999","pais":"BR","indicator":"INDICADOR DA EMPRESA","planId":"1","status":true,"dueDate":"2025/12/20","recurrence":"MENSAL","password":"SENHA DE ACESSO"}'
```
