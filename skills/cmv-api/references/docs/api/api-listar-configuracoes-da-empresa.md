# API Listar Configurações da Empresa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-configuracoes-da-empresa
- **Categoria:** APIs
- **Menu:** APIs › Extras › API Listar Configurações da Empresa

---

🧩 Listar as **Configurações da empresa** — as mesmas chaves da tela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}/settings
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

➡️ **“companyId”:** ID da **sua** empresa — vai no próprio endereço, no lugar de `{companyId}`. **Obrigatório.**

◽ O id da sua empresa aparece no campo `companyId` das respostas das outras chamadas.

◽ Vêm as chaves da tela **Configurações** — avaliação, fuso horário, carteira, roteador, tipo de bot, webhooks e as demais —, em ordem alfabética, cada uma com o valor e a data da última alteração.

◽ Todo valor vem como **texto**, mesmo o que na tela é sim ou não.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}/settings',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/companies/{companyId}/settings' -H 'Authorization: Bearer {seutokenaqui}'
```
