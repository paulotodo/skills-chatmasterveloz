# API Atualizar o Status de um Usuário

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-o-status-de-um-usuario
- **Categoria:** APIs
- **Menu:** APIs › Equipe › API Atualizar o Status de um Usuário

---

🧩 Atualiza o **status de presença** de um usuário da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/users/{userId}/status
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
    "status": "away"
}
```

➡️ **“userId”:** o ID ou o e-mail do usuário — vai no próprio endereço, no lugar de `{userId}`. **Obrigatório.**

➡️ **“status”:** `online`, `away` ou `offline`. **Obrigatório.**

◽ Em `away` (Ausente) a pessoa sai dos rodízios — tanto o do fluxo quanto o do Setor.

⚠️ **Mudar o status não desconecta ninguém.** A pessoa continua no painel, e a bolinha no topo da tela dela muda na hora, avisando que a mudança veio da API. Para tirar alguém do painel, a chamada é outra: a que derruba a sessão.

◽ O webhook de status da empresa é avisado, igual a quando a própria pessoa muda o status.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/users/{userId}/status',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "status": "away"
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/users/{userId}/status' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"status":"away"}'
```
