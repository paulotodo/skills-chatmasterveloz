# API Trocar Imagens da Plataforma

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-trocar-imagens-da-plataforma
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Configurações › API Trocar Imagens da Plataforma

---

🧩 Troca o **logotipo, o fundo ou o favicon** da plataforma.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/settings/media-upload?ref=login
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
    'file' => new CURLFile('/caminho/logotipo.png')
  )
```

➡️ **“file”:** a imagem, em PNG. **Obrigatório.**

◽ Se mandar mais de uma, só a primeira é usada.

➡️ **“ref”:** o destino da imagem, que vai na **query da URL**. **Obrigatório.**

◽ Os destinos que o painel usa: `signup` (tela de registro), `login`, `interno` e `interno-dark` (logotipo do painel), `bg` (fundo), `favicon-32x32`, `favicon-256x256` e `apple-touch-icon`.

⚠️ **O `ref` precisa ir na query da URL, e não no formulário.** O nome do arquivo é decidido antes de a chamada ser processada: mandando o `ref` só no formulário, a imagem é gravada com um nome inválido e não aparece em lugar nenhum. A chamada responde sucesso assim mesmo.

◽ O destino vira o nome do arquivo, e a imagem **substitui** a que estava lá. O nome não é conferido contra a lista: um destino inventado grava um arquivo que nada exibe.

◽ A troca vale para a plataforma inteira, não para uma empresa.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/settings/media-upload?ref=login',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => array(
    'file' => new CURLFile('/caminho/logotipo.png')
  ),
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer {seutokenaqui}' //Token cadastrado na conexão
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
