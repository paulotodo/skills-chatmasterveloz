# API Enviar Áudio Base64

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-audio-base64-pro
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Enviar Áudio Base64

---

🧩 Envia um **áudio a partir do formato base64**, com opções de abrir um ticket e atribuir a conversa a um Setor.

**API:** Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendBase64AudioWhatsmeowPRO
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
    "queueId": "44",
    "body": "data:audio/ogg;base64,iVBORw0a",
    "ptt": true,
    "caption": "Aqui você pode colocar a TRANSCRIÇÃO DO ÁUDIO - Uma vez que o cliente não recebe áudio com caption, utilize para registrar o conteúdo enviado na plataforma"
  }
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“openTicket”:** `0` não abre ticket e `1` abre. Para abrir é obrigatório informar um Setor em `queueId`, e a conversa vai para **Aguardando** mesmo que já esteja em atendimento.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“body”:** o áudio em `string base64`.

➡️ **“ptt”:** `true` para o áudio chegar como mensagem de voz.

➡️ **“caption”:** legenda. O cliente não recebe legenda em áudio, então use este campo para registrar a transcrição do que foi enviado — ela fica visível na plataforma.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendBase64AudioWhatsmeowPRO',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "openTicket": "1",
    "queueId": "44",
    "body": "data:audio/ogg;base64,iVBORw0a",
    "ptt": true,
    "caption": "Aqui você pode colocar a TRANSCRIÇÃO DO ÁUDIO - Uma vez que o cliente não recebe áudio com caption, utilize para registrar o conteúdo enviado na plataforma"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendBase64AudioWhatsmeowPRO' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","openTicket":"1","queueId":"44","body":"data:audio/ogg;base64,iVBORw0a","ptt":true,"caption":"Aqui você pode colocar a TRANSCRIÇÃO DO ÁUDIO - Uma vez que o cliente não recebe áudio com caption, utilize para registrar o conteúdo enviado na plataforma"}'
```
