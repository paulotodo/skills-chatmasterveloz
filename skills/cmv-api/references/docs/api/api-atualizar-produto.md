# API Atualizar Produto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-produto
- **Categoria:** APIs
- **Menu:** APIs › Produtos › API Atualizar Produto

---

🧩 Atualiza os dados de **um produto existente** no catálogo — só o que vier no corpo muda.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/products
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
  "id": 9,
  "name": "Consultoria Premium",
  "price": 1800.00,
  "description": "Consultoria personalizada para empresas - versão 2026",
  "details": "Inclui 10 horas mensais, relatórios detalhados e acompanhamento semanal.",
  "imageUrl": "https://meusite.com/imagens/consultoria.jpg"
}
```

➡️ **“id”:** ID do produto a ser atualizado. **Obrigatório.**

➡️ **“name”:** novo nome do produto.

➡️ **“price”:** novo preço em formato decimal, com os centavos depois do **ponto** — por exemplo, `1800.00`.

➡️ **“description”:** nova descrição curta do produto.

➡️ **“details”:** novos detalhes ou especificações do produto.

➡️ **“imageUrl”:** novo endereço público da imagem do produto.

◽ Os campos que você não enviar ficam como estão.

◽ Mudar o preço vale para as propostas feitas dali em diante. As que já foram emitidas **não** são recalculadas.

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
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
  "id": 9,
  "name": "Consultoria Premium",
  "price": 1800.00,
  "description": "Consultoria personalizada para empresas - versão 2026",
  "details": "Inclui 10 horas mensais, relatórios detalhados e acompanhamento semanal.",
  "imageUrl": "https://meusite.com/imagens/consultoria.jpg"
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/products' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"id":9,"name":"Consultoria Premium","price":1800,"description":"Consultoria personalizada para empresas - versão 2026","details":"Inclui 10 horas mensais, relatórios detalhados e acompanhamento semanal.","imageUrl":"https://meusite.com/imagens/consultoria.jpg"}'
```
