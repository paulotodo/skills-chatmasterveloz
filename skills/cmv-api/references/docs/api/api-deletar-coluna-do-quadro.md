# API Deletar Coluna do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-coluna-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Deletar Coluna do Quadro

---

🧩 Apaga **uma coluna** do quadro de atendimentos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/colunas/{colunaId}
```

##### Método

```
DELETE
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

◽ O `colunaId` vai no próprio endereço: é o `id` que cada coluna traz na lista de quadros.

◽ Os atendimentos que estavam numa coluna de atendimento voltam para **Atendendo**. Nenhum é encerrado.

◽ As duas colunas fixas, Pendentes e Atendendo, não se apagam: a chamada é recusada.

◽ Configurar o quadro é do administrador e do supervisor. Sem `userId`, quem faz é a empresa; para fazer em nome de uma pessoa, acrescente `?userId=` com o ID dela ao endereço — o de um atendente é recusado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/colunas/{colunaId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/ticket-quadros/colunas/{colunaId}' -H 'Authorization: Bearer {seutokenaqui}'
```
