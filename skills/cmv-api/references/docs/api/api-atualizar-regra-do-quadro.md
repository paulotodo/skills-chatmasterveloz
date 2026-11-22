# API Atualizar Regra do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-regra-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Atualizar Regra do Quadro

---

🧩 Atualiza **uma regra do quadro**, pessoal ou da equipe, ou a desliga.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/regras/{regraId}?userId={userId}
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
    "nome": "Boleto para o Financeiro",
    "ativo": true,
    "condicoes": [
        {
            "tipo": "TEXTO",
            "palavras": [
                "boleto",
                "pix"
            ]
        }
    ]
}
```

➡️ **“regraId”:** ID da regra — vai no próprio endereço, no lugar de `{regraId}`. É o `id` que a regra traz nas listas de regras.

➡️ **“userId”:** na regra pessoal, o ID da dona da regra; outra pessoa, ou a chamada sem ele, não a encontra. Na regra da equipe, o de um administrador ou supervisor — ou tire o `userId` do endereço para fazer como a empresa.

➡️ **“nome”:** o nome novo.

➡️ **“ativo”:** `false` desliga a regra sem apagar; `true` religa.

➡️ **“condicoes”:** a lista inteira, que substitui a anterior — de 1 a 20, com os mesmos tipos da criação:

◽ `TEXTO` com `palavras`: a última mensagem do cliente contém uma das palavras. Maiúsculas e acentos não importam.

◽ `TEM_TAG` com `tagIds`: o atendimento tem uma das tags. `NAO_TEM_TAG` com `tagIds`: não tem nenhuma delas.

◽ `FILA` com `queueIds`: o atendimento está em um dos Setores.

◽ `CONTATO` com `contactIds`: é de um dos contatos.

◽ `CONEXAO` com `whatsappIds`: chegou por uma das Conexões.

◽ `CLIENTE_ESPERANDO` com `minutos`: a última mensagem é do cliente, e ninguém respondeu há esse tempo.

◽ `CLIENTE_SEM_RESPONDER` com `minutos`: a última mensagem é da equipe, e o cliente não respondeu há esse tempo.

◽ Os `minutos` vão de **10** a **43200** (30 dias).

⚠️ Em `TEXTO`, as palavras vão numa lista, em `palavras`. Texto corrido, como `"texto": "boleto, pix"`, é recusado.

◽ Mudam também o `colunaId`, a `combinacao` e, na regra da equipe, o `usuarioIds`.

◽ Mande só o que vai mudar. A resposta traz a regra como ficou.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras/{regraId}?userId={userId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Boleto para o Financeiro",
    "ativo": true,
    "condicoes": [
        {
            "tipo": "TEXTO",
            "palavras": [
                "boleto",
                "pix"
            ]
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/ticket-quadros/regras/{regraId}?userId={userId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Boleto para o Financeiro","ativo":true,"condicoes":[{"tipo":"TEXTO","palavras":["boleto","pix"]}]}'
```
