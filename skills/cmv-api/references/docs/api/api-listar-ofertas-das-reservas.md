# API Listar Ofertas das Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-ofertas-das-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Listar Ofertas das Reservas

---

🧩 Obter a **lista de ofertas** das Reservas — o que o cliente reserva, como o serviço, a mesa, o quarto ou a aula —, na ordem do cadastro.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/ofertas
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

◽ Para só as ofertas ativas, as que a página de reservas e o fluxo oferecem, acrescente `?ativas=true` ao endereço.

➡️ **A resposta traz as ofertas**, cada uma com `id`, `nome`, `descricao`, `modo`, `duracaoMinutos`, `preco`, `pessoasMin`, `pessoasMax`, `ativo` e os `recursoIds` dos recursos que a atendem.

◽ `modo`: `horario`, `diaria` ou `turma`.

◽ Na diária, o `preco` é o de uma noite, e a oferta traz também o horário de entrada e de saída e as noites que aceita.

◽ Na turma, a oferta traz as `vagas` de cada sessão.

◽ O `id` da oferta é o `ofertaId` das chamadas de horários livres, de noites livres e de criar a reserva.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/ofertas',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/ofertas' -H 'Authorization: Bearer {seutokenaqui}'
```
