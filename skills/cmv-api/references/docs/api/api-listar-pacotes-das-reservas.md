# API Listar Pacotes das Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-pacotes-das-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Listar Pacotes das Reservas

---

🧩 Obter a **lista de pacotes** das Reservas — o que a empresa vende de uma vez, como 10 aulas ou 4 sessões —, na ordem do cadastro.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/pacotes
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

➡️ Esta chamada não tem payload.

◽ Para só os pacotes que estão à venda, os ativos, acrescente `?ativos=true` ao endereço.

➡️ **A resposta traz os pacotes**, cada um com `id`, `nome`, `descricao`, `quantidade` (quantas reservas o pacote dá), `validadeDias`, `preco`, `ofertaIds`, `ativo` e `ordem`.

◽ `validadeDias`: em quantos dias, a contar da venda, o pacote vence. Com `0`, não vence.

◽ `ofertaIds`: as ofertas que o pacote cobre. Vazio, cobre todas, menos as diárias.

◽ O `id` do pacote é o `pacoteId` da chamada de vender o pacote.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/pacotes',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/pacotes' -H 'Authorization: Bearer {seutokenaqui}'
```
