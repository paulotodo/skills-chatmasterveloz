# API Listar Mensagens do Ticket sem as Internas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-mensagens-do-ticket-sem-as-internas
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Listar Mensagens do Ticket sem as Internas

---

🧩 Listar as **mensagens de um atendimento**, podendo deixar de fora o que o cliente nunca viu.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/list
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
    "pageNumber": 1,
    "pageSize": 50,
    "semInternas": 1
}
```

➡️ **“ticketId”:** ID do Ticket. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

➡️ **“pageNumber”:** página. Padrão `1`, com as mensagens **mais recentes**; `2` traz o bloco anterior, e assim por diante.

➡️ **“pageSize”:** quantas mensagens por página. Padrão **50**, teto **200** — um valor maior não dá erro, é aparado para 200.

➡️ **“semInternas”:** `1` deixa de fora a **nota interna**, o marcador de sistema e o balão de falha de envio.

◽ São as linhas que **o cliente nunca viu**. Uma automação que responde ao cliente deve ignorá-las — senão ela lê como fala do cliente o que o operador escreveu para dentro.

◽ Com `0`, ou sem o campo, elas vêm no meio das outras, com o `mediaType` igual a `internal`.

◽ Com o `semInternas`, o total da resposta também as desconta.

⚠️ As páginas andam **para trás no tempo**: a 1 é a mais recente. Dentro de cada página, a mais antiga vem primeiro. Para montar o histórico inteiro, repita com `pageNumber` 2, 3… enquanto a resposta trouxer `"hasMore": true`.

◽ Os quatro campos valem tanto no corpo quanto na query da URL. Vindo nos dois, a query ganha — menos o `ticketId`, em que o corpo ganha.

◽ O `mediaUrl` de cada mensagem vem como endereço completo, pronto para baixar.

◽ Só leitura: não marca a conversa como lida nem avisa a tela de ninguém.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/list',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": 700,
    "pageNumber": 1,
    "pageSize": 50,
    "semInternas": 1
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/list' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"pageNumber":1,"pageSize":50,"semInternas":1}'
```
