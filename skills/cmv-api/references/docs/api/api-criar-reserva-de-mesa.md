# API Criar Reserva de Mesa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-reserva-de-mesa
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Criar Reserva de Mesa

---

🧩 Cria **uma reserva de mesa** no salão, para um dia e um horário.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/reservas
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
    "inicio": "2026-11-20T20:00:00-03:00",
    "pessoas": 4,
    "duracao": 120,
    "mesaId": 3,
    "number": "5511955892164",
    "clienteNome": "Ana Souza",
    "observacao": "Aniversário",
    "confirmada": false
}
```

➡️ **“inicio”:** data e horário da reserva, no formato ISO 8601 com o fuso — por exemplo, `2026-11-20T20:00:00-03:00` (o `-03:00` é o fuso de Brasília). **Obrigatório.**

◽ Sem o fuso, como em `2026-11-20T20:00`, vale o horário do servidor da plataforma.

➡️ **“pessoas”:** quantas pessoas, de 1 a 999. **Obrigatório.**

➡️ **“duracao”:** quanto tempo a mesa fica reservada, em minutos, de 15 a 480.

◽ Sem a `duracao`, vale a **Duração da reserva (min)** da loja, em **Reserva de mesa**, no menu **PDV  ›  Cardápio digital**.

➡️ **“mesaId”:** o ID da mesa reservada, que vem no `id` da lista de mesas e comandas.

◽ Sem a `mesaId`, a reserva fica sem mesa, e a mesa é escolhida na chegada do cliente.

⚠️ **A mesma mesa não aceita duas reservas que se cruzam no horário**, entre as pendentes e as confirmadas. A reserva que começa no horário em que a outra termina entra.

➡️ **“number”:** telefone do cliente no formato ddi ddd numero (somente números).

◽ Quando o telefone é de um contato da empresa — com ou sem o nono dígito —, o contato vira o cliente da reserva. Em vez do `number`, dá para mandar o **`contactId`** do contato.

➡️ **“clienteNome”:** nome de quem reserva, com até 120 caracteres. **Obrigatório** quando o cliente não vem por um contato.

◽ Com um contato, o `clienteNome` enviado é o que fica na reserva; sem o `clienteNome`, vale o nome do contato.

◽ Sem contato, o telefone de quem reserva vai em **`clienteTelefone`**, com 8 a 15 números. Ele fica só na reserva e não liga a reserva a um contato.

➡️ **“observacao”:** observação da reserva, com até 500 caracteres.

➡️ **“confirmada”:** `true` faz a reserva já nascer **confirmada**. Com `false`, ou sem o campo, ela nasce **pendente**.

◽ A resposta traz a reserva criada, com o `id` dela.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/reservas',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "inicio": "2026-11-20T20:00:00-03:00",
    "pessoas": 4,
    "duracao": 120,
    "mesaId": 3,
    "number": "5511955892164",
    "clienteNome": "Ana Souza",
    "observacao": "Aniversário",
    "confirmada": false
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
curl -X POST 'https://api2.chatmasterveloz.com/api/pdv/reservas' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"inicio":"2026-11-20T20:00:00-03:00","pessoas":4,"duracao":120,"mesaId":3,"number":"5511955892164","clienteNome":"Ana Souza","observacao":"Aniversário","confirmada":false}'
```
