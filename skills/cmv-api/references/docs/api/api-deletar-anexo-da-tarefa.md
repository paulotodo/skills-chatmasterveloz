# API Deletar Anexo da Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-anexo-da-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Deletar Anexo da Tarefa

---

🧩 Apaga **um anexo** de uma tarefa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/attachments/{anexoId}
```

##### Método

```
DELETE
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

◽ O `tarefaId` e o `anexoId` vão no próprio endereço: o `id` da tarefa e o `id` do anexo, que vem na lista de anexos. Anexo que não é da tarefa é recusado.

◽ Sem `userId`, quem apaga é a empresa, como o administrador na tela: apaga qualquer anexo.

◽ Para apagar em nome de quem anexou, acrescente `?userId=` com o ID dele ao endereço. Outra pessoa é recusada.

◽ A resposta é `{"message": "OK"}`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/attachments/{anexoId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/attachments/{anexoId}' -H 'Authorization: Bearer {seutokenaqui}'
```
