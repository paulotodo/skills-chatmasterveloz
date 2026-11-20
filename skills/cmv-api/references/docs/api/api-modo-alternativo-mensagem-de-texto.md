# API Modo Alternativo Mensagem de Texto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-modo-alternativo-mensagem-de-texto
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Modo Alternativo Mensagem de Texto

---

🧩 Envia uma **mensagem de texto** que aparece apenas na página do Modo Alternativo (chat externo por link), sem sair pelo canal.

**API:** Oficial

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
    "body": "Continuamos por aqui. Em que posso ajudar?"
}
```

➡️ **“ticketId”:** ID do Ticket. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

➡️ **“body”:** o texto. Não pode ficar vazio. **Obrigatório.**

⚠️ **A conexão do atendimento precisa estar em Modo Alternativo ou ser de Chat Externo.** Fora disso a chamada é recusada, porque a mensagem não teria como chegar ao cliente.

◽ A mensagem aparece no painel do operador e na página do cliente, e **não sai** pelo WhatsApp.

◽ Não conta para a janela de atendimento.

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
    "body": "Continuamos por aqui. Em que posso ajudar?"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/chat-externo/mensagem' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"body":"Continuamos por aqui. Em que posso ajudar?"}'
```
