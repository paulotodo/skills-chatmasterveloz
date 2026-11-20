# API Atualizar Usuário

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-usuario
- **Categoria:** APIs
- **Menu:** APIs › Equipe › API Atualizar Usuário

---

🧩 Atualiza **um usuário da Equipe**, mudando apenas os campos que você enviar.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/users/{userId}
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
    "name": "Maria Souza",
    "email": "maria@empresa.com.br",
    "password": "segredo123",
    "profile": "user",
    "number": "5511911111111",
    "campoExtra1": "Matrícula 4521",
    "campoExtra2": "Unidade Centro",
    "inactive": false,
    "queueIds": [4, 7],
    "whatsappIds": [2, 5],
    "defaultWhatsappId": 2,
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
    "canCreateTags": true,
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

➡️ **“userId”:** ID do usuário — vai no próprio endereço, no lugar de `{userId}`. **Obrigatório.**

⚠️ **Só os campos enviados mudam.** Os Setores, as conexões e as permissões que não vierem ficam exatamente como estão — diferente da edição pela tela, que grava o formulário inteiro.

⚠️ **O exemplo acima traz tudo o que a chamada aceita, para você escolher** — não é obrigatório enviar inteiro. Copiado como está, ele altera todos esses campos de uma vez, **inclusive a senha**. Monte o seu payload só com o que você quer mudar.

➡️ **“name”:** nome do usuário, com pelo menos 2 caracteres.

➡️ **“email”:** e-mail de login. Precisa ser único em todo o sistema, e não só na sua empresa.

➡️ **“password”:** senha nova. Passa pela regra de senha forte quando a configuração global exige.

➡️ **“profile”:** perfil do usuário — `user`, `admin` ou `supervisor`.

➡️ **“number”:** número de celular ou ramal do usuário.

➡️ **“campoExtra1” e “campoExtra2”:** os dois campos de texto livre do usuário — matrícula, unidade, centro de custo —, usados nas mensagens e no fluxo com `{{user_extra1}}` e `{{user_extra2}}`. Mande `""` para apagar o valor.

➡️ **“inactive”:** `true` desativa o usuário — e apaga a presença dele.

➡️ **“queueIds”:** IDs dos Setores do usuário, em array. Mande `[]` para tirar todos.

➡️ **“whatsappIds”:** IDs das conexões que ele pode atender, em array. Mande `[]` para deixar sem restrição.

➡️ **“defaultWhatsappId”:** ID da conexão padrão do usuário. Mande `null` para tirar.

➡️ **“carteiraQueueId”:** ID do Setor da carteira de clientes do usuário.

➡️ **“startWork” e “endWork”:** início e fim do expediente, no formato `HH:mm`.

➡️ **“limiteDeAtendimentos”:** quantos atendimentos ao mesmo tempo. Vazio ou `0` deixa sem limite.

➡️ **“receiveNotifications”:** `2` todas as notificações, `1` só as de atendimento aberto, `0` nenhuma.

➡️ **“notifyGroups”:** `true` para ele receber notificação de grupos.

➡️ **“restricted”:** `true` deixa o acesso do usuário restrito.

➡️ **“restrictToQueues”:** `true` faz o supervisor enxergar apenas os próprios Setores.

➡️ **“blockNumberView”:** `true` mascara o número dos contatos para ele.

➡️ **Permissões:** `canAccessContacts`, `canAccessCampaigns`, `canCreateTags`, `canAssignTags`, `canRemoveTags`, `canUseContactNotes`, `canAuditSales`, `canUseAnswerFromIA`, `canViewContactSummary`, `canUseRespostaNaVolta` e `canForceHybrid`, cada uma `true` ou `false` — as mesmas caixas que a tela do usuário mostra.

◽ Os Setores e as conexões informados precisam ser da empresa do usuário.

◽ Campo fora desta lista não é gravado: ele volta na resposta, em `camposIgnorados`.

⚠️ **O usuário 1 é protegido:** ele não perde o perfil de administrador e não pode ser desativado por aqui.

◽ A tela de usuários da empresa é avisada na hora.

◽ Campo com valor inválido responde `400`, dizendo qual é. Usuário que não existe responde `404`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/users/{userId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "name": "Maria Souza",
    "email": "maria@empresa.com.br",
    "password": "segredo123",
    "profile": "user",
    "number": "5511911111111",
    "campoExtra1": "Matrícula 4521",
    "campoExtra2": "Unidade Centro",
    "inactive": false,
    "queueIds": [4, 7],
    "whatsappIds": [2, 5],
    "defaultWhatsappId": 2,
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
    "canCreateTags": true,
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/users/{userId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"Maria Souza","email":"maria@empresa.com.br","password":"segredo123","profile":"user","number":"5511911111111","campoExtra1":"Matrícula 4521","campoExtra2":"Unidade Centro","inactive":false,"queueIds":[4,7],"whatsappIds":[2,5],"defaultWhatsappId":2,"carteiraQueueId":"4","startWork":"08:00","endWork":"18:00","limiteDeAtendimentos":5,"receiveNotifications":2,"notifyGroups":true,"restricted":false,"restrictToQueues":false,"blockNumberView":false,"canAccessContacts":true,"canAccessCampaigns":false,"canCreateTags":true,"canAssignTags":true,"canRemoveTags":true,"canUseContactNotes":false,"canAuditSales":false,"canUseAnswerFromIA":true,"canViewContactSummary":false,"canUseRespostaNaVolta":false,"canForceHybrid":false}'
```
