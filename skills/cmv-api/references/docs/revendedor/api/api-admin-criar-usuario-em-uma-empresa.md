# API Criar Usuário em uma Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-criar-usuario-em-uma-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Equipe › API Criar Usuário em uma Empresa

---

🧩 Cria **um usuário na Equipe de uma empresa**, sem precisar entrar nela.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

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
    "companyId": 7,
    "name": "Ana Souza",
    "email": "ana@empresa.com.br",
    "password": "segredo123",
    "profile": "user",
    "number": "5511911111111",
    "campoExtra1": "Matrícula 4521",
    "campoExtra2": "Unidade Centro",
    "queueIds": [4, 5],
    "whatsappIds": [12],
    "whatsappId": 12,
    "startWork": "08:00",
    "endWork": "18:00",
    "limiteDeAtendimentos": 5,
    "carteiraQueueId": "4",
    "inactive": false,
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

➡️ **“companyId”:** ID da empresa em que o registro é criado. **É ele que faz a chamada valer para outra empresa** — sem ele, vale a empresa do próprio token.

➡️ **“name”:** nome do usuário, com pelo menos 2 caracteres. **Obrigatório.**

➡️ **“email”:** e-mail de login. Precisa ser único em **todo o sistema**, e não só naquela empresa. **Obrigatório.**

➡️ **“password”:** senha com pelo menos 5 caracteres. **Obrigatório.**

⚠️ **O exemplo traz tudo o que a criação aceita, para você escolher** — não é obrigatório enviar inteiro.

➡️ **“profile”:** perfil do usuário — `user` (padrão), `admin` ou `supervisor`.

➡️ **“number”:** número de celular ou ramal do usuário.

➡️ **“campoExtra1” e “campoExtra2”:** dois campos de texto livre do usuário — matrícula, unidade, centro de custo —, para usar nas mensagens e no fluxo com `{{user_extra1}}` e `{{user_extra2}}`. Vazio apaga o valor.

➡️ **“queueIds”:** IDs dos Setores do usuário. **“whatsappIds”:** as conexões que ele pode atender; sem o campo, atende todas. **“whatsappId”:** a conexão padrão dele.

➡️ **“startWork” e “endWork”:** início e fim do expediente, em `HH:mm`. **“limiteDeAtendimentos”:** quantos atendimentos ao mesmo tempo. **“carteiraQueueId”:** o Setor da carteira de clientes.

➡️ **“inactive”:** `true` cria o usuário já inativo.

➡️ **“receiveNotifications”:** `2` todas as notificações, `1` só as de atendimento aberto, `0` nenhuma. **“notifyGroups”:** se recebe notificação de grupos.

➡️ **“restricted”, “restrictToQueues” e “blockNumberView”:** acesso restrito, supervisor que só enxerga os próprios Setores, e máscara no número dos contatos.

➡️ **Permissões:** `canAccessContacts`, `canAccessCampaigns`, `canCreateTags`, `canAssignTags`, `canRemoveTags`, `canUseContactNotes`, `canAuditSales`, `canUseAnswerFromIA`, `canViewContactSummary`, `canUseRespostaNaVolta` e `canForceHybrid`, cada uma `true` ou `false`.

◽ Os Setores e as conexões precisam ser da **mesma empresa** do `companyId`.

⚠️ **O limite de usuários é o do plano daquela empresa.** A chamada não passa por cima dele.

◽ Empresa que não existe é recusada.

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
    "companyId": 7,
    "name": "Ana Souza",
    "email": "ana@empresa.com.br",
    "password": "segredo123",
    "profile": "user",
    "number": "5511911111111",
    "campoExtra1": "Matrícula 4521",
    "campoExtra2": "Unidade Centro",
    "queueIds": [4, 5],
    "whatsappIds": [12],
    "whatsappId": 12,
    "startWork": "08:00",
    "endWork": "18:00",
    "limiteDeAtendimentos": 5,
    "carteiraQueueId": "4",
    "inactive": false,
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
curl -X POST 'https://api2.chatmasterveloz.com/api/users' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"companyId":7,"name":"Ana Souza","email":"ana@empresa.com.br","password":"segredo123","profile":"user","number":"5511911111111","campoExtra1":"Matrícula 4521","campoExtra2":"Unidade Centro","queueIds":[4,5],"whatsappIds":[12],"whatsappId":12,"startWork":"08:00","endWork":"18:00","limiteDeAtendimentos":5,"carteiraQueueId":"4","inactive":false,"receiveNotifications":2,"notifyGroups":true,"restricted":false,"restrictToQueues":false,"blockNumberView":false,"canAccessContacts":true,"canAccessCampaigns":false,"canCreateTags":false,"canAssignTags":true,"canRemoveTags":true,"canUseContactNotes":false,"canAuditSales":false,"canUseAnswerFromIA":true,"canViewContactSummary":false,"canUseRespostaNaVolta":false,"canForceHybrid":false}'
```
