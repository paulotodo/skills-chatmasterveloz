# PDV (pedido no fluxo)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pdv-pedido-no-fluxo
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › PDV (pedido no fluxo)

---

🧩 O bloco **PDV (pedido no fluxo)** deixa o cliente fazer o pedido sozinho, pela conversa: ele escolhe os produtos numa lista numerada, diz a quantidade, vê o resumo com o total e confirma. O pedido nasce confirmado no atendimento, com o estoque atualizado, e a equipe é avisada.

**🏷️ Categoria: Mensagem - Roteador**

Ideal para:

☑️ **Cardápio pela conversa:** recebe pedidos de um cardápio curto sem ocupar o atendente.

☑️ **Reposição de cliente fixo:** o cliente que sempre compra os mesmos itens pede sem esperar.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **PDV (pedido no fluxo)**.
>
> ➡️ Busque e escolha os produtos que vão no menu, ou adicione uma categoria inteira, e clique em **Adicionar**.

## Como configurar o bloco PDV (pedido no fluxo)

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  PDV (pedido no fluxo)**

🔘 **Texto antes da lista:** vem antes da lista dos produtos. Em branco, o cliente lê *"Escolha um produto pelo número:"*.

🔘 **Buscar produto do cadastro:** encontra o produto pelo nome; um clique o põe no menu, até 30 produtos por bloco. A lista **Produtos no menu** mostra a ordem em que o cliente vai ver, e **Tirar do menu** tira um produto.

🔘 **Adicionar uma categoria inteira:** põe no menu todos os produtos de uma categoria, inclusive os das subcategorias e os cadastrados depois. Com uma categoria só, o cliente vê direto os produtos dela; com duas ou mais, ele escolhe primeiro a categoria.

🔘 **Sem resposta: seguir pela saída depois de (minutos):** com minutos preenchidos, o bloco ganha a saída **Sem resposta**, para quem não responder nesse tempo. Vazio ou 0 desliga.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco mostra os produtos numerados e tem as saídas **Pedido confirmado** e **Desistiu**, mais **Sem resposta** quando os minutos estão preenchidos.

## O que o cliente vê

➡️ Com duas ou mais categorias no bloco, a primeira lista é *"Escolha uma categoria pelo número:"*, com *"0 - Desistir"*. Escolhida a categoria, vem o nome dela em negrito e *"Escolha um produto pelo número:"*, com *"V - Voltar"*, que volta à lista de categorias.

➡️ A lista: *"Escolha um produto pelo número:"*, cada produto com o preço do cadastro, como *"1 - Caneca · R$ 35,90"*, e *"0 - Desistir"*.

➡️ O produto com variações aparece na lista com *"a partir de"*, como *"1 - Pizza · a partir de R$ 30,00"*. Escolhido, vem *"Escolha a opção de Pizza pelo número:"*, com cada variação e o preço, como *"2 - Grande · R$ 45,00"*, mais *"V - Voltar"* e *"0 - Desistir"*.

➡️ O produto com adicionais pergunta cada grupo, com a regra dele e as opções com o preço: *"Bordas: escolha de 1 a 2. Responda com os números separados por vírgula (ex.: 1,3)."*, *"1 - Catupiry · + R$ 5,00"*.

➡️ A quantidade: *"Quantas unidades de Caneca? Responda com um número de 1 a 999."* No produto com variações, a pergunta leva a variação, como *"Quantas unidades de Pizza (Grande)?"*.

➡️ O item adicionado, com o valor, e as opções *"1 - Adicionar outro produto"*, *"2 - Finalizar o pedido"* e *"0 - Desistir"*. Com opções, o item leva a variação e os adicionais, como *"Adicionado: 1 x Pizza (Grande) + Catupiry · R$ 50,00."*

➡️ O resumo com o total e *"1 - Confirmar o pedido"*, *"2 - Adicionar mais produtos"* e *"0 - Desistir"*.

➡️ Ao confirmar, *"Pedido #16 confirmado! Total: R$ 71,80."*, e o fluxo segue pela saída **Pedido confirmado**. No atendimento, a equipe vê *"Pedido #16 confirmado pelo cliente no fluxo de atendimento"*, com os itens e o total.

## As outras saídas

🔘 **Desistiu:** o **0** desiste em qualquer passo. Nenhum pedido é criado, e o fluxo segue pela saída **Desistiu**.

🔘 **Sem resposta:** quando o cliente para de responder pelo tempo escolhido, o fluxo segue pela saída **Sem resposta**.

⚠️ O preço que o cliente vê e paga é sempre o do cadastro de produtos na hora do pedido.

## O pedido que nasce no fluxo

O pedido feito pelo bloco entra no **Painel de pedidos** em **Novo**, com a frase *"Pedido feito pelo cliente no fluxo de atendimento"*, e na lista de pedidos sem vendedor e com *Nota não enviada*: o bloco confirma o pedido sem mandar a nota. No **Relatório do PDV**, ele aparece em *Sem atendente*.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O pedido feito pelo bloco PDV aparece para a equipe?** Sim. O pedido nasce confirmado no atendimento do cliente, com o estoque atualizado, aparece no **Painel de pedidos** e na lista de pedidos, e a equipe vê o aviso do pedido na própria conversa.
>
> **O cliente recebe a nota do pedido feito pelo bloco PDV?** Não sozinho. O cliente recebe a confirmação com o número e o total. Para mandar a nota, abra o pedido no menu **PDV  ›  Pedidos** e use **Reenviar nota**.
>
> **Dá para o cliente pagar pelo bloco PDV (pedido no fluxo)?** O bloco monta e confirma o pedido. O pagamento é registrado depois, pela equipe, ou feito online, pelo link de pagamento ou pelo Pix gerado no pedido.
>
> **Dá para oferecer só uma categoria no bloco PDV (pedido no fluxo)?** Dá. Com uma categoria só, o cliente vai direto à lista de produtos dela, sem a escolha da categoria.
>
> **O cliente escolhe tamanho e adicionais pelo bloco PDV (pedido no fluxo)?** Sim. No produto com variações, o bloco pergunta a opção pelo número, e no produto com adicionais pergunta cada grupo, com os números separados por vírgula. O preço de cada escolha aparece ao lado da opção.
>
> **Posso continuar o fluxo depois do pedido?** Sim. Ligue a saída **Pedido confirmado** ao próximo bloco, como uma mensagem de agradecimento ou a transferência para um Setor.
