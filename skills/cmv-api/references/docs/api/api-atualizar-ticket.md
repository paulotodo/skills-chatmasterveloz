# API Atualizar Ticket

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-ticket
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Atualizar Ticket

---

🧩 Atualiza **um ticket**, alterando seu status, Setor, atendente ou campos personalizados.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/updateAPI
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
    "ticketId": "1067",
    "status": "pending",
    "userId": "13",
    "queueId": "34",
    "typebot_sessionId": "CAMPO LIVRE LETRAS E NÚMEROS",
    "customA": "CAMPO LIVRE LETRAS E NÚMEROS",
    "customB": "CAMPO LIVRE LETRAS E NÚMEROS",
    "customC": {"origem": "site"},
    "customD": {"pedido": 4471}
}
```

➡️ **“ticketId”:** ID do Ticket.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ Só muda o que vier no payload; o que ficar de fora continua como está.

➡️ **“status”:** `open`, `pending` ou `closed`.

◽ Num ticket já encerrado, mandar `closed` de novo, ou só o `ticketId`, não abre protocolo novo.

➡️ **“userId”:** ID do atendente, ou `null`.

➡️ **“queueId”:** ID do Setor, ou `null`.

◽ A troca de Setor é avisada no webhook da Conexão, com `origemDoEvento: "api"`, e no webhook do Setor novo.

➡️ **“typebot_sessionId”:** ID da sessão do Typebot. Campo livre, letras e números.

➡️ **“customA”:** informação livre A.

➡️ **“customB”:** informação livre B.

➡️ **“customC”:** informação livre C, em JSON.

➡️ **“customD”:** informação livre D, em JSON.

➡️ **“retornoAoAtendente”:** `true` ou `false`, só no encerramento, com `"status": "closed"`. `true` liga o retorno ao mesmo atendente neste encerramento, mesmo com a opção desligada no Setor: se o cliente responder dentro do prazo, o ticket volta como `open` para o mesmo atendente. `false` encerra sem o retorno, e a resposta do cliente segue o caminho de sempre de um ticket encerrado.

➡️ **“minutosDoRetorno”:** só no encerramento. O prazo, em minutos, para a resposta do cliente trazer o ticket de volta ao mesmo atendente, de 1 a 10080 (7 dias). Vale para este encerramento, no lugar do prazo do Setor.

➡️ **“setorDeTransbordoId”:** só no encerramento. ID do Setor de transbordo: se o cliente responder dentro do prazo com o atendente offline, o ticket vai para este Setor, como `pending` e sem atendente.

◽ O que não vier na chamada segue a opção **Retornar ao mesmo atendente** do Setor do ticket.

◽ Valor fora do aceito é recusado, e nada muda no ticket: minutos fora de 1 a 10080, `retornoAoAtendente` que não seja `true` ou `false`, ou um Setor de transbordo que não existe.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/updateAPI',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": "1067",
    "status": "pending",
    "userId": "13",
    "queueId": "34",
    "typebot_sessionId": "",
    "customA": "",
    "customB": "",
    "customC": {"origem": "site"},
    "customD": {"pedido": 4471}
}',
  // "status": open, pending ou closed
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/updateAPI' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":"1067","status":"pending","userId":"13","queueId":"34","typebot_sessionId":"CAMPO LIVRE LETRAS E NÚMEROS","customA":"CAMPO LIVRE LETRAS E NÚMEROS","customB":"CAMPO LIVRE LETRAS E NÚMEROS","customC":{"origem":"site"},"customD":{"pedido":4471}}'
```
