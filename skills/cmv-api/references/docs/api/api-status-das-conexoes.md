# API Status das Conexões

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-status-das-conexoes
- **Categoria:** APIs
- **Menu:** APIs › Conexões › API Status das Conexões

---

🧩 Obter o **status de todas as Conexões** da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/whatsapp-status
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

```
// sem payload
```

➡️ Esta chamada não tem payload.

◽ A resposta traz **todas as Conexões da empresa** dona do token — não só a Conexão usada na chamada.

◽ Cada Conexão vem com o id, o nome, o canal, o status e as mensagens automáticas configuradas nela.

◽ Com o **Token da Empresa**, esta chamada vai sem informar Conexão e traz todas as Conexões da empresa, com o id de cada uma. Se você informar uma Conexão, ela precisa ser desta empresa — senão a resposta é **400**.

⚠️ A resposta traz também o **token** de cada Conexão que tiver um, e os dados de acesso dos canais. Trate o retorno como trata o próprio token: não exiba nem guarde em log.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/whatsapp-status',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token da Conexão ou Token da Empresa
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X POST 'https://api2.chatmasterveloz.com/api/whatsapp-status' -H 'Authorization: Bearer {seutokenaqui}'
```
