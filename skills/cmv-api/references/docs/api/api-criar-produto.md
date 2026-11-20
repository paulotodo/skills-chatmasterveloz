# API Criar Produto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-produto
- **Categoria:** APIs
- **Menu:** APIs › Produtos › API Criar Produto

---

🧩 Cria **um novo produto** no catálogo da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/products
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
  "name": "Consultoria Premium",
  "price": 1500.00,
  "description": "Consultoria personalizada para empresas",
  "details": "Inclui 10 horas mensais, relatórios detalhados e acompanhamento semanal.",
  "imageUrl": "https://meusite.com/imagens/consultoria.jpg"
}
```

➡️ **“name”:** nome do produto. **Obrigatório.**

➡️ **“price”:** preço em formato decimal, com os centavos depois do **ponto** — por exemplo, `1500.00`. **Obrigatório.**

➡️ **“description”:** descrição curta do produto.

➡️ **“details”:** detalhes completos ou especificações do produto.

➡️ **“imageUrl”:** endereço público da imagem do produto.

◽ Campos fora desta lista são descartados.

◽ O produto passa a aparecer nos seletores do painel: na oportunidade e na proposta do CRM, nas regras de encadeamento e nos comandos da IA.

◽ A chamada não envia nada a contato nenhum e não cria atendimento.

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
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
  "name": "Consultoria Premium",
  "price": 1500.00,
  "description": "Consultoria personalizada para empresas",
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
curl -X POST 'https://api2.chatmasterveloz.com/api/products' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"Consultoria Premium","price":1500,"description":"Consultoria personalizada para empresas","details":"Inclui 10 horas mensais, relatórios detalhados e acompanhamento semanal.","imageUrl":"https://meusite.com/imagens/consultoria.jpg"}'
```
