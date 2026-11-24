# API Listar Avisos

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-listar-avisos
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Avisos › API Listar Avisos

---

🧩 Listar os **avisos da plataforma** — o comunicado que aparece no sino do painel.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/announcements?searchParam={searchParam}&pageNumber={pageNumber}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL.

◽ **“searchParam”:** procura um trecho no título, sem diferenciar maiúsculas.

◽ **“pageNumber”:** página, a partir de 1. São **20 avisos por página**.

◽ Vêm **todos** os avisos: os globais e os de qualquer empresa, do mais recente para o mais antigo, cada um com quem o criou.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/announcements?searchParam={searchParam}&pageNumber={pageNumber}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/announcements?searchParam={searchParam}&pageNumber={pageNumber}' -H 'Authorization: Bearer {seutokenaqui}'
```
