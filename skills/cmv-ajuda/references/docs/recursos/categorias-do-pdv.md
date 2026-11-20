# Categorias do PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/categorias-do-pdv
- **Categoria:** Recursos
- **Menu:** PDV › Categorias do PDV

---

🧩 O cardápio cresceu e o atendente perde tempo procurando o produto numa lista comprida? As **Categorias do PDV** organizam os produtos em grupos, como *Bebidas* e *Lanches*, com subcategorias dentro, como *Cafés* dentro de *Bebidas*.

A ordem das categorias é a mesma do **Balcão** e do pedido pelo fluxo, e cada categoria tem uma cor, que aparece na lista de produtos.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **PDV  ›  Produtos** e clique em **Categorias**.
>
> ➡️ Em **Nova categoria**, digite o nome, escolha a cor e clique em **Criar**.
>
> ➡️ No cadastro de cada produto, escolha a **Categoria**.

## Como criar as categorias

Acesse o menu **PDV  ›  Produtos  ›  Categorias**

A janela **Categorias de produto** lista as categorias na ordem do **Balcão** e do fluxo, cada uma com quantos produtos tem.

🔘 **Nova categoria:** o nome e uma das 10 cores prontas. O botão **Criar** fica ativo depois do nome e põe a categoria no fim da lista.

🔘 **Nova subcategoria:** o botão na linha da categoria abre o campo *Nova subcategoria de Bebidas*, com o nome, a cor, **Cancelar** e **Criar**. A subcategoria fica dentro da categoria, como *Cafés* dentro de *Bebidas*.

🔘 **Subir** e **Descer:** mudam a ordem da categoria no **Balcão** e no fluxo, uma posição por clique. A primeira categoria da lista não sobe.

🔘 **Ativa:** desligada, a categoria some do **Balcão** e do fluxo, e os produtos dela continuam no cadastro.

🔘 **Editar categoria:** abre a janela **Editar categoria**, com o **Nome**, a cor, a **Categoria de cima**, o **Setor de produção**, a imagem da categoria e **Salvar**.

🔘 **Apagar:** a janela pergunta *"Apagar Bebidas?"* e avisa que os produtos da categoria ficam sem categoria e continuam no cadastro. Categoria com subcategoria não é apagada: a janela mostra *"Apague ou mova as subcategorias antes de apagar esta categoria."* e o botão **Apagar** fica desativado.

## Como mover uma categoria ou subcategoria

No **Editar categoria**, o campo **Categoria de cima** decide onde a categoria fica:

🔘 **Uma categoria da lista:** a categoria passa a ser subcategoria dela. Assim uma subcategoria muda de categoria, como *Cafés* saindo de *Bebidas* para *Lanches*, e uma categoria principal passa para dentro de outra.

🔘 **Nenhuma (categoria principal):** a subcategoria vira categoria principal e entra no fim da lista.

**Salvar** avisa *"Categoria salva"*. A lista do campo **Categoria de cima** mostra só as categorias principais.

Os produtos vão junto com a subcategoria: no **Balcão**, eles passam a aparecer no botão da categoria nova.

⚠️ A categoria que tem subcategorias continua principal: o campo **Categoria de cima** fica desativado, com o aviso *"Esta categoria tem subcategorias, por isso continua como categoria principal."*

## A imagem e o setor de produção da categoria

O **Editar categoria** tem mais dois campos:

🔘 **Imagem:** **Escolher imagem** põe a foto da categoria, com a ajuda *"JPG, PNG ou WEBP, até 1,5 MB. Aparece no Cardápio e na Loja, ao lado do nome da categoria."* Imagem maior é recusada com *"A imagem passa de 1,5 MB. Escolha uma menor."*. **Tirar imagem**, depois de **Salvar**, deixa a categoria sem imagem. No **Balcão**, os botões de categoria continuam sem a imagem.

🔘 **Setor de produção:** quem prepara os produtos da categoria, como *Cozinha* ou *Bar*, entre **Nenhum setor** e os setores criados no botão **Setores**, em **Produtos**. A lista de categorias mostra o setor ao lado do nome, e a subcategoria segue o setor da categoria de cima.

## Como pôr o produto numa categoria

No cadastro do produto, no menu **PDV  ›  Produtos**, o campo **Categoria** lista as categorias e as subcategorias.

Na lista de **Produtos**, cada produto mostra a categoria na cor dela, com o caminho da subcategoria, como *Bebidas › Cafés*. O filtro **Categoria**, no topo, mostra os produtos de uma categoria, de uma subcategoria ou os **Sem categoria**.

## Onde as categorias aparecem

➡️ **Balcão:** os botões de categoria ficam acima da venda. Tocar numa categoria mostra os produtos dela, com **Todos de** e as subcategorias para filtrar, e tocar no produto põe o item na venda.

➡️ **Pedido pelo fluxo:** o bloco de pedido do fluxo pode oferecer a categoria inteira, e o cliente escolhe primeiro a categoria e depois o produto.

➡️ **Painel de Pedidos:** com setores de produção, a tela de cada setor mostra só os itens das categorias daquele setor.

➡️ **Relatório do PDV:** a tabela **Por categoria** mostra a quantidade, o total e a participação de cada categoria nas vendas.

➡️ **Webhook do PDV:** os avisos `categoria-criada`, `categoria-alterada` e `categoria-removida`.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Desativei uma categoria do PDV. Os produtos dela somem do cadastro?** Não. A categoria desativada some do **Balcão** e do fluxo, e os produtos continuam em **Produtos**, com a categoria.
>
> **Como passo uma subcategoria do PDV para outra categoria?** No **Editar categoria** da subcategoria, escolha a nova categoria no campo **Categoria de cima** e clique em **Salvar**. Escolhendo **Nenhuma (categoria principal)**, a subcategoria vira categoria principal.
>
> **O campo Categoria de cima está desativado no Editar categoria. Por quê?** A categoria tem subcategorias e, por isso, continua como categoria principal. Para pôr essa categoria dentro de outra, mova antes as subcategorias dela.
>
> **A janela Categorias de produto mostra 0 produto(s) numa categoria que tem produtos na subcategoria. Está errado?** Não. A contagem da janela **Categorias de produto** conta só os produtos postos direto naquela categoria. Os produtos da subcategoria contam na subcategoria.
>
> **Pus categoria nos produtos e as vendas antigas continuam em Sem categoria no Relatório do PDV. Por quê?** A venda guarda a categoria que o produto tinha na hora em que foi vendido. As vendas feitas antes de o produto ganhar categoria continuam em **Sem categoria**, e só as vendas novas entram na categoria.
>
> **A tabela Por categoria não aparece no Relatório do PDV.** A tabela **Por categoria** só aparece quando o período tem pelo menos uma venda de produto com categoria.
>
> **O botão Apagar fica desativado ao apagar uma categoria do PDV. Por quê?** A categoria tem subcategoria. Mova cada subcategoria para outra categoria, ou deixe-a como categoria principal, pelo campo **Categoria de cima** do **Editar categoria**, ou apague as subcategorias. Depois apague a categoria.
>
> **Apaguei uma categoria do PDV. O que acontece com os produtos?** Os produtos ficam sem categoria e continuam no cadastro.
>
> **Para que serve o Setor de produção no Editar categoria?** Ele diz quem prepara os produtos daquela categoria, como a cozinha ou o bar. Com o setor escolhido, a tela daquele setor no **Painel de Pedidos** mostra só os itens dele. Os setores são criados no botão **Setores**, no menu **PDV  ›  Produtos**.
