# API Listar Situações dos Projetos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-situacoes-dos-projetos
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Listar Situações dos Projetos

---

🧩 Obter a **lista de situações dos projetos** da sua empresa, na ordem das colunas do quadro de **Projetos**.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos/situacoes
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

◽ Vêm as situações da janela **Situações dos projetos**, no menu **Projetos**: as quatro que vêm de início e as que a empresa cria.

◽ Cada situação traz a `chave`, o `nome`, a `cor` e o `padrao`.

◽ É desta `chave` que o campo `situacao` de um projeto precisa — na criação, na atualização e no filtro da lista de projetos. O nome da situação não serve.

◽ As quatro que vêm de início têm as chaves `planejamento`, `andamento`, `pausado` e `concluido`, e vêm com `padrao: true`. Renomeada, a situação vem com o nome novo e a mesma chave.

◽ As que a empresa cria vêm com `padrao: false` e uma chave como `s17942257596924`.

◽ A `cor` é a da coluna, em hexadecimal, como `#e91e63`. Sem cor, vem `null`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/projetos/situacoes',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token da Empresa
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X GET 'https://api2.chatmasterveloz.com/api/projetos/situacoes' -H 'Authorization: Bearer {seutokenaqui}'
```
