# API Deletar Coluna do Projeto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-coluna-do-projeto
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Deletar Coluna do Projeto

---

🧩 Apaga **uma coluna** do quadro de um projeto.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas/{etapaId}
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

```
// sem payload — o projeto e a coluna vão no endereço
```

➡️ **“projetoId”** e **“etapaId”:** IDs do projeto e da coluna — vão no próprio endereço, no lugar de `{projetoId}` e `{etapaId}`. **Obrigatórios.**

◽ As tarefas da coluna vão para a primeira coluna que sobra no quadro.

⚠️ **A última coluna do projeto não pode ser apagada** — a chamada é recusada.

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
  CURLOPT_CUSTOMREQUEST => 'DELETE',
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas/{etapaId}' -H 'Authorization: Bearer {seutokenaqui}'
```
