# API Obter um Agendamento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-um-agendamento
- **Categoria:** APIs
- **Menu:** APIs › Agendamentos › API Obter um Agendamento

---

🧩 Obter **uma mensagem agendada específica**, com o texto, a data de envio e a situação.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/schedules/{agendamentoId}
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
// sem payload
```

➡️ Esta chamada não tem payload.

◽ O `agendamentoId` vai no próprio endereço: é o `id` que vem na lista de agendamentos e na resposta da criação. Agendamento que não existe é recusado.

◽ O agendamento traz `id`, `texto`, `envioEm`, `enviadoEm`, `situacao` (`pendente`, `enviado` ou `erro`), `erroMotivo`, `repeticao`, `contato`, `conexaoId`, `usuario`, `setorId`, `abrirAtendimento` e `arquivo`.

◽ `repeticao` traz `repetir`, `repetirTodo` e `quantasVezes`, com os valores da criação.

◽ No agendamento de template, vêm também `template`, `templateVariables`, `headerMedia` e `buttonValues`.

◽ `envioEm` e `enviadoEm` vêm em UTC, com o `Z` no fim.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/schedules/{agendamentoId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/schedules/{agendamentoId}' -H 'Authorization: Bearer {seutokenaqui}'
```
