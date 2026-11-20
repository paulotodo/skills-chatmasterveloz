# API Janela de Atendimento pelo Número

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-janela-de-atendimento-pelo-numero
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Janela de Atendimento pelo Número

---

🧩 Obter a **janela de atendimento** do atendimento mais recente de um número.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/janela?number=5511955892164
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
// sem payload — o número vai na própria URL
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números). **Obrigatório.**

◽ Responde pelo atendimento **mais recente** desse contato na conexão do token.

◽ A resposta diz se a janela está **aberta**, quanto tempo falta para ela fechar e se o envio exige mensagem de template.

◽ A regra muda por canal: na API oficial são 24 horas contadas da última mensagem **do cliente**; no Messenger e no Instagram são 24 horas livres e mais alguns dias só com atendimento humano; nos demais canais não existe janela, e a resposta vem sempre aberta.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/janela?number=5511955892164',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/janela?number=5511955892164' -H 'Authorization: Bearer {seutokenaqui}'
```
