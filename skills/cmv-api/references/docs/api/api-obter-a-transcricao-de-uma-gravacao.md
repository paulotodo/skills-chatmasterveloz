# API Obter a Transcrição de uma Gravação

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-a-transcricao-de-uma-gravacao
- **Categoria:** APIs
- **Menu:** APIs › Gravações › API Obter a Transcrição de uma Gravação

---

🧩 Obter **a transcrição de uma gravação**, em texto, em JSON ou como legenda.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}/transcricao?formato={formatoDaTranscricao}
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

➡️ Esta chamada não tem payload. O formato vai como **query** na URL.

➡️ **“gravacaoId”:** ID da gravação.

➡️ **“formato”:** `texto`, `json` ou `vtt`. Sem informar, vem `texto`; outro valor é recusado.

◽ `texto`: o texto puro, um trecho por linha com o tempo — `[00:04] …` —, como vai para a conversa.

◽ `json`: a `transcricao` e os `trechos`, cada fala com `inicio` e `fim` em segundos, `quem` falou e o `texto`.

◽ `vtt`: a legenda do vídeo no formato WebVTT.

◽ Gravação ainda sem transcrição é recusada: a IA está na fila, falhou ou não foi pedida.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}/transcricao?formato={formatoDaTranscricao}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}/transcricao?formato={formatoDaTranscricao}' -H 'Authorization: Bearer {seutokenaqui}'
```
