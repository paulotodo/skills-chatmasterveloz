# API Deletar Agendamento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-agendamento
- **Categoria:** APIs
- **Menu:** APIs › Agendamentos › API Deletar Agendamento

---

🧩 Deleta uma **mensagem agendada via API**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/schedules/delete
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
    "scheduleId":"55"
}
```

➡️ **“scheduleId”:** ID do agendamento realizado via API.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/schedules/delete',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "scheduleId":"55"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/schedules/delete' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"scheduleId":"55"}'
```
