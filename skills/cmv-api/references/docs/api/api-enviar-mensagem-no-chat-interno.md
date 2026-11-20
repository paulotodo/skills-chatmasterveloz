# API Enviar Mensagem no Chat Interno

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-mensagem-no-chat-interno
- **Categoria:** APIs
- **Menu:** APIs › Chat Interno › API Enviar Mensagem no Chat Interno

---

🧩 Envia uma **mensagem de texto** no chat interno, em nome de um usuário da equipe.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/messages
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
    "userId": 7,
    "message": "Pessoal, a fatura de outubro já está fechada.",
    "mentions": [12],
    "quotedMsgId": 0
}
```

◽ O `chatId` é o ID da conversa, que vem na listagem das conversas.

➡️ **“userId”:** ID de quem envia, que precisa ser usuário da empresa **e participar daquela conversa**. **Obrigatório.**

➡️ **“message”:** o texto da mensagem. **Obrigatório.**

➡️ **“mentions”:** IDs dos participantes a mencionar, que são notificados.

◽ Quem ainda não aparece no texto como `@Nome` ganha a marcação no começo da mensagem.

➡️ **“quotedMsgId”:** ID de uma mensagem **daquela mesma conversa**, para responder citando.

➡️ **A mensagem chega como as do painel**, com as notificações de sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/messages',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "userId": 7,
    "message": "Pessoal, a fatura de outubro já está fechada.",
    "mentions": [12],
    "quotedMsgId": 0
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token da Empresa
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X POST 'https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/messages' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"userId":7,"message":"Pessoal, a fatura de outubro já está fechada.","mentions":[12],"quotedMsgId":0}'
```
