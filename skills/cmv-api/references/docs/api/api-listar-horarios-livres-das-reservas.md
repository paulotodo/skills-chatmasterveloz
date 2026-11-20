# API Listar Horários Livres das Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-horarios-livres-das-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Listar Horários Livres das Reservas

---

🧩 Obter os **horários livres** de uma oferta num dia, pela mesma regra que a reserva confere.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/horarios?ofertaId={ofertaId}&data={dataDaReserva}
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

◽ **ofertaId:** a oferta. **Obrigatório.**

◽ **data:** o dia, no formato `AAAA-MM-DD`. **Obrigatório.**

◽ Também filtram: **recursoId** (só este recurso; sem ele, todos os que atendem a oferta) e **pessoas** (entre o mínimo e o máximo da oferta; sem ele, o mínimo).

◽ Para ver os horários como o cliente vê na página de reservas, com a antecedência e o limite de dias à frente, acrescente `&comoCliente=true`. Sem ele, a chamada vê a agenda como a equipe.

➡️ **A resposta traz os `horarios` livres**, cada um com `inicio`, `fim`, `hora` e os `recursoIds` livres naquele horário.

◽ Na turma, cada horário traz as `vagas` que sobram na sessão.

◽ Dia sem atendimento devolve a lista vazia.

◽ A oferta por diária não tem horário: a lista vem vazia. Para ela, use a chamada das noites livres.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/horarios?ofertaId={ofertaId}&data={dataDaReserva}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/horarios?ofertaId={ofertaId}&data={dataDaReserva}' -H 'Authorization: Bearer {seutokenaqui}'
```
