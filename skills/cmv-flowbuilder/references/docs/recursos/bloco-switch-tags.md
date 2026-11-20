# Switch (tags)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-switch-tags
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Switch (tags)

---

🧩 O bloco **Switch (tags)** separa a conversa em vários caminhos de acordo com as tags do atendimento. Funciona como uma recepção que olha o crachá de quem chega e manda cada um para uma porta: em vez de encadear uma **Condição** para cada tag, um único bloco confere as regras e escolhe a saída.

Cada regra vira uma saída do bloco, com o nome que você der a ela. Quem não se encaixa em nenhuma regra segue pela saída **Nenhuma condição atendida**.

**🏷️ Categoria: Roteador**

Ideal para:

☑️ **Roteamento por perfil:** leva cliente, parceiro e fornecedor para caminhos diferentes a partir da tag de cada um.

☑️ **Prioridade de atendimento:** atende primeiro quem tem a tag de prioridade, mesmo que tenha outras tags.

☑️ **Jornada por etapa:** retoma a conversa do ponto certo conforme a tag de etapa que o atendimento já recebeu.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Switch (tags)**.
>
> ➡️ Crie uma regra para cada caminho, na ordem de prioridade, e clique em **Adicionar**.
>
> ➡️ Ligue cada saída do bloco ao próximo passo, inclusive **Nenhuma condição atendida**.

## Como configurar o bloco Switch (tags)

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Switch (tags)**

A janela **Adicionar bloco: Switch (tags)** começa com uma regra. Cada regra tem:

🔘 **Nome da saída:** o nome que aparece na saída do bloco, no desenho. Ex.: *PROPRIETÁRIO*, *VIP*, *Parceiro*.

🔘 **Comparação:** como as tags são conferidas.

◽ **possui a tag:** o atendimento tem a tag escolhida.

◽ **não possui a tag:** o atendimento não tem a tag escolhida.

◽ **possui qualquer tag da lista:** o atendimento tem pelo menos uma das tags escolhidas.

◽ **possui todas as tags da lista:** o atendimento tem todas as tags escolhidas.

🔘 **Tags:** as tags que a regra confere.

🔘 **Adicionar regra:** cria a próxima regra. Arraste uma regra, ou use **Subir** e **Descer**, para mudar a ordem; **Duplicar** cria uma cópia e **Excluir** remove.

🔘 **Nenhuma condição atendida:** fica sempre por último e não pode ser excluída. É por onde segue o atendimento que não se encaixou em nenhuma regra.

🔲 Para finalizar, clique em **Adicionar**.

## Como o Switch (tags) decide

As regras são conferidas **de cima para baixo**. A primeira regra que o atendimento atende decide a saída, e as regras de baixo nem são conferidas. Se nenhuma regra for atendida, o fluxo segue por **Nenhuma condição atendida**.

Por isso a ordem é a prioridade. Com a regra *possui a tag VIP* em primeiro e *possui a tag Cliente* em segundo, um atendimento com as duas tags vai pela saída VIP.

As tags conferidas são as do **atendimento**, no momento em que a conversa passa pelo bloco.

## Os avisos da janela

A janela do Switch (tags) avisa quando uma regra não vai funcionar como parece:

◽ *Sem tag: esta regra nunca casa.* A regra não tem nenhuma tag escolhida.

◽ *Uma das tags foi apagada: esta regra nunca casa.* Uma tag da regra foi excluída da empresa. Escolha outra.

◽ *Nunca chega a vez desta regra: a regra N já casa sempre que esta casaria.* Uma regra de cima sempre é atendida antes desta. Mude a ordem ou o conteúdo das duas.

◽ *Nome repetido: duas saídas com o mesmo nome confundem na hora de ligar.* Dê um nome diferente a cada saída.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual a diferença entre o Switch (tags) e o bloco Condição com o tipo Tag?** A **Condição** faz uma pergunta e tem duas saídas, **Verdadeiro** e **Falso**. O **Switch (tags)** confere várias regras num bloco só e tem uma saída para cada regra, mais **Nenhuma condição atendida**.
>
> **O que acontece quando o atendimento se encaixa em duas regras do Switch (tags)?** Ele segue pela regra que está mais acima. As regras de baixo não são conferidas.
>
> **O Switch (tags) confere as tags do contato ou do atendimento?** As do atendimento, no momento em que a conversa passa pelo bloco.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Regra genérica no topo:** uma regra como *possui qualquer tag da lista* em primeiro lugar atende quase todo mundo, e as regras de baixo nunca têm vez. **Solução:** coloque as regras mais específicas em cima; a janela avisa com *Nunca chega a vez desta regra*.
>
> **Nenhuma condição atendida sem ligação:** quem não se encaixa em nenhuma regra chega ao bloco e o fluxo para ali. **Solução:** ligue também a saída **Nenhuma condição atendida**, nem que seja a uma mensagem ou a um Setor.
