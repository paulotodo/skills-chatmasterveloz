# Gatilho via Comentário do Instagram

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gatilho-via-comentario-do-instagram
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Pontos de Entrada (Gatilho) › Gatilho via Comentário do Instagram

---

🧩 Quer que quem comenta uma palavra-chave num post do Instagram receba a resposta na hora, no comentário e no Direct, sem ninguém da equipe digitar? O **Gatilho via Comentário do Instagram** começa um fluxo a partir do comentário: a Conexão do Instagram encaminha os comentários para um **Setor**, e a palavra-chave desse Setor dispara o fluxo.

O fluxo responde em público, embaixo do comentário, e continua a conversa no Direct da pessoa.

Ideal para:

☑️ **Fim do "link na bio":** entrega o link ou o material no Direct de quem comenta a palavra combinada.

☑️ **Campanha por palavra-chave:** responde todos os comentários de uma promoção na hora, sem ninguém da equipe digitar.

☑️ **Resposta por publicação:** envia uma mensagem diferente conforme o post ou o formato em que a pessoa comentou.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e monte o fluxo com o bloco **Responder Comentário** e um bloco de mensagem para o Direct.
>
> ➡️ Acesse o menu **Setores & Chatbot**, crie um Setor só para os comentários, escolha esse fluxo e preencha **Palavras-Chave e Gatilhos**.
>
> ➡️ Acesse o menu **Conexões**, edite a conexão do Instagram, marque **Habilitar ação para comentários** e escolha o Setor em **Setor para Comentários (INSTAGRAM)**.

## Como o comentário vira conversa

Com a opção **Habilitar ação para comentários** marcada na Conexão do Instagram, cada comentário recebido em posts e reels segue este caminho:

➡️ **Todo comentário** entra na conversa da pessoa, como comentário, e o atendimento vai para o **Setor para Comentários** com o status **Aguardando**. Se o atendimento estava encerrado, ele é reaberto.

➡️ **Comentário com a palavra-chave** dispara o fluxo do Setor. Vale a palavra dentro de uma frase, com maiúsculas ou minúsculas: com a palavra-chave *quero*, o comentário *Eu QUERO saber o preço* também dispara.

➡️ **Comentário sem a palavra-chave** não recebe resposta automática. Ele fica na conversa para a equipe ver.

## Como montar o fluxo do comentário

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo**

🔘 **Responder Comentário:** responde em público, embaixo do comentário da pessoa. Escreva várias frases, separadas por vírgula: a cada comentário, uma delas é sorteada.

🔘 **Bloco de mensagem depois dele**, como o **Conteúdo**: a mensagem vai para o Direct da pessoa, como resposta àquele comentário.

🔘 **Condição com Postagem:** escolha uma ou mais publicações da conta. O fluxo segue por um caminho quando o comentário veio de uma delas e pelo outro quando veio de outra publicação. Mensagem do Direct segue pelo caminho de outra publicação.

🔘 **Condição com Tipo de postagem:** marque os formatos, entre **Publicação do feed**, **Reels**, **Story** e **Anúncio**, para tratar todas as publicações daquele formato sem escolher uma a uma.

⚠️ **Deixe a Mensagem de saudação do Setor vazia.** No Setor dos comentários, a **Mensagem de saudação** também responde o comentário em público, junto com o **Responder Comentário**, e a pessoa recebe duas respostas.

## Como preparar o Setor dos comentários

Acesse o menu **Setores & Chatbot**

🔘 **Palavras-Chave e Gatilhos:** as palavras que disparam o fluxo do comentário, separadas por vírgula.

🔘 **Fluxo do Setor:** escolha o fluxo do comentário no cadastro do Setor. Sem fluxo, nenhum comentário é respondido, nem pela **Mensagem de saudação**.

Reserve um Setor só para os comentários: todo comentário recebido vai para ele, com ou sem palavra-chave.

⚠️ **O fluxo do Setor dos comentários também responde o Direct.** Enquanto o atendimento da pessoa está nesse Setor, uma mensagem dela no Direct também roda o fluxo.

## Como ligar na Conexão do Instagram

Acesse o menu **Conexões**, edite a conexão do Instagram e, na seção **Automação**, marque **Habilitar ação para comentários**. Os comentários recebidos em posts e reels passam a ir para o Setor escolhido em **Setor para Comentários (INSTAGRAM)**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Quem comenta sem a palavra-chave recebe alguma resposta?** Não. O comentário entra na conversa da pessoa e o atendimento vai para o **Setor para Comentários**, mas nenhum fluxo roda.
>
> **A palavra-chave do Gatilho via Comentário precisa ser o comentário inteiro?** Não. Ela dispara dentro de uma frase e sem diferenciar maiúsculas de minúsculas.
>
> **Se a pessoa comentar de novo, o fluxo do comentário roda outra vez?** Roda. Cada comentário com a palavra-chave dispara o fluxo, mesmo com o atendimento aberto.
>
> **A resposta do bloco Responder Comentário vai para o Direct?** Não. Ela fica pública, embaixo do comentário. O Direct é enviado pelo bloco de mensagem que vem depois.
>
> **Posso responder diferente em cada publicação do Instagram?** Pode. Use a **Condição** com **Postagem** ou **Tipo de postagem** logo depois do **Responder Comentário**, com uma mensagem em cada caminho.
>
> **A pessoa mandou mensagem no Direct e recebeu a resposta do fluxo do comentário. Por quê?** O atendimento dela estava no Setor dos comentários, e o fluxo desse Setor roda a cada mensagem que chega. Na **Condição com Postagem**, a mensagem do Direct segue pelo caminho de outra publicação.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Comentaram a palavra-chave e nada aconteceu:** a Conexão do Instagram está sem **Habilitar ação para comentários**, ou o Setor escolhido não tem fluxo ou não tem a palavra em **Palavras-Chave e Gatilhos**. **Solução:** confira a opção na conexão, o fluxo e as palavras do Setor.
