# Rodízio de Atendimento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/rodizio-de-atendimento
- **Categoria:** Recursos
- **Menu:** Atendimento Otimizado › Rodízio de Atendimento

---

🧩 O **rodízio de atendimento** divide as conversas de forma equilibrada entre os atendentes da sua equipe. Cada um recebe a sua vez, ninguém fica sobrecarregado e o cliente não espera alguém escolher a conversa na lista.

Este rodízio é montado com **dois Setores** e funciona no **menu do chatbot** da Conexão: um Setor recebe a conversa e faz a distribuição, e o outro reúne os atendentes que participam.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Crie o Setor de **Atendimento Randomizado** e dê acesso a ele aos atendentes que vão participar.
>
> ➡️ No menu **Configurações  ›  Opções  ›  Atendimento**, seção **Distribuição e rodízio**, escolha quem entra no sorteio em **Modo de Randomização de Atendimento**.
>
> ➡️ Crie o Setor de **Rodízio**, sem nenhum atendente, com **Rodízio de Atendentes** ligado, o **Tempo de Escala** e o **Mover** apontando para o Setor de Atendimento Randomizado.
>
> ➡️ Marque o Setor de Rodízio na Conexão, junto com os outros Setores do menu, para o cliente poder escolhê-lo.

## Os dois Setores do rodízio

🔘 **Setor de Atendimento Randomizado:** para onde a conversa vai depois do sorteio. Os atendentes que participam do rodízio **devem** ter acesso a ele.

🔘 **Setor de Rodízio:** o Setor que distribui o atendimento. **Nenhum** atendente deve ter acesso a ele. É o Setor de Rodízio que aparece como opção no menu do chatbot, então dê a ele o nome que o cliente deve escolher — por exemplo, *Vendas*.

## Como criar o Setor de Atendimento Randomizado

Acesse o menu **Setores & Chatbot  ›  ADICIONAR SETOR**

Crie o Setor com o nome que preferir — por exemplo, *Atendimento Randomizado*. É nele que os atendentes do rodízio precisam estar.

![Cadastro do Setor de Atendimento Randomizado](https://clihelper.chatmasterveloz.com/docs-imagem/18291-rodizio_atendimento.jpg)

Depois, dê acesso a esse Setor para cada atendente que vai participar:

Acesse o menu **Equipe  ›  editar o usuário**

🔘 **Setores:** marque o Setor de Atendimento Randomizado entre os Setores que o atendente acessa.

![Cadastro do usuário com o Setor de Atendimento Randomizado marcado](https://clihelper.chatmasterveloz.com/docs-imagem/18291-rodizio_equipe.jpg)

⚠️ Quem não tem acesso ao Setor de Atendimento Randomizado fica fora do sorteio.

## Quem entra no sorteio

Acesse o menu **Configurações  ›  Opções  ›  Atendimento**, seção **Distribuição e rodízio**

🔘 **Modo de Randomização de Atendimento:** **Somente Usuários Online** sorteia só entre quem está on-line no momento; **Usuários Online e Offline** inclui também quem está off-line.

![Opção Modo de Randomização de Atendimento em Configurações](https://clihelper.chatmasterveloz.com/docs-imagem/18291-rodizio-online-offline.jpg)

## Como criar o Setor de Rodízio

⚠️ Nenhum atendente deve ter acesso a este Setor.

Acesse o menu **Setores & Chatbot  ›  ADICIONAR SETOR**

![Cadastro do Setor de Rodízio com Rodízio de Atendentes, Tempo de Escala e Mover](https://clihelper.chatmasterveloz.com/docs-imagem/18291-rodizio_configuracoes.jpg)

🔘 **Rodízio de Atendentes:** ligado.

🔘 **Tempo de Escala:** quanto tempo o sistema espera antes de fazer o rodízio — de 2 a 60 minutos.

🔘 **Mover:** o Setor de Atendimento Randomizado, onde estão os atendentes que participam.

## Como iniciar um rodízio

O rodízio de Setores funciona no **chatbot**: a Conexão precisa ter **mais de um Setor**, para o cliente receber o menu de escolha, e o Setor de Rodízio precisa estar entre eles.

Acesse o menu **Conexões  ›  editar a Conexão  ›  aba Setores & Tempos**

🔘 **Setores:** marque o Setor de Rodízio junto com os outros Setores que aparecem no menu.

Quando o cliente escolhe o Setor de Rodízio no menu, a conversa espera o **Tempo de Escala**. Depois, ela é sorteada entre os atendentes com acesso ao Setor de Atendimento Randomizado e chega ao escolhido já no status **Atendendo**.

⚠️ Com um Setor só na Conexão não há menu, e o rodízio de Setores não acontece. Nesse caso a distribuição é feita pelo fluxo, com o bloco **Rodízio** no menu **FlowBuilder Nativo**.

## O que o cliente recebe no rodízio

Quando a conversa é sorteada, o cliente recebe a **Mensagem de Encaminhamento** — por exemplo, *"Bom dia Maria, em alguns instantes um atendente irá prosseguir com seu atendimento."* A saudação do Setor de Atendimento Randomizado não é enviada.

O texto da Mensagem de Encaminhamento vale para toda a empresa e se ajusta no menu **Configurações  ›  Opções  ›  Automação**, seção **Mensagens automáticas**.

## Como avisar o atendente no WhatsApp

O atendente pode ser avisado no WhatsApp pessoal quando receber uma conversa pelo rodízio.

Acesse o menu **Setores & Chatbot  ›  editar o Setor**

🔘 **Notificar Operador no WhatsApp:** ligue no Setor de **Atendimento Randomizado**.

⚠️ O aviso vai para o telefone cadastrado no usuário, em **Equipe**, no padrão DDI + DDD + número — por exemplo, 5511912345678.

![Opção Notificar Operador no WhatsApp no cadastro do Setor](https://clihelper.chatmasterveloz.com/docs-imagem/18291-rodizio_notificar_atendente.jpg)

O texto do aviso é a **Mensagem de Notificação Externa** — por exemplo, *"Existe atendimento aguardando sua atenção na plataforma."* Ele se ajusta no menu **Configurações  ›  Opções  ›  Automação**, seção **Mensagens automáticas**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O rodízio de atendimento funciona numa Conexão com um Setor só?** Não. O rodízio de Setores depende do menu do chatbot, que só existe com dois ou mais Setores na Conexão. Com um Setor só, a distribuição é feita pelo bloco **Rodízio** no menu **FlowBuilder Nativo**.
>
> **Quem está off-line entra no rodízio de atendimento?** Depende da opção **Modo de Randomização de Atendimento**, no menu **Configurações  ›  Opções  ›  Atendimento**, seção **Distribuição e rodízio**: em **Somente Usuários Online**, não; em **Usuários Online e Offline**, sim.
>
> **Quanto tempo a conversa espera antes do rodízio?** O **Tempo de Escala** do Setor de Rodízio — de 2 a 60 minutos.
>
> **Que mensagem o cliente recebe quando o rodízio passa a conversa para um atendente?** A **Mensagem de Encaminhamento**, ajustada no menu **Configurações  ›  Opções  ›  Automação**, seção **Mensagens automáticas**. A saudação do Setor de Atendimento Randomizado não é enviada.
>
> **O cliente escolheu o Setor de Rodízio no menu e a conversa não foi distribuída. O que conferir?** Se o Setor de Rodízio tem **Rodízio de Atendentes** ligado, um **Tempo de Escala** escolhido e o **Mover** apontando para o Setor de Atendimento Randomizado, e se algum atendente com acesso a esse Setor entra no sorteio — on-line, quando o **Modo de Randomização de Atendimento** está em **Somente Usuários Online**.
>
> **O atendente não recebeu o aviso no WhatsApp. O que conferir?** Se o **Notificar Operador no WhatsApp** está ligado no Setor de Atendimento Randomizado e se o telefone do usuário, em **Equipe**, está no padrão DDI + DDD + número.
