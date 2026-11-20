# API Oficial Template sem variável (Hub)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-template-sem-variavel-hub
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Oficial Template sem variável (Hub)

---

🧩 Envia uma **mensagem template SEM variável pela API oficial,** estando previamente aprovada.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendOfficial
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
    "number": "5511955892164",
    "name": "vars_001",
    "language": "pt_BR"
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“name”:** nome do template.

➡️ **“language”:** idioma.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendOfficial',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "name": "vars_001",
    "language": "pt_BR"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendOfficial' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","name":"vars_001","language":"pt_BR"}'
```
