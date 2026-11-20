# Relatório do PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/relatorio-do-pdv
- **Categoria:** Recursos
- **Menu:** PDV › Relatório do PDV

---

🧩 Quanto a loja vendeu na semana, quanto entrou de verdade, quanto ainda falta receber e quanto sobrou de lucro? O **Relatório do PDV** responde por período e por atendente, separado por produto, por categoria, por forma de pagamento e por dia, e exporta tudo em CSV.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **PDV  ›  Relatório do PDV**.
>
> ➡️ Escolha o período em **De** e **Até** e, se quiser, um **Atendente**.
>
> ➡️ Para levar os números para uma planilha, clique em **Exportar CSV**.

## O resumo

🔘 **Vendido:** o total dos pedidos do período, da conversa, do balcão e do fluxo de atendimento. O pedido cancelado fica fora.

🔘 **Pedidos** e **Ticket médio:** quantos pedidos e o valor médio de cada um.

🔘 **Recebido (líquido):** o que entrou, descontados os estornos.

🔘 **A receber:** o que foi vendido e ainda não foi pago.

🔘 **Cancelados:** quantos pedidos foram cancelados e o valor deles.

🔘 **Custo**, **Lucro** e **Margem:** quanto custaram os itens vendidos, quanto sobrou e a margem, em porcentagem. Entram só os itens com **Custo** cadastrado no produto; a variação sem custo próprio entra com o custo do produto. Cada venda guarda o custo da hora em que foi feita.

Logo abaixo, uma linha detalha o recebido, o estornado, os descontos, os acréscimos e as entregas, que somam as taxas de entrega.

Quando o período tem venda de item sem custo cadastrado, outra linha diz quanto ficou de fora, como *"R$ 806,20 foram vendidos em itens sem custo cadastrado e ficaram fora do lucro e da margem."* Sem nenhum produto com custo, o Relatório do PDV mostra *"Cadastre o custo dos produtos para ver aqui o lucro e a margem das vendas."*

## As tabelas

🔘 **Por produto:** a quantidade, o total, o **Custo**, o **Lucro** e a **Margem (%)** de cada produto. O produto com variações aparece uma vez por variação, com o nome dela entre parênteses, como *Pizza (Grande)*. O produto sem custo cadastrado aparece com custo e lucro zerados e a margem em branco.

🔘 **Por categoria:** a quantidade, o total e a participação de cada categoria nas vendas, com o caminho da subcategoria, como *Bebidas › Cafés*. A tabela aparece quando o período tem venda de produto com categoria, e as vendas sem categoria ficam em *Sem categoria*.

🔘 **Por atendente:** pedidos, total, ticket médio e recebido de cada pessoa, e o custo, o lucro e a margem das vendas dela. O pedido feito pelo cliente no fluxo de atendimento aparece em *Sem atendente*.

🔘 **Por forma de pagamento:** recebido, estornado e líquido de cada forma, inclusive os links do **Asaas**, do **Mercado Pago** e do **PagSeguro** e o **Pix (PaggPix)**.

🔘 **Por dia:** os pedidos e o total de cada dia, do mais recente para o mais antigo. Sem período escolhido, o relatório mostra os últimos 30 dias, começando por hoje.

🔘 **Ocultar dias sem vendas:** a caixa acima da tabela **Por dia**. Marcada, a tabela mostra só os dias que tiveram venda, e a escolha continua valendo quando você abre o Relatório do PDV de novo.

## O arquivo CSV

O **Exportar CSV** baixa o relatório do período, com as colunas separadas por ponto e vírgula. O resumo traz o **Custo**, o **Lucro**, a **Margem** e o que foi vendido sem custo cadastrado, e as tabelas **Por produto**, **Por atendente** e **Por dia** trazem as colunas **Custo**, **Lucro** e **Margem (%)**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Quem vê o Relatório do PDV?** Administrador e supervisor. O atendente que abre a tela lê *"Só administradores e supervisores veem o relatório do PDV."*
>
> **Por que o Vendido é maior que o Recebido?** O **Vendido** conta os pedidos do período; o **Recebido (líquido)** conta só o que já foi pago, menos os estornos. A diferença está em **A receber**.
>
> **Por que o Relatório do PDV não mostra o lucro de um produto?** O produto não tem **Custo** cadastrado, e as vendas dele ficam fora do lucro e da margem. O custo se preenche no cadastro do produto, no menu **PDV  ›  Produtos**.
>
> **Mudei o custo de um produto. As vendas antigas mudam no Relatório do PDV?** Não. Cada venda guarda o custo da hora em que foi feita, e só as vendas novas usam o custo novo.
>
> **Os adicionais têm custo no Relatório do PDV?** Não. O adicional não tem campo de custo, e o valor dele entra inteiro no lucro: uma venda de R$ 56,00, com a variação de custo R$ 15,00 e duas bordas, aparece com lucro de R$ 41,00.
>
> **Pus categoria nos produtos e as vendas antigas continuam em Sem categoria no Relatório do PDV. Por quê?** A venda guarda a categoria que o produto tinha na hora em que foi vendido. As vendas feitas antes de o produto ganhar categoria continuam em **Sem categoria**, e só as vendas novas entram na categoria.
>
> **Por que a tabela Por dia do Relatório do PDV mostra dias com zero pedidos?** São os dias do período sem venda. Marque **Ocultar dias sem vendas**, acima da tabela, para ver só os dias que tiveram venda.
>
> **O que é Sem atendente no Relatório do PDV?** São os pedidos que o cliente fez sozinho, pelo fluxo de atendimento, sem um atendente vendendo.
