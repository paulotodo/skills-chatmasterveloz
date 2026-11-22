# Remover Tag

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-remover-tag
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Remover Tag

---

🧩 O bloco **Remover Tag** tira uma tag do atendimento enquanto ele passa pelo fluxo. É o par do bloco **Tag**: um marca a etapa em que a conversa entrou, o outro limpa a marca da etapa que ficou para trás.

Ele pode tirar uma tag escolhida ou todas as tags do atendimento de uma vez.

**🏷️ Categoria: Dados**

Ideal para:

☑️ **Troca de etapa:** tira *Novo Lead* quando o cliente vira *Em Negociação*.

☑️ **Recomeço limpo:** zera as tags de um atendimento que volta ao início do fluxo.

☑️ **Fim de uma campanha:** retira a marca de uma ação que já acabou.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Remover Tag**.
>
> ➡️ Escolha a tag, ou **Remover Todas as Tags**, e clique em **Adicionar**.

## Como configurar o bloco Remover Tag

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Remover Tag**

🔘 **Tag:** a tag que será tirada do atendimento quando a conversa passar pelo bloco. A primeira opção da lista, **Remover Todas as Tags**, tira todas as tags que o atendimento tiver.

🔲 Para finalizar, clique em **Adicionar**.

⚠️ **Remover Todas as Tags** não pergunta quais: tira inclusive as tags que a equipe colocou à mão durante o atendimento. Use quando o recomeço tiver de ser completo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **E se o bloco Remover Tag pedir para tirar uma tag que o atendimento não tem?** Nada acontece: o fluxo segue para o próximo passo, sem erro.
>
> **Consigo remover duas tags escolhidas com um bloco Remover Tag só?** Não. Cada bloco tira uma tag, ou todas de uma vez com **Remover Todas as Tags**. Para tirar duas tags específicas, use dois blocos seguidos.
>
> **Qual a diferença entre o bloco Remover Tag e o bloco Tag?** O **Tag** coloca uma tag no atendimento; o **Remover Tag** tira. Os dois costumam andar juntos quando a conversa muda de etapa.
