# Equipe & Canais no Dashboard

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/equipe-canais-no-dashboard
- **Categoria:** Recursos
- **Menu:** Dashboard › Equipe & Canais no Dashboard

---

🧩 O painel **Equipe & Canais** junta três leituras: os **alertas** do que pede atenção agora, o **ranking** de quem atende e os números de cada **canal**. É o painel para saber onde agir primeiro.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Dashboard**.
>
> ➡️ Clique no card **Equipe & Canais**.
>
> ➡️ Escolha o período nos **Filtros Avançados** e clique em **Aplicar Filtros** — o ranking e os canais seguem o período; os alertas, não.

## Alertas Ativos

Os **Alertas Ativos** mostram a situação de **agora**: não mudam com as datas dos filtros, só com a conexão escolhida e com o recorte de **Setores**, **Atendentes** e **Tags** dos **Filtros Avançados**. Cada alerta traz o nível (**CRÍTICO** ou **ATENÇÃO**), o **Valor**, o **Limite** quando houver e uma sugestão do que fazer. No alto do quadro fica a contagem de alertas de cada nível.

Nos alertas **SLA Próximo do Vencimento**, **Atendentes Sobrecarregados**, **Tickets Sem Atendente** e **Clientes Sem Resposta**, a sugestão é um botão: ele abre a lista dos atendimentos que entraram na conta, com **Abrir conversa** e **Transferir** em cada linha.

As réguas dos alertas vêm de **Metas e limites**, no topo do Dashboard: o **Prazo do SLA**, o **Limite de atendente sobrecarregado** e o tempo de **Sem resposta há mais de (minutos)** que o administrador definiu. Sem nada definido, valem o prazo de 24 horas e o limite de 10. Quando um Setor tem meta própria, em **Metas por Setor**, os atendimentos dele contam pelo prazo do Setor.

🔘 **Conexões WhatsApp Offline** (**CRÍTICO**): quantas conexões da empresa estão desconectadas — por exemplo, uma conexão esperando a leitura do QR Code. Apesar do nome, o alerta não olha só o WhatsApp: uma conexão de outro canal fora do ar também entra na conta. O alerta aparece cerca de um minuto depois que a conexão cai e some cerca de um minuto depois que ela volta. Sugestão da tela: *Verificar conexões na página de Conexões*.

🔘 **SLA Próximo do Vencimento:** os atendimentos em atendimento ou aguardando que chegaram ao ponto em que falta 1/6 do prazo de atendimento da empresa, inclusive os que já passaram do prazo. Com o prazo de 24 horas, entram os abertos há mais de 20 horas, e o alerta mostra *Limite: 20 h*; com o prazo de 2 horas, os abertos há mais de 1 h 40 min (*Limite: 100 min*). Sugestão da tela: *Priorizar atendimento destes tickets*. Na lista que o botão abre, o mais antigo vem primeiro, com *Venceu há* ou *Vence em* em cada linha.

🔘 **Atendentes Sobrecarregados:** quantas pessoas estão com mais atendimentos em atendimento ao mesmo tempo do que o **Limite de atendente sobrecarregado** — 10, quando a empresa não definiu outro. Sugestão da tela: *Redistribuir tickets ou adicionar mais atendentes*. A lista que o botão abre agrupa os atendimentos por pessoa, com quantos cada uma tem abertos, e o título diz quantas pessoas e quantos atendimentos — por exemplo, *2 atendente(s) · 48 atendimento(s)*.

🔘 **Tickets Sem Atendente:** os atendimentos aguardando, ainda sem ninguém atendendo. Sugestão da tela: *Atribuir tickets aos atendentes disponíveis*.

🔘 **Clientes Sem Resposta** (**ATENÇÃO**): os atendimentos já aceitos em que a última mensagem é do cliente e ninguém respondeu há mais que o tempo de **Sem resposta há mais de (minutos)** — por exemplo, *7 atendimento(s) com a última mensagem do cliente sem resposta há mais de 30 min*, com *Limite: 30 min*. Sugestão da tela: o botão *Responder os clientes que estão esperando*, que abre a lista do que espera há mais tempo para o mais novo.

Sem nenhum alerta, o quadro mostra *Nenhum alerta ativo no momento*.

## Ranking de Agentes

O **Ranking de Agentes** lista toda a equipe da empresa, inclusive quem não atendeu no período, em ordem de quem mais resolveu. Clicar no título de uma coluna reordena o ranking por ela — **Agente** põe os nomes em ordem alfabética. Para o supervisor cujo cadastro restringe o acesso aos Setores dele, o ranking traz só as pessoas desses Setores. As colunas:

🔘 **Resolvidos:** os atendimentos que começaram no período, já encerrados, em que a pessoa era quem atendia. O atendimento encerrado sem ninguém atendendo não entra no ranking de ninguém.

🔘 **Tempo Médio:** o tempo médio que a pessoa levou para resolver, em horas e minutos. Sem atendimento resolvido, aparece um traço.

🔘 **1ª resposta:** o tempo de primeira resposta da pessoa no período.

🔘 **% no SLA:** a porcentagem dos atendimentos da pessoa dentro do prazo do SLA. Quem não tem atendimento no período mostra um traço.

🔘 **Avaliação:** a média das notas que os clientes deram à pessoa no período. Sem nota, mostra 0.0.

🔘 **Taxa:** a parte dos atendimentos da pessoa que ela resolveu, em porcentagem.

🔘 **Status:** se a pessoa está online agora.

## Estatísticas por Canal

Um card por conexão, com o nome, o tipo de canal e a situação (**Conectado**, por exemplo). Os números do card seguem o período:

🔘 **Recebidas** e **Enviadas:** as mensagens daquela conexão no período. **Enviadas** conta também as mensagens automáticas, como a posição na fila e a mensagem de conclusão.

🔘 **Criados** e **Resolvidos:** os atendimentos daquela conexão criados e resolvidos no período.

🔘 **Uptime** e **Última conexão:** quanto do tempo a conexão ficou disponível e quando ela se conectou pela última vez.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Os Alertas Ativos não mudam quando troco o período do Dashboard.** É assim: os alertas mostram a situação de agora. O ranking e os canais é que seguem o período. O recorte de **Setores**, **Atendentes** e **Tags**, esse sim, muda os alertas.
>
> **O que quer dizer o Limite que aparece nos alertas?** É a régua de cada alerta, e a unidade muda de um para outro. No **SLA Próximo do Vencimento**, é o tempo desde que o atendimento foi aberto a partir do qual ele entra na conta — *20 h* com o prazo de 24 horas. No **Atendentes Sobrecarregados**, é o número de atendimentos em atendimento ao mesmo tempo, por pessoa. No **Clientes Sem Resposta**, é o tempo sem resposta depois da última mensagem do cliente. As réguas vêm de **Metas e limites**.
>
> **Como vejo quais atendimentos estão no alerta SLA Próximo do Vencimento?** Clique em *Priorizar atendimento destes tickets*, no próprio alerta. A lista vem do atendimento mais antigo para o mais novo, com *Venceu há* ou *Vence em* em cada linha e os botões **Abrir conversa** e **Transferir**.
>
> **Como redistribuo os atendimentos de quem está no alerta Atendentes Sobrecarregados?** Clique em *Redistribuir tickets ou adicionar mais atendentes*. A lista agrupa os atendimentos por pessoa; em cada linha, **Transferir** passa o atendimento para outra pessoa ou outro Setor, e ele chega como **Aguardando** para quem recebe. A lista se atualiza na hora, com o aviso *Atendimento transferido.*
>
> **Apareceu o alerta Clientes Sem Resposta no Dashboard. O que eu faço?** Clique em *Responder os clientes que estão esperando*: a lista traz os atendimentos em que o cliente escreveu por último e ficou sem resposta, do que espera há mais tempo para o mais novo, com **Abrir conversa** e **Transferir**. O tempo que conta como sem resposta fica em **Metas e limites**, no campo **Sem resposta há mais de (minutos)**.
>
> **Como ordeno o Ranking de Agentes por outra coluna?** Clique no título da coluna — por exemplo, **1ª resposta** ou **% no SLA**.
>
> **Por que o ranking do Dashboard mostra pessoas que não atendem mais?** O **Ranking de Agentes** lista todos os usuários da empresa, inclusive os inativos, com zero onde não houve atendimento.
>
> **Por que a soma dos Resolvidos do Ranking de Agentes é menor que os Protocolos Resolvidos?** O ranking só dá o atendimento a quem estava atendendo. O atendimento encerrado ainda aguardando, sem ninguém ter aceitado, conta nos **Protocolos Resolvidos** e em nenhuma linha do ranking.
>
> **Encerrei hoje um atendimento antigo e meus Resolvidos de hoje não subiram.** O **Ranking de Agentes** conta o atendimento no período em que ele começou. Um atendimento da semana passada encerrado hoje entra nos **Resolvidos** da semana passada.
>
> **Por que Enviadas, nas Estatísticas por Canal, é maior que o número de respostas da equipe?** A contagem inclui as mensagens automáticas da conexão, como a posição na fila, a conclusão e a pergunta de avaliação.
>
> **Apareceu o alerta Conexões WhatsApp Offline no Dashboard.** Uma conexão da empresa está desconectada. Acesse o menu **Conexões** e reconecte a que estiver fora do ar; depois disso, o alerta leva cerca de um minuto para sumir.
>
> **A Avaliação de uma pessoa no ranking está em 0.0.** Nenhum cliente avaliou um atendimento dela no período escolhido.
