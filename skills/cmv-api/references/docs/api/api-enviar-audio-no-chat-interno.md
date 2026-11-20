# API Enviar Áudio no Chat Interno

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-audio-no-chat-interno
- **Categoria:** APIs
- **Menu:** APIs › Chat Interno › API Enviar Áudio no Chat Interno

---

🧩 Envia um **áudio** no chat interno, que chega com o player, como o gravado no painel.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/audios
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
    "url": "https://seusistema.com.br/arquivos/recado-da-reuniao.mp3",
    "userId": 7,
    "message": "Recado da reunião de hoje.",
    "fileName": "recado-da-reuniao.mp3",
    "mentions": [12],
    "quotedMsgId": 0
}
```

◽ O `chatId` é o ID da conversa, que vem na listagem das conversas.

➡️ **“url”:** endereço de onde baixar o arquivo, começando com `http://` ou `https://`. **Obrigatório.**

◽ O arquivo pode ter até **64 MB**. Se o endereço não entregar o arquivo, a chamada é recusada.

◽ Ele fica guardado na pasta da empresa, como os enviados pelo painel.

➡️ **“userId”:** ID de quem envia, que precisa ser usuário da empresa **e participar daquela conversa**. **Obrigatório.**

➡️ **“message”:** o texto que acompanha o áudio. Sem ele, aparece `🎤 Áudio`.

➡️ **MP3 e WebM tocam como vieram.** Os outros formatos, como ogg, opus, wav e m4a, são convertidos para MP3 para tocar na conversa.

➡️ **“fileName”:** o nome do arquivo na conversa. Sem ele, vale o nome original ou o fim do endereço.

➡️ **“mentions”:** IDs dos participantes a mencionar, que são notificados.

➡️ **“quotedMsgId”:** ID de uma mensagem **daquela mesma conversa**, para responder citando.

⚠️ **Dá para enviar o arquivo direto, em vez do endereço.** Nesse caso a chamada vai como `multipart/form-data`, com o arquivo no campo `file` e os mesmos campos acima — só que `mentions` vira uma lista separada por vírgula, como `3,5`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/audios',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "url": "https://seusistema.com.br/arquivos/recado-da-reuniao.mp3",
    "userId": 7,
    "message": "Recado da reunião de hoje.",
    "fileName": "recado-da-reuniao.mp3",
    "mentions": [12],
    "quotedMsgId": 0
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
curl -X POST 'https://api2.chatmasterveloz.com/api/chat-interno/chats/{chatId}/audios' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"url":"https://seusistema.com.br/arquivos/recado-da-reuniao.mp3","userId":7,"message":"Recado da reunião de hoje.","fileName":"recado-da-reuniao.mp3","mentions":[12],"quotedMsgId":0}'
```
