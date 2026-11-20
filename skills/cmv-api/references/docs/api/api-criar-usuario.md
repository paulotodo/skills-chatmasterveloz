# API Criar Usuário

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-usuario
- **Categoria:** APIs
- **Menu:** APIs › Equipe › API Criar Usuário

---

🧩 Cria **um usuário** na Equipe da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/users
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
    "name": "Ana",
    "email": "ana@empresa.com.br",
    "password": "segredo123",
    "profile": "user",
    "number": "5511911111111",
    "campoExtra1": "Matrícula 4521",
    "campoExtra2": "Unidade Centro",
    "inactive": false,
    "queueIds": [4, 5],
    "whatsappIds": [12],
    "whatsappId": 12,
    "carteiraQueueId": "4",
    "startWork": "08:00",
    "endWork": "18:00",
    "limiteDeAtendimentos": 5,
    "receiveNotifications": 2,
    "notifyGroups": true,
    "restricted": false,
    "restrictToQueues": false,
    "blockNumberView": false,
    "canAccessContacts": true,
    "canAccessCampaigns": false,
    "canCreateTags": false,
    "canAssignTags": true,
    "canRemoveTags": true,
    "canUseContactNotes": false,
    "canAuditSales": false,
    "canUseAnswerFromIA": true,
    "canViewContactSummary": false,
    "canUseRespostaNaVolta": false,
    "canForceHybrid": false
}
```

➡️ **“name”:** nome do usuário, com pelo menos 2 caracteres. **Obrigatório.**

➡️ **“email”:** o e-mail de login. **Único em todo o sistema**, e não só na sua empresa — um e-mail já usado por outra empresa é recusado. **Obrigatório.**

➡️ **“password”:** senha com pelo menos 5 caracteres. **Obrigatório.**

⚠️ **O exemplo acima traz tudo o que a criação aceita, para você escolher** — não é obrigatório enviar inteiro. Os campos que você não mandar nascem com o padrão da tela.

➡️ **“profile”:** o perfil — `user` (padrão), `admin` ou `supervisor`.

➡️ **“number”:** número de celular ou ramal do usuário.

➡️ **“campoExtra1” e “campoExtra2”:** dois campos de texto livre do usuário — matrícula, unidade, centro de custo —, para usar nas mensagens e no fluxo com `{{user_extra1}}` e `{{user_extra2}}`. Vazio apaga o valor.

➡️ **“inactive”:** `true` cria o usuário já inativo.

➡️ **“queueIds”:** IDs dos Setores do usuário.

➡️ **“whatsappIds”:** IDs das conexões que ele pode atender. Sem este campo, ele atende todas.

➡️ **“whatsappId”:** a conexão padrão do usuário.

⚠️ **O `whatsappId`, no singular, é a conexão padrão do usuário** — e não a conexão da chamada. Com o token da empresa, o mesmo campo serve para as duas coisas: para autenticar sem dar conexão padrão ao usuário, mande a conexão na query da URL e deixe o corpo sem ele.

➡️ **“carteiraQueueId”:** ID do Setor da carteira de clientes do usuário.

➡️ **“startWork” e “endWork”:** início e fim do expediente, em `HH:mm`. Padrão das 00:00 às 23:59.

➡️ **“limiteDeAtendimentos”:** máximo de atendimentos ao mesmo tempo. Vazio ou `0` deixa sem limite.

➡️ **“receiveNotifications”:** `2` todas as notificações, `1` só as de atendimento aberto, `0` nenhuma.

➡️ **“notifyGroups”:** `true` para ele receber notificação de grupos.

➡️ **“restricted”:** `true` deixa o acesso do usuário restrito.

➡️ **“restrictToQueues”:** `true` faz o supervisor enxergar apenas os próprios Setores.

➡️ **“blockNumberView”:** `true` mascara o número dos contatos para ele.

➡️ **Permissões:** `canAccessContacts`, `canAccessCampaigns`, `canCreateTags`, `canAssignTags`, `canRemoveTags`, `canUseContactNotes`, `canAuditSales`, `canUseAnswerFromIA`, `canViewContactSummary`, `canUseRespostaNaVolta` e `canForceHybrid`, cada uma `true` ou `false` — as mesmas caixas que a tela do usuário mostra.

◽ **O limite de usuários do plano vale aqui.** A API não passa por cima dele.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/users',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "name": "Ana",
    "email": "ana@empresa.com.br",
    "password": "segredo123",
    "profile": "user",
    "number": "5511911111111",
    "campoExtra1": "Matrícula 4521",
    "campoExtra2": "Unidade Centro",
    "inactive": false,
    "queueIds": [4, 5],
    "whatsappIds": [12],
    "whatsappId": 12,
    "carteiraQueueId": "4",
    "startWork": "08:00",
    "endWork": "18:00",
    "limiteDeAtendimentos": 5,
    "receiveNotifications": 2,
    "notifyGroups": true,
    "restricted": false,
    "restrictToQueues": false,
    "blockNumberView": false,
    "canAccessContacts": true,
    "canAccessCampaigns": false,
    "canCreateTags": false,
    "canAssignTags": true,
    "canRemoveTags": true,
    "canUseContactNotes": false,
    "canAuditSales": false,
    "canUseAnswerFromIA": true,
    "canViewContactSummary": false,
    "canUseRespostaNaVolta": false,
    "canForceHybrid": false
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
curl -X POST 'https://api2.chatmasterveloz.com/api/users' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"Ana","email":"ana@empresa.com.br","password":"segredo123","profile":"user","number":"5511911111111","campoExtra1":"Matrícula 4521","campoExtra2":"Unidade Centro","inactive":false,"queueIds":[4,5],"whatsappIds":[12],"whatsappId":12,"carteiraQueueId":"4","startWork":"08:00","endWork":"18:00","limiteDeAtendimentos":5,"receiveNotifications":2,"notifyGroups":true,"restricted":false,"restrictToQueues":false,"blockNumberView":false,"canAccessContacts":true,"canAccessCampaigns":false,"canCreateTags":false,"canAssignTags":true,"canRemoveTags":true,"canUseContactNotes":false,"canAuditSales":false,"canUseAnswerFromIA":true,"canViewContactSummary":false,"canUseRespostaNaVolta":false,"canForceHybrid":false}'
```
