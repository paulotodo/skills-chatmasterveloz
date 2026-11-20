# API Atualizar Configurações de Campanha

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-configuracoes-de-campanha
- **Categoria:** APIs
- **Menu:** APIs › Campanhas › API Atualizar Configurações de Campanha

---

🧩 Atualiza as **configurações de disparo das Campanhas** — só o que vier no corpo muda.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/companies/{companyId}/campaign-settings
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
    "messageInterval": 400,
    "longerIntervalAfter": 10,
    "greaterInterval": 1000,
    "variables": [
        {
            "key": "saudacao",
            "value": "Bom dia"
        }
    ]
}
```

➡️ **“companyId”:** ID da empresa — vai no próprio endereço, no lugar de `{companyId}`. **Obrigatório.**

➡️ **“messageInterval”:** intervalo entre uma mensagem e a seguinte, em milissegundos. Padrão `400`.

➡️ **“longerIntervalAfter”:** de quantas em quantas mensagens entra o intervalo maior — o tamanho do lote. Padrão `10`.

➡️ **“greaterInterval”:** o intervalo maior, aplicado ao fim de cada lote, em milissegundos. Padrão `1000`.

➡️ **“variables”:** as variáveis da campanha, em pares de `key` e `value`. A `key` não se repete.

◽ As chaves podem vir soltas no corpo, como no exemplo, ou dentro de um `settings` — que é o formato da tela.

◽ O que você não enviar fica como está, e a resposta diz o que passou a valer.

⚠️ **Cada valor é conferido antes de gravar, e por um bom motivo:** um número fora do formato faria a campanha **parar de enviar**. Os intervalos precisam ser inteiros de `0` para cima, e o lote, inteiro de `1` para cima.

◽ Sem nenhuma chave conhecida, a chamada é recusada. O que não é configuração de campanha volta em `camposIgnorados` e não é gravado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/companies/{companyId}/campaign-settings',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "messageInterval": 400,
    "longerIntervalAfter": 10,
    "greaterInterval": 1000,
    "variables": [
        {
            "key": "saudacao",
            "value": "Bom dia"
        }
    ]
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
curl -X PUT 'https://api2.chatmasterveloz.com/api/companies/{companyId}/campaign-settings' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"messageInterval":400,"longerIntervalAfter":10,"greaterInterval":1000,"variables":[{"key":"saudacao","value":"Bom dia"}]}'
```
