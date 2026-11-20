# API Listar Reservas de Mesa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-reservas-de-mesa
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Listar Reservas de Mesa

---

🧩 Obter a **lista de reservas de mesa** da sua empresa, de um dia ou de um período, em ordem de horário.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/reservas?de={dataInicio}&ate={dataFim}&situacao={situacaoDaReserva}&mesaId={mesaId}
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

◽ **de** e **ate:** o primeiro e o último dia do período, no formato `AAAA-MM-DD`. Data em outro formato é recusada. Sem nenhum filtro de data, vêm as reservas de hoje até 60 dias à frente.

◽ **dia:** para um dia só, use `?dia=2026-11-20` no lugar de `de` e `ate`.

◽ **situacao:** `pendente`, `confirmada`, `cancelada`, `compareceu` ou `nao-compareceu`. Outro valor é recusado.

◽ **mesaId:** só as reservas daquela mesa.

⚠️ **Filtro enviado vazio, como `situacao=` ou `ate=`, é recusado.** Tire da URL o filtro que não for usar.

➡️ **As reservas vêm em ordem de horário**, até 500 por chamada.

◽ Cada reserva traz o `id`, a `mesa` (`id` e `nome`, ou `null` quando a mesa é escolhida na chegada), o `inicio` e o `fim`, a `duracao` em minutos, as `pessoas`, o `cliente` (`contactId`, `nome` e `telefone`), a `observacao`, a `situacao`, a `origem`, o `motivo` e o `comandaId`.

◽ A `origem` diz de onde a reserva veio: `painel` (a equipe, na aba **Reservas** do menu **PDV  ›  Mesas e Comandas**), `api` ou `cardapio` (o cliente, pela loja).

◽ O `comandaId` é a conta da mesa aberta na chegada do cliente; antes disso, vem `null`.

◽ O `inicio` e o `fim` vêm em UTC, com o `Z` no fim: uma reserva para as 20:00 de Brasília vem como `23:00:00.000Z`. O `fim` é o início mais a duração.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/reservas?de={dataInicio}&ate={dataFim}&situacao={situacaoDaReserva}&mesaId={mesaId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/reservas?de={dataInicio}&ate={dataFim}&situacao={situacaoDaReserva}&mesaId={mesaId}' -H 'Authorization: Bearer {seutokenaqui}'
```
