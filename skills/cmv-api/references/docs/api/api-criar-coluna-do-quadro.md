# API Criar Coluna do Quadro

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-coluna-do-quadro
- **Categoria:** APIs
- **Menu:** APIs › Quadro de atendimentos › API Criar Coluna do Quadro

---

🧩 Cria **uma coluna** no fim de um quadro de atendimentos.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/colunas
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
    "nome": "Aguardando peça",
    "cor": "#8E24AA",
    "tipo": "LIVRE"
}
```

➡️ **“quadroId”:** ID do quadro — vai no próprio endereço, no lugar de `{quadroId}`. **Obrigatório.**

➡️ **“nome”:** o nome da coluna. **Obrigatório.**

➡️ **“cor”:** opcional. A cor em hexadecimal, como `#8E24AA`. Sem ela, a coluna fica cinza (`#7C7C7C`).

➡️ **“tipo”:** opcional. O que a coluna faz com o atendimento que entra nela:

◽ `LIVRE` — **Coluna de atendimento**, o padrão. O atendimento continua aberto, e a coluna só classifica. É o único tipo para onde as regras do quadro levam um card.

◽ `PENDENTE_LIVRE` — **Coluna de fila (pendente)**. Guarda atendimentos ainda não aceitos, sem aceitar: eles continuam sem dono.

◽ `PENDENTE_FILA` — **Coluna automática por fila (pendente)**. Recebe sozinha os pendentes dos Setores informados em `queueIds`, como `"queueIds": [32]`. Sem Setor, é recusada.

◽ Cada Setor só pode estar em uma coluna automática por quadro: a segunda com o mesmo Setor é recusada.

◽ As duas colunas fixas não se criam de novo: `ATENDENDO` vira `LIVRE`.

◽ A resposta traz a coluna com o `id` e a `ordem`.

◽ Configurar o quadro é do administrador e do supervisor. Sem `userId`, quem faz é a empresa; para fazer em nome de uma pessoa, acrescente `?userId=` com o ID dela ao endereço — o de um atendente é recusado.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/colunas',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Aguardando peça",
    "cor": "#8E24AA",
    "tipo": "LIVRE"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/ticket-quadros/{quadroId}/colunas' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Aguardando peça","cor":"#8E24AA","tipo":"LIVRE"}'
```
