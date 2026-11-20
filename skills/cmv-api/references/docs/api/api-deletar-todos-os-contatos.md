# API Deletar TODOS os Contatos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-todos-os-contatos
- **Categoria:** APIs
- **Menu:** APIs › Contatos › API Deletar TODOS os Contatos

---

🧩 Apaga **todos os contatos** da sua empresa.

⚠️ **Faça por sua conta e risco, e de preferência fora do horário comercial.** A chamada precisa ser repetida quantas vezes forem necessárias até que todos sejam excluídos, e o processo pode levar horas, dependendo da quantidade de mensagens e tickets.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/contacts-delete
```

##### Método

```
DELETE
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```
// sem payload
```

➡️ Esta chamada não tem payload. Repita a chamada até que todos os contatos tenham sido apagados.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/contacts-delete',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X DELETE 'https://api2.chatmasterveloz.com/contacts-delete' -H 'Authorization: Bearer {seutokenaqui}'
```
