# API Atualizar os Quadros de um Usuário

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-os-quadros-de-um-usuario
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Atualizar os Quadros de um Usuário

---

🧩 Atualiza **os quadros atribuídos a um usuário** — os que ele vê na tela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/usuarios/{userId}
```

##### Método

```
PUT
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "quadroIds": [
        3,
        7
    ]
}
```

➡️ **“userId”:** ID do usuário — vai no próprio endereço, no lugar de `{userId}`.

➡️ **“quadroIds”:** a lista **inteira** dos quadros do usuário, que substitui a anterior. `[]` tira todos.

⚠️ Mande sempre a lista completa: o quadro que ficar de fora deixa de ser do usuário.

◽ A resposta traz os IDs gravados.

◽ Atribuir é do administrador e do supervisor. Para eles mesmos não faz diferença: veem todos os quadros.

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
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "quadroIds": [
        3,
        7
    ]
}',
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/usuarios/{userId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"quadroIds":[3,7]}'
```
