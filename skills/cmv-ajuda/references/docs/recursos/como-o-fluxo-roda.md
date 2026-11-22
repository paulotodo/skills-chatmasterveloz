# Como o Fluxo Roda

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/como-o-fluxo-roda
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Como o Fluxo Roda

---

🧩 Um fluxo é uma conversa ensaiada: o cliente escreve, o fluxo responde, pergunta, espera, decide e, no fim, entrega a conversa a alguém ou encerra. Entender como esse ensaio anda evita o problema mais comum de quem monta fluxos: o fluxo que para no meio sem dizer nada.

Este artigo explica as regras que valem para qualquer fluxo, seja qual for o bloco.

## Quando o fluxo começa e quando atende

O fluxo só roda quando está ligado a um ponto de entrada: o Setor de uma conexão, uma tag, uma resposta rápida, uma campanha ou um sistema externo. Fluxo criado e não ligado a nada não atende ninguém.

Ligado pela conexão, o fluxo atende enquanto o atendimento está no **Aguardando**, antes de uma pessoa assumir. Quando o fluxo termina num **Setor** ou num **Operador**, a conversa passa para a equipe.

## Blocos que seguem e blocos que esperam

A maioria dos blocos faz o seu trabalho e segue na hora para o próximo: envia uma mensagem, coloca uma tag, guarda uma variável.

Alguns blocos **esperam o cliente**: **Pergunta**, **Menu**, **Botões** e **Avaliação do Atendimento** enviam algo e só seguem quando o cliente responde. Nesses blocos, e também no **GPT Assistant** e no **Typebot**, o campo **Sem resposta** cria uma saída para quem não responder em alguns minutos. Sem ele, o fluxo fica esperando.

📌 Na **Pergunta**, a opção **Mover de setor por inatividade** decide se o cliente parado ali entra na regra de inatividade da conexão. Desligue quando a resposta puder demorar de propósito.

## Como o fluxo escolhe o caminho

Cada bloco tem as saídas que o trabalho dele pede:

➡️ **Uma saída:** o fluxo segue em frente.

➡️ **Duas saídas:** um sim ou não, como **Verdadeiro** e **Falso** na **Condição**, **Dentro do Horário** e **Fora do Horário**, **Segue** e **Não segue**, **Sucesso** e **Erro**.

➡️ **Várias saídas:** uma por opção, como no **Menu** e no **Switch (tags)**.

➡️ **Nenhuma saída:** o bloco encerra o trabalho do fluxo. É o caso de **Setor**, **Operador**, **Trocar Fluxo**, **Encerrar** e **Encerrar Mensagem Rápida**.

⚠️ Saída sem ligação é um ponto onde a conversa para. O **Verificar**, na barra do editor, lista esses pontos antes de você salvar.

## O que o fluxo lembra

O fluxo guarda informações para usar mais adiante:

◽ **Variáveis**, criadas no bloco **Variável** e escritas entre porcentagens, como `%nome%`. Ficam gravadas no atendimento e podem ser sobrescritas.

◽ **Dados do contato e do atendimento**, como `{{firstName}}`, usados nas mensagens e nos blocos de integração.

◽ **Tags** do atendimento, colocadas e tiradas pelos blocos **Tag** e **Remover Tag**, e conferidas pela **Condição** e pelo **Switch (tags)**.

## Voltar e repetir

Para repetir uma etapa ou voltar ao menu, use o bloco **Pular para**. O caminho de volta precisa passar por um bloco que espera o cliente, como uma pergunta ou um menu. Um caminho que volta a um bloco sem esperar ninguém é um **ciclo sem espera**, e o fluxo é interrompido ao voltar ao mesmo bloco.

Para passar a conversa a outro fluxo, use o **Trocar Fluxo**. Não há volta automática: se precisar retornar, desenhe o caminho de volta no outro fluxo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O que acontece com o cliente que está no meio do fluxo quando eu salvo uma mudança?** Quem já entrou continua o caminho da versão anterior até o atendimento encerrar. Os próximos clientes que entrarem no fluxo veem a versão nova.
>
> **O cliente pode sair do fluxo antes de terminar?** Pode digitar **Sair**, o que encerra o atendimento. Para oferecer uma saída explícita, inclua uma opção no menu que leve a um **Encerrar** ou a um Setor.
>
> **Por que o fluxo parou de responder no meio do caminho?** Quase sempre há uma saída sem ligação, ou um bloco que espera o cliente sem **Sem resposta**. Abra o **Verificar** e confira a lista **Sem conexão de saída (o fluxo para neste bloco)**.
>
> **O mesmo fluxo pode ser usado em mais de uma conexão ou Setor?** Pode. Cada ponto de entrada pode apontar para o mesmo fluxo.
