# API Atualizar Pedido

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-pedido
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Atualizar Pedido

---

🧩 Atualiza **um pedido em rascunho**: os itens, o desconto, o acréscimo e a entrega.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}
```

##### Método

```
PUT
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "itens": [
        {
            "productId": 101,
            "quantidade": 3
        }
    ],
    "descontoTipo": "valor",
    "descontoValor": 10.00,
    "acrescimo": 0,
    "entrega": "retirada",
    "agendadoPara": "2026-11-05T17:00:00-03:00",
    "observacao": "Cliente vai buscar no fim da tarde."
}
```

◽ O `pedidoId` vai no próprio endereço: é o ID do pedido, que vem na listagem dos pedidos e na resposta da criação.

⚠️ **Só o rascunho pode ser atualizado.** Pedido confirmado, entregue ou cancelado é recusado.

➡️ **“itens”:** os produtos do pedido como ele deve ficar — eles substituem os itens atuais. **Obrigatório.**

◽ Cada item leva o produto pelo `productId` **ou** pelo `sku` do cadastro, e a `quantidade`.

◽ Os preços são recalculados pelo cadastro de agora, inclusive dos itens que já estavam no pedido.

⚠️ **O corpo enviado vira o pedido inteiro.** O que ficar de fora volta ao padrão: sem desconto e sem acréscimo, retirada no local, sem taxa, sem endereço e sem bairro de entrega, sem agendamento e sem observação. Para mudar só a quantidade, mande de novo também o que quer manter.

➡️ **“descontoTipo”:** `valor` (em reais) ou `percentual`.

➡️ **“descontoValor”:** o desconto — o valor em reais ou o percentual, conforme o `descontoTipo`.

➡️ **“acrescimo”:** acréscimo em reais.

➡️ **“entrega”:** `retirada` ou `entrega`. Na `entrega`, o **“enderecoEntrega”** é obrigatório e a **“taxaEntrega”** entra no total.

➡️ **“bairroEntrega”:** bairro da entrega. Sem a `taxaEntrega`, vale a taxa desse bairro na tabela de taxas de entrega da empresa.

➡️ **“agendadoPara”:** data e horário combinados com o cliente, no formato ISO 8601 — por exemplo, `2026-11-05T17:00:00-03:00` (o `-03:00` é o fuso de Brasília).

◽ Data em outro formato é recusada.

➡️ **“observacao”:** observação do pedido.

◽ O cliente do pedido não muda por aqui.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "itens": [
        {
            "productId": 101,
            "quantidade": 3
        }
    ],
    "descontoTipo": "valor",
    "descontoValor": 10.00,
    "acrescimo": 0,
    "entrega": "retirada",
    "agendadoPara": "2026-11-05T17:00:00-03:00",
    "observacao": "Cliente vai buscar no fim da tarde."
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"itens":[{"productId":101,"quantidade":3}],"descontoTipo":"valor","descontoValor":10,"acrescimo":0,"entrega":"retirada","agendadoPara":"2026-11-05T17:00:00-03:00","observacao":"Cliente vai buscar no fim da tarde."}'
```
