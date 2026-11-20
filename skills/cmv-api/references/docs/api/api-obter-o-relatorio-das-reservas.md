# API Obter o Relatório das Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-o-relatorio-das-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Obter o Relatório das Reservas

---

🧩 Obter **o relatório das Reservas** de um período, com os mesmos números da aba Relatório.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/relatorio?de={dataInicio}&ate={dataFim}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL.

◽ **de** e **ate:** o período, no formato `AAAA-MM-DD`, de 1 a 366 dias, com a data final depois da inicial. Sem as datas, os 30 dias até hoje.

◽ A reserva entra no período pelo dia em que começa, no fuso da empresa.

◽ Também filtram: **ofertaId** (só as reservas desta oferta) e **recursoId** (só as deste recurso).

➡️ **A resposta traz o relatório do período.**

◽ `totais`: as reservas, as `ativas` (sem as canceladas), cada situação, as pessoas, o `comparecimento` e o `cancelamento`, de 0 a 1.

◽ `valores`: o `previsto`, o `recebido`, o `aReceber`, o `estornado` e o `ticketMedio`.

◽ `porOferta` e `porRecurso`, com a `ocupacao` de cada recurso; `porDiaDaSemana`, `porHora` e `diario`.

◽ `porOrigem`: de onde as reservas vieram — `painel`, `pagina`, `fluxo`, `api` e `sistema`.

◽ `pacotes` (os vendidos, a receita e os créditos usados), `series` e `clientes` (os únicos, os que voltaram e os que mais reservaram).

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/relatorio?de={dataInicio}&ate={dataFim}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/relatorio?de={dataInicio}&ate={dataFim}' -H 'Authorization: Bearer {seutokenaqui}'
```
