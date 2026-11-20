# API Chat Externo Enviar Arquivo por URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-chat-externo-enviar-arquivo-por-url
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Chat Externo Enviar Arquivo por URL

---

🧩 Envia um **arquivo por URL** para o cliente que está na página do **Chat Externo**.

**API:** Chat Externo

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

```javascript
{
    "ticketId": 700,
    "url": "https://suite.chatmasterveloz.com/api/image.jpg",
    "filename": "foto-do-produto.jpg",
    "body": "Segue a foto do produto"
}
```

➡️ **“ticketId”:** ID do Ticket. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ É o `chamadoId` que chega no webhook da mensagem do cliente.

➡️ **“url”:** endereço público do arquivo, em `http` ou `https`. **Obrigatório.**

◽ Imagem, áudio, vídeo ou documento — o tipo é reconhecido pelo próprio arquivo.

◽ Endereço interno é recusado. O arquivo tem até 20 MB, e a plataforma espera até 30 segundos para baixá-lo.

➡️ **“filename”:** opcional. Nome com que o arquivo é gravado. Sem ele, vale o nome que estiver no fim da URL.

➡️ **“body”:** opcional. A legenda. Sem ela, vale o nome do arquivo.

◽ `caption` funciona como sinônimo de `body`.

◽ A mensagem aparece no painel do operador e na página do cliente.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

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
  CURLOPT_POSTFIELDS =>'{
    "ticketId": 700,
    "url": "https://suite.chatmasterveloz.com/api/image.jpg",
    "filename": "foto-do-produto.jpg",
    "body": "Segue a foto do produto"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/chat-externo/midia' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"url":"https://suite.chatmasterveloz.com/api/image.jpg","filename":"foto-do-produto.jpg","body":"Segue a foto do produto"}'
```
