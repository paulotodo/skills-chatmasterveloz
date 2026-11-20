# API Criar Resposta Rápida

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-resposta-rapida
- **Categoria:** APIs
- **Menu:** APIs › Respostas Rápidas › API Criar Resposta Rápida

---

🧩 Cria **uma resposta rápida** no cadastro da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/quick-messages
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
    "shortcode": "prazo",
    "message": "O prazo de entrega é de 3 dias úteis.",
    "categoria": "Entrega",
    "geral": true,
    "flowId": 0
}
```

➡️ **“shortcode”:** o atalho que o operador digita, com pelo menos 3 caracteres. **Obrigatório.**

➡️ **“message”:** o texto da resposta, com pelo menos 3 caracteres. **Obrigatório.**

⚠️ **O exemplo acima cria uma resposta do tipo geral.** Os outros dois tipos trocam o `geral` pelo `queueId` ou pelo `userId` — os três campos **não andam juntos**, e mandar `geral` com `queueId` é recusado.

➡️ **“categoria”:** categoria livre, que organiza a lista na tela.

➡️ **São três tipos, e eles saem da combinação de `geral`, `queueId` e `userId`:**

◽ **Geral** — `"geral": true`. A empresa inteira enxerga. É o que vale quando não vêm nem `queueId` nem `userId`.

◽ **De Setor** — informe o `queueId`. A resposta aparece nos atendimentos daquele Setor. Mandar `geral` junto do `queueId` é recusado.

◽ **Individual** — informe o `userId`, sem Setor e com `"geral": false`. Só aquele operador enxerga. Sem o `userId` a chamada é recusada, porque não há a quem mostrar.

➡️ **“flowId”:** ID de um fluxo disparado pela resposta.

◽ Com o `flowId`, o texto da resposta passa a ser o próprio atalho entre colchetes, como acontece na tela.

◽ O Setor, o operador e o fluxo informados precisam ser da mesma empresa.

⚠️ **Mídia não entra por aqui.** Na tela a resposta rápida aceita arquivo, e isso é upload; esta chamada grava só texto.

◽ Campo fora desta lista não é gravado: ele volta na resposta, em `camposIgnorados`.

◽ A tela de respostas rápidas da empresa é avisada na hora.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/quick-messages',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "shortcode": "prazo",
    "message": "O prazo de entrega é de 3 dias úteis.",
    "categoria": "Entrega",
    "geral": true,
    "flowId": 0
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
curl -X POST 'https://api2.chatmasterveloz.com/api/quick-messages' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"shortcode":"prazo","message":"O prazo de entrega é de 3 dias úteis.","categoria":"Entrega","geral":true,"flowId":0}'
```
