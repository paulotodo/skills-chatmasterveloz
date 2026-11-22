# Distribuição e rodízio em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/distribuicao-e-rodizio-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Atendimento em Configurações › Distribuição e rodízio em Configurações

---

🧩 A seção **Distribuição e rodízio** decide como os atendimentos chegam a cada atendente: quem entra no sorteio do rodízio de atendimento, se o atendimento que já tem dono fica só com ele, onde os blocos **Rodízio** e **Operador** do FlowBuilder Nativo deixam o atendimento e quando alguém deixa de receber — por ter chegado no limite de atendimentos ou por estar numa chamada.

O rodízio em si é montado em outro lugar: nos Setores, no bloco **Rodízio** do FlowBuilder Nativo ou no menu **Rodízios**. A seção **Distribuição e rodízio** guarda as opções da empresa que mudam a entrega, e cada uma vale para a empresa inteira.

Ideal para:

☑️ **Atendimento com dono:** o atendimento aguardando que já tem um atendente vinculado fica só na aba **Aguardando (MEUS)** dele.

☑️ **Carga equilibrada:** tira do rodízio quem chegou no limite de atendimentos ou está numa chamada.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Atendimento**, seção **Distribuição e rodízio**.
>
> ➡️ Escolha o valor de cada opção. Ela grava assim que você muda, com o aviso *"Operação atualizada com sucesso."*
>
> ➡️ Para usar o **Aguardando (MEUS)**, ligue primeiro **Aguardando com dono: só ele vê?**.

## Os campos, na ordem da tela

🔘 **Modo de Randomização de Atendimento:** quem entra no sorteio do rodízio de atendimento. **Somente Usuários Online** sorteia só entre quem está on-line no momento; **Usuários Online e Offline** inclui também quem está off-line.

🔘 **Exibir o Relatório do Rodízio (botão Ver relatório, na tela Rodízios)?:** com **Sim**, a tela do menu **Rodízios** ganha o botão **Ver relatório**, que abre a **Distribuição do rodízio**: como o bloco **Rodízio** do FlowBuilder Nativo distribuiu os atendimentos entre os operadores, comparado com a meta de cada um. Com **Não**, o botão some.

🔘 **Aguardando com dono: só ele vê?:** nas palavras da tela, *"Ligado, o atendimento aguardando que tem um operador vinculado só aparece para ele, na aba "Aguardando (MEUS)"; a aba Aguardando mostra só os sem dono. Admins e supervisores com "ver todos" continuam vendo tudo."*

🔘 **Rodízio do FlowBuilder Nativo deixa no Aguardando (MEUS)?:** nas palavras da tela, *"Ligado, o bloco Rodízio entrega o atendimento ao operador escolhido em "Aguardando (MEUS)", e não em Atendendo. Para o limite de atendimentos, o aguardando dele também conta."* No bloco **Rodízio**, cada participante tem a opção **Entregar em**: a escolha **Padrão da empresa** segue esta opção.

🔘 **Bloco Operador do FlowBuilder Nativo deixa no Aguardando (MEUS)?:** nas palavras da tela, *"Ligado, o bloco Operador entrega o atendimento em "Aguardando (MEUS)" do operador, e não em Atendendo."*

⚠️ As opções que deixam o atendimento no **Aguardando (MEUS)** dependem de **Aguardando com dono: só ele vê?**. Com ela em **Não**, a tela mostra abaixo delas *"Ligue antes "Aguardando com dono: só ele vê?" — sem ela, o aguardando com dono apareceria para todos."* A **Transferência para operador deixa no Aguardando (MEUS)?**, logo abaixo, na seção **Transferências**, segue a mesma regra.

🔘 **Bloquear aceitar acima do limite de atendimentos:** **Sim** ou **Não**. O limite de cada pessoa é o **Limite de atendimentos simultâneos**, no cadastro dela, no menu **Equipe  ›  editar o usuário**, aba **Geral**. Nas palavras da tela: *"Com o limite preenchido no cadastro do usuário, ao chegar nesse número de atendimentos abertos ele não aceita, não recebe transferência e não inicia conversa até finalizar algum — com ou sem rodízio. Admin e supervisor não são bloqueados."* Com **Não**, quem chega no limite só sai do rodízio até fechar algum atendimento.

🔘 **Tirar do rodízio quem está em chamada:** nas palavras da tela, *"Ligado, quem estiver numa chamada de áudio ou vídeo (com a equipe ou com um cliente) não recebe atendimentos do rodízio até sair dela."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Quem está off-line entra no rodízio de atendimento?** Depende do **Modo de Randomização de Atendimento**, na seção **Distribuição e rodízio**: em **Somente Usuários Online**, não; em **Usuários Online e Offline**, sim.
>
> **Não acho o botão Ver relatório na tela Rodízios.** Ele aparece com **Sim** em **Exibir o Relatório do Rodízio (botão Ver relatório, na tela Rodízios)?**, no menu **Configurações  ›  Opções  ›  Atendimento**, seção **Distribuição e rodízio**.
>
> **A tela pede para ligar antes "Aguardando com dono: só ele vê?". Por quê?** As opções que deixam o atendimento no **Aguardando (MEUS)** dependem dela: sem ela, o atendimento aguardando com dono apareceria para todos. Escolha **Sim** em **Aguardando com dono: só ele vê?** e depois ligue a opção que você quer.
>
> **Coloquei o limite de atendimentos e a pessoa continua aceitando acima dele.** A opção **Bloquear aceitar acima do limite de atendimentos** está em **Não**: assim o limite só tira a pessoa do rodízio. Escolha **Sim** para barrar também o aceitar, a transferência e a conversa nova.
>
> **Quem está numa chamada continua recebendo atendimentos do rodízio?** Com **Sim** em **Tirar do rodízio quem está em chamada**, não: a pessoa volta a receber atendimentos do rodízio quando sai da chamada.
