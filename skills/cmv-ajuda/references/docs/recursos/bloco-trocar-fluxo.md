# Trocar Fluxo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-trocar-fluxo
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Trocar Fluxo

---

🧩 O bloco **Trocar Fluxo** passa a conversa para outro fluxo: o do Setor escolhido. É assim que fluxos pequenos se ligam, um para triagem, outro para o financeiro, outro para o suporte, sem o cliente perceber a troca.

O fluxo atual termina no bloco, e o fluxo ligado ao Setor escolhido começa.

**🏷️ Categoria: Finalização**

Ideal para:

☑️ **Fluxos por assunto:** em vez de um fluxo gigante, fluxos menores que passam a conversa adiante.

☑️ **Reaproveitamento:** um mesmo fluxo de cadastro chamado a partir de vários outros.

![Bloco Trocar Fluxo no FlowBuilder](https://clihelper.chatmasterveloz.com/docs-imagem/14350-bloco-trocar-de-fluxo.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Ligue o fluxo de destino a um Setor, no cadastro do Setor.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo atual, clique no **+** e escolha **Trocar Fluxo**.
>
> ➡️ Escolha o Setor e clique em **Adicionar**.

## Como configurar o bloco Trocar Fluxo

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Trocar Fluxo**

🔘 **Setor com fluxo:** o Setor cujo fluxo vai assumir a conversa. A lista mostra só os Setores que têm um fluxo ligado.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco aparece como **Trocar Fluxo** e não tem saída: a conversa segue no outro fluxo.

⚠️ Para o fluxo novo rodar, o atendimento é levado ao **Aguardando**, caso não esteja.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente percebe a troca de fluxo?** Não. Para o cliente, a conversa continua normalmente.
>
> **Posso criar um loop infinito com o Trocar Fluxo?** Pode, e é perigoso. Se o fluxo A manda para o B e o B manda para o A sem nenhuma condição de parada, o cliente fica preso num laço de mensagens.
>
> **Por que o meu Setor não aparece no bloco Trocar Fluxo?** Porque esse Setor não tem um fluxo ligado a ele. Ligue o fluxo no cadastro do Setor.
>
> **O Trocar Fluxo funciona igual ao bloco Setor?** Não. Os dois pedem um Setor, mas o bloco **Setor** deixa o atendimento parado esperando a equipe, mesmo que o Setor tenha fluxo. O **Trocar Fluxo** inicia o fluxo ligado ao Setor.
>
> **O Trocar Fluxo volta ao fluxo anterior depois?** Não há volta automática. Se precisar retornar, desenhe o caminho de volta no segundo fluxo, com outro **Trocar Fluxo**.
