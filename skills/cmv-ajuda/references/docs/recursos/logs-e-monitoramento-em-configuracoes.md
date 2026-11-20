# Logs e Monitoramento em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/logs-e-monitoramento-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Integrações e segurança em Configurações › Logs e Monitoramento em Configurações

---

🧩 A seção **Logs e Monitoramento** liga os registros que a plataforma guarda sobre o que acontece nos atendimentos e nos canais do hub.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Logs e Monitoramento**.
>
> ➡️ Ligue **Registrar Logs de Ação dos Atendimentos?** para ter rastro de quem fez o quê.

## Os campos, na ordem da tela

🔘 **Exibir Logs do HUB?:** o HUB são as conexões pelo NotificaMe. Com **Sim**, quando uma mensagem não é enviada por uma delas, o motivo do erro aparece como nota interna no atendimento.

🔘 **Registrar Logs de Ação dos Atendimentos?:** com **Sim**, cada ação sobre um atendimento — aceitar, transferir, encerrar, marcar — fica registrada com quem executou. É o que alimenta o menu **Registro de Atividades**.

Com **Registrar Logs de Ação dos Atendimentos?** em **Sim**, a conversa também ganha uma linha, só para a equipe, quando alguém aceita ou finaliza o atendimento — *"Fulano aceitou o atendimento"*, *"Fulano finalizou o atendimento"* — e quando o atendimento é aberto ou reaberto, com a origem entre parênteses: *(mensagem recebida)*, quando foi o cliente que voltou a escrever.

Na reabertura, a linha diz também o Setor em que o atendimento voltou — num Setor chamado Atendimento, por exemplo, *"Atendimento reaberto no setor Atendimento (mensagem recebida)"*. Quando a Conexão manda o cliente escolher o Setor num menu, a linha diz *"Atendimento reaberto sem setor (mensagem recebida)"*, porque o Setor ainda vai ser escolhido.

A mesma opção registra também os convites de operador: com **Registrar Logs de Ação dos Atendimentos?** em **Sim**, a própria conversa ganha uma linha, só para a equipe, a cada convite de operador: *"Fulano convidou Beltrano para a conversa"*, *"Fulano removeu Beltrano da conversa"* e, quando o atendimento é finalizado com a remoção dos convidados ligada, *"Beltrano saiu da conversa: o atendimento foi finalizado"*. Com a opção em **Não**, nenhuma dessas linhas aparece.

⚠️ Sem **Registrar Logs de Ação dos Atendimentos?** em **Sim**, o **Registro de Atividades** não guarda as ações sobre os atendimentos — e não há como reconstruir depois o que já passou.

A reabertura é a exceção: quando o cliente volta a escrever num atendimento encerrado, a reabertura entra no menu **Registro de Atividades** como **TICKET_REOPENED**, com a origem, com a opção em **Sim** ou em **Não**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Registro de Atividades não mostra ações de atendimento.** Ligue **Registrar Logs de Ação dos Atendimentos?**. O registro começa a partir do momento em que a opção é ligada.
>
> **Por que a conversa não mostra quem convidou ou removeu um operador?** As linhas de convite só aparecem com **Registrar Logs de Ação dos Atendimentos?** em **Sim**, e só a partir do momento em que a opção é ligada.
>
> **A conversa mostra quem aceitou, quem finalizou e quando o atendimento foi reaberto?** Só com **Registrar Logs de Ação dos Atendimentos?** em **Sim**: a conversa ganha uma linha, só para a equipe, a cada aceite, finalização, abertura e reabertura, e as de abertura e de reabertura trazem a origem; a de reabertura traz também o Setor em que o atendimento voltou. Com a opção em **Não**, nenhuma dessas linhas aparece.
>
> **Com Registrar Logs de Ação dos Atendimentos em Não, a reabertura de um atendimento fica registrada?** Fica. Quando o cliente volta a escrever num atendimento encerrado, a reabertura entra no **Registro de Atividades** como **TICKET_REOPENED**, com a origem, com a opção ligada ou desligada.
