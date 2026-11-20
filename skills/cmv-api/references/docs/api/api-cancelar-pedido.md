# API Cancelar Pedido

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-cancelar-pedido
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Cancelar Pedido

---

🧩 Cancela **um pedido**, devolvendo o estoque e estornando os pagamentos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/cancelar
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
    "motivo": "Cliente desistiu da compra."
}
```

◽ O `pedidoId` vai no próprio endereço: é o ID do pedido, que vem na listagem dos pedidos e na resposta da criação.

➡️ **“motivo”:** o motivo do cancelamento, com até 500 caracteres.

➡️ **O cancelamento desfaz o que o pedido já fez**, como quando é cancelado pela tela:

◽ devolve ao estoque o que a confirmação baixou;

◽ estorna os pagamentos confirmados;

◽ desativa os links de pagamento do Asaas que ainda estiverem abertos.

◽ Pedido já cancelado é recusado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/cancelar',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "motivo": "Cliente desistiu da compra."
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/cancelar' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"motivo":"Cliente desistiu da compra."}'
```
