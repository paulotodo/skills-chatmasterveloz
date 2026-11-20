# API Obter um Projeto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-um-projeto
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Obter um Projeto

---

🧩 Obter **um projeto específico**, com as colunas, as tarefas e a equipe.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos/{projetoId}
```

##### Método

```
GET
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```
// sem payload — o projeto vai no endereço
```

➡️ **“projetoId”:** ID do projeto — vai no próprio endereço, no lugar de `{projetoId}`. **Obrigatório.**

◽ A resposta traz o contato, o responsável, as colunas, as tarefas com o checklist de cada uma, e a equipe.

◽ É daqui que saem os IDs das colunas (`etapaId`), das tarefas e dos itens do checklist usados nas outras chamadas do projeto.

◽ Projeto que não existe, ou de outra empresa, responde **não encontrado** (`404`).

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}' -H 'Authorization: Bearer {seutokenaqui}'
```
