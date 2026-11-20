# Pagamentos do Pedido

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pagamentos-do-pedido
- **Categoria:** Recursos
- **Menu:** PDV › Pagamentos do Pedido

---

🧩 Um pedido pode ser pago de uma vez ou em partes, em formas diferentes, e cada pagamento registrado entra no caixa de quem o registrou. Para o cliente que paga a distância, o pedido gera um pagamento online: um link de pagamento ou um Pix, conforme o meio conectado nas Opções do PDV.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Abra o pedido confirmado, pela conversa ou pelo menu **PDV  ›  Pedidos**.
>
> ➡️ Escolha a **Forma**, informe o **Valor** e clique em **Registrar pagamento**.
>
> ➡️ Repita para pagar o restante em outra forma.
>
> ➡️ Para o cliente que paga a distância, clique no botão do pagamento online, na parte de pagamentos do pedido.

## Vídeo Tutorial

[Vídeo Voomly — id 0oDcz3F4bPBqr1gm1zQAyF4zZWbSDDmBOTt9Fz89QMBiEUNyx, tipo v]  

## Registrar um pagamento

A parte de pagamentos do pedido mostra a situação — **Não pago**, **Pago em parte** ou **Pago** — e quanto falta, como *"Pago R$ 20,00 · falta R$ 15,90"*.

🔘 **Forma:** **Dinheiro**, **Pix**, **Cartão**, **Boleto** ou **Outro**. Aqui se registra o que já foi recebido: nenhuma dessas formas cobra o cliente.

🔘 **Valor:** quanto entra neste pagamento. O campo já vem com o que falta pagar.

🔘 **Valor recebido:** só no dinheiro. Com ele, a tela mostra o troco, e a linha do pagamento fica como *"Recebeu R$ 120,00 · troco R$ 20,00"*.

🔘 **Observação:** opcional.

**Registrar pagamento** avisa *"Pagamento registrado."*. O pagamento entra no caixa aberto de quem registrou. Com o pedido **Pago**, o formulário some da tela.

⚠️ Sem caixa aberto, o pagamento não é registrado: a tela avisa *"Abra o seu caixa para registrar pagamentos."*, e **Registrar pagamento** fica apagado. Abra o caixa no menu **PDV  ›  Caixa** ou pelo botão **Ir para o caixa**, junto do aviso.

## Estornar

Cada pagamento tem **Estornar**, que pede o **Motivo do estorno** e confirma em **Confirmar estorno**. A linha passa a mostrar o motivo, e o estorno é lançado no caixa. Estornar é do administrador e do supervisor.

Com o aviso **Pagamento estornado** ligado nas Opções do PDV, o cliente recebe na conversa a mensagem do estorno, como *"Estornamos o pagamento do pedido #75. O valor volta pela mesma forma de pagamento."*, também no pagamento registrado à mão.

⚠️ No pagamento online, o estorno não é lançado no caixa. No link do Asaas, **Estornar** também devolve o dinheiro ao cliente pela sua conta Asaas. Se a sua conta Asaas pede autorização para ações críticas, a devolução só é feita depois que você digita o token no painel do Asaas. Enquanto isso, o pagamento mostra *Estorno aguardando autorização no Asaas*.

## O pagamento online

O **pagamento online** é gerado no próprio pedido e enviado ao cliente na conversa. Cada meio conectado nas Opções do PDV põe o seu botão no pedido confirmado:

🔘 **Gerar link do Asaas**, **Gerar link do Mercado Pago** e **Gerar link do PagSeguro:** enviam o link de pagamento, e o cliente escolhe como pagar na página de cada um.

🔘 **Gerar Pix (PaggPix):** envia o Pix, com QR Code e Pix copia e cola.

Com o Asaas, o Mercado Pago e o PagSeguro conectados ao mesmo tempo, você escolhe na hora de cobrar qual link gerar.

⚠️ O pagamento online não entra no esperado do caixa: o dinheiro cai na conta do provedor. O resumo do caixa mostra o link à parte, em **Recebido online (fora do caixa)**.

⚠️ O pagamento online cobra em reais. Com a **Moeda** da empresa em outra moeda, no menu **Configurações  ›  Opções  ›  Geral**, seção **Empresa e região**, a parte de pagamentos do pedido avisa *"O pagamento online cobra em reais e fica indisponível na moeda da empresa."*

### O link do Asaas

Com o token do Asaas nas Opções do PDV, o pedido confirmado ganha o botão **Gerar link do Asaas**:

➡️ O cliente recebe na conversa *"Pague o pedido #8 (R$ 35,90) por este link:"* e o link de pagamento, onde escolhe como pagar.

➡️ O pagamento aparece como **Link do Asaas**, com o valor, quem gerou, a data e *Aguardando o cliente*, mais **Copiar o link** e **Conferir no Asaas**. O botão do pedido vira **Reenviar link do Asaas**.

➡️ **Conferir no Asaas** busca o pagamento: pago, o pedido fica **Pago** e a linha, **Recebido**.

➡️ Com o **Aviso do Asaas para o PDV** cadastrado nos webhooks da conta Asaas, o pedido pago pelo link dá baixa sozinho, poucos segundos depois do pagamento, sem precisar do **Conferir no Asaas**.

➡️ Depois do pagamento, a plataforma desativa o link no Asaas: o cliente não consegue pagar o mesmo link de novo.

⚠️ O link do Asaas não aceita pedido abaixo de **R$ 10,00**, o mínimo do Asaas para Boleto e Pix.

### Mercado Pago, PagSeguro e PaggPix

➡️ Quando o cliente paga, o pedido fica **Pago** sozinho. Para a plataforma buscar o pagamento na hora, clique em **Conferir**, na linha do pagamento.

➡️ **Reenviar link do Mercado Pago** e **Reenviar link do PagSeguro** mandam o mesmo link de novo ao cliente.

➡️ **Reenviar Pix (PaggPix)** manda o Pix de novo na conversa. Se o Pix venceu, um novo é gerado na hora; se o cliente já pagou, o pedido é baixado.

➡️ **Copiar o Pix copia e cola**, na linha do Pix, copia o código para você mandar de novo.

## O pagamento na entrega

O entregador registra o pagamento recebido na porta do cliente, pela tela **Minhas entregas**. O pagamento entra no caixa do entregador.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente pode pagar uma parte em dinheiro e outra no Pix?** Sim. Registre um pagamento para cada forma; o pedido fica **Pago em parte** até a soma chegar ao total.
>
> **Cancelei um pedido pago. O que acontece com o pagamento?** O pagamento passa a **Estornado**, com o motivo *Pedido cancelado*, e o estorno é lançado no caixa.
>
> **O cliente pagou pelo link do Asaas e o pedido continua Não pago.** Clique em **Conferir no Asaas**, no pagamento do link. Sem o aviso do Asaas cadastrado, a baixa depende desse botão.
>
> **Estornei um pagamento do link do Asaas e o dinheiro não voltou para o cliente. Por quê?** A sua conta Asaas pode pedir autorização para ações críticas: o estorno fica esperando até você digitar o token no painel do Asaas, que dá 24 horas para isso. Enquanto espera, o pagamento mostra *Estorno aguardando autorização no Asaas*.
>
> **O cliente pagou pelo Mercado Pago, pelo PagSeguro ou pela PaggPix e o pedido continua Não pago.** Clique em **Conferir**, na linha do pagamento, para a plataforma buscar o pagamento. Se as Opções mostram que o servidor não tem um endereço público configurado, a baixa sozinha não está disponível na sua plataforma, e o pedido baixa pelo **Conferir**.
>
> **A forma Pix do pedido gera o QR Code para o cliente?** Não. A forma **Pix** registra um Pix já recebido. Quem gera o Pix para o cliente é o pagamento online, com a PaggPix conectada nas Opções do PDV.
>
> **Sem nenhum pagamento online conectado, o pedido deixa de receber pagamento?** Não. O pedido continua com as formas registradas à mão.
>
> **O pedido avisa que o pagamento online fica indisponível na moeda da empresa. Por quê?** O pagamento online cobra em reais e só funciona com a **Moeda** da empresa em **Real brasileiro (BRL)**, no menu **Configurações  ›  Opções  ›  Geral**, seção **Empresa e região**.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Pagamento não registra:** **Registrar pagamento** fica apagado e a tela avisa *"Abra o seu caixa para registrar pagamentos."*, porque o caixa de quem está registrando está fechado. **Solução:** clique em **Ir para o caixa**, abra o caixa no menu **PDV  ›  Caixa** e registre de novo.
>
> **Link do Asaas não gerado:** ao clicar em **Gerar link do Asaas**, a tela avisa que não foi possível falar com o servidor. Isso acontece quando o Asaas recusa o link, como num pedido abaixo de R$ 10,00 ou com um token de outro ambiente. **Solução:** confira o total do pedido e o token do Asaas nas Opções do PDV; para valores menores, registre o pagamento em outra forma.
