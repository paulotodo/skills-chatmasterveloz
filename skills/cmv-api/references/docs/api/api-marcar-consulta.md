# API Marcar Consulta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-marcar-consulta
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Marcar Consulta

---

🧩 Marca **uma consulta** no Consultório, com as mesmas regras da agenda da tela.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/agendamentos
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
    "servicoId": 1,
    "profissionalId": 8,
    "inicio": "2026-12-14T09:30",
    "modalidade": "presencial",
    "paciente": {
        "nome": "Pedro Souza"
    },
    "contato": {
        "telefone": "5511955892164"
    }
}
```

➡️ **“servicoId”:** o serviço. **Obrigatório.**

➡️ **“profissionalId”:** o profissional. No lugar dele, `"qualquerProfissional": true` marca com o primeiro livre entre os que atendem o serviço.

➡️ **“inicio”:** o horário, como `2026-12-14T09:30` — lido na hora da clínica — ou com o deslocamento, como `2026-12-14T09:30:00-03:00`. **Obrigatório.**

◽ Nunca no passado, e sempre dentro da antecedência e dos dias à frente da marcação de fora.

➡️ **“modalidade”:** `presencial` ou `teleconsulta`, a que o serviço permite.

➡️ **“paciente”:** quem vai à consulta.

◽ Com o `id`, é esse paciente — com a chave de escopo Atendente, só se ele for do contato.

◽ Só com o `nome`, vale o paciente do contato com o mesmo nome, sem diferença de maiúsculas, acentos e espaços.

◽ O contato sem paciente ganha o paciente novo, já ligado a ele. Para o cadastro, mande também `dataNascimento`, `responsavel`, `cpf` e `email`.

◽ O contato com pacientes e nenhum com o nome pedido: a chamada é recusada e traz os pacientes dele em `candidatos`. Para criar mesmo assim, mande `"pacienteNovo": true`.

➡️ **“contato”:** o contato da conversa, pelo `telefone` — em qualquer formato; com e sem o nono dígito é o mesmo — ou pelo `contactId`. **Obrigatório** com a chave de escopo Atendente: ela só mexe nas consultas dos pacientes desse contato.

◽ O contato que não existe é criado.

◽ Opcionais: `salaId`, `observacoes`, `canal` e a conversa ligada à consulta, em `conexaoId` e `ticketId`.

◽ `convenioId`, também opcional: o convênio da consulta. O profissional precisa atender por ele; o que não atende pelo convênio é recusado.

◽ `"encaixe": true` passa por cima do que já está marcado, nunca de um bloqueio — só com a chave de escopo Clínica.

➡️ **A resposta traz a consulta em `agendamento`**, com `id`, `codigo` (o código curto, para o paciente informar), `versao`, `status`, `inicio`, `fim`, o serviço, o profissional, a sala, o paciente e o contato.

◽ A mesma consulta já marcada — mesmo paciente, serviço e horário — volta com `jaExistia` em `true`, sem marcar de novo.

◽ Quando o horário não serve, a recusa traz em `livres` os horários livres daquele dia, para oferecer outro na mesma conversa.

◽ Na recusa, decida pelo `error`; a `mensagem` traz o motivo em português, para o registro ou para repetir ao paciente.

◽ Para repetir a chamada sem risco de gravar duas vezes, mande o cabeçalho `Idempotency-Key` com um uuid. A mesma chave com o mesmo payload, em até 24 horas, devolve a mesma resposta sem gravar de novo, com o cabeçalho `Idempotent-Replayed: true`; com outro payload, é recusada.

◽ Datas e horas vêm com o deslocamento da clínica, como `2026-12-14T09:30:00-03:00`, e o `fuso` pelo nome, como `America/Sao_Paulo`.

◽ **Escopo da chave:** **Atendente** ou **Clínica**. O Token da Empresa vale como todos os escopos.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "servicoId": 1,
    "profissionalId": 8,
    "inicio": "2026-12-14T09:30",
    "modalidade": "presencial",
    "paciente": {
        "nome": "Pedro Souza"
    },
    "contato": {
        "telefone": "5511955892164"
    }
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
curl -X POST 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"servicoId":1,"profissionalId":8,"inicio":"2026-12-14T09:30","modalidade":"presencial","paciente":{"nome":"Pedro Souza"},"contato":{"telefone":"5511955892164"}}'
```
