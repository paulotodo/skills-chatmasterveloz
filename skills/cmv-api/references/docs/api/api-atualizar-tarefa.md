# API Atualizar Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Atualizar Tarefa

---

🧩 Atualiza **uma tarefa** — só o que vier no corpo muda.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}
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
    "title": "Retornar ligação do cliente",
    "description": "Cliente pediu retorno à tarde",
    "priority": "high",
    "assignedTo": 4,
    "dueDate": "2028-12-30T23:59:59.000Z",
    "checklist": [
        {
            "texto": "Ligar para o cliente",
            "feito": true
        },
        {
            "texto": "Registrar o retorno"
        }
    ]
}
```

➡️ **“tarefaId”:** ID da tarefa — vai no próprio endereço, no lugar de `{tarefaId}`. **Obrigatório.**

➡️ **“title”:** novo título da tarefa.

➡️ **“description”:** nova descrição.

➡️ **“priority”:** `high`, `medium` ou `low`.

➡️ **“assignedTo”:** ID do atendente responsável. Mande `0` para deixar a tarefa sem responsável.

➡️ **“dueDate”:** prazo, no formato ISO 8601 — `AAAA-MM-DDTHH:mm:ss.sssZ`. Mande `null` para tirar o prazo.

➡️ **“status”:** `pending` para a tarefa em aberto, `completed` para concluída.

➡️ **“ticketId”:** ID do atendimento vinculado. Mande `0` ou `null` para desvincular.

➡️ **“checklist”:** a lista inteira de itens, com `texto` e `feito` (`true` quando o item foi feito). **Substitui a lista anterior** — o item que não vier sai.

◽ Para um item continuar o mesmo, mande junto o `id` que ele já tem. Sem o `id`, o item entra como novo.

◽ `[]` tira todos os itens. Sem o campo `checklist`, a lista fica como está.

◽ Os campos que você não enviar ficam como estão.

◽ Quando a tarefa está sincronizada com a agenda do Google, o evento de lá acompanha a mudança.

◽ A resposta traz a tarefa com quem criou, o responsável e o atendimento vinculado.

◽ Tarefa que não existe, ou de outra empresa, responde **erro de servidor** — e não "não encontrada". É assim mesmo: não é sinal de que a plataforma está com problema.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "title": "Retornar ligação do cliente",
    "description": "Cliente pediu retorno à tarde",
    "priority": "high",
    "assignedTo": 4,
    "dueDate": "2028-12-30T23:59:59.000Z",
    "checklist": [
        {
            "texto": "Ligar para o cliente",
            "feito": true
        },
        {
            "texto": "Registrar o retorno"
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"title":"Retornar ligação do cliente","description":"Cliente pediu retorno à tarde","priority":"high","assignedTo":4,"dueDate":"2028-12-30T23:59:59.000Z","checklist":[{"texto":"Ligar para o cliente","feito":true},{"texto":"Registrar o retorno"}]}'
```
