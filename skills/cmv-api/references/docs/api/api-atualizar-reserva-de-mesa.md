# API Atualizar Reserva de Mesa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-reserva-de-mesa
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Atualizar Reserva de Mesa

---

🧩 Atualiza **uma reserva de mesa** ainda pendente ou confirmada: o horário, a duração, as pessoas, a mesa, o cliente e a observação.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}
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
    "inicio": "2026-11-20T21:00:00-03:00",
    "pessoas": 6,
    "mesaId": 3,
    "observacao": "Aniversário, com bolo"
}
```

➡️ **“inicio”:** o novo horário, no formato ISO 8601 com o fuso — por exemplo, `2026-11-20T21:00:00-03:00` (o `-03:00` é o fuso de Brasília).

➡️ **“pessoas”:** quantas pessoas, de 1 a 999.

➡️ **“mesaId”:** o ID da mesa, que vem no `id` da lista de mesas e comandas. Com `null`, a reserva fica sem mesa, e a mesa é escolhida na chegada do cliente.

⚠️ **O horário é conferido de novo na mesa:** ela não aceita outra reserva, pendente ou confirmada, que se cruze com o horário da reserva atualizada.

➡️ **“observacao”:** a observação, com até 500 caracteres.

➡️ **Vão só os campos que mudam** — o que ficar de fora continua como está. Também podem ir:

◽ **“duracao”:** quanto tempo a mesa fica reservada, em minutos, de 15 a 480.

◽ **“clienteNome”** e **“clienteTelefone”:** o nome, com até 120 caracteres, e o telefone, com 8 a 15 números, de quem reserva.

⚠️ **Só a reserva pendente ou confirmada pode ser atualizada.** Depois da chegada do cliente, do não comparecimento ou do cancelamento, a chamada é recusada.

◽ O contato da reserva e a situação não mudam por aqui. Corpo sem nenhum campo que muda é recusado.

➡️ **O `reservaId` vai no próprio endereço da chamada:** é o ID da reserva, que vem na lista de reservas e na resposta da criação.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "inicio": "2026-11-20T21:00:00-03:00",
    "pessoas": 6,
    "mesaId": 3,
    "observacao": "Aniversário, com bolo"
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/pdv/reservas/{reservaId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"inicio":"2026-11-20T21:00:00-03:00","pessoas":6,"mesaId":3,"observacao":"Aniversário, com bolo"}'
```
