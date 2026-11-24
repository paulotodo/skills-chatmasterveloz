# API Recuperar Mensagens

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-recuperar-mensagens
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Conexões › API Recuperar Mensagens

---

🧩 Repõe na conversa as **mensagens que chegaram ao webhook e não foram gravadas**, sem enviar nada ao contato.

➡️ **O problema:** o contato escreve *"Quero o boleto"* às 14h52. A plataforma avisa o sistema do seu cliente pelo webhook, mas a mensagem não fica gravada no Ticket: o sistema recebeu, e o atendente abre a conversa e não vê nada.

➡️ **O que a chamada faz:** o sistema devolve à plataforma o evento que recebeu, e a mensagem aparece na conversa às 14h52, no lugar certo do histórico, mesmo com o Ticket encerrado.

➡️ **O que ela não faz:** nada é enviado ao contato, nenhum webhook ou automação é disparado, o status do Ticket não muda e a última mensagem da lista continua a mesma.

➡️ **Quem consegue usar:** quem guardou os eventos do webhook. É uma chamada de conserto, para quando faltar mensagem, e não para o dia a dia.

⚠️ Esta chamada **não** depende do token do Super Admin. Funciona com o token da Conexão do Ticket, ou com o Token da Empresa informando a Conexão. Por isso, o seu cliente consegue usá-la com o token dele.

⚠️ **A plataforma não confere se o evento veio mesmo do webhook.** Quem tem o token consegue gravar qualquer texto em um Ticket da Conexão, em nome do contato ou da equipe, com qualquer data, e na conversa a mensagem aparece igual às outras. Passe esta chamada ao seu cliente só se ele precisar.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/recuperar
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
    "eventos": [
      {
        "mensagem": [
          {
            "type": "text",
            "text": "Quero o boleto"
          }
        ],
        "fromMe": false,
        "chamadoId": 700,
        "data": "2026-11-04T17:52:10.000Z"
      }
    ]
}
```

➡️ **“ticketId”:** ID do Ticket onde as mensagens entram. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

⚠️ O Ticket precisa ser da Conexão usada na chamada. De outra Conexão, a chamada é recusada com **400** `ERR_TICKET_DE_OUTRA_CONVERSA`.

➡️ **“eventos”:** os eventos do webhook, do jeito que chegaram ao sistema, até **500** por chamada. **Obrigatório.**

◽ Cada evento vira uma mensagem do histórico, na hora em que chegou.

➡️ **“mensagem”:** o texto do evento. Sem texto, o evento é recusado.

◽ Mídia entra só com o rótulo, como **Imagem**, sem o arquivo.

➡️ **“fromMe”:** `false` para mensagem do contato e `true` para mensagem da equipe.

➡️ **“chamadoId”:** ID do Ticket que veio no evento. Se for de outro Ticket, o evento é recusado.

➡️ **“data”:** opcional. A hora em que a mensagem chegou. Quando informada, vale mais que a hora do evento.

◽ O `Z` no fim indica o horário **UTC**: `17:52` em UTC são **14h52** em Brasília.

◽ Sem ela, vale a hora que veio no evento: `ticketData.updatedAt` ou `msg.messageTimestamp`. Sem nenhuma hora, o evento é recusado.

⚠️ Use sempre o formato do exemplo. Só com o dia, sem a hora, a mensagem entra à meia-noite em UTC.

➡️ **Mandar o mesmo evento de novo não duplica a mensagem.**

◽ Com o `msg.key.id` no evento, a repetição é reconhecida por ele. Sem ele, pelo Ticket, pela hora, por quem mandou e pelo texto.

➡️ **A resposta traz `gravadas`, `jaExistiam` e `recusados`.** Cada recusado vem com o `indice` do evento, a partir de `0`, e o `motivo`.

◽ A chamada responde **200** mesmo com evento recusado. Confira sempre `recusados`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/recuperar',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": 700,
    "eventos": [
      {
        "mensagem": [
          {
            "type": "text",
            "text": "Quero o boleto"
          }
        ],
        "fromMe": false,
        "chamadoId": 700,
        "data": "2026-11-04T17:52:10.000Z"
      }
    ]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/recuperar' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"eventos":[{"mensagem":[{"type":"text","text":"Quero o boleto"}],"fromMe":false,"chamadoId":700,"data":"2026-11-04T17:52:10.000Z"}]}'
```
