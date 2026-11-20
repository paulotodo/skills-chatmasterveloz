# Chatbot e Menu de Setores na Conexão

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/chatbot-e-menu-de-setores-na-conexao
- **Categoria:** Recursos
- **Menu:** Setores & Chatbot › Chatbot e Menu de Setores na Conexão

---

🧩 Uma Conexão pode ser ligada a **vários Setores ao mesmo tempo**. Quando isso acontece, quem recebe o cliente é o **chatbot**: ele manda um menu com os Setores, o cliente escolhe para onde quer ir, e a conversa chega ao Setor certo sem passar por ninguém.

É o modelo de atendimento em que a triagem é feita pelo próprio cliente. E, dentro de cada Setor, o chatbot pode ir além do menu: com as **Opções do Chatbot**, o Setor escolhido abre um segundo menu, com respostas prontas e encaminhamentos.

Ideal para:

☑️ **Triagem sem custo humano:** o cliente se direciona sozinho, e o atendimento chega ao Setor certo sem que alguém precise ler e transferir.

☑️ **Operação com poucos assuntos:** três ou quatro áreas bem separadas cabem num menu curto que o cliente lê de uma vez.

☑️ **Entrada única para times distintos:** uma Conexão só serve vendas, suporte e financeiro sem que eles compartilhem a mesma caixa de entrada.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Crie os Setores que serão as opções, no menu **Setores & Chatbot**.
>
> ➡️ Defina a **Ordenação do BOT** de cada um — ela determina a ordem no menu.
>
> ➡️ No menu **Conexões**, edite a Conexão e escreva a **Mensagem de saudação**, que abre o menu.
>
> ➡️ Na aba **Setores & Tempos** da mesma Conexão, marque **todos** os Setores que devem aparecer como opção e clique em **Salvar**.

## Como montar o menu

Acesse o menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**

🔘 **Setores:** campo de busca que aceita **mais de um Setor**. Cada Setor marcado vira uma opção que o cliente pode escolher. É a marcação de dois ou mais que faz o menu existir.

🔘 **Mensagem de saudação** (aba Mensagens da Conexão): o texto que vem antes das opções. Com dois ou mais Setores marcados ela é **obrigatória** — sem ela, a Conexão não salva e a tela avisa *"A mensagem de saudação é obrigatória quando há mais de um setor."*

A ordem das opções não é definida na Conexão. Ela vem do campo **Ordenação do BOT** de cada Setor, na aba Geral do cadastro dele: o número menor aparece primeiro.

⚠️ Marcar **um único** Setor não monta menu nenhum: a conversa vai direto para ele. O menu só existe a partir de dois.

## O que o cliente recebe

➡️ **Na primeira mensagem:** a **Mensagem de saudação** da Conexão, seguida de uma linha por Setor, no formato *1 - Suporte*, *2 - Financeiro*.

➡️ **Ao responder com o número:** a conversa entra naquele Setor e o cliente recebe a **Mensagem de saudação** do Setor. Com a opção **Informar a Posição no Setor?** ligada, no menu **Configurações  ›  Opções  ›  Automação**, seção **Bot e FlowBuilder**, chega logo depois a posição dele entre os que esperam no Setor.

➡️ **Ao escrever uma palavra do campo Palavras-Chave e Gatilhos de um dos Setores:** a conversa vai direto para esse Setor, sem precisar do número — vale já na primeira mensagem e também no lugar de escolher uma opção. A lista fica na aba Mensagens do cadastro do Setor.

➡️ **Ao responder qualquer outra coisa:** o menu é enviado de novo, conforme a opção **Repetições do Bot**, no menu **Configurações  ›  Opções  ›  Automação**, seção **Bot e FlowBuilder**.

➡️ **Se o Setor escolhido tiver fluxo** (campo **Fluxos de Automação**): o fluxo começa na mensagem seguinte que o cliente enviar.

A forma do menu segue a opção **Tipo Chatbot**, no menu **Configurações  ›  Opções  ›  Automação**, seção **Bot e FlowBuilder**. Em **Texto**, as opções chegam numeradas, como acima. Dependendo do canal, as opções podem aparecer como botões para o cliente tocar.

## Quantas vezes o menu é enviado

A opção **Repetições do Bot**, no menu **Configurações  ›  Opções  ›  Automação**, seção **Bot e FlowBuilder**, vale para a empresa inteira:

🔘 **Infinito:** o menu volta a cada resposta que não é uma das opções, sem limite.

🔘 **Um número (1, 2, 3…):** é o total de vezes que o menu é enviado na conversa. Em **2**, por exemplo, ele vai na primeira mensagem e mais uma vez depois da primeira resposta errada. Passado o limite, as respostas que não são opção ficam sem retorno, e a conversa espera **sem Setor** até alguém da equipe assumir.

## Opções do Chatbot: um segundo menu dentro do Setor

Depois que o cliente escolhe o Setor, o chatbot pode oferecer um segundo menu, montado no próprio Setor.

Acesse o menu **Setores & Chatbot  ›  editar o Setor  ›  aba Geral**

Na seção **Opções**, o botão **Adicionar** cria uma opção. Cada opção tem:

🔘 **Título da Opção:** o texto que o cliente vê no menu.

🔘 **Selecione uma Opção:** o tipo, que decide o que a opção faz — **Texto**, **Atendente**, **Setor**, **Externo (API)**, **Arquivo** ou **Finalizar**.

🔘 **Texto da opção** (*Digite o texto da opção*): a mensagem que o cliente recebe ao escolher a opção.

🔘 **Finalizar Automaticamente:** com **Sim**, o atendimento é encerrado logo depois que o cliente recebe o texto da opção.

O botão **Próximo Passo** cria uma opção dentro da opção, para menus em mais de um nível.

O que cada tipo faz quando o cliente escolhe a opção:

➡️ **Texto:** envia o texto da opção.

➡️ **Setor:** envia o texto e passa a conversa para o Setor escolhido na opção. O cliente recebe também a **Mensagem de saudação** desse Setor.

➡️ **Atendente:** pede um atendente e um Setor. Envia o texto e entrega a conversa a esse atendente, já em atendimento, no Setor escolhido.

➡️ **Arquivo:** pede um arquivo do **Gerenciador de Arquivos**. Envia o arquivo e o texto da opção.

➡️ **Externo (API):** pede a URL de uma integração externa (N8N, Zapier…).

➡️ **Finalizar:** envia o texto da opção e encerra o atendimento. Depois do texto, o cliente recebe a mensagem de conclusão da Conexão, se ela estiver preenchida.

Ao escolher o Setor no menu da Conexão, o cliente recebe a saudação do Setor e as opções numeradas, com uma linha **SAIR - Encerrar Atendimento** que o sistema acrescenta sozinho. Quem responde **SAIR** encerra o atendimento e recebe o aviso *"Você encerrou este atendimento usando o comando SAIR"*.

⚠️ As **Opções do Chatbot** só aparecem num Setor **já salvo**: crie o Setor, salve, e abra de novo para montar as opções. Cada opção é gravada na hora, separada do **Salvar** do Setor.

## O que cada Setor precisa ter para funcionar como opção

Um Setor que entra no menu não é diferente dos outros, mas três campos dele passam a ter efeito visível para o cliente:

🔘 **Nome:** aparece para o cliente como o texto da opção. Nomes internos como "Suporte N2" ou "Grupo 3" confundem quem está do outro lado — prefira o que o cliente reconhece.

🔘 **Ordenação do BOT:** define em que posição a opção aparece — o número menor vem primeiro.

🔘 **Mensagem de saudação:** o texto que o cliente recebe **depois** de escolher aquela opção, confirmando que chegou no lugar certo. Fica na aba Mensagens do Setor.

## Próximo Passo

🧭 Conferir a **Mensagem de saudação** de cada Setor do menu, no menu **Setores & Chatbot  ›  editar o Setor  ›  aba Mensagens**. Sem ela, o cliente escolhe uma opção e não recebe retorno.

🧭 Cadastrar os atendentes de cada Setor no menu **Equipe  ›  editar o usuário**. Opção de menu que leva a Setor sem gente é conversa que entra e não sai.

🧭 Ajustar os tempos da aba **Setores & Tempos** — os campos **Após** e **Mover** resgatam quem ficou parado sem escolher nenhuma opção.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Como faço o cliente escolher entre vendas e suporte?** Crie os dois Setores, escreva a **Mensagem de saudação** da Conexão e marque **os dois** no campo **Setores**, no menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**. Com dois ou mais marcados, o cliente passa a receber o menu do chatbot.
>
> **A Conexão não salva depois que marquei o segundo Setor. Por quê?** Com dois ou mais Setores, a **Mensagem de saudação** da Conexão é obrigatória — é ela que abre o menu. Preencha na aba Mensagens da Conexão e salve de novo.
>
> **O cliente respondeu outra coisa em vez do número. O que acontece?** O chatbot envia o menu de novo, até o limite da opção **Repetições do Bot**, no menu **Configurações  ›  Opções  ›  Automação**, seção **Bot e FlowBuilder**. Em **Infinito**, ele volta sempre; com um número, depois do limite a conversa fica esperando sem Setor.
>
> **Posso ligar quantos Setores na mesma Conexão?** O campo aceita vários. Na prática, um menu longo faz o cliente desistir de ler — três ou quatro opções costumam ser o limite do que ele acompanha.
>
> **Como mudo a ordem das opções do menu?** Não é na Conexão. A ordem vem do campo **Ordenação do BOT** de cada Setor, no menu **Setores & Chatbot  ›  editar o Setor  ›  aba Geral**. O número menor aparece primeiro.
>
> **Marquei só um Setor. Por que o cliente não recebe menu?** Porque com um Setor só não há escolha a fazer: a conversa vai direto para ele. O menu existe a partir de dois Setores marcados.
>
> **O cliente escolheu uma opção e não recebeu nada. O que faltou?** A **Mensagem de saudação** daquele Setor está vazia. Ela é o retorno que confirma para o cliente que ele chegou no lugar certo.
>
> **O Setor escolhido no menu tem fluxo. Quando o fluxo começa?** Na mensagem seguinte que o cliente enviar. Ao escolher, ele recebe a saudação do Setor; o fluxo responde à próxima mensagem dele.
>
> **Não acho as Opções do Chatbot no Setor que acabei de criar. Onde estão?** Elas só aparecem num Setor já salvo. Salve o Setor, abra de novo no menu **Setores & Chatbot  ›  editar o Setor  ›  aba Geral** e procure a seção **Opções**.
>
> **Como faço uma opção do chatbot passar a conversa para uma pessoa?** Use o tipo **Atendente**: escolha o atendente e o Setor. Quem escolhe essa opção recebe o texto dela e já cai em atendimento com essa pessoa.
>
> **O cliente escolheu a opção do tipo Finalizar. Ele recebe o texto da opção?** Recebe. Primeiro chega o texto da opção, depois a mensagem de conclusão da Conexão, e o atendimento é encerrado.
>
> **A opção do tipo Setor manda a saudação do Setor de destino?** Manda. O cliente recebe o texto da opção e, em seguida, a **Mensagem de saudação** do Setor para onde a conversa foi.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Nome de Setor escrito para uso interno:** "Grupo 3" e "Suporte N2" aparecem para o cliente como a opção do menu, e ele não sabe o que significam. **Solução:** nomeie os Setores do menu com o vocabulário do cliente — "Suporte", "Financeiro", "Quero comprar".
>
> **Menu com opção que leva a Setor sem atendentes:** o cliente escolhe, é direcionado, e a conversa fica parada porque ninguém tem acesso àquele Setor. **Solução:** antes de incluir um Setor no menu, cadastre quem atende nele no menu **Equipe  ›  editar o usuário**.
>
> **Setor no menu sem mensagem de saudação:** o cliente escolhe a opção e o sistema não responde nada. Do lado dele, parece que o menu não funcionou. **Solução:** preencha a saudação de todo Setor que entra no menu.
>
> **Repetições do Bot baixo demais:** o cliente erra o número uma ou duas vezes e o menu para de ser enviado — a conversa fica sem Setor e sem resposta. **Solução:** use um limite que dê margem ao erro, ou **Infinito**, e acompanhe as conversas que ficam sem Setor.
>
> **Menu com opção demais:** oito Setores viram oito linhas que o cliente não lê, e ele responde qualquer número ou desiste. **Solução:** agrupe assuntos e deixe o menu curto.
