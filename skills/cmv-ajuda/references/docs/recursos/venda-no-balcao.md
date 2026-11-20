# Venda no Balcão

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/venda-no-balcao
- **Categoria:** Recursos
- **Menu:** PDV › Venda no Balcão

---

🧩 O cliente está na loja? A venda é feita no **Balcão**, direto no caixa: montada, recebida na hora e entregue ao cliente ou enviada para o painel de pedidos, sem abrir atendimento.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **PDV  ›  Balcão**. Se o seu caixa estiver fechado, clique em **Abrir o caixa**.
>
> ➡️ Busque os produtos, ou toque na categoria e no produto, e lance os pagamentos até o **Falta** chegar a zero.
>
> ➡️ Clique em **Entregar agora** ou em **Enviar para o painel de pedidos**.

## Vídeo Tutorial

[Vídeo Voomly — id CdfIQ5iBs8uP3w0d0FVjYQjeEYbh5HeE2Xt1IEMxTO62Fjl8c, tipo v]  

## Como montar a venda

🔘 **Produto ou código:** digite o nome ou passe o leitor de código de barras e tecle Enter. O código lido é o **SKU** do cadastro do produto. Cada item mostra o estoque, como *"Em estoque: 7"*, e tem **Tirar do pedido**.

🔘 **Categorias:** os botões de categoria ficam logo abaixo da busca. Tocar numa categoria mostra os produtos dela com o preço, mais **Todos de** e as subcategorias para filtrar, e tocar no produto põe o item na venda.

🔘 **Produto com opções:** o produto com variações ou adicionais abre uma janela com o nome dele. Em **Opção**, escolha a variação, cada uma com o preço, como *"Grande · R$ 45,00"*. Em cada grupo de adicionais, marque as opções dentro da regra do grupo, como *"Escolha de 1 a 2"*, cada uma com o preço, como *"Catupiry · + R$ 5,00"*. O **Preço de cada unidade** soma a variação e os adicionais, e **Adicionar** põe o item na venda.

🔘 **Desconto em** **R$** ou **%**, e **Acréscimo**.

🔘 **Cliente (opcional):** sem cliente, a venda fica como Consumidor. Com ele, entra no histórico do contato.

🔘 **Observação:** o recado da venda.

O **Total** e o **Subtotal** aparecem ao lado, com a parte de **Pagamento**.

Na venda, o produto com opções aparece com a variação entre parênteses e os adicionais logo abaixo, como *Pizza (Grande)* e *+ Catupiry, Cheddar*, e o estoque mostrado é o da variação. Mudar a **Quantidade** da linha multiplica o preço da unidade, com os adicionais. O mesmo produto com opções diferentes entra numa linha nova; com as mesmas opções, soma na linha que já existe.

No produto com **ficha de insumos**, a venda baixa do estoque os insumos da ficha, e não o próprio produto. O estoque mostrado no Balcão é quanto dá para fazer com os insumos que estão em estoque, como *"Em estoque: 5"*, e a variação com ficha própria mostra a conta dela, como *"Em estoque: 2"* no tamanho que leva mais insumo.

Quando os insumos não dão para nenhuma unidade, o produto com **ficha de insumos**, ou só a variação que leva mais insumo, fica indisponível sozinho: a linha mostra *"Só 0 em estoque"* e, se a empresa não vende sem estoque, **Entregar agora** fica desativado. Com a entrada do insumo no estoque, o produto volta a ficar disponível sozinho.

O mesmo vale para o adicional com ficha de insumos: quando o insumo dele acaba, a janela de opções mostra o adicional como *"+ Bacon · Indisponível · + R$ 5,00"*, e ele não pode ser marcado.

## Os pagamentos

🔘 **Forma:** **Dinheiro**, **Pix**, **Cartão**, **Boleto** ou **Outro**.

🔘 **Valor** e **Recebido:** no dinheiro, o **Recebido** calcula o troco, e o pagamento lançado fica como *"Dinheiro · recebido R$ 40,00, troco R$ 4,10"*.

🔘 **Lançar:** inclui o pagamento. A venda pode ter mais de um, em formas diferentes; **Tirar o pagamento** desfaz um lançamento.

**Pago**, **Falta** e **Troco** mostram a conta da venda. Os pagamentos têm de somar o total para fechar.

## Fechar a venda

🔘 **Entregar agora:** fecha a venda como entregue. A janela mostra *"Venda #12 concluída"*, o troco e *"Venda entregue ao cliente."*

🔘 **Enviar para o painel de pedidos:** a venda vai para o **Painel de pedidos**, em **Novo**, marcada como *Balcão*, e a janela avisa *"O pedido foi para o painel de pedidos. O cliente espera ficar pronto."*

O texto do botão **Enviar para o painel de pedidos** pode ser outro, como *Mandar para a cozinha*: a empresa escolhe no menu **Configurações  ›  Opções**, no campo **Botão da venda de balcão** de **Nomes das etapas**. Em branco, fica o texto padrão do **Segmento do negócio**, escolhido na mesma página: *Enviar para o painel de pedidos* em **Alimentação**, *Mandar para a separação* em **Varejo** e **Farmácia**, e *Mandar para o painel* em **Outro negócio**.

Depois de fechar, **Imprimir comprovante** imprime a venda com as formas de pagamento e o troco, e **Nova venda** limpa a tela para o próximo cliente.

⚠️ A venda de balcão precisa do caixa aberto de quem vende: os pagamentos entram nele.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A venda de balcão aparece na lista Pedidos e no relatório?** Sim. A venda de balcão ganha um número de pedido, aparece no menu **PDV  ›  Pedidos** com o cliente *Consumidor* quando não há contato, e entra no **Relatório do PDV**. A página **Pedidos** também tem o botão **Venda de balcão**, que abre o Balcão.
>
> **Preciso escolher o cliente para vender no balcão?** Não. Sem cliente, a venda fica como Consumidor. Escolher o contato guarda a compra no histórico dele.
>
> **O botão Mandar para a cozinha sumiu do Balcão. Onde está?** Agora ele se chama **Enviar para o painel de pedidos** e faz o mesmo: leva a venda para o **Painel de pedidos**. Para voltar ao nome antigo, ou dar outro, preencha o campo **Botão da venda de balcão** no menu **Configurações  ›  Opções**.
>
> **Por que o Adicionar da janela de opções do produto não libera no Balcão?** Falta escolher a **Opção**, e a janela avisa *"Escolha uma opção."*, ou o número de adicionais marcados está fora da regra do grupo, como *"Escolha de 1 a 2"*.
>
> **Uma categoria sumiu dos botões do Balcão. O que aconteceu?** A categoria foi desativada. No menu **PDV  ›  Produtos  ›  Categorias**, ligue **Ativa** para ela voltar ao Balcão.
>
> **O produto com ficha de insumos mostra estoque no Balcão, mas o cadastro dele não controla estoque. Está certo?** Sim. No produto com **ficha de insumos**, o estoque do Balcão é a conta do que dá para fazer com os insumos, e a venda baixa os insumos. Quem tem estoque próprio é cada insumo, cadastrado no menu **PDV  ›  Produtos**.
>
> **O leitor de código de barras não achou o produto.** O leitor procura o **SKU** do produto. Confira se o código do produto está preenchido no cadastro, no menu **PDV  ›  Produtos**.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Venda não fecha:** a tela avisa que os pagamentos têm de somar o total da venda. **Solução:** lance o que falta, ou tire o pagamento que passou do total.
