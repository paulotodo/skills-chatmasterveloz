# Aba Mensagens em Setores & Chatbot

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-mensagens-em-setores-e-chatbot
- **Categoria:** Recursos
- **Menu:** Setores & Chatbot › Aba Mensagens em Setores & Chatbot

---

🧩 A aba **Mensagens** cuida do que o cliente lê ao chegar neste Setor. É aqui que você escreve a primeira resposta que ele recebe e, quando o Setor tem expediente, o que ele lê se escrever com o Setor fechado.

São três campos. A **Mensagem de saudação** recebe quem chegou; a **Mensagem de fora de expediente** responde quem chegou fora do horário; e as **Palavras-Chave e Gatilhos** guardam as palavras que levam o cliente direto a este Setor.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Setores & Chatbot** e edite o Setor.
>
> ➡️ Abra a aba **Mensagens**.
>
> ➡️ Escreva a saudação e, se o Setor tiver expediente, a mensagem de fora de expediente. Clique em **Salvar**.

## Os campos

🔘 **Mensagem de saudação:** o texto que o cliente recebe ao chegar neste Setor pela Conexão — seja porque a Conexão aponta só para ele, seja porque o cliente o escolheu no menu. É a primeira coisa que ele lê, e serve para confirmar que chegou no lugar certo e dizer o que esperar.

Uma boa saudação faz três coisas em poucas linhas: diz onde a pessoa chegou, avisa que alguém vai atender, e — quando for o caso — informa o horário. Algo como *"Você está no Suporte. Já vamos te atender. Nosso horário é de segunda a sexta, das 8h às 18h."*

Para usar o nome do cliente, escreva `{{name}}` no ponto do texto em que o nome deve aparecer: na hora de enviar, o sistema troca pelo nome do contato. Por exemplo, `Olá, {{name}}! Você está no Suporte.`

🔘 **Mensagem de fora de expediente:** o texto que o cliente recebe quando escreve com o Setor fechado. O campo só aparece nesta aba quando a empresa usa o expediente por Setor — no menu **Configurações  ›  Opções**, **Gerenciamento de Expediente** em **Gerenciamento Por Setor**. O horário de cada Setor fica na aba **Horários**.

🔘 **Palavras-Chave e Gatilhos:** palavras ligadas ao assunto deste Setor, separadas por vírgula, como `boleto,fatura`. Quando a Conexão tem o menu de Setores e o cliente escreve uma delas — já na primeira mensagem ou no lugar de escolher uma opção do menu —, a conversa vai direto para este Setor e o cliente recebe a **Mensagem de saudação** dele. Basta a palavra aparecer no meio da frase, sem diferença de maiúsculas, minúsculas e acento.

Quando a Conexão do Instagram encaminha comentários de publicações para o Setor, é a mesma lista que decide se o fluxo do Setor responde ao comentário: basta a palavra aparecer no meio da frase, sem diferença entre maiúsculas e minúsculas. Comentário sem nenhuma das palavras não recebe resposta.

⚠️ Deixar a **Mensagem de saudação** vazia não impede o Setor de funcionar, mas o cliente cai num silêncio: a conversa está aguardando e ele não recebeu nenhum sinal disso. É a causa mais comum de cliente que manda "alô?" três vezes seguidas.

## Próximo Passo

🧭 Definir o expediente na aba **Horários** do mesmo cadastro, se você quiser tratar quem chega fora do horário de forma diferente.

🧭 Revisar o comportamento do Setor na aba **Geral** — é lá que ficam o rodízio, os tempos de transferência e a automação.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A Mensagem de saudação do Setor é obrigatória?** Não. O Setor funciona sem ela, mas o cliente chega e não recebe nenhum retorno — fica sem saber se a mensagem foi entregue.
>
> **Posso usar o nome do cliente na Mensagem de saudação?** Sim. Escreva `{{name}}` onde o nome deve aparecer: na hora de enviar, o sistema troca pelo nome do contato.
>
> **A saudação do Setor é a mesma da Conexão?** Não. São textos diferentes, em cadastros diferentes. A da Conexão fala com quem acabou de chegar pela Conexão — e, quando ela tem dois ou mais Setores, abre o menu de escolha; a do Setor fala com quem já foi direcionado para este Setor.
>
> **O cliente volta a escrever outro dia. Recebe a Mensagem de saudação de novo?** Sim. Quando o cliente volta a escrever depois de o atendimento ter sido encerrado, a conversa chega de novo ao Setor pela Conexão e a saudação é enviada outra vez.
>
> **Onde fica a Mensagem de fora de expediente?** Nesta aba **Mensagens**. O campo só aparece quando a empresa usa o expediente por Setor: no menu **Configurações  ›  Opções**, **Gerenciamento de Expediente** em **Gerenciamento Por Setor**. Os horários ficam na aba **Horários** do Setor.
>
> **Onde as Palavras-Chave e Gatilhos fazem efeito?** Em dois lugares. Na Conexão com o menu de Setores: o cliente que escreve uma das palavras, na primeira mensagem ou no lugar de escolher uma opção, vai direto para este Setor e recebe a saudação dele. E nos comentários de publicações do Instagram encaminhados para este Setor: o fluxo do Setor responde ao comentário que tem uma das palavras e ignora o que não tem.
>
> **O cliente precisa escrever a Palavra-Chave do Setor igualzinho ao cadastro?** Não. A palavra vale no meio da frase, com ou sem acento e com qualquer mistura de maiúsculas e minúsculas: com `boleto` na lista, *Quero a segunda via do BOLETO* leva o cliente ao Setor.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Setor sem saudação:** o cliente escolhe o Setor no menu, a conversa entra na lista de aguardando e ele não recebe nada. Do lado dele, parece que a mensagem se perdeu. **Solução:** escreva uma saudação curta em todo Setor que recebe cliente direto.
>
> **Saudação que promete o que o Setor não cumpre:** dizer *"responderemos em instantes"* num Setor que só tem atendente à tarde cria frustração. **Solução:** se o Setor tem horário, diga o horário na saudação e escreva a **Mensagem de fora de expediente**.
>
> **Saudação longa demais:** três parágrafos de boas-vindas fazem o cliente rolar a tela antes de conseguir escrever. **Solução:** duas ou três linhas bastam.
