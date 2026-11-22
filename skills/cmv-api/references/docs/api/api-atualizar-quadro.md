# API Atualizar Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Atualizar Quadro

---

🧩 Atualiza **o nome de um quadro**, ou o desativa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}
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
    "nome": "Comercial",
    "ativo": true
}
```

➡️ **“quadroId”:** ID do quadro — vai no próprio endereço, no lugar de `{quadroId}`.

➡️ **“nome”:** o nome novo do quadro.

➡️ **“ativo”:** `false` tira o quadro da lista da tela, sem apagar a classificação dos atendimentos; `true` traz de volta.

◽ Mande só o que vai mudar.

◽ O quadro desativado continua aparecendo nas chamadas que pedem `incluirInativos=true` e na leitura do próprio quadro.

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
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Comercial",
    "ativo": true
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Comercial","ativo":true}'
```
