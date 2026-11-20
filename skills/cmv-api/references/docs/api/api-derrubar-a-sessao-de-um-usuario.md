# API Derrubar a Sessão de um Usuário

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-derrubar-a-sessao-de-um-usuario
- **Categoria:** APIs
- **Menu:** APIs › Equipe › API Derrubar a Sessão de um Usuário

---

🧩 Tira **um usuário do painel** na hora, encerrando a sessão dele em todas as abas e aparelhos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/users/{userId}/force-logout
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

➡️ **“userId”:** o ID ou o e-mail do usuário — vai no próprio endereço, no lugar de `{userId}`. **Obrigatório.**

➡️ Esta chamada não tem payload.

◽ Todo login da pessoa deixa de valer na hora. As abas abertas vão para a tela de entrar, com o aviso de que a sessão foi encerrada, e o status dela vira `offline`.

⚠️ **Isto não é bloqueio.** A pessoa entra de novo normalmente, com a mesma senha. Para impedir o acesso, o caminho é inativar o usuário.

◽ O webhook de status da empresa é avisado, com a marca de que a sessão foi derrubada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/users/{userId}/force-logout',
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
curl -X POST 'https://api2.chatmasterveloz.com/api/users/{userId}/force-logout' -H 'Authorization: Bearer {seutokenaqui}'
```
