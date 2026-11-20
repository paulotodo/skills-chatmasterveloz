# API Listar Funis

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-funis
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Listar Funis

---

🧩 Listar os **funis do CRM** da empresa, com as raias (lanes / colunas) de cada um.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/crm/v2/funis
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

◽ Comece por aqui: o **id do funil** e o **id da raia** (lane) são exigidos para criar e para mover oportunidades, e não há como adivinhá-los.

◽ Vêm só os funis ativos, cada um com as raias ativas, na ordem em que aparecem no quadro.

◽ Cada raia diz o tipo — em andamento, ganho ou perdido — e a probabilidade de fechar.

◽ A consulta enxerga a empresa inteira, inclusive os funis que no painel aparecem só para alguns operadores.

◽ O segredo do webhook do funil nunca vem na resposta.

⚠️ **A empresa precisa estar com o CRM novo ativado.**

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/crm/v2/funis',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/crm/v2/funis' -H 'Authorization: Bearer {seutokenaqui}'
```
