# API Obter uma Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-obter-uma-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Empresas › API Obter uma Empresa

---

🧩 Obter o **cadastro de uma empresa**: dados básicos, situação, plano e vencimento.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}
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
// sem payload — a empresa vai no endereço
```

➡️ **“companyId”:** ID da empresa — vai no próprio endereço, no lugar de `{companyId}`. **Obrigatório.**

◽ A resposta traz o nome, o contato, a situação, o plano, o vencimento, os modos de atendimento (híbrido, alternativo e concatenação) e a franquia de voz.

◽ **Não saem** o CSS e o JS personalizados, a chave de armazenamento, o proxy, os iframes nem o token — nada de credencial aparece aqui.

◽ Empresa que não existe responde não encontrada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/companies/{companyId}' -H 'Authorization: Bearer {seutokenaqui}'
```
