# API Oficial Mensagem

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-mensagem
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Oficial Mensagem

---

🧩 Envia uma **mensagem de texto pela API oficial,** estando com a Janela de Atendimento ao Cliente **aberta**.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendOfficialData
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
    "number": "5511955892164",
    "ticketId": 700,
    "text": "Texto API OFICIAL"
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números). **Obrigatório**, mesmo quando o `ticketId` é informado.

➡️ **“ticketId”:** ID do Ticket. **Opcional** — não substitui o `number`: só escolhe em qual atendimento a mensagem fica gravada.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ Precisa ser um atendimento desta conexão e do contato de `number`. Sem ele, a mensagem vai para o atendimento do contato que está em atendimento ou aguardando nesta conexão; se não houver, para o último atendimento encerrado dele.

◽ Em qualquer caso, o atendimento fica como estava: o envio não encerra a conversa nem muda o Setor.

➡️ **“text”:** texto da mensagem.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendOfficialData',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "ticketId": 700,
    "text": "Texto API OFICIAL"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendOfficialData' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","ticketId":700,"text":"Texto API OFICIAL"}'
```
