# API Atualizar Coluna do Projeto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-coluna-do-projeto
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Atualizar Coluna do Projeto

---

🧩 Atualiza **uma coluna** do projeto: o nome, a posição no quadro ou se ela conclui as tarefas.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas/{etapaId}
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
    "nome": "Em homologação",
    "ordem": 2,
    "concluida": false
}
```

➡️ **“projetoId”** e **“etapaId”:** IDs do projeto e da coluna — vão no próprio endereço, no lugar de `{projetoId}` e `{etapaId}`. **Obrigatórios.**

◽ Coluna de outro projeto é recusada.

➡️ **“nome”:** novo nome da coluna.

➡️ **“ordem”:** posição da coluna no quadro, a partir de `0`.

◽ As outras colunas não mudam de posição: duas com o mesmo número ficam lado a lado. Para trocar duas de lugar, atualize as duas.

➡️ **“concluida”:** `true` para a coluna concluir as tarefas que caem nela.

⚠️ **Mudar o `concluida` vale também para as tarefas que já estão na coluna:** `true` conclui todas, e `false` reabre todas.

◽ Os campos que você não enviar ficam como estão.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas/{etapaId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Em homologação",
    "ordem": 2,
    "concluida": false
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token da Empresa
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X PUT 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas/{etapaId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Em homologação","ordem":2,"concluida":false}'
```
