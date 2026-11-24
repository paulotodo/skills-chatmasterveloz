# API Criar Tag em uma Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-criar-tag-em-uma-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Tags › API Criar Tag em uma Empresa

---

🧩 Cria **uma tag no cadastro de uma empresa**, sem precisar entrar nela.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

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
    "companyId": 7,
    "name": "Orçamento enviado",
    "color": "#0a84ff",
    "tagType": "Atendimento",
    "kanban": 0,
    "prioridade": 0,
    "active": true,
    "conversao": ""
}
```

➡️ **“companyId”:** ID da empresa em que o registro é criado. **É ele que faz a chamada valer para outra empresa** — sem ele, vale a empresa do próprio token.

➡️ **“name”:** nome da tag, com pelo menos 3 caracteres e único naquela empresa. **Obrigatório.**

◽ A comparação ignora maiúsculas e espaços nas pontas: `Suporte`, `suporte` e `Suporte ` são a mesma tag.

➡️ **“color”:** cor da tag, em hexadecimal.

➡️ **“tagType”:** tipo da tag — `Atendimento`, `Encerramento` ou `CRM`. Sem ele, nasce como `Atendimento`.

◽ O tipo não é conferido: o que você mandar é gravado como está, e um tipo inventado deixa a tag fora das telas que filtram por tipo.

➡️ **“kanban”:** `1` faz a tag virar **coluna do Kanban**. **“prioridade”:** a ordem dessa coluna.

➡️ **“active”:** `false` cria a tag já inativa.

➡️ **“conversao”:** nome do evento de conversão que o Pixel dispara quando a tag entra num atendimento.

◽ A tag nasce pública — todo operador daquela empresa a enxerga.

◽ Criar a tag não a coloca em atendimento nenhum.

◽ Empresa que não existe é recusada.

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
    "companyId": 7,
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tags' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"companyId":7,"name":"Orçamento enviado","color":"#0a84ff","tagType":"Atendimento","kanban":0,"prioridade":0,"active":true,"conversao":""}'
```
