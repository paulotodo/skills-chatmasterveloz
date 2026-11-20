# API Listar Origens de Venda

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-origens-de-venda
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Listar Origens de Venda

---

🧩 Listar as **origens de venda** cadastradas — de onde o negócio surgiu.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/crm/v2/origens
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
// sem payload
```

➡️ Esta chamada não tem payload.

◽ Use o id em `origemVendaId` ao criar ou ao alterar uma oportunidade.

◽ Vêm só as origens ativas, na ordem do cadastro.

⚠️ **A empresa precisa estar com o CRM novo ativado.**

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/crm/v2/origens',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/crm/v2/origens' -H 'Authorization: Bearer {seutokenaqui}'
```
