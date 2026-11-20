# API Obter uma Reserva

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-uma-reserva
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Obter uma Reserva

---

🧩 Obter **uma reserva** das Reservas pelo id.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/{reservaAgendaId}
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

➡️ Esta chamada não tem payload. O id da reserva vai no endereço, no lugar de `{reservaAgendaId}`.

◽ A reserva de outra empresa responde igual à que não existe.

➡️ **A resposta traz a reserva:** `id`, `codigo`, `situacao`, `origem`, a `oferta` e o `recurso`, o cliente (`contactId`, `clienteNome`, `clienteTelefone`, `clienteEmail`), `pessoas`, `inicio`, `fim`, `data`, `horaInicio`, `horaFim`, `modo`, `noites`, `dataSaida`, `observacao`, `preco`, `sinalValor`, `sinalAte`, o cancelamento (`motivoCancelamento`, `canceladaEm`) e o `link`.

◽ A reserva que usa pacote traz o `pacoteClienteId` e o `pacote`; a de uma série, o `serieId`, a `serieOrdem` e a `serie`.

◽ `origem`: de onde a reserva veio, como `api`, `painel`, `pagina` ou `fluxo`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/{reservaAgendaId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/{reservaAgendaId}' -H 'Authorization: Bearer {seutokenaqui}'
```
