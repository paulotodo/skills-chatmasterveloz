# API Mover Atendimento de Coluna

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-mover-atendimento-de-coluna
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Mover Atendimento de Coluna

---

🧩 Move **um atendimento para outra coluna** do quadro, como o arrasto do card na tela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/tickets/{ticketId}/mover?userId={userId}
```

##### Método

```
PUT
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "colunaId": 11
}
```

➡️ **“ticketId”:** ID do Ticket — vai no próprio endereço, no lugar de `{ticketId}`.

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

➡️ **“colunaId”:** a coluna de destino. **Obrigatório.**

◽ O que acontece com o atendimento depende do tipo da coluna:

◽ **Atendendo** e **Coluna de atendimento:** o atendimento fica aberto. Se ainda não estava aberto com um atendente, é aceito por quem está no `userId`.

◽ **Pendentes** e **Coluna de fila (pendente):** o atendimento volta para **Aguardando**, sem dono.

◽ **Coluna automática por fila** com um Setor: o atendimento vai para **Aguardando** naquele Setor, sem dono. Com mais de um Setor na coluna, a chamada é recusada.

➡️ **“userId”:** quem move — o ID de um usuário da empresa, no próprio endereço. **Obrigatório** quando o destino aceita o atendimento; nesse caso, sem ele, a chamada é recusada.

◽ Com o `userId`, só se move o que a pessoa vê no quadro.

◽ Para só levar ao **Aguardando**, ou classificar um atendimento que já tem atendente, o `userId` pode sair do endereço: quem move é a empresa.

◽ A resposta traz o atendimento como ficou.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/tickets/{ticketId}/mover?userId={userId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "colunaId": 11
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/tickets/{ticketId}/mover?userId={userId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"colunaId":11}'
```
