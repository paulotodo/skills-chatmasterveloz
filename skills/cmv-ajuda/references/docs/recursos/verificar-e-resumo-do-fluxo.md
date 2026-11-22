# Verificar e Resumo do Fluxo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/verificar-e-resumo-do-fluxo
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Editor de Fluxos › Verificar e Resumo do Fluxo

---

🧩 O robô que para de responder no meio da conversa quase sempre tem a mesma causa: um bloco ficou sem ligação, e o cliente chegou num ponto de onde o fluxo não tem para onde seguir. No editor do FlowBuilder Nativo, dois botões da barra procuram esse tipo de problema antes de o cliente encontrá-lo: **Verificar** e **Resumo do fluxo**.

O **Verificar** olha as **ligações** entre os blocos. O **Resumo do fluxo** olha a **estrutura** do fluxo inteiro. Um não substitui o outro.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no ícone de ferramenta.
>
> ➡️ Clique em **Verificar** e corrija cada bloco que ele listar.
>
> ➡️ Abra o **Resumo do fluxo** e confira os avisos.
>
> ➡️ Clique em **SALVAR FLUXO**.

## O que o Verificar mostra

O painel do **Verificar** traz a contagem de **blocos**, **conexões**, blocos **alcançáveis** a partir do Início e blocos **isolados**. Com tudo ligado, ele mostra **Todos conectados!** e a frase *Todos os blocos estão corretamente conectados ao fluxo!*

Quando encontra problema, o título muda para a quantidade de **Bloco(s) Desconectado(s)** e ele lista cada caso:

◽ **Não alcançável a partir do Início:** blocos que nenhum caminho do fluxo alcança.

◽ **Sem conexão de entrada:** blocos que não recebem nenhuma ligação.

◽ **Sem conexão de saída (o fluxo para neste bloco):** os pontos onde a conversa termina sem que isso tenha sido planejado.

◽ **"Pular para" sem destino:** blocos **Pular para** que ficaram sem bloco de destino.

◽ **Ciclos sem espera:** caminhos que voltam a um bloco sem esperar a resposta do contato.

Cada item mostra o tipo do bloco e o começo do conteúdo dele, para você reconhecer qual é. No desenho, o bloco com problema fica contornado de vermelho, o botão **Verificar** ganha um selo com a quantidade e o topo do editor avisa quantos blocos não são alcançáveis a partir do Início. Clique num item da lista do Verificar para ir até o bloco.

📌 Bloco alcançado por um **Pular para** conta como alcançável, mesmo sem uma linha chegando até ele.

## O que o Resumo do fluxo mostra

O **Resumo do fluxo** é o botão com o ícone de informação, na barra do editor. Ele mostra quantos **blocos** e **conexões** o fluxo tem, quantos blocos há de cada tipo e os **avisos** de estrutura, como:

◽ **Nenhum bloco de Encerramento encontrado**

◽ **Múltiplos blocos de Início detectados**

⚠️ **O Verificar olha as ligações, não a estrutura.** Um fluxo sem bloco de encerramento pode passar no Verificar sem nenhum problema. Esse aviso só aparece no **Resumo do fluxo**. Antes de pôr um fluxo novo para atender, confira os dois.

## O que acontece ao salvar

O editor salva mesmo com blocos soltos. Junto da confirmação, ele avisa quantos blocos não são alcançáveis, como *2 bloco(s) não alcançável(is) a partir do início*. O aviso não impede o salvamento: a correção é sua.

O que impede salvar é um **Pular para** sem destino válido. O editor avisa quantos são e marca os blocos para você corrigir:

*Não foi possível salvar: N "Pular para" sem destino válido. Corrija os blocos marcados antes de salvar.*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O robô parou de responder no meio do fluxo. Onde olho primeiro?** No **Verificar**, na lista **Sem conexão de saída (o fluxo para neste bloco)**. É ali que aparece o bloco que o cliente alcançou e de onde a conversa não tem para onde seguir.
>
> **Salvei o fluxo com um bloco solto e não deu erro. Está tudo certo?** Não necessariamente. O editor salva e só avisa quantos blocos não são alcançáveis. Abra o **Verificar** para ver quais são e ligue cada um, ou exclua o que sobrou.
>
> **O que é um ciclo sem espera no Verificar?** É um caminho que volta a um bloco por onde a conversa já passou sem nenhum bloco no meio que espere a resposta do contato. Na execução, o fluxo é interrompido ao voltar ao mesmo bloco. Para repetir uma etapa, coloque no caminho de volta um bloco que espere o cliente, como uma pergunta ou um menu.
>
> **O Verificar mostrou Todos conectados!. O fluxo está pronto?** As ligações estão completas, mas confira também o **Resumo do fluxo**: é nele que aparece, por exemplo, o aviso de que o fluxo não tem bloco de encerramento.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Confiar só no Verificar:** o fluxo passa no Verificar e mesmo assim não tem um ponto de encerramento. **Solução:** abra o **Resumo do fluxo** e resolva os avisos antes de salvar.
>
> **Ignorar o aviso ao salvar:** o fluxo é salvo com blocos que nenhum caminho alcança, e o cliente nunca chega a eles. **Solução:** depois de cada salvamento com aviso, abra o **Verificar** e resolva a lista **Não alcançável a partir do Início**.
