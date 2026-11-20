# API Listar Figurinhas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-figurinhas
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Listar Figurinhas

---

🧩 Listar a **biblioteca de figurinhas** da empresa, com as pastas e o ID de cada figurinha.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/figurinhas
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

◽ A resposta traz as pastas cadastradas na tela **Figurinhas** e, dentro de cada uma, as figurinhas com o `id` que o envio usa.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/figurinhas',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/figurinhas' -H 'Authorization: Bearer {seutokenaqui}'
```
