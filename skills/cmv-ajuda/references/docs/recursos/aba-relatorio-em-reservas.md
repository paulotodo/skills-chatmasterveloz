# Aba Relatório em Reservas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-relatorio-em-reservas
- **Categoria:** Recursos
- **Menu:** Reservas › Aba Relatório em Reservas

---

🧩 Quantas reservas o mês teve, quantos clientes faltaram, quanto já entrou e quanto ainda falta receber? A aba **Relatório** responde por período, por oferta e por recurso, e mostra os dias e os horários mais procurados.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Reservas** e abra a aba **Relatório**.
>
> ➡️ Escolha **De** e **Até** e, se quiser, a **Oferta** e o **Recurso**.
>
> ➡️ Clique em **Atualizar**. Para levar os dados para uma planilha, clique em **Exportar CSV**.

## Os filtros

🔘 **De** e **Até:** o período, de 1 a 366 dias. A aba abre nos últimos 30 dias.

🔘 **Oferta** e **Recurso:** **Todas** e **Todos**, ou uma oferta e um recurso.

🔘 **Atualizar:** aplica os filtros. Trocar um filtro sem clicar em **Atualizar** não muda os números.

## Os números

🔘 **Reservas:** as reservas do período, sem as canceladas.

🔘 **Pessoas:** quantas pessoas as reservas somam.

🔘 **Comparecimento** e **Cancelamento:** a parte das reservas que compareceu e a que foi cancelada.

🔘 **Previsto**, **Recebido** e **A receber:** o valor das reservas, o que já foi pago e o que falta.

🔘 **Ticket médio:** o valor médio por reserva.

## Os blocos

🔘 **Por situação:** quantas reservas estão **Pendente**, **Confirmada**, **Concluída**, **Não compareceu** e **Cancelada**.

🔘 **De onde vieram:** quantas reservas vieram de cada origem, como **Equipe** e **API**, mais os pacotes vendidos, os créditos usados e as reservas de séries.

🔘 **Por oferta:** as reservas, as canceladas, o previsto e o recebido de cada oferta.

🔘 **Ocupação:** o tempo reservado de cada recurso. Nas palavras da tela: *"O tempo reservado dividido pelo tempo aberto na grade, já sem os bloqueios. Na diária, as noites reservadas pelos dias do período."*

🔘 **Por dia da semana** e **Por horário de início:** os dias e as horas mais procurados.

🔘 **Clientes:** quantos clientes reservaram, quantos voltaram mais de uma vez e a lista dos que mais reservaram, com o valor.

## Exportar CSV

O arquivo leva as reservas do período e dos filtros da tela, inclusive as canceladas, com as colunas **Código**, **Data**, **Hora**, **Oferta**, **Recurso**, **Cliente**, **Telefone**, **Pessoas**, **Noites**, **Situação**, **Origem**, **Preço**, **Pago**, **Pacote** e **Série**. É um CSV separado por ponto e vírgula, que a planilha abre.

No CSV, a **Situação** e a **Origem** vêm pelo nome, como *Confirmada*, *Não compareceu*, *Equipe*, *Conversa (fluxo)*, *Página de reservas* e *API*. O **Pacote** vem pelo nome do pacote, e a **Série**, pela posição da reserva nela, como *1 de 3*.

## Quando o Atualizar não libera

➡️ *"A data final vem antes da inicial."*

➡️ *"O período vai até 366 dias."*

➡️ *"Escolha as duas datas."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Troquei a oferta e os números não mudaram.** Clique em **Atualizar**: os filtros só valem depois dele.
>
> **O card Reservas mostra menos reservas do que o CSV.** É o esperado: o card **Reservas** conta só as que não foram canceladas, e o CSV leva também as canceladas.
>
> **No CSV das Reservas, o que quer dizer "1 de 3" na coluna Série?** É a posição da reserva na série que se repete: a primeira de três datas.
>
> **Quem vê o Relatório das Reservas?** Os números são do administrador, no menu **Reservas**.
