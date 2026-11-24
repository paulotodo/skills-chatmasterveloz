# API Pagar Fatura

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-pagar-fatura
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Faturas › API Pagar Fatura

---

🧩 Registrar o pagamento de **uma fatura** específica.

⚠️ Esta chamada exige um token da **empresa do Super Admin**. Serve tanto o token de uma Conexão dela quanto o **Token da Empresa**, gerado em **Configurações → Token da Empresa**. Token de outra empresa não é aceito.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/subscription/manualpaid
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

```json
{
    "invoiceId": "28",
    "payment_status": "Completed",
    "paymentId": "IDENTIFICACAO_DO_PAGAMENTO_9031203120"
}
```

➡️ **“invoiceId”:** ID da fatura.

➡️ **“payment_status”:** situação do pagamento — no exemplo, `Completed`.

➡️ **“paymentId”:** a identificação do pagamento no seu sistema.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/subscription/manualpaid',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "invoiceId": "28",
    "payment_status": "Completed",
    "paymentId": "IDENTIFICACAO_DO_PAGAMENTO_9031203120"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/subscription/manualpaid' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"invoiceId":"28","payment_status":"Completed","paymentId":"IDENTIFICACAO_DO_PAGAMENTO_9031203120"}'
```
