# API Listar Atendimentos do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-atendimentos-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Listar Atendimentos do Quadro

---

🧩 Obter **os atendimentos de cada coluna** de um quadro, como a tela desenha.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/tickets
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

◽ O `quadroId` vai no próprio endereço: é o `id` do quadro.

◽ **queueIds**, **whatsappIds** e **userIds:** só os atendimentos destes Setores, Conexões ou atendentes. A lista vai entre colchetes, como `queueIds=[32]` ou `userIds=[11,17]`.

⚠️ Fora dos colchetes o filtro é ignorado, e vêm todos os atendimentos: `queueIds=32` não filtra.

◽ **searchParam:** busca no nome ou no número do contato.

◽ **semResposta:** `true` traz só os atendimentos sem resposta, como o filtro da tela.

◽ **isGroup:** `true` traz só os grupos; `false` deixa os grupos de fora.

◽ **visao:** `tags` troca as colunas pelas tags, como a visão por **Tags** da tela.

➡️ **Cada coluna traz o `total` e os `tickets`**, até 100 por coluna.

◽ Cada atendimento traz o `id`, o `status`, a última mensagem, o `contact`, o `queue`, o `whatsapp`, o `user` e o `fixado` — se está fixado no topo da coluna para quem pede.

◽ Na visão por tags, cada coluna traz o `tagId`, e cada atendimento traz as tags dele em `tagsDoQuadro`. A primeira coluna é a dos pendentes, e a última, a **Sem tag**.

◽ O `resumo` traz, por contato, os números que o card mostra: `oportunidades`, `agendamentos` e `anotacoes`.

◽ Para ver o quadro como uma pessoa da equipe vê, acrescente `userId` com o ID dela: vêm só os atendimentos que ela enxerga, e o quadro que não é dela é recusado. Sem ele, vêm todos.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/tickets',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/tickets' -H 'Authorization: Bearer {seutokenaqui}'
```
