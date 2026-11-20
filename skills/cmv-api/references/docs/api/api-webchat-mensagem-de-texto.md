# API WebChat Mensagem de Texto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-webchat-mensagem-de-texto
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API WebChat Mensagem de Texto

---

🧩 Enviar uma **mensagem de texto** para um visitante ativo no widget WebChat, identificado pelo **sessionId**.

**API:** WebChat

##### Endpoint

```
https://api2.chatmasterveloz.com/api/webchat/messages/send
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
  "sessionId": "session_1745772400000_abc123",
  "body": "Olá! Em que posso te ajudar?"
}
```

➡️ **“sessionId”:** identificador único da sessão do visitante no widget. É gerado pelo widget e pode ser obtido via webhook, pela mensagem-marcador do ticket ou pela página de visitantes ao vivo.

➡️ **“body”:** conteúdo da mensagem que será entregue ao visitante em tempo real.

⚠️ O ticket precisa estar **aberto** ou **pendente**. Tickets fechados não recebem mensagens.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/webchat/messages/send',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "sessionId": "session_1745772400000_abc123",
    "body": "Olá! Em que posso te ajudar?"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/webchat/messages/send' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"sessionId":"session_1745772400000_abc123","body":"Olá! Em que posso te ajudar?"}'
```
