# Setor

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-setor
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Setor

---

🧩 O bloco **Setor** encerra o trabalho do fluxo e entrega o atendimento a um Setor, no **Aguardando**, para qualquer pessoa da equipe daquele Setor assumir. É a passagem do fluxo para a equipe: o cliente foi atendido pelo fluxo até onde dava, e agora uma pessoa continua.

**🏷️ Categoria: Atendimento - Finalização**

Ideal para:

☑️ **Transbordo para a equipe:** depois da triagem do fluxo, leva o cliente ao Setor certo.

☑️ **Assunto fora do fluxo:** encaminha o que o fluxo não resolve, como negociação ou reclamação.

![Bloco Setor no FlowBuilder](https://clihelper.chatmasterveloz.com/docs-imagem/14348-bloco-departamentos.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Setor**.
>
> ➡️ Escolha o Setor e clique em **Adicionar**.

## Como configurar o bloco Setor

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Setor**

🔘 **Setor:** o Setor que vai receber o atendimento.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco aparece como **Setor**, com o nome do Setor, e não tem saída: o fluxo termina ali.

⚠️ O bloco **Setor** deixa o atendimento parado no Setor, esperando alguém da equipe, mesmo que esse Setor tenha um fluxo próprio. Para que o fluxo do outro Setor comece, use o bloco **Trocar Fluxo**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual a diferença entre o bloco Setor e o bloco Operador?** O **Setor** deixa o atendimento no **Aguardando** do Setor, para qualquer pessoa dele assumir. O **Operador** entrega a um atendente específico.
>
> **Qual a diferença entre o bloco Setor e o Trocar Fluxo?** Os dois pedem um Setor. O **Setor** deixa o atendimento esperando a equipe; o **Trocar Fluxo** inicia o fluxo ligado àquele Setor.
>
> **Posso ligar outro bloco depois do bloco Setor?** Não. O bloco não tem saída: depois dele, o atendimento é da equipe.
