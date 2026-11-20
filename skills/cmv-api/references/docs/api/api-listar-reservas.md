# API Listar Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Listar Reservas

---

🧩 Obter a **lista de reservas** de um período, da mais cedo à mais tarde, com a oferta e o recurso de cada uma.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas?de={dataInicio}&ate={dataFim}
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

◽ **de** e **ate:** o período, no formato `AAAA-MM-DD`, com os dois dias inclusos, de até 62 dias. Sem as datas, só as de hoje.

◽ Também filtram: **recursoId** (só deste recurso), **contactId** (as reservas do contato, inclusive as feitas pela equipe) e **situacao** (só desta situação).

◽ As canceladas só vêm pedidas: acrescente `&canceladas=true` para incluí-las, ou `&situacao=cancelada` para ver só elas.

➡️ **A resposta traz `de`, `ate`, `fuso`, `total` e `reservas`**, cada uma com os mesmos campos da chamada de obter uma reserva.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas?de={dataInicio}&ate={dataFim}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas?de={dataInicio}&ate={dataFim}' -H 'Authorization: Bearer {seutokenaqui}'
```
