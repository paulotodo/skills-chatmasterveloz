# API Deletar Produto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-produto
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Deletar Produto

---

🧩 Apaga **um produto** do catálogo permanentemente.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/products
```

##### Método

```
DELETE
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
  "id": 31
}
```

➡️ **“id”:** ID do produto a ser removido. **Obrigatório.**

⚠️ **Não há como desfazer.** A exclusão é permanente e não existe lixeira.

◽ As oportunidades e as propostas que já usam o produto continuam como estão.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/products',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
  CURLOPT_POSTFIELDS =>'{
  "id": 31
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/products' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"id":31}'
```
