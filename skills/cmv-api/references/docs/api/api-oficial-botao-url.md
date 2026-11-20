# API Oficial Botão URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-botao-url
- **Categoria:** APIs
- **Menu:** APIs › Botões › API Oficial Botão URL

---

🧩 Envia uma mensagem com **um botão que abre um link**, estando com a Janela de Atendimento ao Cliente **aberta**.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendCTAURL
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
    "type": "button",
    "header": {
        "type": "text",
        "text": "Catálogo 2026"
    },
    "body": {
      "text": "Confira nosso catálogo completo e escolha o que mais combina com você."
    },
    "footer": {
        "text": "Rodapé opcional"
    },
    "displayText": "Visitar site",
    "url": "https://www.meusite.com.br/produtos",
    "openTicket": 1,
    "queueId": 1
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“type”:** `button`.

➡️ **“header”:** cabeçalho opcional. Pode ser texto, imagem, vídeo ou documento, no formato da Meta.

◽ **Texto:** `{"type": "text", "text": "Meu cabeçalho"}`

◽ **Imagem:** `{"type": "image", "image": {"link": "https://meusite.com.br/foto.jpg"}}`

◽ **Vídeo:** `{"type": "video", "video": {"link": "https://meusite.com.br/video.mp4"}}`

◽ **Documento:** `{"type": "document", "document": {"link": "https://meusite.com.br/catalogo.pdf", "filename": "catalogo.pdf"}}`

◽ **Áudio não existe** no cabeçalho: a Meta não aceita.

➡️ **“body”:** o texto da mensagem, dentro de `text`. Até **1024 caracteres**. **Obrigatório.**

➡️ **“footer”:** rodapé opcional, dentro de `text`.

➡️ **“displayText”:** o rótulo do botão, até **20 caracteres** (limite da Meta). **Obrigatório.**

➡️ **“url”:** o endereço que o botão abre. Precisa começar com `http://` ou `https://`. **Obrigatório.**

➡️ **“openTicket”:** `1` deixa a conversa em **Aguardando** no Setor de `queueId`.

➡️ **“queueId”:** ID do Setor para onde a conversa vai quando `"openTicket": 1`.

⚠️ **Sem `openTicket` (ou com `0`), o atendimento fica como estava:** se a conversa já estava em atendimento ou aguardando, continua no mesmo Setor e com o mesmo atendente. Só quando o contato não tinha atendimento em andamento antes do envio é que o atendimento é encerrado depois do envio.

◽ Só passa dentro da **janela de 24 horas**. Fora dela a Meta recusa, e o caminho é um template aprovado.

◽ A mensagem fica gravada no atendimento com o texto e o rótulo do botão com o link.

◽ Recusa da Meta vira mensagem de erro dentro do próprio atendimento.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendCTAURL',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "type": "button",
    "header": {
        "type": "text",
        "text": "Catálogo 2026"
    },
    "body": {
      "text": "Confira nosso catálogo completo e escolha o que mais combina com você."
    },
    "footer": {
        "text": "Rodapé opcional"
    },
    "displayText": "Visitar site",
    "url": "https://www.meusite.com.br/produtos",
    "openTicket": 1,
    "queueId": 1
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendCTAURL' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","type":"button","header":{"type":"text","text":"Catálogo 2026"},"body":{"text":"Confira nosso catálogo completo e escolha o que mais combina com você."},"footer":{"text":"Rodapé opcional"},"displayText":"Visitar site","url":"https://www.meusite.com.br/produtos","openTicket":1,"queueId":1}'
```
