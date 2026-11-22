# API Atualizar Coluna do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-coluna-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Atualizar Coluna do Quadro

---

🧩 Atualiza **o nome e a cor de uma coluna** do quadro.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/colunas/{colunaId}
```

##### Método

```
PUT
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "nome": "Aguardando peça",
    "cor": "#8E24AA"
}
```

➡️ **“colunaId”:** ID da coluna — vai no próprio endereço, no lugar de `{colunaId}`. É o `id` que cada coluna traz na lista de quadros.

➡️ **“nome”:** o nome novo da coluna.

➡️ **“cor”:** a cor em hexadecimal, como `#8E24AA`.

◽ Mande só o que vai mudar.

◽ Na **Coluna automática por fila**, os Setores mudam com `queueIds`: a lista inteira, que substitui a anterior, como `"queueIds": [33]`. Lista vazia é recusada.

◽ A coluna **Pendentes** não muda de nome: a chamada é recusada. A **Atendendo** muda.

◽ O tipo da coluna não muda.

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
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Aguardando peça",
    "cor": "#8E24AA"
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/colunas/{colunaId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Aguardando peça","cor":"#8E24AA"}'
```
