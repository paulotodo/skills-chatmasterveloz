# API Criar Pedido

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-pedido
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Criar Pedido

---

🧩 Cria **um pedido** no PDV pelo número do cliente, com os itens, o desconto e a entrega.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos
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
    "number": "5511955892164",
    "name": "Carla Souza",
    "userId": 4,
    "itens": [
        {
            "productId": 101,
            "quantidade": 2
        },
        {
            "sku": "CAF-500",
            "quantidade": 1
        }
    ],
    "descontoTipo": "percentual",
    "descontoValor": 10,
    "acrescimo": 0,
    "entrega": "entrega",
    "taxaEntrega": 5.00,
    "enderecoEntrega": "Rua das Flores, 100",
    "bairroEntrega": "Centro",
    "cepEntrega": "80010-000",
    "agendadoPara": "2026-11-05T15:00:00-03:00",
    "observacao": "Entregar depois das 14h.",
    "confirmar": false
}
```

➡️ **“number”:** telefone do cliente no formato ddi ddd numero (somente números).

◽ O contato é achado — ou criado — e o atendimento é achado — ou aberto — na Conexão da chamada, como acontece quando chega uma mensagem.

◽ Em vez do `number`, dá para mandar o **`ticketId`** de um atendimento da empresa: o pedido nasce nesse atendimento. Um dos dois é **obrigatório**.

➡️ **“name”:** nome do cliente, usado só quando o contato é novo. O contato que já existe fica como está.

➡️ **“userId”:** o vendedor do pedido — um usuário da empresa.

➡️ **“itens”:** os produtos do pedido. **Obrigatório.**

◽ Cada item leva o produto pelo `productId` **ou** pelo `sku` do cadastro, e a `quantidade`.

◽ O preço é sempre o do cadastro do produto — não existe campo de preço.

◽ O mesmo produto duas vezes vira um item só, com as quantidades somadas.

➡️ **“descontoTipo”:** `valor` (em reais) ou `percentual`.

➡️ **“descontoValor”:** o desconto — o valor em reais ou o percentual, conforme o `descontoTipo`.

➡️ **“acrescimo”:** acréscimo em reais.

➡️ **“entrega”:** `retirada`, quando o cliente busca no local, ou `entrega`.

➡️ **“taxaEntrega”:** taxa de entrega em reais, só quando a `entrega` é `entrega`.

➡️ **“enderecoEntrega”:** endereço de entrega. **Obrigatório** quando a `entrega` é `entrega`.

◽ Valores em reais vão em formato decimal, com os centavos depois do **ponto** — por exemplo, `5.00`.

➡️ **“bairroEntrega”:** bairro da entrega, com até 120 caracteres.

◽ Sem a `taxaEntrega`, vale a taxa desse bairro na tabela de taxas de entrega da empresa — sem diferença de maiúscula, acento ou espaço. Bairro que não está na tabela fica sem taxa.

◽ Com a `taxaEntrega`, vale a taxa informada.

➡️ **“cepEntrega”:** CEP da entrega — por exemplo, `80010-000`.

◽ É o CEP que as faixas de CEP do frete da empresa usam, as mesmas de **Frete por faixa de CEP**, no menu **Configurações  ›  Opções**.

➡️ **“agendadoPara”:** data e horário combinados com o cliente, no formato ISO 8601 — por exemplo, `2026-11-05T15:00:00-03:00` (o `-03:00` é o fuso de Brasília).

◽ Data em outro formato é recusada, e o pedido não é gravado.

➡️ **“observacao”:** observação do pedido.

➡️ **“confirmar”:** `true` já confirma o pedido e baixa o estoque. Sem ele, o pedido nasce em rascunho.

◽ Se a confirmação for recusada — por falta de estoque, por exemplo —, o pedido fica em rascunho e a resposta traz o motivo em `erroDaConfirmacao`.

➡️ **O payload é conferido antes de criar contato ou atendimento**: pedido recusado não deixa contato nem atendimento novo para trás.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "name": "Carla Souza",
    "userId": 4,
    "itens": [
        {
            "productId": 101,
            "quantidade": 2
        },
        {
            "sku": "CAF-500",
            "quantidade": 1
        }
    ],
    "descontoTipo": "percentual",
    "descontoValor": 10,
    "acrescimo": 0,
    "entrega": "entrega",
    "taxaEntrega": 5.00,
    "enderecoEntrega": "Rua das Flores, 100",
    "bairroEntrega": "Centro",
    "cepEntrega": "80010-000",
    "agendadoPara": "2026-11-05T15:00:00-03:00",
    "observacao": "Entregar depois das 14h.",
    "confirmar": false
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/pedidos' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","name":"Carla Souza","userId":4,"itens":[{"productId":101,"quantidade":2},{"sku":"CAF-500","quantidade":1}],"descontoTipo":"percentual","descontoValor":10,"acrescimo":0,"entrega":"entrega","taxaEntrega":5,"enderecoEntrega":"Rua das Flores, 100","bairroEntrega":"Centro","cepEntrega":"80010-000","agendadoPara":"2026-11-05T15:00:00-03:00","observacao":"Entregar depois das 14h.","confirmar":false}'
```
