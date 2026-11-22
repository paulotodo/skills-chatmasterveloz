# Visão Geral Rodízios

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/visao-geral-rodizios
- **Categoria:** Recursos
- **Menu:** Rodízios › Visão Geral Rodízios

---

🧩 O menu **Rodízios** lista os rodízios da empresa, mostra em quais fluxos cada um está em uso e guarda os registros das últimas 24 horas. É nele que nasce e se altera cada rodízio que o bloco **Rodízio** do FlowBuilder Nativo usa.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Rodízios**.
>
> ➡️ Clique em **Novo rodízio**, dê um nome, escolha como distribuir, o Setor de transbordo e os participantes, e clique em **Salvar**.
>
> ➡️ No fluxo, abra o bloco **Rodízio** e escolha o rodízio em **Distribuição**.
>
> ➡️ Para saber por que um atendimento não chegou a ninguém, clique em **Logs (24h)**.

## O que a lista mostra

Cada linha da lista do menu **Rodízios** é um rodízio:

🔘 **Nome** e **ID:** o nome do rodízio e o número dele.

🔘 **Ativo:** liga e desliga o rodízio direto na lista. Desligado, o atendimento que chega ao bloco vai para o Setor de transbordo.

🔘 **Participantes:** quantas pessoas participam do rodízio.

🔘 **Ciclo:** quando a contagem recomeça, ou a rodada sorteada.

🔘 **Usado nos fluxos:** os fluxos que usam o rodízio, ou *Nenhum fluxo*.

🔘 **Ações:** **Editar** e **Excluir**. Rodízio em uso num fluxo não se exclui: a tela avisa *"Em uso em algum fluxo: desative em vez de excluir"*. Ao excluir, a tela lembra que *"O histórico de distribuição continua no relatório."*

Com o **Relatório do Rodízio** ligado, o topo da tela também tem **Ver relatório**.

## Como cadastrar um rodízio

Acesse o menu **Rodízios  ›  Novo rodízio**

🔘 **Nome do rodízio** e **Ativo:** o nome que aparece no bloco **Rodízio** do fluxo, e se o rodízio está valendo.

🔘 **Como distribuir:** **Equilibrado no ciclo (pelos percentuais)** ou **Rodada sorteada (um para cada antes de repetir)**.

🔘 **Ciclo de Rodízio:** só no modo equilibrado. Define quando a contagem dos percentuais recomeça: **Por Hora Cheia**, **Por Dia**, **Por Semana**, **Por Mês** ou **Integral (Total)**, que considera todo o histórico.

🔘 **Se não encontrar operador disponível (offline ou no limite de atendimentos), mover para:** o **Setor** que recebe o atendimento quando nenhum participante pode receber.

🔘 **Escolha os participantes:** escolha cada pessoa em **Operador**. Cada participante tem o **Status** (**Online** recebe só quando está conectado; **Indiferente** recebe mesmo offline), a **Porcentagem** dele no modo equilibrado, o **Setor** em que o atendimento fica (ou **Manter o setor atual**) e **Entregar em** (**Padrão da empresa**, **Atendendo** ou **Aguardando (MEUS)**).

Clique em **Salvar**. A tela confirma *"Rodízio salvo."*

## Como dividir o transbordo entre vários Setores

Escolhido o Setor de transbordo, a janela do rodízio oferece **Dividir o transbordo entre mais filas**. Clicado, aparece o painel da divisão. Nas palavras da tela: *"Quando ninguém puder receber, o atendimento vai para uma destas filas, dividido pelos percentuais dentro do ciclo do rodízio. Com todos os percentuais em zero, divide igual."*

🔘 **Fila principal (escolhida acima):** o Setor escolhido em **Se não encontrar operador disponível**, com o **Percentual (%)** dele.

🔘 **Fila de transbordo:** outro Setor que divide o transbordo, com o **Percentual (%)** dele.

🔘 **Adicionar fila:** inclui mais um Setor na divisão.

## Como ver os Logs (24h)

Acesse o menu **Rodízios  ›  Logs (24h)**

A janela *"Logs do rodízio — últimas 24 horas"* mostra cada atendimento que foi para o transbordo e cada erro da distribuição nas últimas 24 horas, com um resumo no topo, como *"0 transbordo(s) e 0 erro(s) nas últimas 24 horas."*

🔘 **Rodízio** e **Tipo:** filtram os Logs (24h) por rodízio e por tipo — **Todos**, **Transbordo** ou **Erro**.

🔘 **Atualizar:** recarrega os registros.

Cada linha dos Logs (24h) traz **Quando**, **Tipo**, **Rodízio**, **Atendimento** e **Motivo**. O motivo do transbordo diz por que ninguém recebeu: *"O rodízio está desativado."*, *"O rodízio não tem participantes."* ou *"Ninguém do rodízio podia receber naquela hora."* No último caso, a linha mostra cada participante com o motivo dele: *offline*, *ausente*, *no limite de atendimentos*, *em chamada*, *desativado neste rodízio* ou *usuário inativo*.

A linha também diz para onde o atendimento foi — *"O atendimento foi para a fila …"* ou *"Sem fila de transbordo: ficou onde estava."* — e se ele veio de um rodízio cadastrado, de um *Bloco configurado no fluxo* ou da integração (*pela API*).

Os erros mostram o que falhou na distribuição, como *"A distribuição falhou e o atendimento ficou onde estava"*.

Sem nada no período, a janela diz *"Nenhum transbordo nem erro nas últimas 24 horas."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Por que um atendimento do rodízio foi para o Setor de transbordo?** Abra **Logs (24h)** no menu **Rodízios**: a linha do atendimento diz o motivo — rodízio desativado, rodízio sem participantes ou ninguém disponível — e, no último caso, por que cada participante não recebeu.
>
> **Posso excluir um rodízio que está em uso num fluxo?** Não. O menu **Rodízios** avisa *"Em uso em algum fluxo: desative em vez de excluir"*. Desligue **Ativo** na lista, ou tire o rodízio do bloco **Rodízio** do fluxo antes de excluir.
>
> **No transbordo dividido, o que acontece com todos os percentuais em zero?** A divisão fica igual entre os Setores do painel.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Sem Setor de transbordo:** a equipe sai para o almoço, todos ficam offline e o atendimento fica onde estava — os **Logs (24h)** mostram *"Sem fila de transbordo: ficou onde estava."* **Solução:** escolha um Setor em **Se não encontrar operador disponível**, no cadastro do rodízio.
