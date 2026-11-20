# API Listar Respostas Rápidas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-respostas-rapidas
- **Categoria:** APIs
- **Menu:** APIs › Respostas Rápidas › API Listar Respostas Rápidas

---

🧩 Obter as **respostas rápidas** da empresa — todas, de qualquer tipo e de qualquer dono, como o administrador as vê na tela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/quick-messages?queueId={queueId}&userId={userId}&categoria={categoria}&searchParam={searchParam}&pageNumber={pageNumber}
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
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/quick-messages?queueId={queueId}&userId={userId}&categoria={categoria}&searchParam={searchParam}&pageNumber={pageNumber}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/quick-messages?queueId={queueId}&userId={userId}&categoria={categoria}&searchParam={searchParam}&pageNumber={pageNumber}' -H 'Authorization: Bearer {seutokenaqui}'
```
