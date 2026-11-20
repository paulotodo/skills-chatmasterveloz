# API Atualizar o Status da Consulta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-o-status-da-consulta
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Atualizar o Status da Consulta

---

🧩 Confirma, cancela ou marca **a falta ou o atendimento** de uma consulta.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/agendamentos/{consultaId}/status
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
    "telefone": "5511955892164",
    "versao": 4,
    "status": "cancelado",
    "motivo": "Viagem de trabalho",
    "serie": "esta",
    "pedidoPor": "paciente"
}
```

➡️ **“consultaId”:** ID da consulta — vai no próprio endereço, no lugar de `{consultaId}`. É o `id` que vem na marcação e na busca.

➡️ **“telefone”:** o telefone da conversa, em qualquer formato; com e sem o nono dígito é o mesmo. No lugar dele, `contactId`. **Obrigatório** com a chave de escopo Atendente: ela só mexe nas consultas dos pacientes desse contato.

➡️ **“status”:** `confirmado`, `cancelado`, `faltou` ou `atendido`. **Obrigatório.**

◽ Com a chave de escopo Atendente: só `confirmado` e `cancelado`, só antes do início, sempre pedido pelo paciente.

◽ Com a chave de escopo Clínica: também `faltou` e `atendido`, só depois do início.

◽ O cancelado, a falta e o atendido não voltam pela API: reabrir a consulta é na tela.

➡️ **“versao”:** opcional. A `versao` da consulta que você leu. Se a consulta mudou depois, a chamada é recusada, nada é gravado, e a resposta traz a consulta como está agora em `agendamento`. Vale também no cabeçalho `If-Match`.

➡️ **“motivo”:** opcional. O porquê, como no cancelamento.

➡️ **“serie”:** só no cancelamento. `esta` cancela só esta consulta; `proximas` leva junto as seguintes da série.

➡️ **“pedidoPor”:** `paciente` ou `clinica`. Com a chave de escopo Atendente, é sempre `paciente`.

◽ Pedir o status que a consulta já tem volta com `mudou` em `false`, sem gravar nada.

◽ A resposta traz a consulta em `agendamento`, as afetadas em `agendamentos` (com a série, no cancelamento) e o `mudou`.

◽ Na recusa, decida pelo `error`; a `mensagem` traz o motivo em português, para o registro ou para repetir ao paciente.

◽ Para repetir a chamada sem risco de gravar duas vezes, mande o cabeçalho `Idempotency-Key` com um uuid. A mesma chave com o mesmo payload, em até 24 horas, devolve a mesma resposta sem gravar de novo, com o cabeçalho `Idempotent-Replayed: true`; com outro payload, é recusada.

◽ **Escopo da chave:** **Atendente** ou **Clínica**. O Token da Empresa vale como todos os escopos.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos/{consultaId}/status',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "telefone": "5511955892164",
    "versao": 4,
    "status": "cancelado",
    "motivo": "Viagem de trabalho",
    "serie": "esta",
    "pedidoPor": "paciente"
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Chave do Consultório ou Token da Empresa
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X POST 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos/{consultaId}/status' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"telefone":"5511955892164","versao":4,"status":"cancelado","motivo":"Viagem de trabalho","serie":"esta","pedidoPor":"paciente"}'
```
