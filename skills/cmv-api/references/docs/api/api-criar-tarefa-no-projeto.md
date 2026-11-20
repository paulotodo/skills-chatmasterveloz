# API Criar Tarefa no Projeto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-tarefa-no-projeto
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Criar Tarefa no Projeto

---

🧩 Cria **uma tarefa** dentro de um projeto, com checklist.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos/{projetoId}/tarefas
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
    "title": "Treinar a equipe da loja",
    "description": "Treinamento presencial com os vendedores",
    "priority": "high",
    "dueDate": "2026-11-20",
    "assignedTo": 4,
    "etapaId": 36,
    "checklist": [
        {
            "texto": "Agendar o treinamento"
        },
        {
            "texto": "Enviar o material",
            "feito": true
        }
    ],
    "userId": 4
}
```

➡️ **“projetoId”:** ID do projeto — vai no próprio endereço, no lugar de `{projetoId}`. **Obrigatório.**

➡️ **“title”:** título da tarefa. **Obrigatório.**

➡️ **“description”:** descrição da tarefa.

➡️ **“priority”:** `high`, `medium` ou `low`. Sem informar, entra como `medium`.

➡️ **“dueDate”:** prazo, no formato `AAAA-MM-DD` — gravado ao meio-dia UTC, para não escorregar um dia por causa do fuso.

◽ Também aceita data e hora, no formato ISO 8601.

➡️ **“assignedTo”:** ID do usuário que cumpre a tarefa.

➡️ **“etapaId”:** ID da coluna em que a tarefa nasce. Sem ele, ela nasce na primeira coluna do projeto.

◽ Na coluna que conclui, a tarefa já nasce concluída.

➡️ **“checklist”:** os itens da tarefa, cada um com o `texto` e, quando já foi feito, `"feito": true`.

◽ No máximo 100 itens, de até 500 caracteres cada.

➡️ **“userId”:** ID do usuário em nome de quem a tarefa é criada.

◽ A tarefa do projeto é uma tarefa como as outras: aparece também em **Tarefas** e na agenda.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}/tarefas',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "title": "Treinar a equipe da loja",
    "description": "Treinamento presencial com os vendedores",
    "priority": "high",
    "dueDate": "2026-11-20",
    "assignedTo": 4,
    "etapaId": 36,
    "checklist": [
        {
            "texto": "Agendar o treinamento"
        },
        {
            "texto": "Enviar o material",
            "feito": true
        }
    ],
    "userId": 4
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
curl -X POST 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}/tarefas' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"title":"Treinar a equipe da loja","description":"Treinamento presencial com os vendedores","priority":"high","dueDate":"2026-11-20","assignedTo":4,"etapaId":36,"checklist":[{"texto":"Agendar o treinamento"},{"texto":"Enviar o material","feito":true}],"userId":4}'
```
