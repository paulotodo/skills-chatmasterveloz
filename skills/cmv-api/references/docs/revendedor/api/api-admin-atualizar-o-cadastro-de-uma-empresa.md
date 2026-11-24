# API Atualizar o Cadastro de uma Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-atualizar-o-cadastro-de-uma-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Empresas › API Atualizar o Cadastro de uma Empresa

---

🧩 Atualiza o **cadastro de uma empresa** — só o que vier no corpo muda.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}
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
    "name": "Loja X",
    "phone": "11933334444",
    "email": "financeiro@lojax.com.br",
    "planId": 3,
    "dueDate": "2026-12-10"
}
```

➡️ **“companyId”:** ID da empresa — vai no próprio endereço, no lugar de `{companyId}`. **Obrigatório.**

➡️ **“name”:** nome da empresa. Não pode ficar vazio.

➡️ **“phone”:** telefone de contato.

➡️ **“email”:** e-mail de cadastro.

➡️ **“planId”:** ID do plano da empresa.

➡️ **“dueDate”:** data de vencimento.

⚠️ **Mexer no plano ou no vencimento sincroniza a fatura em aberto** e religa as conexões da empresa que estiverem fora do ar. Não é uma alteração só de cadastro.

◽ Plano que não existe é recusado **antes** de qualquer coisa acontecer com a fatura.

◽ **Outros campos de cadastro:** `namecomplete`, `document`, `pais`, `country`, `recurrence`, `status`, `indicator`, `importar`.

◽ **Recursos e modos:** `campaignsEnabled`, `hybrid_mode`, `alternative_mode`, `concatenation_mode`, `blockGroups`, `blockRead`, `call_minuts`, `voiceBilling`, `apiUsada`, `logar`, `ambiente`.

◽ **Aparência e infraestrutura:** `useCustomCss`, `customCss`, `customJs`, `chatCss`, `useProxy`, `proxyURL`, `keystorage`, os campos de iframe do painel, `typebotName` e `typebotUrl`.

◽ Os campos que você não enviar ficam como estão. Campo desconhecido é ignorado e volta listado na resposta.

◽ Sem nenhum campo editável, a chamada é recusada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "name": "Loja X",
    "phone": "11933334444",
    "email": "financeiro@lojax.com.br",
    "planId": 3,
    "dueDate": "2026-12-10"
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/companies/{companyId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"Loja X","phone":"11933334444","email":"financeiro@lojax.com.br","planId":3,"dueDate":"2026-12-10"}'
```
