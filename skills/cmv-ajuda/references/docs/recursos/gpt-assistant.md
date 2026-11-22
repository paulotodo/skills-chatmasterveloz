# GPT Assistant

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gpt-assistant
- **Categoria:** Recursos
- **Menu:** Inteligência Artificial › GPT Assistant

---

🧩 Sua equipe responde as mesmas perguntas o dia inteiro, e o cliente espera minutos por uma resposta simples? O **GPT Assistant** coloca uma IA para conversar com o cliente, com o tom, as informações e os limites que você definir, e transfere o atendimento para a equipe quando o cliente pede uma pessoa.

Tudo começa no **prompt**: as instruções que dizem como a IA fala, o que ela sabe e o que ela pode fazer no atendimento. Para atender o cliente, o prompt é ligado a um **Setor**, no menu **Setores & Chatbot**, campo **Prompt OPEN.AI (ChatGPT)**, e a IA responde as conversas que aguardam nesse Setor.

## Como colocar a IA no atendimento

➡️ **Pelo FlowBuilder Nativo, o caminho recomendado.** O bloco **GPT Assistant (OpenAI)** entrega o atendimento à IA no meio de um fluxo: o campo **Setor com GPT Assistant** lista só os Setores que têm prompt. Com minutos no campo **Sem resposta: seguir pela saída depois de (minutos)**, o bloco ganha a saída **Sem resposta**, e o fluxo segue por ela quando o cliente fica esse tempo sem responder.

➡️ **Direto no Setor.** Sem fluxo, a conversa chega ao Setor da IA pela Conexão ou por transferência, e a IA responde a partir daí.

⚠️ O tipo **Agente OpenAI** aparece desativado na janela do prompt e não funciona mais. Crie a IA com o tipo **Prompt**, com as instruções escritas no próprio campo do prompt.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Uso o FlowBuilder Nativo ou ligo o GPT Assistant direto no Setor?** O FlowBuilder Nativo é o caminho recomendado: o fluxo pode cumprimentar, coletar dados ou mostrar um menu antes de entregar o atendimento à IA, e pode retomar quando o cliente para de responder. Ligado direto no Setor, o prompt responde as conversas que aguardam ali, venham de onde vierem.
