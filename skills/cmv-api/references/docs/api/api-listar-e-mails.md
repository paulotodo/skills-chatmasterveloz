# API Listar E-mails

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-e-mails
- **Categoria:** APIs
- **Menu:** APIs › E-mail › API Listar E-mails

---

🧩 Obter a **lista de e-mails** recebidos e enviados pelas contas de e-mail da sua empresa, com filtros pela URL.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/email/messages?tipo={tipoDoEmail}&accountId={accountId}&desde={desde}&page={pageNumber}&pageSize={pageSize}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, por exemplo `?tipo=recebidos&pageSize=50`. Filtro que você não usar pode ficar vazio ou fora da URL.

◽ **“tipo”:** `recebidos`, `enviados` ou `todos`. Sem ele, vêm todos.

◽ **“accountId”:** só os e-mails daquela conta de e-mail. É o `id` da conta na lista de contas de e-mail.

◽ **“desde”:** só os e-mails daquela data e hora em diante, em ISO 8601, por exemplo `2026-11-05T08:00:00Z`. Também aceita só o dia, com o ano primeiro (`2026-11-05`) ou em dia/mês/ano (`05/11/2026`).

⚠️ Em dia/mês/ano, o dia vem primeiro: `11/05/2026` é 11 de maio. Data que não existe, como `31/02/2026`, é recusada.

◽ **“page”:** a página, a partir de 1.

◽ **“pageSize”:** quantos e-mails por página, de 1 a 100. Sem ele, vêm 20. Acima de 100, a chamada é recusada.

◽ Os e-mails vêm dos mais novos aos mais antigos, em `messages`, junto com `total`, `page`, `pageSize` e `hasMore`, que diz se há mais páginas.

◽ Cada e-mail vem com o `id`, a conta, a pasta, o `tipo` (`recebido` ou `enviado`), quem enviou, para quem, o assunto, o começo do texto, se tem anexo, se foi lido e a data. **O corpo do e-mail não vem na lista.**

➡️ **A lista é da empresa inteira**, qualquer que seja a Conexão do token.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/email/messages?tipo={tipoDoEmail}&accountId={accountId}&desde={desde}&page={pageNumber}&pageSize={pageSize}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/email/messages?tipo={tipoDoEmail}&accountId={accountId}&desde={desde}&page={pageNumber}&pageSize={pageSize}' -H 'Authorization: Bearer {seutokenaqui}'
```
