# API Criar Conversa no Chat Interno

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-conversa-no-chat-interno
- **Categoria:** APIs
- **Menu:** APIs › Chat Interno › API Criar Conversa no Chat Interno

---

🧩 Cria **uma conversa no chat interno**, a dois ou em grupo, com os participantes já dentro.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/chat-interno/chats
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
    "title": "Equipe do Financeiro",
    "ownerId": 4,
    "users": [7, 12],
    "somenteAvisos": false,
    "webhookUrl": "https://seusistema.com.br/chat-interno"
}
```

➡️ **“title”:** o nome da conversa, como a equipe vê na lista. **Obrigatório.**

➡️ **“ownerId”:** ID do dono da conversa, que precisa ser usuário da empresa. **Obrigatório.**

➡️ **“users”:** IDs dos outros participantes, ao menos um. **Obrigatório.**

◽ Usuário de fora da empresa faz a chamada ser recusada.

◽ Quem participa vê a conversa na hora, sem precisar recarregar a tela.

➡️ **“somenteAvisos”:** `true` cria um grupo em que só o dono e os administradores publicam.

➡️ **“webhookUrl”:** endereço que recebe os avisos **desta** conversa — conversa criada, conversa alterada e mensagem nova.

◽ Precisa começar com `http://` ou `https://` e não pode ter espaços.

◽ Vazio ou `null` tira o webhook da conversa.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/chat-interno/chats',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "title": "Equipe do Financeiro",
    "ownerId": 4,
    "users": [7, 12],
    "somenteAvisos": false,
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
curl -X POST 'https://api2.chatmasterveloz.com/api/chat-interno/chats' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"title":"Equipe do Financeiro","ownerId":4,"users":[7,12],"somenteAvisos":false,"webhookUrl":"https://seusistema.com.br/chat-interno"}'
```
