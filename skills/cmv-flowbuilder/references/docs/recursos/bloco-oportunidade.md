# Oportunidade

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-oportunidade
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Oportunidade

---

🧩 O bloco **Oportunidade** registra o negócio no CRM sem ninguém digitar nada: quando o fluxo passa por ele, nasce uma oportunidade para o contato da conversa, no funil e na etapa escolhidos, já com produto, valor e origem.

Ideal para:

☑️ **Captação pelo robô:** o cliente escolheu *Quero um orçamento* no menu, e a negociação já aparece no Board para a equipe de vendas.

☑️ **Distribuir negócios:** cada fluxo pode deixar a oportunidade com um vendedor diferente.

**🏷️ Categoria: Dados**

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder** e edite o fluxo.
>
> ➡️ Clique no **+** e escolha **Oportunidade**.
>
> ➡️ Escolha o **Operador**, o **Funil do CRM** e a **Etapa do Funil**, preencha o resto e clique em **Adicionar**.
>
> ➡️ Ligue o bloco ao fluxo e clique em **Salvar Fluxo**.

## Os campos do bloco

🔘 **Operador:** quem fica como **responsável** pela oportunidade. É obrigatório: sem ele, a tela avisa *"Escolha um operador!"*.

🔘 **Funil do CRM:** o funil em que a oportunidade nasce. Também é obrigatório.

🔘 **Etapa do Funil:** a etapa de entrada. Sem escolha, vale a **Primeira etapa do funil**. A lista traz também as etapas de ganho e de perda.

🔘 **Produto / Serviço:** escolha um produto do catálogo ou digite um nome.

🔘 **Valor da Oportunidade:** o valor do negócio, em reais.

🔘 **Origem da venda:** de onde veio o negócio, entre as origens cadastradas no menu **CRM  ›  Cadastros do CRM**. O campo aparece quando há origem cadastrada.

🔘 **Unidades responsáveis:** as unidades da empresa que respondem pela venda, cadastradas no menu **CRM  ›  Minha evolução**, no ícone **Unidades e equipes**. Dá para marcar várias; **Selecionar todas** marca todas e vira **Limpar** quando todas estão marcadas.

🔘 **Mensagem da Oportunidade:** opcional. O texto vai para o campo **Informações adicionais** da oportunidade.

No desenho do fluxo, o bloco mostra o operador, a etapa, a origem e o começo da mensagem. Ele tem uma saída: o fluxo continua depois dele.

## O que acontece quando o fluxo passa pelo bloco

🔘 Nasce uma oportunidade para o **contato da conversa**, ligada a ela — no Board, o card ganha o botão **Abrir conversa**.

🔘 O **Operador** fica como responsável pela oportunidade. **A conversa não vai para ele:** o atendimento continua onde estava, no mesmo setor e com o mesmo atendente, ou sem nenhum.

🔘 A oportunidade nasce com as **Unidades responsáveis** marcadas no bloco. Com mais de uma, a venda conta em cada unidade do jeito escolhido no menu **Configurações  ›  Opções  ›  Vendas**, seção **CRM**, em **Venda em várias unidades conta**.

🔘 A oportunidade nasce sem nome próprio. No Board, o card mostra o nome do contato.

⚠️ **O bloco não confere se o contato já tem oportunidade.** Cada passagem do fluxo pelo bloco cria uma nova. Um fluxo que tem só este bloco, ligado a um setor, cria uma oportunidade a cada mensagem que o cliente manda enquanto o atendimento espera no setor. Coloque o bloco num trecho que o cliente atravessa uma vez só — por exemplo, depois de uma escolha no **Menu**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O bloco Oportunidade não aparece na lista de blocos.** Ele faz parte do CRM: aparece quando o plano da empresa inclui o CRM.
>
> **Quem fica com a conversa?** Ninguém novo: o bloco não mexe no atendimento. Para mandar a conversa a alguém, use depois dele o bloco **Operador** ou o bloco **Setor**.
>
> **Onde vejo a mensagem que o bloco gravou?** Na oportunidade, no campo **Informações adicionais**.
>
> **Dá para escolher um produto cadastrado?** Sim. O campo **Produto / Serviço** lista os produtos do catálogo e também aceita um nome digitado.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Oportunidades repetidas no Board:** o fluxo passou várias vezes pelo bloco para o mesmo contato. **Solução:** mude o bloco para um trecho do fluxo que roda uma vez por atendimento, como depois de uma escolha do cliente.
