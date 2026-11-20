# API Criar Tag

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-tag
- **Categoria:** APIs
- **Menu:** APIs › Tags › API Criar Tag

---

🧩 Cria **uma tag** no cadastro da empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tags
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
    "name": "Orçamento enviado",
    "color": "#0a84ff",
    "tagType": "Atendimento",
    "kanban": 0,
    "prioridade": 0,
    "active": true,
    "conversao": ""
}
```

➡️ **“name”:** nome da tag, com pelo menos 3 caracteres e único na empresa. **Obrigatório.**

◽ A comparação ignora maiúsculas e espaços nas pontas: `Suporte`, `suporte` e `Suporte ` são a mesma tag.

➡️ **“color”:** cor da tag, em hexadecimal.

➡️ **“kanban”:** `1` faz a tag virar **coluna do Kanban**; `0` deixa a tag comum. Sem ele, `0`.

➡️ **“prioridade”:** ordem da coluna no Kanban, do menor para o maior. Sem ele, `0`.

➡️ **“tagType”:** tipo da tag — `Atendimento`, `Encerramento` ou `CRM`. Sem ele, a tag nasce como `Atendimento`.

◽ O tipo não é conferido: o que você mandar é gravado como está, e um tipo inventado deixa a tag fora das telas que filtram por tipo.

➡️ **“active”:** `false` cria a tag já inativa. Sem ele, a tag nasce ativa.

➡️ **“conversao”:** nome do evento de conversão que o Pixel dispara quando a tag entra num atendimento.

◽ Só tem efeito com o Pixel configurado no painel.

◽ A tag nasce pública — todo operador a enxerga.

◽ Campos fora desta lista não são gravados.

◽ Criar a tag não a coloca em atendimento nenhum.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tags',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "name": "Orçamento enviado",
    "color": "#0a84ff",
    "tagType": "Atendimento",
    "kanban": 0,
    "prioridade": 0,
    "active": true,
    "conversao": ""
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tags' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"Orçamento enviado","color":"#0a84ff","tagType":"Atendimento","kanban":0,"prioridade":0,"active":true,"conversao":""}'
```
