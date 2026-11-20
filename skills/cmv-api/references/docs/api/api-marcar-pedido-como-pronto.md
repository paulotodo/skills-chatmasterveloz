# API Marcar Pedido como Pronto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-marcar-pedido-como-pronto
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Marcar Pedido como Pronto

---

🧩 Marca **um pedido** como pronto, para o cliente retirar ou para sair para entrega.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/pronto
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

⚠️ **Só o pedido confirmado ou em preparo** fica pronto — dá para pular o preparo. Em rascunho, ou depois de sair para entrega, a chamada é recusada.

➡️ **Pedido de retirada:** o cliente recebe na conversa o aviso de que o pedido está pronto para retirar, quando esse aviso está ligado nos **Avisos do pedido ao cliente**, em Configurações → Opções.

◽ Pedido com entrega fica esperando sair, sem aviso ao cliente.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/pronto',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/pronto' -H 'Authorization: Bearer {seutokenaqui}'
```
