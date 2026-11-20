# API Obter uma Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-uma-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Obter uma Tarefa

---

🧩 Obter **uma tarefa completa**, com tudo o que a janela da tarefa mostra.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}
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

◽ O `tarefaId` vai no próprio endereço: é o `id` da tarefa. Tarefa que não existe, ou de outra empresa, é recusada.

◽ A tarefa traz `title`, `description`, `priority`, `status`, `dueDate`, o horário (`startTime` e `endTime`), o lembrete (`reminderMinutes`), o `tipo`, a sala da reunião (`sala`, `salaCodigo` e `meetingUrl`) e a recorrência (`isRecurring` e `recurringPattern`).

◽ Vêm também o `checklist`, com `texto` e `feito` de cada item, os `responsaveis` (todos, na ordem; o primeiro é o principal), o `sharedWith` e os vínculos dela (`ticketId`, `crmOportunidadeId`, `projetoId`).

◽ Quem criou vem em `creator`, e o responsável principal, em `assignee`.

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
curl -X GET 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}' -H 'Authorization: Bearer {seutokenaqui}'
```
