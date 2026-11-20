# Reservas (agendar no fluxo)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/reservas-agendar-no-fluxo
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Reservas (agendar no fluxo)

---

🧩 O bloco **Reservas (agendar no fluxo)** deixa o cliente reservar sozinho, pela conversa: ele escolhe pelo número a oferta, o dia e o horário livre (na diária, o dia da entrada e as noites), confere o resumo e confirma. A reserva nasce no contato do atendimento, com as mesmas regras da página de reservas, e o cliente recebe o código dela.

**🏷️ Categoria: Mensagem - Roteador**

Ideal para:

☑️ **Reserva fora do expediente:** recebe a reserva de quem chama à noite ou no fim de semana, sem esperar a equipe.

☑️ **Marcação sem vai e vem:** mostra na hora só os horários livres, sem o atendente consultar a agenda e voltar com as opções.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Reservas (agendar no fluxo)**.
>
> ➡️ Escolha as ofertas que vão no bloco, ou não escolha nenhuma para oferecer todas, e clique em **Adicionar**.
>
> ➡️ Ligue as saídas **Reservou** e **Não reservou** ao próximo passo do fluxo.

## Como configurar o bloco Reservas (agendar no fluxo)

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Reservas (agendar no fluxo)**

🔘 **Texto antes da lista:** vem antes da primeira lista. Em branco, o cliente lê *"Escolha o que você quer reservar pelo número:"*.

🔘 **Dias à frente:** quantos dias o cliente pode escolher, a partir de hoje, de 1 a 30. Um número fora da faixa é ajustado ao salvar: abaixo de 1 vira 7, e acima de 30 vira 30.

🔘 **Adicionar uma oferta:** põe uma oferta no bloco. A lista **Ofertas no bloco** mostra a ordem em que o cliente vai ver, e **Tirar do bloco** tira uma oferta. Sem nenhuma escolhida, o bloco oferece todas as ofertas ativas, na ordem do cadastro.

🔘 **Sem resposta: seguir pela saída depois de (minutos):** com minutos preenchidos, o bloco ganha a saída **Sem resposta**, para quem não responder nesse tempo. Vazio ou 0 desliga.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco mostra as ofertas numeradas, ou *"Todas as ofertas ativas"*, e os dias, como *"Próximos 7 dias"*. As saídas são **Reservou** e **Não reservou**, mais **Sem resposta** quando os minutos estão preenchidos.

## O que o cliente vê

➡️ A lista das ofertas, cada uma com o preço, como *"1 - Corte · R$ 50,00"* ou *"2 - Diária Quarto · R$ 200,00 por noite"*, e *"0 - Desistir"*. Com uma oferta só no bloco, essa lista é pulada, e o cliente vai direto aos dias.

➡️ Os dias: *"Escolha o dia pelo número:"*, só com os dias em que há atendimento dentro dos dias à frente, como *"1 - Amanhã 16/11 · 2 - Ter 17/11"*.

➡️ Os horários livres do dia: *"Horários livres em Ter 17/11. Escolha pelo número:"*, na mesma grade da página de reservas. Na turma, cada horário mostra as vagas que sobram, como *"08:00 (1 vaga)"*, e a sessão lotada não aparece.

➡️ Na diária, o dia da entrada, em *"Escolha o dia da entrada pelo número:"*, e depois as noites, em *"Quantas noites? Responda com um número de 1 a 5."*, com o número de noites que a oferta aceita.

➡️ O resumo: *"Confira a sua reserva:"*, com a oferta, o dia e o horário (na diária, a entrada, a saída e as noites) e o valor, e as opções *"1 - Confirmar a reserva"*, *"2 - Escolher outra data"* e *"0 - Desistir"*.

➡️ Ao confirmar, *"Reserva feita! Código: K7M2Q9TX."*, e o fluxo segue pela saída **Reservou**.

➡️ Com **Confirmar sozinho** desligado na aba **Página** das Reservas, a mensagem ao confirmar é *"Pedido de reserva recebido! Código: K7M2Q9TX. A nossa equipe vai confirmar e te avisa."*, e o fluxo também segue pela saída **Reservou**.

➡️ Em todas as listas depois da primeira, o **V** volta um passo. A resposta fora das opções recebe *"Não entendi. Responda com o número de uma das opções."* e a mesma lista de novo.

➡️ Sem horário livre nos dias à frente, o cliente lê *"Não há horários livres nos próximos dias. Fale com a nossa equipe por aqui."*, e o fluxo segue pela saída **Não reservou**.

➡️ Na turma, quando a última vaga é ocupada enquanto o cliente confirma, ele lê *"Essa turma acabou de lotar. Escolha de novo:"* e escolhe outra vez.

## As outras saídas

🔘 **Não reservou:** o **0** desiste em qualquer passo. Nenhuma reserva é criada, e o fluxo segue pela saída **Não reservou**, sem outra mensagem ao cliente. Ligue essa saída a uma mensagem ou à transferência para um Setor.

🔘 **Sem resposta:** quando o cliente para de responder pelo tempo escolhido, o fluxo segue pela saída **Sem resposta**.

## A reserva que nasce no fluxo

A reserva feita pelo bloco **Reservas (agendar no fluxo)** entra na **Agenda de reservas** com a origem **Pela conversa**, no contato do atendimento. Com **Confirmar sozinho** ligado na aba **Página** das Reservas, ela já nasce **Confirmada**. Com ele desligado, ela nasce **Pendente**, à espera da equipe, e já ocupa o horário, que deixa de aparecer para os próximos clientes.

O bloco **Reservas (agendar no fluxo)** segue as mesmas regras da página de reservas e funciona também com a opção **Página no ar** desligada.

Na oferta com mais de um recurso, o cliente não escolhe com quem nem onde: o bloco **Reservas (agendar no fluxo)** põe a reserva num recurso livre no horário escolhido. O horário só some da lista quando todos os recursos da oferta estão ocupados.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A reserva feita pelo bloco Reservas (agendar no fluxo) aparece para a equipe?** Sim. Ela entra na **Agenda de reservas** com a origem **Pela conversa**, no contato do atendimento.
>
> **Preciso deixar a página de reservas no ar para usar o bloco Reservas (agendar no fluxo)?** Não. O bloco funciona com a **Página no ar** desligada e segue as mesmas regras da página, como o **Confirmar sozinho**.
>
> **Quais ofertas aparecem no bloco Reservas (agendar no fluxo)?** As que você pôs no bloco, na ordem da lista **Ofertas no bloco**. Sem nenhuma escolhida, todas as ofertas ativas, na ordem do cadastro. A oferta sem recurso não aparece para o cliente.
>
> **O cliente escolhe o profissional ou a sala no bloco Reservas (agendar no fluxo)?** Não. Na oferta com mais de um recurso, o bloco põe a reserva num recurso livre no horário escolhido.
>
> **Dá para oferecer turmas e diárias pelo bloco Reservas (agendar no fluxo)?** Sim. Na turma, cada horário mostra as vagas que sobram. Na diária, o cliente escolhe o dia da entrada e o número de noites.
>
> **O cliente consegue remarcar ou cancelar pelo bloco Reservas (agendar no fluxo)?** Não. O bloco só cria a reserva. A equipe remarca e cancela no menu **Agenda de reservas**.
>
> **Posso continuar o fluxo depois da reserva?** Sim. Ligue a saída **Reservou** ao próximo bloco, como uma mensagem de agradecimento ou a transferência para um Setor.
