# API Gupshup Mensagem Template

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-gupshup-mensagem-template
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Gupshup Mensagem Template

---

🧩 Envia uma **mensagem template** aprovada na Gupshup, pela conexão do WhatsApp Gupshup.

**API:** Gupshup

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendGupshupTemplate
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
    "template": "pedido_confirmado",
    "language": "pt_BR",
    "variables": {
        "1": "Maria",
        "2": "#123"
    },
    "buttonValues": [
        {
            "text": "Acompanhar",
            "value": "abc123"
        }
    ],
    "name": "Maria Souza",
    "ticketId": 700
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números). **Obrigatório**, mesmo quando o `ticketId` é informado.

➡️ **“template”:** o id do template na Gupshup ou o nome dele. Só template **aprovado**. **Obrigatório.**

◽ Fora da janela de 24 horas, só o template abre a conversa com o cliente.

◽ Quando a Gupshup recusa o template, a chamada responde **400**, e o motivo fica registrado no atendimento.

➡️ **“language”:** o idioma do template, como `pt_BR`. Só faz diferença quando o mesmo nome existe em mais de um idioma.

➡️ **“variables”:** as variáveis do corpo do template, pelo número: `"1"` é a primeira, `"2"` a segunda.

➡️ **“buttonValues”:** o final do link de cada botão de link dinâmico. O `text` é o texto do botão, e o `value`, o que completa o link.

◽ Template com imagem, vídeo ou documento no cabeçalho aceita também o `headerMedia`, com a `url` e o `filename` do arquivo. Sem ele, vai a mídia de exemplo do template.

➡️ **“name”:** nome do contato, usado só quando ele ainda não existe.

➡️ **“ticketId”:** ID do Ticket. **Opcional** — não substitui o `number`: só escolhe em qual atendimento a mensagem fica gravada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendGupshupTemplate',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "template": "pedido_confirmado",
    "language": "pt_BR",
    "variables": {
        "1": "Maria",
        "2": "#123"
    },
    "buttonValues": [
        {
            "text": "Acompanhar",
            "value": "abc123"
        }
    ],
    "name": "Maria Souza",
    "ticketId": 700
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendGupshupTemplate' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","template":"pedido_confirmado","language":"pt_BR","variables":{"1":"Maria","2":"#123"},"buttonValues":[{"text":"Acompanhar","value":"abc123"}],"name":"Maria Souza","ticketId":700}'
```
