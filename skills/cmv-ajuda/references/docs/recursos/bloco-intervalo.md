# Intervalo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-intervalo
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Intervalo

---

🧩 O bloco **Intervalo** faz o fluxo esperar alguns segundos antes de seguir para o próximo bloco. É a pausa de quem fala com calma: dá tempo de o cliente ler uma mensagem antes da seguinte chegar, e de um sistema externo terminar o que estava fazendo.

O tempo é contado em segundos, até no máximo **120 segundos**, e o cliente não recebe nada durante a pausa.

**🏷️ Categoria: Dados**

Ideal para:

☑️ **Ritmo de leitura:** separa mensagens longas para que não cheguem todas de uma vez.

☑️ **Espera por integração:** dá alguns segundos de folga depois de uma consulta a outro sistema, antes de usar o resultado.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Intervalo**.
>
> ➡️ Informe o **Tempo em segundos**, até 120, e clique em **Adicionar**.

## Como configurar o bloco Intervalo

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Intervalo**

🔘 **Tempo em segundos:** quanto tempo o fluxo espera antes de seguir. O máximo é **120 segundos**: com um valor maior, a janela avisa *Máximo de tempo atingido 120 segundos* e não adiciona o bloco.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco mostra o tempo escolhido, como *Intervalo 3 segundos*, e tem uma saída para o próximo passo.

📌 O bloco **Conteúdo** também tem um item **Intervalo** dentro dele, para pausar entre as mensagens do próprio bloco. Use o bloco **Intervalo** quando a pausa for entre dois blocos.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual o tempo máximo do bloco Intervalo?** 120 segundos. Com um valor maior no **Tempo em segundos**, a janela avisa *Máximo de tempo atingido 120 segundos* e o bloco não é adicionado.
>
> **O cliente vê alguma coisa durante o Intervalo?** Não. O fluxo só espera o tempo escolhido e segue para o próximo bloco.
>
> **Posso colocar um Intervalo entre a Pergunta e a Variável?** Pode. O **Intervalo** é a única peça que pode ficar entre os dois sem a **Variável** perder a resposta guardada.
>
> **Qual a diferença entre o bloco Intervalo e o Intervalo dentro do bloco Conteúdo?** O do **Conteúdo** pausa entre as mensagens daquele bloco. O bloco **Intervalo** pausa entre um bloco e o seguinte.
