# API Ligar Paciente a um Contato

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-ligar-paciente-a-um-contato
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Ligar Paciente a um Contato

---

🧩 Liga **um paciente** a um contato, ou troca o contato dele.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/pacientes/{pacienteId}
```

##### Método

```
PUT
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "contato": {
        "contactId": 55
    }
}
```

➡️ **“pacienteId”:** ID do paciente — vai no próprio endereço, no lugar de `{pacienteId}`.

➡️ **“contato”:** o contato novo, pelo `telefone` ou pelo `contactId`. **Obrigatório.**

◽ Só o contato muda: a ficha fica como está, inclusive o telefone dela.

◽ O telefone sem contato ganha um. Contato que não existe é recusado.

◽ A resposta traz o `paciente`, com o contato novo.

◽ Para repetir a chamada sem risco de gravar duas vezes, mande o cabeçalho `Idempotency-Key` com um uuid. A mesma chave com o mesmo payload, em até 24 horas, devolve a mesma resposta sem gravar de novo, com o cabeçalho `Idempotent-Replayed: true`; com outro payload, é recusada.

◽ **Escopo da chave:** **Pacientes**. O Token da Empresa vale como todos os escopos.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/pacientes/{pacienteId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "contato": {
        "contactId": 55
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/consultorio/pacientes/{pacienteId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"contato":{"contactId":55}}'
```
