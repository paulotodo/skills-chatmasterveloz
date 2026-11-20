# API Enviar Vídeo por URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-video-por-url-pro
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Enviar Vídeo por URL

---

🧩 Envia um **vídeo a partir de uma URL**, com opções de abrir um ticket e atribuir a conversa a um Setor.

**API:** Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowPRO
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
  "type": "video",
  "caption": "Aqui vai minha legenda",
  "fileName": "algumnome.mp4",
  "openTicket": "1",
  "queueId": "44",
  "body": "https://suite.chatmasterveloz.com/api/video.mp4"
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“type”:** `video`.

➡️ **“caption”:** legenda exibida junto do arquivo.

➡️ **“fileName”:** nome do arquivo.

➡️ **“openTicket”:** `0` não abre ticket e `1` abre. Para abrir é obrigatório informar um Setor em `queueId`, e a conversa vai para **Aguardando** mesmo que já esteja em atendimento.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“body”:** URL do arquivo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowPRO',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "type": "video",
    "caption": "Aqui vai minha legenda",
    "fileName": "algumnome.mp4",
    "openTicket": "1",
    "queueId": "44",
    "body": "https://suite.chatmasterveloz.com/api/video.mp4"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendUrlFilesWhatsmeowPRO' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","type":"video","caption":"Aqui vai minha legenda","fileName":"algumnome.mp4","openTicket":"1","queueId":"44","body":"https://suite.chatmasterveloz.com/api/video.mp4"}'
```
