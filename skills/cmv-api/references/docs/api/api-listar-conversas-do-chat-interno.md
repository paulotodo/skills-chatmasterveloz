# API Listar Conversas do Chat Interno

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-conversas-do-chat-interno
- **Categoria:** APIs
- **Menu:** APIs › Chat Interno › API Listar Conversas do Chat Interno

---

🧩 Obter as **conversas do chat interno** da sua empresa, da mais recente para a mais antiga.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/chat-interno/chats?userId={userId}&pageNumber={pageNumber}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, e todos são opcionais.

◽ **userId:** só as conversas de que aquele usuário participa. Usuário de fora da empresa faz a chamada ser recusada.

◽ **pageNumber:** a página, de **50 em 50**. Padrão `1`.

➡️ **Cada conversa vem com o seu webhook**, quando tiver um.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/chat-interno/chats?userId={userId}&pageNumber={pageNumber}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/chat-interno/chats?userId={userId}&pageNumber={pageNumber}' -H 'Authorization: Bearer {seutokenaqui}'
```
