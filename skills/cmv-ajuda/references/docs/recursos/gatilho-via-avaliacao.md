# Gatilho via Avaliação

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gatilho-via-avaliacao
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Pontos de Entrada (Gatilho) › Gatilho via Avaliação

---

🧩 Quer que a nota do cliente decida o que acontece depois do atendimento? Com o **Gatilho via Avaliação**, cada nota da avaliação pode começar um fluxo diferente: quem deu nota baixa recebe um pedido de desculpas e uma pergunta sobre o que faltou, e quem deu nota alta recebe um convite para indicar a empresa.

O gatilho fica na própria avaliação, no campo **Fluxo após esta nota** de cada opção, e dispara quando o cliente responde a avaliação enviada no encerramento do atendimento.

Ideal para:

☑️ **Resgate de nota baixa:** pergunta o que deu errado e devolve a conversa para a equipe com a resposta do cliente.

☑️ **Indicação de quem gostou:** envia o link de avaliação pública ou de indicação só para quem deu nota alta.

☑️ **Motivo da nota:** guarda na avaliação o que o cliente respondeu no fluxo, para a gestão ler no **Relatório de Avaliações**.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e monte o fluxo de cada nota.
>
> ➡️ Acesse o menu **Avaliações**, edite a avaliação e, em **Opções de Avaliação**, escolha o fluxo de cada nota em **Fluxo após esta nota**.
>
> ➡️ Encerre o atendimento enviando essa avaliação, escolhida em **Escolha um menu de avaliação**.
>
> ➡️ Para ler as respostas do cliente no fluxo da nota, acesse o menu **Relatório de Avaliações**.

## Como escolher o fluxo de cada nota

Acesse o menu **Avaliações** e edite a avaliação.

🔘 **Fluxo após esta nota:** o fluxo que começa quando o cliente responde com aquela nota. Cada opção da avaliação tem o seu.

🔘 **Nenhum (envia a Mensagem de Avaliação da conexão):** a nota não começa fluxo. O cliente recebe a **Mensagem de Avaliação** cadastrada na conexão do atendimento.

⚠️ **A avaliação só é enviada quando o atendimento está em Atendendo.** Encerrar com avaliação um atendimento em **Aguardando** fecha o atendimento sem enviar a avaliação, e nenhum fluxo de nota começa.

## O que acontece quando o cliente responde a avaliação

➡️ **Nota com fluxo:** o fluxo começa logo depois da resposta, com o atendimento ainda encerrado. A **Mensagem de Avaliação** da conexão não é enviada.

➡️ **Nota com Nenhum:** o cliente recebe a **Mensagem de Avaliação** da conexão, e o atendimento continua encerrado.

➡️ **Resposta a uma pergunta do fluxo da nota:** quando o fluxo faz uma pergunta, a resposta do cliente reabre o atendimento, com protocolo novo, e o fluxo segue a partir dela.

⚠️ **Se o cliente demorar para responder a pergunta, o fluxo pode não continuar.** O atendimento reabre do mesmo jeito, no Setor da conexão, para a equipe atender.

## Onde ver as respostas do fluxo da nota

A resposta de uma **Pergunta** do fluxo da nota seguida de um bloco **Variável** fica guardada na própria avaliação, junto com a nota que o cliente deu.

Acesse o menu **Relatório de Avaliações**.

🔘 **Selo na coluna Nota:** ao lado da nota, a avaliação com respostas guardadas leva um selo com o número de respostas. A dica do selo diz, por exemplo, *"1 resposta(s) do cliente no fluxo da nota"*.

🔘 **Ver detalhes:** o botão da coluna **Ações** abre a janela **Detalhes da avaliação**. O bloco **Respostas do fluxo da nota** mostra, em cada resposta, a pergunta, a **Variável** que a guardou e a data, e embaixo o que o cliente respondeu.

🔘 **Exportar CSV:** o arquivo traz a coluna **Respostas do fluxo**, com cada resposta no formato *pergunta: resposta*, várias separadas por `|`.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso usar um fluxo diferente para cada nota da avaliação?** Pode. Cada opção da avaliação tem o seu **Fluxo após esta nota**, e as notas sem fluxo ficam em **Nenhum**.
>
> **A Mensagem de Avaliação da conexão também é enviada quando a nota tem fluxo?** Não. Ela só é enviada para as notas em **Nenhum (envia a Mensagem de Avaliação da conexão)**.
>
> **O fluxo da nota da avaliação reabre o atendimento?** Não sozinho. O fluxo roda com o atendimento encerrado, e o atendimento reabre quando o cliente responde a uma pergunta do fluxo.
>
> **A nota da avaliação aparece na conversa do atendimento?** Não. A resposta do cliente não fica na conversa, para a equipe não ter acesso a ela: só o administrador consulta as notas.
>
> **Onde vejo as respostas que o cliente deu no fluxo da nota da avaliação?** No menu **Relatório de Avaliações**: a avaliação com respostas leva um selo na coluna **Nota**, e o botão **Ver detalhes** mostra o bloco **Respostas do fluxo da nota**, com a pergunta, a **Variável** e a data de cada resposta. O **Exportar CSV** traz as respostas na coluna **Respostas do fluxo**.
>
> **Onde fica a Mensagem de Avaliação da conexão?** No menu **Conexões**, ao editar a conexão, no campo **Mensagem de Avaliação**.
