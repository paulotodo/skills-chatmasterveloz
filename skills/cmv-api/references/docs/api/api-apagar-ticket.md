# API Apagar Ticket

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-apagar-ticket
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Apagar Ticket

---

🧩 Apaga um **atendimento inteiro**, com as mensagens.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/{ticketId}
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
// sem payload — o ticketId vai no endereço
```

➡️ **“ticketId”:** ID do Ticket — vai no próprio endereço, no lugar de `{ticketId}`. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ Antes de apagar, o atendimento é encerrado — é o que tira a linha das telas que estão abertas.

⚠️ **Não há como desfazer.** As mensagens do atendimento são apagadas junto, e não existe lixeira.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/{ticketId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/tickets/{ticketId}' -H 'Authorization: Bearer {seutokenaqui}'
```
