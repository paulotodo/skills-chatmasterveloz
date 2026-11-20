# API Marcar Pedido em Preparo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-marcar-pedido-em-preparo
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Marcar Pedido em Preparo

---

🧩 Marca **um pedido confirmado** como em preparo, a etapa da cozinha no painel de pedidos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/preparar
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

⚠️ **Só o pedido confirmado** vai para o preparo. Em rascunho, ou que já está em preparo, a chamada é recusada.

➡️ **O cliente recebe na conversa o aviso de que o pedido está sendo preparado** quando esse aviso está ligado nos **Avisos do pedido ao cliente**, no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/preparar',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/preparar' -H 'Authorization: Bearer {seutokenaqui}'
```
