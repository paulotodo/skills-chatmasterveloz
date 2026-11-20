# API Listar Mensagens do Chat Interno

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-mensagens-do-chat-interno
- **Categoria:** APIs
- **Menu:** APIs › Chat Interno › API Listar Mensagens do Chat Interno

---

🧩 Obter as **mensagens de uma conversa** do chat interno, da mais nova para a mais antiga.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/messages?pageNumber={pageNumber}
```

##### Método

```
GET
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```
// sem payload — os filtros vão na própria URL
```

➡️ Esta chamada não tem payload. A página é informada como **query** na URL.

◽ O `chatId` é o ID da conversa, que vem na listagem das conversas.

◽ **pageNumber:** a página, de **50 em 50**. Padrão `1`.

➡️ **As mensagens apagadas também vêm**, marcadas como apagadas.

◽ Ler por aqui **não marca nada como lido** — o não lido da equipe continua como está.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/messages?pageNumber={pageNumber}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/messages?pageNumber={pageNumber}' -H 'Authorization: Bearer {seutokenaqui}'
```
