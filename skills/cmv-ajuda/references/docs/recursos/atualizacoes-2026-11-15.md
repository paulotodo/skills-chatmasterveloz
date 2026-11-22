# Atualizações 15/11/2026

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-11-15
- **Categoria:** Recursos
- **Menu:** Atualizações › Novembro 2026 › Atualizações 15/11/2026

---

🧩 Atualizações de 15 de novembro de 2026.

Todas as novidades abaixo estão disponíveis a partir da versão **WS-30.39.0**. Para ver a sua, clique no ícone do perfil, no topo da tela: a versão aparece no fim do menu.

#### Novidades

⚡️ **Reservas de ponta a ponta:** o módulo novo, do cadastro à reserva do cliente. No menu **Reservas**, o administrador cadastra os recursos, as ofertas, os horários e os bloqueios; a equipe trabalha na **Agenda de reservas**; o cliente reserva sozinho na página de reservas; e os avisos e a lista de espera mantêm o cliente informado.

⚡️ **Diária:** ainda nas Reservas, a oferta pode ser por noite, como numa pousada, com entrada e saída, mínimo e máximo de noites e o total na hora.

☑️ **Saída e noites nos avisos:** os avisos ao cliente podem levar a data de saída e o número de noites da estadia.

⚡️ **Pagamento da reserva:** o detalhe da reserva registra o que o cliente pagou no balcão, mostra quanto foi pago e quanto falta, e permite estornar.

⚡️ **Sinal pelo link:** com uma conta de pagamento conectada nas **Configurações**, o detalhe da reserva gera o link do sinal para enviar ao cliente, que paga na página, com Pix. Com a conta conectada e o **Sinal obrigatório na página** ligado, a reserva feita na página fica guardada até o cliente pagar.

⚡️ **Turmas:** aulas, passeios e sessões em grupo, com vagas em cada horário: várias pessoas reservam o mesmo horário até lotar.

⚡️ **Pacotes:** o cliente compra várias aulas ou sessões de uma vez, e cada reserva feita com o pacote gasta um crédito.

⚡️ **Reservas que se repetem:** na **Nova reserva**, a reserva pode se repetir toda semana, a cada 15 dias, todo mês ou todo dia.

⚡️ **Relatório das Reservas:** a aba **Relatório** mostra, por período, as reservas, o comparecimento, o previsto e o recebido, a ocupação e de onde vieram as reservas.

⚡️ **Agenda do Google:** cada recurso pode ser ligado a uma agenda do Google: a reserva aparece lá, e o compromisso de lá ocupa o horário aqui.

⚡️ **Reservar pela conversa:** no **FlowBuilder Nativo**, o bloco **Reservas** leva a reserva para a conversa: o cliente escolhe a oferta, o dia e o horário pelo número e recebe o código.

⚡️ **API das Reservas:** um site, um app ou outro sistema consulta as ofertas e os horários livres e cria, remarca, confirma e cancela reservas.

☑️ **Webhook das Reservas:** o webhook das Reservas passa a avisar o seu sistema também sobre pacotes, reservas que se repetem e falha na agenda do Google.

#### Melhorias

☑️ **Assistente de IA sobre as reservas:** o **Assistente de IA** também responde sobre as reservas: por exemplo, quantas há amanhã, ou acha uma reserva pelo nome ou pelo telefone do cliente, ou pelo código da reserva.

## O cadastro das Reservas

No menu **Reservas**, o administrador monta o que vai ser reservado. O cadastro é do administrador: supervisor e atendente trabalham na **Agenda de reservas**.

➡️ **Recursos:** quem ou o que atende: o profissional, a sala, a mesa, o quarto ou o equipamento.

➡️ **Ofertas:** o que o cliente reserva, como a consulta num consultório, com duração, preço e, se quiser, um sinal, em percentual ou em valor fixo.

➡️ **Horários:** os horários de cada recurso, dia a dia.

➡️ **Bloqueios:** os períodos em que um recurso, ou todos, não atende, como férias e feriados.

## Agenda de reservas

A equipe trabalha na **Agenda de reservas**, que mostra o **Dia**, com uma coluna por recurso, e a **Semana**.

➡️ A **Nova reserva** só oferece os horários livres.

➡️ Em cada reserva, a equipe confirma, conclui, marca como não compareceu, cancela, com um motivo se quiser, ou remarca pelo **Editar**.

➡️ O detalhe da reserva mostra o código, de onde ela veio, o valor, o sinal e as mensagens enviadas ao cliente.

## Página de reservas

Na aba **Página** do menu **Reservas**, o administrador dá nome e endereço à página de reservas e liga **Página no ar**. Na página, o cliente reserva sozinho, sem login: escolhe a oferta, o dia e o horário e põe os dados dele.

➡️ Ao reservar, o cliente recebe um código e, na **Minha reserva**, pode cancelar até o prazo definido em **Cancelar até quantas horas antes**.

## Avisos e lista de espera

Na aba **Avisos** do menu **Reservas**, o administrador liga as mensagens ao cliente: **Reserva confirmada**, **Pedido recebido**, **Confirmada pela equipe**, **Reserva remarcada** e **Reserva cancelada**, e até cinco lembretes antes do horário. As mensagens são enviadas na conversa do cliente, pela conexão escolhida em **Enviar pela conexão**, e todas começam desligadas.

➡️ Com o aviso **Vaga na lista de espera** ligado, a página de reservas oferece a lista de espera quando o dia lota.

➡️ Quando uma reserva é cancelada e abre vaga, quem está na lista de espera daquele dia é avisado sozinho, com os horários livres.

## Diária

Nas ofertas das Reservas, o **Tipo de reserva** **Por diária** é para quartos, chalés e salas por noite, com **Entrada (check-in)** e **Saída (check-out)**, o mínimo e o máximo de noites e o **Preço da diária (por noite)**.

➡️ Na página de reservas, o cliente escolhe a entrada e a saída num calendário que apaga as noites ocupadas e mostra o total.

➡️ Na **Agenda de reservas**, a estadia aparece em cada dia, com as noites e o total.

➡️ Quem sai e quem entra no mesmo dia, no mesmo quarto, não dá conflito.

➡️ Os avisos ao cliente podem levar a data de saída e o número de noites, pelas variáveis `{{dataSaida}}` e `{{noites}}`. Os textos que já vêm prontos não trazem as duas: para o cliente receber, inclua as variáveis no texto do aviso, na aba **Avisos**.

## Pagamento da reserva

No detalhe da reserva, o bloco **Pagamento da reserva** mostra o valor, quanto foi pago e quanto falta.

➡️ **Registrar pagamento** guarda o que o cliente pagou no balcão, com a forma: **Dinheiro**, **Pix**, **Cartão**, **Boleto** ou **Outro**. O pagamento pode ser de uma parte do valor.

➡️ Cada pagamento registrado pode ser desfeito pelo **Estornar**.

## Turmas

Nas ofertas das Reservas, o **Tipo de reserva** **Turma (sessão em grupo)** é para aulas, passeios e sessões em grupo: num estúdio, cada aula tem vagas, e várias pessoas reservam o mesmo horário até lotar. As **Vagas por sessão** vão de 1 a 500.

➡️ A **Nova reserva**, a página de reservas e a conversa do fluxo mostram quantas vagas sobram em cada horário.

➡️ O horário lotado some da escolha.

## Pacotes

Com os pacotes das Reservas, o cliente compra várias aulas ou sessões de uma vez. Na aba **Pacotes** do menu **Reservas**, o administrador cria cada pacote com quantas reservas ele tem, a validade em dias, o preço e as ofertas que ele cobre. O pacote não vale para diárias.

➡️ Na **Agenda de reservas**, o botão **Pacotes** abre os **Pacotes dos clientes**, onde você vende o pacote ao cliente e vê o saldo de cada um.

➡️ Na **Nova reserva**, **Usar um pacote do cliente** faz a reserva sem cobrar de novo: ela fica sem preço e gasta um crédito do pacote.

➡️ Quando a reserva feita com o pacote é cancelada, o crédito volta.

## Reservas que se repetem

Na **Nova reserva**, **Repetir esta reserva** cria a mesma reserva várias vezes, como a sessão semanal no consultório: **Toda semana**, **A cada 15 dias**, **Todo mês** ou **Todo dia**, de 2 a 52 vezes, dentro de um ano. A diária não se repete.

➡️ **Ver as datas** mostra as datas antes de criar, e **Pular as datas ocupadas** cria só as que estão livres.

➡️ Com pacote, cada data da série gasta um crédito.

➡️ Ao cancelar uma reserva da série, você escolhe: **Só esta**, **Esta e as próximas** ou **Todas da série**.

## Relatório das Reservas

No menu **Reservas**, a aba **Relatório** mostra os números de um período de até 366 dias, por oferta e por recurso. Só o administrador vê os números do Relatório.

➡️ As reservas, o comparecimento, as faltas e os cancelamentos.

➡️ O **Previsto**, o **Recebido** e o que falta receber, em **A receber**.

➡️ A ocupação, os dias da semana e os horários mais procurados, os clientes e de onde vieram as reservas.

➡️ **Exportar CSV** baixa os números do período.

## Reservar pela conversa

No **FlowBuilder Nativo**, o bloco **Reservas (agendar no fluxo)** leva a reserva para a conversa. O cliente escolhe pelo número a oferta, o dia e o horário; na diária, o dia da entrada e quantas noites. Depois confere, confirma e recebe o código da reserva.

➡️ No bloco Reservas, **Dias à frente** diz quantos dias a conversa oferece, de 1 a 30, e **Adicionar uma oferta** escolhe as ofertas do bloco. Sem nenhuma escolhida, valem todas as ofertas ativas.

➡️ O fluxo segue pela saída **Reservou** ou **Não reservou**, e por **Sem resposta** quando você define os minutos em **Sem resposta: seguir pela saída depois de (minutos)**.

➡️ Na **Agenda de reservas**, a reserva aparece como feita **Pela conversa**, no contato do atendimento.

## API das Reservas

Pela API das Reservas, um site, um app ou outro sistema consulta as ofertas e os horários livres e cria, remarca, confirma e cancela reservas, inclusive as que se repetem. A API das Reservas também vende pacotes e consulta o saldo.

➡️ Na **Agenda de reservas**, essas reservas aparecem como feitas **Pela integração**.

#### O que você precisa fazer

➡️ Para usar as Reservas: comece pelo menu **Reservas**, como administrador. Cadastre os recursos, as ofertas e os horários e, na aba **Página**, ligue **Página no ar** para o cliente reservar sozinho.

➡️ Para avisar o cliente: na aba **Avisos**, ligue as mensagens que quiser. Elas começam desligadas.

➡️ Para o cliente reservar pela conversa: no FlowBuilder Nativo, ponha o bloco **Reservas** no fluxo.

➡️ Para os avisos da diária mostrarem a saída e as noites: inclua `{{dataSaida}}` e `{{noites}}` no texto do aviso.

O resto não exige ação.
