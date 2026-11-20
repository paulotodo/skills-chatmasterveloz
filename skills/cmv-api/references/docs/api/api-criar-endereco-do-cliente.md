# API Criar Endereço do Cliente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-endereco-do-cliente
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Criar Endereço do Cliente

---

🧩 Cria **um endereço de entrega** para um cliente do PDV.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/enderecos
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
    "name": "Carla Souza",
    "apelido": "Casa",
    "endereco": "Rua das Flores, 120, apto 31",
    "bairro": "Centro",
    "cep": "01310-100",
    "principal": true
}
```

➡️ **“number”:** telefone do cliente no formato ddi ddd numero (somente números).

◽ Em vez do `number`, dá para mandar o **`contactId`** do cliente. Um dos dois é **obrigatório**.

◽ O cliente que ainda não existe é cadastrado.

➡️ **“name”:** nome do cliente, usado só quando ele ainda não existe. O cliente que já existe fica como está.

➡️ **“apelido”:** como o endereço aparece na lista do cliente — por exemplo, `Casa` ou `Trabalho` —, com até 40 caracteres.

➡️ **“endereco”:** a rua, o número e o complemento, com até 500 caracteres. **Obrigatório.**

➡️ **“bairro”:** o bairro, com até 120 caracteres.

➡️ **“cep”:** o CEP, com 8 números, com ou sem o traço. Ele fica gravado com o traço.

➡️ **“principal”:** `true` faz deste o endereço principal, e o anterior perde a marca. O principal é o que já vem escolhido no pedido com entrega.

◽ O primeiro endereço do cliente já nasce principal.

➡️ **O endereço precisa estar na área de entrega** quando a empresa tem taxas por bairro ou faixas de CEP cadastradas. Fora dela, a chamada é recusada.

◽ Cada cliente guarda até **10 endereços**, e o mesmo endereço não entra duas vezes.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/enderecos',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "name": "Carla Souza",
    "apelido": "Casa",
    "endereco": "Rua das Flores, 120, apto 31",
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/enderecos' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","name":"Carla Souza","apelido":"Casa","endereco":"Rua das Flores, 120, apto 31","bairro":"Centro","cep":"01310-100","principal":true}'
```
