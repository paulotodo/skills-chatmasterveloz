# API Buscar Consultas do Contato

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-buscar-consultas-do-contato
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Buscar Consultas do Contato

---

🧩 Obter **as consultas de um contato** — de todos os pacientes ligados a ele —, pela ordem do horário.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/agendamentos/buscar
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
    "aPartirDe": "agora",
    "status": [
        "agendado",
        "confirmado"
    ],
    "limite": 20
}
```

➡️ **“telefone”:** o telefone da conversa, em qualquer formato; com e sem o nono dígito é o mesmo. No lugar dele, `contactId`. **Obrigatório** com a chave de escopo Atendente: ela só mexe nas consultas dos pacientes desse contato.

◽ É uma chamada POST para o telefone não ir no endereço.

➡️ **“aPartirDe”:** `agora` (o padrão: as que ainda não terminaram), `tudo`, um dia ou um instante.

➡️ **“status”:** só estes status, numa lista, como `["agendado", "confirmado"]`.

➡️ **“limite”:** de 1 a 100. Padrão `20`.

◽ Também filtram: `codigo` (o código curto, sem diferença de maiúsculas), `id` e `pacienteId`. Com a chave de escopo Atendente, só dentro das consultas do contato: a consulta de outra pessoa volta como lista vazia.

◽ Com a chave de escopo Clínica, o contato é opcional: sem ele, vêm as consultas de todos.

➡️ **A resposta traz `agendamentos`**, cada um com `id`, `codigo`, `versao`, `status`, `inicio`, `fim`, o serviço, o profissional, o paciente e o contato. Sem nenhuma, a lista vem vazia.

◽ Datas e horas vêm com o deslocamento da clínica, como `2026-12-14T09:30:00-03:00`, e o `fuso` pelo nome, como `America/Sao_Paulo`.

◽ **Escopo da chave:** **Atendente** ou **Clínica**. O Token da Empresa vale como todos os escopos.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos/buscar',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "telefone": "5511955892164",
    "aPartirDe": "agora",
    "status": [
        "agendado",
        "confirmado"
    ],
    "limite": 20
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
curl -X POST 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos/buscar' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"telefone":"5511955892164","aPartirDe":"agora","status":["agendado","confirmado"],"limite":20}'
```
