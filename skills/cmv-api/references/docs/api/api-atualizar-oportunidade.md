# API Atualizar Oportunidade

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-oportunidade
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Atualizar Oportunidade

---

🧩 Atualiza **uma oportunidade** do CRM — só o que vier no corpo muda.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}
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
    "name": "Reforma da loja",
    "valor": 15000,
    "userId": 5,
    "message": "Cliente pediu desconto",
    "laneId": 8,
    "produto": "Pacote completo",
    "productId": 22,
    "motivoPerdaId": null,
    "origemVendaId": 3,
    "previsaoFechamento": "2026-12-20",
    "fonte": "Indicação",
    "campanha": "Black Friday",
    "origem": "São Paulo",
    "destino": "Curitiba",
    "datadeida": "2026-12-01",
    "datadevolta": "2026-12-10",
    "free1": "",
    "free2": "",
    "free3": "",
    "free4": "",
    "tagIds": [3, 4]
}
```

➡️ **“oportunidadeId”:** ID da oportunidade — vai no próprio endereço, no lugar de `{oportunidadeId}`. **Obrigatório.**

⚠️ **O exemplo acima traz o que a chamada aceita, para você escolher** — não é obrigatório enviar inteiro. Os campos que você não enviar ficam como estão.

➡️ **“name”:** título do card.

➡️ **“valor”:** valor em formato decimal, com os centavos depois do **ponto**.

➡️ **“userId”:** ID do novo responsável, que precisa ser usuário da mesma empresa.

➡️ **“message”:** observações.

➡️ **“laneId”:** a raia. Só vale uma raia do funil em que a oportunidade já está; ao trocar de raia, a situação é recalculada.

➡️ **“produto”:** nome do produto, em texto livre. **“productId”:** o produto do catálogo.

➡️ **“motivoPerdaId”:** o motivo da perda, que só faz sentido em raia de perda. É **obrigatório** quando o `laneId` leva a oportunidade para uma raia de perda: sem ele, a chamada é recusada.

➡️ **“origemVendaId”:** a origem da venda.

➡️ **“previsaoFechamento”:** data prevista de fechamento.

➡️ **“wonAt”:** o dia do ganho, no formato `AAAA-MM-DD` ou com a hora (ISO 8601, como `2026-11-11T15:30:00-03:00`). Sem a hora, vale o meio-dia de Brasília. Só vale na oportunidade que fica **ganha**: a que já está ganha, ou a que vai para uma raia de ganho pelo `laneId` na mesma chamada. Na perdida ou na aberta, a chamada é recusada.

➡️ **“lostAt”:** o dia da perda, no mesmo formato. Só vale na oportunidade **perdida**; na ganha ou na aberta, a chamada é recusada.

◽ As duas datas ficam fora do exemplo porque cada uma só vale numa etapa. Mande uma só por chamada: `wonAt` e `lostAt` juntos são recusados, e a data no futuro ou que não existe também.

◽ Cada troca da data entra no **Histórico** da oportunidade (o evento `CLOSE_DATE_CHANGED`).

➡️ **“fonte”** e **“campanha”:** de onde a oportunidade veio.

➡️ **“origem”, “destino”, “datadeida” e “datadevolta”:** os campos de viagem.

➡️ **“free1”** a **“free4”:** os campos livres.

➡️ **“tagIds”:** as etiquetas. Aceita a lista `[3,4]` ou o texto `"3,4"`.

◽ Em `productId`, `motivoPerdaId` e `origemVendaId`, mande `null`, `""` ou `0` para limpar.

◽ **“tagIds” substitui TODAS as etiquetas** da oportunidade pela lista enviada.

◽ **O funil, o contato e o atendimento não mudam por aqui** — uma oportunidade não troca de funil.

◽ A chamada opera com a credencial da empresa: pode trocar o responsável, reabrir venda fechada e alterar valor ou produto de venda já ganha. As travas que valem para o operador no painel não valem aqui.

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
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "name": "Reforma da loja",
    "valor": 15000,
    "userId": 5,
    "message": "Cliente pediu desconto",
    "laneId": 8,
    "produto": "Pacote completo",
    "productId": 22,
    "motivoPerdaId": null,
    "origemVendaId": 3,
    "previsaoFechamento": "2026-12-20",
    "fonte": "Indicação",
    "campanha": "Black Friday",
    "origem": "São Paulo",
    "destino": "Curitiba",
    "datadeida": "2026-12-01",
    "datadevolta": "2026-12-10",
    "free1": "",
    "free2": "",
    "free3": "",
    "free4": "",
    "tagIds": [3, 4]
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"Reforma da loja","valor":15000,"userId":5,"message":"Cliente pediu desconto","laneId":8,"produto":"Pacote completo","productId":22,"motivoPerdaId":null,"origemVendaId":3,"previsaoFechamento":"2026-12-20","fonte":"Indicação","campanha":"Black Friday","origem":"São Paulo","destino":"Curitiba","datadeida":"2026-12-01","datadevolta":"2026-12-10","free1":"","free2":"","free3":"","free4":"","tagIds":[3,4]}'
```
