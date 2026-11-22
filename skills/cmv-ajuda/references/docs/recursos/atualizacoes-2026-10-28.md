# Atualizações 28/10/2026

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-10-28
- **Categoria:** Recursos
- **Menu:** Atualizações › Outubro 2026 › 28/10/2026

---

🧩 Atualizações de 28 de outubro de 2026.

#### Novidades

⚡️ **Painel de pedidos:** no PDV, a cozinha acompanha cada pedido em **Novo**, **Em preparo**, **Pronto**, **Saiu** e **Entregue**, com **Modo TV**, aviso sonoro e o card mudando de cor quando o pedido demora.

⚡️ **Venda no balcão:** no PDV, a venda direto no caixa, sem atendimento, com leitor de código de barras, troco, pagamento dividido e a escolha entre entregar na hora ou mandar para a cozinha. O cliente é opcional.

⚡️ **Entregadores:** o novo perfil **Entregador** vê só as próprias entregas; a loja escolhe quem leva cada pedido e acompanha todos no **Mapa dos entregadores**.

⚡️ **Rastreio da entrega:** o cliente acompanha a entrega no mapa, ao vivo, e vê quanto falta. O mapa pode ser o OpenStreetMap, grátis, ou o Google Maps com a chave da empresa.

⚡️ **Avisos do pedido ao cliente:** pedido confirmado, pagamento recebido, em preparo, pronto para retirada, saiu para entrega e entregue, cada um com texto próprio e liga e desliga.

⚡️ **Venda pelo fluxo:** no FlowBuilder Nativo, o bloco **PDV (pedido no fluxo)** deixa o cliente escolher os produtos numa lista numerada e confirmar o pedido sozinho; o pedido chega confirmado no atendimento.

⚡️ **Pedidos no painel do contato:** os últimos pedidos do cliente, quantas compras ele fez e quanto já gastou, com o botão **Repetir pedido**, que repete um pedido antigo com o preço de hoje.

⚡️ **Limite de desconto do atendente:** acima do limite, o pedido fica em rascunho até um supervisor ou administrador confirmar.

⚡️ **Taxa de entrega por bairro e pedido agendado:** escolher o bairro preenche a taxa, e o pedido pode ter data e horário combinados com o cliente.

⚡️ **Aplicativo do entregador:** o entregador recebe as entregas direto no celular.

#### Melhorias

☑️ **Chamada de voz no Chat Interno:** a chamada da equipe abre como chamada de voz, numa janela compacta, e o vídeo entra só se alguém ligar a câmera.

☑️ **Estoque baixo:** aviso no sino e no celular quando um produto chega ao estoque mínimo.

#### Correções

◽ **Opções do PDV:** o administrador da empresa passa a ver e preencher, no menu **Configurações  ›  Opções**, o **Token do Asaas da empresa**, o **Aviso do Asaas para o PDV (webhook)** e o **Webhook do PDV**.

◽ **Conexões:** compatibilidade com a versão mais nova do WhatsApp.

## Painel de pedidos

O **Painel de pedidos** fica no menu **PDV  ›  Painel de pedidos**, para administradores, supervisores e atendentes. É a tela da cozinha: cada pedido anda pelas colunas **Novo**, **Em preparo**, **Pronto**, **Saiu** e **Entregue**.

🔘 **Card do pedido:** mostra o número, os minutos de espera, o contato, **Retirada no local** quando for o caso, os itens e o botão da próxima etapa, como **Começar o preparo**.

🔘 **Modo TV:** deixa o painel numa tela da cozinha, com o som ligado em **Ativar o som** para avisar quando chega pedido.

🔘 **Cor do card:** muda pelo tempo de espera, contado desde a confirmação: amarelo na atenção e vermelho no atraso. Os minutos de cada cor ficam no menu **Configurações  ›  Opções**, em **Painel de pedidos**, junto com a antecedência com que o pedido agendado entra em **Novo**.

➡️ No topo do painel ficam o **Mapa dos entregadores** e o **Modo TV**.

## Venda no balcão

O **Balcão** fica no menu **PDV  ›  Balcão** e vende direto no caixa, sem abrir atendimento. O caixa precisa estar aberto: sem ele, a tela pede para abrir o caixa antes de vender.

🔘 **Produto ou código:** digite o nome ou passe o leitor de código de barras e tecle Enter.

🔘 **Desconto e acréscimo:** em R$ ou em %.

🔘 **Cliente (opcional):** sem cliente, a venda é registrada como Consumidor. Com ele, a venda entra no histórico do contato.

🔘 **Pagamento:** aceita mais de uma forma, com troco; os pagamentos precisam somar o total da venda.

➡️ No fim, escolha **Entregar agora** ou **Mandar para a cozinha**, e imprima o comprovante se quiser.

## Entregadores

O cadastro de usuário, no menu **Equipe**, ganhou o perfil **Entregador**. Quem entra com esse perfil vê só a tela **Minhas entregas**, com as entregas dele, e tem caixa próprio para receber na porta, com comprovação por localização e foto opcional.

➡️ Ao despachar um pedido, a loja escolhe quem leva em **Quem leva o pedido?**, ou marca **Sem entregador (a loja leva)**.

➡️ O **Mapa dos entregadores**, no **Painel de pedidos**, mostra os entregadores que estão na rua.

➡️ Se a entrega não der certo, o entregador marca **Não consegui entregar** com o motivo, e o pedido volta para a loja decidir.

## Rastreio da entrega

Quando o pedido sai para entrega, o cliente recebe na conversa o link do rastreio. A página mostra quem está levando o pedido, a posição no mapa, ao vivo, e em quantos minutos chega.

🔘 **Mapa do rastreio da entrega:** no menu **Configurações  ›  Opções**, a empresa escolhe entre o OpenStreetMap, que é grátis e não pede chave, e o Google Maps, com a chave da própria empresa. É o mesmo mapa que a loja vê no **Mapa dos entregadores**.

⚠️ Com o Google Maps, a chave aparece para o cliente na página do rastreio: restrinja a chave ao endereço do seu painel, na conta do Google.

## Avisos do pedido ao cliente

No menu **Configurações  ›  Opções**, a seção **Avisos do pedido ao cliente** reúne seis mensagens que são enviadas sozinhas na conversa do pedido, cada uma quando é ligada: **Pedido confirmado**, **Pagamento recebido**, **Em preparo**, **Pronto para retirada** (só no pedido de retirada), **Saiu para entrega** e **Pedido entregue**.

🔘 **Texto de cada aviso:** editável, com **Voltar ao texto padrão** para recuperar o original.

➡️ Os avisos vêm desligados. Ligue só os que fizer sentido para a sua operação e clique em **Salvar avisos**.

➡️ Só o pedido com entrega passa por **Saiu para entrega**; o de retirada no local vai direto a entregue.

## Venda pelo fluxo

O FlowBuilder Nativo ganhou o bloco **PDV (pedido no fluxo)**. O cliente escolhe um produto pelo número, diz a quantidade, adiciona outro ou finaliza e, no fim, vê o resumo com o preço do cadastro e confirma. O 0 desiste em qualquer passo.

🔘 **Texto antes da lista:** a frase que vem antes dos produtos. Em branco, o bloco usa "Escolha um produto pelo número:".

🔘 **Buscar produto do cadastro:** monta a lista com os produtos que o cliente pode escolher.

🔘 **Sem resposta: seguir pela saída depois de (minutos):** vazio ou 0 desliga.

➡️ O bloco tem duas saídas: **Pedido confirmado** e **Desistiu**. O pedido nasce confirmado no atendimento, e o atendente é avisado.

## Pedidos no painel do contato

O painel do contato, dentro do atendimento, ganhou a seção **Pedidos**, com o total de pedidos confirmados, o total gasto e a lista dos últimos pedidos, cada um com número, valor, data e hora e situação.

➡️ **Repetir pedido** monta o mesmo pedido com os preços de hoje, para você conferir e confirmar. Produto que saiu do cadastro fica de fora, e a tela avisa.

## Limite de desconto do atendente

No menu **Configurações  ›  Opções**, a opção **Desconto máximo do atendente (%)** define até quanto o atendente desconta sozinho. Em branco, não há limite.

➡️ Acima do limite, o atendente salva o pedido como rascunho, e um supervisor ou administrador confirma.

## Taxa de entrega por bairro e pedido agendado

Na janela **Novo pedido**, com **Entrega**, o campo **Bairro** preenche a taxa de entrega pela tabela da empresa, e o atendente ainda pode ajustar. A tabela fica no menu **Configurações  ›  Opções**, em **Taxa de entrega por bairro**.

🔘 **Agendar para:** opcional, a data e o horário combinados com o cliente, para entrega ou retirada.

## Chamada de voz no Chat Interno

A chamada da equipe no **Chat Interno** abre como chamada de voz, numa janela compacta. O vídeo entra só se alguém clicar em **Ligar a câmera (vira videochamada)**; quem está na chamada vê **Há vídeo nesta chamada** e escolhe entre **Ver vídeo** e **Voltar para a chamada de voz**.

## Opções do PDV

No menu **Configurações  ›  Opções**, o administrador da empresa passa a ver e preencher as opções do PDV que antes não apareciam para ele: o **Token do Asaas da empresa (links de pagamento do PDV)**, o **Aviso do Asaas para o PDV (webhook)** e o **Webhook do PDV**.

🔘 **Token do Asaas da empresa:** a chave de API da conta Asaas da empresa. Com ela, o pedido gera o link de pagamento, e o dinheiro cai na conta da empresa.

🔘 **Aviso do Asaas para o PDV (webhook):** o endereço que você cadastra nos webhooks do Asaas, para o pedido ser dado como pago sozinho.

🔘 **Webhook do PDV:** o endereço do seu sistema que recebe os eventos de pedidos, pagamentos, caixa e estoque. Em branco, nada é enviado.

➡️ Só o administrador da empresa muda as opções do PDV.

#### O que você precisa fazer

➡️ No menu **Configurações  ›  Opções**, ligue os avisos ao cliente em **Avisos do pedido ao cliente** e ajuste **Taxa de entrega por bairro**, **Painel de pedidos** e **Mapa do rastreio da entrega**.

➡️ No menu **Equipe**, crie um usuário com o perfil **Entregador** para cada entregador.
