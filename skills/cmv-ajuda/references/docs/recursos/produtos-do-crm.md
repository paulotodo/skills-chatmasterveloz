# Produtos do CRM

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/produtos-do-crm
- **Categoria:** Recursos
- **Menu:** CRM › Produtos do CRM

---

🧩 O catálogo de **Produtos** guarda o que a sua empresa vende, com preço e descrição. Escolhido numa oportunidade, o produto já traz o preço; numa proposta, leva a descrição para o PDF.

Com o catálogo montado, ninguém precisa digitar o mesmo produto de jeitos diferentes. E, com o **SKU** (o código de cada produto), dá para cadastrar e atualizar o catálogo inteiro de uma vez, por planilha.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **CRM  ›  Produtos**.
>
> ➡️ Clique em **Adicionar Produto**.
>
> ➡️ Preencha pelo menos **Nome do Produto** e **Preço** e clique em **Adicionar**.
>
> ➡️ Para cadastrar muitos produtos de uma vez, clique em **Mais ações** e em **Baixar modelo**, preencha a planilha e, no mesmo botão, clique em **Importar planilha**.

## Vídeo Tutorial

[Vídeo Voomly — id CsVdiUdHygzKoE2LwEMgzK1GxS0_Ex8iLuCNaBQjEI4vxnh5W, tipo v]  

## Os campos do produto

🔘 **Nome do Produto:** obrigatório.

🔘 **SKU (código do produto):** opcional e único na empresa, com até 64 caracteres. É por ele que a importação por planilha reconhece o produto para atualizar. Maiúscula e minúscula não fazem diferença: **CAM-001** e **cam-001** são o mesmo código.

🔘 **Marca:** opcional, com até 60 caracteres. Ao digitar, o campo sugere as marcas que a empresa já usa.

🔘 **Descrição:** um texto curto. Aparece no card do produto e, na proposta, logo abaixo do nome do item.

🔘 **Detalhes:** um texto mais longo, que vai para o PDF da proposta só no item em que a caixa **Detalhes** estiver marcada.

🔘 **Preço:** obrigatório. É o valor que entra na oportunidade quando o produto é escolhido.

🔘 **Cobrança padrão:** **Única**, **Mensal** ou **Anual**. Nas palavras da tela: *"Já vem escolhida quando o produto é adicionado numa oportunidade — lá ainda dá para trocar."* Um produto novo começa em **Única**.

🔘 **Imagem:** *JPG, PNG, GIF até 5MB*.

## A lista de produtos

Cada produto aparece num card com a imagem, o nome, a marca e o SKU (quando têm), o preço e a descrição — a cobrança padrão não aparece no card. No card, o lápis edita, o **Duplicar** cria um produto novo a partir daquele e a lixeira apaga — a plataforma pergunta antes de apagar.

O **Duplicar**, o ícone entre o lápis e a lixeira, abre a janela **Duplicar produto** já preenchida com o produto do card: o nome ganha *(cópia)* no fim, o **SKU** fica vazio, e a marca, a descrição, o preço e a **Cobrança padrão** vêm iguais. Ajuste o que for diferente e clique em **Adicionar**. O produto original continua como estava.

O campo **Pesquisar produtos...** procura pelo nome, pelo SKU e pela marca — basta digitar parte do código.

O filtro **Marca** mostra só os produtos de uma marca, ou os **Sem marca**. Ele aparece depois que algum produto tem marca.

O produto sem **Marca** e com a característica *Marca* na ficha técnica do cadastro usa a marca da ficha: o card mostra *Marca: Acme (da ficha técnica)*, e o produto entra no filtro **Marca** e na busca por ela. Com o campo **Marca** vazio, a ajuda do campo mostra a marca que vem da ficha.

## Como cadastrar produtos por planilha

[Vídeo Voomly — id AEYizM2p2pPUWhvGCxRzp3DGSVgRy8umJsBT3sYZDb1bxELeM, tipo v]  

Acesse o menu **CRM  ›  Produtos**

As ações de planilha ficam no botão **Mais ações**, no topo da lista de **Produtos**: **Baixar modelo**, **Importar planilha**, **Exportar planilha** e **Substituir catálogo**.

🔘 **Baixar modelo:** baixa a planilha *modelo-produtos.xlsx*, com duas abas. Na **Produtos**, uma linha por produto, nas colunas **SKU**, **Nome**, **Preço**, **Descrição**, **Detalhes**, **Cobrança** e **URL da imagem**, mais a coluna **Marca**. Na **Instruções**, como preencher cada coluna.

🔘 **Colunas obrigatórias:** **SKU**, **Nome** (de 2 a 50 caracteres) e **Preço** (como *49,90* ou *1.299,00*, com ou sem R$). Na **Cobrança**, use **Única**, **Mensal** ou **Anual**; em branco, o produto novo fica com Única e o produto que já existe continua com a cobrança que tinha.

🔘 **SKU na planilha:** entra exatamente como está escrito, inclusive com zeros à esquerda, como *00710*.

🔘 **URL da imagem:** opcional. O endereço precisa começar com *https://*.

🔘 **Marca:** opcional, com até 60 caracteres. Na atualização, a célula em branco não apaga a marca que o produto já tem.

🔘 **Importar planilha:** escolha o arquivo preenchido. Além do *.xlsx* do modelo, o botão aceita *.xls* e *.csv*. São até 2000 produtos por arquivo. No *.csv*, as colunas podem ser separadas por ponto e vírgula ou por vírgula, e os acentos são mantidos, seja qual for o programa que salvou o arquivo.

⚠️ O modelo vem com duas linhas de exemplo. Apague as duas ou troque pelos seus produtos antes de importar — senão elas entram no catálogo.

### O que a importação faz com cada linha

🔘 **SKU que ainda não existe:** cria o produto.

🔘 **SKU que já existe:** atualiza o produto. A célula em branco não apaga nada: o produto continua com o que já tinha.

🔘 **Produto cadastrado antes, sem SKU:** se o nome for igual ao da planilha, ele recebe o SKU e é atualizado, em vez de virar outro produto.

🔘 **A mesma planilha importada de novo:** não duplica nada. Os produtos entram como atualizados.

### O resultado da importação

Ao terminar, a janela **Resultado da importação** mostra quantos produtos foram **Criados**, quantos foram **Atualizados** e quantas linhas ficaram **Com problema**. Quando todas entram, ela avisa *"Todas as linhas da planilha foram importadas."*

As linhas com problema não entram e aparecem numa tabela com a **Linha** da planilha, o **SKU** e o **Motivo**. As outras entram normalmente: corrija só as recusadas e importe a planilha de novo — o que já entrou é atualizado, sem duplicar.

### Exportar e substituir o catálogo

Para mexer no catálogo inteiro de uma vez, o botão **Mais ações** tem mais duas ações:

🔘 **Exportar planilha:** baixa o catálogo em *produtos.xlsx*, com todos os produtos, ativos e inativos. A aba **Produtos** tem as colunas **ID**, **SKU**, **Nome**, **Preço**, **Descrição**, **Detalhes**, **Cobrança**, **URL da imagem** e **Marca**. A aba **Instruções** explica: *"A coluna ID diz qual produto é cada linha: não a altere. Com ela, até o SKU e o nome podem ser trocados, e o produto continua o mesmo…"*

🔘 **Substituir catálogo:** pergunta *"Substituir o catálogo pela planilha"* e avisa: *"Escolha a planilha (de preferência a exportada, com a coluna ID). Os produtos dela são criados ou atualizados, e os que NÃO estiverem nela serão apagados. Se alguma linha tiver problema, nada é apagado."* Com **OK**, escolha o arquivo.

O resultado mostra também quantos produtos foram **Removidos**. Com alguma linha com problema, nenhum produto é apagado, e a janela avisa *"Nada foi apagado: há linhas com problema. Corrija a planilha e substitua de novo."* As linhas sem problema entram como atualizadas mesmo assim.

⚠️ O **Substituir catálogo** apaga do cadastro todo produto que não está na planilha. Para só criar e atualizar, sem apagar nada, use **Importar planilha**.

## Onde o produto é usado

➡️ Na oportunidade, em **Produto / Serviço**, com Item Único ou Múltiplos Itens. O campo também acha o produto pelo SKU.

➡️ Na regra **Encadear para outro funil**, em **Quando o produto for**.

➡️ Na proposta comercial, com a descrição e, quando marcado, os detalhes.

A tela de Produtos é de administrador e supervisor.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Por que os Detalhes não aparecem no card do produto?** O card mostra só a Descrição. Os Detalhes vão para o PDF da proposta, no item em que a caixa **Detalhes** estiver marcada.
>
> **Quais campos são obrigatórios?** Só **Nome do Produto** e **Preço**.
>
> **Como cadastro um produto parecido com outro que já existe?** No card do produto, clique em **Duplicar**, o ícone entre o lápis e a lixeira. A janela **Duplicar produto** vem preenchida com os dados dele, com *(cópia)* no nome e o **SKU** vazio: troque o que for diferente e clique em **Adicionar**.
>
> **Importei a mesma planilha duas vezes. Duplicou?** Não. O SKU identifica o produto: na segunda vez, todos entram como **Atualizados**.
>
> **Deixei células em branco. O produto perdeu a descrição?** Não. Na atualização, célula em branco não muda nada.
>
> **Meus produtos foram cadastrados antes do SKU. A planilha vai duplicar?** Não, se o nome na planilha for igual ao do cadastro: o produto recebe o SKU e é atualizado.
>
> **Na planilha o código está em minúsculas e no cadastro em maiúsculas. Duplica?** Não. Maiúscula e minúscula não fazem diferença: o produto é atualizado e continua com o código do cadastro.
>
> **Posso cadastrar um produto com cobrança anual pela planilha?** Pode. Escreva **Anual** na coluna **Cobrança**, do mesmo jeito que **Única** e **Mensal**.
>
> **Como tiro do catálogo de Produtos vários produtos de uma vez pela planilha?** Em **Mais ações**, clique em **Exportar planilha**, apague da aba **Produtos** as linhas dos produtos que vão sair, sem mexer na coluna **ID**, e use **Substituir catálogo** com essa planilha. Os produtos que não estão nela são apagados.
>
> **Usei o Substituir catálogo e nenhum produto foi apagado. Por quê?** Alguma linha da planilha teve problema: nesse caso, o **Substituir catálogo** não apaga nada e avisa *"Nada foi apagado: há linhas com problema."* Corrija as linhas da tabela de problemas e substitua de novo.
>
> **Como vejo só os produtos de uma marca?** No filtro **Marca** da lista de produtos, escolha a marca, ou **Sem marca** para os produtos que ainda não têm. O campo **Pesquisar produtos...** também acha pela marca.

> **[ERROS]**
>
> #### Erros Comuns
>
> **SKU em branco:** a linha não tem código e fica de fora. **Solução:** preencha a coluna **SKU** — na planilha ela é obrigatória, mesmo sendo opcional no formulário.
>
> **Nome muito curto (mínimo de 2 caracteres):** o nome tem uma letra só. **Solução:** use um nome de 2 a 50 caracteres.
>
> **Preço inválido:** o valor não é um número, como *abc*. **Solução:** escreva como *49,90* ou *1.299,00*.
>
> **Cobrança inválida:** a coluna tem outra palavra, como *Semanal*, e o motivo avisa *"use Única, Mensal ou Anual"*. **Solução:** use **Única**, **Mensal** ou **Anual**, ou deixe em branco.
>
> **SKU repetido na planilha:** o mesmo código aparece em duas linhas; a segunda fica de fora e o motivo diz em que linha ele já foi usado. **Solução:** dê um código diferente a cada produto.
>
> **Já existe um produto com o SKU:** aparece ao salvar no formulário um código que outro produto já usa, mesmo que mude só a maiúscula, e diz qual é. **Solução:** escolha outro código ou edite o produto que já tem esse.
>
> **URL da imagem com http://:** a linha fica de fora, com o motivo *"URL da imagem com http://: use o endereço com https://"*. **Solução:** use o endereço da imagem que começa com *https://*.
>
> **A planilha não tem a(s) coluna(s) obrigatória(s):** o arquivo não traz, com o título do modelo, uma das colunas **SKU**, **Nome** ou **Preço**, e nada é importado. **Solução:** baixe o modelo e preencha nele, sem mudar os títulos da primeira linha.
