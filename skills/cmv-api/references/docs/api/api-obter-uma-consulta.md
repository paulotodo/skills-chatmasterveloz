# API Obter uma Consulta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-uma-consulta
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Obter uma Consulta

---

🧩 Obter **uma consulta específica** do Consultório, pelo id.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/agendamentos/{consultaId}
```

##### Método

```
GET
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```
// sem payload
```

➡️ Esta chamada não tem payload.

◽ O `consultaId` vai no próprio endereço: é o `id` que vem na marcação e na busca. Consulta que não existe é recusada.

◽ **Escopo da chave:** só **Clínica**. A chave de escopo Atendente é recusada: ela lê as consultas pela busca, com o contato. O Token da Empresa vale como todos os escopos.

◽ A consulta vem em `agendamento`, com `id`, `codigo`, `versao`, `status`, `inicio`, `fim`, `duracaoMinutos`, o serviço, o profissional, a sala, a `modalidade`, o paciente, o contato, a conversa (`conexao` e `ticketId`), a `origem` (`api` ou `painel`) e quem criou, em `criadoPor`.

◽ A `versao` cresce a cada mudança: é ela que a remarcação e a mudança de status conferem.

◽ A consulta criada pela API traz em `criadoPor` o nome da chave, em `integracao`.

◽ Datas e horas vêm com o deslocamento da clínica, como `2026-12-14T09:30:00-03:00`, e o `fuso` pelo nome, como `America/Sao_Paulo`.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos/{consultaId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/consultorio/agendamentos/{consultaId}' -H 'Authorization: Bearer {seutokenaqui}'
```
