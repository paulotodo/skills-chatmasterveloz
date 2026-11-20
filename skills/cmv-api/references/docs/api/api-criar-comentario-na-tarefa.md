# API Criar Comentário na Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-comentario-na-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Criar Comentário na Tarefa

---

🧩 Cria **um comentário** numa tarefa, em nome de uma pessoa da equipe.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/comments?userId={userId}
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
    "content": "Cliente confirmou. @[Maria Souza](17), pode seguir com a proposta."
}
```

➡️ **“tarefaId”:** ID da tarefa — vai no próprio endereço, no lugar de `{tarefaId}`.

➡️ **“userId”:** o autor do comentário — o ID de um usuário da empresa, no endereço ou no payload. **Obrigatório.**

➡️ **“content”:** o texto do comentário. **Obrigatório.**

◽ Para mencionar alguém, use o formato da tela: `@[Nome](id)`, como `@[Maria Souza](17)`. Quem é mencionado e quem acompanha a tarefa recebem o aviso.

◽ A resposta traz o comentário com `id`, `content`, `createdAt` e o autor em `user`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/comments?userId={userId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "content": "Cliente confirmou. @[Maria Souza](17), pode seguir com a proposta."
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/comments?userId={userId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"content":"Cliente confirmou. @[Maria Souza](17), pode seguir com a proposta."}'
```
