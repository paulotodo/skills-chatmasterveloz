# API Editar Mensagem no Painel

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-editar-mensagem-no-painel
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Editar Mensagem no Painel

---

🧩 Troca o **texto de uma mensagem no painel** e avisa na hora a tela de quem está com o atendimento aberto.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/edit
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
    "message_id": 98765,
    "body": "🎙️ Transcrição: bom dia, quero um orçamento"
}
```

➡️ **“message_id”:** ID da mensagem **no painel**. Informe este ou o `wid`.

◽ É o `mensagem.id` que chega no webhook da conexão, e o `id` de cada item da lista de mensagens do atendimento.

➡️ **“body”:** o texto novo. **Obrigatório.**

➡️ **“ticketId”:** opcional. Estreita a busca: a mensagem precisa ser desse atendimento.

⚠️ **Isto não é a edição de mensagem do WhatsApp.** O cliente não vê nada: só a linha do painel muda. Serve para gravar no balão a transcrição de um áudio ou a descrição de uma imagem ou de um PDF.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/edit',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "message_id": 98765,
    "body": "🎙️ Transcrição: bom dia, quero um orçamento"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/edit' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"message_id":98765,"body":"🎙️ Transcrição: bom dia, quero um orçamento"}'
```
