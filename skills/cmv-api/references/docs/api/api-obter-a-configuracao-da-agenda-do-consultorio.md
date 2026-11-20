# API Obter a Configuração da Agenda do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-a-configuracao-da-agenda-do-consultorio
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Obter a Configuração da Agenda do Consultório

---

🧩 Obter **a configuração da agenda** do Consultório: o fuso da clínica, as regras de tempo da marcação de fora e o que a agenda usa.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/config
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

◽ A resposta traz o `fuso` da clínica, a `antecedenciaMinimaMinutos` e o `horizonteDias` da marcação de fora (`null` quando não há limite de dias), se a clínica oferece `teleconsulta`, os `status` da agenda e as `modalidades`.

◽ Em `situacoesDoDia`, as situações que os horários livres usam, e em `maximoDeDiasNosLivres`, quantos dias os horários livres devolvem numa chamada.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/config',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/consultorio/config' -H 'Authorization: Bearer {seutokenaqui}'
```
