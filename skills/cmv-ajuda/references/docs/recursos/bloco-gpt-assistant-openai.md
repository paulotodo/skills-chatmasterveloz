# GPT Assistant (OpenAI)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-gpt-assistant-openai
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › GPT Assistant (OpenAI)

---

🧩 O bloco **GPT Assistant (OpenAI)** passa a conversa do fluxo para um assistente de inteligência artificial, que responde ao cliente dali em diante. É a troca de turno entre o fluxo de menus e o assistente que entende o que o cliente escreve com as próprias palavras.

O bloco não configura a inteligência artificial. Ele escolhe o **Setor** onde o assistente já está ligado, e o assistente desse Setor assume a conversa.

**🏷️ Categoria: Atendimento - Finalização**

Ideal para:

☑️ **Dúvidas abertas:** depois do menu, leva para o assistente quem tem uma pergunta que não cabe nas opções.

☑️ **Atendimento fora do horário:** deixa o assistente responder quando a equipe não está.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Crie o assistente no menu **Prompts OPEN.AI** e ligue-o a um Setor.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo, clique no **+** e escolha **GPT Assistant (OpenAI)**.
>
> ➡️ Escolha o Setor em **Setor com GPT Assistant** e clique em **Adicionar**.

## Como configurar o bloco GPT Assistant (OpenAI)

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  GPT Assistant (OpenAI)**

🔘 **Setor com GPT Assistant:** o Setor que vai receber a conversa. A lista mostra só os Setores que têm um assistente ligado.

🔘 **Sem resposta: seguir pela saída depois de (minutos):** com minutos preenchidos, o bloco ganha a saída **Sem resposta**, para quem não responder ao assistente nesse tempo. Vazio ou 0 desliga.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco aparece como **GPT Assistant (OpenAI)** e não tem saída: a conversa segue com o assistente. Com **Sem resposta** preenchido, ganha essa saída.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A lista do bloco GPT Assistant está vazia.** Nenhum Setor tem assistente ligado. Crie o assistente no menu **Prompts OPEN.AI** e escolha-o no cadastro do Setor.
>
> **O bloco GPT Assistant cria o assistente?** Não. Ele só leva a conversa ao Setor onde o assistente já está ligado. O comportamento do assistente é configurado no menu **Prompts OPEN.AI**.
>
> **Posso continuar o fluxo depois do bloco GPT Assistant?** Só pela saída **Sem resposta**, quando ela está preenchida. Sem ela, o bloco não tem saída e a conversa fica com o assistente.
