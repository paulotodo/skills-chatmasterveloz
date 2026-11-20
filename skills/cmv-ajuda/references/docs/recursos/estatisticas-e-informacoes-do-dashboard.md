# Estatísticas e Informações do Dashboard

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/estatisticas-e-informacoes-do-dashboard
- **Categoria:** Recursos
- **Menu:** Dashboard › Estatísticas e Informações do Dashboard

---

🧩 O painel **Estatísticas e Informações** resume o período escolhido em nove indicadores: quanto a equipe resolveu, em quanto tempo, como os clientes avaliaram e quantos atendimentos e contatos houve. Cada card traz o número, a unidade e uma linha que diz o que ele conta.

Os indicadores seguem o período, a conexão e o recorte de **Setores**, **Atendentes** e **Tags** dos **Filtros Avançados**. O **Total de Contatos** é a exceção: segue só a conexão.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Dashboard**.
>
> ➡️ Clique no card **Estatísticas e Informações**.
>
> ➡️ Escolha o período nos **Filtros Avançados** e clique em **Aplicar Filtros**.

## Os indicadores do período

🔘 **Taxa de Resolução** (%): a parte dos atendimentos do período que foi resolvida — o número de **Protocolos Resolvidos** dividido pelo **Total de Tickets**.

🔘 **Tempo Médio de Resposta** (minutos): quanto tempo, em média, a equipe levou para responder pela primeira vez. Nas palavras da tela: *Tempo médio até a primeira resposta do agente*.

🔘 **NPS Score** (de -100 a 100): a satisfação dos clientes, calculada com as avaliações respondidas no período. As notas **4** e **5** contam a favor, a nota **3** é neutra e as notas **1** e **2** contam contra. O **NPS Score** é a porcentagem de avaliações a favor menos a porcentagem das que contam contra: com uma nota 5 e uma nota 1, fica em 0; só com notas 1 e 2, vai a -100. Sem nenhuma avaliação no período, mostra 0.

🔘 **Conformidade SLA** (%): a parte dos atendimentos resolvidos dentro do prazo de atendimento da empresa, que a linha do card mostra — por exemplo, *Resolvidos em até 24 horas*. O prazo é o **Prazo do SLA** de **Metas e limites**, no topo do Dashboard; sem prazo definido, vale 24 horas. Quando o Setor do atendimento tem meta própria, em **Metas por Setor**, o atendimento é medido pelo prazo do Setor. Com **Contar só o horário de expediente da empresa** ligado, só o tempo dentro do expediente conta.

🔘 **Total de Tickets:** nas palavras da tela, *Protocolos iniciados no período* — os atendimentos que começaram no período, inclusive o atendimento antigo que ganhou um novo protocolo dentro dele, somando os resolvidos, os que estão aguardando e os que estão em atendimento.

🔘 **Protocolos Resolvidos:** nas palavras da tela, *Dos iniciados no período, os já encerrados* — encerrados até hoje, e não só dentro do período.

🔘 **Tempo de Resolução** (horas): o tempo médio entre alguém aceitar o atendimento e encerrá-lo, com uma casa decimal.

🔘 **Primeira Resposta** (minutos): o tempo médio até a primeira resposta, em minutos inteiros.

➡️ Com uma **Meta de primeira resposta** definida em **Metas e limites**, os cards **Tempo Médio de Resposta** e **Primeira Resposta** ganham cor: verde até a meta, amarelo até o dobro dela e vermelho acima disso.

🔘 **Total de Contatos:** todos os contatos da empresa — o mesmo total da tela **Contatos**. O **Total de Contatos** não muda com o período; com uma conexão escolhida no **Filtrar por Conexão**, conta só os contatos dela.

## Os atendimentos por trás do número

Os cards **Total de Tickets** e **Protocolos Resolvidos** abrem, com um clique, a lista dos atendimentos que entram na conta: o contato, o atendente, o Setor e a duração de cada um, com o botão **Abrir conversa**. A lista vem com o mesmo período, a mesma conexão e o mesmo recorte da tela, cem atendimentos por página. Os outros indicadores não abrem lista.

## A tendência "vs período anterior"

Com **Comparar com período anterior** ligado nos **Filtros Avançados**, os quatro primeiros cards — **Taxa de Resolução**, **Tempo Médio de Resposta**, **NPS Score** e **Conformidade SLA** — mostram a diferença entre o número do período e o do período de comparação, na unidade do card: **p.p.** (pontos percentuais) na **Taxa de Resolução** e na **Conformidade SLA**, **min** no **Tempo Médio de Resposta** e **pts** no **NPS Score** — por exemplo, *-339.8 min vs período anterior*.

O período de comparação é o anterior, de mesma duração, ou o que você escolher no bloco **Período de Comparação** dos **Filtros Avançados**.

A linha da tendência só aparece quando há o que comparar. Com a comparação desligada, nenhum card mostra a tendência; com um período de comparação sem atendimentos, também não. O **NPS Score** fica sem a linha quando o período de comparação não tem avaliação, mesmo com os outros três cards mostrando a deles.

A linha da tendência também diz se o número melhorou: fica verde quando melhorou e vermelha quando piorou, e no tempo cair é melhorar. Sem diferença, fica neutra.

## Quando os indicadores mudam

Os indicadores de **Estatísticas e Informações** são calculados quando o painel abre, quando os filtros são aplicados, quando a conexão muda e no **Atualizar**. Um atendimento que acabou de chegar ou de ser encerrado pode levar de alguns segundos a cerca de um minuto para entrar na conta.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A soma dos Criados da Linha do Tempo bate com o Total de Tickets?** Bate: a **Linha do Tempo** conta os atendimentos do mesmo jeito que o **Total de Tickets** — os que começaram no período, inclusive o atendimento antigo que ganhou um novo protocolo —, e a soma dos **Criados** do período dá o **Total de Tickets**.
>
> **Qual a diferença entre Protocolos Resolvidos e o card Fechados?** O card **Fechados**, no topo do Dashboard, conta todos os atendimentos encerrados da empresa, desde sempre. **Protocolos Resolvidos** conta só os do período escolhido nos filtros.
>
> **Por que os Protocolos Resolvidos de um período passado aumentaram?** O card conta os atendimentos que começaram no período e já estão encerrados. Quando alguém encerra hoje um atendimento que começou na semana passada, ele passa a contar nos **Protocolos Resolvidos** da semana passada, e a **Taxa de Resolução** dela sobe junto.
>
> **O NPS Score ficou negativo com uma avaliação só.** Com uma única avaliação de nota 1 ou 2, o **NPS Score** vai a -100. Ele se equilibra conforme chegam as outras avaliações do período.
>
> **Por que uma nota 3 baixou o NPS Score?** A nota 3 é neutra: não conta a favor nem contra, mas entra no total de avaliações. Por isso o **NPS Score** cai quando ela chega — com três notas a favor e uma nota 3, fica em 75.
>
> **O Total de Contatos não muda quando troco o período.** O **Total de Contatos** conta todos os contatos da empresa. Os contatos novos ficam no painel **Linha do Tempo**, no gráfico **Novos Contatos**.
>
> **O Tempo de Resolução mostra 0.0 h.** O card mostra o tempo em horas, com uma casa decimal: médias de poucos minutos aparecem como 0.0.
>
> **Os cards de Estatísticas e Informações não mostram a tendência.** A comparação está desligada, ou o período de comparação não tem o que comparar: sem atendimentos, nenhum card mostra a linha. Para comparar, ligue **Comparar com período anterior** nos **Filtros Avançados** e clique em **Aplicar Filtros**.
>
> **A Conformidade SLA do Dashboard mudou sem eu mexer no período.** Alguém mudou as metas em **Metas e limites**: o **Prazo do SLA** da empresa — e a linha do card mostra o novo, *Resolvidos em até 2 horas*, por exemplo —, o prazo de um Setor em **Metas por Setor** ou a opção **Contar só o horário de expediente da empresa**. A **Conformidade SLA** passa a contar pela regra nova.
>
> **Como vejo quais atendimentos entraram no Total de Tickets do Dashboard?** Clique no card **Total de Tickets**: abre a lista dos atendimentos que começaram no período, com o botão **Abrir conversa** em cada um. O card **Protocolos Resolvidos** abre, do mesmo jeito, só os já encerrados.
>
> **Por que o NPS Score não mostra a tendência e os outros cards mostram?** O período de comparação não tem nenhuma avaliação: sem ela, não há NPS para comparar, e o **NPS Score** fica sem a linha.
