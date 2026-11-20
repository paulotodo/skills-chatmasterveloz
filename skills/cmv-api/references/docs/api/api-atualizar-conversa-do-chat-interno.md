# API Atualizar Conversa do Chat Interno

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-conversa-do-chat-interno
- **Categoria:** APIs
- **Menu:** APIs › Chat Interno › API Atualizar Conversa do Chat Interno

---

🧩 Atualiza **uma conversa do chat interno**: o nome, quem participa, o modo de publicação e o webhook.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}
```

##### Método

```
PUT
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "title": "Equipe do Financeiro e Cobrança",
    "users": [7, 12, 15],
    "somenteAvisos": true,
    "webhookUrl": "https://seusistema.com.br/chat-interno"
}
```

◽ O `chatId` é o ID da conversa, que vem na listagem das conversas.

➡️ **Só muda o que você mandar.** Campo que não vier no payload fica como está.

➡️ **“title”:** o nome novo da conversa.

➡️ **“users”:** a lista **nova e inteira** de participantes — não é acréscimo.

◽ Quem estava e não vier na lista sai da conversa.

◽ O dono continua na conversa de todo jeito.

➡️ **“somenteAvisos”:** `true` deixa só o dono e os administradores publicarem; `false` libera todos.

➡️ **“webhookUrl”:** endereço que recebe os avisos **desta** conversa, começando com `http://` ou `https://` e sem espaços.

◽ Vazio ou `null` tira o webhook da conversa.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "title": "Equipe do Financeiro e Cobrança",
    "users": [7, 12, 15],
    "somenteAvisos": true,
    "webhookUrl": "https://seusistema.com.br/chat-interno"
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"title":"Equipe do Financeiro e Cobrança","users":[7,12,15],"somenteAvisos":true,"webhookUrl":"https://seusistema.com.br/chat-interno"}'
```
