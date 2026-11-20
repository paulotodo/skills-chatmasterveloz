# API Listar Fluxos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-fluxos
- **Categoria:** APIs
- **Menu:** APIs › Fluxos › API Listar Fluxos

---

🧩 Listar **fluxos** do Flowbuilder da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/flowbuilder
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

◽ Cada fluxo vem com o id, o nome, a categoria, quem criou e se está ativo — **sem** o desenho dos blocos, que é a parte pesada.

◽ Serve para montar um seletor e guardar o id do fluxo que outra chamada vai pedir.

◽ A categoria vem vazia quando o fluxo não tem nenhuma, e o autor vem vazio quando não dá para saber quem criou.

◽ A lista vem ordenada por nome.

◽ Só leitura: esta chamada não cria, não edita e não dispara fluxo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/flowbuilder',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/flowbuilder' -H 'Authorization: Bearer {seutokenaqui}'
```
