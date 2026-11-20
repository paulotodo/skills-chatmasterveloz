# API Botão Copia e Cola

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-botao-copia-e-cola-pro
- **Categoria:** APIs
- **Menu:** APIs › Botões › API Botão Copia e Cola

---

🧩 Envia uma mensagem com **botões que copiam um código** ao serem tocados.

**API:** Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendButtonsPRO
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
    "openTicket": 0,
    "queueId": 0,
    "body": [
      {
        "phone": "5511955892164",
        "title": "Seu cupom exclusivo",
        "body": "Escolha um cupom conforme seu pedido",
        "footer": "Oferta válida até hoje",
        "buttons": [
            {
            "type": "copy",
            "text": "10% em compras até R$ 100",
            "code": "CUPOM10"
            },
            {
            "type": "copy",
            "text": "20% em compras até R$ 200",
            "code": "CUPOM20"
            }
        ]
      }
    ]
}
```

➡️ **“openTicket”:** `0` não abre ticket e `1` abre. Para abrir é obrigatório informar um Setor em `queueId`, e a conversa vai para **Aguardando** mesmo que já esteja em atendimento.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“phone”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“title”:** texto do título, acima da mensagem.

➡️ **“body”:** texto principal da mensagem.

➡️ **“footer”:** texto do rodapé, abaixo da mensagem.

➡️ **“buttons”:** a lista de botões da mensagem.

◽ **“type”:** `copy`.

◽ **“text”:** o rótulo que aparece no botão.

◽ **“code”:** o texto que vai para a área de transferência do cliente quando ele toca.

◽ A mensagem fica gravada no atendimento com uma descrição legível do que foi oferecido: título, texto, rodapé e o rótulo de cada botão entre colchetes.

⚠️ **Resposta de sucesso não garante que o cliente recebeu.** Se o motor recusar o envio — por exemplo com a conexão fora do ar — a recusa vira **nota interna** no atendimento e a resposta ainda volta como sucesso.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

◽ Vai no nível de cima do corpo, ao lado de `openTicket`, e não dentro de `body`.

#### 📌 Opcional repetir até 3 botões.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendButtonsPRO',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "openTicket": 0,
    "queueId": 0,
    "body": [
      {
        "phone": "5511955892164",
        "title": "Seu cupom exclusivo",
        "body": "Escolha um cupom conforme seu pedido",
        "footer": "Oferta válida até hoje",
        "buttons": [
            {
            "type": "copy",
            "text": "10% em compras até R$ 100",
            "code": "CUPOM10"
            },
            {
            "type": "copy",
            "text": "20% em compras até R$ 200",
            "code": "CUPOM20"
            }
        ]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendButtonsPRO' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"openTicket":0,"queueId":0,"body":[{"phone":"5511955892164","title":"Seu cupom exclusivo","body":"Escolha um cupom conforme seu pedido","footer":"Oferta válida até hoje","buttons":[{"type":"copy","text":"10% em compras até R$ 100","code":"CUPOM10"},{"type":"copy","text":"20% em compras até R$ 200","code":"CUPOM20"}]}]}'
```
