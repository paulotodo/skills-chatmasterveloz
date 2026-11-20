# API Criar Ticket

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-ticket
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Criar Ticket

---

🧩 Cria **um ticket**, para iniciar uma conversa com um cliente.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/createTicketAPI
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
    "contactId": 9580
}
```

➡️ **“contactId”:** ID do contato cadastrado na plataforma.

◽ Se o contato **não** tiver ticket nesta conexão, abre um ticket em **Aguardando**, sem Setor.

◽ Se o contato **já** tiver ticket nesta conexão, a chamada devolve **esse** ticket, sem criar outro e sem mudar o status dele.

⚠️ Numa Conexão de **Chat Externo**, o ticket só nasce pela página, onde o cliente está: a chamada responde `400` com `ERR_CHAT_EXTERNO_SO_PELA_PAGINA`, e nada é criado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/createTicketAPI',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "contactId": 9580
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/createTicketAPI' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"contactId":9580}'
```
