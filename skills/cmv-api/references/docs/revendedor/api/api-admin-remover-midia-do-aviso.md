# API Remover Mídia do Aviso

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-remover-midia-do-aviso
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Avisos › API Remover Mídia do Aviso

---

🧩 Tira **a imagem ou o arquivo** de um aviso.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/announcements/media-upload
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

◽ Diferente da troca, esta chamada **apaga o arquivo do armazenamento** e limpa o registro no aviso.

◽ As telas são avisadas na hora.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/announcements/media-upload',
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
curl -X DELETE 'https://api2.chatmasterveloz.com/api/announcements/media-upload' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"id":5}'
```
