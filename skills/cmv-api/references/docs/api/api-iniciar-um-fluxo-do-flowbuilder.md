# API Iniciar um Fluxo do FlowBuilder Nativo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-iniciar-um-fluxo-do-flowbuilder
- **Categoria:** APIs
- **Menu:** APIs › Fluxos › API Iniciar um Fluxo do FlowBuilder Nativo

---

🧩 Inicia **um fluxo do flowbuilder,** de forma passiva, ou seja, sem interação do usuário.

Nessa fase inicial, o envio é **somente** para mensagens de texto.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/flowbuilderStart
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
    "queueId": "3"
  }
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“queueId”:** ID do Setor que está vinculado ao fluxo desejado.

⚠️ Ao chamar essa API, o ticket será transferido para o status **Aguardando**.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/flowbuilderStart',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "queueId": "3"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/flowbuilderStart' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","queueId":"3"}'
```
