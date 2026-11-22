# Carrossel de Produtos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-carrossel-de-produtos
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Carrossel de Produtos

---

🧩 O bloco **Carrossel de Produtos** envia ao cliente uma vitrine com os produtos da empresa, organizados em seções, para ele ver e escolher sem sair da conversa. É a prateleira da loja dentro do WhatsApp.

Os produtos vêm do **catálogo da Meta** vinculado à conta do WhatsApp Business (WABA) da conexão.

**🏷️ Categoria: Mensagem**

Ideal para:

☑️ **Vitrine por categoria:** separa os produtos em seções, como *Lançamentos* e *Promoções*.

☑️ **Recomendação no fluxo:** mostra os produtos certos depois que o cliente diz o que procura.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Vincule um catálogo à WABA da conexão, no Gerenciador de Negócios da Meta.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo, clique no **+** e escolha **Carrossel de Produtos**.
>
> ➡️ Escolha a conexão, escreva a mensagem, monte as seções com os produtos e clique em **Adicionar**.

## Como configurar o bloco Carrossel de Produtos

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Carrossel de Produtos**

🔘 **Conexão WhatsApp Oficial:** a conexão por onde o carrossel é enviado. Só as conexões do **WhatsApp Oficial** aparecem nesta lista; conexões Pro, por QR Code e de outros canais ficam de fora. Ao escolher a conexão, a janela procura o catálogo dela.

🔘 **Cabeçalho (opcional, máx. 60):** texto acima da mensagem.

🔘 **Mensagem (obrigatório, máx. 1024):** o texto principal do carrossel.

🔘 **Rodapé (opcional, máx. 60):** texto abaixo da mensagem.

🔘 **Seções do Carrossel:** cada seção tem um **Título da seção**, com até 24 caracteres, e os produtos dela, escolhidos pelo campo **Pesquisar produtos…**. Use **Adicionar seção** para criar outra e **Remover seção** para tirar uma.

🔲 Para finalizar, clique em **Adicionar**. A janela mostra quantos produtos e seções já estão no carrossel.

## Os limites do carrossel

◽ Pelo menos **1 seção com 1 produto**.

◽ No máximo **10 seções**.

◽ No máximo **30 produtos** no total, somando todas as seções.

⚠️ Sem catálogo vinculado à WABA, a janela avisa *Catálogo não encontrado nesta WABA — vincule um Commerce Catalog no Business Manager*, e o bloco não pode ser adicionado.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso usar o bloco Carrossel de Produtos numa conexão Pro ou por QR Code?** Não. O carrossel só é enviado por conexões do **WhatsApp Oficial** (WABA), que são as únicas listadas no bloco.
>
> **De onde vêm os produtos do Carrossel de Produtos?** Do catálogo da Meta vinculado à WABA da conexão. Produto que não está nesse catálogo não aparece na busca.
>
> **Um produto do carrossel aparece como Produto não encontrado no catálogo.** O produto foi tirado do catálogo da Meta depois de entrar no carrossel. Abra o bloco e troque ou remova o produto.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Conexão sem catálogo:** a janela avisa que o catálogo não foi encontrado. **Solução:** vincule um catálogo à WABA no Gerenciador de Negócios da Meta e abra o bloco de novo.
>
> **Carrossel cheio demais:** a janela recusa mais de 10 seções ou mais de 30 produtos. **Solução:** divida os produtos em dois carrosséis, em pontos diferentes do fluxo.
