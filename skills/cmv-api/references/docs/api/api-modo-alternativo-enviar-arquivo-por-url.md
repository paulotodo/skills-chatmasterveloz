# API Modo Alternativo Enviar Arquivo por URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-modo-alternativo-enviar-arquivo-por-url
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Modo Alternativo Enviar Arquivo por URL

---

🧩 Envia um **arquivo por URL** que aparece apenas na página do **Modo Alternativo (chat externo por link)**, sem sair pelo canal.

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

```javascript
{
    "ticketId": 700,
    "url": "https://arquivos.exemplo.com/proposta.pdf",
    "filename": "proposta.pdf",
    "body": "Segue a proposta"
}
```

➡️ **“ticketId”:** ID do Ticket. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

➡️ **“url”:** endereço público do arquivo, em `http` ou `https`. **Obrigatório.**

◽ Endereço interno é recusado. O arquivo tem até 20 MB, e a plataforma espera até 30 segundos para baixá-lo.

➡️ **“filename”:** opcional. Nome com que o arquivo é gravado. Sem ele, vale o nome que estiver no fim da URL.

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
  CURLOPT_POSTFIELDS =>'{
    "ticketId": 700,
    "url": "https://arquivos.exemplo.com/proposta.pdf",
    "filename": "proposta.pdf",
    "body": "Segue a proposta"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/chat-externo/midia' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"url":"https://arquivos.exemplo.com/proposta.pdf","filename":"proposta.pdf","body":"Segue a proposta"}'
```
