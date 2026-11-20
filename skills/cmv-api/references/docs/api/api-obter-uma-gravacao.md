# API Obter uma Gravação

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-uma-gravacao
- **Categoria:** APIs
- **Menu:** APIs › Gravações › API Obter uma Gravação

---

🧩 Obter **uma gravação**, com a transcrição, as falas e a análise da IA.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}
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

➡️ **“gravacaoId”:** ID da gravação.

◽ Além do que vem na lista, traz a **transcricao** (um trecho por linha, com o tempo — `[00:04] …`), os **trechos** (cada fala com `inicio` e `fim` em segundos, `quem` falou e o `texto`) e a **analise**.

◽ O `quem` vem `null` quando não se sabe quem falou.

◽ **endereco** é o link do arquivo da gravação.

◽ Quando a IA falhou, o motivo vem em **iaErro** — por exemplo, `transcrição vazia`, quando não houve fala na chamada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}' -H 'Authorization: Bearer {seutokenaqui}'
```
