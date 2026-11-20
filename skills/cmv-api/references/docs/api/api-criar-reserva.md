# API Criar Reserva

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-reserva
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Criar Reserva

---

🧩 Cria **uma reserva** nas Reservas, com as mesmas regras da Agenda de reservas.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas
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
    "ofertaId": 23,
    "inicio": "2026-11-30T09:00:00-03:00",
    "recursoId": 17,
    "pessoas": 1,
    "clienteNome": "Ana Souza",
    "clienteTelefone": "5511955892164",
    "observacao": "Primeira visita"
}
```

➡️ **“ofertaId”:** a oferta reservada. **Obrigatório.**

➡️ **“inicio”:** o início, na oferta por horário e na turma, como `2026-11-30T09:00:00-03:00`.

◽ O horário precisa estar livre e dentro do atendimento do recurso. Horário ocupado, bloqueado ou fora do atendimento é recusado.

◽ Na diária, no lugar do `inicio`, vão a `entrada` e a `saida`, no formato `AAAA-MM-DD`. As noites, o total e o sinal saem da oferta, e a entrada e a saída seguem os horários da oferta.

➡️ **“recursoId”:** o recurso. Sem ele, a reserva vai para o primeiro recurso livre que atende a oferta.

➡️ **“pessoas”:** quantas pessoas, entre o mínimo e o máximo da oferta.

➡️ **“clienteNome”:** o nome do cliente. **Obrigatório** sem o `contactId`.

◽ No lugar do nome, `"contactId"` liga a reserva a um contato da empresa, e o nome, o telefone e o e-mail que faltarem vêm do contato.

➡️ **“clienteTelefone”:** telefone do cliente no formato ddi ddd numero (somente números).

◽ Opcional: `clienteEmail`.

➡️ **“observacao”:** uma observação, que a equipe vê no detalhe da reserva.

◽ Com `"comoCliente": true`, a reserva segue as regras da página de reservas, como a antecedência e o limite de dias à frente.

◽ Com `"pacoteClienteId"`, a reserva usa o pacote do cliente: fica sem preço e gasta um crédito, que volta se a reserva for cancelada. O pacote precisa ser do mesmo cliente, cobrir a oferta e ter crédito. A diária não usa pacote.

➡️ **A resposta traz a reserva**, com `id`, `codigo` (o código da reserva, de 8 letras), `situacao`, `origem`, `inicio`, `fim`, `preco` e o `link`.

◽ Feita pela equipe, sem o `comoCliente`, a reserva nasce `confirmada`.

◽ Na **Agenda de reservas**, a reserva feita pela API aparece com a origem **Pela integração**.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ofertaId": 23,
    "inicio": "2026-11-30T09:00:00-03:00",
    "recursoId": 17,
    "pessoas": 1,
    "clienteNome": "Ana Souza",
    "clienteTelefone": "5511955892164",
    "observacao": "Primeira visita"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/reservas' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ofertaId":23,"inicio":"2026-11-30T09:00:00-03:00","recursoId":17,"pessoas":1,"clienteNome":"Ana Souza","clienteTelefone":"5511955892164","observacao":"Primeira visita"}'
```
