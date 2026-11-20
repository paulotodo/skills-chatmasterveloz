# API Listar Configurações de Campanha

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-configuracoes-de-campanha
- **Categoria:** APIs
- **Menu:** APIs › Campanhas › API Listar Configurações de Campanha

---

🧩 Obter as **configurações de disparo das Campanhas** — o intervalo entre as mensagens, o lote, o intervalo maior e as variáveis.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}/campaign-settings
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
// sem payload — a empresa vai no endereço
```

➡️ **“companyId”:** ID da empresa — vai no próprio endereço, no lugar de `{companyId}`. **Obrigatório.**

➡️ Esta chamada não tem payload.

◽ Estas configurações são gravadas **à parte** das configurações gerais da empresa.

➡️ **A resposta traz o que vale de fato no envio:** o que foi gravado e, para o que nunca foi, o padrão — e esse padrão vem separado, em `padrao`.

◽ Os valores de fábrica são **400 ms** entre mensagens, lote de **10**, intervalo maior de **1000 ms** e nenhuma variável.

◽ Os intervalos são sempre em **milissegundos**.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}/campaign-settings',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/companies/{companyId}/campaign-settings' -H 'Authorization: Bearer {seutokenaqui}'
```
