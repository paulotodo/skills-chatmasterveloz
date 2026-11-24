# API Listar Respostas Rápidas de uma Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-listar-respostas-rapidas-de-uma-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Respostas Rápidas › API Listar Respostas Rápidas de uma Empresa

---

🧩 Obter as **respostas rápidas de uma empresa**, sem precisar entrar nela.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/quick-messages?companyId={companyId}&queueId={queueId}&userId={userId}&categoria={categoria}&searchParam={searchParam}&pageNumber={pageNumber}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, e todos são opcionais.

◽ **companyId:** a empresa cujas respostas você quer ver. **É ele que faz a chamada valer para outra empresa** — sem ele, vêm as da empresa do próprio token.

◽ **queueId:** só as respostas daquele Setor. **userId:** só as daquele operador.

◽ **categoria:** só as daquela categoria. Com `__sem__`, vêm as que não têm categoria nenhuma.

◽ **searchParam:** procura no atalho, no texto e na categoria, sem diferenciar acentos nem maiúsculas.

◽ **pageNumber:** a página, de **100 em 100**. Padrão `1`.

➡️ **Cada resposta vem com o seu tipo:** `geral`, `fila` ou `individual`.

◽ A lista vem em ordem de atalho.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/quick-messages?companyId={companyId}&queueId={queueId}&userId={userId}&categoria={categoria}&searchParam={searchParam}&pageNumber={pageNumber}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/quick-messages?companyId={companyId}&queueId={queueId}&userId={userId}&categoria={categoria}&searchParam={searchParam}&pageNumber={pageNumber}' -H 'Authorization: Bearer {seutokenaqui}'
```
