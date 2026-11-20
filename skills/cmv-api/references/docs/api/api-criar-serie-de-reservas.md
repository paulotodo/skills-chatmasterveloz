# API Criar Série de Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-serie-de-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Criar Série de Reservas

---

🧩 Cria **uma série de reservas**: a mesma reserva em várias datas, toda semana, a cada 14 dias, todo mês ou todo dia, de uma vez.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/series
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
        "vezes": 4,
        "pularOcupadas": true
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

◽ `pularOcupadas`: `true` deixa de fora as datas que não servem e cria as outras. Sem ele, uma data que não serve impede a série inteira.

➡️ **A resposta traz a `serie`** (`id`, `frequencia`, `vezes`, `criadas`, `puladas`), as `reservas` criadas, cada uma com o `serieId` e a `serieOrdem`, e as `datas`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/series',
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
        "vezes": 4,
        "pularOcupadas": true
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
curl -X POST 'https://api2.chatmasterveloz.com/api/reservas/series' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ofertaId":23,"inicio":"2026-12-07T09:00:00-03:00","clienteNome":"Ana Souza","repetir":{"frequencia":"semanal","vezes":4,"pularOcupadas":true}}'
```
