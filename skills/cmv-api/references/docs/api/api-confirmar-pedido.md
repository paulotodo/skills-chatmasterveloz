# API Confirmar Pedido

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-confirmar-pedido
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Confirmar Pedido

---

🧩 Confirma **um pedido em rascunho** e baixa o estoque dos itens.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/confirmar
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

➡️ **O estoque é baixado** nos itens cujo produto controla estoque.

⚠️ **Sem estoque suficiente, a confirmação é recusada e nada muda** — a menos que a empresa venda sem estoque.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/confirmar',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/pedidos/{pedidoId}/confirmar' -H 'Authorization: Bearer {seutokenaqui}'
```
