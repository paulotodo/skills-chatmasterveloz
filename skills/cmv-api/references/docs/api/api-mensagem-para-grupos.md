# API Mensagem para Grupos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-mensagem-para-grupos
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Mensagem para Grupos

---

🧩 Envia uma **mensagem de texto para um Grupo**, com opções de abrir um ticket e atribuir a conversa a um Setor.

**API:** Básica

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendGroup
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
    "number": "34324434543543212", //ID do grupo
    "openTicket": "1",
    "queueId": "23",
    "body": "Olá pessoal"
  }
```

➡️ **“number”:** ID do grupo, que fica no mesmo lugar do telefone em um ticket comum.

➡️ **“openTicket”:** `0` não abre ticket e `1` abre. Para abrir é obrigatório informar um Setor em `queueId`, e a conversa vai para **Aguardando** mesmo que já esteja em atendimento.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“body”:** mensagem.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendGroup',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "34324434543543212",
    "openTicket": "0",
    "queueId": "0",
    "body": "Teste"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendGroup' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"34324434543543212","openTicket":"1","queueId":"23","body":"Olá pessoal"}'
```
