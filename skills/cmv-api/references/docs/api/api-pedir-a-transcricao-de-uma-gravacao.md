# API Pedir a Transcrição de uma Gravação

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-pedir-a-transcricao-de-uma-gravacao
- **Categoria:** APIs
- **Menu:** APIs › Gravações › API Pedir a Transcrição de uma Gravação

---

🧩 Pede **a transcrição de uma gravação** à IA, quando ela ainda não foi transcrita ou a IA falhou.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}/transcrever
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

```
// sem payload
```

➡️ Esta chamada não tem payload.

➡️ **“gravacaoId”:** ID da gravação.

◽ Vale para gravação **pronta**. Gravação já transcrita é recusada: transcrever de novo repetiria a transcrição na conversa.

◽ A IA faz o que está escolhido em **IA nas gravações das chamadas**, no menu **Configurações  ›  Opções  ›  Chamadas**, seção **Chamadas** — a transcrição com as legendas, a análise ou as duas —, e o resultado vai para a conversa de onde a chamada veio. Com a opção **Desligada**, o pedido é recusado.

◽ A resposta traz o `iaEstado` `pendente`: a gravação entrou na fila. Pedir de novo enquanto ela está na fila não muda nada — a resposta só devolve o estado.

◽ Para saber quando terminou, consulte a gravação: o `ia.estado` passa de `pendente` a `processando` e fica `pronta` ou `falhou`, com o motivo em `iaErro`. O webhook também avisa, com o evento `gravacao-transcrita` ou `gravacao-ia-falhou`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}/transcrever',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/gravacoes/{gravacaoId}/transcrever' -H 'Authorization: Bearer {seutokenaqui}'
```
