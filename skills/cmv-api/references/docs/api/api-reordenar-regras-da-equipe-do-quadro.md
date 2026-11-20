# API Reordenar Regras da Equipe do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-reordenar-regras-da-equipe-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de Atendimentos › API Reordenar Regras da Equipe do Quadro

---

🧩 Reordena **as regras da equipe** de um quadro: a primeira que combinar é a que vale.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras/ordem
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
    "ordem": [
        12,
        3,
        4
    ]
}
```

➡️ **“quadroId”:** ID do quadro — vai no próprio endereço, no lugar de `{quadroId}`.

➡️ **“ordem”:** os IDs de **todas** as regras da equipe deste quadro, na ordem nova.

◽ A resposta traz as regras na ordem nova.

◽ É do administrador e do supervisor.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras/ordem',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "ordem": [
        12,
        3,
        4
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras/ordem' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ordem":[12,3,4]}'
```
