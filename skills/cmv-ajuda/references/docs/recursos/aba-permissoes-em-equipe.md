# Aba Permissões em Equipe

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-permissoes-em-equipe
- **Categoria:** Recursos
- **Menu:** Equipe › Aba Permissões em Equipe

---

🧩 A aba **Permissões** afina o que a pessoa pode fazer dentro do que o perfil dela já libera. São opções de **SIM** ou **NÃO**, que ligam e desligam ações sem abrir nenhum menu que o perfil fechou, mais a lista de colegas cuja agenda a pessoa acompanha, o seletor de notificações e a restrição por endereço IP.

Não confunda com a seção **Atendimento e operador** do menu **Configurações  ›  Opções  ›  Atendimento**: aquela vale para todos os atendentes da empresa de uma vez. Esta é por pessoa.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Equipe**, edite a pessoa e abra a aba **Permissões**.
>
> ➡️ Ajuste as opções e salve. A pessoa não precisa sair: com **Acesso a Contatos** em **NÃO**, por exemplo, o menu **Contatos** some da tela dela em poucos segundos.

## Para quem vale cada opção

**Sempre:** o perfil já tem, e a opção não muda nada para ele. **Configurável:** vale o que estiver marcado no cadastro da pessoa.                                                                                                                        

| Opção | Admin | Supervisor | User |
|---|---|---|---|
| **Acesso Limitado** | configurável | configurável | configurável |
| **Inativar Usuário** | configurável | configurável | configurável |
| **Acesso a Contatos** | configurável | configurável | configurável |
| **Pode Criar Tags no Chat** | sempre | sempre | configurável |
| **Pode Atribuir Tag no Atendimento** | sempre | sempre | configurável |
| **Pode Remover Tag do Atendimento** | sempre | sempre | configurável |
| **Pode Usar o Bloco de Notas do Contato** | sempre | sempre | configurável |
| **Pode Auditar Vendas (CRM)** | sempre | configurável | configurável |
| **Pode ver o Ranking (CRM)** | sempre | sempre | configurável |
| **Pode usar sugestão de IA** | configurável | configurável | configurável |
| **Vê Resumo do Contato** | sempre | sempre | configurável |
| **Pode forçar envio pela conexão híbrida** | sempre | sempre | configurável |
| **Pode responder sem aceitar** | configurável | configurável | configurável |
| **Pode iniciar novos atendimentos** | configurável | configurável | configurável |
| **Ver a agenda de** | vê todas | vê todas | configurável |
| **Receber Notificações** e os três **Notificar** | configurável | configurável | configurável |
| **Alertas da Avaliação pela IA** | configurável | configurável | configurável, sem **Todos os atendentes** |
| **Restrição por IP (CIDR)** | configurável | configurável | configurável |

➡️ **Ver a agenda de** só aparece no cadastro do perfil **User**: administrador e supervisor já acompanham as tarefas de todos.

## Acesso

🔘 **Acesso Limitado:** com **SIM**, o menu da pessoa fica só com **Chats** — os outros itens que o perfil dela teria somem. É a opção para quem só atende. Com **NÃO**, o menu é o do perfil.

🔘 **Inativar Usuário:** com **SIM**, a pessoa não entra mais. É o jeito de desligar alguém sem excluir o cadastro e o histórico. Quem tenta entrar lê *Sua conta está inativa. Procure o administrador para reativá-la.*, e o card da pessoa mostra **Inativo**.

🔘 **Acesso a Contatos:** libera o menu **Contatos**. Com **NÃO**, o item some do menu e o endereço direto volta para os Chats.

🔘 **Acesso a Campanhas:** libera as **Campanhas** para a pessoa. A opção só aparece quando a empresa tem campanhas.

## Etiquetas

🔘 **Pode Criar Tags no Chat:** deixa a pessoa criar uma tag nova de dentro do atendimento. Com **NÃO**, o campo de tags do atendimento mostra *Selecione tags (criar desabilitado)* e só oferece as tags que já existem.

🔘 **Pode Atribuir Tag no Atendimento:** deixa a pessoa classificar a conversa com uma tag existente.

🔘 **Pode Remover Tag do Atendimento:** deixa a pessoa tirar uma tag da conversa. Com **NÃO**, ela classifica sem apagar o que a administração aplicou — e, no Kanban, não move o card entre raias, porque mover é trocar a tag.

## Ferramentas do atendimento

🔘 **Pode Usar o Bloco de Notas do Contato:** libera o bloco de notas do contato, com categoria, filtro e busca.

🔘 **Pode Auditar Vendas (CRM):** libera a **Auditoria de Vendas** do CRM para a pessoa: o item entra no menu **CRM** dela, e ela confere, aprova ou reprova as vendas que estão na fila de auditoria, inclusive as de outros vendedores. Configurar o **Checklist da empresa** continua sendo só do administrador.

🔘 **Pode ver o Ranking (CRM):** libera o **Ranking de Vendas** para o atendente. Com **SIM**, o item **Ranking** entra no menu **CRM** dele, e ele vê a tela inteira — as vendas de todos, as equipes e as unidades —, sem o botão **Configurar metas**: as metas continuam com administrador e supervisor. Com **NÃO**, o item não aparece e o endereço da tela leva de volta aos Chats. Administrador e supervisor veem o Ranking sempre.

🔘 **Pode acessar os Projetos:** libera os **Projetos** para a pessoa. Com **NÃO**, o item **Projetos** some do menu dela e o endereço da tela leva de volta aos Chats. Com **SIM**, o item volta. A opção só aparece quando a empresa tem Projetos.

🔘 **Pode usar sugestão de IA:** libera a sugestão de resposta com inteligência artificial no campo de mensagem.

🔘 **Vê Resumo do Contato:** libera o botão de resumo do contato para o atendente, no atendimento e em cada linha da lista do menu **Contatos**. Nas palavras da tela: *vale para o perfil de atendente; administrador e supervisor veem o botão sempre*.

🔘 **Pode deixar Resposta na Volta:** ao enviar um template pela tela de atendimento, a pessoa pode deixar pronta a mensagem que é enviada sozinha quando o contato responder.

🔘 **Pode forçar envio pela conexão híbrida:** no Modo Híbrido, deixa a pessoa marcar uma mensagem para ser enviada pela conexão híbrida, ignorando o percentual. Nas palavras da tela: *administradores e supervisores já podem*.

🔘 **Pode responder sem aceitar:** deixa a pessoa responder um atendimento que está em **Aguardando** sem aceitá-lo. A mensagem chega ao cliente e o atendimento continua aguardando, no mesmo Setor e sem dono; pela ajuda da tela, o agente de IA do Setor continua atendendo. Enquanto isso, o campo de mensagem avisa *Respondendo sem aceitar — o atendimento continua aguardando*. Com **NÃO**, é preciso aceitar antes de responder.

🔘 **Pode iniciar novos atendimentos:** decide se a pessoa abre atendimento novo por conta própria. Com **NÃO**, o botão **Novo** some da lista de atendimentos dela, e, no menu **Contatos**, cada linha perde **Iniciar conversa** e os outros atalhos que abrem conversa com o contato; a plataforma também recusa abrir um atendimento em nome dela. Aceitar, responder, devolver ao Setor e transferir continuam iguais. Com **SIM**, tudo volta.

## Agenda da equipe

🔘 **Ver a agenda de:** marque os colegas cujas tarefas esta pessoa acompanha, sem precisar compartilhar tarefa por tarefa. Com colegas marcados, o menu **Tarefas** dela ganha o filtro **Responsável**, que abre em **Minhas tarefas** e lista os colegas para marcar. Em branco, o filtro não aparece e a pessoa vê só as tarefas dela. A opção aparece para o perfil **User**.

## Notificações

O aviso de mensagem é a notificação do navegador — *Mensagem de* e o nome do contato, com o texto e a hora. Ele só aparece se o navegador da pessoa permitir notificações da plataforma.

🔘 **Receber Notificações de Grupos:** avisos de mensagens em grupos.

🔘 **Receber Notificações:** quais avisos de atendimento a pessoa recebe. **Todas**: os dos atendimentos dela e os do **Aguardando** dos Setores dela. **Somente Tickets Abertos**: só os dos atendimentos que estão com ela. **Nenhuma**: nenhum aviso, mesmo com as opções abaixo em **SIM**.

🔘 **Notificar mensagem nova nos próprios atendimentos:** avisa quando o cliente escreve num atendimento que está com esta pessoa. Com **NÃO**, essas mensagens chegam sem aviso.

🔘 **Notificar atendimento aguardando na fila:** avisa quando chega mensagem num atendimento sem atendente, num Setor desta pessoa. Com **NÃO**, essas mensagens chegam sem aviso. O supervisor recebe também o aviso de conversa que ainda não tem Setor.

🔘 **Notificar atendimento devolvido para a fila:** nas palavras da tela, *quando um atendimento volta ou é transferido para uma fila deste usuário*.

🔘 **Alertas da Avaliação pela IA:** quais avisos da **Avaliação pela IA** a pessoa recebe no sino da plataforma — nota baixa ou atendimento fora do processo. **Padrão do perfil**: o administrador e o supervisor recebem os da equipe, menos os que falam deles mesmos, e os outros perfis não recebem. **Todos os atendentes**, **Só os meus** e **Nenhum** trocam esse padrão para a pessoa. Nas palavras da tela, *"Todos" vale só para administrador e supervisor*.

## Restrição por IP

🔘 **Restrição por IP (CIDR):** os endereços IP ou faixas CIDR de onde esta pessoa pode entrar. Digite o endereço ou a faixa — por exemplo *192.168.1.0/24* — e use **Adicionar IP**; cada um vira um item que dá para remover. Em branco, o acesso é livre de qualquer lugar — a própria tela escreve *sem restrição de IP, acesso permitido de qualquer lugar*. Serve para prender o acesso de alguém à rede do escritório ou à VPN da empresa.

⚠️ Quem tenta entrar de um endereço fora da lista lê *Acesso negado. Seu IP não está autorizado para este usuário.*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Mudei uma permissão. A pessoa precisa sair e entrar de novo?** Não precisa sair. Com **Acesso a Contatos** em **NÃO**, por exemplo, o menu **Contatos** some da tela dela em poucos segundos.
>
> **Marquei Nenhuma em Receber Notificações. As opções Notificar ainda avisam?** Não. Com **Nenhuma**, a pessoa não recebe aviso de atendimento, mesmo com as três opções **Notificar** em **SIM**.
>
> **O atendente não foi avisado da primeira mensagem de um cliente novo.** É o esperado: a primeira mensagem chega antes de a conversa entrar num Setor, e o atendente só é avisado das conversas dos Setores dele. Da segunda mensagem em diante, ele é avisado. O supervisor é avisado já na primeira.
>
> **O supervisor não quer receber os alertas da Avaliação pela IA.** Na aba **Permissões** do cadastro dele, escolha **Nenhum** em **Alertas da Avaliação pela IA**. As opções de notificação de mensagem continuam como estão.
>
> **A pessoa não recebe aviso de mensagem nova.** Confira, nesta ordem: o navegador dela permite notificações da plataforma; **Receber Notificações** não está em **Nenhuma**; e a opção **Notificar** daquela situação está em **SIM**. Com **Somente Tickets Abertos**, as mensagens do Aguardando chegam sem aviso.
>
> **O atendente não vê o botão do resumo do contato na lista de Contatos.** **Vê Resumo do Contato** está em **NÃO**. Com **SIM**, o botão aparece no atendimento e em cada linha da lista do menu **Contatos**.
>
> **O atendente não consegue tirar uma tag que colocou por engano.** **Pode Remover Tag do Atendimento** está em **NÃO**. Ligue, ou peça para um supervisor remover.
>
> **O atendente não move o card no Kanban.** É a mesma opção: mover entre raias é remover uma tag e colocar outra. Sem **Pode Remover Tag do Atendimento**, o card fica preso.
>
> **Desliguei alguém e as conversas dela sumiram?** Não. **Inativar Usuário** só impede o login. As conversas continuam com ela até você usar **Transferir Tickets**, no **…** do card.
>
> **O atendente não vê o Ranking no menu CRM.** **Pode ver o Ranking (CRM)** está em **NÃO**. Com **SIM**, ele vê o Ranking de Vendas, sem o botão **Configurar metas**.
>
> **O atendente não vê o menu Projetos.** **Pode acessar os Projetos** está em **NÃO**. Com **SIM**, o item volta ao menu dele.
>
> **O atendente não tem o botão Novo para iniciar um atendimento.** **Pode iniciar novos atendimentos** está em **NÃO** no cadastro dele. Quem tenta abrir mesmo assim lê *Você não tem permissão para iniciar novos atendimentos. Peça a um administrador para liberar no seu cadastro.* Com **SIM**, ele volta a iniciar atendimentos.
>
> **O atendente escreve num atendimento em Aguardando e nada é enviado.** **Pode responder sem aceitar** está em **NÃO**: ele precisa aceitar o atendimento antes. Ligue a opção para quem deve responder sem assumir a conversa.
>
> **Marquei colegas em Ver a agenda de e a pessoa continua vendo só as tarefas dela.** No menu **Tarefas**, o filtro **Responsável** abre em **Minhas tarefas**; ela precisa marcar os colegas ali para ver a agenda deles. Se o filtro nem aparece para ela, a lista de **Ver a agenda de** está em branco.
>
> **Restringi o IP e a pessoa ficou sem entrar de casa.** É o efeito esperado: com **Restrição por IP (CIDR)** preenchida, só os endereços listados entram. Inclua o IP de casa ou a faixa da VPN, ou deixe o campo em branco.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Excluir a pessoa em vez de inativar:** o cadastro some e o histórico perde a referência. **Solução:** para desligar alguém, **Inativar Usuário** em **SIM**, e transfira os atendimentos antes.
>
> **Ligar Acesso a Campanhas para o atendente e ele não ver nada:** a empresa precisa ter campanhas habilitadas; a opção por pessoa não basta sozinha. **Solução:** confira primeiro se o menu Campanhas existe para o administrador.
