# API Facebook Mensagem de Lista

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-facebook-mensagem-de-lista
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Facebook Mensagem de Lista

---

🧩 Envia uma **mensagem com uma Lista de opções** pelo **Facebook Messenger** (conexão nativa), estando com a Janela de Atendimento ao Cliente **aberta**.

**API:** Facebook

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/channels/sendList
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
    "header": "Cardápio",
    "body": "Escolha o seu pedido:",
    "footer": "Entrega em 40 minutos",
    "buttonText": "Ver opções",
    "sections": [
        {
            "title": "Pizzas",
            "rows": [
                {
                    "id": "pz-mussarela",
                    "title": "Mussarela",
                    "description": "Molho, mussarela e orégano"
                },
                {
                    "id": "pz-calabresa",
                    "title": "Calabresa"
                }
            ]
        }
    ]
}
```

➡️ **“number”:** identificador do contato no Facebook — não é telefone. Sem o `number`, informe o `ticketId`.

◽ É o `sender` que chega no webhook da mensagem do contato, o mesmo número que fica gravado no contato (17 dígitos).

◽ O contato precisa já ter escrito para a sua conta no Messenger: a chamada não começa conversa.

◽ O `number` é procurado entre os contatos do canal da Conexão. Um `number` que esse canal não conhece é recusado, e o de um contato de outro canal também — o telefone de um contato do WhatsApp, por exemplo.

⚠️ Passadas **24 horas** da última mensagem do contato, a chamada é recusada e nada é enviado: daí até 7 dias, o Messenger só aceita a resposta digitada pelo atendente na conversa.

➡️ **“ticketId”:** ID do Ticket, no lugar do `number`.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

➡️ **“header”:** linha que vai acima do texto, até 60 caracteres. **Opcional.**

➡️ **“body”:** o texto da mensagem, até 1024 caracteres. Não pode ficar vazio. **Obrigatório.**

➡️ **“footer”:** linha que vai abaixo do texto, até 60 caracteres. **Opcional.**

➡️ **“buttonText”:** o texto do botão da lista, até 20 caracteres. **Obrigatório** também no Messenger, onde não há botão para abrir a lista: os itens chegam direto para o contato tocar.

➡️ **“sections”:** até 10 seções, com até 10 itens somando todas. **Obrigatório.**

◽ **“title”** da seção: até 24 caracteres. Obrigatório quando há mais de uma seção.

◽ **“rows”:** os itens da seção. Cada item tem `id` (o que volta para a sua integração, até 200 caracteres, sem repetir), `title` (até 24) e `description` opcional (até 72).

◽ No Messenger, cada item chega como uma resposta rápida do próprio Messenger, com o título em até 20 caracteres. O título das seções e as descrições ficam só no painel.

◽ Só a última mensagem fica com as opções tocáveis; nas anteriores, elas deixam de responder ao toque. É como o Messenger funciona — mande uma pergunta por vez.

⚠️ Campo acima do limite ou faltando é recusado, e a resposta diz qual campo corrigir.

◽ Quando o contato escolhe um item, o título dele entra no atendimento como mensagem do cliente e chega no webhook da conexão com o `id` do item em `postback` (e em `button.payload`).

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/channels/sendList',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "{facebookId}",
    "header": "Cardápio",
    "body": "Escolha o seu pedido:",
    "footer": "Entrega em 40 minutos",
    "buttonText": "Ver opções",
    "sections": [
        {
            "title": "Pizzas",
            "rows": [
                {
                    "id": "pz-mussarela",
                    "title": "Mussarela",
                    "description": "Molho, mussarela e orégano"
                },
                {
                    "id": "pz-calabresa",
                    "title": "Calabresa"
                }
            ]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/channels/sendList' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"{facebookId}","header":"Cardápio","body":"Escolha o seu pedido:","footer":"Entrega em 40 minutos","buttonText":"Ver opções","sections":[{"title":"Pizzas","rows":[{"id":"pz-mussarela","title":"Mussarela","description":"Molho, mussarela e orégano"},{"id":"pz-calabresa","title":"Calabresa"}]}]}'
```
