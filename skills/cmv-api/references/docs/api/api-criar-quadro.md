# API Criar Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de Atendimentos › API Criar Quadro

---

🧩 Cria **um quadro de atendimentos**, já com as duas colunas fixas: Pendentes e Atendendo.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros
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

```javascript
{
    "nome": "Comercial",
    "nomeAtendendo": "Em atendimento"
}
```

➡️ **“nome”:** o nome do quadro. **Obrigatório.**

➡️ **“nomeAtendendo”:** opcional. O nome da coluna **Atendendo**, a dos atendimentos aceitos. Sem ele, fica *Atendendo*.

◽ A coluna **Pendentes** vem com esse nome, que não muda.

➡️ **A resposta traz o quadro com o `id`** e as duas colunas, cada uma com o seu `id`.

◽ O quadro novo só aparece para um atendente depois de atribuído a ele. Administrador e supervisor veem todos os quadros.

◽ Configurar o quadro é do administrador e do supervisor. Sem `userId`, quem faz é a empresa; para fazer em nome de uma pessoa, acrescente `?userId=` com o ID dela ao endereço — o de um atendente é recusado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Comercial",
    "nomeAtendendo": "Em atendimento"
}',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/ticket-quadros' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Comercial","nomeAtendendo":"Em atendimento"}'
```
