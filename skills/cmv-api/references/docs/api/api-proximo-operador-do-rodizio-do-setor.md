# API Próximo Operador do Rodízio do Setor

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-proximo-operador-do-rodizio-do-setor
- **Categoria:** APIs
- **Menu:** APIs › Rodízios › API Próximo Operador do Rodízio do Setor

---

🧩 Descobrir **de quem é a vez** no rodízio de um Setor.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/queues/{queueId}/next-user
```

##### Método

```
POST
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "avancar": false
}
```

➡️ **“queueId”:** ID do Setor — vai no próprio endereço, no lugar de `{queueId}`. **Obrigatório.**

➡️ **“avancar”:** `false` apenas **espia** quem seria o próximo, sem gastar a vez. Sem este campo, a vez é consumida.

◽ Setor sem ninguém disponível **não é erro**: a resposta vem sem operador e com o motivo — ninguém no Setor, ou ninguém online.

◽ A chamada responde mesmo com o rodízio desligado no Setor; a resposta informa se ele está ligado.

◽ A vez que esta chamada consome é a mesma do rodízio automático: o escolhido passa a ser "o último a receber" também para ele.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/queues/{queueId}/next-user',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "avancar": false
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
curl -X POST 'https://api2.chatmasterveloz.com/api/queues/{queueId}/next-user' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"avancar":false}'
```
