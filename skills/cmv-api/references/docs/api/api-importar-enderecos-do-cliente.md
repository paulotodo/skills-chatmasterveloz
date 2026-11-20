# API Importar Endereços do Cliente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-importar-enderecos-do-cliente
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Importar Endereços do Cliente

---

🧩 Importa **endereços de entrega em lote**, de um ou de vários clientes do PDV.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/enderecos/importar
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
    "enderecos": [
        {
            "number": "5511955892164",
            "name": "Carla Souza",
            "apelido": "Casa",
            "endereco": "Rua das Flores, 120, apto 31",
            "bairro": "Centro",
            "cep": "01310-100",
            "principal": true
        },
        {
            "number": "5511955892164",
            "apelido": "Trabalho",
            "endereco": "Avenida Paulista, 1000, sala 12",
            "bairro": "Bela Vista"
        }
    ]
}
```

➡️ **“enderecos”:** a lista de endereços, até 2.000 por chamada. **Obrigatório.**

◽ **number:** telefone do cliente no formato ddi ddd numero (somente números). **Obrigatório.** O cliente que ainda não existe é cadastrado.

◽ **name:** nome do cliente, usado só quando ele ainda não existe.

◽ **apelido:** como o endereço aparece na lista do cliente, com até 40 caracteres.

◽ **endereco:** a rua, o número e o complemento, com até 500 caracteres. **Obrigatório.**

◽ **bairro:** o bairro, com até 120 caracteres.

◽ **cep:** o CEP, com 8 números, com ou sem o traço.

◽ **principal:** `true` faz deste o endereço principal do cliente.

➡️ **Um endereço recusado não barra os outros.** A resposta traz quantos foram `importados`, os `repetidos` (que o cliente já tinha) e os `clientesNovos`. Cada recusado volta em `erros`, com a posição dele na lista (o primeiro é `1`) e o código do erro.

◽ Valem as mesmas regras de um endereço cadastrado sozinho: a área de entrega, até **10 endereços** por cliente e nenhum repetido.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/enderecos/importar',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "enderecos": [
        {
            "number": "5511955892164",
            "name": "Carla Souza",
            "apelido": "Casa",
            "endereco": "Rua das Flores, 120, apto 31",
            "bairro": "Centro",
            "cep": "01310-100",
            "principal": true
        },
        {
            "number": "5511955892164",
            "apelido": "Trabalho",
            "endereco": "Avenida Paulista, 1000, sala 12",
            "bairro": "Bela Vista"
        }
    ]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/enderecos/importar' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"enderecos":[{"number":"5511955892164","name":"Carla Souza","apelido":"Casa","endereco":"Rua das Flores, 120, apto 31","bairro":"Centro","cep":"01310-100","principal":true},{"number":"5511955892164","apelido":"Trabalho","endereco":"Avenida Paulista, 1000, sala 12","bairro":"Bela Vista"}]}'
```
