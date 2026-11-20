# API Mover Oportunidade de Raia

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-mover-oportunidade-de-raia
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Mover Oportunidade de Raia

---

🧩 Move **uma oportunidade** para outra raia (lane / coluna) do mesmo funil.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}/mover
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
    "laneId": 33,
    "motivoPerdaId": 60
}
```

➡️ **“oportunidadeId”:** ID da oportunidade — vai no próprio endereço, no lugar de `{oportunidadeId}`. **Obrigatório.**

➡️ **“laneId”:** ID da raia de destino, do **mesmo funil** da oportunidade. **Obrigatório.**

➡️ **“motivoPerdaId”:** ID do motivo da perda. **Obrigatório** quando a raia de destino é de perda: sem ele, a chamada é recusada com **400** `ERR_CRM_MOTIVO_DA_PERDA_OBRIGATORIO`.

➡️ **“posicao”:** opcional. Posição dentro da raia, começando em `0` no topo. Sem ela, a oportunidade vai para o topo.

◽ A situação vem da raia de destino: raia de ganho marca a venda como ganha, raia de perda como perdida, e raia em andamento **reabre** a oportunidade.

◽ Mover para a raia em que a oportunidade já está apenas reordena a coluna.

◽ A chamada pode reabrir venda fechada — no painel isso é só de administrador.

◽ Id que não existe e id de outra empresa respondem a mesma coisa: não encontrado. A chamada não confirma quais ids existem no sistema.

⚠️ **A empresa precisa estar com o CRM novo ativado.**

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}/mover',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "laneId": 33,
    "motivoPerdaId": 60
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}/mover' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"laneId":33,"motivoPerdaId":60}'
```
