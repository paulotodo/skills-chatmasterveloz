# API Criar Setor

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-setor
- **Categoria:** APIs
- **Menu:** APIs › Setores › API Criar Setor

---

🧩 Cria **um Setor** na empresa, com as mesmas regras do cadastro pela tela.

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

➡️ **“name”:** nome do Setor, com pelo menos 2 caracteres e único na empresa. **Obrigatório.**

➡️ **“color”:** cor do Setor, em hexadecimal. **Obrigatório.**

⚠️ **O exemplo acima traz tudo o que a criação aceita, para você escolher** — não é obrigatório enviar inteiro. Só o `name` e a `color` são exigidos; o resto que você não mandar nasce com o padrão da tela.

➡️ **“greetingMessage”:** mensagem de saudação, enviada a quem entra no Setor.

➡️ **“outOfHoursMessage”:** mensagem enviada fora do horário de atendimento.

➡️ **“msgEncerramento”:** mensagem enviada ao encerrar o atendimento no Setor.

➡️ **“invalidMessage”:** resposta quando o cliente escolhe uma opção que não existe no menu do chatbot.

➡️ **“schedules”:** os horários de atendimento, um item por dia da semana, com `weekday`, `weekdayEn`, `startTime` e `endTime`.

➡️ **“isChatbot”:** `true` faz o Setor usar o menu de opções do chatbot.

➡️ **“prioridade”:** prioridade do Setor, de `0` para cima. Sem ela, `0`.

➡️ **“categoryId”:** ID da categoria do Setor.

➡️ **“gatilhos”:** palavras-chave que levam a conversa para este Setor, separadas por vírgula.

➡️ **“campoExtra1” e “campoExtra2”:** dois campos de texto livre do Setor — centro de custo, unidade, ramal —, para usar nas mensagens e no fluxo com `{{queue_extra1}}` e `{{queue_extra2}}`. Vazio apaga o valor.

➡️ **“ativarRoteador”:** `true` liga o rodízio automático de operadores no Setor.

➡️ **“ativarRoteadorNoti”:** `true` avisa o operador quando o rodízio entrega um atendimento a ele.

➡️ **“tempoRoteador”:** tempo do rodízio, em minutos.

➡️ **“selectedMoveQueueId”:** ID do Setor para onde os atendimentos são movidos.

➡️ **“isNPS”:** `true` faz o Setor enviar a pesquisa de satisfação ao encerrar.

➡️ **“isTranscribe”:** `true` transcreve os áudios recebidos no Setor.

➡️ **“webhookQueueURL”:** URL avisada toda vez que um atendimento entra neste Setor.

➡️ **“templateGroupIds”:** IDs dos grupos de template do Setor, em array. Com `[]`, o Setor mostra todos os templates da conexão.

➡️ **“coverImage”:** ID do arquivo de imagem de capa. Mande `""` para deixar sem capa.

◽ O `selectedMoveQueueId` precisa ser um Setor da mesma empresa.

◽ Campo fora desta lista não é gravado: ele volta na resposta, em `camposIgnorados`.

⚠️ **O plano limita quantos Setores a empresa pode ter.** Ao chegar no teto, a chamada é recusada dizendo o número máximo, e nada é criado.

◽ Nome repetido na mesma empresa também é recusado.

◽ A tela de Setores da empresa é avisada na hora.

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
curl -X POST 'https://api2.chatmasterveloz.com/api/queues' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"Financeiro","color":"#4caf50","greetingMessage":"Você está no Financeiro.","outOfHoursMessage":"Voltamos às 8h.","msgEncerramento":"Atendimento encerrado. Obrigado!","invalidMessage":"Opção inválida. Tente de novo.","isChatbot":true,"prioridade":1,"ativarRoteador":true,"ativarRoteadorNoti":true,"tempoRoteador":5,"selectedMoveQueueId":12,"gatilhos":"boleto, fatura, pagamento","categoryId":3,"campoExtra1":"Centro de custo 12","campoExtra2":"Filial Centro","isNPS":true,"isTranscribe":false,"webhookQueueURL":"https://seusistema.com.br/entrou-no-setor","templateGroupIds":[],"coverImage":"","schedules":[{"weekday":"Segunda-feira","weekdayEn":"monday","startTime":"08:00","endTime":"18:00"}]}'
```
