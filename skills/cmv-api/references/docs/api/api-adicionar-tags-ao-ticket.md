# API Adicionar Tags ao Ticket

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-adicionar-tags-ao-ticket
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Adicionar Tags ao Ticket

---

🧩 Adiciona **tags em um atendimento,** sem tirar as que já estão.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/{ticketId}/tags
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
    "tags": [12, "VIP"]
}
```

➡️ **“ticketId”:** ID do Ticket — vai no próprio endereço, no lugar de `{ticketId}`. **Obrigatório.**

➡️ **“tags”:** lista de ids ou de nomes das tags. **Obrigatório.**

◽ Nome não diferencia maiúsculas de minúsculas. Aceita `[12, "VIP"]` e `"12,31"`.

◽ Adicionar uma tag que o atendimento já tem não altera nada.

◽ Tag que não existe na empresa faz a chamada falhar inteira, sem alterar nada.

⚠️ **Tag de raia do Kanban é exclusiva:** um atendimento fica numa raia só, então adicionar uma tag de raia **tira a raia anterior** — igual a arrastar o card no quadro. As tags comuns não são afetadas.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/{ticketId}/tags',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "tags": [12, "VIP"]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/{ticketId}/tags' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"tags":[12,"VIP"]}'
```
