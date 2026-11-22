# API Criar Regra Pessoal do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-regra-pessoal-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Criar Regra Pessoal do Quadro

---

🧩 Cria **uma regra pessoal** do quadro, que leva o card de um atendimento para uma coluna quando ele combina com as condições.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/regras?userId={userId}
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
    "nome": "Boleto para o Financeiro",
    "colunaId": 11,
    "combinacao": "TODAS",
    "condicoes": [
        {
            "tipo": "TEXTO",
            "palavras": [
                "boleto",
                "segunda via"
            ]
        },
        {
            "tipo": "CLIENTE_ESPERANDO",
            "minutos": 30
        }
    ]
}
```

➡️ **“userId”:** a dona da regra — o ID de um usuário da empresa, no próprio endereço. **Obrigatório.** A regra age nos atendimentos dessa pessoa.

➡️ **“nome”:** o nome da regra. **Obrigatório.**

➡️ **“colunaId”:** a coluna para onde a regra leva o card — sempre uma **Coluna de atendimento**. A coluna **Pendentes** e as colunas de fila são recusadas.

◽ O quadro é o da coluna.

➡️ **“combinacao”:** `TODAS` move quando todas as condições valem; `QUALQUER`, quando basta uma. Sem ela, vale `TODAS`.

➡️ **“condicoes”:** de 1 a 20 condições, cada uma com o `tipo` e o valor dele:

◽ `TEXTO` com `palavras`: a última mensagem do cliente contém uma das palavras. Maiúsculas e acentos não importam.

◽ `TEM_TAG` com `tagIds`: o atendimento tem uma das tags. `NAO_TEM_TAG` com `tagIds`: não tem nenhuma delas.

◽ `FILA` com `queueIds`: o atendimento está em um dos Setores.

◽ `CONTATO` com `contactIds`: é de um dos contatos.

◽ `CONEXAO` com `whatsappIds`: chegou por uma das Conexões.

◽ `CLIENTE_ESPERANDO` com `minutos`: a última mensagem é do cliente, e ninguém respondeu há esse tempo.

◽ `CLIENTE_SEM_RESPONDER` com `minutos`: a última mensagem é da equipe, e o cliente não respondeu há esse tempo.

◽ Os `minutos` vão de **10** a **43200** (30 dias).

⚠️ Em `TEXTO`, as palavras vão numa lista, em `palavras`. Texto corrido, como `"texto": "boleto, pix"`, é recusado.

◽ A regra nasce ligada, no fim da lista da pessoa. Ela age quando o cliente manda mensagem, quando uma tag entra ou sai, a cada minuto nas condições de tempo e quando as regras são executadas.

◽ Vale a primeira regra que combinar, e as regras da equipe vêm antes das pessoais. Cada regra age uma vez por atendimento.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras?userId={userId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Boleto para o Financeiro",
    "colunaId": 11,
    "combinacao": "TODAS",
    "condicoes": [
        {
            "tipo": "TEXTO",
            "palavras": [
                "boleto",
                "segunda via"
            ]
        },
        {
            "tipo": "CLIENTE_ESPERANDO",
            "minutos": 30
        }
    ]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras?userId={userId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Boleto para o Financeiro","colunaId":11,"combinacao":"TODAS","condicoes":[{"tipo":"TEXTO","palavras":["boleto","segunda via"]},{"tipo":"CLIENTE_ESPERANDO","minutos":30}]}'
```
