# API Listar Endereços do Cliente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-enderecos-do-cliente
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Listar Endereços do Cliente

---

🧩 Obter a **lista de endereços de entrega** de um cliente do PDV.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/enderecos?number=5511955892164
```

##### Método

```
GET
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```
// sem payload — o cliente vai na própria URL
```

➡️ Esta chamada não tem payload. O cliente é informado como **query** na URL.

◽ **number:** telefone do cliente no formato ddi ddd numero (somente números), com ou sem o nono dígito.

◽ **contactId:** o ID do contato, no lugar do `number` — `?contactId={contactId}`.

◽ Um dos dois é **obrigatório**.

➡️ O endereço **principal** vem primeiro, e depois o usado por último num pedido.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/enderecos?number=5511955892164',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/enderecos?number=5511955892164' -H 'Authorization: Bearer {seutokenaqui}'
```
