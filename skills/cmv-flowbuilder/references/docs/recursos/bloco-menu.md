# Menu

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-menu
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Menu

---

🧩 O bloco **Menu** oferece opções ao cliente e leva o fluxo pelo caminho que ele escolher. É a principal forma de guiar a conversa: *Vendas*, *Suporte*, *Financeiro*, e cada escolha segue para um lado.

O mesmo bloco envia as opções de três jeitos: em texto numerado, em lista ou em botões. O fluxo espera a resposta do cliente antes de seguir.

**🏷️ Categoria: Mensagem - Roteador**

Ideal para:

☑️ **Facilidade para o cliente:** ele toca numa opção ou digita um número, em vez de escrever frases.

☑️ **Divisão automática:** cada escolha leva a um fluxo, a um Setor ou a uma resposta diferente, sem ninguém da equipe.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Menu**.
>
> ➡️ Escolha o **Tipo de Menu**, escreva a mensagem, crie as opções e clique em **Adicionar**.
>
> ➡️ Ligue cada saída do bloco ao próximo passo.

## Vídeo Tutorial

[Vídeo Voomly — id G0ATSxICAwQHbBMkokJGWrM8CkCtchyn8ldTMrhKWew_SG8qy, tipo v]  

## Os três tipos de menu

![Tipos de Menus no FlowBuilder](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6adcbb4f70864.png)

⚡ **Menu em Texto:** as opções vão numeradas no fim da mensagem, e o cliente responde com o número. A janela não limita o tamanho das opções, e o menu aceita uma imagem de capa.

⚡ **Menu em Lista:** um botão abre a lista com **opções**, cada uma com título e descrição.

⚡ **Menu em Botões:** até **3 opções**, cada uma num botão para o cliente tocar.

⚠️ Na lista e nos botões, cada opção tem no máximo **20 caracteres**. Ao trocar um menu em texto para lista ou botões, encurte as opções.

## Como configurar o bloco Menu

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Menu**

![Formulário Flowbuilder Menu](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6adcbcec83027.png)

A janela **Adicionar bloco: Menu** começa pelo tipo.

🔘 **Tipo de Menu:** **Menu em Texto**, **Menu em Lista** ou **Menu em Botões**. Os campos abaixo mudam conforme o tipo, e as opções já criadas continuam quando você troca.

No **Menu em Texto**:

◽ **Imagem de Capa (Opcional):** uma imagem enviada junto com o menu, escolhida pelo botão **Arquivo de Capa**.

◽ **Mensagem de explicação do menu:** o texto que pergunta o que o cliente deseja. Não numere as opções nela: a plataforma acrescenta a lista numerada no fim da mensagem, como `*1* - Vendas`.

No **Menu em Lista**:

◽ **Cabeçalho da Lista (Opcional):** até 60 caracteres. O cliente vê o cabeçalho dentro da lista aberta, acima das opções.

◽ **Texto do Botão da Lista:** o botão que abre a lista, como *Ver opções*, até 20 caracteres. Em branco, o botão vai como **MENU**.

◽ **Rodapé da Lista (Opcional):** até 60 caracteres.

◽ **Texto Principal da Lista:** o corpo da mensagem, até 1024 caracteres.

No **Menu em Botões**:

◽ **Título dos Botões (Opcional):** texto acima dos botões, até 60 caracteres.

◽ **Rodapé dos Botões (Opcional):** texto abaixo dos botões, até 60 caracteres.

◽ **Mensagem de explicação do menu:** o texto que pergunta o que o cliente deseja.

Para todos os tipos:

🔘 **Adicionar Opção:** cria uma opção do menu, com o **Título** e, na lista, a **Descrição** opcional, de até 72 caracteres.

🔘 **Caminho alternativo (ELSE):** marcado, cria uma saída a mais para a resposta que não corresponde a nenhuma opção.

🔘 **Sem resposta: seguir pela saída depois de (minutos):** com minutos preenchidos, o bloco ganha a saída **Sem resposta**, para quem não responder nesse tempo. Vazio ou 0 desliga.

🔲 Para finalizar, clique em **Adicionar**.

⚠️ No **Menu em Botões**, a janela para na 3ª opção: o **Adicionar Opção** desliga, e aparece *"O Menu em Botões vai até 3 opções. Para mais, use o Menu em Lista."* Um bloco que já tenha mais de 3 opções, vindo de um fluxo importado ou antigo, mostra o aviso em vermelho. Esse menu não chega ao cliente: a conversa ganha a nota interna *Máximo de 3 botões permitido* e o fluxo fica parado no bloco, até o prazo do **Sem resposta**, se houver.

⚠️ O **Rodapé da Lista** pode não aparecer para o cliente, conforme o canal. Não coloque nele uma informação de que a pessoa precise para escolher.

## Dados e variáveis no texto do menu

O bloco **Menu** aceita os dados do contato e do atendimento, como `{{ms}}` (a saudação), `{{firstName}}` (o primeiro nome) e `{{protocol}}` (o protocolo). Eles são trocados na mensagem, no cabeçalho, no rodapé, no texto do botão da lista e também nas opções: no **Menu em Lista**, uma opção *Olá * chega ao cliente como *Olá Maria*.

As variáveis do próprio fluxo, escritas entre porcentagens, como `%nome%`, são trocadas na mensagem e **também nas opções**. Variável que o fluxo ainda não guardou aparece escrita como está.

## As saídas do bloco Menu

No desenho, o bloco mostra a mensagem e as opções numeradas, como *[1] Vendas* e *[2] Suporte*, e tem **uma saída para cada opção**. Ligue cada uma ao caminho daquela escolha. No **Menu em Botões**, tocar num botão também segue pela saída daquela opção.

◽ Com o **Caminho alternativo (ELSE)** marcado, aparece a saída **Resposta inválida**, para quem responder algo fora das opções.

◽ Com **Sem resposta** preenchido, aparece a saída **Sem resposta**, com o tempo escolhido.

## Quando a resposta não é uma das opções

➡️ **Com o Caminho alternativo (ELSE):** o fluxo segue pela saída **Resposta inválida**.

➡️ **Sem o Caminho alternativo (ELSE):** o bloco **Menu** envia o mesmo menu de novo, sem mensagem de erro, e continua esperando.

➡️ **Áudio em resposta a um Menu em Texto:** o bloco **Menu** não reage. O menu não é reenviado, o áudio não conta como escolha, e o fluxo segue pela saída **Sem resposta** quando o prazo acaba.

## Como usar a escolha do cliente depois do Menu

Para guardar a escolha, ponha um bloco **Variável** logo depois do **Menu**: ela guarda a opção que o cliente escolheu. Uma **Condição** logo depois do **Menu** compara a opção escolhida.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Quantas opções cabem no bloco Menu?** No **Menu em Botões**, até 3, e a janela não deixa criar a 4ª. No **Menu em Texto**, não há limite de opções, e a janela não limita o tamanho de cada uma.
>
> **O que acontece se o cliente responder algo fora das opções do Menu?** Com o **Caminho alternativo (ELSE)** marcado, o fluxo segue pela saída **Resposta inválida**, onde você pode explicar e mostrar o menu de novo. Sem ele, o mesmo menu é enviado outra vez.
>
> **O cliente não escolheu nenhuma opção do Menu. O fluxo fica parado?** Fica esperando a resposta. Para seguir depois de um tempo, preencha **Sem resposta** e ligue essa saída.
>
> **Posso usar o nome do cliente no bloco Menu?** Pode, com `{{firstName}}`: na mensagem, no cabeçalho, no rodapé, no botão da lista e nas opções do **Menu em Lista**. As variáveis do fluxo, como `%nome%`, também funcionam nas opções.
>
> **Como guardo a opção que o cliente escolheu no Menu?** Com um bloco **Variável** logo depois do **Menu**. Ela guarda a opção que o cliente escolheu, para usar adiante no fluxo.
>
> **O cliente respondeu a um menu antigo, depois que o fluxo já tinha seguido. O que vale?** A resposta vale para o bloco em que o fluxo está agora. Se o fluxo já seguiu pelo **Sem resposta** e voltou ao menu principal, por exemplo, é o menu principal que recebe a resposta.
>
> **Qual a diferença entre o Menu em Botões e o bloco Botões?** No **Menu em Botões**, cada botão tem a sua saída e leva a um caminho diferente. O bloco **Botões** tem uma saída só, e serve para enviar links, códigos para copiar e respostas prontas.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Mais de 3 opções no Menu em Botões, num fluxo importado ou antigo:** a janela mostra o aviso em vermelho, o menu não é enviado, e a conversa ganha a nota interna *Máximo de 3 botões permitido*. **Solução:** tire as opções que passam de 3, ou troque para **Menu em Lista** ou **Menu em Texto**.
>
> **Opções numeradas na mensagem do Menu em Texto:** a plataforma já acrescenta a lista numerada, e as opções aparecem repetidas. **Solução:** escreva na mensagem só a pergunta.
>
> **Opção longa demais na lista ou nos botões:** o campo não aceita mais de 20 caracteres. **Solução:** use títulos curtos e ponha o detalhe na **Descrição**, no **Menu em Lista**.
>
> **Saída de opção sem ligação:** o cliente escolhe a opção e o fluxo para ali. **Solução:** ligue todas as saídas, inclusive **Resposta inválida** e **Sem resposta**, quando existirem.
