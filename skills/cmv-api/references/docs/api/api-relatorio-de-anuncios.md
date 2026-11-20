# API Relatório de Anúncios

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-relatorio-de-anuncios
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Relatório de Anúncios

---

🧩 Listar, **por anúncio**, quantos leads entraram e quantos viraram venda.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/anuncios?dataInicio={dataInicio}&dataFim={dataFim}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, por exemplo `?dataInicio=2026-09-01&dataFim=2026-09-30`.

◽ **“dataInicio”:** início do período, no formato `AAAA-MM-DD` ou `DD/MM/AAAA`. Sem as duas datas, valem os últimos 30 dias.

◽ **“dataFim”:** fim do período, no formato `AAAA-MM-DD` ou `DD/MM/AAAA`, incluindo o dia inteiro. Data que não existe, como `31/02/2026`, é recusada.

◽ O anúncio é o **Click-to-WhatsApp da Meta**, reconhecido no primeiro contato do lead.

◽ O período filtra a **chegada do lead**. A venda dele entra na conta mesmo que tenha sido fechada depois do período.

◽ Venda é a oportunidade **ganha** no CRM.

◽ A consulta traz até 5000 leads. Acima disso a resposta avisa que veio cortada — estreite o período.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/anuncios?dataInicio={dataInicio}&dataFim={dataFim}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/anuncios?dataInicio={dataInicio}&dataFim={dataFim}' -H 'Authorization: Bearer {seutokenaqui}'
```
