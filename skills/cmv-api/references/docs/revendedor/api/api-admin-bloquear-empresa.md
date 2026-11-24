# API Bloquear Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-bloquear-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Empresas › API Bloquear Empresa

---

🧩 Deixa **uma empresa inativa**.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}/block
```

##### Método

```
POST
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

◽ A empresa para de ser processada: a fila de atendimentos deixa de atendê-la e as sessões de WhatsApp não sobem mais para ela.

◽ **Não mexe em fatura nem em plano** — é só a chave de ativa ou inativa.

◽ A empresa do Super Admin não pode ser bloqueada.

◽ Com a empresa inativa, a tela **Conexões** dela explica o motivo e orienta a reativação quando alguém tenta criar uma conexão, gerar o QR Code ou iniciar uma nova sessão, e nada é criado pela metade.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}/block',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/companies/{companyId}/block' -H 'Authorization: Bearer {seutokenaqui}'
```
