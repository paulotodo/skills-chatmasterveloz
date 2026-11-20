# API Oficial Botão Quick Reply

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-botao-quick-reply
- **Categoria:** APIs
- **Menu:** APIs › Botões › API Oficial Botão Quick Reply

---

🧩 Envia uma mensagem com **botões de resposta rápida**, estando com a Janela de Atendimento ao Cliente **aberta**.

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
    "type": "button",
    "header": {
      "type": "text",
      "text": "Promoção especial"
    },
    "body": {
      "text": "Temos uma oferta exclusiva para você. Como deseja prosseguir?"
    },
    "footer": {
        "text": "Válido até 31/12"
    },
    "buttons": [
      {
        "type": "reply",
        "reply": {
          "id": "ver_produtos",
          "title": "Ver produtos"
        }
      },
      {
        "type": "reply",
        "reply": {
          "id": "falar_vendedor",
          "title": "Falar com vendedor"
        }
      }
    ],
    "openTicket": 1,
    "queueId": 1
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números). **Obrigatório**, mesmo quando o `ticketId` é informado.

➡️ **“ticketId”:** ID do Ticket. **Opcional** — não substitui o `number`: só escolhe em qual atendimento a mensagem fica gravada.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ Precisa ser um atendimento desta conexão e do contato de `number`. Sem ele, vale o atendimento do contato nesta conexão.

➡️ **“type”:** `button`. **Obrigatório.**

➡️ **“header”:** cabeçalho opcional. Pode ser texto, imagem, vídeo ou documento, no formato da Meta.

◽ **Texto:** `{"type": "text", "text": "Meu cabeçalho"}`

◽ **Imagem:** `{"type": "image", "image": {"link": "https://meusite.com.br/foto.jpg"}}`

◽ **Vídeo:** `{"type": "video", "video": {"link": "https://meusite.com.br/video.mp4"}}`

◽ **Documento:** `{"type": "document", "document": {"link": "https://meusite.com.br/catalogo.pdf", "filename": "catalogo.pdf"}}`

◽ **Áudio não existe** no cabeçalho: a Meta não aceita.

➡️ **“body”:** o texto da mensagem, dentro de `text`. Até **1024 caracteres**. **Obrigatório.**

➡️ **“footer”:** rodapé opcional, dentro de `text`.

➡️ **“buttons”:** de 1 a **3** botões, todos do tipo `reply`. **Obrigatório.**

◽ **id:** identificador do botão, para a sua automação saber qual foi tocado.

◽ **title:** o rótulo que o cliente vê, até **20 caracteres**.

◽ Botão de link, de telefone ou de copiar código **não existe aqui** — nesta chamada todos são de resposta.

➡️ **“openTicket”:** `1` deixa a conversa em **Aguardando** no Setor de `queueId`.

➡️ **“queueId”:** ID do Setor para onde a conversa vai quando `"openTicket": 1`.

⚠️ **Sem `openTicket` (ou com `0`), o atendimento fica como estava:** se a conversa já estava em atendimento ou aguardando, continua no mesmo Setor e com o mesmo atendente. Só quando o contato não tinha atendimento em andamento antes do envio é que o atendimento é encerrado depois do envio.

◽ Só passa dentro da **janela de 24 horas**. Fora dela a Meta recusa, e o caminho é um template aprovado.

◽ A mensagem fica gravada no atendimento com o texto e os rótulos dos botões.

◽ Recusa da Meta vira mensagem de erro dentro do próprio atendimento.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

◽ Vai no nível de cima do corpo, ao lado de `openTicket`, e não dentro de `body`.

#### 📌 Opcional repetir até 3 botões.

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
    "type": "button",
    "header": {
      "type": "text",
      "text": "Promoção especial"
    },
    "body": {
      "text": "Temos uma oferta exclusiva para você. Como deseja prosseguir?"
    },
    "footer": {
        "text": "Válido até 31/12"
    },
    "buttons": [
      {
        "type": "reply",
        "reply": {
          "id": "ver_produtos",
          "title": "Ver produtos"
        }
      },
      {
        "type": "reply",
        "reply": {
          "id": "falar_vendedor",
          "title": "Falar com vendedor"
        }
      }
    ],
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendInteractive' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","ticketId":700,"type":"button","header":{"type":"text","text":"Promoção especial"},"body":{"text":"Temos uma oferta exclusiva para você. Como deseja prosseguir?"},"footer":{"text":"Válido até 31/12"},"buttons":[{"type":"reply","reply":{"id":"ver_produtos","title":"Ver produtos"}},{"type":"reply","reply":{"id":"falar_vendedor","title":"Falar com vendedor"}}],"openTicket":1,"queueId":1}'
```
