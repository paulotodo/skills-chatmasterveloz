# API Chat Externo Botão Quick Reply

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-chat-externo-botao-quick-reply
- **Categoria:** APIs
- **Menu:** APIs › Botões › API Chat Externo Botão Quick Reply

---

🧩 Envia uma mensagem com **botões de resposta rápida** para o cliente que está na página do **Chat Externo**: o cliente toca e a resposta volta como mensagem dele.

**API:** Chat Externo

##### Endpoint

```
https://api2.chatmasterveloz.com/api/chat-externo/mensagem
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
    "type": "buttons",
    "header": "Agendamento",
    "body": "Podemos confirmar a sua visita amanhã às 10h?",
    "footer": "Toque numa opção",
    "buttons": [
        {
            "id": "confirmar",
            "title": "Confirmar"
        },
        {
            "id": "remarcar",
            "title": "Remarcar"
        }
    ]
}
```

➡️ **“ticketId”:** ID do Ticket. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ É o `chamadoId` que chega no webhook da mensagem do cliente.

➡️ **“type”:** `buttons`. **Obrigatório.**

➡️ **“header”:** título que aparece acima do texto, até 60 caracteres. **Opcional.**

➡️ **“body”:** o texto da mensagem, até 1024 caracteres. Não pode ficar vazio. **Obrigatório.**

➡️ **“footer”:** linha menor abaixo do texto, até 60 caracteres. **Opcional.**

➡️ **“buttons”:** de 1 a 3 botões. **Obrigatório.**

◽ **“id”:** o que volta para a sua integração quando o cliente toca no botão, até 256 caracteres. Não pode repetir.

◽ **“title”:** o texto do botão, até 20 caracteres.

⚠️ Campo acima do limite é recusado, e a resposta diz qual campo corrigir.

◽ Quando o cliente toca num botão, o título dele entra no atendimento como mensagem do cliente e chega no webhook com `"type": "button_reply"` e `interactive` (o `id`, o `title` e o `messageId` da mensagem com os botões).

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/chat-externo/mensagem',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": 700,
    "type": "buttons",
    "header": "Agendamento",
    "body": "Podemos confirmar a sua visita amanhã às 10h?",
    "footer": "Toque numa opção",
    "buttons": [
        {
            "id": "confirmar",
            "title": "Confirmar"
        },
        {
            "id": "remarcar",
            "title": "Remarcar"
        }
    ]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/chat-externo/mensagem' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"type":"buttons","header":"Agendamento","body":"Podemos confirmar a sua visita amanhã às 10h?","footer":"Toque numa opção","buttons":[{"id":"confirmar","title":"Confirmar"},{"id":"remarcar","title":"Remarcar"}]}'
```
