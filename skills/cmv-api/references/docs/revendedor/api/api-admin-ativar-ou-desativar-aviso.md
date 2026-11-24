# API Ativar ou Desativar Aviso

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-ativar-ou-desativar-aviso
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Avisos › API Ativar ou Desativar Aviso

---

🧩 **Tira do ar ou devolve ao ar** um aviso, sem mexer no resto.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/announcements/toggle-status
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
    "id": 5
}
```

➡️ **“id”:** ID do aviso. **Obrigatório.**

◽ A chamada **inverte** o estado: aviso no ar sai, aviso fora do ar volta. Não existe mandar o valor.

◽ A resposta traz o aviso já com o novo estado, e as telas são avisadas na hora.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/announcements/toggle-status',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "id": 5
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/announcements/toggle-status' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"id":5}'
```
