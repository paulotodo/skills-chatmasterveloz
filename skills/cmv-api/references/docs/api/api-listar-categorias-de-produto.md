# API Listar Categorias de Produto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-categorias-de-produto
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Listar Categorias de Produto

---

🧩 Obter as **categorias de produto** do PDV da sua empresa, com as subcategorias.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/categorias
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

◽ As categorias vêm em árvore, na ordem do cardápio, cada uma com as suas `subcategorias` — as mesmas da janela **Categorias de produto**, em Produtos.

◽ Cada categoria traz o `caminho` (por exemplo, **Bebidas › Refrigerantes**) e, em `produtos`, quantos produtos estão direto nela.

◽ As desativadas também vêm, com `ativa` em `false`.

◽ O `setorId` é o setor de produção que prepara os produtos da categoria. Vem `null` na categoria sem setor — na subcategoria, vale então o da categoria de cima.

◽ A `imagem` é o endereço da imagem da categoria, a que aparece no Cardápio e na Loja. Vem `null` na categoria sem imagem.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/categorias',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/categorias' -H 'Authorization: Bearer {seutokenaqui}'
```
