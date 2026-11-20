# API Atualizar Conexão

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-conexao
- **Categoria:** APIs
- **Menu:** APIs › Conexões › API Atualizar Conexão

---

🧩 Atualiza os dados de **uma conexão** — só o que vier no corpo muda.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/whatsapp/update
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
    "whatsappId": 12,
    "name": "Comercial",
    "isDefault": false,
    "greetingMessage": "Olá! Em que podemos ajudar?",
    "complationMessage": "Atendimento concluído.",
    "outOfHoursMessage": "Estamos fora do horário. Voltamos às 8h.",
    "ratingMessage": "Como você avalia o atendimento?",
    "closeMessage": "Atendimento encerrado.",
    "newFollowerMessage": "Obrigado por seguir a gente!",
    "queueIds": [3, 16],
    "token": "meu-token-de-conexao",
    "webhook": "https://minha-automacao.com.br/hook",
    "webhookb": "https://minha-automacao.com.br/hook-2",
    "ignoreNumbers": "5511999999999, 5511888888888",
    "selectedMoveQueueId": 16,
    "selectedInterval": 30,
    "selectedCommentQueueId": 3,
    "inatividade": 60,
    "inatividadeNQ": 30,
    "markasread": 1,
    "importmessages": 0,
    "allowEcho": false,
    "blockgroupatconnection": false,
    "reopenAsNewTicket": false,
    "transferAsNewTicket": false,
    "respostaNaVoltaBot": "substitui",
    "bloquearForaDaJanela": false,
    "alternativeMode": false,
    "textoBotaoLink": "Abrir conversa",
    "mensagemBotaoLink": "Clique para falar com a gente:",
    "chatExternoAutenticado": false,
    "iframe": "https://seusistema.com.br/ficha-do-cliente",
    "expandDrawer": false,
    "iframeFirst": false,
    "excluded": 0,
    "excludedwpw": 0,
    "ixcrandom": 0,
    "telegram_token": "",
    "whavoip_token": "",
    "voipPrefix": "",
    "proxyAddress": "",
    "proxyUsername": "",
    "proxyPassword": "",
    "sipConfig": {},
    "coverImage": ""
}
```

➡️ **“whatsappId”:** ID da conexão a editar.

◽ Com o token de uma conexão, sem este campo, edita a **própria** conexão do token; com ele, dá para editar outra conexão **da mesma empresa**. Conexão de outra empresa é recusada.

⚠️ **O exemplo acima traz tudo o que a chamada aceita, para você escolher** — não é obrigatório enviar inteiro. Os campos que você não enviar ficam como estão.

➡️ **“name”:** nome da conexão, com pelo menos 2 caracteres.

➡️ **“isDefault”:** `true` torna esta a conexão padrão, e desmarca a anterior.

➡️ **“coverImage”:** ID do arquivo de capa. Vazio limpa.

➡️ **“greetingMessage”:** a saudação ao abrir o atendimento. É obrigatória quando a conexão tem 2 ou mais Setores.

➡️ **“complationMessage”, “outOfHoursMessage”, “ratingMessage” e “closeMessage”:** as mensagens de conclusão, de fora do horário, de avaliação e de encerramento.

➡️ **“newFollowerMessage”:** mensagem para quem passa a seguir o perfil, no canal de Instagram.

➡️ **“queueIds”:** IDs dos Setores da conexão. **Substitui a lista inteira** — o que não vier sai.

➡️ **“selectedMoveQueueId” e “selectedInterval”:** o Setor para onde o atendimento é movido e depois de quantos minutos.

➡️ **“selectedCommentQueueId”:** Setor que recebe os comentários do Instagram.

➡️ **“inatividade” e “inatividadeNQ”:** minutos de inatividade para encerrar o atendimento, com Setor e sem Setor.

➡️ **“token”:** o token de API da conexão. É único na instalação.

➡️ **“webhook” e “webhookb”:** os endereços do webhook principal e do secundário.

➡️ **“ignoreNumbers”:** números que a conexão ignora.

➡️ **“markasread”:** `1` marca como lida a mensagem recebida. **“importmessages”:** `1` importa as mensagens do aparelho.

➡️ **“allowEcho”:** `true` registra também as mensagens enviadas pelo próprio aparelho.

➡️ **“blockgroupatconnection”:** `true` ignora as mensagens de grupo.

➡️ **“reopenAsNewTicket”:** `true` faz a mensagem em atendimento fechado abrir um novo. **“transferAsNewTicket”:** `true` faz a transferência abrir um atendimento novo no destino.

➡️ **“respostaNaVoltaBot”:** o que o bot faz quando há Resposta na Volta guardada — `substitui` ou `antes`.

➡️ **“bloquearForaDaJanela”:** `true` barra a mensagem comum fora da janela de 24 horas, na API oficial.

➡️ **“alternativeMode”:** `true` liga o Modo Alternativo (chat externo por link). **“textoBotaoLink”** e **“mensagemBotaoLink”:** o rótulo do botão e o texto que acompanha o link. **“chatExternoAutenticado”:** `true` pede os 4 últimos dígitos do telefone.

➡️ **“iframe”:** endereço do painel do contato. **“expandDrawer”:** abre esse painel junto com o atendimento. **“iframeFirst”:** abre o painel já nessa aba.

➡️ **“excluded”:** `1` liga a opção CRM. **“excludedwpw”:** `1` liga o Pixel da Meta. **“ixcrandom”:** `1` usa a conexão para disparo IXC.

➡️ **“telegram_token”:** token do bot, no canal Telegram. Trocar o token limpa o erro permanente da conexão.

➡️ **“whavoip_token” e “voipPrefix”:** o token e o prefixo do VoIP. **“sipConfig”:** a configuração SIP.

➡️ **“proxyAddress”, “proxyUsername” e “proxyPassword”:** o proxy da sessão.

⚠️ **A senha do proxy e a configuração SIP não voltam na resposta** — depois de gravadas, só dá para substituí-las.

◽ Campo fora da lista não é gravado e volta na resposta como ignorado. A resposta também diz o que foi de fato alterado. Sem nenhum campo da lista, a chamada é recusada e a resposta traz os campos aceitos.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/whatsapp/update',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "whatsappId": 12,
    "name": "Comercial",
    "isDefault": false,
    "greetingMessage": "Olá! Em que podemos ajudar?",
    "complationMessage": "Atendimento concluído.",
    "outOfHoursMessage": "Estamos fora do horário. Voltamos às 8h.",
    "ratingMessage": "Como você avalia o atendimento?",
    "closeMessage": "Atendimento encerrado.",
    "newFollowerMessage": "Obrigado por seguir a gente!",
    "queueIds": [3, 16],
    "token": "meu-token-de-conexao",
    "webhook": "https://minha-automacao.com.br/hook",
    "webhookb": "https://minha-automacao.com.br/hook-2",
    "ignoreNumbers": "5511999999999, 5511888888888",
    "selectedMoveQueueId": 16,
    "selectedInterval": 30,
    "selectedCommentQueueId": 3,
    "inatividade": 60,
    "inatividadeNQ": 30,
    "markasread": 1,
    "importmessages": 0,
    "allowEcho": false,
    "blockgroupatconnection": false,
    "reopenAsNewTicket": false,
    "transferAsNewTicket": false,
    "respostaNaVoltaBot": "substitui",
    "bloquearForaDaJanela": false,
    "alternativeMode": false,
    "textoBotaoLink": "Abrir conversa",
    "mensagemBotaoLink": "Clique para falar com a gente:",
    "chatExternoAutenticado": false,
    "iframe": "https://seusistema.com.br/ficha-do-cliente",
    "expandDrawer": false,
    "iframeFirst": false,
    "excluded": 0,
    "excludedwpw": 0,
    "ixcrandom": 0,
    "telegram_token": "",
    "whavoip_token": "",
    "voipPrefix": "",
    "proxyAddress": "",
    "proxyUsername": "",
    "proxyPassword": "",
    "sipConfig": {},
    "coverImage": ""
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
curl -X POST 'https://api2.chatmasterveloz.com/api/whatsapp/update' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"whatsappId":12,"name":"Comercial","isDefault":false,"greetingMessage":"Olá! Em que podemos ajudar?","complationMessage":"Atendimento concluído.","outOfHoursMessage":"Estamos fora do horário. Voltamos às 8h.","ratingMessage":"Como você avalia o atendimento?","closeMessage":"Atendimento encerrado.","newFollowerMessage":"Obrigado por seguir a gente!","queueIds":[3,16],"token":"meu-token-de-conexao","webhook":"https://minha-automacao.com.br/hook","webhookb":"https://minha-automacao.com.br/hook-2","ignoreNumbers":"5511999999999, 5511888888888","selectedMoveQueueId":16,"selectedInterval":30,"selectedCommentQueueId":3,"inatividade":60,"inatividadeNQ":30,"markasread":1,"importmessages":0,"allowEcho":false,"blockgroupatconnection":false,"reopenAsNewTicket":false,"transferAsNewTicket":false,"respostaNaVoltaBot":"substitui","bloquearForaDaJanela":false,"alternativeMode":false,"textoBotaoLink":"Abrir conversa","mensagemBotaoLink":"Clique para falar com a gente:","chatExternoAutenticado":false,"iframe":"https://seusistema.com.br/ficha-do-cliente","expandDrawer":false,"iframeFirst":false,"excluded":0,"excludedwpw":0,"ixcrandom":0,"telegram_token":"","whavoip_token":"","voipPrefix":"","proxyAddress":"","proxyUsername":"","proxyPassword":"","sipConfig":[],"coverImage":""}'
```
