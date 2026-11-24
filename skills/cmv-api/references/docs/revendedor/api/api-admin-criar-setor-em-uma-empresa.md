# API Criar Setor em uma Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-criar-setor-em-uma-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Setores › API Criar Setor em uma Empresa

---

🧩 Cria **um Setor dentro de uma empresa**, sem precisar entrar nela.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/queues
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
    "name": "Financeiro",
    "color": "#4caf50",
    "greetingMessage": "Você está no Financeiro.",
    "outOfHoursMessage": "Voltamos às 8h.",
    "msgEncerramento": "Atendimento encerrado. Obrigado!",
    "invalidMessage": "Opção inválida. Tente de novo.",
    "isChatbot": true,
    "prioridade": 1,
    "ativarRoteador": true,
    "ativarRoteadorNoti": true,
    "tempoRoteador": 5,
    "selectedMoveQueueId": 12,
    "gatilhos": "boleto, fatura, pagamento",
    "categoryId": 3,
    "campoExtra1": "Centro de custo 12",
    "campoExtra2": "Filial Centro",
    "isNPS": true,
    "isTranscribe": false,
    "webhookQueueURL": "https://seusistema.com.br/entrou-no-setor",
    "templateGroupIds": [],
    "coverImage": "",
    "schedules": [
        {
            "weekday": "Segunda-feira",
            "weekdayEn": "monday",
            "startTime": "08:00",
            "endTime": "18:00"
        }
    ]
}
```

➡️ **“companyId”:** ID da empresa em que o registro é criado. **É ele que faz a chamada valer para outra empresa** — sem ele, vale a empresa do próprio token.

➡️ **“name”:** nome do Setor, com pelo menos 2 caracteres e único naquela empresa. **Obrigatório.**

➡️ **“color”:** cor do Setor, em hexadecimal. **Obrigatório.**

⚠️ **O exemplo traz tudo o que a criação aceita, para você escolher** — não é obrigatório enviar inteiro.

➡️ **“greetingMessage”, “outOfHoursMessage”, “msgEncerramento” e “invalidMessage”:** as mensagens do Setor — saudação, fora do horário, encerramento e opção inválida no menu do chatbot.

➡️ **“schedules”:** os horários de atendimento, um item por dia da semana, com `weekday`, `weekdayEn`, `startTime` e `endTime`.

➡️ **“isChatbot”, “prioridade”, “categoryId” e “gatilhos”:** uso do menu de opções, ordem do Setor, categoria e as palavras-chave que levam a conversa até ele.

➡️ **“campoExtra1” e “campoExtra2”:** dois campos de texto livre do Setor — centro de custo, unidade, ramal —, para usar nas mensagens e no fluxo com `{{queue_extra1}}` e `{{queue_extra2}}`. Vazio apaga o valor.

➡️ **“ativarRoteador”, “ativarRoteadorNoti”, “tempoRoteador” e “selectedMoveQueueId”:** o rodízio de operadores, o aviso ao operador, o tempo em minutos e o Setor para onde os atendimentos são movidos.

➡️ **“isNPS”, “isTranscribe”, “webhookQueueURL”, “templateGroupIds” e “coverImage”:** pesquisa de satisfação ao encerrar, transcrição dos áudios, URL avisada quando um atendimento entra no Setor, grupos de template e imagem de capa.

◽ O `selectedMoveQueueId` e os grupos de template precisam ser da **mesma empresa** do `companyId`.

⚠️ **O limite de Setores é o do plano daquela empresa.** No teto, a chamada é recusada e nada é criado.

◽ Empresa que não existe é recusada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/queues',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "companyId": 7,
    "name": "Financeiro",
    "color": "#4caf50",
    "greetingMessage": "Você está no Financeiro.",
    "outOfHoursMessage": "Voltamos às 8h.",
    "msgEncerramento": "Atendimento encerrado. Obrigado!",
    "invalidMessage": "Opção inválida. Tente de novo.",
    "isChatbot": true,
    "prioridade": 1,
    "ativarRoteador": true,
    "ativarRoteadorNoti": true,
    "tempoRoteador": 5,
    "selectedMoveQueueId": 12,
    "gatilhos": "boleto, fatura, pagamento",
    "categoryId": 3,
    "campoExtra1": "Centro de custo 12",
    "campoExtra2": "Filial Centro",
    "isNPS": true,
    "isTranscribe": false,
    "webhookQueueURL": "https://seusistema.com.br/entrou-no-setor",
    "templateGroupIds": [],
    "coverImage": "",
    "schedules": [
        {
            "weekday": "Segunda-feira",
            "weekdayEn": "monday",
            "startTime": "08:00",
            "endTime": "18:00"
        }
    ]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/queues' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"companyId":7,"name":"Financeiro","color":"#4caf50","greetingMessage":"Você está no Financeiro.","outOfHoursMessage":"Voltamos às 8h.","msgEncerramento":"Atendimento encerrado. Obrigado!","invalidMessage":"Opção inválida. Tente de novo.","isChatbot":true,"prioridade":1,"ativarRoteador":true,"ativarRoteadorNoti":true,"tempoRoteador":5,"selectedMoveQueueId":12,"gatilhos":"boleto, fatura, pagamento","categoryId":3,"campoExtra1":"Centro de custo 12","campoExtra2":"Filial Centro","isNPS":true,"isTranscribe":false,"webhookQueueURL":"https://seusistema.com.br/entrou-no-setor","templateGroupIds":[],"coverImage":"","schedules":[{"weekday":"Segunda-feira","weekdayEn":"monday","startTime":"08:00","endTime":"18:00"}]}'
```
