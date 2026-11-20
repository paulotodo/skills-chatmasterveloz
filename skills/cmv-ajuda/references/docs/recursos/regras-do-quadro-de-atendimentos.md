# Regras do Quadro de Atendimentos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/regras-do-quadro-de-atendimentos
- **Categoria:** Recursos
- **Menu:** Quadro de Atendimentos › Regras do Quadro de Atendimentos

---

🧩 Sabe a regra do e-mail que joga numa pasta toda mensagem que fala de boleto? As **regras do quadro** fazem a mesma coisa com os atendimentos: levam o card para uma coluna sozinhas, quando o atendimento combina com as condições que você definiu.

O que era arrastar card o dia inteiro passa a acontecer enquanto a equipe responde.

Ideal para:

☑️ **Separação por assunto:** Leva para a coluna do Financeiro todo atendimento em que o cliente falou em boleto, segunda via ou pagamento.

☑️ **Cobrança de retorno:** Separa numa coluna os atendimentos em que o cliente espera resposta há mais de uma hora.

☑️ **Atenção a quem importa:** Reúne numa coluna própria os atendimentos de contatos que merecem cuidado especial.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Quadro de atendimentos** e abra o quadro.
>
> ➡️ Clique em **Regras do quadro** e depois em **Nova regra**.
>
> ➡️ Dê um nome, monte as condições e escolha a coluna de destino.
>
> ➡️ Salve. Para aplicar já nos atendimentos que estão abertos, clique em **Executar regras agora**.

## Quando uma regra roda

A regra é conferida em quatro momentos:

🔘 quando o cliente **manda mensagem**;

🔘 quando uma **tag entra ou sai** do atendimento;

🔘 **a cada minuto**, nas condições de tempo;

🔘 quando alguém clica em **Executar regras agora**.

## A ordem em que as regras valem

⚡ **Vale a primeira regra da lista que combinar.** As outras não chegam a ser testadas para aquele atendimento. Use **Subir (roda antes)** e descer para organizar a prioridade.

⚡ **As regras da equipe vêm antes das suas.** Uma regra da equipe que combine decide antes de qualquer regra pessoal.

⚡ **Cada regra age uma vez por atendimento.** Se você arrastar o card para outra coluna, ele fica onde você pôs — a regra não o traz de volta.

⚡ **Encerrado e reaberto, o atendimento começa do zero.** Quando o cliente volta, as regras conferem o atendimento novo como se fosse a primeira vez.

## As condições

Em **Mover quando** você escolhe se a regra exige que **todas as condições** sejam verdadeiras ou se basta **qualquer uma**. Uma regra aceita até **20 condições**, e cada uma precisa de ao menos um item.

🔘 **Mensagem do cliente contém:** separe as palavras por vírgula. Basta uma aparecer na **última mensagem do cliente**; maiúsculas e acentos não importam.

🔘 **Tem a tag:** basta ter uma das tags escolhidas.

🔘 **Não tem a tag:** não pode ter nenhuma das tags escolhidas.

🔘 **Está na fila:** basta estar em um dos Setores escolhidos.

🔘 **É do contato:** basta ser um dos contatos escolhidos. Para achar, digite ao menos três letras do nome ou do número.

🔘 **Chegou pela conexão:** basta ter chegado por uma das conexões escolhidas.

🔘 **Cliente esperando resposta há:** a última mensagem é do cliente e ninguém respondeu. **Nota interna não conta como resposta**; uma **reação** da equipe conta.

🔘 **Cliente sem responder há:** a última mensagem é da equipe e o cliente não respondeu.

⚠️ Nas duas condições de tempo o mínimo é **10 minutos** e o máximo, **30 dias**, sempre em minutos inteiros.

## Para onde a regra move

Em **Para a coluna** só aparecem **colunas de atendimento** — as colunas de classificação que você cria no quadro. A lista traz as colunas de atendimento de cada quadro, agrupadas pelo nome do quadro, e na lista de regras cada uma mostra *Mover para* a coluna, com o quadro entre parênteses.

⚠️ **A regra organiza o card; ela não aceita nem devolve o atendimento.** Por isso não move para Pendentes, nem para a coluna de quem está em atendimento, nem para uma coluna automática por fila.

⚠️ Se o quadro não tiver nenhuma coluna de atendimento, o editor avisa *"Nenhuma coluna de atendimento disponível. Crie uma na configuração do quadro."* — e a regra não tem para onde mandar o card.

## Regras da equipe

Na aba **Regras da equipe** ficam as regras que valem para um quadro inteiro, criadas por administrador ou supervisor. Na própria regra você escolhe em **Vale para** se ela atinge **todos que usam o quadro** ou **só estas pessoas**.

**Quem usa o quadro** é quem o tem atribuído no cadastro, no menu **Equipe  ›  editar o usuário  ›  aba Setores e Conexões**, campo **Quadros de atendimento**. A regra da equipe só move atendimentos dessas pessoas — o de quem não tem o quadro atribuído fica de fora.

Administrador e supervisor não recebem atribuição — o campo só existe para o perfil User —, então a regra da equipe não age nos atendimentos deles. Para organizar os próprios atendimentos, os dois usam **Minhas regras**, que valem para eles.

Sem ninguém atribuído ao quadro, a aba avisa: *Ninguém está atribuído a este quadro, então as regras da equipe ainda não agem em nenhum atendimento.*

Quem usa o quadro vê as regras da equipe, mas não altera. Elas rodam antes das regras de cada pessoa.

## As regras do atendente

O atendente com quadro atribuído também cria as próprias regras. Para ele a janela **Regras do quadro** não tem abas: em cima ficam as regras **Da equipe (rodam antes das suas)**, só para leitura, e embaixo **Suas regras**, com o botão **Nova regra**. As regras do atendente valem para os atendimentos dele.

## Executar regras agora

Uma regra nova só age a partir do próximo gatilho. O botão **Executar regras agora** aplica as regras imediatamente — para administrador e supervisor, nos **atendimentos abertos de quem usa este quadro**; para o atendente, nos **atendimentos abertos dele**. É o jeito de arrumar o que já estava na tela antes da regra existir.

O resultado aparece na hora, como *16 atendimento(s) avaliado(s), 0 movido(s).* Atendimentos em **Aguardando** ficam de fora: as regras agem nos atendimentos abertos, com atendente. Com muitos atendimentos, a tela avalia os mais recentes, avisa quantos foram, e os demais continuam sendo organizados quando o cliente escrever.

## Como saber que foi uma regra

O card que uma regra moveu mostra **Organizado pela regra** com o nome dela. Assim ninguém fica sem entender por que o atendimento mudou de coluna.

## Excluir uma regra

Excluir uma regra **não mexe nos cards que ela já organizou**: eles continuam onde estão. A regra só para de agir dali em diante.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Criei uma regra e os cards não se mexeram.** A regra só age no próximo gatilho — mensagem do cliente, tag, tempo. Para aplicar já, clique em **Executar regras agora**.
>
> **Arrastei um card e a regra não o devolveu para a coluna dela. É erro?** Não. Cada regra age uma vez por atendimento, e o que você move à mão fica onde você pôs.
>
> **Duas regras combinam com o mesmo atendimento. Qual vale?** A primeira da lista. As regras da equipe vêm antes das pessoais; entre as suas, use **Subir (roda antes)** para mudar a prioridade.
>
> **A regra pode aceitar o atendimento por mim?** Não. Ela só organiza o card entre colunas de atendimento — aceitar, devolver e transferir continuam sendo ação de alguém.
>
> **Nota interna conta como resposta na condição Cliente esperando resposta há?** Não. Só mensagem para o cliente, ou uma reação da equipe à mensagem dele, tira o atendimento dessa condição.
>
> **O que acontece com os cards se eu excluir a regra?** Nada. Eles continuam onde a regra os deixou.
>
> **A regra da equipe não moveu o atendimento de um colega.** Confira se ele tem o quadro atribuído no cadastro, campo **Quadros de atendimento**: a regra da equipe só age nos atendimentos de quem usa o quadro.
>
> **O atendente pode criar as próprias regras do quadro?** Pode, com o quadro atribuído. Ele vê as regras da equipe só para leitura e cria as dele em **Suas regras**.
>
> **O supervisor pode criar regras da equipe?** Pode. Administrador e supervisor criam regras da equipe na aba **Regras da equipe**.
>
> **A regra da equipe não age nos atendimentos do administrador nem do supervisor.** É assim: a regra da equipe só age nos atendimentos de quem tem o quadro atribuído, e o campo **Quadros de atendimento** só existe para o perfil User. Para os próprios atendimentos, administrador e supervisor usam **Minhas regras** — essas valem para eles.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Não aparece nenhuma coluna para escolher como destino:** o quadro não tem coluna de atendimento. **Solução:** crie uma no menu **Quadro de atendimentos  ›  Configurar quadros**, com o tipo **Coluna de atendimento**.
>
> **A regra nunca dispara:** quase sempre outra regra acima dela combina primeiro e fica com o atendimento. **Solução:** confira a ordem da lista e suba a regra que deve ter prioridade.
>
> **Palavra que não pega:** a condição olha só a **última** mensagem do cliente. **Solução:** se a palavra pode vir numa mensagem anterior, combine com uma condição de tag ou de tempo.
