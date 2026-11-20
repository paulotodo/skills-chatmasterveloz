# Webhook do PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-do-pdv
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook do PDV

---

🧩 Quer que o seu sistema saiba na hora que um pedido foi confirmado, pago, despachado ou entregue — ou que um produto chegou ao estoque mínimo? O **Webhook do PDV** avisa o seu sistema a cada evento de pedido, pagamento, caixa, estoque, entrega, taxa de entrega, categoria e setor de produção do PDV.

O **Webhook do PDV** cobre só o PDV. As conversas com os clientes são avisadas pelos webhooks da Conexão e do Setor.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança** e, na seção **Webhooks e integrações**, encontre o **Webhook do PDV**.
>
> ➡️ Preencha o endereço do seu sistema e clique em **Salvar**.

## Onde ligar

🔘 **Webhook do PDV (recebe os eventos de pedidos, pagamentos, caixa e estoque):** o endereço que recebe todos os eventos do PDV da empresa. Em branco, nada é enviado. Ao salvar, a tela avisa *"Webhook do PDV salvo."* e lista os eventos enviados.

O endereço precisa começar com http:// ou https://, sem espaços, e não pode apontar para a rede interna. Ele recebe **POST** com corpo em JSON.

## O campo que separa um aviso do outro

Tudo chega no mesmo endereço, e é o **`acao`** que diz o que aconteceu no PDV:                                                                                  

| `acao` | O que aconteceu |
|---|---|
| `pedido-criado` · `pedido-alterado` | um pedido nasceu (em rascunho ou já confirmado) ou foi mudado antes de confirmar |
| `pedido-confirmado` | o pedido foi confirmado |
| `nota-enviada` | a nota do pedido foi enviada ao cliente |
| `pedido-em-preparo` · `pedido-pronto` · `pedido-saiu` | o pedido avançou no **Painel de pedidos** |
| `pedido-voltou-etapa` | o pedido voltou uma etapa no **Painel de pedidos** |
| `pedido-impresso` | as vias do pedido foram enviadas para a impressora, pelo botão **Imprimir** |
| `rastreio-enviado` · `entregador-posicao` | o link do rastreio foi enviado ao cliente; o entregador mandou a localização |
| `pedido-entregue` · `pedido-nao-entregue` · `pedido-cancelado` | o pedido foi entregue, voltou da entrega ou foi cancelado |
| `pagamento-registrado` · `pagamento-confirmado` · `pagamento-estornado` | um pagamento entrou, foi confirmado pelo Asaas ou foi estornado |
| `pagamento-estorno-pendente` · `pagamento-estorno-cancelado` | o estorno pelo Asaas ficou aguardando autorização, ou a espera foi cancelada |
| `link-de-pagamento-gerado` | o pedido gerou o link de pagamento do Asaas |
| `repasse-da-plataforma` | a parte da plataforma numa cobrança do Asaas mudou de situação |
| `caixa-aberto` · `caixa-movimentado` · `caixa-fechado` | um caixa abriu, recebeu um movimento ou fechou |
| `estoque-movimentado` · `estoque-baixo` | o estoque de um produto mudou, ou chegou ao mínimo |
| `taxa-de-entrega-criada` · `taxa-de-entrega-alterada` · `taxa-de-entrega-removida` | a tabela de taxas por bairro mudou |
| `faixa-de-cep-criada` · `faixa-de-cep-alterada` · `faixa-de-cep-removida` | a tabela de frete por faixa de CEP mudou |
| `categoria-criada` · `categoria-alterada` · `categoria-removida` | uma categoria de produto foi criada, mudou ou foi apagada |
| `setor-criado` · `setor-alterado` · `setor-removido` | um setor de produção, como a cozinha ou o bar, foi criado, mudou ou foi apagado |

Todo aviso do **Webhook do PDV** traz também:

◽ `companyId` — a empresa.

◽ `origem` — de onde veio o evento, como `painel` (alguém na tela).

◽ `enviadoEm` — a hora em que o aviso foi enviado.

◽ `backendURL` — o endereço do backend da sua instalação.

## Exemplo de payload de Pedido

O aviso de um pedido que saiu para entrega:

```json
{
  "acao": "pedido-saiu",
  "companyId": 8,
  "pedido": {
    "id": 42,
    "numero": 42,
    "situacao": "saiu",
    "ticketId": 1207,
    "ticket": {
      "id": 1207,
      "uuid": "3f2a9c1e-5b7d-4e8a-9c0f-1a2b3c4d5e6f",
      "status": "open"
    },
    "contato": {
      "id": 399,
      "nome": "Maria Cliente",
      "numero": "5511999990000"
    },
    "vendedor": {
      "id": 16,
      "nome": "Ana Vendas"
    },
    "subtotal": 35.9,
    "descontoTipo": "valor",
    "descontoValor": 0,
    "desconto": 0,
    "acrescimo": 0,
    "entrega": "entrega",
    "taxaEntrega": 7.5,
    "enderecoEntrega": "Rua das Flores, 100",
    "bairroEntrega": "Centro",
    "agendadoPara": null,
    "observacao": null,
    "total": 43.4,
    "itens": [
      {
        "id": 25,
        "productId": 1,
        "nome": "Caneca",
        "sku": "CAN001",
        "tipo": "produto",
        "quantidade": 1,
        "precoUnitario": 35.9,
        "total": 35.9,
        "estoque": 21
      }
    ],
    "quantidadeDeItens": 1,
    "pagamento": "pendente",
    "valorPago": 0,
    "saldo": 43.4,
    "pagoEm": null,
    "pagamentos": [],
    "confirmadoEm": "2026-10-28T15:50:19.459Z",
    "enviadoEm": "2026-10-28T15:50:19.672Z",
    "preparandoEm": "2026-10-28T15:50:41.028Z",
    "prontoEm": "2026-10-28T15:50:49.637Z",
    "saiuEm": "2026-10-28T15:51:01.433Z",
    "entregueEm": null,
    "canceladoEm": null,
    "canceladoPor": null,
    "motivoCancelamento": null,
    "entregador": {
      "id": 30,
      "nome": "Carlos Entregas"
    },
    "comprovanteDaEntrega": null,
    "naoEntregue": null,
    "balcao": false,
    "rastreio": "https://seu-painel.com.br/rastreio/AbC123",
    "destino": null,
    "previsaoChegada": null,
    "createdAt": "2026-10-28T15:50:19.378Z"
  },
  "origem": "painel",
  "enviadoEm": "2026-10-28T15:51:01.464Z",
  "backendURL": "https://backend_url.com.br"
}
```

◽ `pedido` — o pedido inteiro: número, situação, cliente (`contato`), quem vendeu (`vendedor`), os valores, a entrega com o bairro e os `itens`, cada um com o `estoque` depois da venda.

◽ `pedido.situacao` — `rascunho`, `confirmado`, `preparando`, `pronto`, `saiu`, `entregue` ou `cancelado`; as horas de cada etapa ficam em `confirmadoEm`, `preparandoEm`, `prontoEm`, `saiuEm` e `entregueEm`.

◽ `pedido.pagamento` — `pendente`, em parte ou pago; `valorPago` e `saldo` dizem quanto entrou e quanto falta.

◽ `pedido.entregador` e `pedido.rastreio` — quem leva o pedido e o link do rastreio do cliente; `comprovanteDaEntrega` traz a localização e a foto depois da entrega.

◽ `pedido.agendadoPara` — a data e o horário combinados, no pedido agendado; `pedido.balcao` é `true` na venda de balcão.

◽ `pedido.ticket` — o atendimento onde o pedido foi montado; vazio na venda de balcão.

◽ `pedido.loja` e `pedido.cardapioId` — a vitrine online de onde veio o pedido: `loja` traz `id`, `slug` e `tipo` (`cardapio` ou `loja`). Na venda de balcão, no pedido montado na conversa e no criado pela API, `loja` vem `null`. Os dois campos vêm em todo aviso que leva o pedido: `pedido-*`, `pagamento-*`, `nota-enviada`, `rastreio-enviado` e `pedido-impresso`.

## O que cada aviso traz a mais

◽ **Pagamento:** `pagamento`, com a forma, o valor, o valor recebido, o troco e a situação.

◽ **Caixa:** `caixa`, com o fundo de troco e o esperado de cada forma; no fechamento, também o contado e a diferença.

◽ **Estoque** (`estoque-movimentado` e `estoque-baixo`): `movimento` (tipo, quantidade, saldo anterior e posterior, motivo e o pedido) e `produto` (estoque, estoque mínimo e `estoqueBaixo`).

◽ **Não entregue** (`pedido-nao-entregue`): o pedido, que volta à situação `pronto`, mais `entregador` e `motivo`.

◽ **Posição do entregador** (`entregador-posicao`): `entregador`, `posicao` (latitude, longitude, precisão e a hora) e `pedidos`, os pedidos que estão com ele.

◽ **Taxa de entrega:** `taxa`, com o bairro e o valor.

◽ **Faixa de CEP** (`faixa-de-cep-criada`, `faixa-de-cep-alterada` e `faixa-de-cep-removida`): `faixa`, com `id`, `nome`, `cepInicial`, `cepFinal`, `taxa` (o frete em reais, como `7.5`), `prazo` e `updatedAt`. A faixa removida também chega completa.

◽ **Pedido impresso** (`pedido-impresso`): `pedido` e `impressao`, com a `via` pedida, quantas vias da `cozinha` e do `cliente`, a `largura` da bobina e o `usuarioId` de quem imprimiu. A opção **Pedido** do botão **Imprimir** chega como `via` `cliente`, com uma via do `cliente` e nenhuma da `cozinha`; **Cozinha** chega como `cozinha` e **Ambos** como `ambas`. O **Imprimir sozinho** do **Painel de pedidos** chega como `via` `padrao`, com as vias da **Impressão térmica** das Opções do PDV.

◽ **Pedido que voltou uma etapa** (`pedido-voltou-etapa`): o pedido como ficou em `pedido` e o caminho em `etapa`, com `de` e `para`, nos valores de `pedido.situacao`: a etapa **Novo** do **Painel de pedidos** chega como `confirmado`. A hora da etapa desfeita volta a `null`: o pedido que volta de preparo para Novo chega com `preparandoEm` vazio, o que volta de pronto para preparo, com `prontoEm` vazio, e o que volta de saiu para pronto, com `saiuEm` vazio — e o `entregador` continua no pedido. O cliente não é avisado.

◽ **Repasse da plataforma** (`repasse-da-plataforma`): `pagamento`, com a situação da parte da plataforma em `pagamento.repasse` — `concluido`, `bloqueado` (o valor líquido não cobriu a taxa) ou `cancelado` — e o pedido como ficou em `pedido`.

## Como saber que o aviso veio daqui

Todo aviso do **Webhook do PDV** traz o cabeçalho `X-Pdv-Evento`, com o evento, e vai assinado com o **Token da Empresa** no cabeçalho `X-Assinatura-Pdv`. O token não vai no corpo do aviso.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Webhook do PDV avisa as mensagens dos clientes?** Não. O **Webhook do PDV** cobre só os eventos do PDV. As mensagens dos clientes são avisadas pelos webhooks da Conexão e do Setor.
>
> **Como sei que um pedido foi pago pelo link do Asaas?** Pelo aviso `pagamento-confirmado`, que chega quando o pagamento do link é baixado no pedido.
>
> **Como sei que a parte da plataforma numa cobrança do Asaas ficou bloqueada?** Pelo aviso `repasse-da-plataforma`, com `pagamento.repasse` em `bloqueado`: o valor líquido da cobrança não cobriu a taxa.
>
> **Recebo aviso quando um produto está acabando?** Sim. Quando um movimento deixa o produto no estoque mínimo ou abaixo dele, chega o aviso `estoque-baixo`, com o produto e o movimento.
>
> **Como meu sistema sabe que o pedido veio de uma vitrine online?** Pelo `pedido.loja`, com o `tipo` e o `slug` da vitrine, e pelo `pedido.cardapioId`. No pedido feito no balcão, na conversa ou pela API, `loja` vem `null`.
>
> **Dá para acompanhar o entregador pelo meu sistema?** Sim. Enquanto a entrega está na rua, chega o aviso `entregador-posicao` com a localização do entregador e os pedidos que ele leva.
