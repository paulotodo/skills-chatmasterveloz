# API WebChat Enviar Arquivo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-webchat-enviar-arquivo
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API WebChat Enviar Arquivo

---

🧩 Envia **um arquivo de mídia** (imagem, vídeo, áudio ou documento) para um visitante ativo no widget WebChat, identificado pelo **sessionId**. O arquivo viaja junto da requisição (multipart).

**API:** WebChat

##### Endpoint

```
https://api2.chatmasterveloz.com/api/webchat/messages/send
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

```php
array(
    'sessionId' => 'session_1745772400000_abc123',
    'body' => 'Segue o documento solicitado',
    'medias' => new CURLFile('/caminho/arquivo.pdf', 'application/pdf')
  )
```

➡️ **“sessionId”:** identificador único da sessão do visitante no widget. É gerado pelo widget e pode ser obtido via webhook, pela mensagem-marcador do ticket ou pela página de visitantes ao vivo.

➡️ **“body”:** texto opcional. Quando informado, vira a **legenda do arquivo**.

➡️ **“medias”:** o arquivo a enviar — **um por chamada**, com até 20 MB. O tipo — imagem, vídeo, áudio ou documento — é reconhecido pelo mimetype informado.

⚠️ O campo se chama `medias` e leva **um arquivo só**. `medias[0]`, `medias[]`, o campo repetido ou outro nome (`media`, `file`) são recusados com *"Envie um arquivo por vez, no campo do arquivo."* Para mandar vários, faça uma chamada por arquivo.

◽ O arquivo vai com o **tipo** dele — o segundo valor do `CURLFile`, como `application/pdf`, `image/png`, `audio/mpeg` ou `video/mp4`. Sem ele, a resposta é *"O tipo do arquivo … não foi reconhecido"*. Com o tipo errado, o arquivo chega como outro: um PDF marcado como `image/png` chega como imagem.

◽ O nome do arquivo precisa ter uma das extensões abaixo. Sem extensão, a resposta é *"Extensão de arquivo não permitida no WebChat"*.

◽ Extensões aceitas: `.jpg` `.png` `.gif` `.webp` `.mp4` `.webm` `.mp3` `.ogg` `.pdf` `.doc` `.docx` `.xls` `.xlsx` `.csv`.

◽ Tipos MIME aceitos: `image/*`, `video/*`, `audio/*`, `application/pdf`, `application/msword`, entre outros. Tipo fora da lista é recusado com *"Tipo de arquivo não permitido no WebChat: …"*.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/webchat/messages/send',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => array(
    'sessionId' => 'session_1745772400000_abc123',
    'body' => 'Segue o documento solicitado',
    'medias' => new CURLFile('/caminho/arquivo.pdf', 'application/pdf')
  ),
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
