# API Transferir Tickets para um Setor

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-transferir-tickets-para-um-setor
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Transferir Tickets para um Setor

---

🧩 Transfere **todos os atendimentos da conexão** para um Setor específico.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/changequeue
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
    "NEW_queueId":94
  }
```

➡️ **“NEW_queueId”:** ID do Setor que vai receber os atendimentos. **Obrigatório.**

⚠️ **A chamada move TODOS os atendimentos da conexão do token** — em atendimento, aguardando e também os já encerrados, de qualquer Setor. Não existe filtro: não dá para transferir só os de um Setor.

◽ Não mexe no status nem no operador, e não manda nada ao cliente.

◽ Setor que não existe, ou que é de outra empresa, é recusado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/changequeue',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "NEW_queueId":94
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/changequeue' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"NEW_queueId":94}'
```
