# API Criar Agendamento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-agendamento
- **Categoria:** APIs
- **Menu:** APIs › Agendamentos › API Criar Agendamento

---

🧩 Cria uma **mensagem agendada**, para um contato previamente cadastrado.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/schedules
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
    "body":"Teste de Agendamento",
    "sendAt":"2023-12-17T22:00:00.000Z",
    "contactId":"24294",
    "userId":"34",
    "openTicket":"0",
    "queueId":"0",
    "whatsappId":"2",
    "repetir":"0", //0 = Não Repetir, 999 = Todo Dia (repetirTodo)
    "repetirTodo":"0", //0 = Não Repetir, 999 = Aniversário
    "quantasVezes":"0"
}
```

➡️ **“body”:** texto da mensagem agendada. **Obrigatório.**

➡️ **“sendAt”:** data de envio no formato ANO-MES-DIA(letra T)HORA:MINUTO. Exemplo: `2029-11-20T07:52` **Obrigatório.**

➡️ **“contactId”:** ID do contato. **Obrigatório.**

➡️ **“userId”:** ID do usuário atendente. **Obrigatório.**

➡️ **“openTicket”:** `0` não abre ticket e `1` abre. Para abrir é obrigatório informar um Setor em `queueId`, e a conversa vai para **Aguardando** mesmo que já esteja em atendimento.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“whatsappId”:** ID da conexão remetente. **Obrigatório.**

➡️ **“repetir”:** `0` não repete e `999` repete todo dia.

➡️ **“repetirTodo”:** `0` não repete e `999` repete no aniversário.

➡️ **“quantasVezes”:** quantidade de vezes que a mensagem será repetida.

➡️ **“notation”:** `1` grava o texto como **anotação interna** no atendimento, em vez de mandar a mensagem ao cliente.

➡️ **“template”:** o template aprovado, para agendar o envio nos canais oficiais.

◽ Acompanham o template os campos `templateVariables` (os valores das variáveis), `headerMedia` (a mídia do cabeçalho) e `buttonValues` (os valores dos botões).

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/schedules',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "body":"Teste de Agendamento",
    "sendAt":"2023-12-17T22:00:00.000Z",
    "contactId":"24294",
    "userId":"34",
    "openTicket":"0",
    "queueId":"0",
    "whatsappId":"2",
    "repetir":"0", //0 = Não Repetir, 999 = Todo Dia (repetirTodo)
    "repetirTodo":"0", //0 = Não Repetir, 999 = Aniversário
    "quantasVezes":"0"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/schedules' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"body":"Teste de Agendamento","sendAt":"2023-12-17T22:00:00.000Z","contactId":"24294","userId":"34","openTicket":"0","queueId":"0","whatsappId":"2","repetir":"0","repetirTodo":"0","quantasVezes":"0"}'
```
