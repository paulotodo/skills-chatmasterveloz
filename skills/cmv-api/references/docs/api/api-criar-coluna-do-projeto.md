# API Criar Coluna do Projeto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-coluna-do-projeto
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Criar Coluna do Projeto

---

🧩 Cria **uma coluna** no quadro de um projeto.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas
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
    "nome": "Homologação",
    "concluida": false
}
```

➡️ **“projetoId”:** ID do projeto — vai no próprio endereço, no lugar de `{projetoId}`. **Obrigatório.**

➡️ **“nome”:** nome da coluna. **Obrigatório.**

➡️ **“concluida”:** `true` para a coluna que conclui — a tarefa que cai nela fica concluída.

◽ A coluna entra no fim do quadro.

◽ A resposta traz o **id** da coluna, o `etapaId` das outras chamadas.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Homologação",
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
curl -X POST 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}/etapas' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Homologação","concluida":false}'
```
