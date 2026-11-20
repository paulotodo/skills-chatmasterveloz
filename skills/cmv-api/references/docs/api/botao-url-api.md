# API Botão URL

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/botao-url-api
- **Categoria:** APIs
- **Menu:** APIs › Botões › API Botão URL

---

🧩 Envia uma mensagem com **um botão que abre um link**.

**API:** Básica

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendURLBTN
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
    "customData": {
        "header": "Rastreio",
        "body": "Segue o nosso site",
        "name": "cta_url",
        "params": "{\"display_text\":\"Acessar\",\"id\":\"botao_site\",\"url\":\"https://meusite.com.br\",\"disabled\":false}"
    }
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“body”:** o texto que aparece antes do botão.

➡️ **“header”:** título opcional, acima do texto.

➡️ **“name”:** `cta_url`.

➡️ **“params”:** os parâmetros do botão, em **texto JSON** — repare nas aspas escapadas dentro da string.

◽ **display_text:** o rótulo do botão.

◽ **url:** o endereço que abre quando o cliente toca.

◽ **id:** qualquer identificador seu.

◽ **disabled:** `false` deixa o botão clicável.

◽ O `name` aceita os quatro botões nativos da Meta: `cta_copy` (copiar código), `cta_url` (abrir link), `quick_reply` (resposta rápida) e `cta_call` (ligar). O endereço desta chamada sugere o uso, mas não limita o tipo.

⚠️ **Esta chamada não abre atendimento e não grava a mensagem no painel.** Ela confere o número e envia. Campos como `openTicket` e `queueId` são ignorados aqui.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendURLBTN',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "customData": {
        "header": "Rastreio",
        "body": "Segue o nosso site",
        "name": "cta_url",
        "params": "{\"display_text\":\"Acessar\",\"id\":\"botao_site\",\"url\":\"https://meusite.com.br\",\"disabled\":false}"
    }
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendURLBTN' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","customData":{"header":"Rastreio","body":"Segue o nosso site","name":"cta_url","params":"{\"display_text\":\"Acessar\",\"id\":\"botao_site\",\"url\":\"https://meusite.com.br\",\"disabled\":false}"}}'
```
