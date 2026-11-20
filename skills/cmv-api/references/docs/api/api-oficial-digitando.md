# API Oficial Digitando

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-digitando
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Oficial Digitando

---

🧩 Altera o status para **Digitando...** por 25 segundos ou até que uma mensagem seja enviada.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/typing
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
    "ticketId": 700,
    "status": "on"
}
```

➡️ **“ticketId”:** o atendimento. Informe este ou o `number`.

➡️ **“number”:** o número do cliente. Informe este ou o `ticketId`.

➡️ **“status”:** `on` **Obrigatório.**

⚠️ **Ligar o indicador marca como lida** a última mensagem do cliente — ela fica com o visto azul.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/typing',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": 700,
    "status": "on"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/typing' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"status":"on"}'
```
