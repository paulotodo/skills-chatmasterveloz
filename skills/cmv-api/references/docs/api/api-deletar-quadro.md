# API Deletar Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Deletar Quadro

---

🧩 Apaga **um quadro de atendimentos** e as colunas dele.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}
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

◽ O `quadroId` vai no próprio endereço: é o `id` do quadro.

⚠️ Nenhum atendimento é encerrado nem apagado. Somem o quadro, as colunas, a classificação que existia nele e as atribuições: quem tinha o quadro deixa de vê-lo.

◽ Não tem volta: depois de apagado, o quadro não é mais encontrado.

◽ Configurar o quadro é do administrador e do supervisor. Sem `userId`, quem faz é a empresa; para fazer em nome de uma pessoa, acrescente `?userId=` com o ID dela ao endereço — o de um atendente é recusado.

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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}' -H 'Authorization: Bearer {seutokenaqui}'
```
