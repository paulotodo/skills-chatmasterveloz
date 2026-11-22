# API Obter os Quadros de um Usuário

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-os-quadros-de-um-usuario
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Obter os Quadros de um Usuário

---

🧩 Obter **os quadros atribuídos a um usuário**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/usuarios/{userId}
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

◽ O `userId` vai no próprio endereço: é o ID do usuário cujos quadros você quer ver.

◽ A resposta é a lista dos IDs dos quadros, como `[3, 7]`. Vazia, o usuário não tem quadro atribuído.

◽ Administrador e supervisor vêm com a lista vazia: eles veem todos os quadros, sem atribuição.

◽ A consulta é do administrador e do supervisor.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/usuarios/{userId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/ticket-quadros/usuarios/{userId}' -H 'Authorization: Bearer {seutokenaqui}'
```
