# API Obter uma Reserva de Mesa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-uma-reserva-de-mesa
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Obter uma Reserva de Mesa

---

🧩 Obter **uma reserva de mesa específica**, com a mesa, o horário, as pessoas, o cliente e a situação.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}
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

◽ O `reservaId` vai no próprio endereço: é o ID da reserva, que vem na lista de reservas e na resposta da criação. Reserva que não existe é recusada.

◽ A reserva traz a `mesa` (`id` e `nome`, ou `null` quando a mesa é escolhida na chegada), o `inicio` e o `fim`, a `duracao` em minutos, as `pessoas`, o `cliente` (`contactId`, `nome` e `telefone`), a `observacao`, a `situacao`, a `origem` (`painel`, `api` ou `cardapio`), o `motivo` e o `comandaId` — a conta da mesa aberta na chegada.

◽ O `inicio` e o `fim` vêm em UTC, com o `Z` no fim: uma reserva para as 20:00 de Brasília vem como `23:00:00.000Z`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}' -H 'Authorization: Bearer {seutokenaqui}'
```
