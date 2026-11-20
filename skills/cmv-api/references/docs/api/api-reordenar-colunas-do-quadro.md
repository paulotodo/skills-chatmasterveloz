# API Reordenar Colunas do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-reordenar-colunas-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de Atendimentos › API Reordenar Colunas do Quadro

---

🧩 Reordena **as colunas** de um quadro de atendimentos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/colunas/ordem
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
    "ordem": [
        15,
        11,
        12
    ]
}
```

➡️ **“quadroId”:** ID do quadro — vai no próprio endereço, no lugar de `{quadroId}`.

➡️ **“ordem”:** os IDs de **todas** as colunas que você criou no quadro, na ordem nova, da esquerda para a direita.

◽ As duas fixas, Pendentes e Atendendo, ficam sempre no começo e não entram na lista.

⚠️ Lista com uma coluna fixa, ou sem alguma das suas, é recusada.

◽ A resposta traz todas as colunas, na ordem nova.

◽ Configurar o quadro é do administrador e do supervisor. Sem `userId`, quem faz é a empresa; para fazer em nome de uma pessoa, acrescente `?userId=` com o ID dela ao endereço — o de um atendente é recusado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/colunas/ordem',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "ordem": [
        15,
        11,
        12
    ]
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/colunas/ordem' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ordem":[15,11,12]}'
```
