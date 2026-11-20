# API Oficial Template com variável (Hub)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-template-com-variavel-hub
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Oficial Template com variável (Hub)

---

🧩 Envia uma **mensagem template COM variável pela API oficial,** estando previamente aprovada.

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
    "language": "pt_BR",
    "template": [
        {
            "type": "text",
            "parameter_name": "variavel 1",
            "text": "valor 1"
        },
        {
            "type": "text",
            "parameter_name": "variavel 2",
            "text": "Valor 2"
        },
        {
            "type": "text",
            "parameter_name": "variavel 3",
            "text": "Valor 3"
        }
    ]
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“name”:** nome do template.

➡️ **“language”:** idioma.

➡️ **“template”:** uma entrada por variável do template, sendo que:

◽ `type`: tipo da variável.

◽ `parameter_name`: nome da variável definido no template (key).

◽ `text`: valor da variável (value).

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
    "language": "pt_BR",
    "template": [
        {
            "type": "text",
            "parameter_name": "variavel 1",
            "text": "valor 1"
        },
        {
            "type": "text",
            "parameter_name": "variavel 2",
            "text": "Valor 2"
        },
        {
            "type": "text",
            "parameter_name": "variavel 3",
            "text": "Valor 3"
        }
    ]
}',
// "parameter_name": utilize o nome da variável definido no template
// "text": defina o valor da variável
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendOfficial' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","name":"vars_001","language":"pt_BR","template":[{"type":"text","parameter_name":"variavel 1","text":"valor 1"},{"type":"text","parameter_name":"variavel 2","text":"Valor 2"},{"type":"text","parameter_name":"variavel 3","text":"Valor 3"}]}'
```
