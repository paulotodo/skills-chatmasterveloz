# API Listar Mesas e Comandas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-mesas-e-comandas
- **Categoria:** APIs
- **Menu:** APIs › PDV › API Listar Mesas e Comandas

---

🧩 Obter a **lista de mesas e comandas** do PDV da sua empresa, com a conta aberta de cada uma.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/pdv/mesas?tipo={tipoDaMesa}&ativa={mesaAtiva}
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

◽ **tipo:** `mesa` para só as mesas, ou `comanda` para só as comandas.

◽ **ativa:** `true` para só as ativas, ou `false` para só as desativadas no **Configurar** do menu **PDV  ›  Mesas e Comandas**. Sem esse filtro, vêm as ativas e as desativadas.

◽ Valor fora desses é recusado. Filtro enviado vazio, como `tipo=`, é ignorado.

➡️ **As mesas e as comandas vêm juntas, na ordem da tela.** Cada uma traz o `id`, o `nome`, o `numero`, o `tipo` (`mesa` ou `comanda`), o `ativa` e a `contaAberta`.

◽ O `id` é o `mesaId` das reservas de mesa.

◽ O `numero` vem `null` quando a mesa não tem número.

◽ A `contaAberta` traz a conta aberta agora na mesa: o `id`, a `situacao`, o `abertaEm`, o `contaPedidaEm` e o `fechadaEm`. Com a mesa livre, vem `null`.

◽ Os horários da conta vêm em UTC, com o `Z` no fim.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/pdv/mesas?tipo={tipoDaMesa}&ativa={mesaAtiva}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/pdv/mesas?tipo={tipoDaMesa}&ativa={mesaAtiva}' -H 'Authorization: Bearer {seutokenaqui}'
```
