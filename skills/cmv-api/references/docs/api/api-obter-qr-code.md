# API Obter QR Code

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-qr-code
- **Categoria:** APIs
- **Menu:** APIs › Conexões › API Obter QR Code

---

🧩 Obter o **código do QR Code**, para fazer a leitura da conexão solicitada.

**API:** Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/whatsappqrcodepro
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

◽ A conexão é a do token usado na chamada.

◽ A resposta traz o QR Code como **imagem em base64**, pronta para exibir na sua tela.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/whatsappqrcodepro',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/whatsappqrcodepro' -H 'Authorization: Bearer {seutokenaqui}'
```
