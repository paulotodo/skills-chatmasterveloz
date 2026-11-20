# API Listar Motivos de Perda

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-motivos-de-perda
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Listar Motivos de Perda

---

🧩 Listar os **motivos de perda** cadastrados.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/crm/v2/motivos-perda
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

◽ Use o id em `motivoPerdaId` ao mover uma oportunidade para uma raia de perda.

◽ Vêm os motivos globais, que valem em todos os funis, e os de cada funil — os globais primeiro.

◽ Vêm só os motivos ativos.

⚠️ **A empresa precisa estar com o CRM novo ativado.**

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/crm/v2/motivos-perda',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/crm/v2/motivos-perda' -H 'Authorization: Bearer {seutokenaqui}'
```
