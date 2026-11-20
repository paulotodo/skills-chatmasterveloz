# API Distribuir Atendimento por Rodízio

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-distribuir-atendimento-por-rodizio
- **Categoria:** APIs
- **Menu:** APIs › Rodízios › API Distribuir Atendimento por Rodízio

---

🧩 Entrega **um atendimento a um operador** pelo rodízio cadastrado, com a mesma distribuição que o bloco de rodízio do fluxo faz — só que sem precisar de fluxo nenhum.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/rodizios/{rodizioId}/distribuir
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
    "ticketId": 700,
    "forcar": false
}
```

➡️ **“rodizioId”:** ID do rodízio — vai no próprio endereço, no lugar de `{rodizioId}`. **Obrigatório.**

➡️ **“ticketId”:** ID do Ticket a distribuir. **Obrigatório.**

◽ É o número entre parênteses no cabeçalho da conversa. Em **João da Silva (52) | #25678**, o ticketId é o **52**.

➡️ **“forcar”:** `true` redistribui um atendimento que **já tem responsável**.

◽ A escolha do operador respeita os percentuais do cadastro, a presença de cada um e o limite de atendimentos simultâneos.

◽ O atendimento é entregue com o Setor e o status — **Atendendo** ou **Aguardando** — que estiverem na linha daquele operador no cadastro do rodízio.

◽ A entrega é somada ao Relatório do Rodízio.

⚠️ **Ninguém disponível não é erro.** A chamada responde normalmente dizendo que não distribuiu, e o atendimento vai para o Setor de transbordo do rodízio, quando ele tem um.

⚠️ **Atendimento que já tem responsável é recusado**, a menos que venha o `forcar`. Com ele, se ninguém puder receber na hora, o atendimento fica com quem já estava.

◽ Duas chamadas ao mesmo tempo para o mesmo atendimento são atendidas uma de cada vez: a segunda encontra o responsável que a primeira escolheu e é recusada.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/rodizios/{rodizioId}/distribuir',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "ticketId": 700,
    "forcar": false
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
curl -X POST 'https://api2.chatmasterveloz.com/api/rodizios/{rodizioId}/distribuir' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"ticketId":700,"forcar":false}'
```
