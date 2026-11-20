# API Atualizar Configurações da Empresa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-configuracoes-da-empresa
- **Categoria:** APIs
- **Menu:** APIs › Extras › API Atualizar Configurações da Empresa

---

🧩 Atualiza uma ou várias **Configurações da empresa**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}/settings
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
    "settings": {
        "userRating": "enabled",
        "timezone": "America/Sao_Paulo"
    }
}
```

➡️ **“companyId”:** ID da **sua** empresa — vai no próprio endereço, no lugar de `{companyId}`. **Obrigatório.**

◽ O id da sua empresa aparece no campo `companyId` das respostas das outras chamadas.

➡️ **“settings”:** as chaves a gravar, como pares de chave e valor. Aceita também a forma em lista: `[{ "key": "userRating", "value": "enabled" }]`.

◽ Para uma chave só, dá para mandar `key` e `value` soltos no corpo, sem o `settings`.

◽ O valor pode ser texto, número ou sim/não — tudo é gravado como texto.

⚠️ **A chave é livre: uma que não existe é criada, sem erro.** Um nome digitado errado não falha — cria uma configuração inútil em silêncio. A resposta marca `criada` em cada chave nova: confira esse campo.

⚠️ **É tudo ou nada.** A conferência de todas as chaves acontece antes da primeira gravação: se uma estiver errada, nenhuma é gravada.

◽ Ao gravar o fuso horário, a mudança vale na hora.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}/settings',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "settings": {
        "userRating": "enabled",
        "timezone": "America/Sao_Paulo"
    }
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/companies/{companyId}/settings' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"settings":{"userRating":"enabled","timezone":"America/Sao_Paulo"}}'
```
