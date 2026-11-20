# API Oficial Mensagem Template

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/api-oficial-mensagem-template
- **Categoria:** APIs
- **Menu:** APIs › Mensagem › API Oficial Mensagem Template

---

🧩 Envia uma **mensagem template pela API oficial,** estando previamente aprovada.

**API:** Oficial

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/sendMetaCustom
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
    "number": "5511955892164",
    "name": "vars_001",
    "language": "pt_BR",
    "openTicket": 1,
    "queueId": 100,
    "template": [
        {
            "type": "header",
            "parameters": [
                {
                    "type": "text",
                    "text": "Texto cabeçalho"
                }
            ]
        },
        {
            "type": "body",
            "parameters": [
                {
                    "type": "text",
                    "text": "Maria"
                },
                {
                    "type": "text",
                    "text": "Festa do Peão"
                },
                {
                    "type": "text",
                    "text": "15/01/2028"
                }
            ]
        },
        {
          "type": "button",
          "sub_type": "quick_reply",
          "index": "0",
          "parameters": [
            {
              "type": "payload",
              "payload": "Contato"
            }
          ]
        }
    ]
}
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“name”:** nome do template, idêntico ao aprovado na Meta.

➡️ **“language”:** idioma, idêntico ao aprovado na Meta.

➡️ **“openTicket”:** decide o que acontece com o ticket:

◽ `0` — o ticket é encerrado.

◽ `1` com `"queueId": 0` — o status do ticket permanece como estava.

◽ `1` com um Setor em `queueId` — o status muda para **Aguardando**.

➡️ **“queueId”:** ID do Setor desejado (só funciona quando `"openTicket": "1"`).

➡️ **“template”:** os componentes do template, um por entrada. Cada entrada tem um **type** — `header`, `body` ou `button` — e você adiciona os que existirem no template aprovado na Meta.

➡️ **“assinaturaIa”:** opcional — acrescente ao corpo quando quem envia é a sua IA. Mande o nome da IA, com até 100 caracteres, ou `true`, que assina como **Assistente IA**. A mensagem fica marcada como enviada pela IA e aparece na conversa com o nome dela. Sem o campo, ou com `false`, o envio fica como sempre.

## O componente `header`

Dentro de `parameters`, o **type** pode ser `text`, `image`, `video`, `document` ou `location`. A Meta não tem suporte a áudio no cabeçalho.

```javascript
// texto
{
  "type": "header",
  "parameters": [ { "type": "text", "text": "Meu cabeçalho" } ]
}

// imagem
{
  "type": "header",
  "parameters": [ { "type": "image", "image": { "link": "https://..." } } ]
}

// vídeo
{
  "type": "header",
  "parameters": [ { "type": "video", "video": { "link": "https://..." } } ]
}

// documento
{
  "type": "header",
  "parameters": [ { "type": "document", "document": { "link": "https://...", "filename": "livro.pdf" } } ]
}

// localização
{
  "type": "header",
  "parameters": [ { "type": "location", "location": { "latitude": -22.950762, "longitude": -43.2135083, "name": "Cristo Redentor", "address": "texto do endereço" } } ]
}
```

🚨 Adicione o parâmetro exato do seu template cadastrado na Meta, lembrando que ela só permite **um header por template**.

## O componente `body`

Dentro de `parameters`, o **type** é sempre `text`.

```javascript
{
  "type": "body",
  "parameters": [ { "type": "text", "text": "O valor da sua variável aqui" } ]
}
```

🚨 Adicione mais parâmetros de texto conforme cadastrado no seu template da Meta, seguindo exatamente **a ordem das variáveis**.

## O componente `button`

🔘 **sub_type:** pode ser `quick_reply`, `url`, `copy_code` ou `flow`.

🔘 **index:** número que representa a ordem do botão. Começa em `0`, o próximo é `1`, e assim por diante. O número tem de ser exatamente a ordem cadastrada no template.

🔘 **parameters:** dentro do botão, o **type** pode ser `payload`, `text`, `coupon_code` ou `action`.

```javascript
// quick_reply
{ "type": "payload", "payload": "Texto invisível de retorno para o webhook" }

// url dinâmica — o text é a parte dinâmica da URL: site.com/{{1}}
{ "type": "text", "text": "pagina-de-vendas" }

// copy_code
{ "type": "coupon_code", "coupon_code": "texto a ser copiado aqui" }

// flow
{ "type": "action", "action": { "flow_token": "id_da_sessao", "flow_action_data": { "chave": "valor" } } }
```

🚨 Botões sem variável, como o **URL Estático** e o **Ligação (Call)**, não precisam entrar no payload. Coloque apenas os botões que têm variável, e mantenha o `index` na ordem correta do template cadastrado na Meta.

🚨 Botões **Quick Reply** só podem ser usados junto com outros Quick Reply. Não podem ser combinados com URL, Copy Code ou outros.

#### Utilize o código em requisições HTTPS com ferramentas como cURL ou bibliotecas de integração.

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api2.chatmasterveloz.com/api/messages/sendMetaCustom',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "number": "5511955892164",
    "name": "vars_001",
    "language": "pt_BR",
    "openTicket": 1,
    "queueId": 100,
    "template": [
        {
            "type": "header",
            "parameters": [
                {
                    "type": "text",
                    "text": "Texto cabeçalho"
                }
            ]
        },
        {
            "type": "body",
            "parameters": [
                {
                    "type": "text",
                    "text": "Maria"
                },
                {
                    "type": "text",
                    "text": "Festa do Peão"
                },
                {
                    "type": "text",
                    "text": "15/01/2028"
                }
            ]
        },
        {
          "type": "button",
          "sub_type": "quick_reply",
          "index": "0",
          "parameters": [
            {
              "type": "payload",
              "payload": "Contato"
            }
          ]
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
curl -X POST 'https://api2.chatmasterveloz.com/api/messages/sendMetaCustom' -H 'Authorization: Bearer {seutokenaqui}' -H 'Content-Type: application/json' --data '{"number":"5511955892164","name":"vars_001","language":"pt_BR","openTicket":1,"queueId":100,"template":[{"type":"header","parameters":[{"type":"text","text":"Texto cabeçalho"}]},{"type":"body","parameters":[{"type":"text","text":"Maria"},{"type":"text","text":"Festa do Peão"},{"type":"text","text":"15/01/2028"}]},{"type":"button","sub_type":"quick_reply","index":"0","parameters":[{"type":"payload","payload":"Contato"}]}]}'
```
