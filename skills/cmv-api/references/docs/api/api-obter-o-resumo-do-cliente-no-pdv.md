# API Obter o Resumo do Cliente no PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-o-resumo-do-cliente-no-pdv
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Obter o Resumo do Cliente no PDV

---

🧩 Obter o **resumo de um cliente** no PDV: o cashback, os pedidos, os cupons usados e os produtos que ele mais pede.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/clientes/{contactId}
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
// sem payload — o cliente vai no endereço
```

➡️ **“contactId”:** ID do contato — vai no próprio endereço, no lugar de `{contactId}`. **Obrigatório.**

◽ É o mesmo resumo da tela **Clientes**, no menu **PDV  ›  Clientes**.

◽ Os valores em dinheiro vêm em **centavos**: `45900` são R$ 459,00.

◽ `contato` traz o `id`, o `nome` e o `numero` do cliente.

◽ `totais` traz quantos `pedidos`, o `gasto`, o `ticketMedio` e o `ultimoPedidoEm`. Os pedidos, o gasto e o tíquete médio deixam de fora os pedidos cancelados.

◽ `cashback` traz se a loja está com cashback (`ativo`), o `saldo`, o `expiraEm` (`null`: não expira) e o `extrato`, do mais novo ao mais antigo.

◽ `cupons` traz os cupons que o cliente usou, com o código, o desconto e o pedido.

◽ `pedidos` traz os 50 mais novos, com a data, a situação, o total, os produtos e as formas de pagamento.

◽ `maisPedidos` traz os 10 produtos que o cliente mais pede, sem contar os pedidos cancelados.

◽ Contato que não existe, ou de outra empresa, responde **não encontrado**.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/clientes/{contactId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/clientes/{contactId}' -H 'Authorization: Bearer {seutokenaqui}'
```
