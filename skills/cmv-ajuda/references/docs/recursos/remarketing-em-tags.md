# Remarketing em Tags

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/remarketing-em-tags
- **Categoria:** Recursos
- **Menu:** Tags › Remarketing em Tags

---

🧩 **Remarketing em Tag (Automação)** permite agendar o disparo automático de um fluxo de mensagens sempre que uma tag for vinculada. É ideal para fazer cobranças, lembretes, follow-ups ou recuperação de vendas sem ação manual.

☑️ **Recuperação de Vendas:** configure o sistema para enviar uma mensagem "E aí, ficou alguma dúvida?" automaticamente 30 minutos após o cliente parar de responder (basta adicionar uma tag como "10min" ou "Aguardando").

☑️ **Follow-up Programado:** envie materiais complementares ou pesquisas de satisfação horas ou dias depois, mesmo com o atendimento já encerrado.

☑️ **Respeito aos Horários:** defina janelas de envio para garantir que sua automação não mande mensagens de remarketing de madrugada ou em finais de semana indesejados.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Tags**.
>
> ➡️ Ao adicionar ou Editar uma tag, na aba “Remarketing”, defina o **Fluxo de Automação, quando e as restrições** de envio.

## Como configurar uma automação de Remarketing de Tag

Acesse o menu **Tags  ›  ícone Lápis da tag  ›  aba Remarketing**

![Formulário de Integração Pixel Meta em Tags](https://clihelper.chatmasterveloz.com/docs-imagem/21117-tags-remarketing-formulario.jpg)**⚡** Na aba **REMARKETING**

**“Automação e Remarketing”:**

🔘 **Fluxos de Automação:** selecione qual fluxo será disparado. *Pré-requisito: o fluxo já deve ter sido criado anteriormente no menu de FlowBuilder.*

🔘 **Quando?:** defina o tempo de espera (delay) entre a marcação da tag e o disparo da mensagem. *Exemplo: "A partir de 10 minutos" significa que o sistema contará 10 minutos após você colocar a tag antes de enviar o fluxo.* O menor prazo é **A partir de 5 minutos**, e as opções sobem de 5 em 5 minutos.

🔘 **Pausar Automaticamente / Reiniciar:** (Janela de Envio) Defina um intervalo de horário permitido para o envio. *Exemplo: Pausar às 22:00 e Reiniciar às 08:00. Se o tempo do disparo cair às 23h, o sistema segura a mensagem e só envia às 08h do dia seguinte.*

🔘 **Enviar em Finais de Semana e Feriados Nacionais:**  
- **Habilitado:** envia a mensagem em qualquer dia.
- **Desabilitado:** se o disparo cair num sábado ou domingo, o sistema aguarda até o próximo dia útil.

🔘 **Setor do atendimento reaberto:** em qual Setor o atendimento encerrado é reaberto quando o prazo da tag vence. A lista traz os Setores da empresa e a opção **O da conexão (ou o de antes)**. Nas palavras da tela: *"Se a tag vencer com o atendimento encerrado, ele é reaberto no Aguardando, neste Setor, e o fluxo dispara."*

🔲 Para finalizar, clique em **Salvar**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Se remover a tag antes do tempo, o fluxo é enviado?** Não. Se você adicionar a tag "10min" e removê-la após 5 minutos, o gatilho é cancelado e o fluxo não é ativado.
>
> **Tirei a tag e coloquei de novo. O prazo recomeça?** Sim. O prazo conta da última vez que a tag foi colocada, e o fluxo é enviado uma vez só.
>
> **Isso funciona para tags marcadas manualmente ou por automação?** Funciona para qualquer marcação, seja manualmente pelo atendente ou automaticamente por outro processo do sistema, com o atendimento aberto ou já encerrado.
>
> **O atendimento foi encerrado antes do prazo do remarketing. O fluxo é enviado?** Sim. A tag de atendimento, colocada à mão pelo atendente ou pelo fluxo, dispara mesmo com o atendimento encerrado: o atendimento é reaberto no **Aguardando**, sem atendente, no Setor escolhido em **Setor do atendimento reaberto**, e o fluxo do remarketing é enviado. A tag do tipo **Encerramento**, escolhida na hora de encerrar, também dispara: o fluxo do remarketing é enviado e o atendimento continua encerrado.
>
> **Em que Setor o atendimento reaberto pelo remarketing aparece para a equipe?** No Setor escolhido no campo **Setor do atendimento reaberto**, na aba **Remarketing** da tag. Escolha o Setor da equipe que deve receber o cliente de volta.
>
> **Posso ter vários remarketings ao mesmo tempo?** Sim. Um mesmo cliente pode ter a tag "Boleto Pendente" (que dispara em 1 dia) e a tag "Cliente VIP" (que dispara em 1 mês). Os cronômetros rodam em paralelo.
>
> **O fluxo substitui o atendimento atual?** Sim. Se o cliente estiver conversando com um atendente e o remarketing disparar, o robô pode “atropelar” a conversa. Porém o status da conversa continua em “Atendimento”.
>
> **Por que alguns blocos não funcionam no fluxo do Remarketing de Tag?** Alguns blocos só funcionam com a conversa em “Aguardando”. Se o Remarketing de Tag for acionado durante um **“Atendimento”**, esses blocos podem travar a automação.
>
> Você pode utilizar o bloco “Trocar de Fluxo” em seu fluxo atual, para que a conversa seja direcionada para o “Aguardando”, onde os blocos funcionam corretamente. **Atenção**: tenha em mente que a conversa sairá do atendimento de sua equipe.
