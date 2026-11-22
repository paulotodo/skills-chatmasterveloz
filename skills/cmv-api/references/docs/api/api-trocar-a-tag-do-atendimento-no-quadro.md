# API Trocar a Tag do Atendimento no Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-trocar-a-tag-do-atendimento-no-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Trocar a Tag do Atendimento no Quadro

---

🧩 Troca **a tag de um atendimento** na visão por tags do quadro, como o arrasto do card de uma tag para outra.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/tickets/{ticketId}/tag?userId={userId}
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
    "quadroId": 3,
    "deTagId": 20,
    "paraTagId": 21
}
```

➡️ **“ticketId”:** ID do Ticket — vai no próprio endereço, no lugar de `{ticketId}`.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

➡️ **“quadroId”:** o quadro da visão por tags. **Obrigatório.**

➡️ **“deTagId”:** a tag que sai — a coluna de onde o card sai. `null` quando o atendimento está em **Sem tag**.

➡️ **“paraTagId”:** a tag que entra. `null` leva o atendimento para **Sem tag**.

◽ Só a tag de `deTagId` sai.

➡️ **“userId”:** quem troca — o ID de um usuário da empresa, no próprio endereço. **Obrigatório.**

◽ Vale o que a pessoa pode fazer com tags na tela, como atribuir e remover.

◽ A resposta traz as tags do atendimento depois da troca: `{"ticketId": 310, "tags": [21], "mudou": true}`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/tickets/{ticketId}/tag?userId={userId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "quadroId": 3,
    "deTagId": 20,
    "paraTagId": 21
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/tickets/{ticketId}/tag?userId={userId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"quadroId":3,"deTagId":20,"paraTagId":21}'
```
