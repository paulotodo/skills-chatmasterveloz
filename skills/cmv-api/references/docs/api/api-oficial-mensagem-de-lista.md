# API Oficial Mensagem de Lista

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-mensagem-de-lista
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Oficial Mensagem de Lista

---

🧩 Envia uma **mensagem com uma Lista de opções**, estando com a Janela de Atendimento ao Cliente **aberta,** para o usuário escolher uma resposta. O título da opção é a resposta devolvida quando o lead escolhe.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendInteractive
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
    "ticketId": 700,
    "type": "list",
    "header": {
        "type": "text",
        "text": "Texto do Header"
    },
    "body": {
        "text": "Texto do Body"
    },
    "footer": {
        "text": "Rodapé"
    },
    "action": {
        "sections": [
            {
                "title": "Titulo da lista A",
                "rows": [
                    {
                        "id": 1,
                        "title": "Linha 01 - lista A",
                        "description": "descricao 01 - lista A"
                    },
                    {
                        "id": 2,
                        "title": "Linha 02 - lista A",
                        "description": "descricao 02 - lista A"
                    }
                ]
            },
            {
                "title": "Titulo da lista B",
                "rows": [
                    {
                        "id": 3,
                        "title": "Linha 03 - lista B",
                        "description": "descricao 03 - lista B"
                    },
                    {
                        "id": 4,
                        "title": "Linha 04 - lista B",
                        "description": "descricao 04 - lista B"
                    }
                ]
            }
        ],
        "button": "Lista de opções"
    },
    "openTicket": 1,
    "queueId": 1
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números). **Obrigatório**, mesmo quando o `ticketId` é informado.

➡️ **“ticketId”:** ID do Ticket. **Opcional** — não substitui o `number`: só escolhe em qual atendimento a mensagem fica gravada.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ Precisa ser um atendimento desta conexão e do contato de `number`. Sem ele, vale o atendimento do contato nesta conexão.

➡️ **“type”:** `list`.

➡️ **“header”:** cabeçalho opcional, no campo `text`.

➡️ **“body”:** sua mensagem, no campo `text` (máximo de 1024 caracteres).

➡️ **“footer”:** rodapé opcional, no campo `text`.

➡️ **“action”:** o conteúdo da lista, sendo que:

◽ `sections`: cada seção da lista, com `title` (título da seção) e `rows` (as opções dela).

◽ cada opção dentro de `rows` tem `id`, `title` e `description`.

◽ `button`: texto do botão que, ao ser clicado, exibe as opções da lista.

Adicione mais seções e opções se desejar.

➡️ **“openTicket”:** `1` deixa a conversa em **Aguardando** no Setor de `queueId`.

➡️ **“queueId”:** ID do Setor para onde a conversa vai quando `"openTicket": 1`.

⚠️ **Sem `openTicket` (ou com `0`), o atendimento fica como estava:** se a conversa já estava em atendimento ou aguardando, continua no mesmo Setor e com o mesmo atendente. Só quando o contato não tinha atendimento em andamento antes do envio é que o atendimento é encerrado depois do envio.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendInteractive',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "ticketId": 700,
    "type": "list",
    "header": {
        "type": "text",
        "text": "Texto do Header"
    },
    "body": {
        "text": "Texto do Body"
    },
    "footer": {
        "text": "Rodapé"
    },
    "action": {
        "sections": [
            {
                "title": "Titulo da lista A",
                "rows": [
                    {
                        "id": 1,
                        "title": "Linha 01 - lista A",
                        "description": "descricao 01 - lista A"
                    },
                    {
                        "id": 2,
                        "title": "Linha 02 - lista A",
                        "description": "descricao 02 - lista A"
                    }
                ]
            },
            {
                "title": "Titulo da lista B",
                "rows": [
                    {
                        "id": 3,
                        "title": "Linha 03 - lista B",
                        "description": "descricao 03 - lista B"
                    },
                    {
                        "id": 4,
                        "title": "Linha 04 - lista B",
                        "description": "descricao 04 - lista B"
                    }
                ]
            }
        ],
        "button": "Lista de opções"
    },
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendInteractive' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","ticketId":700,"type":"list","header":{"type":"text","text":"Texto do Header"},"body":{"text":"Texto do Body"},"footer":{"text":"Rodapé"},"action":{"sections":[{"title":"Titulo da lista A","rows":[{"id":1,"title":"Linha 01 - lista A","description":"descricao 01 - lista A"},{"id":2,"title":"Linha 02 - lista A","description":"descricao 02 - lista A"}]},{"title":"Titulo da lista B","rows":[{"id":3,"title":"Linha 03 - lista B","description":"descricao 03 - lista B"},{"id":4,"title":"Linha 04 - lista B","description":"descricao 04 - lista B"}]}],"button":"Lista de opções"},"openTicket":1,"queueId":1}'
```
