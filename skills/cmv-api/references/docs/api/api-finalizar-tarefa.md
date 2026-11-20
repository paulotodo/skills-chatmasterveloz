# API Finalizar Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-finalizar-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Finalizar Tarefa

---

🧩 Marca **uma tarefa como concluída**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/complete
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

```
// sem payload — a tarefa vai no endereço
```

➡️ **“tarefaId”:** ID da tarefa — vai no próprio endereço, no lugar de `{tarefaId}`. **Obrigatório.**

◽ Concluir pela API é o mesmo que concluir pela tela: a tarefa sai da agenda do Google, quando estava lá.

◽ A resposta traz a tarefa com quem criou e quem é o responsável.

◽ Tarefa que não existe, ou de outra empresa, responde **erro de servidor** — e não "não encontrada". É assim mesmo: não é sinal de que a plataforma está com problema.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/complete',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/complete' -H 'Authorization: Bearer {seutokenaqui}'
```
