# Setores de Produção do PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/setores-de-producao-do-pdv
- **Categoria:** Recursos
- **Menu:** PDV › Setores de Produção do PDV

---

🧩 A cozinha recebe o pedido inteiro, com a bebida que é do bar, e o bar fica esperando alguém avisar? Os **Setores de produção do PDV** dividem o preparo: cada categoria de produto tem o setor que a prepara, como *Cozinha*, *Bar*, *Caixa* ou *Copa*.

Com os setores criados, cada tela do **Painel de pedidos** pode mostrar só os itens do seu setor. A cozinha vê o lanche, o bar vê a bebida, e o pedido continua um só.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **PDV  ›  Produtos** e clique em **Setores**.
>
> ➡️ Em **Novo setor**, digite o nome, escolha a cor e clique em **Criar**.
>
> ➡️ Em **Categorias**, abra o **Editar categoria** de cada categoria, escolha o **Setor de produção** e clique em **Salvar**.
>
> ➡️ No **Painel de pedidos**, escolha o setor da tela no filtro **Setor**.

## Como criar os setores de produção

Acesse o menu **PDV  ›  Produtos  ›  Setores**

A janela **Setores de produção** explica: *"Quem prepara cada pedido: Cozinha, Bar, Caixa, Copa... Escolha o setor de cada categoria no Editar da categoria, e cada tela do Painel de pedidos mostra só o que é do seu setor."* Antes do primeiro setor, ela mostra *"Nenhum setor ainda. Crie o primeiro: Cozinha, Bar, Copa..."*.

🔘 **Novo setor:** o nome e uma das 10 cores prontas. **Criar** avisa *"Setor criado."* e põe o setor na lista.

🔘 **A linha do setor:** mostra o nome e quantas categorias o setor prepara, como *Cozinha · 1 categoria(s)*, com **Subir**, **Descer**, **Editar setor** e **Apagar**.

🔘 **Desativar o setor:** o interruptor da linha tira o setor do filtro do **Painel de pedidos**. Os itens das categorias dele deixam de mostrar o nome do setor no painel.

🔘 **Apagar:** a janela pergunta *"Apagar o setor Cozinha?"* e avisa *"As categorias deste setor ficam sem setor, e os produtos continuam no cadastro."* **Apagar** confirma, com *"Setor apagado."*.

## Como dar um setor a cada categoria

Acesse o menu **PDV  ›  Produtos  ›  Categorias**

No **Editar categoria**, o campo **Setor de produção** lista **Nenhum setor** e os setores criados, com a ajuda *"Crie os setores (Cozinha, Bar...) no botão Setores, em Produtos."* **Salvar** avisa *"Categoria salva"*, e a lista de categorias passa a mostrar o setor ao lado do nome.

A subcategoria vai para o setor da categoria de cima: *Cafés*, dentro de *Bebidas*, é preparada pelo setor de *Bebidas*.

## Como o Painel de pedidos mostra os setores de produção

Com pelo menos um setor de produção ativo, o topo do **Painel de pedidos** ganha o filtro **Setor**, com **Todos os setores**, cada setor ativo e **Sem setor**.

➡️ **Todos os setores:** o card mostra o pedido inteiro, com o nome do setor ao lado de cada item.

➡️ **Um setor:** o card mostra só os itens daquele setor. Quando o pedido tem item de outro setor, o card avisa, como *"+1 item(ns) de outros setores"*.

➡️ **Sem setor:** os itens das categorias que ainda não têm setor de produção.

Os setores de produção também chegam às integrações: o **Webhook do PDV** avisa quando um setor é criado, alterado ou removido.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O setor de produção é o mesmo Setor do atendimento?** Não. O setor de produção diz quem prepara os itens do pedido no PDV, como a cozinha ou o bar. O **Setor** do atendimento, no menu **Setores & Chatbot**, é o grupo da equipe que responde as conversas.
>
> **Desativei um setor de produção. O que muda no Painel de pedidos?** O setor sai do filtro **Setor** do **Painel de pedidos**, e os itens das categorias dele deixam de mostrar o nome do setor.
>
> **Apaguei um setor de produção. O que acontece com as categorias?** As categorias daquele setor ficam sem setor, e os produtos continuam no cadastro.
>
> **Por que o filtro Setor não aparece no Painel de pedidos?** O filtro **Setor** só aparece quando a empresa tem pelo menos um setor de produção ativo. Crie o setor no menu **PDV  ›  Produtos  ›  Setores**.
>
> **Como faço o bar ver só as bebidas?** Crie o setor *Bar*, escolha esse setor no **Editar categoria** das categorias de bebida e, na tela do bar, escolha **Bar** no filtro **Setor** do **Painel de pedidos**.
