# Mensagens automáticas em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/mensagens-automaticas-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Automação em Configurações › Mensagens automáticas em Configurações

---

🧩 A seção **Mensagens automáticas** guarda os textos que a plataforma envia sozinha em situações específicas: quando o atendimento é encerrado pelo sistema, quando a conversa é encaminhada a um atendente, no aviso que o atendente recebe no WhatsApp pessoal e no aniversário do contato.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Automação**, seção **Mensagens automáticas**.
>
> ➡️ Escreva em cada campo o texto da mensagem correspondente.

## Os campos, na ordem da tela

🔘 **Mensagem Saída Forçada:** enviada quando o atendimento é encerrado pelo sistema, não pelo atendente.

🔘 **Mensagem de Encaminhamento:** enviada ao cliente quando a conversa é encaminhada a um atendente — por exemplo, quando o rodízio de atendimento passa a conversa para o atendente sorteado. O texto aceita `{{ms}}`, que vira a saudação do horário (Bom dia, Boa tarde…), e `{{name}}`, o nome do cliente: com `{{ms}} *{{name}}*, em alguns instantes um atendente irá prosseguir com seu atendimento.`, a cliente Maria recebe pela manhã *"Bom dia Maria, em alguns instantes um atendente irá prosseguir com seu atendimento."*

🔘 **Mensagem de Notificação Externa:** o texto do aviso que o **atendente** recebe no WhatsApp pessoal quando o Setor tem **Notificar Operador no WhatsApp** ligado — por exemplo, quando o rodízio de atendimento entrega uma conversa a ele. Um exemplo de texto: *"Existe atendimento aguardando sua atenção na plataforma."* O aviso vai para o telefone cadastrado no usuário, no menu **Equipe**.

🔘 **Mensagem de Aniversário (enviada todos os dias às 10 horas, no fuso da empresa):** o texto da felicitação que a plataforma envia sozinha no dia do aniversário de cada contato com data de nascimento preenchida. Vazio, nada é enviado. O fuso é o escolhido em **Fuso horário da empresa**, no menu **Configurações  ›  Opções  ›  Geral**, seção **Empresa e região**.

⚠️ A **Mensagem de Aniversário** depende de o contato ter a **data de nascimento** preenchida na ficha, no menu **Contatos  ›  editar o contato**. Sem a data, o contato não entra na rotina.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Escrevi a Mensagem de Aniversário e ninguém recebeu.** Confira se os contatos têm data de nascimento cadastrada, e lembre que o envio acontece só às 10 horas, no fuso da empresa — não na hora em que você salva.
>
> **Onde mudo a mensagem que o cliente recebe quando o rodízio passa a conversa para um atendente?** Em **Mensagem de Encaminhamento**, nesta seção. O texto vale para toda a empresa.
>
> **Onde mudo o texto do aviso que o atendente recebe no WhatsApp?** Em **Mensagem de Notificação Externa**, nesta seção. O aviso só é enviado quando o Setor tem **Notificar Operador no WhatsApp** ligado e o usuário tem telefone cadastrado no menu **Equipe**, no padrão DDI + DDD + número.
