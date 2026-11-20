# API Modo Alternativo Enviar Arquivo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-modo-alternativo-enviar-arquivo
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Modo Alternativo Enviar Arquivo

---

🧩 Envia **arquivos do seu computador** que aparecem apenas na página do **Modo Alternativo (chat externo por link)**, sem sair pelo canal.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/chat-externo/midia
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
    'ticketId' => 700,
    'body' => 'Segue a proposta em PDF',
    'medias' => new CURLFile('/caminho/proposta.pdf', 'application/pdf')
  )
```

➡️ **“ticketId”:** ID do Ticket. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

➡️ **“medias”:** o arquivo. **Obrigatório.**

⚠️ O campo se chama `medias`, sem número nem colchetes. `medias[0]`, `medias[]` ou outro nome (`media`, `file`) são recusados com erro.

◽ Informe o **tipo** certo do arquivo — o segundo valor do `CURLFile`, como `application/pdf`, `image/png`, `audio/mpeg` ou `video/mp4`. Sem ele, a plataforma deduz; com o tipo errado, o arquivo chega como outro: um PDF marcado como `image/png` chega como imagem.

◽ Para mandar mais de um arquivo, faça uma chamada por arquivo. Ferramenta que repete o campo `medias` na mesma chamada também funciona: **cada arquivo vira uma mensagem**.

◽ Imagem, áudio, vídeo ou documento — o tipo é reconhecido pelo tipo informado ou, sem ele, pelo próprio arquivo.

➡️ **“body”:** opcional. A legenda. Sem ela, vale o nome do arquivo.

◽ `caption` funciona como sinônimo de `body`.

⚠️ **A conexão do atendimento precisa estar em Modo Alternativo ou ser de Chat Externo.** Fora disso a chamada é recusada, porque a mensagem não teria como chegar ao cliente.

◽ A mensagem aparece no painel do operador e na página do cliente, e **não sai** pelo WhatsApp.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/chat-externo/midia',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => array(
    'ticketId' => 700,
    'body' => 'Segue a proposta em PDF',
    'medias' => new CURLFile('/caminho/proposta.pdf', 'application/pdf')
  ),
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
