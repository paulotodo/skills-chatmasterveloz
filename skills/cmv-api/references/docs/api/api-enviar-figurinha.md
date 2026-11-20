# API Enviar Figurinha

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-figurinha
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Enviar Figurinha

---

🧩 Envia uma **figurinha da biblioteca** em um atendimento.

**API:** Pro, Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/figurinhas/enviar
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
    "ticketId": 700,
    "figurinhaId": "{figurinhaId}"
}
```

➡️ **“ticketId”:** o atendimento. Informe este ou o `number`.

➡️ **“figurinhaId”:** ID da figurinha na biblioteca da empresa. **Obrigatório.**

➡️ **“queueId”:** opcional. Setor para o atendimento que ainda **não tem** Setor; o que já tem fica como está.

➡️ **“quotedMsgId”:** opcional. ID interno da mensagem deste atendimento que a figurinha vai citar. De outro atendimento, é ignorado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/figurinhas/enviar',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": 700,
    "figurinhaId": "{figurinhaId}"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/figurinhas/enviar' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"figurinhaId":"{figurinhaId}"}'
```
