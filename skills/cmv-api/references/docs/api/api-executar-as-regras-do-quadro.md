# API Executar as Regras do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-executar-as-regras-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de Atendimentos › API Executar as Regras do Quadro

---

🧩 Aplica **as regras do quadro agora** nos atendimentos abertos, como o botão **Executar regras agora** da tela.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras/executar
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

◽ O `quadroId` vai no próprio endereço: é o `id` do quadro.

◽ Entram os atendimentos abertos, com atendente, de quem tem o quadro atribuído. Os que estão em **Aguardando** ficam de fora.

◽ A resposta diz o que aconteceu: `avaliados` e `movidos` (quantos atendimentos), `usuariosNoQuadro` (quantas pessoas têm o quadro atribuído) e `limitado`.

◽ `limitado` em `true`: só os atendimentos mais recentes foram avaliados. Os demais continuam sendo organizados quando o cliente escrever.

◽ Com `usuariosNoQuadro` em `0`, nada é avaliado: ninguém tem o quadro atribuído.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras/executar',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/regras/executar' -H 'Authorization: Bearer {seutokenaqui}'
```
