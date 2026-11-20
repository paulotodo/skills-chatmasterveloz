# API Listar Taxas de Entrega

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-taxas-de-entrega
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Listar Taxas de Entrega

---

🧩 Obter a **tabela de taxas de entrega** por bairro e as **faixas de CEP** do frete do PDV da sua empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/taxas-de-entrega
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
// sem payload
```

➡️ Esta chamada não tem payload.

◽ A tabela vem em ordem de bairro, com o `bairro` e a `taxa` de cada um — a mesma cadastrada em **Taxa de entrega por bairro**, no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**.

◽ É essa taxa que entra no pedido com entrega que informa o bairro e não informa a taxa.

◽ Em `faixas` vêm as faixas de CEP do frete, em ordem de CEP — as mesmas de **Frete por faixa de CEP**, no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**. Cada faixa traz o `nome` (a região, ou `null` quando não foi preenchida), o `cepInicial`, o `cepFinal`, a `taxa` (o frete da faixa) e o `prazo` (ou `null`).

◽ No pedido de entrega, o CEP que cai numa faixa usa o frete e o prazo dela; fora das faixas, vale a taxa do bairro. Sem nenhuma faixa cadastrada, `faixas` vem vazia.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/taxas-de-entrega',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/taxas-de-entrega' -H 'Authorization: Bearer {seutokenaqui}'
```
