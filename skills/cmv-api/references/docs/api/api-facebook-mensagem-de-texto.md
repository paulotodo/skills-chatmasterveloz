# API Facebook Mensagem de Texto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-facebook-mensagem-de-texto
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Facebook Mensagem de Texto

---

🧩 Envia uma **mensagem de texto** pelo **Facebook Messenger** (conexão nativa ou pelo portal), estando com a Janela de Atendimento ao Cliente **aberta**.

**API:** Facebook

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
    "number": "{facebookId}",
    "ticketId": 700,
    "text": "Olá! Recebemos sua mensagem."
}
```

➡️ **“number”:** identificador do contato no Facebook — não é telefone. **Obrigatório**, mesmo quando o `ticketId` é informado.

◽ É o `sender` que chega no webhook da mensagem do contato, o mesmo número que fica gravado no contato (17 dígitos).

➡️ **“ticketId”:** ID do Ticket. **Opcional** — não substitui o `number`: só escolhe em qual atendimento a mensagem fica gravada.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ Precisa ser um atendimento desta conexão e do contato de `number`. Sem ele, a mensagem vai para o atendimento do contato que está em atendimento ou aguardando nesta conexão; se não houver, para o último atendimento encerrado dele.

◽ Em qualquer caso, o atendimento fica como estava: o envio não encerra a conversa nem muda o Setor.

➡️ **“text”:** texto da mensagem.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

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
    "number": "{facebookId}",
    "ticketId": 700,
    "text": "Olá! Recebemos sua mensagem."
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendOfficialData' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"{facebookId}","ticketId":700,"text":"Olá! Recebemos sua mensagem."}'
```
