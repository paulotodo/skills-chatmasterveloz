# API Listar Tarefas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-tarefas
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Listar Tarefas

---

🧩 Listar **tarefas** da empresa, com filtros pela URL.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/list?status={statusDaTarefa}&priority={priorityDaTarefa}&userId={userId}
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
// sem payload — os filtros vão na própria URL
```

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, por exemplo `?status=pending&priority=medium`.

◽ **“status”:** `pending` ou `completed`.

◽ **“priority”:** `high`, `medium` ou `low`.

◽ **“createdBy”:** só as criadas por aquele atendente.

◽ **“assignedTo”:** só as designadas para aquele atendente.

◽ **“sharedWith”:** só as compartilhadas com aquele atendente.

◽ **“userId”:** as criadas por, designadas para **ou** compartilhadas com aquele atendente.

⚠️ **Esses quatro filtros de pessoa se excluem, nesta ordem:** `createdBy`, `assignedTo`, `sharedWith`, `userId`. Se você mandar mais de um, **só o primeiro da ordem vale** e os outros são ignorados, sem aviso.

◽ **“ticketId”:** só as vinculadas àquele Ticket. Este soma-se a qualquer um dos outros.

◽ Cada tarefa vem com quem criou e quem é o responsável, das mais prioritárias e mais recentes para as demais.

◽ Não há páginas: a lista vem inteira.

◽ Qualquer falha responde **erro de servidor** — por exemplo uma prioridade fora das três.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/list?status={statusDaTarefa}&priority={priorityDaTarefa}&userId={userId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/tasks/list?status={statusDaTarefa}&priority={priorityDaTarefa}&userId={userId}' -H 'Authorization: Bearer {seutokenaqui}'
```
