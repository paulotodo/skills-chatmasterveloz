# Intervalo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-intervalo
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Intervalo

---

🧩 O bloco **Intervalo** faz o fluxo esperar antes de seguir para o próximo bloco. É a pausa de quem fala com calma: dá tempo de o cliente ler uma mensagem antes da seguinte chegar, de um sistema externo terminar o que estava fazendo, ou de o fluxo retomar a conversa mais tarde.

A espera vai de 1 segundo a 24 horas, contada em segundos, minutos ou horas, e o cliente não recebe nada durante a pausa. A espera não depende de o FlowBuilder estar aberto.

**🏷️ Categoria: Dados**

Ideal para:

☑️ **Ritmo de leitura:** separa mensagens longas para que não cheguem todas de uma vez.

☑️ **Espera por integração:** dá alguns segundos de folga depois de uma consulta a outro sistema, antes de usar o resultado.

☑️ **Retorno programado:** retoma a conversa minutos ou horas depois, sem ninguém precisar lembrar.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Intervalo**.
>
> ➡️ Informe o **Tempo de espera**, escolha a **Unidade** e clique em **Adicionar**.

## Como configurar o bloco Intervalo

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Intervalo**

🔘 **Tempo de espera:** quanto tempo o fluxo espera antes de seguir, em número inteiro.

🔘 **Unidade:** **Segundos**, **Minutos** ou **Horas**. O bloco Intervalo aceita de 1 segundo a 24 horas: fora disso, a janela avisa *"O intervalo vai de 1 segundo a 24 horas."* e não fecha.

🔘 **Se o cliente responder durante a espera:** **Continuar esperando** ou **Cancelar a espera (o fluxo para aqui)**. Com **Cancelar a espera**, a resposta do cliente para o fluxo ali; com **Continuar esperando**, o fluxo espera o tempo inteiro e segue para o próximo bloco.

⚠️ Nas palavras da janela: *"Se o atendimento for aceito, transferido para um atendente ou encerrado durante a espera, o fluxo não continua."*

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco Intervalo mostra o tempo de um jeito fácil de ler, como *⏱ 2 min 1 s* ou *⏱ 1 h 30 min*, e tem uma saída para o próximo passo.

## A saída Janela expirada

Em alguns canais, a mensagem livre só pode ser enviada até 24 horas depois da última mensagem do cliente, e essa janela pode fechar durante uma espera longa. Por isso, o bloco Intervalo com mais de 2 minutos ganha a saída **Janela expirada**.

Nas palavras da tela: *"Se a janela fechar durante a espera, o fluxo segue pela saída "Janela expirada" — sem ela ligada, para e deixa um aviso no atendimento."* A janela do bloco também diz quanto das 24 horas a espera usa, como *"Esta espera usa 1 h 30 min das 24 horas da janela."*

📌 O bloco **Conteúdo** também tem um item **Intervalo** dentro dele, para pausar entre as mensagens do próprio bloco, de 1 a 120 segundos. Use o bloco **Intervalo** quando a pausa for entre dois blocos.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual o tempo máximo do bloco Intervalo?** 24 horas. O bloco Intervalo aceita de 1 segundo a 24 horas, em segundos, minutos ou horas; fora disso, a janela avisa *"O intervalo vai de 1 segundo a 24 horas."* e não fecha.
>
> **O cliente vê alguma coisa durante o Intervalo?** Não. O fluxo só espera o tempo escolhido e segue para o próximo bloco.
>
> **O fluxo continua se alguém aceitar o atendimento durante o Intervalo?** Não. Se o atendimento for aceito, transferido para um atendente ou encerrado durante a espera, o fluxo para ali, e o bloco seguinte não roda.
>
> **Um bloco Intervalo que eu criei antes, só em segundos, mudou?** Não. Ele abre com o mesmo tempo, na unidade **Segundos**, e com **Continuar esperando**.
>
> **Por que o meu bloco Intervalo ganhou a saída Janela expirada?** Porque a espera passou de 2 minutos. Ligue a saída **Janela expirada** ao bloco que deve rodar quando a janela de 24 horas fechar durante a espera.
>
> **Posso colocar um Intervalo entre a Pergunta e a Variável?** Pode. O **Intervalo** é a única peça que pode ficar entre os dois sem a **Variável** perder a resposta guardada.
>
> **Qual a diferença entre o bloco Intervalo e o Intervalo dentro do bloco Conteúdo?** O do **Conteúdo** pausa entre as mensagens daquele bloco. O bloco **Intervalo** pausa entre um bloco e o seguinte.
