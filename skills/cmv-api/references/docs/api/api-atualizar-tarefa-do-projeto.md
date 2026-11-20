# API Atualizar Tarefa do Projeto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-tarefa-do-projeto
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Atualizar Tarefa do Projeto

---

🧩 Atualiza **uma tarefa** de um projeto e a move de coluna.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos/{projetoId}/tarefas/{tarefaId}
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
    "etapaId": 39,
    "checklist": [
        {
            "id": "5d1a7c09b2e4",
            "texto": "Agendar o treinamento",
            "feito": true
        }
    ]
}
```

➡️ **“projetoId”** e **“tarefaId”:** IDs do projeto e da tarefa — vão no próprio endereço, no lugar de `{projetoId}` e `{tarefaId}`. **Obrigatórios.**

◽ Tarefa de outro projeto responde **não encontrada** (`404`).

➡️ **“etapaId”:** ID da coluna para onde a tarefa vai.

◽ Ir para a coluna que conclui fecha a tarefa; sair dela reabre.

➡️ **“checklist”:** a lista **inteira** de itens — substitui a anterior.

◽ Mande de volta o `id` de cada item que já existe, para ele continuar o mesmo. Item sem `id` vira um item novo.

◽ Também valem aqui os outros campos da criação — `title`, `description`, `priority`, `status`, `dueDate` e `assignedTo`. Em `dueDate` e `assignedTo`, `null` tira o valor.

◽ Os campos que você não enviar ficam como estão.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}/tarefas/{tarefaId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "etapaId": 39,
    "checklist": [
        {
            "id": "5d1a7c09b2e4",
            "texto": "Agendar o treinamento",
            "feito": true
        }
    ]
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token da Empresa
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X PUT 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}/tarefas/{tarefaId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"etapaId":39,"checklist":[{"id":"5d1a7c09b2e4","texto":"Agendar o treinamento","feito":true}]}'
```
