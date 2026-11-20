# API Atualizar Endereço do Cliente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-endereco-do-cliente
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Atualizar Endereço do Cliente

---

🧩 Atualiza **um endereço de entrega** de um cliente do PDV.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/enderecos/{enderecoId}
```

##### Método

```
PUT
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "apelido": "Casa",
    "endereco": "Rua das Flores, 120, apto 32",
    "bairro": "Centro",
    "cep": "01310-100",
    "principal": true
}
```

➡️ **“apelido”:** como o endereço aparece na lista do cliente, com até 40 caracteres.

➡️ **“endereco”:** a rua, o número e o complemento, com até 500 caracteres. **Obrigatório.**

➡️ **“bairro”:** o bairro, com até 120 caracteres.

➡️ **“cep”:** o CEP, com 8 números, com ou sem o traço. Sem ele, o CEP gravado continua o mesmo.

➡️ **“principal”:** `true` faz deste o endereço principal, e o anterior perde a marca.

➡️ **O `enderecoId` vai no próprio endereço da chamada:** é o ID do endereço, que vem na lista de endereços do cliente e na resposta do cadastro.

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
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "apelido": "Casa",
    "endereco": "Rua das Flores, 120, apto 32",
    "bairro": "Centro",
    "cep": "01310-100",
    "principal": true
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/pdv/enderecos/{enderecoId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"apelido":"Casa","endereco":"Rua das Flores, 120, apto 32","bairro":"Centro","cep":"01310-100","principal":true}'
```
