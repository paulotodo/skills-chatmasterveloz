# Permissões Dashboard

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/permissoes-dashboard
- **Categoria:** Recursos
- **Menu:** Dashboard › Permissões Dashboard

---

🧩 O **Dashboard** é uma tela de gestão: aparece para o administrador e para o supervisor. O administrador enxerga os números da empresa inteira; o supervisor também, ou só os dos Setores dele, conforme o cadastro. O atendente não abre o Dashboard, mas pode ganhar a página **Meus números**, só com os números dele, quando o administrador liga essa opção.

## Quem vê o Dashboard                                                                                          

|  | Admin | Supervisor | User |
|---|---|---|---|
| **Dashboard** no menu | ✔️ | ✔️ | ❌ |
| Abrir a tela pelo endereço | ✔️ | ✔️ | ❌ volta aos Chats |
| Números da empresa inteira | ✔️ | ✔️ (sem a restrição de setores) | — |
| Só os números dos Setores dele | — | com **Restringir acesso apenas aos setores específicos** | — |
| **Dashboard** como **Página inicial após o login** | ✔️ | ✔️ | ❌ |
| Alterar **Metas e limites** | ✔️ | ❌ só vê os valores | — |
| **Resumo automático** | ✔️ | ❌ | — |
| **Aviso dos alertas** | ✔️ | ❌ | — |
| **Visões** | ✔️ as dele | ✔️ as dele | — |
| **Modo TV** | ✔️ | ✔️ | — |
| **Transferir marcados** e **Distribuir entre os online**, nas listas | ✔️ | ✔️ | — |
| **Meus números** no menu | ❌ | ❌ | com **Atendente vê os próprios números** em **Sim**, também com **Acesso Limitado** |
| **Meus números** pelo endereço | — | ✔️ | com a opção em **Sim**, também com **Acesso Limitado** |

## Administrador e supervisor

Os dois perfis têm o **Dashboard** no menu, no grupo Principal. O administrador enxerga os números de toda a empresa: todos os Setores, todas as conexões e toda a equipe. O supervisor enxerga o mesmo enquanto a restrição de setores estiver desligada no cadastro dele, com ou sem Setor marcado.

Quase tudo o que o Dashboard oferece vale igual para os dois perfis: filtros, painéis, listas e as ações delas (**Transferir**, **Transferir marcados** e **Distribuir entre os online**), relatórios de qualquer pessoa da equipe, a exportação para Excel, as **Visões** e o **Modo TV**. Três coisas são só do administrador:

➡️ **Metas e limites:** o supervisor abre a janela e vê os valores, mas os campos ficam travados, com o aviso *Só o administrador altera as metas.*

➡️ **Resumo automático:** o botão não aparece para o supervisor.

➡️ **Aviso dos alertas:** o botão não aparece para o supervisor.

As **Visões** são de cada pessoa: a visão que o administrador salva não aparece para o supervisor, e a visão padrão de um não muda o Dashboard do outro.

## Supervisor com a restrição de setores

Com **Restringir acesso apenas aos setores específicos** em **SIM** no cadastro do supervisor, o Dashboard dele mostra só os atendimentos dos Setores marcados para ele na aba **Setores e Conexões**. A opção fica no menu **Equipe**: edite o supervisor e procure na aba **Geral** — ela aparece só quando o perfil é **Supervisor**. Quem liga a restrição é o administrador.

Com a restrição ligada, contam só os atendimentos dos Setores do supervisor:

➡️ Os três cards do topo: **Atendendo**, **Aguardando** e **Fechados**.

➡️ Os indicadores de **Estatísticas e Informações** e a **Linha do Tempo de Tickets**.

➡️ Em **Equipe & Canais**, os alertas **SLA Próximo do Vencimento** e **Tickets Sem Atendente**, os **Resolvidos** do **Ranking de Agentes** e os atendimentos de cada canal.

➡️ Em **Relatórios Detalhados**, o **Relatório por Período** e o **Relatório por Operador** — o de qualquer pessoa conta só o que ela atendeu nesses Setores.

➡️ As listas que abrem ao clicar num número, e o painel **Quanto a automação resolve**.

➡️ A exportação para Excel, com os mesmos números.

➡️ O **Dashboard (legado)**: os cards e a tabela da equipe.

As pessoas também se restringem: a lista **Selecionar Operador**, em **Relatórios Detalhados**, as linhas do **Ranking de Agentes** e a tabela da equipe do **Dashboard (legado)** trazem só as pessoas dos Setores do supervisor.

Os filtros dos **Filtros Avançados** também: **Setores** lista só os Setores dele e **Atendentes**, só as pessoas desses Setores. O campo **Tags** traz as tags da empresa. Pedir um Setor de fora não traz números dele.

Os contatos não se dividem por Setor: o **Total de Contatos** e os **Novos Contatos** continuam com os números da empresa inteira, assim como o card **Contatos** do **Dashboard (legado)**.

## Atendente

O perfil User não tem o **Dashboard** no menu. Quem digita o endereço da tela é levado de volta aos **Chats**, com o aviso *Você não possui permissão para acessar essa página! Estamos lhe redirecionando.* O mesmo vale para o atendente com **Acesso Limitado**.

O que o atendente pode ganhar é a página **Meus números**: quando o administrador liga **Atendente vê os próprios números**, no menu **Configurações  ›  Opções  ›  Atendimento**, o item **Meus números** aparece no menu dele, com os atendimentos encerrados, os tempos de primeira resposta e de resolução e as avaliações dele — só os dele. Com a opção em **Não**, a página mostra *O administrador ainda não liberou esta página.*

O atendente com **Acesso Limitado** também ganha o item: com a opção em **Sim**, o menu dele traz os **Chats** e o **Meus números**; com a opção em **Não**, só os **Chats**. O supervisor não tem o item no menu e abre a página pelo endereço.

## Abrir o Dashboard logo depois do login

Acesse o menu **Equipe**, edite a pessoa e, na aba **Geral**, escolha **Dashboard** em **Página inicial após o login**. A opção **Dashboard** só aparece na lista quando o perfil da pessoa é **Admin** ou **Supervisor**.

Sem escolha, em **Padrão (Chats)**, o login abre os Chats para todos os perfis.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O atendente pode ver os números dos próprios atendimentos?** Pode, pela página **Meus números**, quando o administrador liga **Atendente vê os próprios números** no menu **Configurações  ›  Opções  ›  Atendimento**. O Dashboard em si continua fechado para o perfil User. Para o administrador e o supervisor, os números de cada pessoa ficam também no **Relatório por Operador**, em **Relatórios Detalhados**.
>
> **O supervisor consegue mudar as Metas e limites do Dashboard?** Não. O supervisor abre a janela **Metas e limites** e vê o prazo do SLA, a meta de primeira resposta e o limite de atendente sobrecarregado, mas os campos ficam travados, com o aviso *Só o administrador altera as metas.*
>
> **O supervisor pode programar o Resumo automático do Dashboard?** Não. O botão **Resumo automático** aparece só para o administrador.
>
> **O supervisor pode configurar o Aviso dos alertas do Dashboard?** Não. O botão **Aviso dos alertas** aparece só para o administrador.
>
> **As Visões do Dashboard são da equipe toda?** Não. Cada pessoa tem as próprias **Visões**: a visão salva pelo administrador não aparece para o supervisor.
>
> **O atendente com Acesso Limitado vê o Meus números?** Vê. Com **Atendente vê os próprios números** em **Sim**, o menu do atendente com **Acesso Limitado** traz os **Chats** e o **Meus números**, com os números dele. Com a opção em **Não**, o menu dele fica só com os **Chats**.
>
> **Preciso ligar Setores ao supervisor para ele ver o Dashboard?** Não. Sem a restrição de setores, o supervisor vê o Dashboard da empresa inteira, com ou sem Setor no cadastro. Com **Restringir acesso apenas aos setores específicos** em **SIM**, ele vê só os números dos Setores marcados para ele.
>
> **O supervisor com a restrição de setores vê só os contatos dos Setores dele no Dashboard?** Não. O **Total de Contatos** e os **Novos Contatos** contam os contatos da empresa inteira; o que se restringe aos Setores dele são os atendimentos e as pessoas.
>
> **O supervisor com a restrição de setores vê toda a equipe em Selecionar Operador?** Não. A lista **Selecionar Operador** e o **Ranking de Agentes** trazem só as pessoas dos Setores dele, e o **Relatório por Operador** de cada uma conta só o que ela atendeu nesses Setores.
>
> **A restrição de setores vale também no Dashboard (legado)?** Vale: com **Restringir acesso apenas aos setores específicos** em **SIM**, o **Dashboard (legado)** do supervisor mostra só os atendimentos e as pessoas dos Setores dele. O card **Contatos** segue com a empresa inteira.
>
> **O supervisor com a restrição de setores consegue filtrar outro Setor no Dashboard?** Não. O campo **Setores** dos **Filtros Avançados** mostra só os Setores dele, e a plataforma não devolve números de outros Setores.
>
> **A opção Dashboard não aparece em Página inicial após o login.** O perfil da pessoa é **User**, e a opção só existe para os perfis **Admin** e **Supervisor**.
