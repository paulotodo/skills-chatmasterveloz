# API Buscar Tickets por Filtro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-buscar-tickets-por-filtro
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Buscar Tickets por Filtro

---

🧩 Obter a **lista de atendimentos** que casam com um filtro de tags, situação, Setor e tempo parado.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/search
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
    "tagIds": [3, 8],
    "statuses": ["open", "pending"],
    "queueIds": [4],
    "connectionId": 3,
    "updatedBeforeMinutes": 60,
    "limit": 50
}
```

➡️ **“tagIds”:** ids das tags. O atendimento entra se tiver **qualquer** uma delas. Aceita também `"3,8"`.

➡️ **“statuses”:** situação do atendimento — `open`, `pending` ou `closed`. Aceita também `"open,pending"`.

➡️ **“queueIds”:** ids dos Setores. Aceita também `"4,5"`.

➡️ **“connectionId”:** id da conexão. Traz só os atendimentos dela.

➡️ **“updatedBeforeMinutes”:** só os atendimentos parados há mais de X minutos.

◽ Conta como movimento qualquer mensagem e qualquer troca de situação, de Setor ou de operador.

➡️ **“limit”:** quantos atendimentos trazer. Padrão `50`, teto `200`.

➡️ **“offset”:** opcional. De qual atendimento começar, para paginar.

◽ Todos os campos são opcionais: sem filtro nenhum, vêm os atendimentos da empresa.

◽ A lista vem com os parados há mais tempo primeiro.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/search',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "tagIds": [3, 8],
    "statuses": ["open", "pending"],
    "queueIds": [4],
    "connectionId": 3,
    "updatedBeforeMinutes": 60,
    "limit": 50
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/search' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"tagIds":[3,8],"statuses":["open","pending"],"queueIds":[4],"connectionId":3,"updatedBeforeMinutes":60,"limit":50}'
```
