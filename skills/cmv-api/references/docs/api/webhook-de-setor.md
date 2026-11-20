# Webhook do Setor

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-de-setor
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook do Setor

---

🧩 O **Webhook do Setor** avisa o seu sistema sobre o que acontece nos atendimentos de **um Setor**. É o recorte de quem só se interessa por uma parte da operação — a triagem, o time de vendas, o financeiro — e não quer o canal inteiro.

O aviso é enviado toda vez que um atendimento daquele Setor:

◽ **recebe** uma mensagem.

◽ **envia** uma mensagem.

◽ **chega** ao Setor — quando entra nele pela Conexão ou é transferido para ele, por qualquer caminho.

◽ tem uma **tag** alterada.

◽ ganha uma **mensagem interna** ou uma linha no **Registro do atendimento**.

⚠️ **Com o webhook da Conexão ligado ao mesmo tempo, a mensagem é avisada duas vezes.** Enquanto o atendimento está no Setor escolhido, os dois disparam; fora dele, só o da Conexão. Os dois avisos da mesma mensagem chegam com o mesmo `eventoId`, e é por ele que o seu sistema descarta o repetido.

## Onde ligar

Acesse o menu **Setores & Chatbot  ›  editar o Setor** e preencha o campo **URL do Webhook** com o endereço do seu sistema.

Esse endereço precisa aceitar **POST** com corpo em JSON.

⚠️ **Estes avisos carregam o token da Conexão** (nos campos `token_origin`, `connection_token` e `ticketData.whatsapp.token`), além do telefone e do nome do contato. Aponte apenas para endereços seus, sob HTTPS, e não registre o corpo inteiro em log acessível a terceiros.

## O campo que separa um aviso do outro

Tudo chega no mesmo endereço, e é o **`acao`** que diz o que aconteceu:                              

| `acao` | O que aconteceu |
|---|---|
| `queue_webhook` | chegou uma mensagem — é o aviso do conteúdo como ele veio |
| `queue_webhook_from_internal` | a mensagem foi gravada no atendimento |
| `queue_webhook_update` | o atendimento chegou ao Setor: entrou nele pela Conexão ou foi transferido para ele |
| `tag-sync` | as tags do atendimento mudaram |
| `comunicacao_interna` | uma mensagem interna ou uma linha do Registro do atendimento foi gravada |

⚠️ **No aviso de tag a chave se chama `action`**, e não `acao`. Quem verifica apenas `acao` deixa de reconhecê-lo.

◽ No `comunicacao_interna`, a linha gravada vem em `comunicacaoInterna`: `id`, `wid`, `texto`, `tipo` (`nota` para a mensagem interna, `registro` para a linha do Registro do atendimento), `autor` (quem escreveu, ou `null`) e `criadaEm`.

## Os campos que identificam cada aviso

Todo aviso do **Webhook do Setor** traz, além do `acao`, quatro campos que identificam a entrega:

◽ `eventoId` — o código do fato. É o mesmo em todos os endereços que recebem aquele fato, inclusive nas mensagens, quando o webhook da Conexão e o do Setor estão ligados juntos. **É por ele que se descarta o aviso repetido:** guarde os `eventoId` já tratados e ignore o que voltar.

◽ `sequencia` — o número da entrega **naquele endereço**. Cada endereço cadastrado tem a sua própria conta, que sobe de 1 em 1 a cada aviso. Recebeu o 41 e depois o 43? O 42 se perdeu.

◽ `enviadoEm` — a hora do envio, com milissegundos.

◽ `origemDoEvento` — quem fez o que gerou o aviso. Por exemplo: `contato` (o que o cliente mandou ou fez), `painel` (o atendente, pela tela), `flowbuilder` (um fluxo), `chatbot` (o menu de Setores e o chatbot do Setor), `ia` (a IA da plataforma), `agendamento` (um agendamento), `sistema` (as mensagens e as regras automáticas da plataforma) e `api` (uma chamada da sua integração). É o campo que separa o aviso de algo que a sua própria integração fez.

Quando a `sequencia` pula um número, o aviso que faltou pode ser buscado de novo pela API, por até **7 dias**: `GET /api/webhook-da-conexao/entregas`, com o **Token da Empresa**, informando em `destino` a **URL do Webhook** do Setor, exatamente como está cadastrada, e em `desde` o último número que chegou.

📌 **Os campos abaixo não são a lista completa do payload.** Cada aviso traz dezenas de campos, e eles mudam de uma versão da plataforma para outra.

## Exemplo de payload de Mensagem

Uma mensagem **recebida** gera **dois avisos**, com um segundo de diferença: primeiro o `queue_webhook`, com o conteúdo como veio; depois o `queue_webhook_from_internal`, que grava a mensagem no atendimento. A mensagem **enviada** costuma gerar só o segundo.

É esse segundo aviso que vale a pena tratar: ele traz o texto final e o identificador da mensagem.

```json
{
  "acao": "queue_webhook_from_internal",
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
  "eventoId": "9a3f2c1e-5b7d-4e8a-9c0f-1d2e3f4a5b6c",
  "sequencia": 42,
  "enviadoEm": "2026-11-12T10:53:19.570Z",
  "origemDoEvento": "contato",
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

◽ `queueId` — o Setor do atendimento. É ele que decide se este aviso é enviado.

◽ `sender` — o número do cliente, sempre.

◽ `name` — muda de conteúdo conforme a direção: quando a mensagem foi **recebida**, traz o nome do cliente; quando foi **enviada**, traz o celular dele.

◽ `chamadoId` — o identificador do atendimento (número do ticket). É a chave para amarrar mensagens da mesma conversa.

◽ `fromMe` — **é o campo que diz a direção**: `false` quando o cliente mandou, `true` quando a mensagem foi enviada daqui.

◽ `backendURL` — o endereço do backend da sua instalação.

◽ `mensagem` — **muda de formato conforme o aviso.** No `queue_webhook_from_internal` é um **objeto** com a mensagem já gravada. No `queue_webhook` é uma **lista** com as partes do conteúdo. Nos canais por QR Code o texto está em `msg.message`, e não aqui.

◽ `mensagem.body` — o texto da mensagem. Quando o cliente manda um áudio e a transcrição está ligada, é aqui que o texto transcrito aparece.

◽ `mensagem.wid` — o identificador da mensagem no canal. Ele não serve para descartar aviso repetido: a mesma mensagem gera mais de um aviso, e cada aviso tem o seu `eventoId`.

◽ `mensagem.userId` e `mensagem.fromApp` — dizem **quem** enviou, quando `fromMe` é `true`: `userId` preenchido é um atendente pela tela; `fromApp` é alguém pelo celular da conta.

◽ `ticketData` — o retrato do atendimento no momento do evento. Vale a pena guardar `ticketData.status` (`open`, `pending` ou `closed`), `ticketData.protocolo` (o número que o cliente enxerga), `ticketData.userId` e `ticketData.contact.number`.

## Aviso de chegada ao Setor

O Setor **novo** recebe um `queue_webhook_update` toda vez que um atendimento entra nele, venha de onde vier: na entrada pela Conexão ou numa transferência pela tela, pelo FlowBuilder, pelo menu de Setores da Conexão, pelo chatbot do Setor, pela IA da plataforma, pelas regras automáticas (como mover após inatividade e o tempo de escala), por um agendamento ou pela sua integração.

◽ `ticketData.queueId` — o Setor novo, em número.

◽ `ticketData.userId` e `ticketData.status` — o atendente e o status do atendimento depois da troca.

◽ `origemDoEvento` — por onde veio a troca: `painel` (a tela), `flowbuilder` (um fluxo), `chatbot` (o menu de Setores e o chatbot do Setor), `ia`, `sistema` (as regras automáticas), `agendamento` ou `api` (a sua integração).

◽ Com o webhook da Conexão ligado, a Conexão recebe a mesma troca como `action_from_user`, com outro `eventoId` e com o Setor de antes em `ticketData_completo.queueId`.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Com o webhook da Conexão e o do Setor ligados, como descarto o aviso repetido?** Pelo `eventoId`: a mesma mensagem chega com o mesmo código nos dois endereços. Guarde os códigos já tratados e ignore o que voltar.
>
> **Como sei pelo Webhook do Setor que um atendimento foi transferido para ele?** Pelo aviso `queue_webhook_update`, que chega ao Setor novo a cada entrada, com o caminho da troca em `origemDoEvento`.
>
> **Como sei se a mensagem foi enviada ou recebida?** Pelo campo `fromMe`: `false` é do cliente para você, `true` é de você para o cliente. Não use o campo `name` para isso — ele muda de conteúdo conforme a direção.
