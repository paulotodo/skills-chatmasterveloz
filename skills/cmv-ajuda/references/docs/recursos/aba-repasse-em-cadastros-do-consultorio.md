# Aba Repasse em Cadastros do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-repasse-em-cadastros-do-consultorio
- **Categoria:** Recursos
- **Menu:** Consultório › Aba Repasse em Cadastros do Consultório

---

🧩 O **repasse** é a parte de cada consulta que vai para o profissional que atendeu. A aba **Repasse** guarda as regras dessa divisão, soma o que cada profissional tem a receber das consultas já pagas e registra quando a clínica acerta com ele.

Ideal para:

☑️ **Clínica com profissionais parceiros:** cada um recebe um percentual do que atendeu.

☑️ **Fechamento do mês:** ver quanto falta pagar a cada profissional e registrar o que foi pago.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Consultório  ›  Cadastros do consultório** e abra a aba **Repasse**.
>
> ➡️ Em **Regras de repasse**, escolha o **Profissional**, o **Serviço** e o **Tipo**, preencha o valor e clique em **Salvar regra**.
>
> ➡️ Em **Relatório de repasse**, marque as consultas que vai pagar e clique em **Marcar como pago**.

## As regras de repasse

Cada regra diz quanto vai para o profissional: um percentual do que a consulta recebeu ou um valor fixo por consulta.

🔘 **Profissional:** a quem a regra vale. **Todos** vale para qualquer profissional.

🔘 **Serviço:** em qual serviço a regra vale. **Todos** vale para qualquer serviço.

🔘 **Tipo:** **Percentual**, com o campo **Percentual (%)**, ou **Valor fixo**, com o campo **Valor por consulta (R$)**.

O **Salvar regra** não libera com **Todos** nos dois campos, nem com percentual acima de 100. Salva, a regra entra na lista com a coluna **Vale para**: **o profissional**, **o serviço** ou **profissional + serviço**.

Quando mais de uma regra serve para a mesma consulta, vale a mais específica. Nas palavras da tela: *"a do profissional com o serviço, depois a do serviço, depois a do profissional."*

📌 **Exemplo:** a regra da Dra. Ana com **Todos** os serviços dá 40%; a do serviço **Retorno** dá R$ 30,00 para qualquer profissional; e a da Dra. Ana com o **Retorno** dá 50%. No retorno da Dra. Ana vale a última, 50%, porque é a mais específica.

🔘 **Remover a regra:** o ícone na linha da regra. Remove na hora, sem pedir confirmação, e a tela avisa *"Regra de repasse removida."*

## O relatório de repasse

O relatório mostra as consultas quitadas do período, separadas por profissional.

🔘 **De** e **Até:** o período.

🔘 **Profissional:** um profissional ou **Todos**.

🔘 **Situação:** **A pagar**, em que a tela abre, **Pago** ou **Todos**.

No topo fica o total do filtro, como *A pagar: R$ 52,00 · Pago: R$ 0,00 · 1 consulta(s)*. Cada profissional tem o seu bloco, com o que falta pagar e o que já foi pago, e uma linha por consulta: **Data**, **Paciente**, **Serviço**, **Recebido**, **Regra**, **Repasse** e **Situação**.

◽ **Recebido** é o que a consulta recebeu na cobrança, e **Repasse** é a regra aplicada sobre ele: 40% de R$ 130,00 dá R$ 52,00.

◽ **Regra** mostra qual regra valeu, como *40% · o profissional*.

A **Situação** de cada consulta:

◽ **A pagar** — a consulta tem regra e o repasse ainda não foi pago.

◽ **Pago** — o repasse da consulta já foi registrado.

◽ **Sem regra** — nenhuma regra serve para o profissional e o serviço da consulta. Cadastre a regra para ela entrar no pagamento.

◽ **Pago (consulta estornada depois)** — o repasse já estava pago quando um pagamento da consulta foi estornado.

## Marcar como pago

➡️ Marque a caixa das consultas que vai pagar. A caixa do cabeçalho marca todas as do profissional, e só as consultas **A pagar** têm caixa.

➡️ Se quiser, escreva a **Observação do pagamento**, como a forma ou o dia em que pagou.

➡️ Clique em **Marcar como pago**. O botão mostra quantas consultas e o total, como *Marcar como pago (1) · R$ 52,00*.

A tela avisa *"Repasse registrado como pago."*, a consulta passa a **Pago** e o repasse entra em **Repasses pagos**. Pagar de novo a mesma consulta é recusado: *"Uma das consultas já teve o repasse pago."*

⚠️ **Marcar como pago** não transfere dinheiro ao profissional. Ele registra o repasse que a clínica paga por fora, do jeito que já paga.

## Repasses pagos

A lista mostra os repasses registrados no período: **Pago em**, **Profissional**, **Valor**, **Consultas**, **Quem pagou** e a observação.

🔘 **Desfazer:** cancela um repasse registrado por engano. A tela pede confirmação — *"As 1 consulta(s) deste repasse de R$ 52,00 voltam para a pagar. O registro fica como desfeito."* — e, no **OK**, avisa *"Repasse desfeito: as consultas voltaram para a pagar."*

O repasse desfeito continua na lista, com *Desfeito por* quem e quando, e as consultas dele voltam a **A pagar**.

## Quando a consulta é estornada depois

Se um pagamento da consulta for estornado depois do repasse pago, o repasse não muda: a linha passa a **Pago (consulta estornada depois)**, com o **Recebido** novo e o mesmo **Repasse**. O acerto com o profissional fica com a clínica. Quando a consulta recebe de novo, a linha volta a **Pago**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A consulta de hoje não aparece no relatório.** Só entram as consultas quitadas. Registre o pagamento na cobrança da consulta, e ela aparece em **A pagar**.
>
> **Marquei como pago o repasse errado.** Em **Repasses pagos**, clique em **Desfazer** no repasse. As consultas voltam a **A pagar**, e o registro fica na lista como desfeito.
>
> **Um profissional recebe diferente num serviço.** Crie a regra com o profissional e o serviço juntos. Ela vale só para esse par e vence a regra do profissional e a do serviço.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Salvar regra parado:** o botão não libera. **Solução:** confira se **Profissional** e **Serviço** não estão os dois em **Todos** e se o percentual não passa de 100.
