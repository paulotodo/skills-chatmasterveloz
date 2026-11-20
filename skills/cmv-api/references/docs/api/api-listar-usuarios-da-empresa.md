# API Listar Usuários da Empresa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-listar-usuarios-da-empresa
- **Categoria:** APIs
- **Menu:** APIs › Equipe › API Listar Usuários da Empresa

---

🧩 Listar **usuários** de uma empresa.

**API:** Todas

##### Endpoint

```
https://api2.chatmasterveloz.com/api/company/users
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
// sem payload
```

➡️ Esta chamada não tem payload.

◽ Cada usuário da resposta traz o campo `expediente`, com o horário de trabalho que vale para ele:

◽ `origem` — de onde vem o horário: `usuario` (o horário próprio, do cadastro do usuário), `empresa` (o **Horário padrão para todos os usuários**, no menu **Configurações  ›  Opções  ›  Geral**, seção **Gerenciamento de Expediente**) ou `null` (sem horário: o acesso não tem restrição).

◽ `dias` — os sete dias da semana, cada um com os intervalos de trabalho (`inicio` e `fim`). Dia sem restrição vem com `livre: true`.

◽ `dentroAgora` — `true` quando o usuário está dentro do expediente neste momento.

◽ `statusAutomatico` — `true` com a opção **Status automático pelo expediente** ligada, na mesma seção.

◽ `fuso` — o fuso horário em que os horários valem.

◽ Com o **Horário padrão para todos os usuários** ligado, todo usuário sem horário próprio vem com `origem: empresa` — inclusive administradores e supervisores.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/company/users',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
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
curl -X GET 'https://api2.chatmasterveloz.com/api/company/users' -H 'Authorization: Bearer {seutokenaqui}'
```
