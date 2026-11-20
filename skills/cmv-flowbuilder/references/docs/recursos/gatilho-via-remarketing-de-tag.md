# Gatilho via Remarketing de Tag

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gatilho-via-remarketing-de-tag
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Pontos de Entrada (Gatilho) › Gatilho via Remarketing de Tag

---

🧩 O **Gatilho via Remarketing de Tag** é o ponto de entrada por tempo: assim que uma tag é colocada na conversa, o sistema espera o período configurado e então dispara o fluxo.

☑️ **Recuperação de vendas:** o cliente parou de responder, o atendente coloca a tag *Aguardando retorno* e o robô manda *"Oi, ficou alguma dúvida?"* 30 minutos depois.

☑️ **Follow-up e pós-venda:** a tag é colocada no fim do atendimento, ou o atendente encerra escolhendo uma tag do tipo **Encerramento**, e o robô envia uma pesquisa de satisfação ou um material complementar 24 horas depois, mesmo com o atendimento já encerrado.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Tags** e, ao criar ou editar uma tag, escolha o fluxo e o tempo na aba **Remarketing**.

## Como configurar o remarketing de tag

### Passo 1: o fluxo

Acesse o menu **FlowBuilder Nativo** e monte o fluxo.

### Passo 2: a tag

Acesse o menu **Tags** para criar ou editar uma tag.

Na aba **Remarketing**, escolha o fluxo no campo **Fluxos de Automação** e configure **quando** o fluxo é disparado depois que a tag é colocada na conversa. O menor prazo do campo **Quando?** é **A partir de 5 minutos**.

Ainda na aba **Remarketing**, o campo **Setor do atendimento reaberto** escolhe em qual Setor o atendimento encerrado volta quando o prazo da tag vence: um dos Setores da empresa ou a opção **O da conexão (ou o de antes)**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Se a tag for removida antes do tempo, o fluxo é enviado?** Não. Se a tag é colocada e removida antes do tempo configurado, o gatilho é cancelado e o fluxo não roda.
>
> **Tirei a tag e coloquei de novo. O prazo recomeça?** Sim. O prazo conta da última vez que a tag foi colocada, e o fluxo é enviado uma vez só.
>
> **O remarketing funciona para tags colocadas à mão e por automação?** Funciona para qualquer marcação, feita pelo atendente ou por outro processo do sistema, com o atendimento aberto ou já encerrado.
>
> **O atendimento foi encerrado antes do prazo do remarketing. O fluxo é enviado?** Sim. A tag de atendimento, colocada à mão pelo atendente ou pelo fluxo, dispara mesmo com o atendimento encerrado: o atendimento é reaberto no **Aguardando**, sem atendente, no Setor escolhido em **Setor do atendimento reaberto**, e o fluxo do remarketing é enviado. A tag do tipo **Encerramento**, escolhida na hora de encerrar, também dispara: o fluxo do remarketing é enviado e o atendimento continua encerrado.
>
> **Em que Setor o atendimento reaberto pelo remarketing aparece para a equipe?** No Setor escolhido no campo **Setor do atendimento reaberto**, na aba **Remarketing** da tag.
>
> **Posso ter vários remarketings ao mesmo tempo?** Pode. Um cliente pode ter a tag *Boleto Pendente*, que dispara em 1 dia, e a tag *Cliente VIP*, que dispara em 1 mês. Os prazos correm em paralelo.
>
> **O fluxo do remarketing passa por cima do atendimento?** Sim. Se o cliente estiver conversando com um atendente quando o remarketing disparar, o robô pode atropelar a conversa, e o atendimento continua em **Atendendo**.
>
> **Por que alguns blocos não funcionam no fluxo do remarketing?** Alguns blocos só funcionam com a conversa no **Aguardando**. Se o remarketing disparar com o atendimento em **Atendendo**, esses blocos podem travar a automação. Use o bloco **Trocar Fluxo** no começo do fluxo para levar a conversa ao **Aguardando**, onde os blocos funcionam. ⚠️ A conversa sai das mãos da equipe.
