# Relatórios Detalhados do Dashboard

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/relatorios-detalhados-do-dashboard
- **Categoria:** Recursos
- **Menu:** Dashboard › Relatórios Detalhados do Dashboard

---

🧩 O painel **Relatórios Detalhados** é uma página só, em duas seções: o **Relatório por Operador**, com os números de uma pessoa, e, logo abaixo, o **Relatório por Período**, cada um com a exportação em PDF. Embaixo dos dois fica o botão que exporta os números do Dashboard para Excel. Os dois relatórios são calculados na hora em que abrem, sem a espera dos outros painéis, e seguem o período, a conexão e o recorte de **Setores**, **Atendentes** e **Tags** dos **Filtros Avançados**.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Dashboard**.
>
> ➡️ Clique no card **Relatórios Detalhados**.
>
> ➡️ Escolha o período nos **Filtros Avançados**, clique em **Aplicar Filtros** e vá até a seção do relatório.

## Relatório por Operador

Escolha a pessoa em **Selecionar Operador**. A lista traz todos os usuários da empresa — para o supervisor cujo cadastro restringe o acesso aos Setores dele, só as pessoas desses Setores — e abre em quem está usando a tela, marcado **(Você)**. O **Relatório de Atendimento** abre com o nome, o e-mail e o período, e com estes números:

🔘 **Conversas atendidas:** os atendimentos que a pessoa encerrou no período.

🔘 **Mensagens enviadas:** as mensagens que a pessoa escreveu no período.

🔘 **Tempo total de resolução:** a soma do tempo de cada atendimento, de quando a pessoa aceitou até encerrar.

🔘 **Tempo médio de espera:** quanto tempo, em média, o cliente esperou entre entrar na fila e a pessoa aceitar.

🔘 **Tempo Médio de Resolução:** nas palavras da tela, *Tempo médio para finalizar um protocolo*.

🔘 **Avaliação Média:** a média das notas que os clientes deram à pessoa, mostrada sobre **5.0**, com a quantidade de avaliações. Sem nota no período, aparece *Sem avaliações no período*.

🔘 **Distribuição por Horário:** em que horas do dia os atendimentos da pessoa aconteceram. Para o movimento da empresa inteira por dia da semana e hora, use o painel **Horários de pico**.

Com um Setor, um atendente ou uma tag escolhidos nos **Filtros Avançados**, o relatório conta só os atendimentos da pessoa dentro desse recorte.

O ícone **Atualizar**, no alto do relatório, busca os números de novo, com o aviso *Atualizando relatório...*. O ícone **Exportar PDF** baixa o relatório da pessoa em PDF, com o período no nome do arquivo. O PDF traz os números com os mesmos nomes da tela e o período em dia/mês/ano, como *09/11/2026 - 15/11/2026*.

## Relatório por Período

A seção **Relatório por Período**, logo abaixo do **Relatório por Operador**, usa as datas dos **Filtros Avançados** e tem o próprio agrupamento: **Por Dia**, **Por Semana** ou **Por Mês**. Por semana, cada período começa na segunda-feira.

🔘 **Tickets por Período:** em cada período, o total de atendimentos e quantos estão fechados, aguardando e em atendimento.

🔘 **Mensagens por Período:** as mensagens enviadas e as recebidas.

🔘 **Detalhes por Período:** um card por período, com os atendimentos (e quantos foram fechados), as mensagens (e quantas foram enviadas) e os **Top Operadores**, com quantos atendimentos cada um resolveu.

O primeiro e o último dia do período entram no relatório. O **Relatório por Período** conta os atendimentos como a **Linha do Tempo de Tickets**: os que começaram em cada período, e a soma dá o **Total de Tickets** de **Estatísticas e Informações**.

O ícone **Exportar PDF** da seção baixa o relatório do período em PDF, com as datas no nome do arquivo e cada período em dia/mês/ano, como *09/11/2026*.

## Exportar para Excel

O botão **Exportar para Excel**, embaixo das duas seções, baixa um arquivo com os números do período, da conexão e do recorte de **Setores**, **Atendentes** e **Tags** escolhidos nos filtros, com o aviso *Relatório exportado com sucesso!*. O nome do arquivo traz as datas do período, como `relatorio_dashboard_2026-11-05_2026-11-12.xlsx`.

O arquivo tem cinco abas: **Resumo**, **Ranking de Agentes**, **Estatísticas por Canal**, **Linha do Tempo de Tickets** e **Alertas Ativos**. Na aba **Estatísticas por Canal**, a coluna **Tipo** traz o nome do canal, como *WebChat* ou *Chat Externo*.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Relatório por Operador conta os atendimentos que a pessoa só aceitou?** Não. **Conversas atendidas** conta os atendimentos que a pessoa encerrou no período; o que ainda está aberto com ela entra quando for encerrado.
>
> **Por que o Tempo total de resolução de uma pessoa está tão alto?** Ele soma o tempo de cada atendimento, de quando a pessoa aceitou até encerrar. Um atendimento que ficou aberto por dias pesa muito nessa soma.
>
> **Onde fica o Relatório por Período nos Relatórios Detalhados?** Na mesma página do **Relatório por Operador**, logo abaixo dele: os **Relatórios Detalhados** não têm abas.
>
> **Qual a diferença entre o Relatório por Período e a Linha do Tempo?** Os dois contam os atendimentos do mesmo jeito: a soma do **Relatório por Período** dá o mesmo total da **Linha do Tempo de Tickets** e do **Total de Tickets**. A diferença está no que cada um mostra: o **Relatório por Período** tem agrupamento próprio, traz as mensagens e os **Top Operadores**, e é calculado na hora; a **Linha do Tempo** mostra os criados, resolvidos e pendentes de cada ponto do período e os contatos novos.
>
> **Por que o supervisor não vê a equipe inteira em Selecionar Operador?** Com **Restringir acesso apenas aos setores específicos** em **SIM** no cadastro do supervisor, a lista **Selecionar Operador** traz só as pessoas dos Setores dele.
>
> **Como baixo o relatório de uma pessoa em PDF?** Escolha a pessoa em **Selecionar Operador** e clique no ícone **Exportar PDF**, no alto do relatório. O arquivo vem com o período dos **Filtros Avançados**.
>
> **O Excel exportado do Dashboard respeita a conexão escolhida?** Respeita: o arquivo é gerado com o período e o recorte de **Setores**, **Atendentes** e **Tags** dos **Filtros Avançados** e com a conexão do **Filtrar por Conexão**.
>
> **Dá para exportar para Excel os números de um Setor só?** Dá. Escolha o Setor em **Setores**, nos **Filtros Avançados**, clique em **Aplicar Filtros** e depois em **Exportar para Excel**: o arquivo vem só com os atendimentos desse Setor.
