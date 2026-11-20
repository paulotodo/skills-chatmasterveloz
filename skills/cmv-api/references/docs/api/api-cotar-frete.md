# API Cotar Frete

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-cotar-frete
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Cotar Frete

---

🧩 Cotar o **frete de uma entrega** pelo CEP ou pelo bairro, com a mesma regra do pedido do PDV.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/frete?cep={cep}&bairro={bairro}
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
// sem payload — o CEP e o bairro vão na própria URL
```

➡️ Esta chamada não tem payload. O CEP e o bairro são informados como **query** na URL: um dos dois, ou os dois.

◽ **cep:** o CEP da entrega, com 8 números, com ou sem o traço.

◽ **bairro:** o bairro da entrega, sem diferença de maiúscula, acento ou espaço.

➡️ **O CEP vem antes do bairro:** o CEP que cai numa faixa de CEP usa o frete e o prazo dela. Fora das faixas, vale a taxa do bairro.

◽ Fora das duas, a resposta vem com `atende: false`. Dentro, com a `taxa` e, na faixa de CEP, também o `prazo`.

◽ Na empresa sem taxas por bairro e sem faixas de CEP, a entrega sai sem taxa: `atende: true` e `taxa: 0`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/frete?cep={cep}&bairro={bairro}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/frete?cep={cep}&bairro={bairro}' -H 'Authorization: Bearer {seutokenaqui}'
```
