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
    "dueDate": "2028-12-30T23:59:59.000Z",
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

◽ Este campo **não é conferido** contra a empresa: um id de outra empresa é gravado do mesmo jeito. Informe um atendente da sua.

➡️ **“title”:** título da tarefa. **Obrigatório.**

➡️ **“description”:** descrição da tarefa.

➡️ **“priority”:** `high`, `medium` ou `low`. Sem informar, entra como `medium`.

➡️ **“assignedTo”:** ID do atendente a quem a tarefa foi designada.

◽ Ele é avisado na hora, por notificação e pela tela, como numa tarefa criada pelo painel.

➡️ **“ticketId”:** ID do Ticket ao qual a tarefa fica vinculada.

➡️ **“dueDate”:** data de vencimento, no formato ISO 8601 — `AAAA-MM-DDTHH:mm:ss.sssZ`.

◽ Também aceita só a data, `AAAA-MM-DD`: nesse caso ela é gravada ao meio-dia UTC, para não escorregar um dia por causa do fuso.

➡️ **“checklist”:** os itens da tarefa, um objeto por item, com `texto` e, se quiser, `feito` (`true` quando o item já foi feito).

◽ No máximo 100 itens, de até 500 caracteres cada. Item sem texto é descartado.

◽ A tarefa nasce como **pendente**.

◽ Qualquer falha responde **erro de servidor** — inclusive título vazio ou `createdBy` ausente. Não é sinal de que a plataforma está com problema.

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
    "dueDate": "2028-12-30T23:59:59.000Z",
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tasks/create' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"createdBy":1,"title":"Nova tarefa via API","description":"Descrição da tarefa","priority":"high","assignedTo":4,"ticketId":700,"dueDate":"2028-12-30T23:59:59.000Z","checklist":[{"texto":"Separar a proposta"},{"texto":"Enviar ao cliente","feito":false}]}'
```
