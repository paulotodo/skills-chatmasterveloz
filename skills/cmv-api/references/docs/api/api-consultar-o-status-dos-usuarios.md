# API Consultar o Status dos Usuários

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-consultar-o-status-dos-usuarios
- **Categoria:** APIs
- **Menu:** APIs › Equipe › API Consultar o Status dos Usuários

---

🧩 Obter o **status de presença** de cada usuário da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/users/status?usuario={userId}
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
// sem payload — o filtro vai na própria URL
```

➡️ Esta chamada não tem payload — o único filtro vai na própria URL.

◽ **usuario:** o ID ou o e-mail de um usuário da empresa, para trazer só ele. É opcional: sem ele — `api/users/status`, sem o `?usuario=` — vem a equipe inteira, em ordem de nome.

⚠️ **Aqui o usuário vai na query, depois do `?`**

➡️ **Os três status possíveis:**

◽ `online`

◽ `away`

◽ `offline`

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/users/status?usuario={userId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/users/status?usuario={userId}' -H 'Authorization: Bearer {seutokenaqui}'
```
