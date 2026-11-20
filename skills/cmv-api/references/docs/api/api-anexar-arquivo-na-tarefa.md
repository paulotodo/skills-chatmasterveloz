# API Anexar Arquivo na Tarefa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-anexar-arquivo-na-tarefa
- **Categoria:** APIs
- **Menu:** APIs › Tarefas › API Anexar Arquivo na Tarefa

---

🧩 Anexa **um arquivo do seu computador** a uma tarefa, em nome de uma pessoa da equipe.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/attachments?userId={userId}
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

```php
array(
    'files' => new CURLFile('/caminho/proposta.pdf', 'application/pdf')
  )
```

➡️ **“tarefaId”:** ID da tarefa — vai no próprio endereço, no lugar de `{tarefaId}`.

➡️ **“userId”:** quem anexa — o ID de um usuário da empresa. **Obrigatório**, e sempre **no endereço**: no envio de arquivo, o `userId` no payload não vale.

➡️ **“files”:** o arquivo. **Obrigatório.**

⚠️ O campo se chama `files`, sem número nem colchetes. `files[0]`, `files[]` ou outro nome, como `file`, são recusados com erro.

◽ Informe o **tipo** do arquivo — o segundo valor do `CURLFile`, como `application/pdf` ou `image/png`. É o tipo que fica gravado no anexo.

◽ Para mais de um arquivo, faça uma chamada por arquivo. Ferramenta que repete o campo `files` na mesma chamada, como o cURL de linha de comando com `-F` duas vezes, também funciona: cada arquivo vira um anexo.

◽ A resposta traz os anexos criados, cada um com `id`, `nomeOriginal`, `url`, `mimeType` e `tamanho`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tasks/{tarefaId}/attachments?userId={userId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => array(
    'files' => new CURLFile('/caminho/proposta.pdf', 'application/pdf')
  ),
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
