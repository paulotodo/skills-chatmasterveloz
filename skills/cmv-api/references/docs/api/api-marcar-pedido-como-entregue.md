# API Marcar Pedido como Entregue

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-marcar-pedido-como-entregue
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Marcar Pedido como Entregue

---

🧩 Marca **um pedido confirmado** como entregue.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/entregue
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

```
// sem payload
```

➡️ Esta chamada não tem payload.

◽ O `pedidoId` vai no próprio endereço: é o ID do pedido, que vem na listagem dos pedidos e na resposta da criação.

⚠️ **Só o pedido confirmado** pode ser marcado como entregue — em qualquer etapa do painel de pedidos: confirmado, em preparo, pronto ou depois de sair para entrega. Em rascunho ou cancelado, a chamada é recusada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/entregue',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/entregue' -H 'Authorization: Bearer {seutokenaqui}'
```
