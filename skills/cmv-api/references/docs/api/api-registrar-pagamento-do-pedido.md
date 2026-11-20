# API Registrar Pagamento do Pedido

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-registrar-pagamento-do-pedido
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Registrar Pagamento do Pedido

---

🧩 Registra **um pagamento** num pedido confirmado — inteiro ou em partes.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/pagamentos
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
    "forma": "dinheiro",
    "valor": 45.00,
    "valorRecebido": 50.00,
    "observacao": "Pago na retirada.",
    "userId": 4
}
```

◽ O `pedidoId` vai no próprio endereço: é o ID do pedido, que vem na listagem dos pedidos e na resposta da criação.

⚠️ **Só o pedido confirmado recebe pagamento** — em qualquer etapa, do confirmado ao entregue, passando pelo preparo e pela saída para entrega. Em rascunho ou cancelado, a chamada é recusada.

➡️ **“forma”:** `dinheiro`, `pix`, `cartao`, `boleto` ou `outro`. **Obrigatório.**

➡️ **“valor”:** valor em formato decimal, com os centavos depois do **ponto** — por exemplo, `45.00`.

◽ Vazio, vale o que falta pagar.

◽ Pode ser em partes: o pedido fica `parcial` até a soma fechar.

◽ Valor maior que o saldo, ou pedido já pago, é recusado.

➡️ **“valorRecebido”:** só no `dinheiro` — quanto o cliente entregou, para calcular o troco. Menor que o `valor` é recusado.

➡️ **“observacao”:** observação do pagamento, com até 500 caracteres.

➡️ **“userId”:** quem recebeu — um usuário da empresa.

◽ Com ele, o pagamento entra no **caixa aberto** desse usuário. Caixa fechado faz a chamada ser recusada.

◽ Sem ele, o pagamento fica no pedido sem passar por caixa — é o dinheiro que a sua integração recebeu por fora.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/pagamentos',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "forma": "dinheiro",
    "valor": 45.00,
    "valorRecebido": 50.00,
    "observacao": "Pago na retirada.",
    "userId": 4
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/pagamentos' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"forma":"dinheiro","valor":45,"valorRecebido":50,"observacao":"Pago na retirada.","userId":4}'
```
