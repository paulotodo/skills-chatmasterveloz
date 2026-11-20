# API Listar Projetos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-projetos
- **Categoria:** APIs
- **Menu:** APIs › Projetos › API Listar Projetos

---

🧩 Obter a **lista de projetos** da sua empresa, dos alterados por último aos mais antigos.

⚠️ Esta chamada usa o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**, sem informar a Conexão — o token de uma Conexão não é aceito.

**API:** Empresa

##### Endpoint

```
https://api2.chatmasterveloz.com/api/projetos?situacao={situacaoDoProjeto}&contactId={contactId}&busca={busca}
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

```
// sem payload — os filtros vão na própria URL
```

➡️ Esta chamada não tem payload. Os filtros são informados como **query** na URL, e todos são opcionais.

◽ **situacao:** a chave de uma das situações de projeto da empresa — `planejamento`, `andamento`, `pausado` ou `concluido` nas quatro que vêm de início, e uma chave como `s17942257596924` nas que a empresa cria. Valor que não é a chave de uma situação, inclusive o nome dela, é ignorado, e a lista vem inteira.

◽ A chave de cada situação vem na lista de situações dos projetos, junto com o nome que aparece no quadro. Ela também vem no campo `situacao` de cada projeto.

◽ **contactId:** só os projetos daquele contato.

◽ **busca:** parte do nome do projeto.

◽ Cada projeto vem com o contato, o responsável e o progresso: quantas tarefas tem, quantas estão concluídas e quantas estão atrasadas.

➡️ **A chamada vê todos os projetos da empresa**, como a gestão.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/projetos?situacao={situacaoDoProjeto}&contactId={contactId}&busca={busca}',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/projetos?situacao={situacaoDoProjeto}&contactId={contactId}&busca={busca}' -H 'Authorization: Bearer {seutokenaqui}'
```
