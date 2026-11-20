# API Listar Comentários da Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-comentarios-da-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Listar Comentários da Tarefa

---

🧩 Obter **os comentários de uma tarefa**, dos mais novos aos mais antigos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/comments
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

◽ O `tarefaId` vai no próprio endereço: é o `id` da tarefa.

◽ Cada comentário traz `id`, `content`, `createdAt` e o autor em `user` (`id`, `name` e `profile`).

◽ As menções aparecem no texto no formato da tela: `@[Maria Souza](17)`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/comments',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/comments' -H 'Authorization: Bearer {seutokenaqui}'
```
