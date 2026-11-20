# Colunas do Quadro de Atendimentos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/colunas-do-quadro-de-atendimentos
- **Categoria:** Recursos
- **Menu:** Quadro de Atendimentos › Colunas do Quadro de Atendimentos

---

🧩 As colunas são o desenho do seu quadro. Duas já vêm prontas e não podem faltar; da terceira em diante, você escolhe **o tipo** de cada uma — e é o tipo que decide se a coluna apenas classifica ou se também mexe no atendimento.

Acesse o menu **Quadro de atendimentos  ›  Configurar quadros**.

As colunas valem para a visão por **Colunas** do quadro. Na visão por **Tags**, as colunas são as tags dos atendimentos, e esta configuração não muda nada nela.

## As duas colunas que todo quadro tem

🔘 **Pendentes:** recebe todo atendimento que chega e ainda não foi aceito. **Não pode ser renomeada, movida nem excluída** — o campo dela vem travado.

🔘 **Atendendo:** os atendimentos aceitos e ainda sem classificação. **O nome pode ser trocado** no próprio campo da lista, e a troca vale ao sair do campo; a posição e a existência, não.

⚠️ Essas duas refletem o que o sistema já sabe sobre o atendimento, e é por isso que são fixas. A primeira é o mesmo estado que a tela de conversas chama de **Aguardando**.

## Os três tipos de coluna que você cria

Escreva o nome no campo **Nome da nova coluna**, escolha o tipo e a cor, e clique em **ADICIONAR COLUNA**.

🔘 **Coluna de atendimento:** a classificação clássica. O atendimento que entra aqui **continua aberto** — segue na lista de atendimentos, nos relatórios e recebendo mensagem. Serve para dizer por que o atendimento está parado: *Aguardando peça*, *Enviado ao financeiro*, *Retornar amanhã*. É também o **único tipo de coluna para onde as regras do quadro movem um card**.

🔘 **Coluna de fila (pendente):** guarda atendimentos que **ainda não foram aceitos**. Arrastar um card pendente para ela organiza a espera **sem aceitar** o atendimento — ele continua sem dono, disponível para quem pegar.

🔘 **Coluna automática por fila (pendente):** você escolhe um ou mais Setores, no campo **Setores**, e a coluna **se enche sozinha** com os pendentes deles, sem ninguém arrastar. Sem nenhum Setor escolhido, o **ADICIONAR COLUNA** fica desativado.

Quando a coluna automática tem **um** Setor, **arrastar um card para ela transfere o atendimento para aquele Setor** — o sistema pergunta antes. Com **mais de um** Setor, o arrasto não transfere: a tela avisa *Esta coluna reúne mais de uma fila. Transfira o atendimento pelo próprio atendimento, escolhendo a fila.*

Na coluna automática, cada pessoa vê só os pendentes dos Setores dela.

⚠️ **Cada Setor só pode estar em uma coluna automática por quadro.** A tela recusa a segunda com *Uma das filas já está em outra coluna automática deste quadro.*

⚠️ **Sem nenhuma coluna de atendimento, as regras do quadro não têm para onde mover.** O editor de regras avisa *"Nenhuma coluna de atendimento disponível"* — crie uma aqui primeiro.

## A ordem das colunas

Cada coluna sua tem as setas **Mover para a esquerda no quadro** e **Mover para a direita no quadro**, e é essa ordem que o quadro usa. As duas fixas ficam sempre no começo.

## Quando o atendimento é encerrado e o cliente volta

A coluna não guarda o atendimento depois de encerrado. Quando o cliente escreve de novo, ele chega como **atendimento novo**: entra em **Pendentes**, ou na **coluna automática do Setor** dele, e vai para **Atendendo** quando alguém aceita.

Ou seja: a classificação que o atendimento tinha antes de encerrar **não volta com ele**. Cada atendimento começa limpo.

## O que acontece ao excluir uma coluna

Os atendimentos que estavam nela **voltam para a coluna de atendimento**, e nenhum é excluído. A própria confirmação avisa isso antes de você decidir.

Testado: um atendimento classificado numa coluna própria voltou para **Atendendo** quando a coluna foi apagada, e continuou aberto.

## Como nomear bem uma coluna

➡️ **Nomeie a espera, não a pessoa.** *Aguardando peça*, *Enviado ao financeiro*, *Retornar amanhã* dizem por que o atendimento está parado. *João* e *Equipe 2* não — para isso existe o filtro de Usuários.

➡️ **Uma coluna por motivo de parada.** Se ninguém consegue dizer o que diferencia duas colunas, elas são a mesma.

➡️ **Cor ajuda mais que nome comprido.** O card é pequeno; a cor é o que se enxerga de longe.

## Criar, renomear e excluir um quadro

No mesmo lugar você escreve o **Nome do novo quadro** e clica em **CRIAR**. Com um quadro selecionado, o campo **Nome do quadro** renomeia, e **Excluir quadro** apaga.

⚠️ Excluir um quadro não encerra nem apaga atendimento nenhum — somem a visão em colunas, a classificação que existia nela e as **atribuições**: quem tinha aquele quadro no cadastro deixa de tê-lo.

A classificação é de cada quadro: o mesmo atendimento pode estar numa coluna de um quadro e em outra coluna de outro quadro.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso excluir a coluna Pendentes?** Não. Ela e a coluna de atendimento são fixas em todo quadro. A primeira nem renomear aceita.
>
> **Qual a diferença entre a coluna de fila e a coluna automática por fila?** Na de fila você arrasta os pendentes à mão, para organizar a espera do seu jeito. A automática se enche sozinha com os pendentes dos Setores que você escolheu — e, com um Setor só, o arrasto para ela passa a transferir de Setor.
>
> **Um card apareceu numa coluna automática e eu não consigo tirar.** Ele está ali por causa do Setor do atendimento. Para tirá-lo, transfira o atendimento de Setor — a própria tela avisa isso quando você tenta.
>
> **Por que a coluna automática mostra um número para mim e outro para o atendente?** Cada pessoa vê na coluna automática só os pendentes dos Setores dela.
>
> **Encerrei um atendimento e o cliente voltou. Por que ele não está na coluna onde estava?** Porque volta como atendimento novo, começando em Pendentes ou na coluna automática do Setor. A classificação anterior não acompanha.
>
> **Se eu excluir uma coluna minha, o que acontece com os atendimentos que estavam nela?** Voltam para a coluna de atendimento. Nenhum atendimento é excluído, encerrado ou alterado — some só a classificação que eles tinham naquela coluna.
>
> **Mudar a ordem das colunas muda alguma coisa nos atendimentos?** Não. A ordem é só a sequência em que elas aparecem na tela.
