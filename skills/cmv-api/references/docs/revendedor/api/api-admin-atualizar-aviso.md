# API Atualizar Aviso

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-atualizar-aviso
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Avisos › API Atualizar Aviso

---

🧩 Atualiza **um aviso** — só o que vier no corpo muda.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/announcements
```

##### Método

```
PUT
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "id": 5,
    "title": "Manutenção adiada",
    "text": "<p>A manutenção passou para sábado.</p>",
    "priority": 2,
    "status": true,
    "visibility": "all",
    "youtubeUrl": null,
    "scope": "company",
    "companyId": 7
}
```

➡️ **“id”:** ID do aviso. **Obrigatório.**

➡️ **“title”:** título do aviso. **Obrigatório.**

➡️ **“text”:** o conteúdo. Aceita HTML.

➡️ **“priority”:** `1` alta, `2` média, `3` baixa.

➡️ **“status”:** `true` exibe o aviso, `false` o deixa guardado.

➡️ **“visibility”:** quem vê o aviso. Padrão `all`.

➡️ **“youtubeUrl”:** endereço de um vídeo do YouTube. Mande `null` para tirar.

➡️ **“scope”:** `global` mostra o aviso em todas as empresas; `company` mostra só na empresa de `companyId`.

➡️ **“companyId”:** a empresa alvo, quando o `scope` é `company`. Sem ele, vale a empresa da conexão do token.

⚠️ **O `title` é obrigatório em toda edição**, mesmo quando não é ele que você está mudando. Sem o título, a chamada é recusada.

◽ Só os campos presentes no corpo mudam; mandar `null` num campo o deixa vazio.

◽ Vale para aviso de qualquer empresa.

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
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "id": 5,
    "title": "Manutenção adiada",
    "text": "<p>A manutenção passou para sábado.</p>",
    "priority": 2,
    "status": true,
    "visibility": "all",
    "youtubeUrl": null,
    "scope": "company",
    "companyId": 7
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/announcements' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"id":5,"title":"Manutenção adiada","text":"<p>A manutenção passou para sábado.</p>","priority":2,"status":true,"visibility":"all","youtubeUrl":null,"scope":"company","companyId":7}'
```
