# API Listar Setores de Produção

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-setores-de-producao
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Listar Setores de Produção

---

🧩 Obter a **lista de setores de produção** do PDV da sua empresa — como Cozinha, Bar e Copa —, na ordem do filtro do Painel de pedidos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/setores
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

◽ São os mesmos setores do botão **Setores**, em Produtos, na ordem do filtro do **Painel de pedidos**.

◽ Cada setor traz o `id`, o `nome`, a `cor` (em `#RRGGBB`, ou `null` sem cor), o `ativo`, a `ordem` e, em `categorias`, quantas categorias usam o setor.

◽ Os desativados também vêm, com `ativo` em `false`.

◽ O `id` é o `setorId` que cada categoria de produto traz.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/setores',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/setores' -H 'Authorization: Bearer {seutokenaqui}'
```
