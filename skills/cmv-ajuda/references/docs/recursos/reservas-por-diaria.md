# Reservas por Diária

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/reservas-por-diaria
- **Categoria:** Recursos
- **Menu:** Reservas › Reservas por Diária

---

🧩 Pousada, hotel, chalé ou sala alugada por dia não trabalham com horário de 30 minutos: trabalham com noites. A **oferta por diária** reserva o recurso da data de entrada até a de saída, cobra por noite e mostra ao cliente só as noites livres.

Ideal para:

☑️ **Hospedagem:** quartos e chalés com entrada à tarde e saída no fim da manhã.

☑️ **Estadia mínima:** o feriado que só aceita reservas de três noites ou mais.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No menu **Reservas**, aba **Ofertas**, clique em **Adicionar oferta** e escolha **Por diária** em **Tipo de reserva**.
>
> ➡️ Preencha **Entrada (check-in)**, **Saída (check-out)**, **Mínimo de noites**, **Máximo de noites** e **Preço da diária (por noite)**.
>
> ➡️ Escolha o quarto em **Quem atende / onde** e clique em **Salvar**.

## Como a diária funciona

A diária não usa a grade de horários da aba **Horários**. Nas palavras da tela: *"O que fecha uma data é um bloqueio ou outra estadia."*

🔘 **Entrada e saída:** toda estadia começa no horário de **Entrada (check-in)** do dia da entrada e termina no horário de **Saída (check-out)** do dia da saída.

🔘 **Noites:** o cliente fica entre o **Mínimo de noites** e o **Máximo de noites** da oferta.

🔘 **Preço:** o **Preço da diária (por noite)** vezes as noites, quando a oferta não tem **Tarifas por dia**. Três noites de R$ 200,00 dão R$ 600,00.

🔘 **Tarifas por dia:** com elas na oferta, a estadia soma o preço de cada noite. A noite de um dia da semana com preço próprio, ou de uma data especial, vale esse preço, e o bloco **Estadia** da **Nova reserva** já mostra o total. O quarto de R$ 250,00 a noite, com a sexta a R$ 300,00, o sábado a R$ 320,00 e a data especial 22/11, um domingo, a R$ 400,00, cobra a estadia de 20/11 a 23/11 por R$ 300,00 + R$ 320,00 + R$ 400,00, ou R$ 1.020,00.

🔘 **Sinal:** o sinal de valor fixo vale uma vez por estadia, seja qual for o número de noites. O percentual é calculado sobre uma noite.

🔘 **Saída e entrada no mesmo dia:** o hóspede que sai e o que entra no mesmo quarto, no mesmo dia, não se chocam: as duas estadias são aceitas.

## Na Agenda de reservas

Na **Nova reserva** de uma diária, a equipe escolhe **Entrada**, **Saída**, **Pessoas** e **Recurso**. O bloco **Estadia** mostra a conta antes de salvar, como *"3 noite(s) · total R$ 600,00 · entrada às 14:00, saída às 12:00"*.

Na visão **Semana**, a estadia aparece em cada um dos dias dela, com as datas de entrada e de saída, como *18/11 → 21/11*.

A diária não tem a opção **Repetir esta reserva**, e as ofertas por diária ficam fora dos pacotes.

## Na página de reservas

O cliente lê *"Escolha o dia da entrada"*, com os horários de entrada e saída, e depois *"Agora escolha o dia da saída"*. As noites ocupadas aparecem desligadas. Com as duas datas, a página mostra o total, como *"De 25/11 a 27/11 · 2 noite(s) · total R$ 400,00"*.

## Os avisos da diária

Os avisos ao cliente aceitam `{{dataSaida}}` e `{{noites}}`. Acrescente as duas ao texto do aviso, no menu **Reservas**, aba **Avisos**, para o hóspede receber a data de saída e as noites, e não só a entrada.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O quarto está livre, mas a página não deixa escolher a data.** Confira os bloqueios do quarto no menu **Reservas**, aba **Bloqueios**, e se outra estadia ocupa aquela noite. Na diária, só os dois fecham uma data.
>
> **O cliente quer ficar mais noites do que a oferta permite.** A estadia é recusada fora do **Mínimo de noites** e do **Máximo de noites**. Ajuste os dois na oferta, no menu **Reservas**, aba **Ofertas**.
>
> **Preciso cadastrar horários para o quarto na aba Horários?** Não. A oferta por diária não usa a grade: basta o quarto em **Quem atende / onde**.
