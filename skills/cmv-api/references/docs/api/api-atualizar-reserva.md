# API Atualizar Reserva

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-reserva
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Atualizar Reserva

---

🧩 Atualiza **uma reserva** das Reservas: remarca o horário ou muda o cliente, as pessoas e a observação.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/{reservaAgendaId}
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
    "inicio": "2026-11-30T10:00:00-03:00",
    "observacao": "Remarcada a pedido do cliente"
}
```

➡️ **Só o que vier no payload muda.** O id da reserva vai no endereço, no lugar de `{reservaAgendaId}`.

➡️ **“inicio”:** o novo início, na oferta por horário e na turma. O horário é conferido de novo, sem contar a própria reserva, e o horário ocupado é recusado.

◽ Na diária, `entrada` e `saida` (`AAAA-MM-DD`) mudam a estadia, e as noites e o total são calculados de novo.

◽ Também mudam: `recursoId`, `ofertaId`, `pessoas` e o cliente (`clienteNome`, `clienteTelefone`, `clienteEmail`, `contactId`).

➡️ **“observacao”:** a observação, que a equipe vê no detalhe da reserva.

◽ `"pacoteClienteId": null` tira o pacote da reserva e devolve o crédito ao cliente.

➡️ **Só a reserva pendente ou confirmada muda.** A concluída, a cancelada e a que não compareceu são recusadas.

➡️ **A resposta traz a reserva** como ficou, com os mesmos campos da chamada de obter uma reserva.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/{reservaAgendaId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "inicio": "2026-11-30T10:00:00-03:00",
    "observacao": "Remarcada a pedido do cliente"
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/reservas/{reservaAgendaId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"inicio":"2026-11-30T10:00:00-03:00","observacao":"Remarcada a pedido do cliente"}'
```
