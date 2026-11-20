# Aba Marcação em Cadastros do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-marcacao-em-cadastros-do-consultorio
- **Categoria:** Recursos
- **Menu:** Consultório › Aba Marcação em Cadastros do Consultório

---

🧩 A aba **Marcação** define as regras de tempo da agenda: com quanta antecedência e até quantos dias à frente uma consulta pode ser marcada. Há uma regra para a recepção, na tela, e outra para quem marca de fora, pela integração da clínica.

Os horários livres seguem as mesmas regras. Nas palavras da tela: *"o que eles escondem, a marcação recusa."*

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Consultório  ›  Cadastros do consultório** e abra a aba **Marcação**.
>
> ➡️ Preencha **Antecedência mínima (minutos)** e **Até quantos dias à frente** em **Na tela (recepção)** e em **Pela API (integração e atendente de IA)**.
>
> ➡️ Clique em **Salvar**.

## Os campos

🔘 **Antecedência mínima (minutos):** o mínimo entre agora e o horário da consulta. De 0 a 43.200 minutos. Na recepção, **0** deixa marcar para daqui a pouco.

🔘 **Até quantos dias à frente:** o máximo de dias à frente em que a agenda aceita consulta. De 0 a 730; **0** é sem limite.

## Na tela e pela API

**Na tela (recepção)** vale para quem marca pela **Agenda**. Uma data além do limite é recusada: *"Esta data está longe demais: a agenda ainda não está aberta para ela."* — e a marcação explica quantos dias a recepção pode marcar.

**Pela API (integração e atendente de IA)** vale para quem marca de fora. Cada serviço pode ter a regra dele, no cadastro do serviço; o serviço sem regra própria usa esta.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A recepção não consegue marcar uma consulta para daqui a quatro meses.** Confira **Até quantos dias à frente** em **Na tela (recepção)**: a data passou do limite. Aumente o número ou deixe **0** para não ter limite.
>
> **Um serviço precisa de mais antecedência que os outros na marcação de fora.** Preencha a antecedência no próprio serviço, na aba **Serviços**. Ela vale só para ele, e os outros seguem a regra da aba **Marcação**.
