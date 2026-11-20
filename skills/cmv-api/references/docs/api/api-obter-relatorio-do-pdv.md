# API Obter Relatório do PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-relatorio-do-pdv
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Obter Relatório do PDV

---

🧩 Obter o **relatório de vendas** do PDV da sua empresa no período, com os totais, as quebras por produto, categoria, atendente, forma de pagamento e dia, e a comissão dos garçons.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/relatorio?de={dataInicio}&ate={dataFim}&userId={userId}
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

◽ **de** e **ate:** o primeiro e o último dia do período, no formato `AAAA-MM-DD` ou `DD/MM/AAAA`. Sem os dois, vêm os últimos 30 dias, até hoje; só com `de`, vai até hoje; só com `ate`, começa 29 dias antes.

◽ O período vai até **um ano**. Mais longo, ou com `de` depois de `ate`, a chamada é recusada.

⚠️ Em `DD/MM/AAAA`, o dia vem primeiro: `01/10/2026` é 1º de outubro. Data que não existe, como `31/02/2026`, é recusada.

◽ **userId:** só os pedidos daquele atendente (o id do usuário). Um id sem pedidos devolve o relatório zerado.

➡️ **O relatório é da empresa inteira**, qualquer que seja a Conexão do token.

◽ O `resumo` traz os totais do período — vendido, recebido, estornado, a receber, cancelados, custo e margem —, e as quebras vêm em `porProduto`, `porCategoria`, `porAtendente`, `porForma` e `porDia`.

◽ O `resumo` traz também a `taxaServico` e os `descontosDaConta`: a taxa de serviço e o desconto dados na conta da mesa, que já estão dentro do vendido.

◽ Os valores vêm em reais, com o ponto separando os centavos; a `margem` vem em %.

◽ O `porDia` traz todos os dias do período, também os sem venda.

➡️ **A `comissao` dos garçons** vem junto, calculada pela regra de **Comissão do garçom**, no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**.

◽ Em `regra`, o `repasseDaTaxa` é quanto da taxa de serviço vai para o garçom que lançou a rodada, em %, e o `sobreOConsumo` é o percentual sobre o consumo da rodada.

◽ Em `porGarcom`, cada garçom traz o `userId`, o `nome`, as `rodadas` que lançou e as `mesas` em que lançou, o `consumo` e a `taxaServico` dessas rodadas e a `comissao`, em reais. O `total` soma os mesmos números de todas as linhas.

◽ O pedido feito pelo cliente no QR Code da mesa não tem garçom: entra em `porGarcom` numa linha com `"semGarcom": true`, o `userId` e o `nome` nulos e a `comissao` zero.

◽ A `comissao` de cada garçom é somada rodada a rodada e arredondada uma vez, no total dele.

◽ Cada rodada usa a regra que valia quando foi confirmada. A `regra` é a de agora, e `vigencias` lista todas as que já valeram, cada uma com o `repasseDaTaxa`, o `sobreOConsumo` e o `desde`: a data e a hora em que passou a valer, em UTC. A primeira vem com o `desde` nulo: é a regra de antes da primeira mudança.

◽ Com o filtro `userId`, a `comissao` também fica só a daquele usuário.

◽ Contam as rodadas lançadas nas mesas e confirmadas no período; as canceladas ficam de fora.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/relatorio?de={dataInicio}&ate={dataFim}&userId={userId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/relatorio?de={dataInicio}&ate={dataFim}&userId={userId}' -H 'Authorization: Bearer {seutokenaqui}'
```
