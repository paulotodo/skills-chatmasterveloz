# API Validar Contato

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-validar-contato
- **Categoria:** APIs
- **Menu:** APIs › Contatos › API Validar Contato

---

🧩 Verifica **se um número é válido no WhatsApp**. Quando é, o número volta já formatado com a quantidade certa de dígitos — 8 ou 9.

**API:** Básica, Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/isValid
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

```javascript
{
    "number": "5511955892164"
}
```

⚠️ A validação só funciona com duas condições atendidas: no menu **Configurações  ›  Ignorar Validação de Contatos?** o valor precisa ser **Não**, e no menu **Conexões** precisa haver uma Conexão marcada como **Padrão**.

➡️ **“number”:** telefone do contato no formato ddi ddd numero (somente números).

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/isValid',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/isValid' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164"}'
```
