# Produtos e Estoque do PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/produtos-e-estoque-do-pdv
- **Categoria:** Recursos
- **Menu:** PDV › Produtos e Estoque do PDV

---

🧩 O PDV vende o que está no cadastro de **Produtos**, e cada venda baixa o estoque na hora. Com o estoque controlado, a plataforma avisa quando um produto chega ao mínimo, antes de faltar para o cliente.

Os campos de estoque ficam no próprio cadastro do produto, junto do nome, do preço e da categoria. No mesmo cadastro ficam o **Custo**, as **Variações**, como tamanhos e sabores, e os **Adicionais**, como bordas e extras.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **PDV  ›  Produtos** e clique em **Adicionar Produto**.
>
> ➡️ Escolha o **Tipo**, ligue **Controlar estoque**, preencha **Estoque inicial** e, se quiser o aviso, **Estoque mínimo**.
>
> ➡️ Para vender o mesmo produto em tamanhos ou sabores, ou com bordas e extras, use **Adicionar variação** e **Adicionar grupo de adicionais**, no mesmo cadastro.
>
> ➡️ Para a pizza com mais de um sabor, use **Adicionar sabores (pizza)**, no mesmo cadastro.
>
> ➡️ Para o prato que baixa do estoque os ingredientes, e não ele mesmo, monte a **Ficha de insumos**, no mesmo cadastro.
>
> ➡️ Para cadastrar um produto parecido com outro, clique em **Duplicar** na lista.
>
> ➡️ Para tirar o produto do Cardápio Digital sem apagar o cadastro, desligue **Ativo no Cardápio** na lista.
>
> ➡️ Para dar entrada, saída ou acertar a contagem depois, use o botão **Movimentar estoque** na lista.

## Vídeo Tutorial

[Vídeo Voomly — id FxfKBBwr_tTTQoRWmk_L-8HONwwXMegCrKl6XDchM2LAuEcdV, tipo v]  

## Os campos de estoque

🔘 **Tipo:** **Produto** ou **Serviço**. Serviço não tem estoque.

🔘 **Controlar estoque:** com o controle ligado, cada entrada, saída e venda muda o saldo do produto.

🔘 **Estoque inicial:** a quantidade com que o produto começa. Ela entra no histórico como uma entrada, com o motivo *Estoque inicial*.

🔘 **Estoque mínimo:** no mínimo ou abaixo dele, o produto aparece como estoque baixo. Vazio, sem mínimo.

Na lista de **Produtos**, cada produto mostra o saldo e o mínimo, como *"Estoque: 10 · mínimo 3"*, em vermelho quando chega ao mínimo. O filtro **Estoque baixo** mostra só esses.

## O custo do produto

🔘 **Custo:** quanto custa uma unidade para a loja. É dele que o **Relatório do PDV** tira o lucro e a margem.

No produto com variações, cada variação tem o seu **Custo**, e a venda usa o custo da variação vendida; a variação sem custo usa o **Custo** do produto. Os adicionais não têm custo.

Cada venda guarda o custo da hora em que foi feita: mudar o custo depois não muda as vendas antigas.

O campo **Custo** só aparece para administrador e supervisor. O atendente vende o produto sem ver o custo dele.

## Variações: tamanhos e sabores

As **Variações** vendem o mesmo produto em versões diferentes, como tamanhos ou sabores, cada uma com o preço e o estoque próprios. Com variação cadastrada, quem vende escolhe uma delas na hora da venda.

🔘 **Adicionar variação:** cria uma linha com **Nome da variação**, **Preço**, **Custo** e **Ativa**. Com **Ativa** desligada, a variação continua no cadastro e deixa de aparecer na venda: no **Balcão**, ela não aparece para escolher.

🔘 **Tirar a variação:** tira a linha na hora, sem pedir confirmação, e a mudança vale ao **Salvar**. As vendas que já tiveram a variação continuam no **Relatório do PDV**, com o nome dela.

🔘 **Estoque da variação:** com **Controlar estoque** ligado e variação cadastrada, o campo **Estoque inicial** some do cadastro. O estoque de cada variação entra depois, pelo botão **Movimentar estoque**, escolhendo a **Variação**.

Na venda, o item leva o nome da variação entre parênteses, como *Pizza (Grande)*, e o estoque mostrado é o daquela variação. No prato com **Ficha de insumos**, o estoque mostrado é o que os insumos permitem fazer.

## Adicionais: bordas e extras

Os **Adicionais** são grupos de opções escolhidas junto com o produto, como Bordas ou Extras, cada opção com o seu preço.

🔘 **Adicionar grupo de adicionais:** cria o grupo, com **Nome do grupo**, **Mínimo** e **Máximo**.

🔘 **Adicionar opção:** cada opção do grupo tem **Opção**, o nome dela, **Preço** e **Máx. por item**.

🔘 **Máx. por item:** quantas vezes a mesma opção pode entrar num item, como 3 ovos no mesmo lanche. Na venda, a opção ganha os botões **−** e **+**, até esse limite.

🔘 **Mínimo** e **Máximo:** quantas opções do grupo quem vende tem de escolher. Com mínimo 1 e máximo 2, a venda mostra *"Escolha de 1 a 2"*, e o item só entra no pedido com uma ou duas opções marcadas.

O preço das opções escolhidas soma no preço do item: uma variação de R$ 45,00 com duas bordas de R$ 5,00 e R$ 6,00 fica em R$ 56,00 a unidade. Na venda, os adicionais aparecem logo abaixo do item, como *+ Catupiry, Cheddar*.

## Sabores: a pizza meio a meio

Os **Sabores (pizza)** deixam montar a pizza com mais de um sabor, como meio a meio. O botão **Adicionar sabores (pizza)**, no cadastro do produto, cria o grupo:

🔘 **Nome do grupo**, **Mínimo** e **Máx. de sabores:** quantos sabores entram em cada pizza.

🔘 **Preço da pizza:** **O preço do tamanho** ou **A média dos sabores** escolhidos.

🔘 **Sabor** e **Ingredientes (opcional):** cada sabor, com os ingredientes que aparecem para o cliente. **Adicionar sabor** cria mais um.

🔘 **Preço de cada sabor:** no produto com variações, um preço por tamanho, e a tela orienta: *"Informe o preço de cada sabor em cada tamanho. Tamanho em branco usa o preço do tamanho."*

Com **A média dos sabores**, a pizza Grande com Calabresa (R$ 58,00) e Portuguesa (R$ 64,50) fica em R$ 61,25, e a pizza de um sabor só fica com o preço daquele sabor. Na página da loja, a janela da pizza avisa *"vale a média dos sabores"*, com o preço de cada sabor no tamanho. No pedido e na via da cozinha, os sabores aparecem como *1/2 Calabresa, 1/2 Portuguesa*.

## Ficha de insumos: o prato que baixa os ingredientes

A **Ficha de insumos** fica no cadastro do produto, logo depois de **Controlar estoque**, e a tela explica: *"Produto composto: a venda baixa do estoque os insumos (ex.: 1 carne e 1 fatia de queijo), e não o próprio produto. O insumo é um produto com controle de estoque e sem variações."*

🔘 **Insumo** e **Quantidade:** cada linha da ficha, criada em **Adicionar insumo**. A lista de insumos só oferece produto com **Controlar estoque** ligado e sem variações.

🔘 **Ficha de insumos**, na variação: o botão mostra quantos insumos a variação tem, e a tela avisa *"A ficha da variação substitui a do produto. Vazia, vale a do produto."*

🔘 **Ficha de insumos**, na opção do adicional: *"Quanto de cada insumo sai por unidade deste adicional."*

O prato com ficha fica com **Controlar estoque** desligado: o estoque dele é o que os insumos permitem fazer. O cadastro mostra esse número, como *"Dá para fazer agora com os insumos: 5"*, e o **Balcão** mostra o mesmo número em *"Em estoque"*. Com 10 carnes e 5 fatias de queijo, o prato de 1 carne e 1 fatia dá 5, e a variação Duplo, com 2 de cada, dá 2.

Na venda, cada insumo baixa do estoque: um Simples com o adicional Bacon e um Duplo baixam 3 carnes, 3 fatias de queijo e 1 bacon. Quando falta insumo, o prato fica sem estoque sozinho, e a variação que usa mais insumo esgota antes das outras: com 1 fatia de queijo, o Duplo esgota e o Simples continua. A entrada do insumo devolve o prato à venda.

## Galeria de fotos e ficha técnica

🔘 **Galeria de fotos:** a tela explica *"Até 12 fotos a mais, além da principal. A primeira daqui aparece logo depois dela na loja."* As fotos novas sobem quando o produto é salvo, e com 12 fotos o botão **Adicionar fotos** fica desativado. Para mudar a ordem, salve o produto, reabra o cadastro e use as setas de cada foto.

🔘 **Ficha técnica:** a tela explica *"As características do produto, como Marca, Modelo, Tamanho ou Ano. Aparecem na página do produto, na loja."* Cada linha tem **Característica** e **Valor** e é criada em **Adicionar característica**. Cada linha precisa do nome da característica: sem ele, o produto não salva, e a tela avisa *"Dê um nome a cada característica da ficha técnica."*

## A categoria do produto

No cadastro do produto, o campo **Categoria** põe o produto numa das **Categorias do PDV**, que são criadas no botão **Categorias**, no topo da lista de **Produtos**.

Na lista de **Produtos**, cada produto mostra a categoria na cor dela, com o caminho da subcategoria, como *Bebidas › Cafés*. O filtro **Categoria**, no topo, mostra só os produtos de uma categoria, de uma subcategoria ou os **Sem categoria**.

No botão **Categorias**, em **Editar categoria**, o interruptor **Pedir observação nos produtos** decide se o cliente pode escrever uma observação no Cardápio Digital. A tela avisa: *"Desligado, os produtos desta categoria (e das subcategorias) não mostram o campo "Alguma observação?" no Cardápio."* Vale a categoria de cima: com o interruptor desligado nela, a subcategoria também não mostra o campo, mesmo com o dela ligado.

## Duplicar um produto

O botão **Duplicar**, na linha do produto, abre **Duplicar produto** já preenchido com o que o original tem — o preço, as variações, os adicionais e os sabores, com os preços — e o nome com *(cópia)* no fim. O **SKU** vem vazio. Ajuste o que muda e salve: a cópia entra na mesma categoria do original.

## Onde e quando o produto aparece

No bloco **Onde e quando aparece no Cardápio Digital**, o cadastro diz *"em qual canal o produto aparece e, se for uma oferta de horário marcado, os dias e horários. Fora deles, o produto some da loja."*

Na empresa que tem também a Loja Digital, o bloco se chama *"Onde e quando aparece no Cardápio e na Loja Digital"* e ganha a lista **Em qual vitrine aparece**: *No Cardápio e na Loja Digital*, *Só no Cardápio Digital* ou *Só na Loja Digital*. O produto *Só na Loja Digital* não aparece no Cardápio Digital.

🔘 **Ativo: aparece no Cardápio** × **Inativo: não aparece no Cardápio:** na lista de **Produtos**, o mesmo interruptor fica em cada produto, como **Ativo no Cardápio** × **Inativo no Cardápio**, e muda com um clique. O produto inativo some da loja, continua no cadastro e segue à venda no **Balcão** e em **Lançar na mesa**. Na empresa que tem também a Loja Digital, o interruptor fala das duas vitrines: *"Ativo: aparece no Cardápio e na Loja Digital"* × *"Inativo: não aparece no Cardápio nem na Loja Digital"*.

🔘 **Onde aparece:** *Cardápio online e Mesa*, *Só no Cardápio online* ou *Só na Mesa*.

🔘 **Destaque no cardápio:** põe o produto na seção **Destaques**, no topo da loja, e ele continua também na categoria dele. A seção **Os mais pedidos**, logo abaixo, é automática e não depende dessa marcação.

🔘 **Preço antes da promoção (riscado):** o preço antigo do produto, para anunciar a promoção. Com 15,00 nesse campo e **Preço** de 10,00, a loja mostra R$ 15,00 riscado, R$ 10,00 e *-33%*. Em branco, ou com valor menor que o **Preço**, não há promoção.

🔘 **Aparece todos os dias, o dia todo** × **Só nos dias e horários marcados:** na oferta de horário, escolha os dias e os horários, com **Mais um horário** e **Tirar o horário**. O horário não passa da meia-noite: para das 22h às 2h, marque os dois dias. Na loja, a oferta mostra até quando vale ao lado do nome, como *"Até 22:00"*.

## Movimentar o estoque

O botão **Movimentar estoque**, na linha do produto, abre a janela **Estoque** com o saldo atual e o mínimo:

🔘 **Movimento:** **Entrada**, **Saída** ou **Ajuste (contagem)**. No ajuste, você informa o **Estoque contado** e o sistema lança a diferença.

🔘 **Variação:** só no produto com variações. O movimento é de uma variação, escolhida aqui. A janela **Estoque** mostra o total do produto e o saldo de cada variação.

🔘 **Motivo:** opcional, fica no histórico.

🔘 **Registrar:** grava o movimento. O **Histórico** logo abaixo mostra data, movimento, quantidade, saldo, motivo e quem fez, e, no produto com variações, a variação de cada movimento.

As vendas entram no histórico sozinhas: o pedido confirmado baixa o estoque, e o pedido cancelado devolve. No produto com variações, a venda baixa o estoque da variação vendida. No prato com **Ficha de insumos**, a venda baixa os insumos, cada um com o movimento de venda e o número do pedido, e o cancelamento devolve os insumos.

## O aviso de estoque baixo

Quando uma venda deixa o produto no mínimo ou abaixo dele, chega um aviso no sino de notificações, como *"Caneca ficou com 2 em estoque (o mínimo é 3)."* O aviso também é enviado ao **Webhook do PDV**, para um sistema de reposição saber na hora.

## Vender o que não tem em estoque

Com **PDV: vender sem estoque** em **Não**, no menu **Configurações  ›  Opções**, o pedido mostra *"Só 12 em estoque"* quando a quantidade passa do saldo e não deixa confirmar até a quantidade ser ajustada. Com **Sim**, o pedido confirma e o saldo fica negativo.

No Cardápio Digital, com **Não**, o produto com estoque zero aparece como *Indisponível*: ganha a etiqueta no card, mostra *"Indisponível no momento"* na janela do produto, e o botão **Adicionar à sacola** fica desativado. Com **Sim**, quem decide é a opção **Cardápio Digital: mostrar "Indisponível" quando o estoque zerar**, no menu **Configurações  ›  Opções**: em **Sim**, o produto zerado aparece como Indisponível e não pode ser pedido pelo Cardápio Digital; em **Não**, continua à venda.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O serviço baixa estoque quando é vendido?** Não. O **Tipo** **Serviço** não tem estoque e pode ser vendido sem limite de quantidade.
>
> **Cancelei um pedido. O estoque volta?** Sim. O cancelamento devolve ao estoque o que o pedido tinha baixado, e o movimento aparece no histórico do produto.
>
> **Cadastrei variações e o campo Estoque inicial sumiu. Como dou estoque a cada variação?** Pelo botão **Movimentar estoque**, na linha do produto: escolha o **Movimento**, a **Variação** e a quantidade, e clique em **Registrar**. A janela **Estoque** mostra o saldo de cada variação.
>
> **Como cadastro uma pizza meio a meio no PDV?** No cadastro do produto, clique em **Adicionar sabores (pizza)**, defina o **Máx. de sabores**, escolha o **Preço da pizza** e cadastre cada **Sabor**, com o preço em cada tamanho. No pedido, a pizza aparece como *1/2 Calabresa, 1/2 Portuguesa*.
>
> **Como faço o lanche baixar do estoque a carne e o queijo, e não o próprio lanche?** Com a **Ficha de insumos**, no cadastro do lanche: cadastre a carne e o queijo como produtos com **Controlar estoque** ligado e sem variações, e acrescente cada um na ficha, com a quantidade. A venda do lanche baixa os insumos.
>
> **Quantas fotos o produto do PDV pode ter?** A principal e mais 12 na **Galeria de fotos**. Com 12, o botão **Adicionar fotos** fica desativado.
>
> **O atendente vê o Custo do produto?** Não. O **Custo** só aparece para administrador e supervisor, e o atendente vende o produto sem ver o custo dele.
>
> **Como anuncio uma promoção de produto no PDV, com o preço antigo riscado?** No cadastro do produto, coloque o preço novo em **Preço** e o antigo em **Preço antes da promoção (riscado)**. A loja mostra os dois e o desconto em porcentagem. Para encerrar a promoção, deixe o campo em branco.
>
> **Como tiro um produto do Cardápio Digital sem apagar o cadastro?** Na lista de **Produtos**, desligue **Ativo no Cardápio**. O produto some da loja, continua no cadastro e segue à venda no **Balcão**.
>
> **O produto zerou o estoque e continua à venda no Cardápio Digital. Por quê?** Com **PDV: vender sem estoque** em **Sim**, o produto zerado continua à venda. Para ele aparecer como Indisponível, ponha em **Sim** a opção **Cardápio Digital: mostrar "Indisponível" quando o estoque zerar**, no menu **Configurações  ›  Opções**.
>
> **Como tiro o campo Alguma observação dos produtos no Cardápio Digital?** Pela categoria: no botão **Categorias**, em **Editar categoria**, desligue **Pedir observação nos produtos**. Os produtos da categoria e das subcategorias deixam de mostrar o campo.
