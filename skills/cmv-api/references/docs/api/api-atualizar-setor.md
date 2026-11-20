# API Atualizar Setor

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-setor
- **Categoria:** APIs
- **Menu:** APIs › Setores › API Atualizar Setor

---

🧩 Atualiza os dados de **um Setor** — só o que vier no corpo muda.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/queues/update
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
    "queueId": 4,
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

➡️ **“queueId”:** ID do Setor a editar. **Obrigatório.**

⚠️ **O exemplo acima traz tudo o que a chamada aceita, para você escolher** — não é obrigatório enviar inteiro. Os campos que você não mandar **ficam como estão**.

⚠️ **Mande pelo menos um campo editável** além do `queueId`. Só com o id, a chamada é recusada.

➡️ **“name”:** nome do Setor. Pelo menos 2 caracteres, e único entre os Setores da empresa.

➡️ **“color”:** cor do Setor, em hexadecimal.

➡️ **“greetingMessage”:** mensagem de saudação do Setor.

➡️ **“outOfHoursMessage”:** mensagem enviada fora do horário de funcionamento.

➡️ **“msgEncerramento”:** mensagem enviada ao encerrar o atendimento no Setor.

➡️ **“invalidMessage”:** resposta quando o cliente escolhe uma opção que não existe no menu do chatbot.

➡️ **“schedules”:** o horário de funcionamento. **Substitui a lista inteira** — o que não vier sai.

➡️ **“isChatbot”:** `true` faz o Setor usar o menu de opções do chatbot.

➡️ **“prioridade”:** prioridade do Setor, de `0` para cima.

➡️ **“categoryId”:** ID da categoria do Setor.

➡️ **“gatilhos”:** palavras-chave que levam a conversa para este Setor, separadas por vírgula.

➡️ **“campoExtra1” e “campoExtra2”:** os dois campos de texto livre do Setor — centro de custo, unidade, ramal —, usados nas mensagens e no fluxo com `{{queue_extra1}}` e `{{queue_extra2}}`. Mande `""` para apagar o valor.

➡️ **“ativarRoteador”:** `true` liga o rodízio automático de operadores no Setor.

➡️ **“ativarRoteadorNoti”:** `true` avisa o operador quando o rodízio entrega um atendimento a ele.

➡️ **“tempoRoteador”:** tempo do rodízio, em minutos.

➡️ **“selectedMoveQueueId”:** ID do Setor para onde os atendimentos são movidos.

➡️ **“isNPS”:** `true` faz o Setor enviar a pesquisa de satisfação ao encerrar.

➡️ **“isTranscribe”:** `true` transcreve os áudios recebidos no Setor.

➡️ **“webhookQueueURL”:** URL avisada toda vez que um atendimento entra neste Setor.

➡️ **“templateGroupIds”:** IDs dos grupos de template do Setor. Ausente significa "não mexa"; uma lista vazia tira todos os grupos, e o Setor passa a mostrar todos os templates da conexão.

➡️ **“coverImage”:** ID do arquivo de imagem de capa. Mande `""` para tirar a capa.

◽ Campo fora da lista não é gravado e volta na resposta como ignorado. A resposta também diz o que foi de fato alterado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/queues/update',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "queueId": 4,
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
curl -X POST 'https://api2.chatmasterveloz.com/api/queues/update' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"queueId":4,"name":"Financeiro","color":"#4caf50","greetingMessage":"Você está no Financeiro.","outOfHoursMessage":"Voltamos às 8h.","msgEncerramento":"Atendimento encerrado. Obrigado!","invalidMessage":"Opção inválida. Tente de novo.","isChatbot":true,"prioridade":1,"ativarRoteador":true,"ativarRoteadorNoti":true,"tempoRoteador":5,"selectedMoveQueueId":12,"gatilhos":"boleto, fatura, pagamento","categoryId":3,"campoExtra1":"Centro de custo 12","campoExtra2":"Filial Centro","isNPS":true,"isTranscribe":false,"webhookQueueURL":"https://seusistema.com.br/entrou-no-setor","templateGroupIds":[],"coverImage":"","schedules":[{"weekday":"Segunda-feira","weekdayEn":"monday","startTime":"08:00","endTime":"18:00"}]}'
```
