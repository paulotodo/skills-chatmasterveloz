# API Listar Regras da Equipe do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-regras-da-equipe-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de Atendimentos › API Listar Regras da Equipe do Quadro

---

🧩 Obter **as regras da equipe** de um quadro, na ordem em que valem.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras
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

◽ O `quadroId` vai no próprio endereço: é o `id` do quadro.

◽ Cada regra traz `id`, `nome`, `ativo`, `ordem`, `combinacao`, `condicoes`, a `coluna` de destino e o `usuarioIds` — `null` quando vale para todos que usam o quadro.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras' -H 'Authorization: Bearer {seutokenaqui}'
```
