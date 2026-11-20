# API Deletar Oportunidade

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-deletar-oportunidade
- **Categoria:** APIs
- **Menu:** APIs › CRM › API Deletar Oportunidade

---

🧩 Manda **uma oportunidade** do CRM para a lixeira.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}
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
// sem payload
```

➡️ **“oportunidadeId”:** ID da oportunidade — vai no próprio endereço, no lugar de `{oportunidadeId}`. **Obrigatório.**

⚠️ A oportunidade vai para **Excluídas**, com o histórico de eventos: some do quadro, das listas e das contagens. Dali ela pode ser restaurada ou excluída de vez pela tela, no menu **CRM  ›  Board**. Essas duas ações não têm rota na API. Na lista, ela aparece como *Excluída pela API*.

◽ Id que não existe e id de outra empresa respondem a mesma coisa: não encontrado. A chamada não confirma quais ids existem no sistema.

⚠️ **A empresa precisa estar com o CRM novo ativado.**

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/crm/v2/oportunidades/{oportunidadeId}' -H 'Authorization: Bearer {seutokenaqui}'
```
