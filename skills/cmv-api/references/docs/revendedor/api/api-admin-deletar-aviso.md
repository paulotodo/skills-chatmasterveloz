# API Deletar Aviso

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-deletar-aviso
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Avisos › API Deletar Aviso

---

🧩 Apaga **um aviso**.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/announcements
```

##### Método

```
DELETE
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "id": 5
}
```

➡️ **“id”:** ID do aviso. **Obrigatório.**

⚠️ **Não há como desfazer.** Não existe lixeira de avisos.

⚠️ **A mídia anexada NÃO é apagada do armazenamento.** Para não deixar arquivo órfão, tire a mídia antes de apagar o aviso.

◽ As telas recebem o aviso da remoção.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/announcements',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
  CURLOPT_POSTFIELDS =>'{
    "id": 5
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/announcements' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"id":5}'
```
