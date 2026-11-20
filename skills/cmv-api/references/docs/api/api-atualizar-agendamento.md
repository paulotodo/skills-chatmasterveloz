# API Atualizar Agendamento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-agendamento
- **Categoria:** APIs
- **Menu:** APIs › Agendamentos › API Atualizar Agendamento

---

🧩 Atualiza **uma mensagem agendada** que ainda não foi enviada.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/schedules/{agendamentoId}
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
    "body": "Olá! Sua consulta é amanhã às 10h.",
    "sendAt": "2026-12-31 11:30"
}
```

➡️ **“agendamentoId”:** ID do agendamento — vai no próprio endereço, no lugar de `{agendamentoId}`.

➡️ **“body”:** o texto novo, com pelo menos 5 caracteres.

➡️ **“sendAt”:** a nova data e hora de envio, no fuso da empresa, como `2026-12-31 11:30`. Precisa ficar no futuro.

◽ Na resposta, o `envioEm` vem em UTC: numa empresa no horário de Brasília, `2026-12-31 11:30` volta como `2026-12-31T14:30:00.000Z`.

◽ Mudam também `repetir`, `repetirTodo` e `quantasVezes` e, no agendamento de template, `template`, `templateVariables`, `headerMedia` e `buttonValues`, com os valores da criação.

◽ Mande só o que vai mudar. O contato não muda: o campo que não se edita volta em `camposIgnorados`.

⚠️ Só se edita o que ainda não foi enviado. O agendamento já enviado é recusado, e também o que está saindo nos próximos 30 segundos.

◽ O agendamento que tinha dado erro volta para a fila de envio.

◽ A resposta traz o `agendamento` como ficou e o `camposIgnorados`.

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
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "body": "Olá! Sua consulta é amanhã às 10h.",
    "sendAt": "2026-12-31 11:30"
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/schedules/{agendamentoId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"body":"Olá! Sua consulta é amanhã às 10h.","sendAt":"2026-12-31 11:30"}'
```
