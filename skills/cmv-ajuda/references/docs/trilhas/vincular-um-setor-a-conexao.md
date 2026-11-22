# Vincular um Setor à Conexão

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/vincular-um-setor-a-conexao
- **Categoria:** Trilhas
- **Menu:** Primeiros Passos › Vincular um Setor à Conexão

---

🧩 Agora que definimos a porta de entrada, precisamos garantir que o atendimento tenha para onde ir. Vamos preparar a **sala de espera** e vinculá-la à Conexão.

Para isso, vamos criar um ou mais **Setores**. Eles funcionam como departamentos para organizar suas conversas. Pense nos **Setores** como as áreas da sua empresa: cada pessoa da equipe atende os Setores a que tem acesso.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Setores & Chatbot**.
>
> ➡️ Clique no botão **ADICIONAR SETOR**.
>
> ➡️ Preencha **Nome**, **Ordenação do BOT** e **Cor** e clique no botão **Adicionar**.
>
> ➡️ No menu **Conexões**, edite a Conexão e marque o Setor na aba **Setores & Tempos**.

## Como adicionar um Setor

Acesse o menu **Setores & Chatbot  ›  ADICIONAR SETOR**

Na nova janela você encontrará várias opções, incluindo algumas avançadas. Por agora, vamos focar só nos três campos obrigatórios — o sistema não salva o Setor sem eles:

🔘 **Nome:** o nome do Setor, usado para identificá-lo na lista de Setores e exibido nos atendimentos.

🔘 **Ordenação do BOT:** um número que define a ordem do Setor na lista de Setores e, quando a Conexão aponta para dois ou mais Setores, no menu que o cliente recebe. O número menor vem primeiro.

🔘 **Cor:** a cor para identificação rápida na lista de Setores e nos atendimentos.

## Vincular o Setor a uma Conexão

Com a Conexão e ao menos um **Setor** criados:

Acesse o menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**

🔘 **Setores:** marque o Setor (ou os Setores) que vão receber as conversas desta Conexão.

Quantos Setores você marca muda o que o cliente encontra:

➡️ **Um Setor:** a conversa vai direto para ele — e, se esse Setor tiver um fluxo do **FlowBuilder Nativo**, é o fluxo que recebe o cliente.

➡️ **Dois ou mais:** quem recebe o cliente é o chatbot, com um menu para ele escolher o Setor. Neste caso, a **Mensagem de saudação** da Conexão, na aba Mensagens, é obrigatória: sem ela, a Conexão não salva.

⚠️ Se um cliente mandar mensagem e o sistema não souber para qual Setor mandar (por falta de configuração), esse atendimento pode ficar invisível para os atendentes que têm permissão restrita.

## Próximo Passo

🧭 Cadastrar sua **Equipe** de atendimento e definir quais Setores cada pessoa atende, no menu **Equipe  ›  editar o usuário**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente sabe em qual Setor está?** Depende de como a Conexão está montada. Com dois ou mais Setores, ele escolhe o Setor pelo nome, no menu do chatbot. Com um Setor só, ele apenas recebe o atendimento — a divisão fica interna da sua empresa.
>
> **Posso transferir um cliente de um Setor para outro?** Sim. Durante o atendimento, se o vendedor perceber que o cliente precisa de ajuda técnica, ele usa o botão de transferência e passa o atendimento do Setor "Vendas" para o Setor "Suporte".
>
> **Marquei dois Setores na Conexão e ela não salva. Por quê?** Com dois ou mais Setores, a **Mensagem de saudação** da Conexão é obrigatória — é ela que abre o menu do chatbot. Preencha na aba Mensagens da Conexão e salve de novo.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Esquecer de vincular na Conexão:** o erro nº 1. O Setor é criado, mas o sistema não sabe que ele recebe as conversas daquela Conexão. **Solução:** depois de salvar o Setor, edite a Conexão no menu **Conexões** e marque o Setor na aba **Setores & Tempos**.
>
> **Atendimentos "invisíveis":** o cliente manda mensagem e ninguém vê. **Solução:** isso acontece quando a Conexão não tem um Setor vinculado — o atendimento fica sem Setor e quem tem acesso restrito não o enxerga. Vincule um Setor na aba **Setores & Tempos** da Conexão.
