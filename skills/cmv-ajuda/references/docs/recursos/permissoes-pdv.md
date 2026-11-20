# Permissões PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/permissoes-pdv
- **Categoria:** Recursos
- **Menu:** PDV › Permissões PDV

---

🧩 O PDV não mostra a mesma coisa para todo mundo. O que cada pessoa vê, vende, estorna e cancela depende do **perfil** dela: administrador, supervisor, atendente, **Entregador**, o perfil de quem só faz entregas, ou **Garçom**, o perfil de quem só lança pedidos nas mesas.

## O que cada perfil faz                                                                                                                              

| No PDV | Administrador | Supervisor | Atendente | Entregador | Garçom |
|---|---|---|---|---|---|
| Itens do menu **PDV** | todos | todos | **Pedidos**, **Balcão**, **Mesas e Comandas**, **Painel de pedidos** e **Caixa** | nenhum: vê só **Minhas entregas** | nenhum: vê só **Mesas e comandas** |
| Montar pedido na conversa | sim | sim | sim | não | não |
| Confirmar pedido com desconto acima do limite | sim | sim | não | não | não |
| Pedidos na lista **Pedidos** | todos | todos | só os dele | — | — |
| **Estornar** um pagamento | sim | sim | não | não | não |
| **Cancelar pedido** | sim | sim | só sem pagamento | não | não |
| **Caixa** | **Caixas da equipe** | **Caixas da equipe** | **Meus caixas** | o dele, em **Minhas entregas** | não |
| **Produtos** e **Relatório do PDV** | sim | sim | não | não | não |
| Ver o **Custo** do produto, o lucro e a margem | sim | sim | não | não | não |
| **Painel de pedidos** | todos os pedidos | todos os pedidos | todos os pedidos | não | não |
| **Aceitar** e **Recusar** o pedido novo no **Painel de pedidos** | sim | sim | sim | não | não |
| Ligar o aceite automático do **Painel de pedidos** | sim | sim | não: as opções ficam desativadas | não | não |
| **Opções do PDV** | sim | não | não | não | não |
| Receber o pagamento na porta e marcar a entrega | — | — | — | só nas entregas que estão com ele | — |

As **Opções do PDV** ficam no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**. Só o administrador abre esse menu.

O **Custo** do produto aparece só para administrador e supervisor, no cadastro do produto e no **Relatório do PDV**. O atendente vende o produto, com as variações e os adicionais, sem ver o custo dele.

## Na página Mesas e Comandas                                    

| Em **Mesas e Comandas** | Administrador | Atendente | Garçom |
|---|---|---|---|
| As abas **Mesas**, **Comandas**, **Reservas** e **Histórico** | sim | sim | sim |
| **Configurar**, que cria as mesas e as comandas | sim | não | não |
| **Lançar na mesa** | sim | sim | sim |
| **Taxa de serviço** e **Desconto na conta** | sim | sim, com o desconto até o **Desconto máximo do atendente** | não |

## O perfil Entregador

➡️ O **Entregador** é um perfil do cadastro de usuário, escolhido no menu **Equipe**, ao criar ou editar a pessoa.

➡️ Quem entra com o perfil **Entregador** não vê o menu nem os atendimentos: a plataforma inteira vira a tela **Minhas entregas**, com as entregas que estão com ele e o caixa dele.

➡️ Só aparece na hora de despachar um pedido quem tem o perfil **Entregador**.

## O perfil Garçom

➡️ O **Garçom** é um perfil do cadastro de usuário, escolhido no menu **Equipe**, ao criar ou editar a pessoa. Ele vem junto com a página **Mesas e Comandas**: quando ela não está no seu menu **PDV**, o **Garçom** também não aparece na lista de perfis.

➡️ Quem entra com o perfil **Garçom** não vê o menu nem os atendimentos: a plataforma inteira vira a tela **Mesas e comandas**, com o salão e a comissão dele no topo.

➡️ Na conta da mesa, o garçom transfere a mesa, muda as pessoas e o cliente, divide a conta, imprime a conta e lança pedidos. A taxa de serviço, o desconto, o pagamento, **Fechar mesa** e **Juntar com outra mesa** ficam com o caixa.

➡️ O garçom tira item só da rodada que ele mesmo lançou e que ainda está *Confirmado*. A rodada em preparo, ou lançada por outra pessoa, só a gestão tira.

➡️ Na aba **Reservas**, o garçom vê as reservas do dia só com o botão **Chegou**.

## O limite de desconto

➡️ Com o **Desconto máximo do atendente** preenchido nas Opções, o atendente monta o pedido com qualquer desconto, mas acima do limite o botão **Confirmar e enviar** fica desativado e a janela avisa: *"O desconto passa do seu limite de 10%. Salve o rascunho e peça a um supervisor ou administrador para confirmar."*

➡️ O supervisor ou o administrador abre o rascunho no menu **PDV  ›  Pedidos** e confirma.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O atendente não vê os pedidos dos colegas na lista Pedidos.** É o esperado: o atendente vê só os pedidos que ele vendeu. Administrador e supervisor veem todos.
>
> **O atendente não encontra o botão Estornar.** Estornar um pagamento é do administrador e do supervisor. O atendente cancela um pedido só enquanto ele não tem pagamento.
>
> **O atendente não consegue ligar o Aceitar pedidos automaticamente, nem o Mandar direto para a produção os pedidos das mesas, no Painel de pedidos.** É o esperado: para o atendente as opções do aceite automático ficam desativadas, com o aviso *"Só a gestão (administrador ou supervisor) muda esta opção."* Ele continua aceitando e recusando cada pedido novo pelo card.
>
> **O supervisor pode mudar as Opções do PDV?** Não. As **Opções do PDV** ficam no menu **Configurações**, que só o administrador abre.
>
> **O entregador entrou e não vê os atendimentos.** É o perfil **Entregador**: ele vê só a tela **Minhas entregas**. Para atender clientes, a pessoa precisa de outro perfil.
>
> **O garçom entrou e só vê as mesas.** É o perfil **Garçom**: a plataforma inteira vira a tela **Mesas e comandas**, onde ele abre as mesas e lança os pedidos. Para atender clientes na conversa, a pessoa precisa de outro perfil.
>
> **O perfil Garçom não aparece na lista de perfis da Equipe.** O **Garçom** vem junto com a página **Mesas e Comandas**: se ela não está no seu menu **PDV**, o perfil também não aparece, porque os dois dependem do seu plano.
>
> **O garçom não encontra a taxa de serviço nem o desconto na conta da mesa.** É o esperado: a taxa de serviço, o desconto, o pagamento e o **Fechar mesa** ficam com o caixa. O garçom lança os pedidos, divide e imprime a conta.
