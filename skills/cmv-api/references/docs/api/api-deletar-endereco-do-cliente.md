# API Deletar Endereço do Cliente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-endereco-do-cliente
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Deletar Endereço do Cliente

---

🧩 Apaga **um endereço de entrega** de um cliente do PDV.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/enderecos/{enderecoId}
```

##### Método

```
DELETE
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

◽ O `enderecoId` vai no próprio endereço: é o ID do endereço, que vem na lista de endereços do cliente e na resposta do cadastro.

➡️ **Apagado o endereço principal**, o usado por último num pedido passa a ser o principal.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/enderecos/{enderecoId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/pdv/enderecos/{enderecoId}' -H 'Authorization: Bearer {seutokenaqui}'
```
