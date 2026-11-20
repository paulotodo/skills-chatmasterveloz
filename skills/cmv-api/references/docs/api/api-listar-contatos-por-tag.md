# API Listar Tickets por Tag

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-contatos-por-tag
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Listar Tickets por Tag

---

🧩 Listar os **Tickets** que têm uma tag.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/contacts/findbytag
```

##### Método

```
GET
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```javascript
{
    "tagid":"56"
}
```

➡️ **“tagid”:** ID da Tag. **Obrigatório.**

◽ Para mais de uma, use uma lista: `"tagid": [56,47]`. O Ticket entra se tiver **qualquer** uma delas.

⚠️ **Sem o `tagid`, a chamada devolve TODOS os Tickets da empresa** — sem páginas e sem teto. Numa base grande, é uma resposta enorme de uma vez só.

◽ A tag é procurada em três lugares: a tag posta no Ticket, a tag de **Encerramento** escolhida ao encerrar e a tag de **CRM** da oportunidade ligada ao Ticket.

◽ Cada Ticket vem com o contato, o Setor, o operador, a conexão e as tags dele.

◽ Oportunidade que não está ligada a Ticket nenhum não aparece nesta lista.

◽ A lista vem inteira, do Ticket mexido mais recentemente para o mais antigo.

◽ Repare que é um `GET` que lê o filtro no **corpo**, e não na URL.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/contacts/findbytag',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_POSTFIELDS =>'{
    "tagid":"56"
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
curl -X GET 'https://api2.chatmasterveloz.com/api/contacts/findbytag' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"tagid":"56"}'
```
