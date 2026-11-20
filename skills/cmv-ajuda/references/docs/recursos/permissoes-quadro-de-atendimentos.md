# Permissões Quadro de Atendimentos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/permissoes-quadro-de-atendimentos
- **Categoria:** Recursos
- **Menu:** Quadro de Atendimentos › Permissões Quadro de Atendimentos

---

🧩 O menu do **Quadro de atendimentos** aparece para administrador, supervisor e atendente, mas o que cada um encontra ao entrar é diferente. É a causa mais comum de um atendente dizer que a tela está vazia.

## O que cada perfil faz no quadro                                                            

|  | Administrador | Supervisor | Atendente |
|---|---|---|---|
| Quadros que enxerga | todos da empresa | todos da empresa | só os atribuídos a ele |
| **Configurar quadros** (criar, renomear, colunas, excluir) | ✔️ | ✔️ | ❌ |
| Botão de encerrar nos cards | ✔️ | ✔️ | ❌ |
| Filtro de **Usuários** e **Mostrar só os meus atendimentos** | ✔️ | ✔️ | ❌ |
| Ler a última mensagem e abrir a conversa pelo card | ✔️ | ✔️ | conforme **Operador Visualiza Prévias** |
| Regras próprias | ✔️ | ✔️ | ✔️ |
| Regras da equipe | cria | cria | vê, não altera |
| **Escolher tags** na visão por Tags | ✔️ | ✔️ | ✔️ |

## Administrador e supervisor

Enxergam **todos os quadros da empresa**, sem precisar de atribuição, e são os únicos que veem o botão **Configurar quadros** — criam, renomeiam e excluem quadros e colunas. Também são os únicos com o interruptor que mostra o **FINALIZAR** nos cards, com o filtro de **Usuários** e com o botão de **mostrar só os meus atendimentos**.

Administrador e supervisor leem a última mensagem e abrem a conversa de qualquer card, com dois cliques — o pendente inclusive, numa janela com o botão **Aceitar**.

## Atendente

Enxerga **apenas os quadros atribuídos a ele**. Sem atribuição, a tela abre com o recado *"Você ainda não tem nenhum quadro. Peça ao administrador para atribuir um"*.

A barra dele é menor: tem a busca por nome ou número, **Novo atendimento**, **Atualizar**, **Regras do quadro**, o filtro de sem resposta e os filtros de Conexões, Setores e Grupos — e não tem Configurar quadros, nem o interruptor do FINALIZAR, nem o filtro de Usuários, nem o botão de mostrar só os seus.

Na **coluna automática**, cada pessoa vê só os pendentes dos Setores dela. A mesma coluna pode mostrar números diferentes para o gestor e para o atendente.

## O que o atendente lê e abre no card

Depende da opção **Operador Visualiza Prévias**, no menu **Configurações  ›  Opções  ›  Atendimento**, seção **Atendimento e operador**. Com ela ligada, o atendente lê a última mensagem nos cards e abre a conversa com dois cliques — o pendente inclusive, numa janela com o botão **Aceitar**.

Com a opção **Operador Visualiza Prévias** desligada, os cards não mostram a última mensagem ao atendente e o quadro não abre a conversa para ele: os dois cliques mostram *Mova o atendimento para atender antes de abrir a conversa*. Administrador e supervisor continuam lendo e abrindo.

## Quem vê e quem altera as regras do quadro

Para administrador e supervisor, as regras do quadro ficam em duas abas, **Minhas regras** e **Regras da equipe**.

🔘 **Regras da equipe:** criadas por administrador ou supervisor para um quadro, valem para quem usa aquele quadro — todos, ou só as pessoas marcadas — e **rodam antes** das regras de cada pessoa. Quem usa o quadro **vê essas regras, mas não altera**.

🔘 **Minhas regras:** as regras de cada pessoa, que só valem para os atendimentos dela.

**Quem usa o quadro** é quem o tem atribuído no cadastro. A regra da equipe só move atendimentos dessas pessoas — o atendimento de quem não tem o quadro atribuído fica de fora. Administrador e supervisor, que não recebem atribuição, também ficam de fora: para os próprios atendimentos, os dois usam **Minhas regras**.

O atendente com quadro atribuído também cria as próprias regras. Para ele a janela não tem abas: mostra **Da equipe (rodam antes das suas)**, só para leitura, e **Suas regras**, com o botão **Nova regra**.

⚠️ Sem quadro aberto, o botão **Regras do quadro** não aparece. Atendente sem quadro atribuído não chega às regras.

## Tags pelo quadro

Na visão por **Tags**, arrastar o card põe ou troca a tag do atendimento, e o arrasto respeita as permissões do cadastro da pessoa, na aba **Permissões**: sem **Pode Atribuir Tag no Atendimento**, o atendente não põe tag arrastando; sem **Pode Remover Tag do Atendimento**, não troca nem tira.

A escolha das tags que viram colunas, em **Escolher tags**, é de cada pessoa e fica salva na conta dela — o que um marca não muda o quadro do outro.

## Como atribuir um quadro a alguém

Acesse o menu **Equipe  ›  editar o usuário  ›  aba Setores e Conexões** e preencha o campo **Quadros de atendimento**.

⚠️ **O campo só existe para quem tem perfil User.** Em cadastro de administrador ou de supervisor ele não aparece — e não é falha: os dois já veem todos os quadros.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O atendente abriu o Quadro de atendimentos e não apareceu nada.** Nenhum quadro foi atribuído a ele. Isso se resolve no cadastro dele, na aba Setores e Conexões, campo **Quadros de atendimento**.
>
> **Sou administrador, abri o Quadro de atendimentos e está escrito que não há nenhum quadro.** Nenhum quadro foi criado ainda: a própria tela oferece o botão para criar o primeiro.
>
> **Atribuí o quadro e ele continua sem ver.** Peça para sair e entrar de novo: quem já estava logado continua com as permissões antigas até renovar a sessão.
>
> **Preciso atribuir quadro para o supervisor?** Não. Administrador e supervisor enxergam todos os quadros da empresa.
>
> **O atendente pode mudar uma regra da equipe?** Não. Ele vê as regras da equipe do quadro que usa, mas só administrador e supervisor criam e alteram.
>
> **O atendente pode transferir um atendimento de Setor arrastando?** Pode, se o quadro dele tiver uma coluna automática de um Setor só. A confirmação aparece para ele igual aparece para o gestor.
>
> **Os quadros de uma empresa aparecem em outra?** Não. Cada empresa monta os seus, e um quadro nunca atravessa para a outra.
