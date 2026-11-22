# API Obter um Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-um-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Obter um Quadro

---

🧩 Obter **um quadro de atendimentos específico**, com as colunas.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}
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

◽ O `quadroId` vai no próprio endereço: é o `id` que vem na lista de quadros e na resposta da criação. Quadro que não existe é recusado.

◽ O quadro traz o `id`, o `nome`, o `ativo` e as `colunas`, cada uma com `id`, `nome`, `cor`, `ordem` e `tipo`.

◽ O `tipo` de cada coluna: `PENDENTES` e `ATENDENDO` são as duas fixas; `LIVRE` é a **Coluna de atendimento**, `PENDENTE_LIVRE` a **Coluna de fila (pendente)** e `PENDENTE_FILA` a **Coluna automática por fila (pendente)**, com os Setores dela em `queueIds`.

◽ Vem também o quadro desativado, com `ativo` em `false`.

◽ Para ver como uma pessoa da equipe vê, acrescente `?userId=` com o ID dela ao endereço. Sem ele, quem pede é a empresa, e vem tudo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}' -H 'Authorization: Bearer {seutokenaqui}'
```
