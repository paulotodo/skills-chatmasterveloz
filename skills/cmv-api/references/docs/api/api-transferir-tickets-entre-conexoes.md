# API Transferir Tickets entre Conexões

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-transferir-tickets-entre-conexoes
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Transferir Tickets entre Conexões

---

🧩 Transfere **todos os tickets de uma conexão** para outra.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/changeconnection
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
    "OLD_connectionId":158,
    "NEW_connectionId":159
  }
```

➡️ **“OLD_connectionId”:** ID da conexão que entrega os tickets. **Obrigatório.**

➡️ **“NEW_connectionId”:** ID da conexão que recebe os tickets. **Obrigatório.**

◽ A resposta diz quantos tickets foram migrados e quantos foram pulados.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/changeconnection',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "OLD_connectionId":158,
    "NEW_connectionId":159
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/changeconnection' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"OLD_connectionId":158,"NEW_connectionId":159}'
```
