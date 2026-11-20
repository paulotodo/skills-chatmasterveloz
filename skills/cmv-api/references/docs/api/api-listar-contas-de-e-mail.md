# API Listar Contas de E-mail

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-contas-de-e-mail
- **Categoria:** APIs
- **Menu:** APIs › E-mail › API Listar Contas de E-mail

---

🧩 Obter a **lista de contas de e-mail** da sua empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/email/accounts
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

◽ Cada conta vem com o **id**, o nome, o endereço de e-mail e se está ativa.

◽ É deste `id` que o `accountId` do envio de e-mail precisa. Sem `accountId`, o envio usa a **primeira conta ativa** desta lista.

◽ Servidor, usuário e senha das contas não vêm na resposta.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/email/accounts',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/email/accounts' -H 'Authorization: Bearer {seutokenaqui}'
```
