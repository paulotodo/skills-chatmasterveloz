# API Criar Regra da Equipe do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-regra-da-equipe-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de Atendimentos › API Criar Regra da Equipe do Quadro

---

🧩 Cria **uma regra da equipe** num quadro, que vale para quem usa o quadro e roda antes das regras de cada pessoa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras
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
    "nome": "Esperando há 1 hora",
    "colunaId": 15,
    "combinacao": "TODAS",
    "condicoes": [
        {
            "tipo": "CLIENTE_ESPERANDO",
            "minutos": 60
        }
    ],
    "usuarioIds": [
        8,
        17
    ]
}
```

➡️ **“quadroId”:** ID do quadro — vai no próprio endereço, no lugar de `{quadroId}`.

➡️ **“nome”:** o nome da regra. **Obrigatório.**

➡️ **“colunaId”:** a coluna para onde a regra leva o card — sempre uma **Coluna de atendimento**. A coluna **Pendentes** e as colunas de fila são recusadas.

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

➡️ **“usuarioIds”:** opcional. Só para estas pessoas. Sem ele, ou com `null`, a regra vale para todos que usam o quadro.

◽ Lista vazia é recusada.

◽ A regra da equipe só age nos atendimentos de quem tem o quadro atribuído.

◽ A regra nasce ligada, no fim da lista da equipe.

◽ Regra da equipe é do administrador e do supervisor. Sem `userId`, quem cria é a empresa; para criar em nome de uma pessoa, acrescente `?userId=` com o ID dela ao endereço — o de um atendente é recusado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Esperando há 1 hora",
    "colunaId": 15,
    "combinacao": "TODAS",
    "condicoes": [
        {
            "tipo": "CLIENTE_ESPERANDO",
            "minutos": 60
        }
    ],
    "usuarioIds": [
        8,
        17
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
curl -X POST 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Esperando há 1 hora","colunaId":15,"combinacao":"TODAS","condicoes":[{"tipo":"CLIENTE_ESPERANDO","minutos":60}],"usuarioIds":[8,17]}'
```
