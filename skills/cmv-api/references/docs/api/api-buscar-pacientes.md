# API Buscar Pacientes

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-buscar-pacientes
- **Categoria:** APIs
- **Menu:** APIs › Consultório › API Buscar Pacientes

---

🧩 Obter **os pacientes** de um telefone, de um contato ou de um CPF.

⚠️ Esta chamada usa uma **chave do Consultório**, criada no menu **Consultório  ›  Cadastros do consultório**, aba **Integrações**, ou o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa** — sem informar a Conexão. O token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/consultorio/pacientes/buscar
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
    "telefone": "5511955892164"
}
```

➡️ **“telefone”:** o telefone, em qualquer formato; com e sem o nono dígito é o mesmo.

◽ No lugar dele, `contactId` (o contato) ou `cpf` (com ou sem pontuação). Um dos três é **obrigatório**, e a busca é exata: por nome, não busca.

◽ A resposta traz `pacientes`, cada um com `id`, `nome`, `cpf`, `dataNascimento`, `responsavel`, `telefone`, `email`, `contactId`, `contato`, `ativo` e o resto da ficha de cadastro. Sem nenhum, a lista vem vazia.

◽ **Escopo da chave:** **Pacientes**. O Token da Empresa vale como todos os escopos.

◽ Até **120 chamadas por minuto** por chave. Passando disso, a chamada é recusada, e o cabeçalho `Retry-After` diz quantos segundos esperar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/consultorio/pacientes/buscar',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "telefone": "5511955892164"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/consultorio/pacientes/buscar' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"telefone":"5511955892164"}'
```
