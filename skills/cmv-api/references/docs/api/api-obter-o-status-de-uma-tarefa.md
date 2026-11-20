# API Obter o Status de uma Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-o-status-de-uma-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Obter o Status de uma Tarefa

---

🧩 Obter o **resumo de uma tarefa**: em que pé ela está, para quem é e até quando.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/status
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
// sem payload — a tarefa vai no endereço
```

➡️ **“tarefaId”:** ID da tarefa — vai no próprio endereço, no lugar de `{tarefaId}`. **Obrigatório.**

◽ A resposta traz o título, a situação, a prioridade, o prazo, quem criou e quem é o responsável.

◽ Só leitura: esta chamada não altera nada.

◽ Tarefa que não existe, ou de outra empresa, responde **não encontrada**.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/status',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/status' -H 'Authorization: Bearer {seutokenaqui}'
```
