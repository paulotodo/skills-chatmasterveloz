# API Atualizar a Situação de uma Reserva de Mesa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-a-situacao-de-uma-reserva-de-mesa
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Atualizar a Situação de uma Reserva de Mesa

---

🧩 Atualiza a **situação de uma reserva de mesa**: confirma, marca a chegada do cliente, marca que ele não veio ou cancela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}/situacao
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
    "situacao": "cancelada",
    "motivo": "Cliente desmarcou pelo WhatsApp."
}
```

➡️ **“situacao”:** a situação nova — `confirmada`, `compareceu` (o cliente chegou), `nao-compareceu` ou `cancelada`.

◽ A reserva **pendente** vai para qualquer uma delas; a **confirmada**, para `compareceu`, `nao-compareceu` ou `cancelada`.

◽ Depois de `compareceu`, `nao-compareceu` ou `cancelada`, a reserva não muda mais, e a chamada é recusada.

➡️ **“motivo”:** o motivo, com até 500 caracteres — usado sobretudo no cancelamento, e pode ficar de fora.

➡️ **A chegada (`compareceu`) com mesa abre a conta da mesa** com as pessoas e o cliente da reserva, e a reserva passa a guardar o `comandaId` dessa conta.

◽ Vale a mesa da reserva, ou outra mandada em **`mesaId`**, junto com a `situacao` — por exemplo, `{"situacao": "compareceu", "mesaId": 3}`. Com a `mesaId`, a reserva passa para essa mesa.

◽ Sem mesa na reserva e sem `mesaId`, a chegada é marcada sem abrir conta, e o `comandaId` fica `null`.

⚠️ **Mesa com conta aberta recusa a chegada**, e a reserva continua como estava.

➡️ **O `reservaId` vai no próprio endereço da chamada:** é o ID da reserva, que vem na lista de reservas e na resposta da criação.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}/situacao',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "situacao": "cancelada",
    "motivo": "Cliente desmarcou pelo WhatsApp."
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}/situacao' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"situacao":"cancelada","motivo":"Cliente desmarcou pelo WhatsApp."}'
```
