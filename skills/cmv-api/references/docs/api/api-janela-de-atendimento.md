# API Janela de Atendimento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-janela-de-atendimento
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Janela de Atendimento

---

🧩 Obter em que ponto da **janela de atendimento** está um atendimento.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/{ticketId}/janela
```

##### Método

```
GET
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```
// sem payload — o ticketId vai no endereço
```

➡️ **“ticketId”:** ID do Ticket — vai no próprio endereço, no lugar de `{ticketId}`. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

◽ O **25678** é o protocolo, e não serve nesta chamada.

◽ A resposta diz se a janela está **aberta**, quanto tempo falta para ela fechar e se o envio exige mensagem de template.

◽ A regra muda por canal: na API oficial são 24 horas contadas da última mensagem **do cliente**; no Messenger e no Instagram são 24 horas livres e mais alguns dias só com atendimento humano; nos demais canais não existe janela, e a resposta vem sempre aberta.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/{ticketId}/janela',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/tickets/{ticketId}/janela' -H 'Authorization: Bearer {seutokenaqui}'
```
