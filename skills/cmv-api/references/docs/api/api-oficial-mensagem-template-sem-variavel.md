# API Oficial Mensagem Template sem variável

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-mensagem-template-sem-variavel
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Oficial Mensagem Template sem variável

---

🧩 Envia uma **mensagem template pela API oficial,** estando previamente aprovada.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendMetaCustom
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
    "openTicket": 1,
    "queueId": 100,
    "template": []
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“name”:** nome do template.

➡️ **“language”:** idioma.

➡️ **“openTicket”:** `0` não abre ticket e `1` abre. Para abrir é obrigatório informar um Setor em `queueId`, e a conversa vai para **Aguardando** mesmo que já esteja em atendimento.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“template”:** `array vazio`, porque este template não tem variável.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendMetaCustom',
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
    "openTicket": 1,
    "queueId": 100,
    "template": []
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendMetaCustom' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","name":"vars_001","language":"pt_BR","openTicket":1,"queueId":100,"template":[]}'
```
