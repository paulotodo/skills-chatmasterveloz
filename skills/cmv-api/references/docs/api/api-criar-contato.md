# API Criar Contato

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-contato
- **Categoria:** APIs
- **Menu:** APIs › Contatos › API Criar Contato

---

🧩 Cria **um contato** na sua empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/contacts
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

➡️ **“name”, “email”, “cpfcnpj”, “genero”, “estado”, “cidade”, “endereco”:** dados gerais do contato, de preenchimento livre.

➡️ **“number”:** telefone do contato no formato ddi ddd numero (somente números).

➡️ **“referencia”:** quem indicou o contato.

➡️ **“aniversario”:** data de nascimento no formato ANO-MES-DIA(letra T)HORA:MINUTO — por exemplo, `1982-11-20T07:52`.

➡️ **“carteiraId”:** ID do atendente dono da carteira, quando o recurso estiver habilitado. Deixe vazio ou `null` para não usar.

➡️ **“isValid”:** `true` marca o número como confirmado no WhatsApp. A chamada não confere nada — quem afirma é você.

➡️ **“acceptAudioMessage”:** `true` se o contato aceita receber áudio.

➡️ **“active”:** `false` cria o contato já inativo.

➡️ **“promptId”:** ID do prompt de IA ligado ao contato.

➡️ **“extraInfo”:** campos adicionais do contato, em pares de `name` e `value`. Repita o par para cada informação extra.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/contacts',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
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
curl -X POST 'https://api2.chatmasterveloz.com/api/contacts' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"name":"José Silva","number":"5511955892164","email":"email@email.com","cpfcnpj":"000.111.222-33","genero":"masculino","estado":"SP","cidade":"São Paulo","referencia":"indicado por Lucas","aniversario":"1982-11-20T07:52","endereco":"Av Principal 987","carteiraId":"","extraInfo":[{"name":"Tamanho","value":"1,80 m"},{"name":"Peso","value":"90 kg"}]}'
```
