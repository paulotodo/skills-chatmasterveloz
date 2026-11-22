# Setores & Chatbot

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/setores-e-chatbot
- **Categoria:** Recursos
- **Menu:** Setores & Chatbot

---

🧩 Sua equipe sofre com mensagens que chegam no lugar errado, causando confusão, atraso e clientes insatisfeitos? O pedido de reenvio de boleto, o cliente novo pedindo orçamento, a dúvida técnica de quem já comprou — tudo misturado e para todos os atendentes.

O **Setor** divide o atendimento por assunto. Vendas, suporte e financeiro deixam de disputar a mesma caixa de entrada: cada área passa a ter as próprias pessoas, o próprio horário e a própria forma de receber quem chega.

Imagine uma loja com balcões separados — quem vai comprar procura um balcão específico, quem vai trocar um produto procura outro. No sistema, a conversa é direcionada ao balcão certo antes de chegar a um atendente.

Ideal para:

☑️ **Divisão por área:** vendas, suporte e financeiro respondem apenas pelo que é da sua área, sem triar mensagem que pertence a outro time.

☑️ **Horário por equipe:** cada Setor tem o próprio expediente — o financeiro atende só em dias úteis enquanto o suporte atende de segunda a sábado.

☑️ **Ponto de entrada da automação:** o Setor determina qual fluxo ou automação responde antes de um atendente assumir a conversa.

#### O que existe nesta seção

O cadastro de um Setor é dividido em abas:

⚡ **Geral** — a identidade e o comportamento do Setor. Nome, cor, tempo até transferir, quem é notificado e qual automação entra. É a aba mais cheia e a única obrigatória.

⚡ **Mensagens** — o que o cliente recebe ao chegar e, quando o Setor tem expediente, o que ele recebe fora do horário.

⚡ **Horários** — o expediente deste Setor, dia a dia. Precisa ser habilitado no menu **Configurações  ›  Opções  ›  Geral**, seção **Gerenciamento de Expediente**.

⚡ **Integrações** — ligação com plataformas externas, se disponível no seu plano.

## Como a conversa chega até um Setor

Apenas criar um Setor não faz a conversa chegar nele. É necessário configurar por onde ela chegará, de uma das seguintes formas:

➡️ **Pela Conexão.** Quando a Conexão aponta para **um único** Setor, toda conversa recebida vai direto para ele — e, se esse Setor tiver um fluxo do **FlowBuilder Nativo**, é o fluxo que recebe o cliente. Se mais de um Setor for selecionado, quem recebe o cliente é o chatbot, com um menu das opções disponíveis (modo *chatbot legado*).

➡️ **Por transferência.** Um atendente transfere para um Setor de modo manual.

➡️ **Por uma automação.** Um fluxo montado no **FlowBuilder Nativo** direcionando para um Setor específico.

> **[ATENCAO]**
>
> #### Atenção
>
> Essa é a decisão mais importante da seção, e ela **não** é tomada no cadastro do Setor: acesse o menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**.

## Próximo Passo

🧭 Criar os Setores no menu **Setores & Chatbot**.

🧭 Cadastrar quem atende cada um, no menu **Equipe  ›  editar o usuário**, marcando o Setor no cadastro da pessoa.

🧭 Definir por onde a conversa chega, no menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual a diferença entre Setor e Conexão?** A Conexão é o canal por onde a mensagem chega até você. O Setor é o balcão que recebe essa mensagem depois de ela entrar. Uma Conexão pode alimentar vários Setores, e um mesmo Setor pode receber de mais de uma Conexão.
>
> **Quantos Setores eu preciso ter?** Um por time que atende áreas diferentes. Criar Setor demais espalha a equipe e deixa conversa parada em balcão vazio; criar de menos joga tudo no mesmo lugar e o atendente perde tempo classificando. Comece com um por área real da sua empresa.
>
> **Criei o Setor e nada chega nele. Por quê?** Porque nada aponta para ele ainda. O Setor precisa ser destino de uma Conexão, de uma transferência ou de uma automação — o cadastro sozinho não atrai conversa.
>
> **O cliente escolhe o Setor ou o sistema escolhe?** Depende de quantos Setores a Conexão alcança. Com vários, o chatbot manda um menu e o cliente escolhe. Com um só, a conversa vai direto e ele não escolhe nada — e, se o Setor tiver fluxo, é o fluxo que conversa com ele.
>
> **O que acontece com quem chega fora do horário?** Depende do que você configurar. Enquanto o expediente por Setor estiver desligado, o Setor atende a qualquer hora e a conversa fica aguardando até alguém assumir.
>
> **Antes eu via "Fila" e "Departamento" — sumiram?** Não sumiu o recurso, mudou o nome. Hoje a plataforma chama de **Setor** em todo lugar. A palavra "fila" continua aparecendo quando quer dizer *espera* — o cliente que aguarda atendimento está na fila de espera do Setor.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Criar o Setor e esperar que a conversa chegue sozinha:** o cadastro existe, mas nada aponta para ele. **Solução:** vincule o Setor a uma Conexão no menu **Conexões  ›  editar a Conexão**, ou torne-o destino de uma transferência ou de uma automação.
>
> **Setor sem ninguém dentro:** a conversa chega e ninguém consegue assumir. **Solução:** ao criar um Setor, cadastre na mesma hora quem vai atendê-lo, no menu **Equipe  ›  editar o usuário**.
>
> **Um Setor para cada assunto:** dez Setores numa equipe de três pessoas espalha o atendimento e faz o cliente esperar em balcão vazio. **Solução:** um Setor por time que existe de verdade, não por tipo de dúvida.
>
> **Nomear o Setor com vocabulário interno:** o nome vira a opção que o cliente lê no menu, e ele não sabe o que significa. **Solução:** nomeie pelo que o cliente reconhece — "Suporte", "Financeiro", "Quero comprar".
