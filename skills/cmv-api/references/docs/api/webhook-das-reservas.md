# Webhook das Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-das-reservas
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook das Reservas

---

🧩 Quer que o sistema da sua empresa saiba na hora que uma reserva foi feita, confirmada, remarcada ou cancelada, que um pagamento entrou ou que um pacote foi vendido? O **Webhook das Reservas** avisa o seu sistema a cada mudança nas Reservas, com os dados completos.

O **Webhook das Reservas** cobre só as Reservas. As conversas com os clientes são avisadas pelos webhooks da Conexão e do Setor.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Reservas** e abra a aba **Webhook**.
>
> ➡️ Preencha a **URL do webhook** com o endereço do seu sistema e clique em **Salvar**.

## Onde ligar

🔘 **URL do webhook:** o endereço que recebe todos os eventos das Reservas da empresa. Ele precisa começar com **https://**; outro endereço é recusado com *"Use um endereço https:// válido para o webhook das Reservas."* Ao salvar, a tela avisa *"Webhook salvo."* Apagar o endereço e salvar desliga os avisos.

## O nome do evento

Tudo chega no mesmo endereço, e o nome do evento vai no cabeçalho `X-Reservas-Evento`. O mesmo nome vem no corpo do aviso, em **`acao`**.                                                                              

| Evento | O que aconteceu |
|---|---|
| `reserva-criada` · `reserva-alterada` · `reserva-remarcada` | uma reserva foi criada, mudou ou foi remarcada |
| `reserva-confirmada` · `reserva-concluida` · `reserva-nao-compareceu` · `reserva-cancelada` | a reserva foi confirmada, concluída, marcada como não compareceu ou cancelada |
| `serie-criada` · `serie-cancelada` | uma série de reservas foi criada ou cancelada |
| `aviso-enviado` · `aviso-nao-enviado` | um aviso ao cliente foi enviado, ou não pôde ser enviado |
| `avisos-alterados` | os avisos da aba **Avisos** mudaram |
| `espera-criada` · `espera-avisada` · `espera-atendida` · `espera-removida` | alguém entrou na lista de espera, foi avisado da vaga, foi marcado como atendido ou foi removido |
| `cobranca-gerada` · `cobranca-cancelada` | uma cobrança por link foi gerada ou cancelada |
| `pagamento-registrado` · `pagamento-confirmado` · `pagamento-estornado` | um pagamento entrou, foi confirmado ou foi estornado |
| `sinal-pago` · `sinal-expirado` | o sinal foi pago, ou o prazo para pagar venceu |
| `pacote-criado` · `pacote-alterado` · `pacote-removido` | um pacote da aba **Pacotes** foi criado, mudou ou foi removido |
| `pacote-vendido` · `pacote-cancelado` · `pacote-esgotado` | um pacote foi vendido a um cliente, foi cancelado ou teve o último crédito usado |
| `recurso-criado` · `recurso-alterado` · `recurso-removido` | um recurso foi criado, mudou ou foi removido |
| `oferta-criada` · `oferta-alterada` · `oferta-removida` | uma oferta foi criada, mudou ou foi removida |
| `disponibilidade-alterada` | os horários de um recurso mudaram |
| `bloqueio-criado` · `bloqueio-alterado` · `bloqueio-removido` | um bloqueio foi criado, mudou ou foi removido |
| `configuracao-alterada` | a configuração das Reservas mudou |
| `agenda-externa-falhou` | a ligação de um recurso com a agenda de fora falhou |

## O que chega no corpo

O seu sistema recebe **POST** com corpo em JSON. Todo aviso do **Webhook das Reservas** traz:

◽ `acao` — o nome do evento, o mesmo do cabeçalho `X-Reservas-Evento`.

◽ `companyId` — a empresa.

◽ `origem` — de onde veio a mudança: `painel` quando alguém fez pela tela, e `sistema` quando foi a própria plataforma, como a reserva confirmada depois do sinal pago.

◽ `enviadoEm` — quando o aviso foi enviado, em UTC.

◽ `backendURL` — o endereço do backend da sua instalação.

Junto vem o registro de que o aviso trata, já como ficou depois da mudança, como `reserva`, `bloqueio` ou `pagamento`. Quando uma reserva ou um bloqueio muda (`reserva-alterada`, `reserva-remarcada` e `bloqueio-alterado`), o aviso traz também `antes`, com o registro inteiro como estava antes da mudança.

## Exemplo de payload de Reserva

O aviso de uma reserva criada pela equipe, aguardando o pagamento do sinal:

```json
{
  "acao": "reserva-criada",
  "companyId": 8,
  "reserva": {
    "id": 51,
    "codigo": "K7QM2XRA",
    "situacao": "pendente",
    "origem": "painel",
    "ofertaId": 4,
    "oferta": {
      "id": 4,
      "nome": "Sala de reunião",
      "cor": null
    },
    "recursoId": 2,
    "recurso": {
      "id": 2,
      "nome": "Sala Azul",
      "tipo": "sala"
    },
    "contactId": null,
    "clienteNome": "Maria Silva",
    "clienteTelefone": null,
    "clienteEmail": null,
    "pessoas": 1,
    "inicio": "2026-11-25T11:00:00.000Z",
    "fim": "2026-11-25T12:00:00.000Z",
    "data": "2026-11-25",
    "horaInicio": "08:00",
    "horaFim": "09:00",
    "modo": "horario",
    "noites": null,
    "dataSaida": "2026-11-25",
    "observacao": "Reunião com a equipe",
    "preco": 100,
    "sinalValor": 30,
    "sinalAte": "2026-11-16T17:37:22.469Z",
    "motivoCancelamento": null,
    "canceladaEm": null,
    "criadoPorId": 11,
    "pacoteClienteId": null,
    "pacote": null,
    "serieId": null,
    "serieOrdem": null,
    "serie": null
  },
  "origem": "painel",
  "enviadoEm": "2026-11-16T17:32:22.489Z",
  "backendURL": "https://backend_url.com.br"
}
```

## O que cada aviso traz a mais

◽ **Reserva** (`reserva-criada`, `reserva-alterada`, `reserva-remarcada`, `reserva-confirmada`, `reserva-concluida` e `reserva-cancelada`): `reserva`, a reserva inteira — `codigo`, `situacao`, a `oferta` e o `recurso`, o cliente (`clienteNome`, `clienteTelefone`, `clienteEmail` e `contactId`), `pessoas`, `preco`, o sinal (`sinalValor` e `sinalAte`), o cancelamento (`motivoCancelamento` e `canceladaEm`) e o pacote e a série, quando a reserva usa um deles.

◽ **Pagamento** (`pagamento-registrado` e `pagamento-estornado`): o `reservaId`, o `pagamento` (forma, valor, situação e as horas da confirmação e do estorno) e a `cobranca` da reserva como ficou — `tipo`, `valor`, `pago`, `falta`, `situacao` e a lista de `pagamentos`. O estorno traz também `devolvidoNoProvedor`, que vem `false` no pagamento registrado à mão.

◽ **Sinal pago** (`sinal-pago`): a `reserva` e a `cobranca` quitada.

◽ **Bloqueio** (`bloqueio-criado`, `bloqueio-alterado` e `bloqueio-removido`): `bloqueio`, com o `recursoId`, o `inicio`, o `fim` e o `motivo`. O bloqueio removido também chega completo.

Na reserva e no bloqueio, `inicio` e `fim` vêm em UTC. Na reserva, `data`, `horaInicio` e `horaFim` trazem o horário como aparece na agenda das Reservas.

## Qual aviso chega em cada mudança

Registrar o pagamento do sinal de uma reserva que aguarda o sinal gera três avisos seguidos, nesta ordem: `pagamento-registrado`, `reserva-confirmada` e `sinal-pago`. O `reserva-confirmada` chega com `origem` `sistema`, porque quem confirmou a reserva foi a plataforma.

Remarcar uma reserva gera só o `reserva-remarcada`, com o horário anterior em `antes`. Mudar outro dado da reserva, como a observação, gera o `reserva-alterada`.

## Como saber que o aviso veio daqui

Todo aviso vai assinado com o **Token da Empresa**. Nas palavras da tela: *"O nome do evento vai no cabeçalho X-Reservas-Evento e a assinatura (sha256= e o HMAC do corpo com o token da empresa) em X-Assinatura-Reservas."*                  

| Cabeçalho | O que leva |
|---|---|
| `X-Reservas-Evento` | o nome do evento |
| `X-Assinatura-Reservas` | `sha256=` e a assinatura do corpo, em HMAC com o **Token da Empresa** |

Para conferir, calcule o HMAC-SHA256 do corpo recebido com o seu **Token da Empresa** e compare com o valor depois de `sha256=`.

Sem o **Token da Empresa**, os avisos não são enviados. Gere o token no menu **Configurações  ›  Token da Empresa**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Webhook das Reservas avisa as mensagens dos clientes?** Não. Ele cobre só os eventos das Reservas. As mensagens são avisadas pelos webhooks da Conexão e do Setor.
>
> **Como sei qual evento chegou?** Pelo cabeçalho `X-Reservas-Evento` ou pelo `acao` do corpo, que levam o nome do evento, como `reserva-confirmada`.
>
> **Como sei de onde veio a mudança na reserva?** Pelo `origem` do aviso do **Webhook das Reservas**: `painel` quando alguém fez pela tela, e `sistema` quando foi a própria plataforma.
>
> **Por que chegaram três avisos ao registrar o sinal da reserva?** Porque o sinal pago confirma a reserva. Chegam o `pagamento-registrado`, o `reserva-confirmada` e o `sinal-pago`, nessa ordem.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Endereço recusado ao salvar:** a tela avisa *"Use um endereço https:// válido para o webhook das Reservas."* **Solução:** use um endereço do seu sistema que comece com **https://**.
>
> **Avisos parados:** a aba avisa que os avisos estão parados por falta do token. **Solução:** gere o **Token da Empresa** no menu **Configurações  ›  Token da Empresa**.
