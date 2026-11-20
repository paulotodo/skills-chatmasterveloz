# API Listar Descontos e Taxas das Formas de Pagamento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-descontos-e-taxas-das-formas-de-pagamento
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Listar Descontos e Taxas das Formas de Pagamento

---

🧩 Obter o **desconto e a taxa de cada forma de pagamento** do PDV da sua empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/formas-de-pagamento
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

◽ São as regras do bloco *Desconto e taxa por forma de pagamento*, no menu **Configurações  ›  Opções**, seção PDV.

◽ Em `formas` vem uma chave por forma: `dinheiro`, `pix`, `cartao`, `boleto` e `outro`. A forma sem regra não vem.

◽ Cada forma traz o `desconto` e a `taxa`. Cada um tem o `tipo` — `valor`, em reais, ou `percentual`, em % — e o `valor`. Sem desconto, ou sem taxa, vem `null`.

◽ Exemplo: `"pix": { "desconto": { "tipo": "percentual", "valor": 5 }, "taxa": null }` é 5% de desconto no Pix, sem taxa.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/formas-de-pagamento',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/formas-de-pagamento' -H 'Authorization: Bearer {seutokenaqui}'
```
