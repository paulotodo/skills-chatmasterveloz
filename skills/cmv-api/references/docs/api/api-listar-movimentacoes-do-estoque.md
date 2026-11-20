# API Listar Movimentações do Estoque

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-movimentacoes-do-estoque
- **Categoria:** APIs
- **Menu:** APIs › Produtos › API Listar Movimentações do Estoque

---

🧩 Obter **o histórico do estoque** de um produto, do movimento mais novo ao mais antigo.

⚠️ Esta chamada é exclusiva do **PDV**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/products/{produtoId}/estoque?tipo={tipoDoMovimento}&de={dataInicio}&ate={dataFim}&pageNumber={pageNumber}
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
// sem payload — os filtros vão na própria URL
```

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, e todos são opcionais.

◽ O `produtoId` vai no próprio endereço: é o `id` do produto.

◽ **tipo:** `entrada`, `saida`, `ajuste`, `venda` ou `cancelamento`.

◽ **de** e **ate:** a partir de e até esse dia, no formato `AAAA-MM-DD` ou `DD/MM/AAAA`.

◽ **variacaoId:** só os movimentos desta variação.

◽ **pageNumber:** a página, de **20 em 20**. Padrão `1`. O `hasMore` da resposta diz se há outra página, e o `count`, quantos movimentos há.

➡️ **A resposta traz o `produto`**, com o saldo em `estoque`, o `estoqueMinimo` e o `estoqueBaixo`, as `variacoes`, com o saldo de cada uma, e os `movimentos`.

◽ Cada movimento traz `tipo`, `quantidade` (negativa na saída e na venda), `saldoAnterior`, `saldoPosterior`, `motivo`, `pedidoId` (o pedido da venda), `variacaoId`, quem lançou em `usuario` e `createdAt`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/products/{produtoId}/estoque?tipo={tipoDoMovimento}&de={dataInicio}&ate={dataFim}&pageNumber={pageNumber}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/products/{produtoId}/estoque?tipo={tipoDoMovimento}&de={dataInicio}&ate={dataFim}&pageNumber={pageNumber}' -H 'Authorization: Bearer {seutokenaqui}'
```
