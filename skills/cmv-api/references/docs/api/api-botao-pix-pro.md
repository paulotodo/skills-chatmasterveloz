# API Botão Pix

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-botao-pix-pro
- **Categoria:** APIs
- **Menu:** APIs › Botões › API Botão Pix

---

🧩 Envia uma mensagem com **botão de copiar a chave Pix** para o cliente pagar.

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
        "title": "Pagamento com PIX",
        "body": "Toque para copiar e pagar",
        "footer": "Pedido #123",
        "buttons": [
            {
            "type": "pix",
            "text": "Pagar com PIX",
            "pixKey": "sua-chave-pix",
            "pixType": "evp"
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

◽ **“type”:** `pix`.

◽ **“text”:** o rótulo que aparece no botão.

◽ **“pixKey”:** a chave Pix que o cliente copia ao tocar.

◽ **“pixType”:** o tipo da chave — `email`, `phone`, `cpf`, `cnpj` ou `evp`.

◽ A mensagem fica gravada no atendimento com uma descrição legível do que foi oferecido: título, texto, rodapé e o rótulo de cada botão entre colchetes.

⚠️ **Resposta de sucesso não garante que o cliente recebeu.** Se o motor recusar o envio — por exemplo com a conexão fora do ar — a recusa vira **nota interna** no atendimento e a resposta ainda volta como sucesso.

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
        "title": "Pagamento com PIX",
        "body": "Toque para copiar e pagar",
        "footer": "Pedido #123",
        "buttons": [
            {
            "type": "pix",
            "text": "Pagar com PIX",
            "pixKey": "sua-chave-pix",
            "pixType": "evp"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/whatsmeow/sendButtonsPRO' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"openTicket":0,"queueId":0,"body":[{"phone":"5511955892164","title":"Pagamento com PIX","body":"Toque para copiar e pagar","footer":"Pedido #123","buttons":[{"type":"pix","text":"Pagar com PIX","pixKey":"sua-chave-pix","pixType":"evp"}]}]}'
```
