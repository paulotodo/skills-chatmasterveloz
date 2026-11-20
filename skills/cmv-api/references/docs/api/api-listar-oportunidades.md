# API Listar Oportunidades

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-oportunidades
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Listar Oportunidades

---

🧩 Listar **oportunidades** do CRM, com filtros e páginas.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/crm/v2/oportunidades?status={statusDaOportunidade}&pageNumber={pageNumber}&pageSize={pageSize}
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
// sem payload — os filtros vão na própria URL
```

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, por exemplo `?pipelineId=7&status=OPEN`.

◽ **“pipelineId”:** só as de um funil. **“laneId”:** só as de uma raia.

◽ **“userId”:** só as de um responsável. **“contactId”:** só as de um contato.

◽ **“status”:** `OPEN`, `WON` ou `LOST`. Aceita minúsculas.

◽ **“dataInicial”** e **“dataFinal”:** cortam pela **data de criação**, no formato `AAAA-MM-DD`; o fim inclui o dia inteiro. Outro formato responde erro.

◽ **“searchParam”:** procura no título, no produto, nas observações e no nome e número do contato.

◽ **“pageNumber”** e **“pageSize”:** página e quantos por página. Padrão `1` e `20`; o teto é `100`.

◽ A lista traz a empresa inteira. Para recortar por operador, use o `userId` — a chamada não tem usuário por trás.

◽ Cada linha vem com o contato, o atendimento, o responsável, o funil, a raia, o motivo de perda e a origem. As **etiquetas não vêm aqui**: elas aparecem quando você consulta uma oportunidade pelo id.

◽ A ordem é do id mais novo para o mais antigo, estável para sincronização.

⚠️ **A empresa precisa estar com o CRM novo ativado.**

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/crm/v2/oportunidades?status={statusDaOportunidade}&pageNumber={pageNumber}&pageSize={pageSize}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/crm/v2/oportunidades?status={statusDaOportunidade}&pageNumber={pageNumber}&pageSize={pageSize}' -H 'Authorization: Bearer {seutokenaqui}'
```
