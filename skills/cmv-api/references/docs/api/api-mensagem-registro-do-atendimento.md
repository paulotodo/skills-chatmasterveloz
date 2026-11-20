# API Mensagem Registro do Atendimento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-mensagem-registro-do-atendimento
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Mensagem Registro do Atendimento

---

🧩 Grava uma linha no **Registro do atendimento** — o mesmo em que a tela conta que alguém aceitou ou transferiu o atendimento.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/{ticketId}/registro
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
    "body": "emitiu a nota fiscal 123",
    "userId": 31
}
```

➡️ **“ticketId”:** ID do Ticket — vai no próprio endereço, no lugar de `{ticketId}`. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

➡️ **“body”:** o texto da linha. **Obrigatório.**

➡️ **“userId”:** ID do usuário que fica como autor da linha. Opcional.

⚠️ **Com o `userId`, o nome entra na frente do texto** — como nas linhas que a própria tela escreve. O `body` `emitiu a nota fiscal 123`, com a Maria, vira **Maria emitiu a nota fiscal 123**. Escreva o texto como a continuação de um nome. Sem o `userId`, a linha sai exatamente como você mandou.

◽ Serve para a integração contar o que ela fez: a nota emitida, a entrega agendada, o pedido faturado.

⚠️ **Nada disso chega ao cliente.** A linha é interna, e também não é a mensagem interna que a equipe troca dentro do atendimento.

◽ A linha é gravada com a opção de registrar os logs de ação ligada ou desligada — ela vale para as linhas automáticas, não para esta.

◽ Ticket encerrado também recebe a linha, e o ticket não muda de estado por causa dela.

⚠️ **A última mensagem do ticket passa a ser “AÇÃO EXECUTADA”** na lista de atendimentos, como acontece com qualquer linha do Registro.

◽ Ticket que não existe, ou de outra empresa, responde `404`. `body` vazio e `userId` de outra empresa respondem `400`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/{ticketId}/registro',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "body": "emitiu a nota fiscal 123",
    "userId": 31
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/{ticketId}/registro' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"body":"emitiu a nota fiscal 123","userId":31}'
```
