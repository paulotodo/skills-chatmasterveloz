# API Listar Regras Pessoais do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-regras-pessoais-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Listar Regras Pessoais do Quadro

---

🧩 Obter **as regras do quadro que valem para uma pessoa**: as dela e as da equipe.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/regras?userId={userId}
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

◽ O `userId` é obrigatório: o ID da pessoa, no próprio endereço.

◽ A resposta tem duas listas, na ordem em que valem: `minhas`, as regras da pessoa, e `doAdmin`, as regras da equipe que valem para ela.

◽ Cada regra traz `id`, `nome`, `ativo`, `ordem`, `combinacao`, `condicoes`, a `coluna` de destino e o `quadro`.

◽ Em `rotulos`, os nomes das tags, Setores, contatos e Conexões usados nas condições.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras?userId={userId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras?userId={userId}' -H 'Authorization: Bearer {seutokenaqui}'
```
