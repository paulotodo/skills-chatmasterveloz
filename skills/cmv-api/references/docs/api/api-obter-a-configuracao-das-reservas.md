# API Obter a Configuração das Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-obter-a-configuracao-das-reservas
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Obter a Configuração das Reservas

---

🧩 Obter a **configuração das Reservas** da sua empresa: o fuso, a grade da agenda, as regras da página de reservas e as situações da reserva.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/config
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

➡️ **A resposta traz a configuração que a integração precisa para reservar.**

◽ `fuso`: o fuso da empresa, como `America/Sao_Paulo`. As datas e as horas das Reservas seguem esse fuso.

◽ `passoMinutos`: de quantos em quantos minutos a agenda oferece os horários, como `15`.

◽ `paginaNoAr`: `true` quando a página de reservas está no ar.

◽ `comoCliente`: as regras da página de reservas — `antecedenciaMinutos`, `horizonteDias` (os dias à frente), `cancelamentoAteHoras`, `confirmacaoAutomatica` e `sinalObrigatorio`.

◽ `modos`: os tipos de oferta, `horario`, `diaria` e `turma`.

◽ `situacoes` e `transicoes`: as situações da reserva e para onde cada uma pode ir. A `pendente` vai para `confirmada` ou `cancelada`; a `confirmada`, para `concluida`, `nao_compareceu` ou `cancelada`; as outras não mudam mais.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/config',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/reservas/config' -H 'Authorization: Bearer {seutokenaqui}'
```
