# API Reordenar Regras Pessoais do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-reordenar-regras-pessoais-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de Atendimentos › API Reordenar Regras Pessoais do Quadro

---

🧩 Reordena **as regras pessoais** de uma pessoa: a primeira que combinar é a que vale.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/regras/ordem?userId={userId}
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
        10,
        9,
        6
    ]
}
```

➡️ **“userId”:** a dona das regras — o ID de um usuário da empresa, no próprio endereço. **Obrigatório.**

➡️ **“ordem”:** os IDs de **todas** as regras pessoais da pessoa, na ordem nova. **Obrigatório.**

⚠️ Lista sem alguma das regras da pessoa é recusada.

◽ As regras da equipe continuam valendo antes das pessoais.

◽ A resposta traz as regras na ordem nova.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras/ordem?userId={userId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "ordem": [
        10,
        9,
        6
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras/ordem?userId={userId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ordem":[10,9,6]}'
```
