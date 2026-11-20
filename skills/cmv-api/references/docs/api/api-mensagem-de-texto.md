# API Mensagem de Texto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-mensagem-de-texto
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Mensagem de Texto

---

🧩 Envia uma **mensagem de texto**, com opções de abrir um ticket e atribuir a conversa a um Setor.

**API:** Básica, Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/send
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
    "number": "5511955892164",
    "openTicket": "1",
    "queueId": "16",
    "body": "Bem vindo Lead"
  }
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“openTicket”:** `0` não abre ticket e `1` abre. Para abrir é obrigatório informar um Setor em `queueId`, e a conversa vai para **Aguardando** mesmo que já esteja em atendimento.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“body”:** mensagem.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/send',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "openTicket": "0",
    "queueId": "0",
    "body": "Olá, tudo bem?"
  }',
  // "openTicket": "0", 0 Não abre ticket e 1 Abre Ticket
  // "queueId": "0", ID do Setor desejado (necessário definir se abrir ticket)
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/send' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","openTicket":"1","queueId":"16","body":"Bem vindo Lead"}'
```
