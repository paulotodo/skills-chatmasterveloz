# API Chat Externo Mensagem de Lista

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-chat-externo-mensagem-de-lista
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Chat Externo Mensagem de Lista

---

🧩 Envia uma **mensagem com uma Lista de opções** para o cliente que está na página do **Chat Externo**. O título da opção é a resposta devolvida quando o cliente escolhe.

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
    "type": "list",
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

➡️ **“ticketId”:** ID do Ticket. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ É o `chamadoId` que chega no webhook da mensagem do cliente.

➡️ **“type”:** `list`. **Obrigatório.**

➡️ **“header”:** título que aparece acima do texto, até 60 caracteres. **Opcional.**

➡️ **“body”:** o texto da mensagem, até 1024 caracteres. Não pode ficar vazio. **Obrigatório.**

➡️ **“footer”:** linha menor abaixo do texto, até 60 caracteres. **Opcional.**

➡️ **“buttonText”:** o texto do botão que abre a lista, até 20 caracteres. **Obrigatório.**

◽ Na página, o botão aparece com ☰ na frente — em **☰ Ver opções**, o cliente toca e a lista abre.

➡️ **“sections”:** até 10 seções, com até 10 itens somando todas. **Obrigatório.**

◽ **“title”** da seção: até 24 caracteres. Obrigatório quando há mais de uma seção.

◽ **“rows”:** os itens da seção. Cada item tem `id` (o que volta para a sua integração, até 200 caracteres, sem repetir), `title` (até 24) e `description` opcional (até 72).

⚠️ Campo acima do limite ou faltando é recusado, e a resposta diz qual campo corrigir.

◽ Quando o cliente escolhe um item, o título dele entra no atendimento como mensagem do cliente e chega no webhook com `"type": "list_reply"` e `interactive` (o `id`, o `title` e o `messageId` da mensagem com a lista).

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
    "type": "list",
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
curl -X POST 'https://api2.chatmasterveloz.com/api/chat-externo/mensagem' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"type":"list","header":"Cardápio","body":"Escolha o seu pedido:","footer":"Entrega em 40 minutos","buttonText":"Ver opções","sections":[{"title":"Pizzas","rows":[{"id":"pz-mussarela","title":"Mussarela","description":"Molho, mussarela e orégano"},{"id":"pz-calabresa","title":"Calabresa"}]}]}'
```
