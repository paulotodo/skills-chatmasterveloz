# API Mensagem de Lista

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-mensagem-de-lista
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Mensagem de Lista

---

🧩 Envia uma **mensagem com uma Lista de opções**, para o usuário escolher uma resposta. O título da opção é a resposta devolvida quando o lead escolhe.

**API:** Básica

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendList
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
  "body": "Selecione a melhor opção:",
  "optionList": {
    "buttonLabel": "Abrir lista de opções",
    "options": [
      {
        "id": "1",
        "title": "Título A",
        "description": "Descrição A"
      },
      {
        "id": "2",
        "title": "Título B",
        "description": "Descrição B"
      }
    ]
  }
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“body”:** texto logo acima do botão.

➡️ **“buttonLabel”:** texto do botão que, ao ser clicado, exibe as opções da lista.

➡️ **“options”:** cada opção da lista, sendo que:

◽ `id`: define o id da opção.

◽ `title`: título da opção.

◽ `description`: descrição da opção.

Adicione mais opções se desejar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendList',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
  "number": "5511955892164",
  "body": "Selecione a melhor opção:",
  "optionList": {
    "buttonLabel": "Abrir lista de opções",
    "options": [
      {
        "id": "1",
        "title": "Título A",
        "description": "Descrição A"
      },
      {
        "id": "2",
        "title": "Título B",
        "description": "Descrição B"
      }
    ]
  }
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendList' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","body":"Selecione a melhor opção:","optionList":{"buttonLabel":"Abrir lista de opções","options":[{"id":"1","title":"Título A","description":"Descrição A"},{"id":"2","title":"Título B","description":"Descrição B"}]}}'
```
