# API WebChat Botão Quick Reply

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-webchat-botao-quick-reply
- **Categoria:** APIs
- **Menu:** APIs › Botões › API WebChat Botão Quick Reply

---

🧩 Envia uma mensagem com **botões de resposta rápida** para o visitante do **WebChat**, no chat do site: o visitante toca e a resposta volta como mensagem dele.

**API:** WebChat

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
    "number": "session_1745772400000_abc123",
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

➡️ **“number”:** o **sessionId** do visitante, o identificador da sessão dele no widget. É gerado pelo widget e pode ser obtido via webhook, pela mensagem-marcador do ticket ou pela página de visitantes ao vivo. Sem o `number`, informe o `ticketId`.

◽ O visitante precisa já ter aberto o chat do site: a chamada não começa conversa.

◽ O `number` é procurado entre os contatos do canal da Conexão. Um `number` que esse canal não conhece é recusado, e o de um contato de outro canal também — o telefone de um contato do WhatsApp, por exemplo.

➡️ **“ticketId”:** ID do Ticket, no lugar do `number`.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

➡️ **“header”:** título que aparece acima do texto, até 60 caracteres. **Opcional.**

➡️ **“body”:** o texto da mensagem, até 1024 caracteres. Não pode ficar vazio. **Obrigatório.**

➡️ **“footer”:** linha menor abaixo do texto, até 60 caracteres. **Opcional.**

➡️ **“buttons”:** de 1 a 3 botões. **Obrigatório.**

◽ **“id”:** o que volta para a sua integração quando o visitante toca no botão, até 256 caracteres. Não pode repetir.

◽ **“title”:** o texto do botão, até 20 caracteres.

⚠️ Campo acima do limite ou faltando é recusado, e a resposta diz qual campo corrigir.

◽ Quando o visitante toca num botão, o título dele entra no atendimento como mensagem do cliente e chega no webhook da conexão com o `id` do botão em `postback`. Com um fluxo rodando no atendimento, o toque é a resposta do bloco que está esperando.

◽ Só a última mensagem com opções aceita o toque: as opções das mensagens anteriores ficam desativadas no chat do site, e o toque numa delas é recusado.

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
    "number": "session_1745772400000_abc123",
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/channels/sendButtons' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"session_1745772400000_abc123","header":"Agendamento","body":"Podemos confirmar a sua visita amanhã às 10h?","footer":"Toque numa opção","buttons":[{"id":"confirmar","title":"Confirmar"},{"id":"remarcar","title":"Remarcar"}]}'
```
