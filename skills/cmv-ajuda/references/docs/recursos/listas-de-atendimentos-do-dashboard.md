# Listas de atendimentos do Dashboard

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/listas-de-atendimentos-do-dashboard
- **Categoria:** Recursos
- **Menu:** Dashboard › Listas de atendimentos do Dashboard

---

🧩 Os números do **Dashboard** dizem quantos; as listas dizem **quais**. Clicar num número abre uma janela com os atendimentos que ele contou — o contato, quem atende, o Setor e há quanto tempo — e dali dá para abrir a conversa, transferir um ou vários atendimentos de uma vez e exportar a lista para Excel, sem sair do painel.

É também o caminho para a dúvida mais comum de quem lê o painel, *"esse número não bate com o que eu vejo"*: a lista mostra, um por um, os atendimentos por trás do número.

Ideal para:

☑️ **Prioridade do dia:** a lista do alerta de SLA põe no topo o atendimento que espera há mais tempo.

☑️ **Redistribuição:** a lista de Atendentes Sobrecarregados mostra quem está carregado e permite transferir dali mesmo.

☑️ **Conferência dos números:** o gestor vê, atendimento por atendimento, o que entrou em **Total de Tickets** ou em **Protocolos Resolvidos**.

☑️ **Começo do dia cheio:** os atendimentos marcados vão de uma vez para outro Setor ou, em partes iguais, para quem está online.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Dashboard**.
>
> ➡️ Clique num número que abre lista — por exemplo, o card **Aguardando**, no topo.
>
> ➡️ Na janela, use **Abrir conversa** ou **Transferir** em cada linha, e **Fechar** para voltar ao painel.
>
> ➡️ Para agir em vários de uma vez, marque as caixas das linhas e use **Transferir marcados** ou **Distribuir entre os online**. Para levar a lista a uma planilha, clique em **Exportar para Excel**.

## Os números que abrem lista

🔘 **Atendendo**, **Aguardando** e **Fechados:** os três cards do topo, do status em tempo real.

🔘 **Total de Tickets** e **Protocolos Resolvidos:** os dois cards de **Estatísticas e Informações**.

🔘 **Os botões dos alertas:** em **Equipe & Canais**, o botão de cada alerta abre a lista daquele alerta — *Priorizar atendimento destes tickets* no **SLA Próximo do Vencimento**, *Redistribuir tickets ou adicionar mais atendentes* no **Atendentes Sobrecarregados** e *Atribuir tickets aos atendentes disponíveis* no **Tickets Sem Atendente** e *Responder os clientes que estão esperando* no **Clientes Sem Resposta**.

🔘 **Desistiram antes da resposta** e **Reabertos:** os dois números do painel **Abandono e reabertura**.

Os outros indicadores de **Estatísticas e Informações** — como **Taxa de Resolução**, **Conformidade SLA**, **Primeira Resposta** e **Total de Contatos** — não abrem lista: o clique não faz nada.

## A janela da lista

No alto da janela ficam o nome do número e quantos atendimentos ele tem. Cada linha é um atendimento, com quatro colunas:

🔘 **Contato:** o nome e o número (ou a identificação) do contato.

🔘 **Atendente:** quem está com o atendimento, ou **Sem atendente**.

🔘 **Setor:** o Setor do atendimento.

🔘 **Há quanto tempo:** há quanto tempo o atendimento está aberto. Nas listas de **Total de Tickets** e **Protocolos Resolvidos**, a coluna se chama **Duração** e mostra quanto o atendimento durou.

A janela mostra 100 atendimentos por vez. Os botões **Anterior** e **Próxima**, no rodapé, passam de uma página para a outra.

A lista traz os mesmos atendimentos que o número contou, com os mesmos filtros da tela: a conexão escolhida em **Filtrar por Conexão** e os **Setores**, **Atendentes** e **Tags** escolhidos em **Filtros Avançados**. Nas listas de **Total de Tickets** e **Protocolos Resolvidos**, vale também o período.

### A lista do SLA Próximo do Vencimento

A lista do alerta **SLA Próximo do Vencimento** traz os atendimentos em atendimento ou aguardando que já passaram do ponto de aviso, do mais antigo para o mais novo. A frase do alto diz qual é esse ponto e qual é o prazo — por exemplo, *Em atendimento ou aguardando há mais de 20 h (o SLA é de 1 d), do mais antigo para o mais novo.*

Embaixo do tempo de cada linha, **Venceu há** mostra quanto o atendimento já passou do prazo, e **Vence em**, quanto falta para vencer.

O prazo e o ponto de aviso vêm de **Metas e limites**, no topo do Dashboard: o aviso chega quando falta 1/6 do prazo. Quando o Setor do atendimento tem meta própria, em **Metas por Setor**, o **Venceu há** e o **Vence em** contam pelo prazo do Setor.

### A lista de Atendentes Sobrecarregados

A lista do alerta **Atendentes Sobrecarregados** é separada por pessoa: cada atendente acima do limite aparece com quantos atendimentos abertos tem — no formato *Nome da pessoa: 28 abertos* — e, embaixo, os atendimentos dela. A frase do alto diz o limite, por exemplo *Atendentes com mais de 10 atendimentos abertos, e os atendimentos de cada um.*, e o título diz quantas pessoas e quantos atendimentos a lista tem — por exemplo, *2 atendente(s) · 48 atendimento(s)*.

### A lista de Clientes Sem Resposta

A lista do alerta **Clientes Sem Resposta** traz os atendimentos já aceitos em que o cliente escreveu por último e ninguém respondeu além do tempo de **Sem resposta há mais de (minutos)**, em **Metas e limites**. A frase do alto diz esse tempo e a ordem — por exemplo, *Atendendo, com a última mensagem do cliente sem resposta há mais de 30 min; do que espera há mais tempo para o mais novo.*

### As listas de Abandono e reabertura

No painel **Abandono e reabertura**, **Desistiram antes da resposta** e **Reabertos** abrem a lista dos atendimentos que cada número contou, com **Contato**, **Atendente**, **Setor** e **Há quanto tempo**. São listas de atendimentos já encerrados: têm só **Abrir conversa** e **Exportar para Excel**.

## Abrir a conversa e transferir

🔘 **Abrir conversa:** leva ao atendimento na mesma aba do navegador e fecha a lista. Para voltar ao painel, use o menu **Dashboard**.

🔘 **Transferir:** abre a janela **Transferir Ticket**, com a busca de usuário (*Digite para buscar usuários*) e o campo **Transferir para setor**. Escolha a pessoa e o Setor e clique em **Transferir**. O atendimento vai para a pessoa escolhida como **Aguardando**, a tela mostra o aviso *Atendimento transferido.* e a lista se atualiza na hora.

O botão **Transferir** aparece nas listas de atendimentos que ainda estão abertos — **Atendendo**, **Aguardando** e as listas dos alertas. As listas de **Fechados**, **Total de Tickets**, **Protocolos Resolvidos**, **Desistiram antes da resposta** e **Reabertos** têm só **Abrir conversa**.

⚠️ Abrir uma lista não muda nada. Já o **Transferir** da lista muda o atendimento de verdade, como a transferência feita dentro da conversa.

## Marcar vários e agir de uma vez

Nas listas de atendimentos que ainda estão abertos — **Atendendo**, **Aguardando** e as listas dos alertas — cada linha tem uma caixa de marcar, e o cabeçalho tem a caixa que marca a página inteira. Com atendimentos marcados, a lista mostra *N marcado(s)* e dois botões.

🔘 **Transferir marcados:** abre a janela *Transferir N atendimento(s)*, com **Setor** e **Atendente**. Basta o Setor para confirmar. Nas palavras da tela: *"Sem atendente: vão para o Aguardando do Setor."* Ao confirmar, a tela mostra *N atendimento(s) transferido(s).*

🔘 **Distribuir entre os online:** abre a janela *Distribuir N atendimento(s)*, só com o **Setor**. Nas palavras da tela: *"Os atendimentos marcados vão, em partes iguais, para as pessoas online do Setor escolhido."* Cada atendimento fica como **Aguardando** com a pessoa que o recebeu. Se ninguém do Setor estiver online, a janela avisa *Ninguém online neste Setor agora.* e nada muda.

⚠️ Os dois botões mudam todos os atendimentos marcados de uma vez, cada um como uma transferência feita dentro da conversa.

## Exportar para Excel

Toda lista tem o botão **Exportar para Excel**, no alto — também as de atendimentos encerrados. O arquivo traz todos os atendimentos da lista, inclusive os que não cabem na página de 100. Na lista **Aguardando**, por exemplo, ele vem com as colunas *Atendimento, Contato, Número, Setor, Atendente, Status, Criado em* e *Há quanto tempo (min)*.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O número do Dashboard não bate com o que eu vejo nos Chats. Como confiro?** Clique no número: a janela lista, um por um, os atendimentos que ele contou, com o contato, o atendente e o Setor. Confira também os filtros da tela — a conexão de **Filtrar por Conexão** e os Setores, atendentes e tags de **Filtros Avançados** valem para o número e para a lista.
>
> **Cliquei na Taxa de Resolução do Dashboard e nada aconteceu.** É o esperado: só abrem lista os três cards do topo, **Total de Tickets**, **Protocolos Resolvidos**, os botões dos alertas de **Equipe & Canais** e os dois números de **Abandono e reabertura**.
>
> **Quero ver primeiro o atendimento que espera há mais tempo. Onde fica no Dashboard?** Abra a lista do alerta **SLA Próximo do Vencimento**, em **Equipe & Canais**: ela vem do mais antigo para o mais novo, com **Venceu há** em quem já passou do prazo.
>
> **Transferi um atendimento pela lista do Dashboard. Para onde ele vai?** Para a pessoa e o Setor escolhidos na janela **Transferir Ticket**, como **Aguardando** com essa pessoa. A lista se atualiza logo depois.
>
> **Posso transferir vários atendimentos de uma vez pela lista do Dashboard?** Sim. Nas listas de atendimentos abertos, marque as caixas das linhas — ou a do cabeçalho, para a página inteira — e clique em **Transferir marcados**, para um Setor ou uma pessoa, ou em **Distribuir entre os online**, para dividir entre quem está online no Setor.
>
> **O Distribuir entre os online do Dashboard não mudou nada.** Ninguém do Setor escolhido estava online: a janela avisa *Ninguém online neste Setor agora.* Escolha outro Setor ou use **Transferir marcados**, que manda para o Aguardando do Setor.
>
> **Como levo a lista do Dashboard para uma planilha?** Clique em **Exportar para Excel**, no alto da lista. O arquivo traz todos os atendimentos da lista, também os que não cabem na página de 100.
>
> **Por que a lista de Fechados do Dashboard não tem o botão Transferir?** Atendimento encerrado não se transfere: as listas de **Fechados**, **Total de Tickets** e **Protocolos Resolvidos** têm só **Abrir conversa**.
>
> **A lista do Dashboard mostra só 100 atendimentos?** Mostra 100 por vez. Use **Próxima** e **Anterior**, no rodapé da janela, para ver os outros. O **Exportar para Excel** leva a lista inteira.
>
> **Abri uma conversa pela lista do Dashboard. Como volto?** **Abrir conversa** usa a mesma aba e fecha a lista. Volte pelo menu **Dashboard**.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Lista com menos atendimentos do que o esperado:** um filtro está ligado — uma conexão em **Filtrar por Conexão** ou Setores, atendentes e tags em **Filtros Avançados**. **Solução:** confira os filtros no alto do Dashboard; para voltar à empresa inteira, escolha **Todas as Conexões** e clique em **Limpar** nos **Filtros Avançados**.
