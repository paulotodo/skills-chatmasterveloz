# API Listar Gravações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-gravacoes
- **Categoria:** APIs
- **Menu:** APIs › Gravações › API Listar Gravações

---

🧩 Obter a **lista de gravações das chamadas** da sua empresa, das mais novas às mais antigas.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/gravacoes?pageNumber={pageNumber}&de={dataInicio}&ate={dataFim}&origem={origemDaGravacao}&ticketId={ticketId}&chatId={chatId}&estado={estadoDaGravacao}&busca={busca}
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

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, e todos são opcionais.

◽ **pageNumber:** a página, começando em `1`. Vêm 20 gravações por página: `hasMore` diz se há outra, e `count`, quantas casam com os filtros em todas as páginas.

◽ **de** e **ate:** só as chamadas que começaram a partir de um dia e até um dia, no formato `AAAA-MM-DD`.

◽ **origem:** `atendimento` (videochamada com o cliente) ou `chat` (chamada da equipe no Chat Interno).

◽ **ticketId** e **chatId:** só as de um atendimento ou só as de uma conversa do Chat Interno. Use um ou outro: cada gravação é de um atendimento ou de uma conversa, e com os dois preenchidos a lista vem vazia.

◽ **estado:** `gravando`, `salvando`, `baixando`, `pronta` ou `falhou`. É o estado do vídeo, não o da IA: uma gravação `pronta` pode ter a IA com falha.

◽ **busca:** procura no que foi falado na chamada, no nome dos participantes, no título da conversa e no nome do contato.

◽ Filtro deixado vazio, ou com um valor fora dos aceitos, é ignorado — a lista vem sem aquele filtro.

◽ Cada gravação vem com o **id**, a duração em segundos, quem gravou, os participantes e a **origem**: com `tipo` `atendimento`, o `ticketId` e o contato; com `tipo` `chat`, o `chatId` e o título da conversa.

◽ A lista não traz a transcrição. Em **ia**, `temTranscricao` e `temAnalise` dizem se a gravação tem cada uma, e `estado` mostra em que ponto a IA está: `pendente`, `processando`, `pronta` ou `falhou`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/gravacoes?pageNumber={pageNumber}&de={dataInicio}&ate={dataFim}&origem={origemDaGravacao}&ticketId={ticketId}&chatId={chatId}&estado={estadoDaGravacao}&busca={busca}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token da Empresa
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X GET 'https://api2.chatmasterveloz.com/api/gravacoes?pageNumber={pageNumber}&de={dataInicio}&ate={dataFim}&origem={origemDaGravacao}&ticketId={ticketId}&chatId={chatId}&estado={estadoDaGravacao}&busca={busca}' -H 'Authorization: Bearer {seutokenaqui}'
```
