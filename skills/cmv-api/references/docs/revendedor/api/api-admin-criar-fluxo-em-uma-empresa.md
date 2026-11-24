# API Criar Fluxo em uma Empresa

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/api-admin-criar-fluxo-em-uma-empresa
- **Categoria:** APIs
- **Menu:** APIs Administrativas › Fluxos › API Criar Fluxo em uma Empresa

---

🧩 Cria **um fluxo dentro de uma empresa**, sem precisar entrar nela.

⚠️ Esta chamada exige um token da **empresa do Super Admin**.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/flowbuilder
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
    "companyId": 7,
    "name": "Boas-vindas",
    "categoryId": 3,
    "active": true,
    "userId": 4,
    "nodes": [
        {
            "id": "1",
            "type": "start",
            "data": {
                "label": "Início"
            },
            "position": {
                "x": 0,
                "y": 0
            }
        },
        {
            "id": "2",
            "type": "message",
            "data": {
                "label": "Olá! Em que posso ajudar?"
            },
            "position": {
                "x": 0,
                "y": 150
            }
        }
    ],
    "connections": [
        {
            "id": "e1-2",
            "source": "1",
            "target": "2"
        }
    ]
}
```

➡️ **“companyId”:** ID da empresa em que o registro é criado. **É ele que faz a chamada valer para outra empresa** — sem ele, vale a empresa do próprio token.

➡️ **“name”:** nome do fluxo, único naquela empresa. **Obrigatório.**

➡️ **“nodes”:** os blocos, do mesmo jeito que a tela grava — cada um com `id` único, `type`, `data` e `position`.

➡️ **“connections”:** as ligações, cada uma com `source` e `target` apontando para ids de blocos que existem.

➡️ **“flow”:** um fluxo inteiro já pronto, no lugar do `nodes` e do `connections`.

◽ É **o conteúdo do arquivo que a tela baixa** no menu **Mais opções  ›  Exportar Fluxo**, de dentro de um fluxo que já existe. Abra o arquivo, copie o que está escrito nele e mande como valor do `flow` — não é envio de arquivo, é o conteúdo dele dentro do payload.

◽ Esse arquivo é um objeto com duas listas, `{"nodes": [...], "connections": [...]}` — os mesmos dois campos desta chamada, só que juntos. Por isso **é um jeito OU o outro**: mandar o `flow` junto do `nodes` e do `connections` é recusado.

◽ Pela tela, esse mesmo arquivo entra pelo botão **Importar** da lista de fluxos, que escolhe o nome sozinho. Por aqui o nome é o que você mandar em `name`.

◽ **É assim que um fluxo pronto vai de uma empresa para outra:** exporte na empresa de origem, mande o conteúdo como `flow` e aponte o `companyId` da empresa de destino. O mesmo arquivo serve para quantas empresas você quiser.

➡️ **“categoryId”:** categoria do fluxo. Precisa ser uma categoria de fluxo **daquela** empresa.

➡️ **“active”:** `true` faz o fluxo nascer ativo.

➡️ **“userId”:** o dono do fluxo, que precisa ser usuário **daquela** empresa. Sem ele, o fluxo nasce do primeiro administrador dela.

➡️ **O desenho é conferido antes de gravar**, e a recusa diz onde está o problema:

◽ bloco sem `id` único ou sem `type`;

◽ ligação que sai ou chega num bloco que não existe;

◽ nome de fluxo repetido na empresa;

◽ fluxo maior que o teto — o mesmo do salvar pela tela.

◽ Campo fora desta lista não é gravado: ele volta na resposta, em `camposIgnorados`.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/flowbuilder',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "companyId": 7,
    "name": "Boas-vindas",
    "categoryId": 3,
    "active": true,
    "userId": 4,
    "nodes": [
        {
            "id": "1",
            "type": "start",
            "data": {
                "label": "Início"
            },
            "position": {
                "x": 0,
                "y": 0
            }
        },
        {
            "id": "2",
            "type": "message",
            "data": {
                "label": "Olá! Em que posso ajudar?"
            },
            "position": {
                "x": 0,
                "y": 150
            }
        }
    ],
    "connections": [
        {
            "id": "e1-2",
            "source": "1",
            "target": "2"
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
curl -X POST 'https://api2.chatmasterveloz.com/api/flowbuilder' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"companyId":7,"name":"Boas-vindas","categoryId":3,"active":true,"userId":4,"nodes":[{"id":"1","type":"start","data":{"label":"Início"},"position":{"x":0,"y":0}},{"id":"2","type":"message","data":{"label":"Olá! Em que posso ajudar?"},"position":{"x":0,"y":150}}],"connections":[{"id":"e1-2","source":"1","target":"2"}]}'
```
