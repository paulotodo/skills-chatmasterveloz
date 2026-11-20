# Aba Confirmação em Cadastros do Consultório

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-confirmacao-em-cadastros-do-consultorio
- **Categoria:** Recursos
- **Menu:** Consultório › Aba Confirmação em Cadastros do Consultório

---

🧩 A aba **Confirmação** prepara a mensagem que a clínica envia ao paciente antes da consulta, com os botões **Confirmar**, **Remarcar** e **Cancelar**. O clique do paciente muda a consulta sozinho, ele recebe a resposta e o atendimento ganha uma nota. Na mesma aba ficam os **lembretes automáticos**, que vão sozinhos antes da consulta, com os mesmos botões.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Consultório  ›  Cadastros do consultório** e abra a aba **Confirmação**.
>
> ➡️ Ajuste a **Mensagem da consulta**, os botões e as respostas, ou deixe em branco para usar o texto padrão.
>
> ➡️ Escolha a **Conexão** e o que acontece **Ao enviar**, e clique em **Salvar**.
>
> ➡️ Em **Lembretes automáticos**, clique em **Adicionar lembrete** para cada aviso antes da consulta.

## A mensagem e as respostas

Os textos aceitam as variáveis da consulta, que aparecem na própria aba: `{{paciente}}`, `{{data}}`, `{{hora}}`, `{{diaDaSemana}}`, `{{profissional}}`, `{{servico}}`, `{{local}}`, `{{clinica}}` e `{{link}}`. Campo em branco volta ao texto padrão.

🔘 **Mensagem da consulta:** o texto que acompanha os botões.

🔘 **Botão Confirmar**, **Botão Remarcar** e **Botão Cancelar:** o texto de cada botão, com até 20 letras.

🔘 **Resposta quando o paciente confirma**, **quando pede para remarcar** e **quando cancela:** o que o paciente recebe depois do clique.

🔘 **Resposta quando a consulta já não pode mudar:** o que o paciente recebe ao clicar depois que a consulta já começou ou já mudou.

## O que cada botão faz

🔘 **Cancelar: perguntar antes se o paciente tem certeza:** marcado, o **Cancelar** não cancela na hora: o paciente recebe uma pergunta, com um botão para confirmar o cancelamento e outro para manter a consulta.

🔘 **Remarcar: abrir o atendimento no setor:** o Setor para onde vai o paciente que pede para remarcar, com a consulta ainda marcada, para a recepção combinar o novo horário. **Só avisar a equipe com a nota no atendimento** não abre atendimento: só registra o pedido.

## Por onde a confirmação é enviada

🔘 **Conexão:** a Conexão por onde a confirmação e os lembretes são enviados. A lista traz só as Conexões ativas da empresa, e a do Chat Externo não entra. **A do atendimento do paciente** usa a Conexão da conversa dele. Escolher outra Conexão serve, por exemplo, para atender por um número e enviar os avisos por outro; a resposta do paciente chega pela Conexão por onde o aviso foi enviado.

🔘 **Usar um modelo aprovado da API oficial:** na conexão oficial, fora da janela de 24 horas só é enviada mensagem por modelo aprovado. Marcado, a aba pede o modelo e liga cada variável dele a uma informação da consulta. Na conexão por QR Code, vai o texto de sempre.

## Ao enviar

🔘 **Atendimento:** **Não abrir atendimento** envia a mensagem e nada entra em espera até o paciente responder. **Abrir atendimento** abre a conversa num Setor: nas palavras da tela, *"Se a conversa do paciente estiver encerrada, ela abre neste setor. Se já houver um atendimento aguardando ou aberto, a mensagem entra nele e nada muda."*

🔘 **Setor**, **Status** e **Usuário:** com **Abrir atendimento**, o Setor da conversa, o status — **Aguardando** ou **Em atendimento** — e, em **Em atendimento**, o usuário que fica com ela. **Sem usuário (o setor distribui)** deixa a distribuição com o Setor.

🔘 **Quando o paciente responder, mandar para o setor:** o Setor que recebe a resposta do paciente, onde está quem cuida das consultas. Vale por 7 dias depois do envio. **O de sempre** segue o caminho normal da Conexão.

## Lembretes automáticos

Cada lembrete é enviado uma vez só, antes da consulta, com os mesmos botões da confirmação. São até 6 por consulta, cada um com o seu prazo; se a consulta for remarcada, os lembretes são refeitos para o novo horário.

🔘 **Nome:** como a equipe reconhece o lembrete, como *1 dia antes*. Só a equipe vê.

🔘 **Quanto antes** e **Em:** o prazo — de 5 a 1.440 minutos, de 1 a 720 horas ou de 1 a 30 dias antes. Em dias, o lembrete tem também a **Hora do envio**.

🔘 **Serviços:** os serviços que recebem o lembrete. Nenhum marcado vale para todos.

🔘 **Quem recebe:** as consultas **Agendada**, **Confirmada** ou as duas.

🔘 **Por onde o lembrete é enviado:** a Conexão das confirmações, a do atendimento do paciente ou uma Conexão fixa — com uma reserva para quando a escolhida estiver desconectada.

🔘 **Texto:** o texto do lembrete, com as mesmas variáveis. Em branco, vai o texto padrão.

🔘 **Ao enviar:** o mesmo bloco da confirmação, só para este lembrete.

⚠️ Quem marca a consulta depois da hora de um lembrete não recebe aquele lembrete, só os que ainda cabem.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Onde a recepção envia a confirmação da consulta?** No painel do contato, na seção **Consultório**, no botão **Enviar a confirmação ao paciente (Confirmar, Remarcar, Cancelar)** da consulta.
>
> **O paciente clicou em Remarcar. A consulta foi desmarcada?** Não. Com **Remarcar: abrir o atendimento no setor**, o paciente vai para o Setor escolhido com a consulta ainda marcada, para a recepção combinar o novo horário.
>
> **Quantos lembretes automáticos posso ter?** Até 6. Cada um é enviado uma vez por consulta, no prazo dele.
>
> **O lembrete precisa abrir um atendimento?** Não precisa. Com **Não abrir atendimento**, ele é enviado e a conversa só volta para a equipe quando o paciente responde. Com **Abrir atendimento**, a conversa entra no Setor escolhido.
