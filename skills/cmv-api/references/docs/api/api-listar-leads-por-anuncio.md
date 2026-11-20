# API Listar Leads por Anúncio

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-leads-por-anuncio
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Listar Leads por Anúncio

---

🧩 Listar **leads** que entraram por anúncio.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/anuncios/leads?anuncioId={anuncioId}&dataInicio={dataInicio}&dataFim={dataFim}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, por exemplo `?anuncioId=120210000000000000&dataInicio=2026-09-01`.

◽ **“anuncioId”:** só os leads daquele anúncio. Com `__sem_id__` vêm os que chegaram sem identificação de anúncio.

◽ **“dataInicio”** e **“dataFim”:** período de entrada do lead, no formato `AAAA-MM-DD` ou `DD/MM/AAAA`. Sem as duas, valem os últimos 30 dias.

⚠️ Em `DD/MM/AAAA`, o dia vem primeiro: `01/10/2026` é 1º de outubro. Data que não existe, como `31/02/2026`, ou em outro formato é recusada.

◽ Cada lead vem com o contato, a conexão e o atendimento que nasceram do clique, a data de entrada, as tags daquele atendimento e se converteu.

◽ A **origem** (Facebook, Instagram) só aparece quando o canal informa: o `whatsapp_whatsmeow_pro` informa, a API oficial não.

◽ Lead antigo pode vir sem conexão, porque ela só passou a ser gravada depois.

◽ A consulta traz até 500 leads. Acima disso a resposta avisa que veio cortada — estreite por anúncio e por período.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/anuncios/leads?anuncioId={anuncioId}&dataInicio={dataInicio}&dataFim={dataFim}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/anuncios/leads?anuncioId={anuncioId}&dataInicio={dataInicio}&dataFim={dataFim}' -H 'Authorization: Bearer {seutokenaqui}'
```
