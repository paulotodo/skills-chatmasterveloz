# API Listar Horários Livres do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-horarios-livres-do-consultorio
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Listar Horários Livres do Consultório

---

🧩 Obter **os horários livres** de um serviço, dia a dia e por profissional, para oferecer ao paciente.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/horarios-livres?servicoId={servicoId}&de={dataInicio}&ate={dataFim}
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
// sem payload — os filtros vão na própria URL
```

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL.

◽ **servicoId:** o serviço. **Obrigatório.**

◽ **de** e **ate:** o primeiro e o último dia, no formato `AAAA-MM-DD`, no calendário da clínica. Sem `de`, vale hoje; sem `ate`, o mesmo dia do `de`.

⚠️ Só `AAAA-MM-DD`: `17/11/2026` é recusado.

◽ Vêm até **31 dias** por chamada. Pedido maior responde os 31 primeiros, com `cortado` em `true`.

◽ **profissionalId:** um ou mais profissionais, como `profissionalId=8,9`. Sem ele, vêm todos os ativos que atendem o serviço e aceitam marcação pela API.

◽ **modalidade:** `presencial` ou `teleconsulta`, a que o serviço permite. A teleconsulta não ocupa sala.

◽ **salaId:** a sala também precisa estar livre.

◽ **convenioId:** o convênio do paciente, como `convenioId=2`. Vêm só os profissionais que atendem por ele, cada um nos dias e horários em que atende por aquele convênio; o dia fora desses horários vem `fechado`. Convênio que não existe é recusado.

➡️ **Cada dia traz cada profissional com a `situacao` e os `inicios` livres:**

◽ `aberto` — há horários; `lotado` — tem expediente, mas está cheio; `fechado` — sem expediente; `bloqueado` — um bloqueio cobre o expediente inteiro; `antes_da_antecedencia` e `alem_do_horizonte` — fora das regras de tempo da marcação de fora.

◽ Os horários dividem o expediente pela duração do serviço e seguem as regras da marcação: o que aparece aqui pode ser marcado, a não ser que alguém marque antes.

◽ `primeiroLivre` traz o horário mais cedo de todos, com o profissional.

◽ Serviço ou profissional que não aceita marcação pela API é recusado.

◽ Datas e horas vêm com o deslocamento da clínica, como `2026-12-14T09:30:00-03:00`, e o `fuso` pelo nome, como `America/Sao_Paulo`.

◽ **Escopo da chave:** **Atendente** ou **Clínica**. O Token da Empresa vale como todos os escopos.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/horarios-livres?servicoId={servicoId}&de={dataInicio}&ate={dataFim}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/consultorio/horarios-livres?servicoId={servicoId}&de={dataInicio}&ate={dataFim}' -H 'Authorization: Bearer {seutokenaqui}'
```
