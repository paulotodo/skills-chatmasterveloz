# API Deletar Tag

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-tag
- **Categoria:** APIs
- **Menu:** APIs › Tags › API Deletar Tag

---

🧩 Apaga **uma tag** do cadastro da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tags/{tagId}
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
// sem payload — a tag vai no endereço
```

➡️ **“tagId”:** ID da tag — vai no próprio endereço, no lugar de `{tagId}`. **Obrigatório.**

⚠️ **Isto não é tirar a tag de um Ticket.** A tag é apagada do cadastro da **empresa inteira** e some de todos os Tickets que a tinham.

◽ Não há como desfazer: não existe lixeira.

◽ A resposta diz quantos Tickets estavam com a tag no momento da exclusão.

◽ Tag que não existe e tag de outra empresa respondem a mesma coisa: não encontrada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tags/{tagId}',
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/tags/{tagId}' -H 'Authorization: Bearer {seutokenaqui}'
```
