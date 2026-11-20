# API Criar Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Criar Tarefa

---

🧩 Cria **uma tarefa** na empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/create
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
    "createdBy": 1,
    "title": "Nova tarefa via API",
    "description": "Descrição da tarefa",
    "priority": "high",
    "assignedTo": 4,
    "ticketId": 700,
    "dueDate": "2028-12-30",
    "startTime": "09:00",
    "endTime": "10:30",
    "reminderMinutes": 15,
    "tipo": "reuniao",
    "sala": "nossa",
    "sharedWith": [5],
    "isRecurring": true,
    "recurringPattern": "weekly",
    "recurringOptions": {
        "daysOfWeek": [1, 3]
    },
    "checklist": [
        {
            "texto": "Separar a proposta"
        },
        {
            "texto": "Enviar ao cliente",
            "feito": false
        }
    ]
}
```

➡️ **“createdBy”:** ID do atendente que está criando a tarefa. **Obrigatório.**

◽ Precisa ser um atendente da sua empresa: de outra, a chamada é recusada.

➡️ **“title”:** título da tarefa. **Obrigatório.**

➡️ **“description”:** descrição da tarefa.

➡️ **“priority”:** `high`, `medium` ou `low`. Sem informar, entra como `medium`.

➡️ **“assignedTo”:** ID do atendente a quem a tarefa foi designada.

◽ Ele é avisado na hora, por notificação e pela tela, como numa tarefa criada pelo painel.

➡️ **“ticketId”:** ID do Ticket ao qual a tarefa fica vinculada.

➡️ **“dueDate”:** data de vencimento. Só a data, `AAAA-MM-DD`, é gravada ao meio-dia UTC, para não escorregar um dia por causa do fuso.

◽ Também aceita data e hora no formato ISO 8601 — `AAAA-MM-DDTHH:mm:ss.sssZ`.

➡️ **“startTime”:** horário de início, `HH:MM`, no fuso da empresa. Vazio ou `null`: a tarefa fica sem horário.

➡️ **“endTime”:** horário de fim, no mesmo formato. Não pode vir antes do início.

➡️ **“reminderMinutes”:** o lembrete, em minutos antes: `5`, `15`, `30`, `60`, `120` ou `1440` — as opções da janela **Editar Tarefa**. Vazio, `null` ou `0`: sem lembrete.

➡️ **“tipo”:** `lembrete`, `reuniao`, `ligacao`, `email`, `visita` ou `tarefa`. Vazio: sem tipo.

➡️ **“sala”:** só na reunião — `nossa` (a sala de vídeo da plataforma), `meet` (o Google Meet, pela agenda) ou `nenhuma`.

➡️ **“sharedWith”:** os IDs dos atendentes da empresa com quem a tarefa é compartilhada.

➡️ **“isRecurring”:** `true` para a tarefa se repetir: ao concluir, nasce a próxima. Com `true`, o `recurringPattern` é obrigatório.

➡️ **“recurringPattern”:** `daily`, `weekly`, `monthly` ou `yearly`.

➡️ **“recurringOptions”:** só no semanal — os dias em `daysOfWeek`, de `0` (domingo) a `6` (sábado).

➡️ **“checklist”:** os itens da tarefa, um objeto por item, com `texto` e, se quiser, `feito` (`true` quando o item já foi feito).

◽ No máximo 100 itens, de até 500 caracteres cada. Item sem texto é descartado.

➡️ **“sincronizarAgenda”:** fora do exemplo. `true` põe a tarefa na agenda do Google do responsável, como a opção da janela; `false` tira.

◽ A tarefa nasce como **pendente**.

◽ A janela **Editar Tarefa** mostra o que a chamada gravou — o tipo, a sala, o lembrete e a repetição —, e o histórico da tarefa diz que ela foi criada *Pela API*.

◽ Quando algo vem fora do esperado — título vazio, `createdBy` ausente ou de outra empresa, um valor que o campo não aceita —, a chamada é recusada e a resposta diz qual campo corrigir.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/create',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "createdBy": 1,
    "title": "Nova tarefa via API",
    "description": "Descrição da tarefa",
    "priority": "high",
    "assignedTo": 4,
    "ticketId": 700,
    "dueDate": "2028-12-30",
    "startTime": "09:00",
    "endTime": "10:30",
    "reminderMinutes": 15,
    "tipo": "reuniao",
    "sala": "nossa",
    "sharedWith": [5],
    "isRecurring": true,
    "recurringPattern": "weekly",
    "recurringOptions": {
        "daysOfWeek": [1, 3]
    },
    "checklist": [
        {
            "texto": "Separar a proposta"
        },
        {
            "texto": "Enviar ao cliente",
            "feito": false
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tasks/create' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"createdBy":1,"title":"Nova tarefa via API","description":"Descrição da tarefa","priority":"high","assignedTo":4,"ticketId":700,"dueDate":"2028-12-30","startTime":"09:00","endTime":"10:30","reminderMinutes":15,"tipo":"reuniao","sala":"nossa","sharedWith":[5],"isRecurring":true,"recurringPattern":"weekly","recurringOptions":{"daysOfWeek":[1,3]},"checklist":[{"texto":"Separar a proposta"},{"texto":"Enviar ao cliente","feito":false}]}'
```
