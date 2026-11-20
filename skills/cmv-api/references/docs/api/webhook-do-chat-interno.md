# Webhook do Chat Interno

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-do-chat-interno
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook do Chat Interno

---

🧩 Quer levar para outro sistema o que a equipe combina no **Chat Interno** — um recado, uma chamada que terminou, a transcrição de uma reunião gravada? O **Webhook do Chat Interno** avisa o seu sistema na hora, a cada mensagem, reação, conversa ou chamada da equipe.

O **Webhook do Chat Interno** cobre só as conversas internas da equipe. As conversas com os clientes são avisadas pelos webhooks da Conexão e do Setor.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Chat Interno** e clique no ícone **Webhook do chat interno**, no topo da tela.
>
> ➡️ Preencha **URL do webhook** com o endereço do seu sistema e clique em **Salvar**.
>
> ➡️ Para receber os avisos de uma conversa só, o administrador usa o campo **Webhook desta conversa (opcional)**, na janela de editar aquela conversa.

## Onde ligar

🔘 **Webhook do chat interno:** o ícone fica no topo da tela do **Chat Interno** e aparece só para o administrador. A **URL do webhook** recebe os eventos de todas as conversas do Chat Interno da empresa. Com o campo em branco, nada é enviado. Ao salvar, a tela avisa *"Webhook do chat interno salvo"*.

🔘 **Webhook desta conversa (opcional):** na janela de editar uma conversa do **Chat Interno**, recebe os eventos só daquela conversa. O campo também aparece só para o administrador: quem criou o grupo, sem ser administrador, não o vê.

📌 Pela documentação da API da plataforma, a mesma URL no webhook geral e no de uma conversa recebe cada aviso uma vez só.

O endereço precisa aceitar **POST** com corpo em JSON.

## O campo que separa um aviso do outro

Tudo chega no mesmo endereço, e é o **`acao`** que diz o que aconteceu no **Chat Interno**:                                          

| `acao` | O que aconteceu |
|---|---|
| `mensagem-criada` | uma mensagem nova numa conversa — texto, arquivo, áudio, a gravação de uma chamada ou a transcrição e a análise da IA |
| `mensagem-editada` | uma mensagem foi editada |
| `mensagem-apagada` | uma mensagem foi apagada |
| `mensagens-entregues` · `mensagens-lidas` | mensagens chegaram a uma pessoa ou foram lidas por ela |
| `reacao` | alguém reagiu a uma mensagem ou tirou a reação |
| `chat-criado` · `chat-alterado` · `chat-apagado` | uma conversa foi criada, alterada ou apagada |
| `chamada-iniciada` · `chamada-encerrada` | uma chamada da equipe começou ou terminou |
| `gravacao-iniciada` · `gravacao-concluida` · `gravacao-transcrita` | a gravação de uma chamada começou, ficou pronta, ou a IA terminou a transcrição e a análise |

Todo aviso do **Webhook do Chat Interno** traz também:

◽ `companyId` — a empresa.

◽ `chat` — o resumo da conversa: `id`, `uuid`, `title`, `somenteAvisos` (se é um grupo de avisos), `ownerId` (quem criou) e `participantes`, com o `id` e o `nome` de cada um.

◽ `origem` — de onde veio o evento: `painel` (alguém na tela), `sistema` (a própria plataforma, como nas chamadas e gravações) ou `api`. Use o `origem` para o seu sistema não responder ao eco do que ele mesmo mandou pela API.

◽ `enviadoEm` — a hora em que o aviso foi enviado.

◽ `backendURL` — o endereço do backend da sua instalação.

## Exemplo de payload de Mensagem

```json
{
  "acao": "mensagem-criada",
  "companyId": 8,
  "chat": {
    "id": 9,
    "uuid": "3f2a9c1e-5b7d-4e8a-9c0f-1a2b3c4d5e6f",
    "title": "Time de Vendas",
    "somenteAvisos": false,
    "imagem": null,
    "ownerId": 16,
    "participantes": [
      { "id": 16, "nome": "Ana Supervisora" },
      { "id": 18, "nome": "Bruno Vendas" }
    ]
  },
  "mensagem": {
    "id": 407,
    "chatId": 9,
    "remetente": { "id": 16, "nome": "Ana Supervisora" },
    "message": "Reunião às 15h para fechar a proposta",
    "mediaName": null,
    "mediaUrl": null,
    "quotedMsgId": null,
    "apagada": false,
    "editadaEm": null,
    "figurinhaId": null,
    "createdAt": "2026-10-27T09:17:53.895Z",
    "mencionados": [],
    "protocolos": []
  },
  "origem": "painel",
  "enviadoEm": "2026-10-27T09:17:53.957Z",
  "backendURL": "https://backend_url.com.br"
}
```

◽ `mensagem.remetente` — quem escreveu, com `id` e `nome`.

◽ `mensagem.message` — o texto. Numa mensagem com arquivo, `mediaName` e `mediaUrl` trazem o nome e o endereço do arquivo. Numa figurinha, também: `message` vem vazio.

◽ `mensagem.quotedMsgId` — a mensagem respondida, quando é uma resposta.

◽ `mensagem.mencionados` — os ids de quem foi marcado com `@`.

◽ `mensagem.editadaEm` — a hora da edição; numa mensagem que não foi editada, vem `null`.

◽ `mensagem.figurinhaId` — a figurinha enviada; numa mensagem comum, vem `null`.

◽ `mensagem.protocolos` — os números de protocolo citados na mensagem com `#`.

◽ No `mensagem-editada`, `mensagem` traz `id`, `chatId`, o texto novo em `message`, o texto de antes em `anterior` e a hora em `editadaEm`, e `por` diz quem editou.

◽ No `mensagens-entregues` e no `mensagens-lidas`, `por` diz quem recebeu ou leu, `em` traz a hora e `mensagens`, a lista de ids. Cada pessoa gera o seu aviso.

◽ No `mensagem-apagada`, `mensagem` traz só `id` e `chatId`, e `por` diz quem apagou. No `reacao`, vêm `por`, o `emoji` e `reacoes`, a lista inteira de reações da mensagem: reagir de novo com o mesmo emoji tira a reação.

## Exemplo de payload de Chamada

O aviso do fim da chamada traz a duração e quem participou.

```json
{
  "acao": "chamada-encerrada",
  "companyId": 8,
  "chat": {
    "id": 9,
    "uuid": "3f2a9c1e-5b7d-4e8a-9c0f-1a2b3c4d5e6f",
    "title": "Time de Vendas",
    "somenteAvisos": false,
    "imagem": null,
    "ownerId": 16,
    "participantes": [
      { "id": 16, "nome": "Ana Supervisora" },
      { "id": 18, "nome": "Bruno Vendas" }
    ]
  },
  "chamada": {
    "id": 9,
    "tipo": "chat",
    "ticketId": null,
    "iniciadaPorId": 16,
    "iniciadaEm": "2026-10-27T09:18:17.708Z",
    "encerradaEm": "2026-10-27T09:18:37.872Z",
    "duracaoSegundos": 20
  },
  "participantes": [
    { "nome": "Ana Supervisora", "userId": 16, "cliente": false, "entrouEm": "2026-10-27T09:18:17.718Z", "saiuEm": "2026-10-27T09:18:35.314Z" },
    { "nome": "Bruno Vendas", "userId": 18, "cliente": false, "entrouEm": "2026-10-27T09:18:23.945Z", "saiuEm": "2026-10-27T09:18:37.861Z" }
  ],
  "origem": "sistema",
  "enviadoEm": "2026-10-27T09:18:37.893Z",
  "backendURL": "https://backend_url.com.br"
}
```

◽ `chamada.tipo` — `chat` numa chamada do **Chat Interno**.

◽ `chamada.iniciadaPorId` — quem começou a chamada.

◽ `chamada.duracaoSegundos` e `chamada.encerradaEm` — preenchidos no `chamada-encerrada`; no `chamada-iniciada` vêm vazios, e o aviso traz `por`, com quem começou.

◽ `participantes` — só no `chamada-encerrada`: cada pessoa que entrou na chamada, com a hora em que entrou e saiu.

◽ `gravacao` — nos avisos de gravação. No `gravacao-iniciada`, `gravacao.automatica` é `false` quando alguém tocou em **Gravar a chamada**. No `gravacao-concluida`, `gravacao.url` é o endereço do vídeo, `gravacao.duracaoSegundos` a duração e `gravacao.messageId` a mensagem do vídeo na conversa.

◽ `transcricao` e `analise` — só no `gravacao-transcrita`: o texto inteiro da transcrição e da análise.

## Como saber que o aviso veio daqui

Todo aviso do **Webhook do Chat Interno** traz o cabeçalho `X-Chat-Interno-Evento`, que repete o evento. Com o **Token da Empresa** gerado, traz também o cabeçalho `X-Assinatura-Chat-Interno`: `sha256=` seguido do HMAC-SHA256 do corpo, calculado com o **Token da Empresa** como chave.

Para conferir, calcule o HMAC-SHA256 do corpo recebido com o seu **Token da Empresa** e compare com o valor do cabeçalho. O token não vai no corpo do aviso.

⚠️ O aviso não é repetido. Se o endereço não responder em 15 segundos, aquele aviso se perde. Responda rápido e deixe o processamento pesado para depois.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Webhook do Chat Interno avisa as mensagens dos clientes?** Não. O **Webhook do Chat Interno** cobre só as conversas internas da equipe. As mensagens dos clientes são avisadas pelos webhooks da Conexão e do Setor.
>
> **Atender uma chamada gera aviso no Webhook do Chat Interno?** Não. A chamada gera aviso quando começa (`chamada-iniciada`) e quando termina (`chamada-encerrada`). Quem entrou e quando aparece na lista `participantes` do aviso do fim.
>
> **Como evito que o meu sistema responda à própria mensagem no Webhook do Chat Interno?** Pelo campo `origem`. O que o seu sistema manda pela API chega com `origem` igual a `api`; ignore esses avisos para não responder ao próprio eco.
>
> **A transcrição de uma chamada gravada chega pelo Webhook do Chat Interno?** Sim. Quando a IA das gravações termina, chega o aviso `gravacao-transcrita`, com a transcrição e a análise inteiras. As mensagens que a IA põe na conversa também chegam, como `mensagem-criada`.
