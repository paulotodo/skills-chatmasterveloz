# API Obter uma Oportunidade

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-uma-oportunidade
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Obter uma Oportunidade

---

🧩 Obter **uma oportunidade** do CRM, com tudo o que está ligado a ela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}
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

➡️ **“oportunidadeId”:** ID da oportunidade — no lugar de `{oportunidadeId}`. **Obrigatório.**

◽ Vem o registro completo com o contato e a foto, o atendimento e a conexão por onde a conversa corre, o responsável, as etiquetas, o funil e a raia.

◽ Quando o card nasceu do encadeamento de outro funil, vem também a oportunidade que o originou.

◽ Id que não existe e id de outra empresa respondem a mesma coisa: não encontrado. A chamada não confirma quais ids existem no sistema.

⚠️ **A empresa precisa estar com o CRM novo ativado.**

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}' -H 'Authorization: Bearer {seutokenaqui}'
```
