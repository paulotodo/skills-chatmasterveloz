# Visão Geral Setores & Chatbot

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/visao-geral-setores-e-chatbot
- **Categoria:** Recursos
- **Menu:** Setores & Chatbot › Visão Geral Setores & Chatbot

---

🧩 A tela **Setores & Chatbot** é a lista de todos os balcões de atendimento da sua empresa. É onde você pode criar um Setor novo, encontrar um que já existe e acessar um cadastro para editar.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Setores & Chatbot**.
>
> ➡️ Use **ADICIONAR SETOR** para criar, ou o ícone de lápis de um card para editar.
>
> ➡️ O filtro **Categoria**, no topo, organiza a exibição dos Setores.

## Como chegar

Acesse o menu: **Setores & Chatbot**

## O que tem no topo

🔘 **Categoria:** filtro que organiza a exibição dos Setores. Começa em **Todas as categorias**, mostrando tudo. Faz sentido usar depois que você cadastrar categorias e atribuí-las aos Setores.

🔘 **ADICIONAR SETOR:** abre o cadastro de um Setor em branco.

## O que cada card mostra

Cada Setor aparece como um card com quatro informações:

🔘 **Nome:** o nome que você deu ao Setor.

🔘 **Número (#9, por exemplo):** o identificador do Setor no sistema. Serve para diferenciar dois Setores de nome parecido e é o número que aparece em integrações e chamados de suporte.

🔘 **Estado da saudação:** mostra **"Sem mensagem de saudação"** quando a aba Mensagens está vazia. É um aviso útil — Setor sem saudação recebe o cliente em silêncio.

🔘 **Ordenação:** a posição do Setor nesta lista e no menu de Setores que a Conexão envia ao cliente, exibida como um rótulo seguido do número — **Alta (1)**, **Média (5)**, **Baixa (9)**. De 1 a 3 o rótulo é Alta, de 4 a 6 é Média, e de 7 em diante é Baixa. Quanto menor o número, mais cedo o Setor aparece.

## Os selos de recurso

Além das informações acima, o card exibe um **selo** para cada recurso ligado naquele Setor. São eles que permitem ver, sem abrir cadastro nenhum, o que está configurado em cada um:

🔘 **O nome da categoria** — quando o Setor pertence a uma, o próprio nome dela aparece como selo.

🔘 **FlowBuilder** — o Setor tem um fluxo escolhido no campo Fluxos de Automação.

🔘 **Prompt GPT** — o Setor tem um assistente escolhido no campo Prompt OPEN.AI.

🔘 **Chatbot** — o Setor está com o ChatBot Externo ligado.

🔘 **Roteador** — o Setor distribui os atendimentos pelo Rodízio de Atendentes.

🔘 **Motivo** — o Setor exige que o atendente escolha um motivo ao encerrar.

🔘 **Webhook** — o Setor tem uma URL de webhook configurada.

As integrações preenchidas na aba **Integrações** também ganham selo próprio, com o nome do serviço.

⚠️ **Os selos de automação podem aparecer juntos.** Um Setor com **FlowBuilder** e **Prompt GPT** ao mesmo tempo é possível: a tela aceita os dois sem avisar nada. Vale conferir se é isso mesmo que você quer, porque dois motores no mesmo Setor dificultam prever qual atende.

⚠️ Setor sem selo nenhum apenas recebe a conversa e espera que alguém assuma — o que pode ser exatamente o que você quer.

## O que cada botão do card faz

🔘 **Editar setor** (ícone de lápis): abre o cadastro do Setor. É o mesmo formulário do ADICIONAR SETOR, já preenchido.

🔘 **Excluir setor** (ícone de lixeira): remove o Setor.

⚠️ A exclusão **não apaga os atendimentos** daquele Setor. A própria tela avisa: eles continuam existindo, mas ficam **sem Setor atribuído** — e isso os torna invisíveis para o atendente comum, que enxerga a lista pelo Setor a que pertence. Transfira os atendimentos antes de excluir.

⚠️ O Setor excluído também sai das **Conexões** que apontavam para ele. Depois de excluir, confira o campo **Setores** de cada Conexão, no menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**.

## Próximo Passo

🧭 Criar seu primeiro Setor pelo botão **ADICIONAR SETOR** — o mínimo são três campos da aba Geral: **Nome**, **Ordenação do BOT** e **Cor**.

🧭 Cadastrar categorias no menu **Categorias**, logo abaixo de **Setores & Chatbot**, se a sua lista já estiver grande.

🧭 Vincular o Setor a uma Conexão, no menu **Conexões  ›  editar a Conexão**, para que a conversa comece a chegar nele.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Como adiciono um Setor?** Pelo botão **ADICIONAR SETOR**, no topo da tela. Ele abre o cadastro em branco. Na aba Geral, preencha ao menos **Nome**, **Ordenação do BOT** e **Cor** — o resto pode ficar para depois.
>
> **Como edito um Setor que já existe?** Clique no ícone de lápis do card. Abre o mesmo cadastro do ADICIONAR SETOR, já preenchido.
>
> **Como excluo um Setor?** Pelo ícone de lixeira do card. A tela avisa que a ação não pode ser revertida e que **os atendimentos daquele Setor continuam existindo, mas sem Setor atribuído** — o que os deixa fora da lista de quem atende por Setor. O Setor também sai das Conexões que apontavam para ele. Transfira os atendimentos antes.
>
> **O que significa o número com cerquilha no card, tipo #9?** É o identificador do Setor no sistema. Ele é útil para diferenciar Setores de nome parecido e para informar em chamados de suporte e integrações.
>
> **O que são os selos que aparecem no card?** Cada selo indica um recurso ligado naquele Setor: o **nome da categoria** a que ele pertence, **FlowBuilder** (tem fluxo), **Prompt GPT** (tem assistente), **Chatbot** (ChatBot Externo), **Roteador** (Rodízio de Atendentes), **Motivo** (motivo de encerramento obrigatório), **Webhook** (URL configurada) e as integrações da aba **Integrações**. Servem para ver o que cada Setor tem sem abrir o cadastro.
>
> **Configurei um recurso e o selo não apareceu no card?** Nem todo campo do cadastro tem selo — **Grupos de templates**, por exemplo, fica gravado no Setor e não gera selo nenhum. Se o recurso é um dos que têm selo, abra o Setor pelo lápis e confira se o campo está mesmo preenchido: o selo acompanha a configuração gravada.
>
> **Posso ter FlowBuilder e Prompt GPT no mesmo Setor?** A tela aceita os dois e mostra os dois selos. Mas com dois motores de automação ligados fica difícil prever qual responde — o recomendado é escolher um por Setor.
>
> **O que significa "Alta", "Média" e "Baixa" no card?** É a Ordenação do BOT, que define a posição do Setor nesta lista e no menu de Setores que a Conexão envia ao cliente. De 1 a 3 aparece como Alta, de 4 a 6 como Média, e de 7 em diante como Baixa. O número entre parênteses é o valor exato.
>
> **Um card diz "Sem mensagem de saudação". Isso é um erro?** Não é erro, é aviso. Significa que a aba **Mensagens** daquele Setor está vazia, e o cliente que chegar nele não vai receber nenhum retorno automático. Vale preencher.
>
> **O filtro de Categoria está vazio. Por quê?** Porque nenhuma categoria foi cadastrada ainda. Elas são criadas no item **Categorias**, logo abaixo de Setores & Chatbot no menu, e depois atribuídas a cada Setor na aba Geral do cadastro.
>
> **Onde configuro o robô que atende neste Setor?** Não é nesta tela. Entre no Setor pelo lápis e vá à aba **Geral** — é lá que ficam as opções de automação.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Procurar as configurações do Setor na lista:** a tela mostra só o resumo. Nome, saudação, horário, automação e tudo mais vive dentro do cadastro. **Solução:** clique no lápis do card.
>
> **Deixar Setores com "Sem mensagem de saudação":** o cliente é direcionado, a conversa entra em aguardando e ele não recebe nada — do lado dele, parece que a mensagem sumiu. **Solução:** abra o Setor, vá à aba **Mensagens** e escreva uma saudação curta.
>
> **Excluir um Setor sem verificar os atendimentos:** as conversas que estavam nele ficam sem destino e ninguém percebe até um cliente cobrar. **Solução:** antes de excluir, transfira os atendimentos para outro Setor.
>
> **Excluir o Setor de uma Conexão sem conferir a Conexão:** a Conexão deixa de apontar para ele, e o caminho da conversa muda. **Solução:** depois de excluir, confira o campo **Setores** da Conexão.
>
> **Criar Setores demais e usar o filtro para se achar:** o filtro de Categoria resolve a lista longa, mas não resolve o atendimento espalhado. **Solução:** um Setor por time que existe de verdade.
