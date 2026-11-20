# API Mensagem de Lista

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-mensagem-de-lista-pro
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Mensagem de Lista

---

🧩 Envia uma **mensagem com uma Lista de opções**, para o usuário escolher uma resposta. O título da opção é a resposta devolvida quando o lead escolhe.

**API:** Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendListPRO
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
  "openTicket": 1,
  "queueId": 100,
  "body": {
    "Desc": "Selecione a melhor opção:",
    "ButtonText": "Abrir lista de opções",
    "TopText": "Escolha uma das opções",
    "List": [
      {
        "RowId": "1",
        "title": "Título A",
        "desc": "Descrição A"
      },
      {
        "RowId": "2",
        "title": "Título B",
        "desc": "Descrição B"
      },
      {
        "RowId": "3",
        "title": "Título C",
        "desc": "Descrição C"
      }
    ]
  }
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“openTicket”:** `0` não abre ticket e `1` abre. Para abrir é obrigatório informar um Setor em `queueId`, e a conversa vai para **Aguardando** mesmo que já esteja em atendimento.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“Desc”:** texto logo acima do botão.

➡️ **“ButtonText”:** texto do botão que, ao ser clicado, exibe as opções da lista.

➡️ **“TopText”:** texto logo acima das opções.

➡️ **“List”:** cada opção da lista, sendo que:

◽ `RowId`: define o id da opção.

◽ `title`: título da opção.

◽ `desc`: descrição da opção.

Adicione mais opções se desejar.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

◽ Vai no nível de cima do corpo, ao lado de `openTicket`, e não dentro de `body`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendListPRO',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
  "number": "5511955892164",
  "openTicket": 1,
  "queueId": 100,
  "body": {
    "Desc": "Selecione a melhor opção:",
    "ButtonText": "Abrir lista de opções",
    "TopText": "Escolha uma das opções",
    "List": [
      {
        "RowId": "1",
        "title": "Título A",
        "desc": "Descrição A"
      },
      {
        "RowId": "2",
        "title": "Título B",
        "desc": "Descrição B"
      },
      {
        "RowId": "3",
        "title": "Título C",
        "desc": "Descrição C"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendListPRO' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","openTicket":1,"queueId":100,"body":{"Desc":"Selecione a melhor opção:","ButtonText":"Abrir lista de opções","TopText":"Escolha uma das opções","List":[{"RowId":"1","title":"Título A","desc":"Descrição A"},{"RowId":"2","title":"Título B","desc":"Descrição B"},{"RowId":"3","title":"Título C","desc":"Descrição C"}]}}'
```
