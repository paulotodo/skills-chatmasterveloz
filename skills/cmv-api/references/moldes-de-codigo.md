# Moldes de código para chamar a API do Chat Master Veloz

Cada molde abaixo faz a **mesma chamada de exemplo**: `API Mensagem de Texto` (selo Básica, Pro), copiada de `references/docs/api/api-mensagem-de-texto.md`. Para qualquer outra chamada, troque só três coisas, sempre pelo que o artigo dela diz: **o endereço**, **o método** e **o payload**. O resto (token fora do código, tempo limite, conferência do status, exibir o corpo do erro) fica igual.

Caminhos escritos como `api/...` e `recursos/...` ficam dentro de `references/docs/`.

## Sumário

1. Como definir a variável de ambiente
2. cURL
3. Node.js
4. Python
5. PHP
6. n8n: nó HTTP Request
7. Variações (GET, Token da Empresa, arquivo anexado, GET com corpo, chamada administrativa)
8. Receita: receber a mensagem e responder (passo a passo, do aviso para o payload, mídia por biblioteca, sintoma → causa → artigo, esqueleto de receptor)

## O que os moldes têm em comum, e por quê

- **Token em variável de ambiente (`CMV_TOKEN`).** Quem tem o token fala pela conexão (ou pela empresa inteira, no Token da Empresa); um token da empresa do Super Admin alcança todas as empresas da instância (`references/api-administrativa.md`). Escrito no código, ele vai parar em repositório, print e conversa.
- **Mostrar o corpo da resposta quando dá erro.** A documentação diz que a resposta explica o que faltou (por exemplo, o 400 do Token da Empresa sem a conexão). Engolir o corpo esconde a causa.
- **Sem repetição automática em envio de mensagem.** Repetir um POST que na verdade já tinha sido aceito manda a mensagem duas vezes para o cliente. Deixe a decisão de reenviar para a pessoa ou para a lógica do sistema dela.
- **Não registrar em log o token nem respostas que o contenham** (a de `api/api-status-das-conexoes.md` traz o token de cada conexão; das administrativas, a de `revendedor/api/api-admin-obter-uma-empresa-completa.md` traz o Token da Empresa em `apiToken` e a de `revendedor/api/api-admin-criar-token-da-empresa.md` devolve o token inteiro).

Os códigos de status e o formato da resposta de sucesso **não estão descritos** na maioria dos artigos. Por isso os moldes tratam "2xx = aceito" e "qualquer outro = mostrar status e corpo", sem interpretar campos da resposta. Se o artigo da chamada citar um código ou erro específico, acrescente o tratamento dele.

## Como definir a variável de ambiente

```bash
# Linux, macOS, Git Bash ou WSL (vale só para a janela de terminal aberta)
export CMV_TOKEN='cole-o-token-aqui'
```

```powershell
# Windows PowerShell (vale só para a janela aberta)
$env:CMV_TOKEN = 'cole-o-token-aqui'
```

Em servidor, use o cofre de segredos ou o arquivo `.env` do próprio sistema, com o `.env` fora do repositório (no `.gitignore`).

## cURL

```bash
: "${CMV_TOKEN:?defina a variável CMV_TOKEN antes de rodar}"

curl -sS --max-time 30 -w '\nHTTP %{http_code}\n' \
  -X POST 'https://api2.chatmasterveloz.com/api/messages/send' \
  -H "Authorization: Bearer $CMV_TOKEN" \
  -H 'Content-Type: application/json' \
  --data '{"number":"5511955892164","openTicket":"1","queueId":"16","body":"Bem vindo Lead"}'
```

A última linha da saída mostra o status HTTP; acima dela vem o corpo da resposta. Fora de `2xx`, leia o corpo: é ele que diz o que faltou.

## Node.js (18 ou mais novo, sem instalar nada)

```javascript
const token = process.env.CMV_TOKEN;
if (!token) throw new Error("Defina a variável de ambiente CMV_TOKEN.");

const resposta = await fetch("https://api2.chatmasterveloz.com/api/messages/send", {
  method: "POST",
  headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
  body: JSON.stringify({
    number: "5511955892164",
    openTicket: "1",
    queueId: "16",
    body: "Bem vindo Lead",
  }),
  signal: AbortSignal.timeout(30_000),
});

const corpo = await resposta.text();
if (!resposta.ok) {
  throw new Error(`CMV respondeu HTTP ${resposta.status}: ${corpo}`);
}
console.log("Aceito pelo CMV:", corpo);
```

Salve como `enviar.mjs` e rode com `node enviar.mjs`. Este código é para servidor: nunca o coloque em página web, porque o token ficaria visível para qualquer visitante.

## Python (só biblioteca padrão)

```python
import json
import os
import sys
import urllib.error
import urllib.request

token = os.environ.get("CMV_TOKEN")
if not token:
    sys.exit("Defina a variável de ambiente CMV_TOKEN.")

payload = {
    "number": "5511955892164",
    "openTicket": "1",
    "queueId": "16",
    "body": "Bem vindo Lead",
}
pedido = urllib.request.Request(
    "https://api2.chatmasterveloz.com/api/messages/send",
    data=json.dumps(payload).encode("utf-8"),
    method="POST",
    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
)
try:
    with urllib.request.urlopen(pedido, timeout=30) as resposta:
        print("Aceito pelo CMV:", resposta.read().decode("utf-8"))
except urllib.error.HTTPError as erro:
    sys.exit(f"CMV respondeu HTTP {erro.code}: {erro.read().decode('utf-8', 'replace')}")
except urllib.error.URLError as erro:
    sys.exit(f"Não consegui falar com o CMV: {erro.reason}")
```

## PHP (cURL, como nos exemplos da documentação)

```php
<?php
$token = getenv('CMV_TOKEN');
if (!$token) {
    exit("Defina a variável de ambiente CMV_TOKEN.\n");
}

$curl = curl_init('https://api2.chatmasterveloz.com/api/messages/send');
curl_setopt_array($curl, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_CUSTOMREQUEST => 'POST',
    CURLOPT_POSTFIELDS => json_encode([
        'number' => '5511955892164',
        'openTicket' => '1',
        'queueId' => '16',
        'body' => 'Bem vindo Lead',
    ]),
    CURLOPT_HTTPHEADER => [
        'Content-Type: application/json',
        'Authorization: Bearer ' . $token,
    ],
]);

$corpo = curl_exec($curl);
$status = curl_getinfo($curl, CURLINFO_HTTP_CODE);
$falha = curl_error($curl);
curl_close($curl);

if ($corpo === false) {
    exit("Não consegui falar com o CMV: $falha\n");
}
if ($status < 200 || $status >= 300) {
    exit("CMV respondeu HTTP $status: $corpo\n");
}
echo "Aceito pelo CMV: $corpo\n";
```

Os exemplos em PHP dos artigos trazem `CURLOPT_TIMEOUT => 0` (sem limite) e o token escrito no código; o molde troca os dois de propósito.

## n8n: nó HTTP Request

Entregue a configuração campo a campo, porque quem usa n8n preenche um formulário. Os nomes dos campos abaixo são da documentação do n8n, não da do Chat Master Veloz, e podem mudar entre versões do n8n: se a tela da pessoa estiver diferente, oriente pela documentação do n8n.

| Campo do nó | Valor |
|---|---|
| **Method** | o método do artigo (aqui, `POST`) |
| **URL** | o endereço do artigo (aqui, `https://api2.chatmasterveloz.com/api/messages/send`) |
| **Authentication** | `Generic Credential Type`, do tipo `Bearer Auth`; na credencial, cole o token do CMV em **Bearer Token** |
| **Send Body** | ligado |
| **Body Content Type** | `JSON` |
| **Specify Body** | `Using JSON` |
| **JSON** | o payload do artigo (abaixo) |

```json
{
  "number": "{{ $json.body.sender }}",
  "openTicket": "0",
  "queueId": "0",
  "body": "Recebemos sua mensagem!"
}
```

- **Por que credencial e não o token colado na URL ou no cabeçalho à mão:** a credencial do n8n fica guardada à parte e não aparece no JSON do workflow quando ele é exportado ou compartilhado. `Bearer Auth` equivale a um cabeçalho `Authorization` com o valor `Bearer <token>`, que é o que a API do CMV pede; `Header Auth` com esse nome e esse valor também serve.
- **Dados vindos de um webhook do CMV** ficam dentro de `body` no nó Webhook do n8n (a documentação usa expressões como `{{$json.body.mensagem[0]...}}` em `api/arquivos-no-webhook.md`); a receita de receber e responder está no fim deste arquivo. Os avisos de webhook e o bloco HTTP Request do FlowBuilder também podem trazer o token da conexão (`token_origin`, `{{connection_token}}`); usar esse valor funciona, mas ele passa a aparecer no histórico de execuções do n8n.
- **Erro:** por padrão o nó falha quando a resposta não é `2xx`. Em **Settings › On Error**, escolha `Continue (using error output)` para tratar a falha num ramo próprio. Em **Options › Response**, ligar **Include Response Headers and Status** mostra o status junto do corpo. Não ligue **Retry On Fail** em nó que envia mensagem, pelo mesmo motivo dos outros moldes: pode enviar duas vezes.
- **Envio de arquivo anexado:** o corpo deixa de ser JSON e passa a ser um formulário (multipart/form-data), com um campo de arquivo cujo nome é o que o artigo pede (por exemplo `medias`). Como anexar o binário no nó muda entre versões do n8n: peça à pessoa a versão ou oriente a conferir na documentação do n8n, em vez de afirmar nomes de campo de memória.

## Variações

**Chamada GET, com filtros na URL** (o artigo traz o endereço já com os filtros; não há corpo nem `Content-Type`):

```bash
curl -sS --max-time 30 -w '\nHTTP %{http_code}\n' \
  -X GET 'https://api2.chatmasterveloz.com/api/janela?number=5511955892164' \
  -H "Authorization: Bearer $CMV_TOKEN"
```

**Token da Empresa:** a chamada é a mesma, mas é obrigatório dizer a conexão com `whatsappId`, `connectionId` ou `whatsappName`, na query string ou no corpo (`references/docs/recursos/token-da-empresa-em-configuracoes.md`). Em envio com arquivo, use a query string.

```bash
curl -sS --max-time 30 -w '\nHTTP %{http_code}\n' \
  -X POST 'https://api2.chatmasterveloz.com/api/messages/send?connectionId=67' \
  -H "Authorization: Bearer $CMV_TOKEN_EMPRESA" \
  -H 'Content-Type: application/json' \
  --data '{"number":"5511955892164","openTicket":"0","queueId":"0","body":"Olá, tudo bem?"}'
```

**Arquivo anexado (multipart):** o corpo é um formulário, com um campo por arquivo, e o cabeçalho `Content-Type` não é informado, porque quem monta a requisição o preenche (`references/docs/api/estrutura-de-api.md`). Os nomes dos campos estão no artigo da chamada (em `api/api-enviar-arquivo.md`: `medias`, `number`, `openTicket`, `queueId`, `body`).

```bash
curl -sS --max-time 120 -w '\nHTTP %{http_code}\n' \
  -X POST 'https://api2.chatmasterveloz.com/api/messages/send' \
  -H "Authorization: Bearer $CMV_TOKEN" \
  -F 'medias=@/caminho/para/arquivo.jpg' \
  -F 'number=5511955892164' -F 'openTicket=0' -F 'queueId=0' -F 'body=Teste'
```

**GET com corpo:** `api/api-listar-tickets-do-painel.md` avisa que é uma chamada GET com payload, e que há bibliotecas e servidores intermediários que descartam o corpo de um GET. O `fetch` do Node recusa esse formato; use cURL (`-X GET` com `--data`) ou um cliente que permita. Duas chamadas administrativas também são GET com corpo: `GET /api/companies`, com o `id` da empresa no corpo (`revendedor/api/api-admin-obter-uma-empresa-completa.md`, que manda enviar o corpo com `Content-Type: application/json`), e `GET /api/invoices/listar`, com `status` no corpo (`revendedor/api/api-admin-obter-faturas.md`).

**Chamada administrativa (revendedor):** a forma é a mesma; o que muda é o token, que tem de ser da empresa do Super Admin, do tipo que o aviso do começo do artigo pedir, e o `companyId` quando a chamada age na empresa de um cliente. Leia `references/api-administrativa.md` antes: várias dessas chamadas valem para a instância inteira.

## Receita: receber a mensagem e responder (n8n ou receptor próprio)

Caso típico: o webhook da Conexão entrega as mensagens num fluxo do n8n (ou num servidor da pessoa) e a integração responde pela API. Os caminhos de campo abaixo são os dos artigos; a lista completa de avisos e de armadilhas de webhook está na seção 7 de `references/mapa-da-api.md`. No n8n, tudo o que chega do CMV fica dentro de `body` (`body.acao`, `body.sender`…), como nas expressões de `api/arquivos-no-webhook.md`; num receptor próprio, os mesmos campos estão na raiz do JSON.

### Passo a passo

1. **Receber.** O endereço precisa aceitar POST com corpo em JSON. No n8n: nó Webhook em POST, com a URL de produção colada no campo de webhook da Conexão (`recursos/n8n-via-webhook.md`).
2. **Ficar só com o aviso que interessa.** Uma mensagem recebida gera dois avisos: primeiro `acao` = `start`, depois `from_internal` (canal Oficial) ou `fila-data` (canais por QR Code). O artigo manda tratar o segundo, que traz o texto final e o identificador da mensagem (`api/webhooks-da-conexao.md`). No webhook do Setor os nomes são outros: `queue_webhook` e depois `queue_webhook_from_internal` (`api/webhook-de-setor.md`). Os avisos de tag usam a chave `action` em vez de `acao`.
3. **Ficar só com o que o cliente mandou: `fromMe` igual a `false`.** O artigo diz que a mensagem enviada daqui também gera aviso, com `fromMe` igual a `true`, e que todo aviso traz `origemDoEvento`, que vem `api` quando o aviso é de algo que a própria integração fez. *Inferência (o artigo não fala em laço):* a resposta que a integração envia pela API volta como um desses avisos; sem este filtro, o fluxo responde à própria resposta, sem parar.
4. **Descartar repetidos pelo `eventoId`.** Todo aviso da Conexão e do Setor traz `eventoId`, o código do fato, igual em todos os endereços que recebem aquele fato (acontece, por exemplo, com webhook da Conexão e do Setor ligados juntos). O artigo manda guardar os `eventoId` já tratados e ignorar o que voltar; guarde-os em algum lugar que sobreviva entre execuções. O `mensagem.wid` não serve para isso: a mesma mensagem gera mais de um aviso. Se a `sequencia` (que sobe de 1 em 1 por endereço) pular um número, o aviso perdido se busca de novo por até 7 dias (`api/api-listar-entregas-do-webhook-da-conexao.md`).
5. **Se for mídia, buscar o arquivo conforme a biblioteca** (tabela abaixo).
6. **Responder pela API**, com os campos do aviso no payload do artigo da conexão (tabela abaixo).

Como montar o filtro (nó IF ou Filter), guardar valores entre execuções e baixar ou converter um arquivo no n8n: confira na documentação do n8n. Esta skill só garante os nomes dos campos do CMV.

### Do aviso para o payload da resposta

| Campo do aviso | O que é, segundo o artigo | Básica e Pro (`api/api-mensagem-de-texto.md`) | Oficial (`api/api-oficial-mensagem.md`) |
|---|---|---|---|
| `sender` | o número do cliente, sempre | `number` | `number` (obrigatório, mesmo com `ticketId`) |
| `chamadoId` | o identificador do atendimento (número do ticket) | não há campo de ticket neste artigo | `ticketId` (opcional: só escolhe em qual atendimento a mensagem fica gravada) |
| texto da resposta | | `body` | `text` |
| efeito no atendimento | | `openTicket` e `queueId`: com `"1"` e um Setor, a conversa vai para **Aguardando** mesmo que já esteja em atendimento; o exemplo do artigo que não abre ticket usa `"0"` nos dois | o atendimento fica como estava: o envio não encerra a conversa nem muda o Setor |

Oficial, respondendo a quem acabou de escrever (corpo do nó HTTP Request para `https://api2.chatmasterveloz.com/api/messages/sendOfficialData`):

```json
{
  "number": "{{ $json.body.sender }}",
  "ticketId": {{ $json.body.chamadoId }},
  "text": "Recebemos sua mensagem!"
}
```

Básica e Pro: o corpo é o do molde do nó HTTP Request, acima, com `sender` em `number`.

No exemplo do artigo, `ticketId` é número (`700`), por isso a expressão vai sem aspas; como o campo é opcional, na dúvida sobre como o n8n monta esse valor, deixe-o de fora ou confira na documentação do n8n.

Na Oficial o envio de texto exige a janela de atendimento aberta. A regra do artigo `api/api-janela-de-atendimento.md` é de 24 horas contadas da última mensagem do cliente; logo, numa resposta a uma mensagem que acabou de chegar a janela está aberta. Em Instagram, Facebook, WebChat e Chat Externo o artigo de envio é outro e o destinatário também (seções 3 e 8 do mapa).

### Mídia recebida, por biblioteca (`api/arquivos-no-webhook.md`)

Chegam dois avisos seguidos. O primeiro traz, no lugar do texto, só uma indicação do tipo (`Áudio`, o nome do arquivo quando é PDF, ou vazio quando é imagem ou vídeo); o segundo carrega as informações do arquivo.

| Biblioteca | Onde está o arquivo |
|---|---|
| Oficial | GET no endereço que vem em `body.mensagem.mediaUrl` |
| Pro | não há endereço: o conteúdo vem em base64 em `body.mensagem[0].mediaData[0].buffer`, com o nome em `originalname` (em áudio, trocando `oga` por `ogg`) e o tipo em `mimetype` |
| Básica | GET no endereço formado por `body.backendURL`, `body.mediaFolder` e `body.mediaName`, nessa ordem, separados por barra |

O artigo de arquivos não diz qual valor de `acao` cada um dos dois avisos traz. Na Oficial, o caminho `mensagem.mediaUrl` é o do objeto `mensagem` do aviso `from_internal`. Nas outras, reconheça o aviso do arquivo pela presença dos campos acima, e confirme com um aviso real. Texto de áudio: com a transcrição ligada, o texto transcrito aparece em `mensagem.body` (`api/webhooks-da-conexao.md`).

### Sintoma → causa → artigo

| Sintoma | Causa que o artigo explica | Correção | Artigo |
|---|---|---|---|
| Toda mensagem recebida dispara o fluxo duas vezes | Cada mensagem recebida gera dois avisos (`start` e depois `from_internal` ou `fila-data`) | Tratar só o segundo | `api/webhooks-da-conexao.md` |
| A mesma mensagem chega duas vezes, com o mesmo `eventoId` | Webhook da Conexão e do Setor ligados ao mesmo tempo: com o atendimento no Setor escolhido, disparam os dois | Apontar cada um para um endereço diferente, desligar um deles ou descartar pelo `eventoId` | `api/qual-webhook-usar.md`, `api/webhook-de-setor.md` |
| Faltou um aviso (a `sequencia` pulou um número) | O aviso daquela entrega se perdeu | Buscar de novo, por até 7 dias, a partir do último número que chegou | `api/api-listar-entregas-do-webhook-da-conexao.md` |
| Áudio, imagem ou documento chega "vazio" | É o primeiro dos dois avisos de mídia | Usar o segundo aviso e buscar o arquivo conforme a biblioteca | `api/arquivos-no-webhook.md` |
| Áudio chega sem o texto falado | O texto transcrito só aparece em `mensagem.body` com a transcrição ligada | Ligar a transcrição (pela API, campo `isTranscribe` do Setor) ou baixar o áudio | `api/webhooks-da-conexao.md`, `api/api-atualizar-setor.md` |
| O fluxo responde a si mesmo | *Inferência:* a mensagem enviada também gera aviso, com `fromMe` igual a `true` | Tratar só `fromMe` igual a `false` e ignorar `origemDoEvento` igual a `api` | `api/webhooks-da-conexao.md` |
| Não dá para saber se a mensagem foi enviada ou recebida, ou `name` traz o celular | `name` muda de conteúdo conforme a direção | Usar `fromMe` | `api/webhooks-da-conexao.md` |
| Avisos de tag não são reconhecidos | Nos avisos de tag a chave é `action` | Ler `acao` e, na falta, `action` | `api/webhooks-da-conexao.md`, `api/webhook-de-setor.md` |
| O aviso da Pro com mídia é muito grande | O arquivo vem embutido em base64 | O receptor precisa aceitar corpos grandes | `api/arquivos-no-webhook.md` |

Se o sintoma não estiver na tabela, diga que os artigos não explicam e peça à pessoa um aviso real (sem o token) para comparar com os exemplos.

### Esqueleto de receptor próprio (Python, só biblioteca padrão)

Aplica os passos 2 a 4 para o canal Oficial e não grava o corpo inteiro em log, porque ele carrega o token da conexão.

```python
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

ja_vistos = set()  # em produção, guarde em banco ou cache com validade


class Receptor(BaseHTTPRequestHandler):
    def do_POST(self):
        tamanho = int(self.headers.get("Content-Length", 0))
        try:
            aviso = json.loads(self.rfile.read(tamanho) or b"{}")
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            return
        self.send_response(200)  # responda logo; processe depois
        self.end_headers()

        acao = aviso.get("acao") or aviso.get("action")  # avisos de tag usam "action"
        if acao != "from_internal":  # QR Code: "fila-data", com outro formato; webhook do Setor: "queue_webhook_from_internal"
            return
        if aviso.get("fromMe") or aviso.get("origemDoEvento") == "api":
            return  # enviada daqui ou pela própria integração: não responder a si mesmo
        mensagem = aviso.get("mensagem")
        if not isinstance(mensagem, dict):
            return
        evento = aviso.get("eventoId")
        if evento:
            if evento in ja_vistos:
                return  # aviso repetido (Conexão e Setor ligados juntos, por exemplo)
            ja_vistos.add(evento)
        # daqui em diante: responder pela API com sender -> number e chamadoId -> ticketId
        print(f"mensagem do cliente no atendimento {aviso.get('chamadoId')}"
              + (" (com mídia)" if mensagem.get("mediaUrl") else ""))

    def log_message(self, *args):
        pass  # sem log automático de requisições


HTTPServer(("0.0.0.0", 8080), Receptor).serve_forever()
```

O endereço público precisa estar sob HTTPS (um proxy reverso na frente deste servidor, por exemplo).
