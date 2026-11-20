# Gerenciamento de Expediente em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gerenciamento-de-expediente-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Geral em Configurações › Gerenciamento de Expediente em Configurações

---

🧩 A seção **Gerenciamento de Expediente** liga o controle de horário de atendimento dos Setores — que depois é preenchido, dia a dia, na aba Horários de cada Setor — e guarda o horário de trabalho padrão da equipe, no subtítulo **Expediente dos usuários**.

O fuso horário que vale para o expediente não fica aqui: é o **Fuso horário da empresa**, na seção **Empresa e região**, na mesma aba **Geral**.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Geral**, seção **Gerenciamento de Expediente**.
>
> ➡️ Confira o **Fuso horário da empresa**, na seção **Empresa e região** da mesma aba.
>
> ➡️ Em **Gerenciamento de Expediente**, escolha **Gerenciamento Por Setor** para destravar a aba Horários dos Setores.
>
> ➡️ Para um horário de trabalho igual para a equipe, em **Expediente dos usuários**, ligue o **Horário padrão para todos os usuários**, preencha a semana e clique em **SALVAR EXPEDIENTE**.

## Os campos, na ordem da tela

🔘 **Gerenciamento de Expediente:** **Desabilitado** ou **Gerenciamento Por Setor**. É esta opção que faz a aba **Horários** aparecer preenchível no cadastro de cada Setor; desabilitada, a aba mostra só um aviso.

🔘 **Abrir Atendimentos Fora do Expediente?:** define o que acontece com a mensagem que chega fora do horário configurado.

⚠️ O horário de cada Setor não fica aqui. Aqui você **liga** o controle por Setor; os dias e faixas de cada Setor ficam no menu **Setores & Chatbot  ›  editar o Setor  ›  aba Horários**.

## Expediente dos usuários

O subtítulo **Expediente dos usuários** aparece só para o administrador. É onde a empresa define um horário de trabalho padrão para a equipe: com ele ligado, o atendente só entra no painel dentro do horário.

🔘 **Horário padrão para todos os usuários:** ligado, abre a semana, uma linha por dia, com **Dia da Semana**, **Hora Inicial** e **Hora Final**, de 10 em 10 minutos. Nas palavras da tela: *"Vale para quem não tem horário próprio no cadastro. Quem tem, continua com o seu. O atendente só entra no painel dentro do horário."*

🔘 **Adicionar outro intervalo de trabalho:** o botão de cada dia, que divide o dia em mais de uma faixa — por exemplo, das 8h às 12h e das 14h às 18h.

🔘 **Status automático pelo expediente:** nas palavras da tela: *"Ligado: fora do expediente (fim do dia, intervalo, folga), o atendente fica offline sozinho; no começo do expediente, volta a online se estiver com o painel aberto. Desligado: o status é o que cada um escolhe."*

🔘 **SALVAR EXPEDIENTE:** grava o horário padrão e o status automático, com o aviso *"Expediente salvo."*

Fora do horário padrão, o atendente que tenta entrar recebe o aviso *"Acesso fora do horário permitido!"*. Quem já estava com o painel aberto continua dentro: o horário barra a entrada, não derruba quem está trabalhando.

⚠️ O horário próprio do usuário vence o padrão. Quem tem **Horário de Trabalho** preenchido no cadastro, no menu **Equipe  ›  editar o usuário  ›  aba Geral**, continua com o seu; o **Horário padrão para todos os usuários** vale para os outros.

⚠️ O **SALVAR EXPEDIENTE** recusa o horário padrão ligado com a semana vazia — *"Ligue o horário padrão só com algum horário preenchido."* — e o dia preenchido pela metade — *"Confira o horário de trabalho: cada dia precisa do horário inicial e do final, ou ficar em branco."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A aba Horários do Setor está vazia, só com um aviso.** É o comportamento esperado com **Gerenciamento de Expediente** em **Desabilitado**. Troque para **Gerenciamento Por Setor**.
>
> **Onde escolho o fuso horário do expediente?** No **Fuso horário da empresa**, na seção **Empresa e região**, na mesma aba **Geral**. Esse fuso vale também para agendamentos e campanhas, não só para o expediente: ajuste antes de programar envios.
>
> **Liguei o Horário padrão para todos os usuários. Quem tem horário próprio no cadastro muda?** Não. Nas palavras da tela, *"Quem tem, continua com o seu"*: o horário padrão vale só para quem não tem horário próprio.
>
> **O horário padrão acabou e o atendente estava trabalhando. Ele cai?** Não. O horário barra a entrada: quem já estava com o painel aberto continua; fora do horário, o atendente que tenta entrar recebe *"Acesso fora do horário permitido!"*.
