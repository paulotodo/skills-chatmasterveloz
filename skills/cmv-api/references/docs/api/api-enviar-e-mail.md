# API Enviar E-mail

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-e-mail
- **Categoria:** APIs
- **Menu:** APIs › E-mail › API Enviar E-mail

---

🧩 Envia um **e-mail** por uma conta de e-mail da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/email/send
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
    "to": "cliente@exemplo.com",
    "subject": "Sua proposta",
    "text": "Olá! Segue a proposta que combinamos.",
    "cc": ["gerente@exemplo.com"],
    "bcc": ["diretoria@exemplo.com"],
    "accountId": 2
}
```

➡️ **“to”:** endereço de quem recebe. **Obrigatório.**

➡️ **“subject”:** o assunto. **Obrigatório.**

➡️ **“text”:** o e-mail em texto simples. Informe este ou o `html`.

➡️ **“html”:** o e-mail em HTML. Informe este ou o `text`.

➡️ **“cc”:** opcional. Lista de endereços em cópia.

➡️ **“bcc”:** opcional. Lista de endereços em cópia oculta.

➡️ **“accountId”:** opcional. A conta de e-mail que envia. Sem ele, vale a **primeira conta ativa** da empresa.

◽ A conta precisa ser da empresa do token e estar ativa.

◽ O e-mail é enviado com a assinatura da conta e fica guardado em **Enviadas**, como qualquer e-mail do painel.

⚠️ **Anexo não disponível.** Esta chamada envia só o texto do e-mail.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/email/send',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "to": "cliente@exemplo.com",
    "subject": "Sua proposta",
    "text": "Olá! Segue a proposta que combinamos.",
    "cc": ["gerente@exemplo.com"],
    "bcc": ["diretoria@exemplo.com"],
    "accountId": 2
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
curl -X POST 'https://api2.chatmasterveloz.com/api/email/send' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"to":"cliente@exemplo.com","subject":"Sua proposta","text":"Olá! Segue a proposta que combinamos.","cc":["gerente@exemplo.com"],"bcc":["diretoria@exemplo.com"],"accountId":2}'
```
