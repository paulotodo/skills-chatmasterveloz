# Webhook do Cardápio Digital

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-do-cardapio-digital
- **Categoria:** APIs
- **Menu:** Webhooks › Webhook do Cardápio Digital

---

🧩 Quer que o seu sistema saiba na hora que um cliente entrou na loja, que uma mesa pediu a conta ou que um cupom foi usado? O **Webhook do Cardápio Digital** avisa o seu sistema a cada evento da loja, dos endereços do cliente, das mesas, das comandas, das reservas de mesa, dos cupons e do cashback.

Os avisos do Cardápio Digital chegam no mesmo endereço do **Webhook do PDV**, que é o único campo a preencher.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções** e desça até **Webhook do PDV**.
>
> ➡️ Preencha o endereço do seu sistema e clique em **Salvar**.
>
> ➡️ Confira os eventos na lista **Eventos enviados**, logo abaixo do campo.

## Onde ligar

🔘 **Webhook do PDV (recebe os eventos de pedidos, pagamentos, caixa e estoque):** o endereço que recebe também os eventos do Cardápio Digital. Em branco, nada é enviado. Ao salvar, a tela avisa *"Webhook do PDV salvo."* e lista os eventos enviados.

O endereço precisa começar com http:// ou https://, sem espaços, e não pode apontar para a rede interna. Ele recebe **POST** com corpo em JSON.

## O campo que separa um aviso do outro

Tudo chega no mesmo endereço, e é o **`acao`** que diz o que aconteceu no Cardápio Digital:                                                                  

| `acao` | O que aconteceu |
|---|---|
| `cardapio-alterado` | a loja do Cardápio Digital foi salva, a cada **Salvar**, mesmo quando nada mudou |
| `cardapio-cliente-entrou` | o cliente entrou na loja com o código do WhatsApp |
| `cardapio-endereco-salvo` · `cardapio-endereco-removido` | um endereço de entrega do cliente foi guardado, alterado ou removido — na loja, no pedido do painel, pela integração ou pela planilha |
| `mesa-criada` · `mesa-alterada` · `mesa-removida` | uma mesa do salão foi criada, mudou (também quando o QR Code é trocado) ou foi removida |
| `comanda-aberta` · `comanda-conta-pedida` · `comanda-fechada` | a comanda da mesa abriu, a conta foi pedida ou a comanda fechou |
| `comanda-alterada` | a conta da mesa mudou: as pessoas, o cliente, a taxa de serviço ou o desconto na conta |
| `comanda-conta-impressa` | a pré-conta da mesa foi impressa na impressora térmica |
| `pedido-item-cancelado` | um item, ou parte dele, foi tirado de um pedido já confirmado da mesa |
| `comanda-transferida` · `rodada-movida` · `comandas-unidas` | a conta foi para outra mesa livre, um pedido sem pagamento foi para outra conta aberta, ou duas mesas foram juntadas |
| `reserva-criada` · `reserva-alterada` | uma reserva de mesa foi criada ou mudou |
| `reserva-confirmada` · `reserva-compareceu` · `reserva-nao-compareceu` · `reserva-cancelada` | a reserva foi confirmada, o cliente chegou, o cliente não veio ou a reserva foi cancelada |
| `cupom-criado` · `cupom-alterado` · `cupom-removido` | um cupom foi criado, mudou (também quando é ligado ou desligado) ou foi removido |
| `cupom-usado` | um cupom foi usado num pedido da loja |
| `cashback-creditado` · `cashback-usado` · `cashback-estornado` · `cashback-expirado` | uma linha do extrato de cashback do cliente: crédito, uso, estorno ou expiração |

Todo aviso do **Webhook do Cardápio Digital** traz também:

◽ `companyId` — a empresa.

◽ `origem` — de onde veio o evento, como `painel` (alguém na tela) ou `cardapio` (a loja). Nos endereços, também `api` (a integração) e `planilha` (a importação de endereços).

◽ `enviadoEm` — a hora em que o aviso foi enviado.

◽ `backendURL` — o endereço do backend da sua instalação.

## Exemplo de payload de Cupom

O aviso de um cupom que teve o desconto mudado para 15%:

```json
{
  "acao": "cupom-alterado",
  "companyId": 8,
  "cupom": {
    "id": 5,
    "codigo": "BEMVINDO10",
    "tipo": "codigo",
    "descricao": "Desconto da semana",
    "descontoTipo": "percentual",
    "descontoValor": 1500,
    "descontoMaximo": null,
    "pedidoMinimo": null,
    "validoDe": null,
    "validoAte": null,
    "limiteDeUsos": null,
    "usosPorCliente": 1,
    "pedidosParaFidelidade": 5,
    "diasDoAniversario": 7,
    "ativo": true,
    "usos": 0
  },
  "origem": "painel",
  "enviadoEm": "2026-11-07T12:29:37.928Z",
  "backendURL": "https://backend_url.com.br"
}
```

O mesmo cupom, quando é removido, chega só com o `id` e o `codigo`:

```json
{
  "acao": "cupom-removido",
  "companyId": 8,
  "cupom": { "id": 5, "codigo": "BEMVINDO10" },
  "origem": "painel",
  "enviadoEm": "2026-11-07T12:29:46.113Z",
  "backendURL": "https://backend_url.com.br"
}
```

## O que cada aviso traz a mais

◽ **Loja** (`cardapio-alterado`): `cardapio`, com a configuração da loja como está na tela: o `slug` e o `link` da loja, `ativo` (se ela está no ar), os dados do topo, a entrega e a retirada, os `horarios`, os `horariosDaMesa`, os `diasFechados`, `pedidoOnline` (pedido pela sacola ou pelo WhatsApp), o pagamento online, o cashback e o `exemploDaObservacao`. O código do front não vai no aviso; `frontProprio` diz se a loja usa um front próprio.

◽ **Cliente que entrou** (`cardapio-cliente-entrou`): `cliente`, com `contactId`, `numero` e `nome`.

◽ **Endereço** (`cardapio-endereco-salvo` e `cardapio-endereco-removido`): `endereco`, com `id`, `contactId`, `apelido`, `endereco`, `bairro`, `cep` (com o traço, como `80010-000`), `principal` e `usadoEm`. O salvo traz também `novo`: `true` no endereço cadastrado agora, inclusive o que o pedido com entrega guardou sozinho, sem apelido, e `false` no alterado. O removido não traz `novo`.

◽ **Mesa** (`mesa-criada`, `mesa-alterada` e `mesa-removida`): `mesa`, com `id`, `nome`, o `tipo` (`mesa` ou `comanda`, na comanda avulsa), o `numero`, `ativa`, `ordem`, o `link` do QR Code e a `comanda` aberta. Criar várias de uma vez avisa um `mesa-criada` por mesa.

◽ **Comanda** (`comanda-aberta`, `comanda-conta-pedida` e `comanda-fechada`): `comanda`, com a `mesa`, a `situacao`, o `total`, o `pago` e o `saldo` em centavos, e os `pedidos`.

◽ **Conta alterada** (`comanda-alterada`): a comanda como ficou em `comanda`, também com `pessoas`, `cliente`, `consumo`, `taxaServico` (`percentual` e `valor` em centavos) e `desconto` (`tipo`, `valor` e o `aplicado` em centavos), e o que mudou em `mudou`. A taxa e o desconto da conta são repartidos pelos pedidos dela: cada pedido traz a sua parte em `taxaServico` e `descontoDaConta`, em reais, já dentro do `total`.

◽ **Conta impressa** (`comanda-conta-impressa`): `comanda` e `impressao`, com a `largura` e o `usuarioId` de quem imprimiu.

◽ **Item tirado da conta** (`pedido-item-cancelado`): o pedido como ficou em `pedido` e o que saiu em `item`, com `nome`, `variacao`, `quantidade`, `precoUnitario` e `total` em reais, o `motivo` e o `canceladoPorId`. O estoque volta, com um `estoque-movimentado` de cancelamento, e a conta é refeita.

◽ **Conta transferida** (`comanda-transferida`): `comanda`, a mesa de antes em `de` e a nova em `para`, com `id` e `nome`.

◽ **Rodada movida** (`rodada-movida`): o pedido em `pedido` e as duas comandas, como ficaram, em `de` e `para`.

◽ **Mesas juntadas** (`comandas-unidas`): os pedidos e os pagamentos da outra conta vêm para esta. A comanda como ficou chega em `comanda`, e a que fechou, em `unida`, com `id` e `mesa`; a comanda que fechou passa a trazer `unidaNaId`.

◽ O item tirado, a conta transferida, a rodada movida e as mesas juntadas trazem também o `usuarioId` de quem fez.

◽ **Reserva** (`reserva-criada`, `reserva-alterada`, `reserva-confirmada`, `reserva-compareceu`, `reserva-nao-compareceu` e `reserva-cancelada`): `reserva`, com `id`, `mesa`, `inicio`, `fim`, `duracao`, `pessoas`, `cliente`, `observacao`, `situacao` (`pendente`, `confirmada`, `compareceu`, `nao-compareceu` ou `cancelada`), `origem` (`painel`, `api` ou `cardapio`, a reserva feita pelo cliente na loja), `motivo` e `comandaId`. O `reserva-alterada` traz o que mudou em `mudou`, e os avisos de situação trazem a situação de antes em `de`. O `reserva-compareceu` da reserva com mesa abre a conta da mesa e traz o `comandaId`; o `reserva-cancelada` traz o `motivo`.

◽ **Cupom** (`cupom-criado` e `cupom-alterado`): `cupom`, com `id`, `codigo`, `tipo` (`codigo`, `boas-vindas`, `aniversario` ou `fidelidade`), `descricao`, `descontoTipo`, `descontoValor` (em centavos, ou o percentual × 100, como `1500` para 15%), as regras (`descontoMaximo`, `pedidoMinimo`, `validoDe`, `validoAte`, `limiteDeUsos`, `usosPorCliente`, `pedidosParaFidelidade` e `diasDoAniversario`), `ativo` e os `usos`. Ligar ou desligar o cupom chega como `cupom-alterado`, com o `ativo` novo.

◽ **Cupom removido** (`cupom-removido`): `cupom`, só com o `id` e o `codigo`.

◽ **Cupom usado** (`cupom-usado`): `cupom`, com as regras e os `usos` já somados, e `uso`, com `id`, `contactId`, `pedidoId`, `numero`, `desconto` em centavos e, no cupom de aniversário, o `ano`.

◽ **Cashback** (`cashback-creditado`, `cashback-usado`, `cashback-estornado` e `cashback-expirado`): `cashback`, com `contactId`, `pedidoId`, `valor` e `saldo` em centavos. O creditado e o usado trazem também o `numero` do pedido. No `cashback-estornado`, o `tipo` é `estorno` (o saldo que o pedido cancelado tinha usado volta ao cliente) ou `anulado` (o crédito do pedido entregue que foi cancelado é retirado, com o `valor` negativo). Nos outros avisos de cashback, o `valor` vem positivo, também no uso.

## Os pedidos da loja e da mesa

Os pedidos do Cardápio Digital chegam pelos avisos de pedido do **Webhook do PDV**, como `pedido-criado`, com estes campos a mais:

◽ **Pedido pela loja:** `origem` com o valor `cardapio`.

◽ **Pedido na mesa:** `mesa` e `comandaId`.

◽ **De qual vitrine veio:** `pedido.loja`, com `id`, `slug` e `tipo` (`cardapio` ou `loja`, a vitrine em que o cliente fez o pedido; o pedido feito na mesa vem com `cardapio`), e `pedido.cardapioId`. No Balcão, no chat e na API, `loja` vem `null`. Os avisos da comanda não trazem `loja`.

◽ **Pedido com cupom:** no `pedido-confirmado`, `cupom`, com `id` e `codigo`, e o valor em `desconto`.

◽ **Pedido com cashback:** no `pedido-confirmado`, `cashbackUsado`, já dentro do `desconto`.

◽ Os valores do pedido vêm em reais, como `28.9`; os do cupom e do cashback, em centavos.

◽ **Conta da mesa paga online:** `link-de-pagamento-gerado` com `origem` `cardapio` e, quando o pagamento é confirmado, um `pagamento-confirmado` para cada pedido da comanda, com `comandaId` no pagamento.

## Como saber que o aviso veio daqui

Todo aviso do **Webhook do Cardápio Digital** traz o cabeçalho `X-Pdv-Evento`, com o evento, e vai assinado com o **Token da Empresa** no cabeçalho `X-Assinatura-Pdv`. O token não vai no corpo do aviso.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Webhook do Cardápio Digital tem um campo próprio?** Não. Os avisos do Cardápio Digital chegam no endereço preenchido em **Webhook do PDV**, no menu **Configurações  ›  Opções**, e o `acao` separa um aviso do outro.
>
> **Como meu sistema sabe que uma mesa pediu a conta?** Pelo aviso `comanda-conta-pedida`, com a mesa, o total, o que foi pago e o saldo em `comanda`.
>
> **Desliguei um cupom do Cardápio Digital. Qual aviso chega?** O `cupom-alterado`, com `ativo` em `false`. Não há aviso próprio para ligar ou desligar o cupom.
>
> **O endereço importado pela planilha avisa o Webhook do Cardápio Digital?** Sim. Cada endereço importado chega como `cardapio-endereco-salvo`, com `origem` `planilha`; pela integração, com `origem` `api`.
>
> **Como meu sistema sabe que um cupom do Cardápio Digital foi usado?** Pelo aviso `cupom-usado`, com o cupom em `cupom` e o pedido e o desconto em `uso`.
>
> **Quando chega o aviso de cashback creditado no Cardápio Digital?** Quando o pedido é entregue, o aviso `cashback-creditado` traz o valor e o saldo do cliente em `cashback`.
>
> **O pedido feito na mesa do Cardápio Digital gera qual aviso?** Os avisos de pedido do **Webhook do PDV**, com `mesa` e `comandaId`. A abertura da conta chega em `comanda-aberta`.
>
> **Como meu sistema sabe que a taxa de serviço ou o desconto da conta da mesa mudou?** Pelo aviso `comanda-alterada`, com a comanda como ficou em `comanda` e o que mudou em `mudou`.
>
> **Como meu sistema sabe que o cliente reservou uma mesa pelo Cardápio Digital?** Pelo aviso `reserva-criada`, com `origem` `cardapio` dentro de `reserva`. A reserva feita pela equipe vem com `painel`, e a feita pela integração, com `api`.
>
> **Como meu sistema sabe de qual vitrine veio um pedido do Cardápio Digital?** Pelo `pedido.loja` dos avisos de pedido, com o `id`, o `slug` e o `tipo` da vitrine, e pelo `pedido.cardapioId`.
