# API Criar Projeto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-criar-projeto
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Criar Projeto

---

🧩 Cria **um projeto** na sua empresa, com as colunas padrão ou as de um modelo.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos
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
    "nome": "Implantação — Loja Centro",
    "descricao": "Implantação do sistema na loja do centro",
    "situacao": "planejamento",
    "cor": "#3f51b5",
    "prazo": "2026-12-15",
    "contactId": 50,
    "responsavelId": 4,
    "membros": [
        4,
        7
    ],
    "modeloId": 3,
    "userId": 4
}
```

➡️ **“nome”:** nome do projeto. **Obrigatório.**

➡️ **“descricao”:** descrição do projeto.

➡️ **“situacao”:** a chave de uma das situações de projeto da empresa — `planejamento`, `andamento`, `pausado` ou `concluido` nas quatro que vêm de início, e uma chave como `s17942257596924` nas que a empresa cria.

◽ Sem informar, o projeto entra na primeira situação da empresa, a da primeira coluna do quadro de **Projetos**. Valor que não é a chave de uma situação da empresa é recusado.

◽ A chave de cada situação vem na lista de situações dos projetos, junto com o nome que aparece no quadro. Ela também vem no campo `situacao` de cada projeto.

➡️ **“cor”:** cor do projeto, em hexadecimal — por exemplo, `#3f51b5`.

➡️ **“prazo”:** prazo do projeto, no formato `AAAA-MM-DD`.

➡️ **“contactId”:** ID do contato do projeto.

➡️ **“responsavelId”:** ID do usuário responsável. Ele entra na equipe.

➡️ **“membros”:** IDs dos usuários da equipe.

◽ Quem cria o projeto também entra na equipe.

➡️ **“modeloId”:** ID do modelo de projeto — o projeto nasce com as colunas e as tarefas dele.

◽ Sem modelo, o projeto nasce com as colunas **A fazer**, **Fazendo**, **Revisão** e **Feito**. A tarefa que cai em **Feito** fica concluída.

◽ Modelo que não existe é recusado.

➡️ **“userId”:** ID do usuário em nome de quem o projeto é criado.

◽ Sem ele, o projeto é criado em nome do primeiro administrador da empresa.

➡️ **“crmOportunidadeId”:** ID da oportunidade a que o projeto fica ligado.

◽ Para uma oportunidade do CRM V1, use **“oportunidadeId”**.

◽ A resposta traz o projeto com o **id**, as colunas e a equipe.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/projetos',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "nome": "Implantação — Loja Centro",
    "descricao": "Implantação do sistema na loja do centro",
    "situacao": "planejamento",
    "cor": "#3f51b5",
    "prazo": "2026-12-15",
    "contactId": 50,
    "responsavelId": 4,
    "membros": [
        4,
        7
    ],
    "modeloId": 3,
    "userId": 4
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
curl -X POST 'https://api2.chatmasterveloz.com/api/projetos' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"nome":"Implantação — Loja Centro","descricao":"Implantação do sistema na loja do centro","situacao":"planejamento","cor":"#3f51b5","prazo":"2026-12-15","contactId":50,"responsavelId":4,"membros":[4,7],"modeloId":3,"userId":4}'
```
