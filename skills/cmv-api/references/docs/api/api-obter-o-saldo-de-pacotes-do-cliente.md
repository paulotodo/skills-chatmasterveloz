# API Obter o Saldo de Pacotes do Cliente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-o-saldo-de-pacotes-do-cliente
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Obter o Saldo de Pacotes do Cliente

---

🧩 Obter **os pacotes de um cliente** nas Reservas, com o crédito que sobra em cada um.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/pacotes-dos-clientes?telefone={number}
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

◽ **telefone:** o telefone do cliente; só os números contam. No lugar dele, **contactId**, o contato do cliente. Um dos dois é **obrigatório**.

◽ **ofertaId:** só os pacotes que cobrem esta oferta.

◽ Sem mais nada, vêm só os pacotes ativos. Para ver também os esgotados, os vencidos e os cancelados, acrescente `&todos=true`.

➡️ **A resposta traz `total`, `restantes` e `pacotes`**, os mais novos primeiro.

◽ `restantes`: a soma do crédito dos pacotes ativos.

◽ Cada pacote traz `id`, `nome`, `quantidade`, `usadas`, `restantes`, `validoAte`, `estado` (`ativo`, `esgotado`, `vencido` ou `cancelado`) e as `ofertaIds` que cobre.

◽ Para a reserva usar o pacote, mande o `id` dele como `pacoteClienteId` na chamada de criar a reserva.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/pacotes-dos-clientes?telefone={number}',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/pacotes-dos-clientes?telefone={number}' -H 'Authorization: Bearer {seutokenaqui}'
```
