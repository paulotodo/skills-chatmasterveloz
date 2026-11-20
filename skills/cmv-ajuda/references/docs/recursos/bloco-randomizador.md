# Randomizador

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-randomizador
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Randomizador

---

🧩 O bloco **Randomizador** divide o fluxo em dois caminhos por sorteio. Você define a chance de cada um, por exemplo 40% para o caminho A e 60% para o B, e a cada cliente que passa o bloco sorteia por onde ele segue.

É o jeito de testar duas versões de uma mensagem, ou de dividir os contatos entre duas equipes, sem regra fixa.

**🏷️ Categoria: Roteador**

Ideal para:

☑️ **Teste A/B:** compara duas ofertas ou dois textos, cada um com uma parte dos clientes.

☑️ **Divisão de carga:** manda parte dos contatos para um caminho e o resto para outro.

![FlowBuilder Bloco Randomizador](https://clihelper.chatmasterveloz.com/docs-imagem/14338-bloco-randomizador-768x414.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Randomizador**.
>
> ➡️ Arraste o controle até a porcentagem do primeiro caminho e clique em **Adicionar**.
>
> ➡️ Ligue as duas saídas aos caminhos.

## Como configurar o bloco Randomizador

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Randomizador**

🔘 **Porcentagem:** o controle vai de 0% a 100% e define a chance do primeiro caminho. O segundo fica com o restante. A janela mostra a porcentagem de cada caminho, uma de cada lado da barra.

🔲 Para finalizar, clique em **Adicionar**. Com o controle em 0%, a janela avisa *Adicione o valor de intervalo* e não adiciona o bloco.

No desenho, o bloco tem **duas saídas**, cada uma com a sua porcentagem, como *40%* e *60%*. Ligue as duas.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Randomizador divide os clientes com a porcentagem exata?** Não. A porcentagem é a chance de cada cliente, sorteada a cada passagem, sem levar em conta quem já passou. Em volume alto, a divisão se aproxima do configurado; com poucos clientes, pode haver diferença.
>
> **Posso ter mais de dois caminhos no Randomizador?** Cada bloco divide em dois. Para três ou mais caminhos, ligue uma saída a um segundo **Randomizador**.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Uma saída sem ligação:** a parte dos clientes sorteada para aquele caminho para no bloco. **Solução:** ligue as duas saídas.
