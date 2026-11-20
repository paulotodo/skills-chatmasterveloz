# API Deletar Regra do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-regra-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de Atendimentos › API Deletar Regra do Quadro

---

🧩 Apaga **uma regra do quadro**, pessoal ou da equipe.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/regras/{regraId}?userId={userId}
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

◽ O `regraId` vai no próprio endereço: é o `id` que a regra traz nas listas de regras.

◽ Na regra pessoal, o `userId` é o da dona da regra; outra pessoa, ou a chamada sem ele, não a encontra. Na regra da equipe, o de um administrador ou supervisor — ou tire o `userId` do endereço para fazer como a empresa.

◽ Os cards que a regra já organizou continuam onde estão.

◽ A resposta vem sem corpo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras/{regraId}?userId={userId}',
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras/{regraId}?userId={userId}' -H 'Authorization: Bearer {seutokenaqui}'
```
