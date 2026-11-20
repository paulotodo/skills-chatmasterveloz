# API Encerrar Tickets da Conexão por "Dias de Inatividade"

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-encerrar-tickets-da-conexao-por-dias-de-inatividade
- **Categoria:** APIs
- **Menu:** APIs › Ticket › API Encerrar Tickets da Conexão por "Dias de Inatividade"

---

🧩 Encerra à força **todos os tickets da conexão** que estão parados há mais de um número de dias.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/tickets/closeforced
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
    "days": 10,
    "userId": 31
}
```

➡️ **“days”:** número de dias sem nenhuma mexida no ticket. **Obrigatório.**

◽ Conta a partir da última alteração do ticket, não da última mensagem.

➡️ **“userId”:** ID do usuário que fica como autor do encerramento. Opcional.

⚠️ **O alcance é a conexão do token**, e não a empresa inteira: entram os tickets daquela conexão, **inclusive os que já estavam encerrados**. Com o Token da Empresa, a conexão é a que você informar na chamada.

◽ O ticket encerrado fica sem Setor e sem operador, e o protocolo dele é fechado.

◽ Cada ticket que fecha agora ganha uma linha no Registro do atendimento: com o `userId`, assinada pela pessoa; sem ele, como encerramento pela API. O que já estava encerrado não ganha linha.

⚠️ **Nada é enviado ao cliente** — não sai mensagem de despedida nem pedido de avaliação.

◽ A resposta traz só o total de tickets que entraram na varredura.

◽ Um `userId` que não existe, ou que é de outra empresa, é recusado **antes** de encerrar qualquer ticket.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/tickets/closeforced',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "days": 10,
    "userId": 31
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
curl -X POST 'https://api2.chatmasterveloz.com/api/tickets/closeforced' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"days":10,"userId":31}'
```
