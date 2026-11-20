# API Obter uma Mensagem Template Meta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-uma-mensagem-template-meta
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Obter uma Mensagem Template Meta

---

🧩 Obter **um template específico** — é por aqui que se acompanha a aprovação da Meta.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/waba-templates/{id}
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
// sem payload — o id vai no endereço
```

➡️ **“id”:** o id **local** do template, que vai no próprio endereço, no lugar de `{id}`. **Obrigatório.**

◽ É o `id` que vem na resposta da criação e na lista de templates — não o `apiTemplateId`, que é o id do template na Meta.

⚠️ **Não consulte em laço curto.** A análise da Meta leva de minutos a horas: uma consulta a cada poucos minutos resolve, e de segundo em segundo só gasta requisição.

⚠️ Volta **404** quando o template não é da conexão da chamada — a dona do token, quando se usa o token da Conexão, ou a informada quando se usa o Token da Empresa —, inclusive quando ele existe, mas em outra conexão.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/waba-templates/{id}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/waba-templates/{id}' -H 'Authorization: Bearer {seutokenaqui}'
```
