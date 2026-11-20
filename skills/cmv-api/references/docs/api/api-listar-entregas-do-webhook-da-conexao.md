# API Listar Entregas do Webhook da Conexão

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-entregas-do-webhook-da-conexao
- **Categoria:** APIs
- **Menu:** APIs › Conexões › API Listar Entregas do Webhook da Conexão

---

🧩 Obter **as entregas do webhook** de uma Conexão ou de um Setor nos últimos 7 dias — para buscar de novo um aviso que não chegou.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/webhook-da-conexao/entregas?destino={destino}&desde={desde}&limite={limite}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL.

◽ **destino:** obrigatório. A URL que recebe os avisos, exatamente como está cadastrada — o webhook ou o webhook B da Conexão, ou o webhook do Setor.

◽ A URL vai codificada: `https://minha-automacao.com/hook` vira `https%3A%2F%2Fminha-automacao.com%2Fhook`.

◽ **desde:** vêm as entregas com `sequencia` maior que este número. Padrão `0`, desde a primeira guardada.

◽ **limite:** quantas entregas, de 1 a 500. Padrão `100`.

➡️ **Cada aviso desses webhooks traz a `sequencia`:** o número da entrega naquele destino, que sobe 1 a cada aviso. Recebeu a 41 e depois a 43? A 42 se perdeu: busque com `desde=41`.

◽ A resposta traz `ultimaSequencia` (o último número do destino), `diasGuardados`, `temMais` e as `entregas`. Com `temMais` em `true`, busque de novo a partir da última `sequencia` recebida.

◽ Cada entrega traz `sequencia`, `eventoId`, `evento` (o mesmo `acao` do aviso), `entregue` (se a URL respondeu com sucesso; `null` quando ainda não se sabe), `statusHttp` e o `corpo` enviado.

➡️ **Use o `eventoId` para descartar o repetido:** é o mesmo em todos os destinos que recebem o mesmo fato, e o mesmo ao buscar de novo.

◽ Com o Token da Empresa gerado, cada aviso leva o cabeçalho `X-Assinatura-Conexao`: `sha256=` e o HMAC-SHA256 do corpo, com o Token da Empresa como chave. A entrega traz essa assinatura em `assinatura`, e o texto que ela cobre, em `corpoOriginal`.

◽ Destino que nunca recebeu aviso da empresa é recusado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/webhook-da-conexao/entregas?destino={destino}&desde={desde}&limite={limite}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/webhook-da-conexao/entregas?destino={destino}&desde={desde}&limite={limite}' -H 'Authorization: Bearer {seutokenaqui}'
```
