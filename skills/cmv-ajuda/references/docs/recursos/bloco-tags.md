# Tag

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-tags
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Tag

---

🧩 O bloco **Tag** coloca uma tag no atendimento enquanto ele passa pelo fluxo, sem ninguém da equipe precisar fazer isso à mão. É a etiqueta que separa quem pediu orçamento, quem é cliente antigo ou em que etapa a conversa está.

A tag não aparece para o cliente. Ela serve à equipe e ao próprio fluxo: dá para decidir caminhos por ela mais adiante e encontrar os atendimentos marcados.

**🏷️ Categoria: Dados**

Ideal para:

☑️ **Segmentação:** marca o interesse do cliente, como Vendas, Suporte ou Financeiro, para ações futuras.

☑️ **Etapa da jornada:** registra em que ponto do funil a conversa chegou.

☑️ **Decisão mais adiante:** prepara o atendimento para um bloco **Condição** ou **Switch (tags)** decidir o caminho pela tag.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Tag**.
>
> ➡️ Escolha a tag e clique em **Adicionar**.

## Como configurar o bloco Tag

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Tag**

🔘 **Tag:** a tag, entre as cadastradas na empresa, que será colocada no atendimento quando a conversa passar pelo bloco.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco aparece como **Tag**, com o nome da tag escolhida, e tem uma saída para o próximo passo.

⚠️ Cada bloco coloca **uma** tag. Para colocar mais de uma, use um bloco **Tag** para cada uma, um seguido do outro.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente vê a tag que o bloco Tag coloca?** Não. As tags são internas, vistas só pela equipe.
>
> **Posso colocar várias tags com um bloco Tag só?** Não. Cada bloco coloca uma tag; para mais de uma, encadeie um bloco **Tag** para cada.
>
> **Como tiro uma tag do atendimento pelo fluxo?** Com o bloco **Remover Tag**, que tira uma tag escolhida ou todas de uma vez.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Esquecer de criar a tag antes:** a tag não aparece na lista **Escolha** do bloco. **Solução:** cadastre a tag no menu **Tags** e abra o bloco de novo.
>
> **Confundir tag com Setor:** colocar a tag "Financeiro" esperando que o atendimento vá para o Setor Financeiro. A tag só marca; ela não move a conversa. **Solução:** para mudar o atendimento de Setor, use o bloco **Setor**.
