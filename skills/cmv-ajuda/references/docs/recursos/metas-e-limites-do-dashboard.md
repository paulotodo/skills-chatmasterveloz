# Metas e limites do Dashboard

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/metas-e-limites-do-dashboard
- **Categoria:** Recursos
- **Menu:** Dashboard › Metas e limites do Dashboard

---

🧩 Cada empresa tem o seu ritmo: uma clínica quer responder em minutos, uma indústria aceita um dia. As **Metas e limites** do Dashboard dizem ao painel qual é o ritmo da sua empresa — o prazo para resolver um atendimento, a meta de primeira resposta, quantos atendimentos abertos uma pessoa pode ter e quanto tempo um cliente pode ficar sem resposta antes de virar alerta. O prazo e a meta de primeira resposta podem ser diferentes em cada Setor.

Com as metas salvas, os alertas, a **Conformidade SLA** e as cores dos indicadores de tempo passam a usar os valores da empresa. Nas palavras da tela: *"Sem nada configurado, o SLA é de 24 horas e o limite de atendente sobrecarregado é 10."*

Ideal para:

☑️ **Prazo do negócio:** o alerta de SLA avisa com a antecedência que faz sentido para o tipo de atendimento da empresa.

☑️ **Meta da equipe:** o tempo de primeira resposta muda de cor conforme a meta, e o gestor vê de longe se a equipe está dentro dela.

☑️ **Carga por pessoa:** o alerta de sobrecarga dispara no limite que a empresa considera demais.

☑️ **Cliente esperando:** o alerta de clientes sem resposta mostra quem escreveu e ficou sem retorno além do tempo combinado.

☑️ **Setores com ritmos diferentes:** cada Setor pode ter o seu prazo e a sua meta de primeira resposta, e o painel mede cada atendimento pela meta do Setor dele.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Dashboard**.
>
> ➡️ Clique no botão **Metas e limites**, no topo da tela.
>
> ➡️ Preencha os campos e clique em **Salvar**.

## Os campos da janela Metas e limites

A janela se chama **Metas e limites do Dashboard**. Os campos de cima valem para a empresa inteira; embaixo, o bloco **Metas por Setor** troca o prazo e a meta de primeira resposta de cada Setor.

🔘 **Prazo do SLA:** o tempo que a empresa se dá para resolver um atendimento, em **minutos** ou **horas**, escolhidos no campo **Unidade**. Vai de 5 minutos a 30 dias. A ajuda da tela explica quando o alerta aparece: *"O alerta de SLA avisa quando falta 1/6 do prazo (com 24 horas, aos 20 horas)."*

🔘 **Meta de primeira resposta (minutos):** quanto tempo, no máximo, o cliente deve esperar pela primeira resposta. Vai de 1 a 1440 minutos. Vazio, não há meta.

🔘 **Limite de atendente sobrecarregado:** quantos atendimentos abertos uma pessoa pode ter ao mesmo tempo. Acima disso, o alerta **Atendentes Sobrecarregados** avisa. Vai de 1 a 500.

🔘 **Sem resposta há mais de (minutos):** quanto tempo o cliente pode esperar depois de escrever, num atendimento já aceito. Nas palavras da tela: *"O atendimento aceito com a última mensagem do cliente sem resposta há mais disso entra no alerta Clientes Sem Resposta."* Vai de 1 a 1440 minutos.

🔘 **Contar só o horário de expediente da empresa:** nas palavras da tela, *"O SLA e o alerta contam só o tempo dentro do expediente: o do Setor do atendimento (com o Gerenciamento de Expediente Por Setor) ou o horário padrão do Expediente dos usuários. O atendimento que chega na sexta à noite não entra no alerta no sábado."* Ligada, o tempo fora do expediente deixa de contar: um atendimento aberto há semanas passa a somar só as horas de expediente desse período.

Sem nenhum expediente cadastrado, a caixa **Contar só o horário de expediente da empresa** fica desativada, com o aviso *"Nenhum expediente cadastrado: preencha o horário dos Setores (Gerenciamento de Expediente Por Setor) ou o horário padrão em Expediente dos usuários para usar esta opção."* Os dois ficam no menu **Configurações  ›  Opções  ›  Geral**, seção **Gerenciamento de Expediente**.

⚠️ O horário padrão do **Expediente dos usuários** não serve só ao Dashboard: com ele ligado, o atendente só entra no painel dentro do horário.

Com um valor fora desses limites, o erro aparece em vermelho embaixo do campo e o botão **Salvar** fica desativado até a correção.

Ao salvar, a tela mostra *Metas salvas. O painel já usa os valores novos.* Ao abrir a janela de novo, os valores salvos continuam lá.

## Metas por Setor

No fim da janela **Metas e limites**, o bloco **Metas por Setor** tem uma linha para cada Setor da empresa. Nas palavras da tela: *"Vazio: vale a meta da empresa. O expediente de cada Setor é o horário do Setor (Gerenciamento de Expediente Por Setor)."*

🔘 **SLA (minutos):** o prazo para resolver os atendimentos daquele Setor. Vai de 5 a 43200 minutos (30 dias).

🔘 **1ª resposta (minutos):** a meta de primeira resposta dos atendimentos daquele Setor. Vai de 1 a 1440 minutos.

Com um valor fora dos limites, a janela avisa *"Confira as metas dos Setores: SLA de 5 a 43200 minutos; 1ª resposta de 1 a 1440."* e o **Salvar** fica desativado.

Com a meta do Setor salva, os atendimentos daquele Setor passam a contar pelo prazo dele: o alerta **SLA Próximo do Vencimento**, a lista dele e a **Conformidade SLA** — a do Setor e a da empresa — medem cada atendimento pela meta do Setor em que ele está. O **Limite** escrito no alerta continua mostrando o prazo da empresa.

## O que as metas mudam no Dashboard

➡️ **Alerta SLA Próximo do Vencimento:** conta os atendimentos em atendimento ou aguardando quando falta 1/6 do **Prazo do SLA**. Com o prazo de 24 horas, o aviso vem às 20 horas; com 2 horas, a 1 hora e 40 minutos, e o alerta mostra *Limite: 100 min*.

➡️ **Alerta Atendentes Sobrecarregados:** conta as pessoas com mais atendimentos abertos que o **Limite de atendente sobrecarregado**, e o **Limite** do alerta mostra esse número.

➡️ **Alerta Clientes Sem Resposta:** conta os atendimentos aceitos em que a última mensagem é do cliente há mais que o tempo do campo **Sem resposta há mais de (minutos)**, e o **Limite** do alerta mostra esse tempo — por exemplo, *Limite: 30 min*.

➡️ **Conformidade SLA:** mede os atendimentos resolvidos dentro do **Prazo do SLA**, e a descrição do card diz qual é o prazo — por exemplo, *Resolvidos em até 2 horas*.

➡️ **Primeira Resposta** e **Tempo Médio de Resposta:** com a **Meta de primeira resposta** preenchida, o número fica verde até a meta, amarelo até o dobro dela e vermelho acima disso. Sem meta, o card fica com a cor de sempre.

➡️ **Listas dos alertas:** a lista do **SLA Próximo do Vencimento** usa o mesmo prazo — ou o do Setor do atendimento, quando ele tem meta própria — e mostra, em cada atendimento, **Venceu há** ou **Vence em**.

Os mesmos valores aparecem no **Meus números** dos atendentes, quando a empresa libera essa página: a meta de primeira resposta e o prazo do SLA.

## Quem altera as Metas e limites

Só o administrador altera as metas. O supervisor abre a janela **Metas e limites** para consultar os valores, com os campos travados, o aviso *Só o administrador altera as metas.* e só o botão **Fechar**.

As metas valem para todos: quem abre o Dashboard vê os alertas e as cores com os mesmos valores, os da empresa e os de cada Setor.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Por que o alerta de SLA do Dashboard aparece antes de o prazo vencer?** O alerta avisa quando falta 1/6 do **Prazo do SLA**: com 24 horas, aos 20 horas. Ele avisa que o prazo está perto, não que já venceu.
>
> **Configurei o Prazo do SLA em 2 horas. Por que o alerta mostra Limite: 100 min?** O alerta dispara quando falta 1/6 do prazo. Um sexto de 2 horas são 20 minutos, então o aviso vem aos 100 minutos.
>
> **Nunca mexi em Metas e limites. Que valores o Dashboard usa?** Nas palavras da janela: *"Sem nada configurado, o SLA é de 24 horas e o limite de atendente sobrecarregado é 10."* Sem **Meta de primeira resposta**, os cards de tempo ficam sem as cores da meta.
>
> **O supervisor consegue mudar as Metas e limites do Dashboard?** Não. Ele vê os valores, com os campos travados e o aviso *Só o administrador altera as metas.*
>
> **Posso colocar o Prazo do SLA do Dashboard em dias?** A **Unidade** oferece **minutos** e **horas**. Para dias, use horas: 2 dias são 48 horas. O prazo pode chegar a 30 dias.
>
> **Posso ter um prazo de SLA diferente para cada Setor no Dashboard?** Sim. No fim da janela **Metas e limites**, o bloco **Metas por Setor** tem **SLA (minutos)** e **1ª resposta (minutos)** para cada Setor. O Setor com o campo vazio usa a meta da empresa.
>
> **A caixa Contar só o horário de expediente da empresa está desativada.** A empresa ainda não tem expediente cadastrado. Preencha o horário dos Setores, com o **Gerenciamento Por Setor**, ou o horário padrão do **Expediente dos usuários**, no menu **Configurações  ›  Opções  ›  Geral**, e a caixa se habilita.
>
> **O botão Salvar das Metas e limites está desativado.** Algum campo está fora do limite e mostra o erro embaixo: o prazo vai de 5 minutos a 30 dias, a primeira resposta de 1 a 1440 minutos, o limite de sobrecarga de 1 a 500 e o tempo sem resposta de 1 a 1440 minutos. Nas **Metas por Setor**, o SLA vai de 5 a 43200 minutos e a 1ª resposta de 1 a 1440. Corrija o valor e o botão volta.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Prazo do SLA apagado:** o campo vazio conta como fora do limite, e o **Salvar** fica desativado. **Solução:** preencha o **Prazo do SLA** — para voltar ao valor da tela sem configuração, 24 horas.
>
> **Meta de primeira resposta em zero para "desligar":** o zero é recusado, e o **Salvar** fica desativado. **Solução:** para ficar sem meta, deixe o campo **Meta de primeira resposta (minutos)** vazio.
