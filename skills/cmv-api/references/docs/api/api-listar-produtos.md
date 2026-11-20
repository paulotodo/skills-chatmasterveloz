# API Listar Produtos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-produtos
- **Categoria:** APIs
- **Menu:** APIs › Produtos › API Listar Produtos

---

🧩 Obter a **lista de produtos** da sua empresa, em ordem de nome, com filtros e páginas.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/products?searchParam={searchParam}&pageNumber={pageNumber}&limit={limit}
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
// sem payload — os filtros vão na própria URL
```

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, e todos são opcionais.

◽ **searchParam:** busca no nome, no SKU, na descrição, nos detalhes e na marca, sem diferenciar maiúscula.

◽ **pageNumber:** a página. Padrão `1`.

◽ **limit:** quantos por página. Padrão `20`, até `200` — acima disso, vale `200`.

◽ **marca:** só os desta marca, sem diferenciar acento e maiúscula. `sem` traz os produtos sem marca.

◽ **Só no PDV:** **categoriaId** (a categoria, com as subcategorias dela; `sem` traz os sem categoria), **tipo** (`produto` ou `servico`), **ativo** (`true` só os ativos, `false` só os inativos), **estoque** (`baixo`: os que estão no estoque mínimo ou abaixo dele) e **vitrine** (`cardapio` ou `loja`).

◽ Os filtros se somam.

➡️ **A resposta traz `produtos`, `total`, `pagina`, `porPagina` e `temMais`.**

◽ Cada produto traz `id`, `name`, `sku`, `marca`, `description`, `details`, `price`, `imageUrl`, a cobrança padrão em `recorrencia` e o `ativo`.

◽ O `price` vem como texto decimal, com ponto: `"35.90"`.

◽ **Só no PDV:** `custo`, `precoDelivery`, `categoriaId`, `tipo` (`produto` ou `servico`), as `variacoes`, os `adicionais`, a ficha de `insumos`, a galeria em `imagens`, o peso e as medidas, e o estoque — `controlaEstoque` e `estoqueResumo`, com o saldo, o mínimo e se está baixo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/products?searchParam={searchParam}&pageNumber={pageNumber}&limit={limit}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/products?searchParam={searchParam}&pageNumber={pageNumber}&limit={limit}' -H 'Authorization: Bearer {seutokenaqui}'
```
