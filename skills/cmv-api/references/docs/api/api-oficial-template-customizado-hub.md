# API Oficial Template Customizado (Hub)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-template-customizado-hub
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Oficial Template Customizado (Hub)

---

🧩 Envia uma **mensagem template customizado pela API oficial,** estando previamente aprovada.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendOfficialCustom
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
                        "type": "header",
                        "parameters": [{
                                "type": "image",
                                "image": {
                                    "link": "https://URL/wp-content/uploads/2024/03/front-view-woman-holding-smartphone-removebg-preview.png"
                                }
                            }
                        ]
                    }, {
                        "type": "button",
                        "sub_type": "quick_reply",
                        "index": "0",
                        "parameters": [{
                                "type": "payload",
                                "payload": "Descadastrar"
                            }
                        ]
                    }, {
                        "type": "button",
                        "sub_type": "quick_reply",
                        "index": "1",
                        "parameters": [{
                                "type": "payload",
                                "payload": "Alterar Contato"
                            }
                        ]
                    }
                ]
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“name”:** nome do template.

➡️ **“language”:** idioma.

➡️ **“template”:** os componentes do template aprovado na Meta, sendo que:

◽ `type`: o componente — `header`, `body` ou `button`.

◽ `parameters`: o conteúdo daquele componente, no formato que a Meta espera.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendOfficialCustom',
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
                        "type": "header",
                        "parameters": [{
                                "type": "image",
                                "image": {
                                    "link": "https://URL/wp-content/uploads/2024/03/front-view-woman-holding-smartphone-removebg-preview.png"
                                }
                            }
                        ]
                    }, {
                        "type": "button",
                        "sub_type": "quick_reply",
                        "index": "0",
                        "parameters": [{
                                "type": "payload",
                                "payload": "Descadastrar"
                            }
                        ]
                    }, {
                        "type": "button",
                        "sub_type": "quick_reply",
                        "index": "1",
                        "parameters": [{
                                "type": "payload",
                                "payload": "Alterar Contato"
                            }
                        ]
                    }
                ]
}
',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendOfficialCustom' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","name":"vars_001","language":"pt_BR","template":[{"type":"header","parameters":[{"type":"image","image":{"link":"https://URL/wp-content/uploads/2024/03/front-view-woman-holding-smartphone-removebg-preview.png"}}]},{"type":"button","sub_type":"quick_reply","index":"0","parameters":[{"type":"payload","payload":"Descadastrar"}]},{"type":"button","sub_type":"quick_reply","index":"1","parameters":[{"type":"payload","payload":"Alterar Contato"}]}]}'
```
