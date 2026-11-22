# API Listar Quadros

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-quadros
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Listar Quadros

---

🧩 Obter a **lista de quadros de atendimentos** da sua empresa, cada um com as colunas.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros
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

◽ Cada quadro traz o `id`, o `nome`, o `ativo` e as `colunas`, na ordem do quadro.

◽ Cada coluna traz o `id`, o `nome`, a `cor`, a `ordem` e o `tipo`.

◽ O `tipo` de cada coluna: `PENDENTES` e `ATENDENDO` são as duas fixas; `LIVRE` é a **Coluna de atendimento**, `PENDENTE_LIVRE` a **Coluna de fila (pendente)** e `PENDENTE_FILA` a **Coluna automática por fila (pendente)**, com os Setores dela em `queueIds`.

◽ Os quadros desativados não vêm. Para incluí-los, acrescente `?incluirInativos=true` ao endereço.

◽ Para ver os quadros que uma pessoa da equipe abre na tela, acrescente `?userId=` com o ID dela: o atendente vê só os quadros atribuídos a ele. Sem `userId`, vêm todos os da empresa.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/ticket-quadros' -H 'Authorization: Bearer {seutokenaqui}'
```
