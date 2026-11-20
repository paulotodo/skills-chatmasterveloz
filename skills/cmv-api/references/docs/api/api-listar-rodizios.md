# API Listar Rodízios

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-rodizios
- **Categoria:** APIs
- **Menu:** APIs › Rodízios › API Listar Rodízios

---

🧩 Obter a **lista de rodízios** cadastrados na empresa, em ordem de nome.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/rodizios
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

◽ Cada rodízio vem com o **id**, o nome, se está ativo, o ciclo da contagem, o Setor de transbordo e quantos participantes tem.

◽ É deste `id` que a chamada de distribuir um atendimento precisa.

◽ A chamada é só de leitura: nada é alterado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/rodizios',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/rodizios' -H 'Authorization: Bearer {seutokenaqui}'
```
