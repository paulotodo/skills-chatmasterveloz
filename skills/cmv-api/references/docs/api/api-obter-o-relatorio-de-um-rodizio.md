# API Obter o Relatório de um Rodízio

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-o-relatorio-de-um-rodizio
- **Categoria:** APIs
- **Menu:** APIs › Rodízios › API Obter o Relatório de um Rodízio

---

🧩 Obter o **Relatório do Rodízio** de um rodízio cadastrado, num período.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/rodizios/{rodizioId}/relatorio?dataInicio={dataInicio}&dataFim={dataFim}
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
// sem payload — o período vai na própria URL
```

➡️ **“rodizioId”:** ID do rodízio — vai no próprio endereço, no lugar de `{rodizioId}`. **Obrigatório.**

◽ O ID vem na lista de rodízios da empresa. Rodízio que não existe responde **não encontrado** (`404`).

➡️ O período vai como **query** na URL, no formato `AAAA-MM-DD`, e é opcional:

◽ **dataInicio:** o primeiro dia. Sem ele, 29 dias antes do fim — os últimos 30 dias.

◽ **dataFim:** o último dia, inteiro. Sem ele, hoje.

◽ Os dias contam no horário de Brasília. O período vai até 366 dias; fim antes do início, ou data em outro formato, é recusado.

➡️ **A resposta traz os números da tela do Relatório do Rodízio:**

◽ por operador, quantos atendimentos recebeu, a participação, a meta do cadastro e a diferença;

◽ quantos atendimentos o rodízio não conseguiu entregar (o transbordo), e para que Setor foi cada um.

◽ Todo participante do cadastro aparece, mesmo com zero no período. Quem recebeu e saiu do cadastro aparece com `noRodizio` em `false`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/rodizios/{rodizioId}/relatorio?dataInicio={dataInicio}&dataFim={dataFim}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/rodizios/{rodizioId}/relatorio?dataInicio={dataInicio}&dataFim={dataFim}' -H 'Authorization: Bearer {seutokenaqui}'
```
