# Permissões CRM

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/quem-visualiza-o-que-no-crm
- **Categoria:** Recursos
- **Menu:** CRM › Permissões CRM

---

🧩 O CRM não mostra a mesma coisa para todo mundo, nem deixa todo mundo fazer o mesmo. O que cada pessoa vê, cria, edita e exclui depende de três coisas: o **perfil** dela, os **funis liberados** para ela e as opções de cada funil. Entender essa combinação resolve a dúvida mais comum: *"meu vendedor abriu o Board e não vê nada"*.

## O que cada perfil faz                                                                                                                                                

| No CRM | Administrador | Supervisor | Atendente |
|---|---|---|---|
| Itens do menu **CRM** | todos | os mesmos do administrador; a **Auditoria de Vendas** só com a permissão | **Board**, **Propostas**, **Relatório de vendas** e **Minha evolução** |
| Funis que enxerga | todos | os liberados para ele e os que ele cria | só os liberados para ele |
| Criar, editar e excluir funis e etapas | sim | sim | não |
| Liberar funil para a equipe (**Quem acessa**) | sim | não | não |
| **Cadastros do CRM**: origens de venda e motivos de perda | sim | sim | não |
| **Produtos** | sim | sim | não |
| Criar e editar oportunidades | sim | sim | sim |
| Trocar o responsável da oportunidade | sim | sim | não |
| Excluir oportunidade | sim | sim | não |
| Devolver venda ganha ou perdida ao funil | sim | não | não |
| Propostas na lista | todas | todas | só as próprias |
| Excluir proposta de outra pessoa | sim | sim | não |
| **Dados da proposta** (botão **Configurar**) | sim | sim | sim |
| Metas do **Ranking** | sim | sim | não |
| **Minha evolução** | sim | sim | sim |
| Regras de **pontuação e níveis** | sim | sim | não |
| **Prêmios para resgate**: cadastrar e apagar prêmios | sim | sim | não |
| **Pedidos de resgate**: aprovar, recusar e entregar | sim | sim | não |
| Trocar pontos por prêmio (**Resgatar**) | sim | sim | sim |
| **Unidades e equipes** e **Metas da campanha** | sim | não | não |
| **Painel de metas** | todas as equipes | só as equipes que ele lidera | não |
| **Leads de anúncio** | sim | sim | não |

Na oportunidade, quem não pode trocar o responsável nem excluir não vê o campo **Responsável** nem o botão **Excluir**.

⚠️ Os **Dados da proposta** valem para todas as propostas da empresa — nome, documento, contato, validade, observações e logo — e o atendente também consegue alterá-los.

⚠️ Num funil **Compartilhado**, o atendente vê e edita as oportunidades de toda a equipe, não só as dele.

## O perfil

➡️ **Administrador:** vê todos os funis, sem precisar de liberação. É o único que define quem acessa cada funil e que monta o checklist da auditoria.

➡️ **Supervisor:** dentro dos funis liberados para ele, vê tudo — as oportunidades de todos, os ganhos e as perdas. Cria e edita funis, transfere e exclui oportunidades e altera cadastros, produtos, metas e as regras de pontuação. Cadastra prêmios, decide os pedidos de resgate e, no **Painel de metas**, acompanha as equipes que lidera. Não libera funis para a equipe nem monta unidades, equipes e metas da campanha.

➡️ **Atendente:** trabalha nas oportunidades dos funis liberados para ele. No menu **CRM** ele tem **Board**, **Propostas**, **Relatório de vendas** e **Minha evolução**. Não transfere nem exclui oportunidade e não altera os cadastros. No **Relatório de vendas** e em **Propostas**, vê só o que é dele.

## Os funis liberados

O acesso a um funil é dado no menu **CRM  ›  Funis**, pelo botão **Quem acessa** daquele funil. O cadastro da pessoa também permite escolher os funis dela, no campo **Funis do CRM que esta pessoa acessa**, aba **Setores e Conexões**, no menu **Equipe  ›  editar o usuário**.

Sem nenhum funil liberado, a pessoa continua vendo o menu **CRM**, mas o Board abre sem funil — o atendente lê *"Você ainda não tem acesso a nenhum funil. Peça ao administrador."*

⚠️ A liberação vale também para o supervisor: ele só enxerga os funis liberados para ele — o funil que ele mesmo cria já fica liberado. Quem vê todos os funis sem liberação é só o administrador.

## As opções de cada funil

🔘 **Visibilidade Compartilhado:** quem acessa o funil vê as **oportunidades** de toda a equipe nele.

🔘 **Visibilidade Individual:** cada atendente vê só as **próprias oportunidades**, e o Board avisa *"Funil individual — você vê só as suas"*. Administrador e supervisor continuam vendo tudo.

🔘 **Ocultar ganhas e perdidas do vendedor:** o atendente deixa de ver no Board as colunas de ganho e de perda e os totais delas — fica à vista só o que está em negociação. Ele continua podendo marcar uma oportunidade como ganha ou perdida pela **Etapa do Funil**, dentro da própria oportunidade.

## Depois da venda ganha ou perdida

➡️ A oportunidade trava campos: o atendente encontra **Produto**, **Valor** e **Origem da venda** travados; o supervisor, **Produto** e **Valor**.

➡️ Só o administrador devolve uma venda ganha ou perdida para uma etapa em andamento. Quem tenta sem ser administrador recebe *"Só administradores podem devolver uma venda ganha ou perdida ao funil."*

## A auditoria

➡️ O item **Auditoria de Vendas** aparece no menu do administrador e de quem tem a permissão **Pode Auditar Vendas (CRM)**, depois que as vendas começam a passar pela auditoria. A permissão fica no menu **Equipe  ›  editar o usuário  ›  Permissões**.

➡️ Com essa permissão, o supervisor confere e aprova vendas de outras pessoas. O **Checklist da empresa**, que diz o que todo auditor confere, só o administrador monta.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Meu vendedor abriu o Board e não vê nenhum funil.** Falta liberar o funil para ele. O administrador faz isso no menu **CRM  ›  Funis**, pelo botão **Quem acessa** do funil.
>
> **O supervisor não vê um funil que o administrador vê.** O supervisor também precisa ser liberado no funil. Só o administrador enxerga todos sem liberação.
>
> **O vendedor não vê as vendas ganhas no Board.** O funil está com **Ocultar ganhas e perdidas do vendedor** ligado. Administrador e supervisor seguem vendo as colunas de ganho e de perda.
>
> **O vendedor não consegue mudar o valor de uma venda ganha.** Depois de ganha, a oportunidade trava Produto, Valor e Origem da venda para ele. Peça a alteração a um administrador.
>
> **Por que o supervisor não vê o Checklist da empresa na Auditoria?** O checklist é montado só pelo administrador, mesmo quando o supervisor tem a permissão **Pode Auditar Vendas (CRM)**.
>
> **O atendente pode excluir uma oportunidade?** Não. O botão **Excluir** não aparece para ele — peça a um supervisor ou ao administrador.
>
> **Quem libera um funil para a equipe?** Só o administrador, pelo botão **Quem acessa**. O supervisor cria e edita funis, mas não libera.
>
> **O atendente não acha a proposta que um colega gerou.** Em **Propostas**, o atendente vê só as próprias. Administrador e supervisor veem todas.
