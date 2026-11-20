# Pedido na Conversa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pedido-na-conversa
- **Categoria:** Recursos
- **Menu:** PDV › Pedido na Conversa

---

🧩 O cliente pediu pela conversa? O pedido é montado ali mesmo, sem sair do atendimento: os produtos, o desconto, a entrega e o total. Ao **Confirmar e enviar**, o cliente recebe a nota do pedido na conversa e o estoque baixa na hora.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No atendimento, clique no botão **Pedido**, no topo da conversa, ou em **Novo pedido**, no card **Pedidos** do painel do contato.
>
> ➡️ Busque e adicione os produtos, ajuste quantidade, desconto e entrega.
>
> ➡️ Clique em **Confirmar e enviar**, ou em **Salvar rascunho** para terminar depois.
>
> ➡️ Para responder quanto custa ou se tem no estoque, e enviar o preço na conversa, use o ícone **Consultar preço e estoque**, ao lado do **Pedido**.

## Vídeo Tutorial

[Vídeo Voomly — id l9BZa1aFQxFnAQBOOj1FtvdyHUdaOETq1NoVPHIzuxww91VtH, tipo v]  

## Como montar o pedido

O botão **Pedido**, no topo da conversa, e o **Novo pedido**, no card **Pedidos** do painel do contato, sempre começam um pedido novo, na janela **Novo pedido**:

🔘 **Buscar produto ou serviço:** digite o nome e escolha o produto. O resultado mostra o estoque, como *"Em estoque: 12"*. Cada item da tabela tem preço, quantidade, total e **Tirar do pedido**.

🔘 **Produto com opções:** o produto com variações aparece na busca com *"a partir de"* e o preço. Ao escolher, abre a janela das opções: a variação em **Opção** e os adicionais de cada grupo, marcados dentro da regra, como *"Escolha de 1 a 2"*. O **Preço de cada unidade** soma a variação e os adicionais, e **Adicionar** põe o item no pedido. Na tabela, o item leva a variação entre parênteses e os adicionais abaixo, como *Pizza (Pequena)* e *+ Catupiry*, com o estoque da variação.

🔘 **Desconto em:** **R$** ou **%**, e o valor do **Desconto**.

🔘 **Acréscimo:** um valor somado ao total.

🔘 **Retirada no local** ou **Entrega:** na entrega aparecem **Taxa de entrega**, **Endereço de entrega** e **Bairro**. O **Bairro** sugere os bairros da tabela de taxas, como *"Centro · R$ 7,50"*, e preenche a taxa, que ainda pode ser ajustada. O **Endereço de entrega** é obrigatório na entrega: sem ele, **Salvar rascunho** e **Confirmar e enviar** ficam desativados.

🔘 **CEP:** na entrega, quando a empresa tem faixas cadastradas no **Frete por faixa de CEP**, aparece o **CEP**, entre a **Taxa de entrega** e o **Endereço de entrega**. O CEP que cai numa faixa preenche a taxa e mostra a região, o frete e o prazo da faixa, como *"Centro · R$ 7,50 · até 40 min"*.

🔘 **Endereço salvo do cliente:** na entrega, quando o cliente da conversa tem endereços guardados, a lista traz cada um como *apelido — endereço · bairro*. O endereço principal já vem escolhido, com o **Endereço de entrega**, o **Bairro** e a **Taxa de entrega** preenchidos. Escolher outro endereço da lista preenche os mesmos campos, com a taxa pela tabela de bairros. Para um endereço que não está na lista, digite no **Endereço de entrega**: a lista fica em branco. O *Outro endereço (digitado abaixo)*, no topo da lista, só indica esse caso e não se escolhe.

🔘 **Salvar este endereço no cadastro do cliente:** aparece já marcado quando o endereço digitado não está na lista do cliente. Marcado, o endereço entra nos endereços do cliente, sem apelido, já no **Salvar rascunho**; desmarcado, fica só neste pedido.

🔘 **Agendar para:** opcional, a data e o horário combinados com o cliente. O pedido agendado leva *"Agendado para"* na nota, aparece na lista de pedidos com a data combinada e entra em **Agendados** no **Painel de pedidos**.

🔘 **Observação:** o recado do pedido, que vai na nota.

O **Subtotal**, a **Taxa de entrega** e o **Total** aparecem no fim da janela.

### Os endereços do cliente

Na entrega, o botão **Endereços do cliente** abre a janela de mesmo nome, com o nome do contato, onde ficam os endereços de entrega guardados dele. Sem nenhum, a janela avisa *"O cliente ainda não tem endereço salvo."*

🔘 **Novo endereço:** abre o formulário com **Apelido**, **Endereço (rua, número e complemento)**, **Bairro**, **CEP** e **Usar como endereço principal**. **Salvar** só fica ativo com o endereço preenchido e avisa *"Endereço salvo."*

🔘 **Tornar principal:** faz do endereço o principal, que sobe para o topo da lista e já vem escolhido na entrega. O primeiro endereço do cliente nasce principal.

🔘 **Editar endereço** e **Apagar endereço:** o apagar pede a confirmação *"Apagar este endereço do cliente?"* e avisa *"Endereço apagado."* Apagado o principal, o endereço usado por último passa a ser o principal.

⚠️ O bairro fora da tabela de taxas de entrega não é salvo, com o aviso *"Ainda não entregamos neste bairro."*, e o mesmo endereço não entra duas vezes: *"Este endereço já está na lista do cliente."*

## Confirmar e enviar

**Confirmar e enviar** confirma o pedido e avisa *"Pedido confirmado e nota enviada ao cliente."* O cliente recebe duas mensagens na conversa: o texto do pedido, com a data, os itens, o subtotal, o desconto, a taxa, o total e *Entregar em* ou *Retirada no local*, e o PDF do pedido. O estoque dos produtos baixa na hora.

No item com variação, o texto do pedido traz a variação entre parênteses e, na linha de baixo, os adicionais escolhidos, como *"1 x Pizza (Pequena) · R$ 35,00"* e *"+ Catupiry"*.

**Confirmar e enviar só o link** aparece na janela do pedido ligado a um atendimento quando a empresa tem um meio de pagamento online conectado, no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**. O botão confirma o pedido e envia ao cliente o link de pagamento, com o aviso *"Pedido confirmado e link de pagamento enviado ao cliente."* Quando o link não é enviado, o pedido fica confirmado mesmo assim, e a janela avisa *"Pedido confirmado, mas o link não foi enviado. Gere o link em Pagamentos."*

**Salvar rascunho** guarda o pedido sem enviar nada, com o aviso *"Rascunho salvo."*. O rascunho é reaberto pelo menu **PDV  ›  Pedidos**, no botão **Abrir pedido**.

⚠️ Quando um item passa do estoque, a janela mostra *"Só 12 em estoque"* e o **Confirmar e enviar** fica desativado até a quantidade ser ajustada, a não ser que a empresa venda sem estoque.

⚠️ Com o **Desconto máximo do atendente** preenchido nas Opções, o atendente que passa do limite vê *"O desconto passa do seu limite de 10%. Salve o rascunho e peça a um supervisor ou administrador para confirmar."*

## Depois de confirmado

🔘 **Registrar pagamento:** os pagamentos do pedido ficam na mesma janela, abaixo dos itens. Sem o seu caixa aberto, a janela mostra **Ir para o caixa**.

🔘 **Imprimir:** imprime o pedido.

🔘 **Via da cozinha:** abre o PDF da via da cozinha, só com os itens, sem preço e com letra grande.

🔘 **Reenviar nota:** manda a nota do pedido de novo ao cliente.

🔘 **Saiu para entrega:** só no pedido com entrega. Escolhe quem leva o pedido e o despacha, como no **Painel de pedidos**.

🔘 **Marcar como entregue:** fecha o pedido como entregue.

🔘 **Rastreio da entrega:** com o pedido na rua, a janela mostra o link do rastreio, **Copiar link** e **Enviar ao cliente**, que manda na conversa *"Acompanhe a entrega do pedido #24:"* e o link, com o aviso *"Link do rastreio enviado na conversa"*.

🔘 **Ver onde foi entregue** e **Ver a foto da entrega:** no pedido entregue por um entregador, junto com o nome de quem entregou.

## Cancelar o pedido

**Cancelar pedido**, no rodapé da janela do pedido, mostra o campo **Motivo do cancelamento**, com até 500 caracteres, e o botão **Cancelar o pedido**.

🔘 **Pedido confirmado:** o motivo é obrigatório. O **Cancelar o pedido** só cancela com o **Motivo do cancelamento** preenchido.

🔘 **Rascunho:** cancela sem motivo.

🔘 **Pedido de mesa ou comanda:** o motivo fica só no pedido, e a tela avisa *"Fica no pedido. Pedido de mesa ou comanda não manda mensagem ao cliente."*

Ao cancelar, o estoque volta, e o pagamento registrado é estornado. A janela do pedido passa a mostrar quem cancelou e o motivo, como *"Cancelado por Ana — Cliente desistiu"*.

⚠️ O aviso **Pedido cancelado** ao cliente depende de estar ligado nos **Avisos do pedido ao cliente**, no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**. Com o aviso desligado, cancelar o pedido não envia nada ao cliente.

## Os pedidos no painel do contato

O painel do contato, no atendimento, mostra o card **Pedidos**: o resumo *"Pedidos confirmados: 2 · Total gasto: R$ 238,62"* e a lista dos pedidos do cliente, com número, valor, data e situação. No pedido cancelado, a lista mostra também quem cancelou e o motivo, como *"Cancelado por Ana — Cliente desistiu"*; o rascunho cancelado sem motivo mostra só quem cancelou. A lista se atualiza sozinha, sem recarregar a tela, quando o pedido é criado, confirmado, muda de etapa ou é cancelado.

🔘 **Novo pedido:** no topo do card **Pedidos**, abre a janela **Novo pedido**, a mesma do botão **Pedido** do topo da conversa, com o pedido ligado a este atendimento. Com o atendimento encerrado, o card não mostra o **Novo pedido**.

🔘 **Repetir pedido:** cria um pedido novo com os mesmos itens, a mesma entrega e o mesmo bairro, com o preço de hoje, e avisa *"Pedido #11 repetido com os preços de hoje. Confira e confirme."* O pedido novo nasce em rascunho, e nada é enviado ao cliente até a confirmação.

## Consultar preço e estoque

O cliente só quer saber quanto custa ou se tem? Ao lado do botão **Pedido**, no topo da conversa, o ícone **Consultar preço e estoque** abre a janela **Preço e estoque**, que mostra o preço e o estoque sem montar pedido e, com um clique, envia o nome e o preço ao cliente na conversa. Quando a barra não mostra o ícone, ele fica no botão ⋯ **Mais ações**. Com as **Ações do topo do ticket** em **Agrupadas**, o **Pedido** e o **Consultar preço e estoque** ficam no botão **Mais**, no grupo **ORGANIZAÇÃO**.

🔘 **Procurar produto pelo nome ou SKU:** a busca acha pelo nome e pelo SKU, com letra maiúscula ou minúscula. Antes da busca, a janela orienta: *"Digite o nome ou o SKU para ver o preço e o estoque, sem montar pedido."* Sem resultado, avisa *"Nenhum produto encontrado."*

🔘 **Enviar com a foto do produto:** a caixa logo abaixo da busca. Marcada, o **Enviar na conversa** de um produto com foto envia a foto, com o nome e o preço na legenda, e o botão passa a dizer *"Enviar na conversa, com a foto"*. No produto sem foto, vai só o texto. A escolha fica guardada no navegador para a próxima consulta.

🔘 **Produto**, **Preço** e **Estoque:** cada linha traz o produto, com o SKU e a categoria embaixo do nome, o preço e o estoque. O produto com variações ganha uma linha por variação, como *"Cheese (Simples)"* e *"Cheese (Duplo)"*, cada uma com o preço e o estoque dela.

🔘 **Estoque:** como *"10 em estoque"*; *"5 pela ficha"*, no prato com **Ficha de insumos**; *"Sem controle de estoque"*, no produto sem o controle ligado; ou *"Serviço"*. O produto inativo leva *"Inativo"* embaixo do nome.

🔘 **Enviar na conversa:** o botão de cada linha, antes do **Copiar nome e preço**. Envia ao cliente, na conversa, o nome e o preço do produto, como *"Caneca — R$ 35,90"*, e avisa *"Enviado na conversa."* Na linha de uma variação, ela vai entre parênteses, como *"Cheese (Simples) — R$ 30,00"*.

🔘 **Copiar nome e preço:** copia o nome e o preço do produto, como *"Caneca — R$ 35,90"*, e avisa *"Copiado. Cole na conversa."* O **Copiar nome e preço** não envia nada ao cliente e não muda a caixa de mensagem.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A nota do pedido é nota fiscal?** Não. A nota do PDV é o resumo do pedido, em texto e em PDF, e não substitui o documento fiscal.
>
> **Cliquei em Pedido para continuar um pedido e veio um pedido vazio.** O botão **Pedido** e o **Novo pedido** do card **Pedidos** sempre começam um pedido novo. Para continuar um rascunho, abra o pedido no menu **PDV  ›  Pedidos**.
>
> **Não acho o botão Pedido nem o Consultar preço e estoque no topo da conversa.** Com as **Ações do topo do ticket** em **Agrupadas**, no menu **Configurações  ›  Opções  ›  Atendimento**, seção **Conversa**, os dois ficam no botão **Mais** do topo da conversa, no grupo **ORGANIZAÇÃO**. Com **Todas à mostra**, o que não cabe na largura da tela vai para o botão ⋯ **Mais ações**.
>
> **O cliente recebe alguma mensagem quando eu salvo o rascunho?** Não. Nada é enviado até o **Confirmar e enviar**.
>
> **Por que o Cancelar o pedido não cancela o pedido confirmado?** Falta o **Motivo do cancelamento**. No pedido confirmado, o motivo é obrigatório; só o rascunho cancela sem motivo.
>
> **O cliente fica sabendo que o pedido foi cancelado?** Depende do aviso **Pedido cancelado**, nos **Avisos do pedido ao cliente**, no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**: com ele desligado, cancelar não envia nada ao cliente. O pedido de mesa ou comanda não manda mensagem ao cliente.
>
> **O botão Novo pedido sumiu do card Pedidos. Por quê?** O atendimento foi encerrado. Com o atendimento encerrado, o card **Pedidos** não mostra o **Novo pedido**.
>
> **O campo CEP não aparece no pedido com entrega. Por quê?** O **CEP** só aparece quando a empresa tem faixas cadastradas no **Frete por faixa de CEP**, no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**. Sem faixas, a taxa vem do **Bairro**.
>
> **Como guardo o endereço do cliente para o próximo pedido na conversa?** Deixe marcado **Salvar este endereço no cadastro do cliente** ao digitar um endereço novo, ou cadastre pelo botão **Endereços do cliente**, na entrega do pedido. Nos próximos pedidos, ele aparece na lista **Endereço salvo do cliente**.
>
> **O Consultar preço e estoque envia alguma coisa ao cliente?** Só quando você clica em **Enviar na conversa**, na linha do produto: o cliente recebe o nome e o preço, como *"Caneca — R$ 35,90"*, ou, com **Enviar com a foto do produto** marcada, a foto do produto com esse texto na legenda. Buscar e **Copiar nome e preço** não enviam nada.
>
> **Repeti um pedido antigo e faltou um item.** O item foi tirado do cadastro de produtos. A janela avisa *"Ficaram de fora, porque saíram do cadastro"*, com o nome dos itens.
