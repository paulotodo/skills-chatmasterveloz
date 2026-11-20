# API Atualizar Projeto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-atualizar-projeto
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Atualizar Projeto

---

🧩 Atualiza **um projeto** — só o que vier no corpo muda.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos/{projetoId}
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
    "situacao": "andamento",
    "prazo": "2026-12-20",
    "membros": [
        4,
        7
    ]
}
```

➡️ **“projetoId”:** ID do projeto — vai no próprio endereço, no lugar de `{projetoId}`. **Obrigatório.**

➡️ **“situacao”:** a chave de uma das situações de projeto da empresa — `planejamento`, `andamento`, `pausado` ou `concluido` nas quatro que vêm de início, e uma chave como `s17942257596924` nas que a empresa cria. Valor que não é a chave de uma situação, inclusive o nome dela, é recusado.

◽ A chave de cada situação vem na lista de situações dos projetos, junto com o nome que aparece no quadro. Ela também vem no campo `situacao` de cada projeto.

➡️ **“prazo”:** novo prazo, no formato `AAAA-MM-DD`.

➡️ **“membros”:** a equipe **inteira** — substitui a atual.

◽ O responsável continua na equipe mesmo que não esteja na lista. Mandar `[]` deixa só ele.

◽ Também valem aqui os outros campos da criação — `nome`, `descricao`, `cor`, `contactId`, `responsavelId` e `crmOportunidadeId` —, menos `modeloId` e `userId`.

◽ Os campos que você não enviar ficam como estão.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'PUT',
  CURLOPT_POSTFIELDS =>'{
    "situacao": "andamento",
    "prazo": "2026-12-20",
    "membros": [
        4,
        7
    ]
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer {seutokenaqui}' //Token da Empresa
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

cURL:

```bash
curl -X PUT 'https://api2.chatmasterveloz.com/api/projetos/{projetoId}' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"situacao":"andamento","prazo":"2026-12-20","membros":[4,7]}'
```
