# API Anexar Mídia ao Aviso

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-anexar-midia-ao-aviso
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Avisos › API Anexar Mídia ao Aviso

---

🧩 Anexa **uma imagem ou arquivo** a um aviso.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/announcements/media-upload
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

```php
array(
    'id' => 5,
    'file' => new CURLFile('/caminho/banner.png')
  )
```

➡️ **“id”:** ID do aviso. **Obrigatório.**

➡️ **“file”:** o arquivo, de qualquer tipo, até **50 MB**. **Obrigatório.**

◽ Se mandar mais de um, só o primeiro é usado.

⚠️ **A mídia nova substitui a anterior no aviso, mas o arquivo antigo continua guardado** — ele não é apagado do armazenamento.

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
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => array(
    'id' => 5,
    'file' => new CURLFile('/caminho/banner.png')
  ),
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
