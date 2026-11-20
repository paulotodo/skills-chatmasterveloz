# API Atualizar Contato

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-contato
- **Categoria:** APIs
- **Menu:** APIs › Contatos › API Atualizar Contato

---

🧩 Atualiza **um contato** da sua empresa pelo ID.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/contact/update
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
    "id": "31",
    "name": "José Silva",
    "number": "5511955892164",
    "email": "email@email.com",
    "cpfcnpj": "000.111.222-33",
    "genero": "masculino",
    "estado": "SP",
    "cidade": "São Paulo",
    "referencia": "indicado por Lucas",
    "aniversario": "1982-11-20T07:52",
    "endereco": "Av Principal 987",
    "carteiraId": "",
    "acceptAudioMessage": true,
    "active": true,
    "disableBot": false,
    "compartilhado": false,
    "promptId": null,
    "extraInfo": [
        {
            "name": "Tamanho",
            "value": "1,80 m"
        },
        {
            "name": "Peso",
            "value": "90 kg"
        }
    ]
}
```

➡️ **“id”:** ID do contato cadastrado na plataforma.

⚠️ **O exemplo acima traz tudo o que a chamada aceita, para você escolher** — não é obrigatório enviar inteiro. Os campos que você não enviar ficam como estão.

➡️ **“name”, “email”, “cpfcnpj”, “genero”, “estado”, “cidade”, “endereco”:** dados gerais do contato, de preenchimento livre.

➡️ **“number”:** telefone do contato no formato ddi ddd numero (somente números).

➡️ **“referencia”:** quem indicou o contato.

➡️ **“aniversario”:** data de nascimento no formato ANO-MES-DIA(letra T)HORA:MINUTO — por exemplo, `1982-11-20T07:52`.

➡️ **“carteiraId”:** ID do atendente dono da carteira, quando o recurso estiver habilitado. Deixe vazio ou `null` para não usar.

➡️ **“acceptAudioMessage”:** `true` se o contato aceita receber áudio.

➡️ **“active”:** `false` bloqueia o contato.

➡️ **“disableBot”:** `true` desliga o robô para este contato.

➡️ **“compartilhado”:** `true` faz o contato aparecer para todos na lista de **Enviar contato**.

➡️ **“promptId”:** ID do prompt de IA ligado ao contato.

➡️ **“extraInfo”:** campos adicionais do contato, em pares de `name` e `value`. Repita o par para cada informação extra.

⚠️ **O `extraInfo` substitui o conjunto inteiro.** O que não vier na lista é apagado — para não mexer nos campos extras, não envie o campo.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/contact/update',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "id": "31",
    "name": "José Silva",
    "number": "5511955892164",
    "email": "email@email.com",
    "cpfcnpj": "000.111.222-33",
    "genero": "masculino",
    "estado": "SP",
    "cidade": "São Paulo",
    "referencia": "indicado por Lucas",
    "aniversario": "1982-11-20T07:52",
    "endereco": "Av Principal 987",
    "carteiraId": "",
    "acceptAudioMessage": true,
    "active": true,
    "disableBot": false,
    "compartilhado": false,
    "promptId": null,
    "extraInfo": [
        {
            "name": "Tamanho",
            "value": "1,80 m"
        },
        {
            "name": "Peso",
            "value": "90 kg"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/contact/update' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"id":"31","name":"José Silva","number":"5511955892164","email":"email@email.com","cpfcnpj":"000.111.222-33","genero":"masculino","estado":"SP","cidade":"São Paulo","referencia":"indicado por Lucas","aniversario":"1982-11-20T07:52","endereco":"Av Principal 987","carteiraId":"","acceptAudioMessage":true,"active":true,"disableBot":false,"compartilhado":false,"promptId":null,"extraInfo":[{"name":"Tamanho","value":"1,80 m"},{"name":"Peso","value":"90 kg"}]}'
```
