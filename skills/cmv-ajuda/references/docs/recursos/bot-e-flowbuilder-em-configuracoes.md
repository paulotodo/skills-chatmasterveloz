# Bot e FlowBuilder Nativo em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bot-e-flowbuilder-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Automação em Configurações › Bot e FlowBuilder Nativo em Configurações

---

🧩 A seção **Bot e FlowBuilder Nativo** ajusta o que o cliente recebe da automação antes de chegar a um atendente: o menu de Setores, a saudação e a posição na espera ao entrar num Setor, a junção das mensagens que ele manda em sequência e o limite de mensagens que o fluxo responde a um mesmo contato.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Automação**, seção **Bot e FlowBuilder Nativo**.
>
> ➡️ Escolha o **Tipo Chatbot**, as **Repetições do Bot** e o **Idioma do Bot** do menu de Setores.
>
> ➡️ Ajuste a saudação, a posição no Setor, a concatenação e o limite de mensagens do fluxo.

## O menu de Setores

Acesse o menu **Configurações  ›  Opções  ›  Automação**, seção **Bot e FlowBuilder Nativo**. Os três primeiros campos ajustam o menu que o cliente recebe quando a Conexão aponta para vários Setores: se ele vem como texto numerado ou como botões, quantas vezes se repete e em que idioma.

🔘 **Tipo Chatbot:** **Texto** manda o menu como lista numerada; **Botões em Lista** manda como opções clicáveis.

🔘 **Repetições do Bot:** quantas vezes o menu é reapresentado quando o cliente responde algo que não é uma opção — de **1** a **5**, ou **Infinito**.

🔘 **Idioma do Bot:** **Português**, **Inglês** ou **Español** — o idioma das mensagens automáticas do menu.

⚠️ **Tipo Chatbot**, **Repetições do Bot** e **Idioma do Bot** só têm efeito no caminho em que o cliente **escolhe o Setor pelo menu**. Com a Conexão apontando para um único Setor não há menu, e esses três campos não mudam nada.

## Saudação e posição no Setor

🔘 **Mensagem de Saudação para setor único?:** decide se o cliente recebe a **Mensagem de saudação** do Setor quando a Conexão aponta para um único Setor, sem menu de escolha. Com **Sim**, a saudação do Setor é enviada assim que o cliente escreve; com **Não**, ela não é enviada. Nos dois casos a saudação da Conexão fica de fora: com um Setor só, não há menu para ela abrir.

🔘 **Informar a Posição no Setor?** e **Mensagem de Posição no Setor:** com **Sim**, o cliente que entra num Setor e fica aguardando recebe, logo depois da saudação do Setor, a posição dele na espera — a contagem inclui todos os que aguardam naquele Setor, ele mesmo também. O texto vem de **Mensagem de Posição no Setor** e é seguido do número da posição. No texto, `{{ms}}` vira a saudação do horário (Bom dia, Boa tarde…) e `{{name}}`, o nome do cliente: com `{{ms}} *{{name}}*, sua posição na fila de atendimento é:`, a cliente Maria recebe pela manhã *"Bom dia Maria, sua posição na fila de atendimento é: 3"*. Quando o Setor escolhido tem **Opções do Chatbot**, a posição não é enviada enquanto o cliente escolhe a opção.

## Concatenação no FlowBuilder Nativo

🔘 **Concatenação no FlowBuilder Nativo?** e **Tempo de Concatenação:** com **Sim**, as mensagens que o **cliente** manda em sequência são juntadas antes de o fluxo responder — e o tempo de espera vai de **2** a **10 segundos**. Serve para o fluxo não responder cada fragmento de frase.

⚠️ Esta concatenação é de **entrada** — junta o que o cliente escreve. A que junta o que o **atendente** escreve, para ser enviado como uma mensagem só, é outra: fica no card da Conexão oficial, no botão **Concatenador**, e vai de 2 a 60 segundos. As duas se chamam "concatenação" e não são a mesma coisa.

## Limite de mensagens do fluxo

🔘 **Limitar as mensagens que o fluxo responde ao mesmo contato?:** protege contra quem fica disparando o fluxo sem parar. Com **Sim**, defina o limite:

◽ **Máximo de mensagens do mesmo contato:** quantas mensagens o fluxo responde a um mesmo contato.

◽ **Contadas dentro de:** a janela de tempo, em minutos, em que essas mensagens são contadas.

◽ **Ao passar do limite, pausar o robô por:** por quantas horas o fluxo deixa de responder àquele contato.

Passou do limite, o fluxo deixa de responder a esse contato pelo tempo escolhido, e o atendimento fica em **Aguardando** para a equipe, com um aviso na conversa.

Para retomar antes do prazo, o cadastro do contato mostra o aviso de que a automação está pausada para ele, com a data, e o botão **Retomar o robô agora**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Escolhi Botões em Lista no Tipo Chatbot e o cliente continua recebendo texto.** O formato depende do canal da Conexão. Se não aparecer como botão, o canal não suporta e a plataforma cai para texto.
>
> **Minha Conexão tem um Setor só. O cliente recebe a saudação do Setor?** Depende de **Mensagem de Saudação para setor único?**, nesta seção: com **Sim**, recebe assim que escreve; com **Não**, não recebe.
>
> **O cliente deveria saber quantos estão na frente dele. Onde ligo isso?** Em **Informar a Posição no Setor?**, nesta seção: com **Sim**, quem entra num Setor e aguarda recebe a posição logo depois da saudação do Setor. O texto do aviso fica em **Mensagem de Posição no Setor**.
>
> **O fluxo responde cada palavra que o cliente manda.** Ligue **Concatenação no FlowBuilder Nativo?** e dê um **Tempo de Concatenação** de alguns segundos.
>
> **Um contato fica mandando mensagem sem parar e o fluxo responde a todas.** Ligue **Limitar as mensagens que o fluxo responde ao mesmo contato?** e defina o máximo, a janela de tempo e a pausa.
