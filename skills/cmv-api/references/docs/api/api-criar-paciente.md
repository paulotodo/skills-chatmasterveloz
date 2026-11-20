# API Criar Paciente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-paciente
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Criar Paciente

---

🧩 Cria **um paciente** no Consultório, já ligado ao contato da conversa.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/pacientes
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
    "nome": "Pedro Souza",
    "dataNascimento": "2018-03-02",
    "responsavel": "Carla Souza",
    "cpf": "123.456.789-09",
    "email": "pedro@exemplo.com",
    "contato": {
        "telefone": "5511955892164"
    }
}
```

➡️ **“nome”:** o nome do paciente. **Obrigatório.**

➡️ **“dataNascimento”:** no formato `AAAA-MM-DD`.

➡️ **“responsavel”:** o responsável, como na ficha de uma criança.

➡️ **“cpf”:** com ou sem pontuação. CPF inválido é recusado, e o CPF que já é de outro paciente também: a recusa traz o `pacienteId` dele.

➡️ **“email”:** o e-mail do paciente.

➡️ **“contato”:** o contato a que o paciente fica ligado, pelo `telefone` ou pelo `contactId`. O telefone sem contato ganha um.

◽ A resposta traz o `paciente`, com o `id`, a ficha, o `contactId`, o `contato` e o `ativo`.

◽ Para repetir a chamada sem risco de gravar duas vezes, mande o cabeçalho `Idempotency-Key` com um uuid. A mesma chave com o mesmo payload, em até 24 horas, devolve a mesma resposta sem gravar de novo, com o cabeçalho `Idempotent-Replayed: true`; com outro payload, é recusada.

◽ **Escopo da chave:** **Pacientes**. O Token da Empresa vale como todos os escopos.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/pacientes',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Pedro Souza",
    "dataNascimento": "2018-03-02",
    "responsavel": "Carla Souza",
    "cpf": "123.456.789-09",
    "email": "pedro@exemplo.com",
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
curl -X POST 'https://api2.chatmasterveloz.com/api/consultorio/pacientes' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Pedro Souza","dataNascimento":"2018-03-02","responsavel":"Carla Souza","cpf":"123.456.789-09","email":"pedro@exemplo.com","contato":{"telefone":"5511955892164"}}'
```
