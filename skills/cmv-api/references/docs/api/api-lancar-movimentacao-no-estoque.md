# API Lançar Movimentação no Estoque

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-lancar-movimentacao-no-estoque
- **Categoria:** APIs
- **Menu:** APIs › Produtos › API Lançar Movimentação no Estoque

---

🧩 Lança **uma entrada, uma saída ou um ajuste** no estoque de um produto, como a janela **Estoque** da tela.

⚠️ Esta chamada é exclusiva do **PDV**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/products/{produtoId}/estoque
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
    "tipo": "entrada",
    "quantidade": 10,
    "motivo": "Chegou mercadoria",
    "userId": 16
}
```

➡️ **“produtoId”:** ID do produto — vai no próprio endereço, no lugar de `{produtoId}`.

➡️ **“tipo”:** `entrada` soma, `saida` tira, e `ajuste` informa o saldo contado — o movimento é a diferença. **Obrigatório.**

➡️ **“quantidade”:** até 3 casas decimais, com ponto. No ajuste, é o saldo contado, e zero vale. **Obrigatório.**

◽ A saída que deixaria o saldo negativo é recusada.

➡️ **“motivo”:** opcional. O porquê, com até 500 caracteres.

➡️ **“userId”:** opcional. Quem lança — o ID de um usuário da empresa. O lançamento leva o autor.

◽ Para mexer numa variação, informe `variacaoId`. No produto com variação ativa, ele é obrigatório.

◽ O produto precisa estar com o controle de estoque ligado; sem isso, a chamada é recusada.

◽ O webhook do PDV recebe o movimento, como no lançamento pela tela, e também o aviso de estoque baixo quando o saldo chega ao mínimo.

◽ A resposta traz o `movimento` (tipo, quantidade, saldo antes e depois, motivo e autor) e o `produto`, com o saldo novo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/products/{produtoId}/estoque',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "tipo": "entrada",
    "quantidade": 10,
    "motivo": "Chegou mercadoria",
    "userId": 16
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
curl -X POST 'https://api2.chatmasterveloz.com/api/products/{produtoId}/estoque' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"tipo":"entrada","quantidade":10,"motivo":"Chegou mercadoria","userId":16}'
```
