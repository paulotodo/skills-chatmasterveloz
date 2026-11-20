# API Atualizar a Situação de uma Reserva

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-a-situacao-de-uma-reserva
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Atualizar a Situação de uma Reserva

---

🧩 Atualiza **a situação de uma reserva** das Reservas: confirma, conclui, marca a falta ou cancela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/{reservaAgendaId}/situacao
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
    "motivo": "O cliente pediu para cancelar"
}
```

➡️ **“situacao”:** `confirmada`, `concluida`, `nao_compareceu` ou `cancelada`. **Obrigatório.**

◽ A situação segue os caminhos da reserva: a `pendente` vai para `confirmada` ou `cancelada`; a `confirmada`, para `concluida`, `nao_compareceu` ou `cancelada`. A concluída, a cancelada e a que não compareceu não mudam mais, e confirmar a já confirmada é recusado.

◽ A falta é `nao_compareceu`, com sublinhado.

➡️ **“motivo”:** o motivo do cancelamento, até 200 caracteres. Opcional.

◽ Cancelar a reserva que usa pacote devolve o crédito ao cliente.

◽ Na reserva de uma série, o `escopo` escolhe o que cancelar: `esta` (só ela), `proximas` (ela e as seguintes) ou `todas` (as da série que ainda estão pendentes ou confirmadas). Sem o `escopo`, só esta. As outras canceladas junto ficam com o mesmo motivo.

➡️ **A resposta traz a reserva** na situação nova. No cancelamento de uma série, traz também `canceladasNaSerie`, quantas outras reservas da série foram canceladas junto.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/{reservaAgendaId}/situacao',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "situacao": "cancelada",
    "motivo": "O cliente pediu para cancelar"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/reservas/{reservaAgendaId}/situacao' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"situacao":"cancelada","motivo":"O cliente pediu para cancelar"}'
```
