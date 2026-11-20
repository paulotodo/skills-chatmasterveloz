# API Listar Recursos das Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-recursos-das-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Listar Recursos das Reservas

---

🧩 Obter a **lista de recursos** das Reservas — quem ou o que atende a reserva, como o profissional, a mesa, a sala ou o quarto —, na ordem do cadastro.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/recursos
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

◽ Para só os recursos ativos, acrescente `?ativos=true` ao endereço.

➡️ **A resposta traz os recursos**, cada um com `id`, `tipo`, `nome`, `descricao`, `fotoUrl`, `capacidade`, `userId` (o usuário da plataforma ligado ao recurso), `ativo` e `ordem`.

◽ O recurso traz também a ligação com a agenda do Google: `agendaGoogle`, `agendaGoogleId`, `agendaGoogleBloqueia`, `agendaGoogleSincronizadaEm` e `agendaGoogleErro`.

◽ O `id` do recurso é o `recursoId` das outras chamadas das Reservas.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/recursos',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/recursos' -H 'Authorization: Bearer {seutokenaqui}'
```
