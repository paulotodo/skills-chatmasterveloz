# API Conferir as Datas de uma Série de Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-conferir-as-datas-de-uma-serie-de-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Conferir as Datas de uma Série de Reservas

---

🧩 Obter **as datas de uma série de reservas** antes de criá-la, com as datas livres e as que não servem, sem gravar nada.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/series/previa
```

##### Método

```
POST
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "ofertaId": 23,
    "inicio": "2026-12-07T09:00:00-03:00",
    "clienteNome": "Ana Souza",
    "repetir": {
        "frequencia": "semanal",
        "vezes": 4
    }
}
```

➡️ **“ofertaId”:** a oferta reservada. **Obrigatório.** A diária não se repete.

➡️ **“inicio”:** o início da primeira data, como `2026-12-07T09:00:00-03:00`. As outras datas ficam no mesmo horário.

➡️ **“clienteNome”:** o nome do cliente, ou o `contactId` no lugar dele. Valem os mesmos campos da chamada de criar a reserva: `recursoId`, `pessoas`, `clienteTelefone`, `clienteEmail`, `observacao` e `pacoteClienteId`.

➡️ **“repetir”:** como a reserva se repete. **Obrigatório.**

◽ `frequencia`: `diaria` (todo dia), `semanal`, `quinzenal` (a cada 14 dias) ou `mensal` (o mesmo dia do mês; no mês que não tem o dia, o último dele).

◽ `vezes`: quantas datas, contando a primeira, de 2 a 52. A série inteira cabe em um ano.

◽ Cada data passa pela mesma regra da reserva: o recurso, o horário de atendimento, os bloqueios, as vagas da turma e o pacote, que gasta um crédito por data.

➡️ **A resposta traz a conta da série:** `frequencia`, `vezes`, `livres`, `ocupadas` e as `datas`.

◽ Cada data traz `ordem`, `data`, `hora`, `inicio`, o `recursoId` e o `motivo`: por que a data não serve, ou `null` quando está livre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/series/previa',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ofertaId": 23,
    "inicio": "2026-12-07T09:00:00-03:00",
    "clienteNome": "Ana Souza",
    "repetir": {
        "frequencia": "semanal",
        "vezes": 4
    }
}',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/reservas/series/previa' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ofertaId":23,"inicio":"2026-12-07T09:00:00-03:00","clienteNome":"Ana Souza","repetir":{"frequencia":"semanal","vezes":4}}'
```
