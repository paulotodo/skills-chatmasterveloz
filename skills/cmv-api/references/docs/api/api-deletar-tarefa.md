# API Deletar Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Deletar Tarefa

---

🧩 Manda **uma tarefa** para a lixeira.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}
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
// sem payload — a tarefa vai no endereço
```

➡️ **“tarefaId”:** ID da tarefa — vai no próprio endereço, no lugar de `{tarefaId}`. **Obrigatório.**

⚠️ A tarefa vai para **Excluídas**: some das listas e das contagens. Dali ela pode ser restaurada ou excluída de vez pela tela, no menu **Tarefas**. Essas duas ações não têm rota na API. Na lista, ela aparece como *Excluída pela API*.

◽ O evento correspondente sai da agenda do Google, quando existe.

◽ Tarefa que não existe, ou de outra empresa, responde **não encontrada**.

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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}' -H 'Authorization: Bearer {seutokenaqui}'
```
