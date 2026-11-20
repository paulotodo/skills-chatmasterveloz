# API Listar Lançamentos do PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-lancamentos-do-pdv
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Listar Lançamentos do PDV

---

🧩 Obter a **lista de lançamentos financeiros** do PDV da sua empresa, um por linha, para o ERP conciliar: recebimentos, estornos, valores a receber, sangrias e suprimentos do caixa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/relatorio/lancamentos?de={dataInicio}&ate={dataFim}&tipo={tipoDoLancamento}&pageNumber={pageNumber}
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

◽ **tipo:** `recebimento`, `estorno`, `a_receber`, `sangria` ou `reforco`; para mais de um, separe por vírgula, como `sangria,reforco`. Sem ele, ou com `todos`, vêm todos.

◽ **pageNumber:** a página, de **100 em 100**. Padrão `1`. O `temMais` da resposta diz se há outra página.

➡️ **Cada lançamento traz o `valor`, sempre positivo, e o `sentido`:** `entra`, `sai` ou `previsto`.

◽ **recebimento** (entra): o pagamento de um pedido, na data em que foi confirmado. Se depois foi estornado, continua na lista, com `estornado: true`.

◽ **estorno** (sai): o pagamento devolvido, na data do estorno. O `pagamentoId` diz qual recebimento foi estornado.

◽ **a_receber** (previsto): o que falta receber de um pedido confirmado no período — o total menos o já pago. Muda conforme o cliente paga: consulte de novo.

◽ **sangria** (sai) e **reforco** (entra): dinheiro retirado do caixa ou posto nele. O `reforco` é o **Suprimento** da tela do Caixa.

◽ A lista vem da mais antiga para a mais nova, e os `totais` somam cada tipo no período inteiro, de todas as páginas.

➡️ **Grave o `id` de cada linha** — `pagamento-12`, `estorno-12`, `pedido-40`, `caixa-7`. Ele não muda entre consultas, e é o que impede a mesma linha de entrar duas vezes no ERP.

➡️ **A lista é da empresa inteira**, qualquer que seja a Conexão do token.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/relatorio/lancamentos?de={dataInicio}&ate={dataFim}&tipo={tipoDoLancamento}&pageNumber={pageNumber}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/relatorio/lancamentos?de={dataInicio}&ate={dataFim}&tipo={tipoDoLancamento}&pageNumber={pageNumber}' -H 'Authorization: Bearer {seutokenaqui}'
```
