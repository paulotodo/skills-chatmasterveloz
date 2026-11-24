# API Criar Conexão em uma Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-criar-conexao-em-uma-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Conexões › API Criar Conexão em uma Empresa

---

🧩 Cria **uma conexão de WhatsApp dentro de uma empresa**, já ligada aos Setores dela. É o passo que falta na empresa recém-criada: sem conexão, o token dela não fala com a API.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}/whatsapps
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
    "name": "Loja X - Vendas",
    "queueIds": [12, 13],
    "greetingMessage": "Olá! Escolha uma opção:",
    "token": "",
    "webhook": null
}
```

➡️ **“companyId”:** ID da empresa — vai no próprio endereço, no lugar de `{companyId}`. **Obrigatório.**

➡️ **“name”:** nome da conexão. Precisa ser único em **toda a instalação**, não só na empresa. **Obrigatório.**

➡️ **“queueIds”:** IDs dos Setores da empresa ligados à conexão, em array.

➡️ **“greetingMessage”:** mensagem de saudação. **Obrigatória quando a conexão tem mais de um Setor.**

➡️ **“token”:** defina um token para a conexão, ou deixe `""` para a plataforma gerar.

➡️ **“webhook”:** `null`, ou a URL do webhook da conexão.

➡️ **“webhookb”:** `null`, ou a URL do segundo webhook.

◽ Só WhatsApp: os outros canais precisam ser autorizados na tela do próprio canal.

◽ A conexão nasce **desconectada** — o pareamento vem depois, pelo QR Code ou pelo painel.

◽ A primeira conexão da empresa vira a conexão padrão dela.

⚠️ **O limite de conexões do plano vale aqui**, e é conferido antes de abrir a sessão.

◽ Setor que não é da empresa informada é recusado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}/whatsapps',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "name": "Loja X - Vendas",
    "queueIds": [12, 13],
    "greetingMessage": "Olá! Escolha uma opção:",
    "token": "",
    "webhook": null
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
curl -X POST 'https://api2.chatmasterveloz.com/api/companies/{companyId}/whatsapps' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"Loja X - Vendas","queueIds":[12,13],"greetingMessage":"Olá! Escolha uma opção:","token":"","webhook":null}'
```
