# API Listar Contatos de uma Tag

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-contatos-de-uma-tag
- **Categoria:** APIs
- **Menu:** APIs › Contatos › API Listar Contatos de uma Tag

---

🧩 Listar os **contatos que têm uma tag**, seja ela de que tipo for.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tags/{tagId}/contacts?searchParam={searchParam}
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
// sem payload — a tag vai no endereço e o filtro na própria URL
```

➡️ **“tagId”:** ID da tag — vai no próprio endereço, no lugar de `{tagId}`. **Obrigatório.**

◽ **“searchParam”:** filtra por nome, número ou e-mail do contato. Vai como **query** na URL.

◽ Cada contato aparece **uma vez**, mesmo que tenha vários Tickets com a tag.

◽ Cada um diz de onde a tag veio: do **Ticket** (posta na tela, no Kanban, por fluxo ou por API), do **Encerramento** (a tag escolhida ao encerrar) e/ou do **CRM** (a tag na oportunidade, do CRM atual ou do antigo).

◽ Entra também quem tem a tag apenas numa oportunidade do CRM, sem Ticket ligado.

◽ Vem também o Ticket mais recente em que a tag aparece e a oportunidade mais recente com a tag.

◽ A lista vem em ordem de nome. Tag que ninguém tem responde lista vazia, e não erro.

◽ Tag que não existe e tag de outra empresa respondem a mesma coisa: não encontrada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tags/{tagId}/contacts?searchParam={searchParam}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/tags/{tagId}/contacts?searchParam={searchParam}' -H 'Authorization: Bearer {seutokenaqui}'
```
