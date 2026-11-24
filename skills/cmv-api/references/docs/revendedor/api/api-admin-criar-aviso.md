# API Criar Aviso

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-criar-aviso
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Avisos › API Criar Aviso

---

🧩 Cria **um aviso** — o comunicado que aparece no sino do painel.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/announcements
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
    "title": "Manutenção programada",
    "text": "<p>Sistema indisponível das 02h às 04h.</p>",
    "priority": 1,
    "status": true,
    "visibility": "all",
    "scope": "global"
}
```

➡️ **“title”:** título do aviso. **Obrigatório.**

➡️ **“text”:** o conteúdo. Aceita HTML.

➡️ **“priority”:** `1` alta, `2` média, `3` baixa.

➡️ **“status”:** `true` exibe o aviso, `false` o deixa guardado.

➡️ **“visibility”:** quem vê o aviso. Padrão `all`.

➡️ **“youtubeUrl”:** endereço de um vídeo do YouTube. Mande `null` para tirar.

➡️ **“scope”:** `global` mostra o aviso em todas as empresas; `company` mostra só na empresa de `companyId`.

➡️ **“companyId”:** a empresa alvo, quando o `scope` é `company`. Sem ele, vale a empresa da conexão do token.

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
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "title": "Manutenção programada",
    "text": "<p>Sistema indisponível das 02h às 04h.</p>",
    "priority": 1,
    "status": true,
    "visibility": "all",
    "scope": "global"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/announcements' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"title":"Manutenção programada","text":"<p>Sistema indisponível das 02h às 04h.</p>","priority":1,"status":true,"visibility":"all","scope":"global"}'
```
