# Aba Serviços em Cadastros do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-servicos-em-cadastros-do-consultorio
- **Categoria:** Recursos
- **Menu:** Consultório › Aba Serviços em Cadastros do Consultório

---

🧩 A aba **Serviços** cadastra o que a clínica oferece: a consulta, o retorno, a avaliação. A duração de cada serviço é o que divide a agenda em horários.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Consultório  ›  Cadastros do consultório** e abra a aba **Serviços**.
>
> ➡️ Clique em **Adicionar serviço**, preencha **Serviço**, **Duração (min)** e **Preço (R$)**.
>
> ➡️ Escolha a **Modalidade** e quem atende, e clique em **Salvar**.

## Os campos

🔘 **Serviço:** o nome, como aparece na marcação e na agenda. Nome repetido é recusado, mesmo com maiúsculas e minúsculas diferentes: *"Já existe um serviço com este nome. Escolha outro nome."*

🔘 **Duração (min):** de 5 a 480 minutos. É o tamanho de cada horário na agenda; fora desse intervalo, o **Salvar** não libera.

🔘 **Preço (R$):** de 0 a 999.999,99. É o valor que a cobrança da consulta usa, e pode ser trocado em cada consulta.

🔘 **Modalidade:** **Presencial**, **Teleconsulta** ou **Presencial ou teleconsulta**. A teleconsulta aparece quando disponível no seu plano.

🔘 **Quem atende:** os profissionais que fazem o serviço. Vazio, vale para todos. Na marcação, cada profissional mostra só os serviços que atende.

🔘 **Descrição:** o que o serviço inclui, até 2.000 caracteres.

🔘 **Ativo:** desmarcado, o serviço sai das novas consultas.

🔘 **Aceita marcação pela API (atendente de IA):** desmarcado, a integração da clínica não marca este serviço. Marcado, aparecem dois campos só deste serviço:  
- **Antecedência pela API, só deste serviço (minutos)** — vazio, vale a regra da clínica;
- **Até quantos dias à frente pela API, só deste serviço** — vazio, vale a regra da clínica; **0** é sem limite.

## A lista

A aba mostra cada serviço com **Serviço**, **Duração**, **Preço**, **Modalidade**, **Quem atende** e **Situação**, e os botões para editar e remover. Serviço com consultas na agenda não é removido: desative-o.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O serviço não aparece na hora de marcar a consulta.** Confira **Quem atende**: o serviço só aparece para os profissionais escolhidos ali. Confira também se ele está **Ativo**.
>
> **Uma consulta precisa de um valor diferente do Preço do serviço.** Troque o valor na própria consulta, na cobrança dela. O **Preço (R$)** do serviço continua o mesmo para as outras.
>
> **Como faço um serviço que a recepção marca, mas a integração não?** Desmarque **Aceita marcação pela API (atendente de IA)** no serviço.
