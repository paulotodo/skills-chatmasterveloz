# Aguardando x Atendendo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aguardando-x-atendendo
- **Categoria:** Recursos
- **Menu:** Chats / Tickets › Aguardando x Atendendo

---

🧩 Um ticket pode estar em três estados:

🔴 **Encerrado** (`closed`), 🟡 **Aguardando** (`pending`), 🟢 **Atendendo** (`open`)**.**

Cada estado te diz **quem é responsável pela conversa naquele momento** — ninguém, um bot, ou um atendente.

☑️ **Saiba onde está cada conversa:** o estado já mostra se o ticket precisa de gente, já tem alguém, ou foi resolvido.

☑️ **Distribui trabalho com clareza:** atendentes assumem só o que está livre; ninguém pisa no atendimento do outro.

☑️ **Evita cliente esquecido:** ticket parado em Aguardando muito tempo é preocupação — você consegue agir antes de perder o cliente.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Os três estados são 🔴 **Encerrado**, 🟡 **Aguardando** e 🟢 **Atendendo**.
>
> ➡️ “Ticket **aberto**” = está em **Aguardando ou Atendendo** (qualquer um que não seja Encerrado).
>
> ➡️ **Aguardando** = sem atendente humano (pode ter bot conversando).
>
> ➡️ **Atendendo** = com atendente humano.
>
> ➡️ A lista **Aguardando** segue a ordem de chegada, e o botão **Ordenar tickets** escolhe quem fica no topo: os **mais recentes** ou os **mais antigos**.

## 📘 Como funciona o status de um ticket

**Os três estados**

### 🔴 **Encerrado**

(`closed` no código) — ticket fechado. ▫️Aparece na aba **Encerrados/Resolvidos**.

Nenhum atendimento ativo dentro dele.

### 🟡 **Aguardando**

(`pending` no código) — ticket aberto, **sem atendente humano** atribuído. ▫️ Aparece na aba **Aguardando**.

Pode estar:  
- esperando alguém da equipe puxar; ou
- sendo atendido por uma **automação** (chatbot, FlowBuilder Nativo, IA) — ele continua em Aguardando enquanto não tem atendente humano.

### 🟢 **Atendendo**

(`open` no código) — ticket aberto, **com atendente humano** atribuído. ▫️ Aparece na aba **Atendendo**.

### **A palavra "aberto"**

Quando alguém fala que o ticket está **aberto**, está se referindo aos dois estados ativos juntos — **Aguardando + Atendendo**. A aba "Tickets Abertos" do produto mostra os dois; a aba "Encerrados" mostra os fechados.

## **Como é o fluxo de um ticket**

O ticket não precisa passar por todos os estados. Os caminhos mais comuns são:

Ticket está **Encerrado**:  
- **Cliente manda mensagem nova:** o ticket é aberto com um novo protocolo em 🟡 **Aguardando**.

Enquanto estiver no **Aguardando**, pode acontecer:  
- **Atendente puxar/aceitar o ticket** (ou algum atendente ou bot transferir pra ele) → 🟢 **Atendendo**.
- **Atendente responder sem aceitar** (com a permissão **Pode responder sem aceitar** no cadastro dele): a mensagem chega ao cliente e o atendimento continua em 🟡 **Aguardando**, no mesmo setor e sem dono.
- **Bot resolver sozinho:** automação encerra o ticket ainda em 🟡 Aguardando → 🔴 **Encerrado**, sem nunca passar por Atendendo.

Enquanto estiver no **Atendendo**, pode acontecer:  
- **Atendente devolver ao setor:** 🟢 Atendendo → 🟡 **Aguardando** de novo, mantendo o setor atual, e o atendimento volta à lista **Aguardando** como se tivesse acabado de chegar.
- **Atendente transfere pra outra pessoa:** ticket continua 🟢 Atendendo, agora com outro dono.
- **Atendente encerra:** vai pra 🔴 **Encerrado**.

Agora com o ticket **Encerrado** novamente:  
- **Cliente manda mensagem após encerrado:** ticket reabre em 🟡 Aguardando, com **um novo protocolo** dentro do mesmo número de ticket, e o ciclo reinicia.

Em qualquer transição, o **número do ticket não muda**. O que muda é o **protocolo** ativo dentro dele — cada vez que o ticket fecha e reabre, um novo protocolo nasce.

### O que o atendente consegue visualizar

Atendente só visualiza tickets em Aguardando dos **Setores** em que tem permissão. Atendente sem Setor configurado vê tela vazia — não é bug. O ticket existe, só não é dele.

## A ordem da lista Aguardando

A lista **Aguardando** segue a **ordem de chegada**, no sentido escolhido no botão **Ordenar tickets**, na barra da lista:

🔘 **Mais recentes primeiro:** quem acabou de chegar fica no topo.

🔘 **Mais antigos primeiro:** quem espera há mais tempo fica no topo, e a equipe atende primeiro quem está esperando há mais tempo.

A espera conta a partir do momento em que o atendimento entrou em 🟡 **Aguardando**, e não da primeira mensagem do cliente. Ao lado de cada atendimento da lista **Aguardando** aparece há quanto tempo ele espera, como *(agora mesmo)* ou *(1 min atrás)*.

Na lista **Aguardando**, o atendimento **mantém o lugar** quando:

➡️ O cliente manda mais mensagens, em qualquer uma das duas ordens.

➡️ O atendimento é transferido para outro Setor ou para outra pessoa da equipe sem ser aceito: ele continua em 🟡 **Aguardando**, no mesmo lugar e com o mesmo tempo de espera.

Na lista **Aguardando**, o atendimento **volta como recém-chegado** quando:

➡️ É devolvido ao Setor: a espera recomeça do zero.

➡️ Foi encerrado e o cliente volta a escrever: o ticket reabre em 🟡 **Aguardando**, com novo protocolo, como recém-chegado.

Quando alguém aceita o atendimento, ele sai da lista **Aguardando** e passa para 🟢 **Atendendo**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Como o ticket entra em Aguardando?** Quando o cliente manda mensagem em um ticket com status Encerrado.
>
> **Aguardando aparece pra todo mundo da empresa?** Não. Só aparece pra quem tem **permissão no setor** daquele ticket. Por isso atendente sem Setor configurado vê tela vazia.
>
> **Bot conversando com o cliente é Aguardando?** Sim. Enquanto não tem **atendente humano** atribuído, o ticket continua em Aguardando — mesmo que o bot esteja respondendo ativamente.
>
> **O bot pode encerrar o ticket sem passar por Atendendo?** Pode. Depende da programação.
>
> **Posso pular Aguardando e atender direto?** Pode. Pelo botão **NOVO** você inicia uma conversa do zero — esse ticket nasce em 🟢 Atendendo, com você como dono. O botão **NOVO** só aparece para quem está com **Pode iniciar novos atendimentos** em **SIM**, na aba **Permissões** do cadastro. Ao digitar o nome do contato, cada opção mostra o nome, o identificador do contato e as tags dele, o que ajuda a escolher o certo quando dois contatos têm o mesmo nome.
>
> **Devolver ao setor é o mesmo que encerrar e reabrir?** Não. **Devolver ao setor** mantém o ticket aberto, sem atendente e altera os status para 🟡 Aguardando de novo, mantendo o protocolo atual, e o atendimento volta à lista **Aguardando** como se tivesse acabado de chegar. **Encerrar** fecha o ticket e o protocolo.
>
> **Por que o cliente que mandou várias mensagens não sobe na lista Aguardando?** Porque a lista **Aguardando** segue a ordem de chegada: conta o momento em que o atendimento entrou em Aguardando, e mensagens novas não mudam o lugar, em nenhuma das duas ordens do botão **Ordenar tickets**.
>
> **Transferir de Setor faz o cliente perder o lugar na lista Aguardando?** Não. O atendimento transferido para outro Setor, ou para outra pessoa sem ser aceito, continua em 🟡 Aguardando com o mesmo tempo de espera e no mesmo lugar da ordem de chegada.
>
> **Dá para mostrar os mais recentes primeiro na lista Aguardando?** Dá. No botão **Ordenar tickets**, escolha **Mais recentes primeiro**: quem acabou de chegar fica no topo. Com **Mais antigos primeiro**, fica no topo quem espera há mais tempo.
>
> **Quando um ticket muda de setor?** Quando alguém usa **Transferir Ticket** e escolhe outro setor no momento da transferência. Devolver ao setor não troca setor — mantém o mesmo.
>
> **Dá para responder quem está em Aguardando sem assumir o atendimento?** Dá, com a permissão **Pode responder sem aceitar** no cadastro da pessoa: a mensagem chega ao cliente e o atendimento continua em 🟡 Aguardando, sem dono, e o campo de mensagem avisa *Respondendo sem aceitar — o atendimento continua aguardando*. Sem a permissão, é preciso aceitar antes.
>
> **Ticket pode ficar Aguardando pra sempre?** Pode, se ninguém puxar e nenhuma automação estiver configurada.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Confundir devolver ao setor com transferir.** Devolver tira você do atendimento e manda o ticket pra Aguardando do mesmo Setor, como recém-chegado. Transferir manda pra outra pessoa (e pode trocar de setor também).
>
> **Atendente sem permissão no setor ficando procurando ticket "que sumiu".** Aguardando é filtrado por setor. Se o atendente não tem acesso ao setor daquele ticket, ele não vê — não é bug.

#### 💡 Sugestões de Ouro  
- Use **Mover após (Aguardando)** pra evitar ticket parado. Se nada acontecer em X minutos, o sistema age sozinho.
- Use o **Avise-me** vinculado ao setor. Você é avisado no celular assim que entra um ticket novo no Aguardando desse Setor, sem precisar olhar a tela.
