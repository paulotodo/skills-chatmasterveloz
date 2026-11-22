# API Fixar Atendimento no Topo da Coluna

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-fixar-atendimento-no-topo-da-coluna
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Fixar Atendimento no Topo da Coluna

---

🧩 Fixa **um atendimento no topo da coluna**, ou solta, como a estrela do card na tela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/tickets/{ticketId}/fixar?userId={userId}
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

```
// sem payload
```

➡️ Esta chamada não tem payload.

◽ O `ticketId` vai no próprio endereço: é o ID do Ticket.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ O `userId` é obrigatório: a estrela é da pessoa, não do quadro — cada um fixa os seus.

◽ Cada chamada inverte: o fixado fica solto, e o solto fica fixado. A resposta diz como ficou: `{"fixado": true}` ou `{"fixado": false}`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/tickets/{ticketId}/fixar?userId={userId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/tickets/{ticketId}/fixar?userId={userId}' -H 'Authorization: Bearer {seutokenaqui}'
```
