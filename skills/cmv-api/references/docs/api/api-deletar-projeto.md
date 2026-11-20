# API Deletar Projeto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-projeto
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Deletar Projeto

---

🧩 Apaga **um projeto** e as colunas dele.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos/{projetoId}
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
// sem payload — o projeto vai no endereço
```

➡️ **“projetoId”:** ID do projeto — vai no próprio endereço, no lugar de `{projetoId}`. **Obrigatório.**

⚠️ **Não há como desfazer.**

◽ As tarefas do projeto **não** são apagadas: voltam a ser tarefas avulsas, com o responsável e o prazo que tinham.

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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}' -H 'Authorization: Bearer {seutokenaqui}'
```
