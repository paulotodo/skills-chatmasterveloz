# API Deletar Oportunidade V1

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-oportunidade-v1
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Deletar Oportunidade V1

---

🧩 Apaga **uma oportunidade** permanentemente.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/oportunidade
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

```javascript
{
  "id": 147
}
```

➡️ **“id”:** ID da oportunidade. **Obrigatório.**

⚠️ **Não há como desfazer.** A exclusão é permanente.

⚠️ **A empresa precisa estar no CRM antigo.** Se já estiver no CRM novo, esta chamada é recusada — o registro não apareceria em quadro nenhum.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/oportunidade',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
  CURLOPT_POSTFIELDS =>'{
  "id": 147
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/oportunidade' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"id":147}'
```
