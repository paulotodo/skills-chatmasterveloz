# API Instagram Botão Quick Reply

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-instagram-botao-quick-reply
- **Categoria:** APIs
- **Menu:** APIs › Botões › API Instagram Botão Quick Reply

---

🧩 Envia uma mensagem com **botões de resposta rápida** pelo **Instagram Direct** (conexão nativa), estando com a Janela de Atendimento ao Cliente **aberta**.

**API:** Instagram

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/channels/sendButtons
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
    "number": "{instagramId}",
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

➡️ **“number”:** identificador do contato no Instagram — não é telefone. Sem o `number`, informe o `ticketId`.

◽ É o `sender` que chega no webhook da mensagem do contato, o mesmo número que fica gravado no contato (15 dígitos).

◽ O contato precisa já ter escrito para a sua conta no Instagram: a chamada não começa conversa.

◽ O `number` é procurado entre os contatos do canal da Conexão. Um `number` que esse canal não conhece é recusado, e o de um contato de outro canal também — o telefone de um contato do WhatsApp, por exemplo.

⚠️ Passadas **24 horas** da última mensagem do contato, a chamada é recusada e nada é enviado: daí até 7 dias, o Instagram só aceita a resposta digitada pelo atendente na conversa.

➡️ **“ticketId”:** ID do Ticket, no lugar do `number`.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

➡️ **“header”:** linha que vai acima do texto, até 60 caracteres. **Opcional.**

➡️ **“body”:** o texto da mensagem, até 1024 caracteres. Não pode ficar vazio. **Obrigatório.**

➡️ **“footer”:** linha que vai abaixo do texto, até 60 caracteres. **Opcional.**

➡️ **“buttons”:** de 1 a 3 botões. **Obrigatório.**

◽ **“id”:** o que volta para a sua integração quando o contato toca no botão, até 256 caracteres. Não pode repetir.

◽ **“title”:** o texto do botão, até 20 caracteres.

◽ No Instagram, os botões chegam como respostas rápidas do próprio Instagram: opções que o contato toca para responder.

◽ Só a última mensagem fica com as opções tocáveis; nas anteriores, elas deixam de responder ao toque. É como o Instagram funciona — mande uma pergunta por vez.

⚠️ Campo acima do limite ou faltando é recusado, e a resposta diz qual campo corrigir.

◽ Quando o contato toca num botão, o título dele entra no atendimento como mensagem do cliente e chega no webhook da conexão com o `id` do botão em `postback` (e em `button.payload`).

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/channels/sendButtons',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "{instagramId}",
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/channels/sendButtons' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"{instagramId}","header":"Agendamento","body":"Podemos confirmar a sua visita amanhã às 10h?","footer":"Toque numa opção","buttons":[{"id":"confirmar","title":"Confirmar"},{"id":"remarcar","title":"Remarcar"}]}'
```
