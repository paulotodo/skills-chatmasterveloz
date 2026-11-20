# API Listar Avaliações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-avaliacoes
- **Categoria:** APIs
- **Menu:** APIs › Extras › API Listar Avaliações

---

🧩 Listar as **respostas das pesquisas de satisfação**, com as estatísticas do período.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ratings?dateStart={dateStart}&dateEnd={dateEnd}&pageNumber={pageNumber}&pageSize={pageSize}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, por exemplo `?dateStart=2026-09-01&userId=31`.

◽ **“dateStart”** e **“dateEnd”:** período, no formato `AAAA-MM-DD` ou `DD/MM/AAAA`, incluindo o dia inteiro. Data que não existe, como `31/02/2026`, é recusada.

◽ **“searchParam”:** busca por nome ou número do contato, ou por nome do operador.

◽ **“ratingId”:** só as respostas de um modelo de pesquisa.

◽ **“userId”:** só as respostas dos atendimentos de um operador.

◽ **“queueId”:** só as respostas dos atendimentos de um Setor.

◽ **“pageNumber”** e **“pageSize”:** página e quantos itens por página. Padrão `1` e `20`; o teto é `200`.

◽ Cada resposta vem com a nota, a opção marcada, o atendimento com o contato e o Setor, o operador e o modelo de pesquisa.

◽ A lista vem das mais recentes para as mais antigas, e acompanha as estatísticas do recorte: total, média das notas e quantas respostas por opção.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ratings?dateStart={dateStart}&dateEnd={dateEnd}&pageNumber={pageNumber}&pageSize={pageSize}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/ratings?dateStart={dateStart}&dateEnd={dateEnd}&pageNumber={pageNumber}&pageSize={pageSize}' -H 'Authorization: Bearer {seutokenaqui}'
```
