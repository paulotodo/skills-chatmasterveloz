# API Listar Serviços do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-servicos-do-consultorio
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Listar Serviços do Consultório

---

🧩 Obter a **lista de serviços** do Consultório, em ordem de nome.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/servicos
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

◽ **Escopo da chave:** **Atendente** ou **Clínica**. O Token da Empresa vale como todos os escopos.

◽ Cada serviço traz `id`, `nome`, `descricao`, `duracaoMinutos`, `preco` (número; `0` é sem preço), `modalidade` (`presencial`, `teleconsulta` ou `ambas`), quem atende — `todosOsProfissionais` em `true`, ou os `profissionalIds` —, `marcacaoExterna` (se aceita marcação pela API) e `ativo`.

◽ `antecedenciaMinimaMinutos` e `horizonteDias` são a regra de tempo da marcação de fora que vale para o serviço: a dele, ou a geral da clínica.

◽ Para filtrar, acrescente ao endereço `?ativos=1` (só os ativos) e `marcacaoExterna=1` (só os que aceitam marcação pela API).

◽ É deste `id` que o `servicoId` dos horários livres e da marcação precisa.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/servicos',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/consultorio/servicos' -H 'Authorization: Bearer {seutokenaqui}'
```
