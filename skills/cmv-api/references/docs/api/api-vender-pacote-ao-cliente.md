# API Vender Pacote ao Cliente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-vender-pacote-ao-cliente
- **Categoria:** APIs
- **Menu:** APIs › Reservas › API Vender Pacote ao Cliente

---

🧩 Vende **um pacote** das Reservas a um cliente, que passa a ter o crédito para reservar.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/reservas/pacotes-dos-clientes
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
    "pacoteId": 1,
    "clienteNome": "Ana Souza",
    "clienteTelefone": "5511955892164"
}
```

➡️ **“pacoteId”:** o pacote vendido, que precisa estar ativo. **Obrigatório.**

➡️ **“clienteNome”:** o nome do cliente.

➡️ **“clienteTelefone”:** telefone do cliente no formato ddi ddd numero (somente números). **Obrigatório:** é pelo telefone que a agenda acha o pacote do cliente.

◽ No lugar do nome e do telefone, `"contactId"` vende ao contato da empresa, e o nome e o telefone vêm dele. O telefone de um contato que já existe liga a venda a esse contato.

◽ Opcionais: `clienteEmail`, `observacao` e `preco`, que vale no lugar do preço do pacote.

➡️ **A resposta traz o pacote do cliente**, com `id`, `nome`, `quantidade`, `usadas`, `restantes`, `ofertaIds`, `preco`, `validoAte` e `estado`.

◽ O `id` é o `pacoteClienteId` que a reserva usa para gastar o crédito.

◽ `validoAte`: o vencimento, contado a partir do dia da venda, no fuso da empresa. No pacote que não vence, `null`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/reservas/pacotes-dos-clientes',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "pacoteId": 1,
    "clienteNome": "Ana Souza",
    "clienteTelefone": "5511955892164"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/reservas/pacotes-dos-clientes' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"pacoteId":1,"clienteNome":"Ana Souza","clienteTelefone":"5511955892164"}'
```
