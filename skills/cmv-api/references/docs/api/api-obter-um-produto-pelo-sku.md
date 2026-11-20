# API Obter um Produto pelo SKU

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-um-produto-pelo-sku
- **Categoria:** APIs
- **Menu:** APIs › Produtos › API Obter um Produto pelo SKU

---

🧩 Obter **um produto pelo SKU**, o código do produto.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/products/sku/{sku}
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
// sem payload
```

➡️ Esta chamada não tem payload.

◽ O `sku` vai no próprio endereço, sem diferenciar maiúscula: `cam-001` acha o produto `CAM-001`.

◽ SKU que não existe é recusado.

◽ O produto vem no mesmo formato da lista: `id`, `name`, `sku`, `marca`, `description`, `details`, `price`, `imageUrl`, a cobrança padrão em `recorrencia` e o `ativo`.

◽ **Só no PDV:** `custo`, `precoDelivery`, `categoriaId`, `tipo` (`produto` ou `servico`), as `variacoes`, os `adicionais`, a ficha de `insumos`, a galeria em `imagens`, o peso e as medidas, e o estoque — `controlaEstoque` e `estoqueResumo`, com o saldo, o mínimo e se está baixo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/products/sku/{sku}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/products/sku/{sku}' -H 'Authorization: Bearer {seutokenaqui}'
```
