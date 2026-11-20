# API Listar Agendamentos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-agendamentos
- **Categoria:** APIs
- **Menu:** APIs › Agendamentos › API Listar Agendamentos

---

🧩 Obter a **lista de mensagens agendadas** da sua empresa, da mais próxima de ser enviada à mais distante.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/schedules?situacao={situacaoDoAgendamento}&contactId={contactId}&de={dataInicio}&ate={dataFim}&pageNumber={pageNumber}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, e todos são opcionais.

◽ **situacao:** `pendente`, `enviado` ou `erro`. O `pendente` inclui o que vai ser enviado nos próximos 30 segundos.

◽ **contactId:** só os agendamentos deste contato.

◽ **de** e **ate:** envio a partir de e até esse dia, no formato `AAAA-MM-DD` ou `DD/MM/AAAA`.

⚠️ Em `DD/MM/AAAA`, o dia vem primeiro: `01/10/2026` é 1º de outubro.

◽ Também filtram: **conexaoId** (só os desta Conexão) e **userId** (só os criados por este usuário).

◽ **pageNumber:** a página, de **20 em 20**. Padrão `1`. O `temMais` da resposta diz se há outra página.

➡️ **A resposta traz `agendamentos`, `total`, `pagina` e `temMais`.**

◽ Cada agendamento traz `id`, `texto`, `envioEm`, `enviadoEm`, `situacao`, `erroMotivo`, `repeticao`, `contato`, `conexaoId`, `usuario`, `setorId`, `abrirAtendimento`, `template` e `arquivo`.

◽ `envioEm` e `enviadoEm` vêm em UTC, com o `Z` no fim.

➡️ **A lista é da empresa inteira**, qualquer que seja a Conexão do token.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/schedules?situacao={situacaoDoAgendamento}&contactId={contactId}&de={dataInicio}&ate={dataFim}&pageNumber={pageNumber}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/schedules?situacao={situacaoDoAgendamento}&contactId={contactId}&de={dataInicio}&ate={dataFim}&pageNumber={pageNumber}' -H 'Authorization: Bearer {seutokenaqui}'
```
