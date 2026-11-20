# API Listar Pedidos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-pedidos
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Listar Pedidos

---

🧩 Obter a **lista de pedidos** do PDV da sua empresa, do mais novo ao mais antigo.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos?situacao={situacaoDoPedido}&pagamento={pagamentoDoPedido}&de={dataInicio}&ate={dataFim}&busca={busca}&ticketId={ticketId}&pageNumber={pageNumber}
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

◽ **situacao:** `rascunho`, `confirmado`, `preparando`, `pronto`, `saiu`, `entregue` ou `cancelado`.

◽ `preparando`, `pronto` e `saiu` são as etapas do painel de pedidos: em preparo, pronto e saiu para entrega.

◽ **pagamento:** `pendente`, `parcial` ou `pago`.

◽ **de** e **ate:** pedidos criados a partir de e até esse dia, no formato `AAAA-MM-DD` ou `DD/MM/AAAA`.

⚠️ Em `DD/MM/AAAA`, o dia vem primeiro: `01/10/2026` é 1º de outubro. Data que não existe, como `31/02/2026`, ou em outro formato é recusada.

◽ **busca:** o número do pedido, ou o nome ou o telefone do cliente.

◽ **ticketId:** só os pedidos daquele atendimento.

◽ **pageNumber:** a página, de **20 em 20**. Padrão `1`.

➡️ **A chamada vê todos os pedidos da empresa**, de qualquer vendedor.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos?situacao={situacaoDoPedido}&pagamento={pagamentoDoPedido}&de={dataInicio}&ate={dataFim}&busca={busca}&ticketId={ticketId}&pageNumber={pageNumber}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/pedidos?situacao={situacaoDoPedido}&pagamento={pagamentoDoPedido}&de={dataInicio}&ate={dataFim}&busca={busca}&ticketId={ticketId}&pageNumber={pageNumber}' -H 'Authorization: Bearer {seutokenaqui}'
```
