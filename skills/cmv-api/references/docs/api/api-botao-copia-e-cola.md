# API Botão Copia e Cola

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-botao-copia-e-cola
- **Categoria:** APIs
- **Menu:** APIs › Botões › API Botão Copia e Cola

---

🧩 Envia uma mensagem com **um botão que copia um código** ao ser tocado.

**API:** Básica

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendCopyPaste
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
        "header": "Seu código",
        "body": "Segue o nosso Pix",
        "name": "cta_copy",
        "params": "{\"display_text\":\"Copiar Pix\",\"id\":\"botao_pix\",\"copy_code\":\"meupix@gmail.com\",\"disabled\":false}"
    }
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“body”:** o texto que aparece antes do botão.

➡️ **“header”:** título opcional, acima do texto.

➡️ **“name”:** `cta_copy`.

➡️ **“params”:** os parâmetros do botão, em **texto JSON** — repare nas aspas escapadas dentro da string.

◽ **display_text:** o rótulo do botão.

◽ **copy_code:** o texto que vai para a área de transferência do cliente.

◽ **id:** qualquer identificador seu.

◽ **disabled:** `false` deixa o botão clicável.

◽ O `name` aceita os quatro botões nativos da Meta: `cta_copy` (copiar código), `cta_url` (abrir link), `quick_reply` (resposta rápida) e `cta_call` (ligar). O endereço desta chamada sugere o uso, mas não limita o tipo.

⚠️ **Esta chamada não abre atendimento e não grava a mensagem no painel.** Ela confere o número e envia. Campos como `openTicket` e `queueId` são ignorados aqui.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendCopyPaste',
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
        "header": "Seu código",
        "body": "Segue o nosso Pix",
        "name": "cta_copy",
        "params": "{\"display_text\":\"Copiar Pix\",\"id\":\"botao_pix\",\"copy_code\":\"meupix@gmail.com\",\"disabled\":false}"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendCopyPaste' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","customData":{"header":"Seu código","body":"Segue o nosso Pix","name":"cta_copy","params":"{\"display_text\":\"Copiar Pix\",\"id\":\"botao_pix\",\"copy_code\":\"meupix@gmail.com\",\"disabled\":false}"}}'
```
