# API Listar Usuários do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-usuarios-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de Atendimentos › API Listar Usuários do Quadro

---

🧩 Obter **a lista de quem usa um quadro**: as pessoas que têm o quadro atribuído.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/usuarios
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

◽ Cada pessoa traz o `id` e o `name`.

◽ Administrador e supervisor não entram na lista: eles veem todos os quadros, sem atribuição.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/usuarios',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/usuarios' -H 'Authorization: Bearer {seutokenaqui}'
```
