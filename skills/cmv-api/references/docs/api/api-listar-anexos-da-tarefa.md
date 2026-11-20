# API Listar Anexos da Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-anexos-da-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Listar Anexos da Tarefa

---

🧩 Obter **os anexos de uma tarefa**, dos mais novos aos mais antigos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/attachments
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

◽ Cada anexo traz `id`, `nomeOriginal`, `url` (o endereço do arquivo), `mimeType`, `tamanho` (em bytes), `createdAt` e quem anexou, em `user`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/attachments',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/attachments' -H 'Authorization: Bearer {seutokenaqui}'
```
