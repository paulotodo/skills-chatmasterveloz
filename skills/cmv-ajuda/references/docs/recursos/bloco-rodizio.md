# Rodízio

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-rodizio
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Rodízio

---

🧩 O bloco **Rodízio** distribui os clientes que chegam ao fluxo entre vários atendentes, e entrega cada atendimento direto a um deles. Diferente de um Setor comum, onde a conversa espera alguém pegar, o rodízio garante que cada lead já tenha um dono.

O rodízio pode ser montado no próprio bloco ou vir de um rodízio cadastrado no menu **Rodízios**, para ser usado em vários fluxos.

**🏷️ Categoria: Atendimento - Finalização - Roteador**

☑️ **Justiça:** divide os leads de forma igual ou proporcional entre a equipe.

☑️ **Estratégia:** dá pesos diferentes, como mais leads para o vendedor sênior.

☑️ **Segurança:** se ninguém estiver disponível, leva o cliente para um Setor de espera.

![FlowBuilder - Bloco Rodízio](https://clihelper.chatmasterveloz.com/docs-imagem/23524-bloco-rodizio-1.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Rodízio**.
>
> ➡️ Em **Distribuição**, escolha um rodízio cadastrado ou **Configurar neste bloco**.
>
> ➡️ Se for configurar no bloco, defina como distribuir, o Setor de transbordo e os participantes, e clique em **Adicionar**.

## Como configurar o bloco Rodízio

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Rodízio**

![FlowBuilder Formulário Bloco Rodízio](https://clihelper.chatmasterveloz.com/docs-imagem/23524-bloco-rodizio-formulario.jpg)

🔘 **Distribuição:** **Configurar neste bloco** ou um dos rodízios cadastrados no menu **Rodízios**. Com um rodízio cadastrado, o bloco não pede mais nada: os participantes, o ciclo e o transbordo vêm do cadastro, e o que mudar lá vale em todos os fluxos que o usam.

Configurando no bloco:

🔘 **Como distribuir:** **Equilibrado no ciclo (pelos percentuais)** ou **Rodada sorteada (um para cada antes de repetir)**.

🔘 **Ciclo de Rodízio:** só no modo equilibrado. Define quando a contagem recomeça:  
- **Por Hora Cheia:** a cada hora cheia.
- **Por Dia:** à meia-noite, ideal para operações diárias.
- **Por Semana:** no início da semana.
- **Por Mês:** no início do mês.
- **Integral (Total):** considera todo o histórico, sem zerar.

🔘 **Se não encontrar operador disponível (offline ou no limite de atendimentos), mover para:** o Setor que recebe o atendimento quando nenhum participante pode receber, no **Aguardando**. Ex.: um Setor *Orçamentos* ou *Espera*, para o cliente não ficar travado no fluxo.

🔘 **Dividir o transbordo entre mais filas:** aparece depois de escolhido o Setor de transbordo e divide o transbordo entre vários Setores, cada um com o seu **Percentual (%)**. Nas palavras da tela: *"Quando ninguém puder receber, o atendimento vai para uma destas filas, dividido pelos percentuais dentro do ciclo do rodízio. Com todos os percentuais em zero, divide igual."* O Setor escolhido acima é a **Fila principal**; os outros entram em **Fila de transbordo**, e **Adicionar fila** inclui mais um.

🔘 **Escolha os participantes:** escolha o atendente na lista **Operador** para incluí-lo. Cada participante tem:

◽ **Status:** **Online** recebe só quando está conectado; o rodízio pula quem está offline. **Indiferente** recebe mesmo offline.

◽ **Porcentagem:** a parte dos atendimentos que vai para ele, no modo equilibrado.

◽ **Setor:** o Setor em que o atendimento fica, ou **Manter o setor atual**.

◽ **Entregar em:** **Padrão da empresa**, **Atendendo** ou **Aguardando (MEUS)**.

🔲 Para finalizar, clique em **Adicionar**. Sem nenhum participante, a janela avisa *Adicione pelo menos um operador ao rodízio!*

🚨 No modo equilibrado, a soma das porcentagens de todos os participantes **precisa dar exatamente 100%**.

## Rodada sorteada

No modo **Rodada sorteada**, cada atendimento é sorteado entre os disponíveis que ainda não receberam naquela rodada. Quem fica online no meio entra na rodada e recebe um, sem receber vários seguidos. Quando todos os disponíveis receberam, começa outra rodada.

Neste modo não há ordem, nem percentual, nem ciclo.

## Onde o atendimento chega

A opção **Entregar em** de cada participante decide: **Atendendo**, **Aguardando (MEUS)** ou **Padrão da empresa**. O padrão da empresa é a opção **Rodízio do Flowbuilder deixa no Aguardando (MEUS)?**, nas configurações da empresa.

⚠️ **Aguardando (MEUS)** só vale com **Aguardando com dono: só ele vê?** ligada. Sem ela, o atendimento vai para **Atendendo**.

📌 O limite de atendimentos de cada pessoa conta também o que está no **Aguardando (MEUS)** dela.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O que acontece se o atendente estiver offline no Rodízio?** Com **Status Online**, o rodízio pula esse atendente e entrega ao próximo disponível. Se ninguém estiver disponível, o cliente vai para o Setor de **Se não encontrar operador disponível**.
>
> **Dá para dividir o transbordo do Rodízio entre vários Setores?** Sim. Depois de escolher o Setor de transbordo, clique em **Dividir o transbordo entre mais filas** e dê um **Percentual (%)** a cada Setor. Com todos os percentuais em zero, a divisão fica igual.
>
> **A distribuição do Rodízio é exata, um para um?** No modo equilibrado, a distribuição é por probabilidade. Num ciclo curto pode parecer desigual; ao longo do dia, as porcentagens tendem a se igualar. Para um para cada, use **Rodada sorteada**.
>
> **Qual a diferença entre configurar no bloco Rodízio e usar um rodízio cadastrado?** O configurado no bloco vale só ali. O cadastrado no menu **Rodízios** pode ser usado em vários fluxos, e uma mudança no cadastro vale em todos.

> **[ERROS]**
>
> #### Erros Comuns
>
> **A conta não fecha:** 12 atendentes com 8% cada somam 96%, e sobram 4% sem destino. **Solução:** ajuste os números para fechar 100% cravado, sem casas decimais, como 9% em alguns.
>
> **Sem Setor de transbordo:** a equipe sai para o almoço, todos ficam offline e o cliente trava no bloco. **Solução:** sempre escolha o Setor em **Se não encontrar operador disponível**.
