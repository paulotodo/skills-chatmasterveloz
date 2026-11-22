# Gatilho via Resposta Rápida

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gatilho-via-resposta-rapida
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Pontos de Entrada (Gatilho) › Gatilho via Resposta Rápida

---

🧩 O **Gatilho via Resposta Rápida** permite ao atendente chamar um fluxo no meio da conversa. Diferente dos outros pontos de entrada, que são automáticos, aqui a decisão de chamar o robô é **do atendente**.

Ideal para:

☑️ **Coleta de dados repetitiva:** em vez de perguntar item por item, o atendente digita `/cadastro` e o robô faz as perguntas do cadastro.

☑️ **Padronização:** apresentações, explicações longas e contratos chegam sempre iguais.

☑️ **Tempo da equipe:** o que era digitado a cada atendimento passa a ser feito pelo fluxo.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Respostas Rápidas** e, ao criar ou editar uma resposta rápida, escolha o fluxo no campo **Fluxo de Automação**.

## Como configurar o fluxo por resposta rápida

### Passo 1: o fluxo

Acesse o menu **FlowBuilder Nativo** e monte o fluxo.

📌 O último bloco desse fluxo deve ser o **Encerrar Mensagem Rápida**, que devolve a conversa ao atendente, ou o **Trocar Fluxo**.

### Passo 2: a resposta rápida

Acesse o menu **Respostas Rápidas** para criar ou editar uma resposta rápida e escolha o fluxo no campo **Fluxo de Automação**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O atendimento fecha quando eu chamo o fluxo pela resposta rápida?** Não. O atendimento continua aberto com o atendente, mas quem fala é o robô.
>
> **O atendente pode interromper o robô da resposta rápida?** Com o fluxo rodando em **Atendendo**, o atendente não consegue pausar. Se o fluxo estiver no **Aguardando**, por exemplo depois de um **Trocar Fluxo**, o atendente pausa ao puxar o atendimento de novo.
>
> **Por que alguns blocos não funcionam no fluxo da resposta rápida?** Alguns blocos só funcionam com a conversa no **Aguardando**. Use o bloco **Trocar Fluxo** para levar a conversa ao **Aguardando**, onde os blocos funcionam. ⚠️ A conversa sai das mãos da equipe.
