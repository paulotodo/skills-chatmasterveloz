# API Listar Profissionais do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-profissionais-do-consultorio
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Listar Profissionais do Consultório

---

🧩 Obter a **lista de profissionais** do Consultório, com o expediente de cada um.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/profissionais
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

◽ Cada profissional traz `id`, `nome`, `conselho`, `registro`, `especialidades`, os serviços ativos que atende (`servicoIds`), `marcacaoExterna` (se aceita marcação pela API) e `ativo`.

◽ O `expediente` vem dia a dia, de `segunda` a `domingo`, com os intervalos de `inicio` e `fim`. O dia sem expediente vem com a lista vazia.

◽ Com `expedienteCadastrado` em `false`, o profissional não tem horário cadastrado, e os horários livres não oferecem horário dele.

◽ Para filtrar, acrescente ao endereço `?ativos=1`, `marcacaoExterna=1` ou `servicoId=` com o ID de um serviço — só quem atende esse serviço. Serviço que não existe é recusado.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/profissionais',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/consultorio/profissionais' -H 'Authorization: Bearer {seutokenaqui}'
```
