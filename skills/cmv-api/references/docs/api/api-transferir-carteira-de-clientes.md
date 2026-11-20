# API Transferir Carteira de Clientes

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-transferir-carteira-de-clientes
- **Categoria:** APIs
- **Menu:** APIs › Equipe › API Transferir Carteira de Clientes

---

🧩 Transfere toda a **Carteira de Clientes** de um membro da Equipe para outro.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/contacts/changecarteira
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
    "OLD_carteiraId":39,
    "NEW_carteiraId":40
  }
```

➡️ **“OLD_carteiraId”:** ID do usuário da Equipe que entrega a carteira. **Obrigatório.**

➡️ **“NEW_carteiraId”:** ID do usuário da Equipe que recebe a carteira. **Obrigatório.**

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/contacts/changecarteira',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "OLD_carteiraId":39,
    "NEW_carteiraId":40
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
curl -X POST 'https://api2.chatmasterveloz.com/api/contacts/changecarteira' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"OLD_carteiraId":39,"NEW_carteiraId":40}'
```
