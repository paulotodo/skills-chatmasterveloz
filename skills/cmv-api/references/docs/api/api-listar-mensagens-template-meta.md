# API Listar Mensagens Template Meta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-mensagens-template-meta
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Listar Mensagens Template Meta

---

🧩 Obter a **lista de templates** da conexão, com filtro opcional por situação e categoria.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/waba-templates?status={statusDoTemplate}&category={category}
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
// sem payload — os filtros vão na própria URL
```

➡️ **“status”:** opcional — `PENDING`, `APPROVED`, `REJECTED`, `PAUSED` ou `DISABLED`.

➡️ **“category”:** opcional — `MARKETING`, `UTILITY` ou `AUTHENTICATION`.

◽ Sem nenhum dos dois, a lista vem completa: basta chamar `https://api2.chatmasterveloz.com/api/waba-templates`.

⚠️ A lista traz **apenas os templates da conexão da chamada** — a dona do token, quando se usa o token da Conexão, ou a informada quando se usa o Token da Empresa.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/waba-templates?status={statusDoTemplate}&category={category}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/waba-templates?status={statusDoTemplate}&category={category}' -H 'Authorization: Bearer {seutokenaqui}'
```
