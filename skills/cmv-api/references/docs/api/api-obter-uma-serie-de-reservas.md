# API Obter uma Série de Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-uma-serie-de-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Obter uma Série de Reservas

---

🧩 Obter **uma série de reservas** pelo id, com todas as reservas dela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/series/{serieId}
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

➡️ Esta chamada não tem payload. O id da série vai no endereço, no lugar de `{serieId}`. É o `serieId` de cada reserva da série.

➡️ **A resposta traz a `serie`** (`id`, `frequencia`, `vezes`, `origem`, `createdAt`), quantas reservas ainda valem em `ativas` (as pendentes e as confirmadas) e todas as `reservas` da série, inclusive as canceladas, na ordem das datas.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/series/{serieId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/series/{serieId}' -H 'Authorization: Bearer {seutokenaqui}'
```
