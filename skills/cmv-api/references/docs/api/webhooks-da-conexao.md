# Webhook da Conexão

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhooks-da-conexao
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook da Conexão

---

🧩 O **Webhook da Conexão** avisa o seu sistema sobre tudo o que passa por um canal — todas as conversas daquela Conexão, de qualquer Setor. É o aviso mais amplo da seção, e o caminho natural de quem quer espelhar o atendimento inteiro em outro lugar.

O aviso é enviado toda vez que a Conexão:

◽ **recebe** uma mensagem.

◽ **envia** uma mensagem.

◽ tem o **atendimento aberto ou encerrado**.

◽ tem o **atendimento mexido pelo atendente** — assumido, transferido de Setor ou encerrado na tela.

◽ tem uma **tag** alterada no atendimento, pela tela ou por um fluxo.

◽ tem uma **videochamada** aberta a partir de um atendimento — quando ela começa e termina, e quando a gravação dela começa, fica pronta ou é transcrita.

◽ tem um **operador convidado** para o atendimento, ou um convidado que saiu dele.

## Onde ligar

Acesse o menu **Conexões  ›  editar a Conexão  ›  aba Integrações** e preencha o campo **Webhook** com o endereço do seu sistema.

Esse endereço precisa aceitar **POST** com corpo em JSON.

![Campo de URL do Webhook no cadastro da Conexão](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6abbf9fc87484.png)

⚠️ **Estes avisos carregam o token da Conexão** (nos campos `token_origin`, `connection_token` e `ticketData.whatsapp.token`), além do telefone e do nome do contato. Aponte apenas para endereços seus, sob HTTPS, e não registre o corpo inteiro em log acessível a terceiros.

## O campo que separa um aviso do outro

Tudo chega no mesmo endereço, e é o **`acao`** que diz o que aconteceu:                                                  

| `acao` | O que aconteceu |
|---|---|
| `start` | chegou uma mensagem — é o aviso do conteúdo como ele veio |
| `from_internal` | a mensagem foi gravada no atendimento — canal **Oficial** |
| `fila-data` | a mensagem foi gravada no atendimento — canais por **QR Code** |
| `open` · `closed` | o atendimento abriu ou foi encerrado |
| `action_from_user` | o atendente mexeu no atendimento pela tela |
| `tag-sync` | as tags do atendimento mudaram pela tela |
| `tag-sync-flow-add` · `tag-sync-flow-remove` | uma tag entrou ou saiu por um fluxo |
| `chamada-iniciada` · `chamada-encerrada` | uma videochamada do atendimento começou ou terminou |
| `gravacao-iniciada` · `gravacao-concluida` · `gravacao-transcrita` | a gravação da videochamada começou, ficou pronta, ou a IA terminou a transcrição e a análise |
| `convidado-adicionado` · `convidado-removido` | um operador foi convidado para o atendimento, ou saiu dele |

⚠️ **Nos avisos de tag a chave se chama `action`.** Alguns trazem `acao` e `action` juntos, com o mesmo valor; outros só `action`. Quem verifica apenas `acao` deixa de reconhecer parte deles.

📌 **Os campos abaixo não são a lista completa do payload.** Cada aviso traz dezenas de campos, e eles mudam de uma versão da plataforma para outra. Estão aqui os que sustentam uma integração: os que identificam o evento, o atendimento e o conteúdo.

## Exemplo de payload de Mensagem

Uma mensagem **recebida** gera **dois avisos**, com um segundo de diferença: primeiro o `start`, com o conteúdo como veio; depois o que grava a mensagem no atendimento — `from_internal` no canal Oficial, `fila-data` nos canais por QR Code. A mensagem **enviada** costuma gerar só o segundo.

É esse segundo aviso que vale a pena tratar: ele traz o texto final e o identificador da mensagem.

```json
{
  "acao": "from_internal",
  "sender": "554199999999",
  "name": "José Cliente",
  "chamadoId": 15321,
  "queueId": 5,
  "fromMe": false,
  "isGroup": false,
  "companyId": 8,
  "defaultWhatsapp_x": 27,
  "backendURL": "https://backend_url.com.br",
  "token_origin": "SEU_TOKEN_DA_CONEXAO",
  "mensagem": {
    "id": 1669479,
    "wid": "wamid.HBgMNTU0MTk5OTk5OTk5FQIAEhggQTUwOTY3QTAw",
    "body": "Está faltando acento no glúten",
    "fromMe": false,
    "userId": null,
    "fromApp": false,
    "mediaType": null,
    "mediaUrl": null
  },
  "ticketData": { "id": 15321, "status": "open", "protocolo": "54212" }
}
```

◽ `sender` — o número do cliente, sempre.

◽ `name` — muda de conteúdo conforme a direção: quando a mensagem foi **recebida**, traz o nome do cliente; quando foi **enviada**, traz o celular dele.

◽ `chamadoId` — o identificador do atendimento (número do ticket). É a chave para amarrar mensagens da mesma conversa.

◽ `fromMe` — **é o campo que diz a direção**: `false` quando o cliente mandou, `true` quando a mensagem foi enviada daqui.

◽ `queueId` — o Setor do atendimento.

◽ `backendURL` — o endereço do backend da sua instalação.

◽ `mensagem` — **muda de formato conforme o aviso.** No `from_internal` é um **objeto** com a mensagem já gravada. No `start` é uma **lista** com as partes do conteúdo. Nos canais por QR Code o texto está em `msg.message`, e não aqui.

◽ `mensagem.body` — o texto da mensagem. Quando o cliente manda um áudio e a transcrição está ligada, é aqui que o texto transcrito aparece.

◽ `mensagem.wid` — o identificador da mensagem no canal. É por ele que se evita processar a mesma mensagem duas vezes.

◽ `mensagem.userId` e `mensagem.fromApp` — dizem **quem** enviou, quando `fromMe` é `true`: `userId` preenchido é um atendente pela tela; `fromApp` é alguém pelo celular da conta.

◽ `ticketData` — o retrato do atendimento no momento do evento. Vale a pena guardar `ticketData.status` (`open`, `pending` ou `closed`), `ticketData.protocolo` (o número que o cliente enxerga), `ticketData.userId` e `ticketData.contact.number`.

## Exemplo de payload de Videochamada

Uma videochamada aberta a partir do atendimento gera um aviso quando começa (`chamada-iniciada`) e outro quando termina (`chamada-encerrada`). Com a gravação ligada, vêm também `gravacao-iniciada`, `gravacao-concluida` e, com a IA nas gravações, `gravacao-transcrita`. A mensagem com o link que o atendente envia ao cliente gera, além disso, os avisos comuns de mensagem enviada.

O aviso do fim é o que fecha a conta da chamada: duração e quem participou.

```json
{
  "acao": "chamada-encerrada",
  "sender": "554199999999",
  "chamadoId": 15321,
  "companyId": 8,
  "chamada": {
    "id": 14,
    "tipo": "ticket",
    "ticketId": 15321,
    "iniciadaPorId": 5,
    "iniciadaEm": "2026-10-27T09:52:07.041Z",
    "encerradaEm": "2026-10-27T09:54:00.010Z",
    "duracaoSegundos": 113
  },
  "ticket": {
    "id": 15321,
    "status": "open",
    "userId": 5,
    "queueId": 3,
    "contact": { "id": 412, "name": "José Cliente", "number": "554199999999" }
  },
  "participantes": [
    { "nome": "Ana Atendente", "userId": 5, "cliente": false, "entrouEm": "2026-10-27T09:52:07.056Z", "saiuEm": "2026-10-27T09:53:11.676Z" },
    { "nome": "José Cliente", "userId": null, "cliente": true, "entrouEm": "2026-10-27T09:52:21.199Z", "saiuEm": "2026-10-27T09:53:02.587Z" }
  ],
  "backendURL": "https://backend_url.com.br",
  "token_origin": "SEU_TOKEN_DA_CONEXAO"
}
```

◽ `chamada.tipo` — `ticket` numa videochamada aberta a partir do atendimento.

◽ `chamada.ticketId` e `chamadoId` — o atendimento em que a videochamada começou.

◽ `chamada.duracaoSegundos` e `chamada.encerradaEm` — preenchidos no `chamada-encerrada`; no `chamada-iniciada` vêm vazios.

◽ `ticket` — o atendimento, com o contato, o atendente, o Setor e a Conexão.

◽ `participantes` — só no `chamada-encerrada`: cada pessoa que entrou, com a hora em que entrou e saiu. `cliente: false` é alguém da equipe; `cliente: true` é quem entrou pelo link — o cliente e os convidados de fora, que vêm com `userId` vazio. Com a gravação ligada, a lista pode trazer também uma entrada sem nome, com `cliente: true`, que entra junto com a gravação.

◽ `link` — só no `chamada-iniciada`: o link de entrada do cliente, o mesmo que o atendente envia.

◽ `gravacao` — nos avisos de gravação. No `gravacao-concluida`, `gravacao.url` é o endereço do vídeo, `gravacao.duracaoSegundos` a duração da gravação e `gravacao.messageId` a mensagem do vídeo na conversa.

◽ `transcricao` e `analise` — só no `gravacao-transcrita`: o texto inteiro da transcrição e da análise.

## Exemplo de payload de Convidado

Cada operador convidado para o atendimento gera um aviso `convidado-adicionado`. Quando o convidado sai, chega um `convidado-removido`: seja porque alguém retirou o convite, seja porque o atendimento foi finalizado com a opção de remover os convidados ligada.

```json
{
  "acao": "convidado-adicionado",
  "sender": "554199999999",
  "chamadoId": 15321,
  "companyId": 8,
  "convidado": { "id": 8, "nome": "Ana Atendente" },
  "por": { "id": 5, "nome": "Carlos Supervisor" },
  "motivo": "convite",
  "ticket": { "id": 15321, "uuid": "0a1b2c3d-1111-4222-8333-444455556666", "status": "open", "userId": 5, "queueId": 3 },
  "backendURL": "https://backend_url.com.br",
  "token_origin": "SEU_TOKEN_DA_CONEXAO"
}
```

◽ `convidado` — o operador que entrou ou saiu, com o número e o nome.

◽ `por` — quem convidou ou quem retirou o convite. Vem vazio (`null`) quando o convidado saiu porque o atendimento foi finalizado.

◽ `motivo` — por que o aviso foi enviado: `convite` quando o operador foi convidado, `removido` quando alguém retirou o convite, `atendimento-finalizado` quando ele saiu com a finalização do atendimento.

◽ `ticket` — o atendimento naquele momento. No aviso de `atendimento-finalizado`, `ticket.status` já vem `closed`, com `ticket.userId` e `ticket.queueId` vazios.

◽ `chamadoId` — o identificador do atendimento, o mesmo dos avisos de mensagem.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Como sei se a mensagem foi enviada ou recebida?** Pelo campo `fromMe`: `false` é do cliente para você, `true` é de você para o cliente. Não use o campo `name` para isso — ele muda de conteúdo conforme a direção.
>
> **Como sei quanto durou uma videochamada pelo Webhook da Conexão?** Pelo aviso `chamada-encerrada`: `chamada.duracaoSegundos` traz a duração da chamada, e a lista `participantes` traz quando cada pessoa entrou e saiu.
>
> **Como sei pelo Webhook da Conexão por que um operador convidado saiu do atendimento?** Pelo campo `motivo` do aviso `convidado-removido`: `removido` quando alguém retirou o convite, `atendimento-finalizado` quando ele saiu com a finalização do atendimento.
