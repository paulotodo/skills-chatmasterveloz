# API Remarcar Consulta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-remarcar-consulta
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Remarcar Consulta

---

🧩 Remarca **uma consulta** para outro horário e, se pedido, outro profissional.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/agendamentos/{consultaId}/remarcar
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
    "versao": 3,
    "inicio": "2026-12-15T15:00",
    "motivo": "Paciente pediu pelo WhatsApp",
    "pedidoPor": "paciente"
}
```

➡️ **“consultaId”:** ID da consulta — vai no próprio endereço, no lugar de `{consultaId}`. É o `id` que vem na marcação e na busca.

➡️ **“telefone”:** o telefone da conversa, em qualquer formato; com e sem o nono dígito é o mesmo. No lugar dele, `contactId`. **Obrigatório** com a chave de escopo Atendente: ela só mexe nas consultas dos pacientes desse contato.

➡️ **“versao”:** opcional. A `versao` da consulta que você leu. Se a consulta mudou depois, a chamada é recusada, nada é gravado, e a resposta traz a consulta como está agora em `agendamento`. Vale também no cabeçalho `If-Match`.

➡️ **“inicio”:** o horário, como `2026-12-14T09:30` — lido na hora da clínica — ou com o deslocamento, como `2026-12-14T09:30:00-03:00`. **Obrigatório.**

➡️ **“profissionalId”:** opcional. Outro profissional.

➡️ **“motivo”:** opcional. O porquê da remarcação.

➡️ **“pedidoPor”:** `paciente` ou `clinica`. Com a chave de escopo Atendente, é sempre `paciente`.

◽ O serviço não muda: para trocar o serviço, cancele e marque de novo.

◽ Passa pelas mesmas regras da marcação. A confirmação volta para `agendado`, e o lembrete é refeito para o horário novo.

◽ Não remarca a consulta que já começou, foi cancelada ou atendida.

◽ O mesmo horário volta com `mudou` em `false`.

◽ Opcionais: a conversa ligada, em `conexaoId` e `ticketId`, e `"encaixe": true`, só com a chave de escopo Clínica.

◽ A resposta traz a consulta como ficou, em `agendamento`, e o `mudou`.

◽ Quando o horário não serve, a recusa traz em `livres` os horários livres daquele dia, para oferecer outro na mesma conversa.

◽ Na recusa, decida pelo `error`; a `mensagem` traz o motivo em português, para o registro ou para repetir ao paciente.

◽ Para repetir a chamada sem risco de gravar duas vezes, mande o cabeçalho `Idempotency-Key` com um uuid. A mesma chave com o mesmo payload, em até 24 horas, devolve a mesma resposta sem gravar de novo, com o cabeçalho `Idempotent-Replayed: true`; com outro payload, é recusada.

◽ Datas e horas vêm com o deslocamento da clínica, como `2026-12-14T09:30:00-03:00`, e o `fuso` pelo nome, como `America/Sao_Paulo`.

◽ **Escopo da chave:** **Atendente** (só antes do início) ou **Clínica**. O Token da Empresa vale como todos os escopos.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos/{consultaId}/remarcar',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "telefone": "5511955892164",
    "versao": 3,
    "inicio": "2026-12-15T15:00",
    "motivo": "Paciente pediu pelo WhatsApp",
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
curl -X POST 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos/{consultaId}/remarcar' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"telefone":"5511955892164","versao":3,"inicio":"2026-12-15T15:00","motivo":"Paciente pediu pelo WhatsApp","pedidoPor":"paciente"}'
```
