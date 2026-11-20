# API Marcar Pedido como Saiu para Entrega

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-marcar-pedido-como-saiu-para-entrega
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Marcar Pedido como Saiu para Entrega

---

🧩 Marca **um pedido com entrega** como saiu para entrega, com ou sem entregador.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/saiu
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
    "entregadorId": 12
}
```

➡️ **“entregadorId”:** quem leva o pedido — o ID de um usuário da empresa com o perfil **Entregador**. O pedido aparece para ele em **Minhas entregas**.

◽ Usuário de outro perfil é recusado.

◽ Sem o `entregadorId`, a própria loja entrega.

◽ O `pedidoId` vai no próprio endereço: é o ID do pedido, que vem na listagem dos pedidos e na resposta da criação.

⚠️ **Só o pedido com entrega** sai: confirmado, em preparo ou pronto. Pedido de retirada no local, em rascunho ou já entregue é recusado.

➡️ **O pedido ganha o link para acompanhar a entrega**, e o cliente recebe na conversa o aviso de saída com esse link quando o aviso está ligado nos **Avisos do pedido ao cliente**, no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/saiu',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "entregadorId": 12
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/saiu' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"entregadorId":12}'
```
