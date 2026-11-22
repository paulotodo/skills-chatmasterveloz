# Setor Único com Fluxo Automático

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/setor-unico-com-fluxo-automatico
- **Categoria:** Recursos
- **Menu:** Setores & Chatbot › Setor Único com Fluxo Automático

---

🧩 Quando a Conexão aponta para **um único Setor**, o cliente não escolhe nada: a conversa vai direto para lá. E se esse Setor tiver um fluxo vinculado, quem recebe o cliente é o fluxo — com as perguntas, condições e respostas que você desenhou.

A diferença em relação ao menu é onde a decisão acontece. No menu, o cliente decide digitando um número. Aqui, o fluxo decide: ele pergunta o que precisa, entende a resposta e encaminha.

Ideal para:

☑️ **Triagem por conversa:** o fluxo pergunta em linguagem normal em vez de exigir que o cliente escolha entre opções numeradas.

☑️ **Atendimento com regra:** o fluxo consulta um dado, verifica um horário ou aplica uma condição antes de decidir o destino.

☑️ **Automação que resolve sozinha:** parte dos atendimentos termina dentro do fluxo, sem chegar a um atendente.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Monte o fluxo em **FlowBuilder Nativo**.
>
> ➡️ No menu **Setores & Chatbot**, edite o Setor e escolha o fluxo no campo **Fluxos de Automação**, na aba Geral.
>
> ➡️ No menu **Conexões**, edite a Conexão, abra a aba **Setores & Tempos** e marque **apenas esse Setor**.

## As três peças, na ordem

O caminho tem três etapas, e ele só funciona com as três. É comum montar o fluxo, achar que acabou, e não entender por que nada acontece — falta amarrar as outras duas.

⚡ **O fluxo**, montado em **FlowBuilder Nativo**. É o roteiro: o que perguntar, o que fazer com a resposta, quando chamar um humano.

⚡ **O vínculo com o Setor**, no campo **Fluxos de Automação** da aba Geral do Setor. É o que diz ao sistema que aquele fluxo pertence àquele Setor.

⚡ **O vínculo com a Conexão**, na aba **Setores & Tempos** da Conexão. É o que faz a conversa chegar ao Setor.

⚠️ Marcar **um único** Setor na Conexão é o que caracteriza este caminho. Com dois ou mais marcados, quem recebe o cliente é o menu do chatbot, que pede para ele escolher um Setor, e o fluxo deixa de ser a primeira coisa que ele encontra.

## Como amarrar o fluxo ao Setor

Acesse o menu **Setores & Chatbot  ›  editar o Setor  ›  aba Geral**

🔘 **Fluxos de Automação:** escolhe qual fluxo do construtor atende as conversas deste Setor.

Um Setor tem um fluxo. Para usar fluxos diferentes, use Setores diferentes.

## Como apontar a Conexão para o Setor

Acesse o menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**

🔘 **Setores:** marque **apenas o Setor** que tem o fluxo. O campo aceita vários, mas marcar mais de um muda o comportamento: passa a existir menu.

## Quando o fluxo começa

O fluxo do Setor começa quando chega uma mensagem do cliente com a conversa naquele Setor. Com a Conexão apontando só para ele, isso acontece já na **primeira mensagem**: o cliente escreve e o fluxo responde.

Quando a conversa chega ao Setor de outro jeito — escolhida num menu ou transferida por um atendente —, o fluxo do Setor começa na **próxima mensagem** que o cliente enviar.

## A saudação do Setor e a mensagem do fluxo se somam

O fluxo normalmente já cumprimenta o cliente antes de encaminhá-lo. Se o Setor também tiver uma **Mensagem de saudação** preenchida, na aba Mensagens, o cliente recebe **as duas** logo na primeira mensagem.

A diferença entre elas é o alcance. A mensagem que está dentro do fluxo só existe enquanto o fluxo roda. A **Mensagem de saudação do Setor** pertence ao Setor: é enviada quando o cliente chega a ele pela Conexão, com ou sem fluxo.

⚠️ Neste modo, o normal é **deixar a saudação do Setor vazia** e fazer o cumprimento dentro do fluxo, onde você controla o momento e o texto. Preencher as duas duplica as boas-vindas para o cliente.

## Próximo Passo

🧭 Testar mandando uma mensagem pela Conexão e acompanhando se o fluxo responde.

🧭 Usar o botão **Verificar**, dentro do editor do fluxo, para encontrar erros antes de deixá-lo no ar.

🧭 Cadastrar os atendentes do Setor no menu **Equipe  ›  editar o usuário** — o fluxo eventualmente passa a conversa para uma pessoa, e ela precisa existir.

🧭 Conferir se a **Mensagem de saudação** do Setor está vazia, na aba Mensagens. Ver o aviso acima.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Montei o fluxo e nada acontece quando mando mensagem. Por quê?** Faltou uma das amarrações. O fluxo precisa estar escolhido no campo **Fluxos de Automação** do Setor, e esse Setor precisa estar marcado na aba **Setores & Tempos** da Conexão. Sem as duas, o fluxo existe mas nunca é chamado.
>
> **Transferi um atendimento para um Setor que tem fluxo. Quando o fluxo começa?** Na próxima mensagem que o cliente enviar. O fluxo do Setor começa quando chega mensagem do cliente com a conversa naquele Setor.
>
> **Posso ter mais de um fluxo no mesmo Setor?** Não. O campo aceita um fluxo por Setor. Para roteiros diferentes, crie Setores diferentes.
>
> **Preciso apagar os outros Setores para usar este caminho?** Não. Os outros continuam existindo e recebendo conversa por transferência, por menu ou por outro fluxo. O que define este caminho é marcar **um só** na Conexão.
>
> **Qual a diferença entre escolher um fluxo e escolher um Prompt OPEN.AI no Setor?** O **fluxo** é um roteiro que você desenha, com etapas e condições — e dentro dele cabe também um assistente de inteligência artificial, como um dos blocos. O **Prompt** coloca o assistente direto no Setor, sem roteiro em volta.
>
> **O cliente recebeu duas mensagens de boas-vindas. Por quê?** Porque o fluxo cumprimentou e a **Mensagem de saudação** do Setor também está preenchida. As duas se somam. Neste modo, deixe a saudação do Setor vazia e faça o cumprimento dentro do fluxo.
>
> **O cliente consegue falar com uma pessoa se o fluxo estiver atendendo?** Depende do que você desenhou. O fluxo precisa ter um caminho que entregue a conversa a um atendente — se não tiver, o cliente fica dentro dele.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Montar o fluxo e parar por aí:** o roteiro existe, está salvo e correto, e nada acontece — porque ninguém o chamou. **Solução:** escolha o fluxo no campo **Fluxos de Automação** do Setor e marque esse Setor na Conexão.
>
> **Marcar mais de um Setor na Conexão sem querer:** o cliente passa a receber o menu do chatbot e o fluxo deixa de ser o primeiro contato. **Solução:** na aba **Setores & Tempos**, deixe marcado apenas o Setor que tem o fluxo.
>
> **Fluxo sem saída para atendimento humano:** o cliente pede para falar com alguém e o roteiro não tem por onde entregar a conversa. **Solução:** inclua no fluxo um caminho que direcione a um Setor com atendentes.
>
> **Publicar o fluxo sem conferir:** um bloco desconectado ou um campo vazio derruba a conversa no meio. **Solução:** use o botão **Verificar** no editor antes de deixar o fluxo atendendo.
