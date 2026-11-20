# Webhook do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-do-consultorio
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook do Consultório

---

🧩 Quer que o sistema da sua clínica saiba na hora que uma consulta foi marcada, confirmada ou cancelada, que o paciente chegou à recepção ou que um pagamento entrou? O **Webhook do Consultório** avisa o seu sistema a cada evento do Consultório: consultas, recepção, pacientes, prontuário, documentos, cobrança, repasse e os cadastros.

O **Webhook do Consultório** cobre só o Consultório. As conversas com os pacientes são avisadas pelos webhooks da Conexão e do Setor.

⚠️ Os avisos vão com os dados completos do paciente e da consulta. Aponte o webhook para um sistema da clínica, protegido com o mesmo cuidado do prontuário.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Consultório  ›  Cadastros do consultório** e abra a aba **Webhook**.
>
> ➡️ Preencha a **URL do webhook** com o endereço do seu sistema e clique em **Salvar**.

## Onde ligar

🔘 **URL do webhook:** o endereço que recebe todos os eventos do Consultório da empresa. Em branco, nada é enviado. Ao salvar, a tela avisa *"Webhook salvo."*

O endereço precisa começar com **https://** e não pode apontar para a rede interna: endereços com **http://**, **localhost** ou IPs como **127.0.0.1**, **10.0.0.5** e **192.168.0.10** são recusados. Espaços antes e depois do endereço são tirados ao salvar. O seu sistema recebe **POST** com corpo em JSON.

## O campo que separa um aviso do outro

Tudo chega no mesmo endereço, e é o **`evento`** que diz o que aconteceu no Consultório. O mesmo nome vem em **`acao`**.                                                                                                                                  

| `evento` | O que aconteceu |
|---|---|
| `agendamento-criado` · `agendamento-alterado` · `agendamento-remarcado` | uma consulta foi marcada, mudou ou foi remarcada |
| `agendamento-confirmado` · `agendamento-cancelado` | a consulta foi confirmada ou cancelada |
| `agendamento-remarcacao-pedida` | o paciente pediu para remarcar a consulta |
| `agendamento-faltou` · `agendamento-atendido` · `agendamento-reaberto` | a consulta ficou como falta ou como atendida, ou foi reaberta |
| `bloqueio-criado` · `bloqueio-alterado` · `bloqueio-removido` | um horário bloqueado da agenda foi criado, mudou ou foi removido |
| `paciente-chegou` · `paciente-chamado` · `paciente-em-atendimento` | o paciente chegou à recepção, foi chamado ou entrou para o atendimento |
| `teleconsulta-iniciada` · `teleconsulta-encerrada` | a chamada da teleconsulta começou, ou ficou vazia e terminou |
| `teleconsulta-link-enviado` | o link da teleconsulta foi enviado ao paciente |
| `teleconsulta-entrada-pedida` · `teleconsulta-entrada-decidida` | o paciente pediu para entrar na teleconsulta, e o profissional aceitou ou recusou |
| `confirmacao-enviada` | a confirmação da consulta foi enviada ao paciente |
| `lembrete-enviado` · `lembrete-nao-enviado` | um lembrete da consulta foi enviado, ou não pôde ser enviado |
| `regra-de-lembrete-salva` · `regra-de-lembrete-removida` | um lembrete da aba **Confirmação** foi salvo ou removido |
| `paciente-criado` · `paciente-alterado` · `paciente-removido` | o cadastro de um paciente foi criado, mudou ou foi removido |
| `prontuario-registrado` | um registro entrou no prontuário |
| `prontuario-chave-criada` · `prontuario-chave-restaurada` | a chave do prontuário foi criada ou restaurada |
| `documento-emitido` · `documento-enviado` · `documento-cancelado` | um documento ou receita foi emitido, enviado ao paciente ou cancelado |
| `modelo-de-documento-criado` · `modelo-de-documento-alterado` · `modelo-de-documento-removido` | um modelo da aba **Documentos** foi criado, mudou ou foi removido |
| `valor-da-consulta-alterado` | o valor de uma consulta mudou |
| `cobranca-gerada` · `cobranca-cancelada` | a cobrança por link foi gerada ou cancelada |
| `pagamento-registrado` · `pagamento-confirmado` · `pagamento-estornado` | um pagamento entrou, foi confirmado ou foi estornado |
| `consulta-paga` | a consulta ficou quitada |
| `regra-de-repasse-salva` · `regra-de-repasse-removida` | uma regra da aba **Repasse** foi salva ou removida |
| `repasse-pago` · `repasse-desfeito` | um repasse foi marcado como pago ou desfeito |
| `profissional-criado` · `profissional-alterado` · `profissional-removido` | o cadastro de um profissional foi criado, mudou ou foi removido |
| `servico-criado` · `servico-alterado` · `servico-removido` | um serviço foi criado, mudou ou foi removido |
| `sala-criada` · `sala-alterada` · `sala-removida` | uma sala foi criada, mudou ou foi removida |
| `painel-criado` · `painel-alterado` · `painel-removido` | um painel da TV da recepção foi criado, mudou ou foi removido |
| `termo-publicado` | uma versão nova do termo de consentimento foi publicada |
| `acesso-a-agenda-alterado` | mudou quem vê qual agenda |
| `chave-da-api-criada` · `chave-da-api-revogada` | uma chave da aba **Integrações** foi criada ou revogada |

Todo aviso do **Webhook do Consultório** traz também:

◽ `id` — o código único do evento.

◽ `companyId` — a empresa.

◽ `ocorridoEm` — quando o evento aconteceu, com o fuso, como `2026-11-13T11:09:02-03:00`.

◽ `enviadoEm` — quando este envio foi feito, em UTC.

◽ `tentativa` — `1` no primeiro envio; `2`, `3` e assim por diante nas novas tentativas.

◽ `autor` — quem fez, com `tipo`, `id` e `nome`. O `tipo` é `usuario` quando alguém fez pela tela, e `sistema` quando foi a própria plataforma, como nos eventos da teleconsulta.

◽ `origem` — de onde veio o evento: `painel` (alguém na tela) ou `sistema`.

◽ `backendURL` — o endereço do backend da sua instalação.

Quando o evento muda a situação da consulta, como `agendamento-atendido` e `paciente-em-atendimento`, ele traz também `mudancas`, com os campos que mudaram, e `antes`, com o valor anterior: `"antes": {"status": "em_atendimento"}`.

## Exemplo de payload de Repasse

O aviso de um repasse marcado como pago:

```json
{
  "id": "8bb3186f-6fa8-4faf-9cf6-2f4b0775441c",
  "evento": "repasse-pago",
  "acao": "repasse-pago",
  "companyId": 8,
  "repasse": {
    "id": 2,
    "profissionalId": 1,
    "profissional": {
      "id": 1,
      "nome": "Ana Souza"
    },
    "valor": 52,
    "quantidade": 1,
    "observacao": "Pix de novembro",
    "pagoEm": "2026-11-13T14:09:02.384Z",
    "pagoPor": {
      "id": 11,
      "nome": "Carla Recepção"
    },
    "desfeitoEm": null,
    "desfeitoPor": null,
    "consultas": [
      {
        "agendamentoId": 2,
        "repasse": 52,
        "regra": {
          "id": 1,
          "tipo": "percentual",
          "valor": 40,
          "origem": "profissional"
        }
      }
    ]
  },
  "ocorridoEm": "2026-11-13T11:09:02-03:00",
  "autor": {
    "tipo": "usuario",
    "id": 11,
    "nome": "Carla Recepção"
  },
  "origem": "painel",
  "backendURL": "https://backend_url.com.br",
  "tentativa": 1,
  "enviadoEm": "2026-11-13T14:09:02.410Z"
}
```

## O que cada aviso traz a mais

◽ **Consulta** (`agendamento-criado`, `agendamento-atendido` e `paciente-em-atendimento`): `agendamento`, a consulta inteira — `codigo`, `status`, `modalidade`, o `link` da teleconsulta, `data`, `hora`, `horaFim`, `profissional`, `paciente`, `servico`, `sala` e as horas de cada passo (`chegouEm`, `atendimentoIniciadoEm`).

◽ **Teleconsulta** (`teleconsulta-iniciada`, `teleconsulta-entrada-pedida`, `teleconsulta-entrada-decidida` e `teleconsulta-encerrada`): o `agendamento` e a `chamada`. O pedido de entrada traz `pedido`, com o `nome` de quem pediu e `cliente` `true` para o paciente; a decisão traz também `aceita` (`true` ou `false`) e `por`, quem decidiu. A chamada encerrada traz `encerradaEm`, `duracaoSegundos` e os `participantes`, com a hora em que cada um entrou e saiu.

◽ **Prontuário** (`prontuario-registrado`): `registro`, com o `tipo`, o profissional e, na retificação, o `retificaId` do registro corrigido, e o `paciente`. O texto do registro não vai no aviso.

◽ **Sala** (`sala-criada`, `sala-alterada` e `sala-removida`): `sala`, com `id`, `nome`, `descricao` e `ativo`. A sala removida também chega completa.

◽ **Regra de repasse** (`regra-de-repasse-salva` e `regra-de-repasse-removida`): `regra`, com o `profissional` e o `servico` (`null` quando a regra vale para **Todos**), o `tipo` (`percentual` ou `fixo`), o `valor` e a `origem` (`profissional`, `servico` ou `par`). Na regra nova, `nova` vem `true`.

◽ **Repasse** (`repasse-pago` e `repasse-desfeito`): `repasse`, com o profissional, o `valor`, a `quantidade` de consultas, a `observacao`, quem pagou e quando (`pagoPor` e `pagoEm`), quem desfez e quando (`desfeitoPor` e `desfeitoEm`) e as `consultas`, cada uma com o `agendamentoId` e o `repasse`. No pago, cada consulta traz também a `regra` que valeu.

◽ **Pagamento** (`pagamento-registrado` e `pagamento-estornado`): o `agendamentoId`, o `pagamento` (forma, valor, situação e as horas da confirmação e do estorno) e a `cobranca` da consulta como ficou — `valor`, `pago`, `falta`, `situacao` e a lista de `pagamentos`. O estorno traz também `devolvidoNoProvedor`, que vem `false` no pagamento registrado à mão.

◽ **Consulta paga** (`consulta-paga`): o `agendamentoId` e a `cobranca` quitada. Chega junto com o `pagamento-registrado` do pagamento que completou o valor.

## Entrega e novas tentativas

O aviso conta como entregue quando o seu sistema responde **2xx** em até **15 segundos**. Se não, o evento é enviado de novo depois de 1 min, 5 min, 30 min, 2 h, 6 h e 24 h, em sete tentativas ao todo. Depois da última, os administradores da empresa são avisados no sino.

Na nova tentativa, o `ocorridoEm` continua o de quando o evento aconteceu; o `enviadoEm` e a `tentativa` são os do novo envio.

⚠️ Um evento que precisou de nova tentativa chega **depois** dos eventos que vieram a seguir. Para saber a ordem em que as coisas aconteceram, use o `ocorridoEm`, não a ordem de chegada, e use o `id` para reconhecer um evento que você já recebeu.

## Como saber que o aviso veio daqui

Todo aviso vai assinado com o **Token da Empresa**, e o token não vai no corpo do aviso. Os cabeçalhos:                              

| Cabeçalho | O que leva |
|---|---|
| `X-Consultorio-Evento` | o nome do evento |
| `X-Assinatura-Consultorio` | a assinatura do corpo, em HMAC-SHA256 com o **Token da Empresa** |
| `X-Consultorio-Evento-Id` | o `id` do evento |
| `X-Consultorio-Enviado-Em` | a hora do envio |
| `X-Consultorio-Tentativa` | o número da tentativa |

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Webhook do Consultório avisa as mensagens dos pacientes?** Não. Ele cobre só os eventos do Consultório. As mensagens são avisadas pelos webhooks da Conexão e do Setor.
>
> **Recebi um aviso com `tentativa` 2. O que aconteceu com o primeiro?** O primeiro envio não contou como entregue, e o evento foi enviado de novo. O `ocorridoEm` é o de quando ele aconteceu, e o `enviadoEm`, o do novo envio.
>
> **Como sei quem fez a mudança?** Pelo `autor`, com o `tipo`, o `id` e o `nome` de quem fez. Nos eventos que a própria plataforma gera, como os da teleconsulta, o `tipo` é `sistema`.
>
> **Como sei que o paciente chegou à recepção?** Pelo aviso `paciente-chegou`. Quando ele é chamado, chega o `paciente-chamado`.
>
> **O texto do prontuário chega no meu sistema?** Não. O `prontuario-registrado` avisa que um registro entrou, com o tipo e o profissional, mas sem o texto.
>
> **Quando chega o `teleconsulta-encerrada`?** Quando a chamada fica vazia, depois que o último participante sai. Ele não depende de a consulta ser finalizada na **Recepção**: a consulta finalizada chega como `agendamento-atendido`.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Endereço recusado ao salvar:** a tela avisa *"A URL do webhook precisa começar com https:// e não pode apontar para o próprio servidor."* **Solução:** use um endereço **https://** do seu sistema que a internet alcance; http://, localhost e endereços da rede interna não são aceitos.
>
> **Avisos fora de ordem:** um evento que precisou de nova tentativa chegou depois dos seguintes. **Solução:** ordene os eventos pelo `ocorridoEm`.
