# API Listar Tags da Empresa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-tags-da-empresa
- **Categoria:** APIs
- **Menu:** APIs › Tags › API Listar Tags da Empresa

---

🧩 Listar **Tags** de uma empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tags?todas={todas}&tipo={tipoDaTag}
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

➡️ Esta chamada não tem payload — os dois filtros vão na própria URL.

◽ **todas:** `1` traz também as tags inativas. Sem ele, só as ativas.

◽ **tipo:** traz só um tipo — `Atendimento`, `Encerramento` ou `CRM`. Maiúsculas não importam, e um tipo inventado é recusado.

◽ Sem os dois, vêm todas as tags ativas da empresa, em ordem de nome.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tags?todas={todas}&tipo={tipoDaTag}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/tags?todas={todas}&tipo={tipoDaTag}' -H 'Authorization: Bearer {seutokenaqui}'
```
