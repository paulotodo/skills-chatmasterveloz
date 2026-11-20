# Pedido na Conversa

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pedido-na-conversa
- **Categoria:** Recursos
- **Menu:** PDV › Pedido na Conversa

---

🧩 O cliente pediu pela conversa? O pedido é montado ali mesmo, sem sair do atendimento: os produtos, o desconto, a entrega e o total. Ao confirmar, o cliente recebe a nota do pedido na conversa e o estoque baixa na hora.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No atendimento, clique no botão **Pedido**, no topo da conversa.
>
> ➡️ Busque e adicione os produtos, ajuste quantidade, desconto e entrega.
>
> ➡️ Clique em **Confirmar e enviar**, ou em **Salvar rascunho** para terminar depois.

## Vídeo Tutorial

[Vídeo Voomly — id TJQWlQDVe8XU-xKrABsvz8qeRVKRB37A17dZC58ZLVMeB-EdW, tipo v]  

## Como montar o pedido

O botão **Pedido** sempre começa um pedido novo, na janela **Novo pedido**:

🔘 **Buscar produto ou serviço:** digite o nome e escolha o produto. O resultado mostra o estoque, como *"Em estoque: 12"*. Cada item da tabela tem preço, quantidade, total e **Tirar do pedido**.

🔘 **Produto com opções:** o produto com variações aparece na busca com *"a partir de"* e o preço. Ao escolher, abre a janela das opções: a variação em **Opção** e os adicionais de cada grupo, marcados dentro da regra, como *"Escolha de 1 a 2"*. O **Preço de cada unidade** soma a variação e os adicionais, e **Adicionar** põe o item no pedido. Na tabela, o item leva a variação entre parênteses e os adicionais abaixo, como *Pizza (Pequena)* e *+ Catupiry*, com o estoque da variação.

🔘 **Desconto em:** **R$** ou **%**, e o valor do **Desconto**.

🔘 **Acréscimo:** um valor somado ao total.

🔘 **Retirada no local** ou **Entrega:** na entrega aparecem **Taxa de entrega**, **Endereço de entrega** e **Bairro**. O **Bairro** sugere os bairros da tabela de taxas, como *"Centro · R$ 7,50"*, e preenche a taxa, que ainda pode ser ajustada. O **Endereço de entrega** é obrigatório na entrega: sem ele, **Salvar rascunho** e **Confirmar e enviar** ficam desativados.

🔘 **CEP:** na entrega, quando a empresa tem faixas cadastradas no **Frete por faixa de CEP**, aparece o **CEP**, entre a **Taxa de entrega** e o **Endereço de entrega**. O CEP que cai numa faixa preenche a taxa e mostra a região, o frete e o prazo da faixa, como *"Centro · R$ 7,50 · até 40 min"*.

🔘 **Endereço salvo do cliente:** na entrega, quando o cliente da conversa tem endereços guardados, a lista traz cada um como *apelido — endereço · bairro* e a opção *Outro endereço (digitado abaixo)*. O endereço principal já vem escolhido. Escolher um endereço da lista preenche o **Endereço de entrega**, o **Bairro** e a **Taxa de entrega**, pela tabela de bairros.

🔘 **Salvar este endereço no cadastro do cliente:** aparece já marcado quando o endereço digitado não está na lista do cliente. Marcado, o endereço entra nos endereços do cliente, sem apelido, já no **Salvar rascunho**; desmarcado, fica só neste pedido.

🔘 **Agendar para:** opcional, a data e o horário combinados com o cliente. O pedido agendado leva *"Agendado para"* na nota, aparece na lista de pedidos com a data combinada e entra em **Agendados** no **Painel de pedidos**.

🔘 **Observação:** o recado do pedido, que vai na nota.

O **Subtotal**, a **Taxa de entrega** e o **Total** aparecem no fim da janela.

### Os endereços do cliente

Na entrega, o botão **Endereços do cliente** abre a janela de mesmo nome, com o nome do contato, onde ficam os endereços de entrega guardados dele. Sem nenhum, a janela avisa *"O cliente ainda não tem endereço salvo."*

🔘 **Novo endereço:** abre o formulário com **Apelido**, **Endereço (rua, número e complemento)**, **Bairro**, **CEP** e **Usar como endereço principal**. **Salvar** só fica ativo com o endereço preenchido e avisa *"Endereço salvo."*

🔘 **Tornar principal:** faz do endereço o principal, que sobe para o topo da lista e já vem escolhido na entrega. O primeiro endereço do cliente nasce principal.

🔘 **Editar endereço** e **Apagar endereço:** o apagar pede a confirmação *"Apagar este endereço do cliente?"* e avisa *"Endereço apagado."* Apagado o principal, o endereço usado por último passa a ser o principal.

⚠️ O bairro fora da tabela de taxas de entrega não é salvo, com o aviso *"Ainda não entregamos neste bairro."*, e o mesmo endereço não entra duas vezes: *"Este endereço já está na lista do cliente."*

## Confirmar e enviar

**Confirmar e enviar** confirma o pedido e avisa *"Pedido confirmado e nota enviada ao cliente."* O cliente recebe duas mensagens na conversa: o texto do pedido, com a data, os itens, o subtotal, o desconto, a taxa, o total e *Entregar em* ou *Retirada no local*, e o PDF do pedido. O estoque dos produtos baixa na hora.

No item com variação, o texto do pedido traz a variação entre parênteses e, na linha de baixo, os adicionais escolhidos, como *"1 x Pizza (Pequena) · R$ 35,00"* e *"+ Catupiry"*.

**Salvar rascunho** guarda o pedido sem enviar nada, com o aviso *"Rascunho salvo."*. O rascunho é reaberto pelo menu **PDV  ›  Pedidos**, no botão **Abrir pedido**.

⚠️ Quando um item passa do estoque, a janela mostra *"Só 12 em estoque"* e o **Confirmar e enviar** fica desativado até a quantidade ser ajustada, a não ser que a empresa venda sem estoque.

⚠️ Com o **Desconto máximo do atendente** preenchido nas Opções, o atendente que passa do limite vê *"O desconto passa do seu limite de 10%. Salve o rascunho e peça a um supervisor ou administrador para confirmar."*

## Depois de confirmado

🔘 **Registrar pagamento:** os pagamentos do pedido ficam na mesma janela, abaixo dos itens. Sem o seu caixa aberto, a janela mostra **Ir para o caixa**.

🔘 **Imprimir:** imprime o pedido.

🔘 **Via da cozinha:** abre o PDF da via da cozinha, só com os itens, sem preço e com letra grande.

🔘 **Reenviar nota:** manda a nota do pedido de novo ao cliente.

🔘 **Saiu para entrega:** só no pedido com entrega. Escolhe quem leva o pedido e o despacha, como no **Painel de pedidos**.

🔘 **Marcar como entregue:** fecha o pedido como entregue.

🔘 **Rastreio da entrega:** com o pedido na rua, a janela mostra o link do rastreio, **Copiar link** e **Enviar ao cliente**, que manda na conversa *"Acompanhe a entrega do pedido #24:"* e o link, com o aviso *"Link do rastreio enviado na conversa"*.

🔘 **Ver onde foi entregue** e **Ver a foto da entrega:** no pedido entregue por um entregador, junto com o nome de quem entregou.

🔘 **Cancelar pedido:** pede o **Motivo do cancelamento (opcional)** e cancela; o estoque volta, e o pagamento registrado é estornado.

## Os pedidos no painel do contato

O painel do contato, no atendimento, mostra **Pedidos**: o resumo *"Pedidos confirmados: 2 · Total gasto: R$ 238,62"* e a lista dos pedidos do cliente, com número, valor, data e situação. A lista se atualiza sozinha, sem recarregar a tela, quando o pedido é criado, confirmado, muda de etapa ou é cancelado.

🔘 **Repetir pedido:** cria um pedido novo com os mesmos itens, a mesma entrega e o mesmo bairro, com o preço de hoje, e avisa *"Pedido #11 repetido com os preços de hoje. Confira e confirme."* O pedido novo nasce em rascunho, e nada é enviado ao cliente até a confirmação.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A nota do pedido é nota fiscal?** Não. A nota do PDV é o resumo do pedido, em texto e em PDF, e não substitui o documento fiscal.
>
> **Cliquei em Pedido para continuar um pedido e veio um pedido vazio.** O botão **Pedido** sempre começa um pedido novo. Para continuar um rascunho, abra o pedido no menu **PDV  ›  Pedidos**.
>
> **O cliente recebe alguma mensagem quando eu salvo o rascunho?** Não. Nada é enviado até o **Confirmar e enviar**.
>
> **O campo CEP não aparece no pedido com entrega. Por quê?** O **CEP** só aparece quando a empresa tem faixas cadastradas no **Frete por faixa de CEP**, no menu **Configurações  ›  Opções**. Sem faixas, a taxa vem do **Bairro**.
>
> **Como guardo o endereço do cliente para o próximo pedido na conversa?** Deixe marcado **Salvar este endereço no cadastro do cliente** ao digitar um endereço novo, ou cadastre pelo botão **Endereços do cliente**, na entrega do pedido. Nos próximos pedidos, ele aparece na lista **Endereço salvo do cliente**.
>
> **Repeti um pedido antigo e faltou um item.** O item foi tirado do cadastro de produtos. A janela avisa *"Ficaram de fora, porque saíram do cadastro"*, com o nome dos itens.
