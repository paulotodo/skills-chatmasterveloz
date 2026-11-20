# API Enviar Arquivo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-enviar-arquivo
- **Categoria:** APIs
- **Menu:** APIs › Mídias › API Enviar Arquivo

---

🧩 Envia um **arquivo que o seu próprio sistema anexa à requisição** — aqui o arquivo viaja junto (multipart), em vez de ser buscado em uma URL —, com opções de abrir um ticket e atribuir a conversa a um Setor.

**API:** Básica, Pro

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/send
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

```php
array(
    'medias'=> new CURLFILE('IMAGEM.JPEG'),
    'number' => '5511955892164',
    'openTicket' => '0',
    'queueId' => '0',
    'body' => 'Teste'
  )
```

➡️ **“medias”:** o arquivo a ser enviado.

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“openTicket”:** `0` não abre ticket e `1` abre. Para abrir é obrigatório informar um Setor em `queueId`, e a conversa vai para **Aguardando** mesmo que já esteja em atendimento.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“body”:** legenda do arquivo.

➡️ **“assinaturaIa”:** opcional — acrescente aos campos do formulário quando quem envia é a sua IA, com o nome da IA (até 100 caracteres). A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, o envio fica como sempre.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/send',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => array(
    'medias'=> new CURLFILE('IMAGEM.JPEG'),
    'number' => '5511955892164',
    'openTicket' => '0', //0 Não abre ticket e 1 Abre Ticket
    'queueId' => '0', // Informe o ID do Setor desejado (se abrir ticket)
    'body' => 'Teste' // Se enviado aparecerá como legenda do arquivo
  ),
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
