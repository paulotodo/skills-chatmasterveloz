# API Listar Noites Livres da Diária

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-noites-livres-da-diaria
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Listar Noites Livres da Diária

---

🧩 Obter as **noites livres** de uma oferta por diária num período e, com a entrada e a saída, conferir uma estadia antes de reservar.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/diarias?ofertaId={ofertaId}&de={dataInicio}&ate={dataFim}
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

◽ **ofertaId:** a oferta por diária. **Obrigatório.** Oferta por horário é recusada.

◽ **de** e **ate:** o período, no formato `AAAA-MM-DD`, de até 62 dias. Sem as datas, de hoje a 41 dias à frente.

◽ Para conferir uma estadia, acrescente `&entrada=AAAA-MM-DD&saida=AAAA-MM-DD`.

◽ Também filtram: **recursoId**, **pessoas** e `comoCliente=true`, que aplica a antecedência e o limite de dias à frente da página de reservas.

➡️ **A resposta traz as noites livres do período.** Com a entrada e a saída, traz também a `estadia`: as `noites`, o `preco` total, o `sinal` e os `recursoIds` livres.

◽ Estadia que não serve, como uma com mais noites do que a oferta aceita, vem com o `motivo`, que é o mesmo da recusa ao reservar.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/diarias?ofertaId={ofertaId}&de={dataInicio}&ate={dataFim}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/diarias?ofertaId={ofertaId}&de={dataInicio}&ate={dataFim}' -H 'Authorization: Bearer {seutokenaqui}'
```
