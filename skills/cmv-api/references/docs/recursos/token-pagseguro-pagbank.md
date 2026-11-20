# Token PagSeguro (PagBank)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/token-pagseguro-pagbank
- **Categoria:** Recursos
- **Menu:** Integrações › Token PagSeguro (PagBank)

---

🧩 O **Token do PagSeguro** é o token de segurança da conta PagBank da sua empresa. É com ele que a plataforma cria o link de pagamento de um pedido do PDV na sua conta PagBank e fica sabendo quando o cliente pagou. O dinheiro cai direto na sua conta, com as tarifas do seu contrato com o PagBank.

Na página do PagSeguro, o cliente escolhe como pagar: Pix, cartão ou boleto. O Token do PagSeguro pode ficar ligado junto com os do Asaas e do Mercado Pago, e aí você escolhe na hora de cobrar qual link gerar.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No PagBank, em **Venda Online**, abra **Integrações** e gere o **token de segurança**.
>
> ➡️ Na plataforma, acesse o menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**, cole o token em **Token do PagSeguro (PagBank) da empresa (links de pagamento do PDV)** e clique em **Salvar**.

## Como gerar o token no PagBank

➡️ Entre na sua conta PagBank.

➡️ No menu da esquerda, clique em **Venda Online** e depois em **Integrações**.

➡️ Em **Utilização de APIs**, clique em **Gerar Token**. O PagBank envia o token para o e-mail da conta.

⚠️ Gerar um token novo no PagBank invalida o anterior na hora. Se o token antigo estava salvo na plataforma, cole o novo no campo do PagSeguro, nas Opções.

## Como integrar o PagSeguro à nossa plataforma

Acesse o menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**.

🔘 **Token do PagSeguro (PagBank) da empresa (links de pagamento do PDV):** cole o token e clique em **Salvar**. A tela confirma que o PagSeguro foi conectado.

🔘 **Trocar o Token do PagSeguro:** cole o token novo no mesmo campo e clique em **Salvar**.

🔘 **Desconectar:** tira o PagSeguro dos pedidos. Sem o token, o pedido oferece só os outros meios de pagamento.

⚠️ Só o administrador da empresa vê e muda o campo do PagSeguro.

A tela não pede endereço de aviso para cadastrar no PagBank: a plataforma já tem um endereço próprio para receber o aviso de pagamento do PagSeguro.

## Testar antes no ambiente de testes

O token de uma conta de testes do PagBank (sandbox) também pode ser salvo no mesmo campo: a plataforma reconhece sozinha o ambiente de testes. Conectado assim, a tela avisa *"PagSeguro conectado no ambiente de testes (sandbox): os links não cobram de verdade."*

Depois do teste, troque pelo token da conta de produção para os links do PagSeguro cobrarem de verdade.

## Como fica no pedido

☑️ Com o token salvo, o pedido confirmado ganha o botão **Gerar link do PagSeguro** na parte de pagamentos. O link é enviado na conversa, e o cliente escolhe como pagar na página do PagSeguro.

☑️ Quando o cliente paga, o pedido fica **Pago** sozinho. Para a plataforma buscar o pagamento na hora, clique em **Conferir**, na linha do link: a tela responde *"Pagamento do PagSeguro recebido e baixado."* ou *"O PagSeguro ainda não registrou o pagamento deste link."*

☑️ Para mandar o mesmo link de novo ao cliente, use **Reenviar link do PagSeguro**.

## Boas práticas para gerenciar o Token do PagSeguro

➡️ **Não compartilhe o Token do PagSeguro:** com ele, qualquer sistema age na sua conta PagBank pela API, como se fosse você.

➡️ **Token vazado:** gere um token novo no PagBank, o que invalida o anterior, e cole o novo no campo **Token do PagSeguro (PagBank) da empresa**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente pagou pelo link do PagSeguro e o pedido continua Não pago. Por quê?** Clique em **Conferir**, na linha do link, para a plataforma buscar o pagamento. Se as Opções mostram *"O servidor não tem um endereço público configurado: o pagamento não baixa sozinho"*, a baixa sozinha não está disponível na sua plataforma, e o pedido baixa pelo **Conferir**.
>
> **Posso usar o PagSeguro, o Asaas e o Mercado Pago ao mesmo tempo nos pedidos?** Pode. Com os tokens salvos nas Opções, você escolhe na hora de cobrar qual link gerar.
>
> **O link do PagSeguro feito com o token de testes cobra o cliente?** Não. Com o token de uma conta de testes do PagBank, a tela avisa que os links não cobram de verdade. Para cobrar, salve o token da conta de produção.
>
> **Sem o Token do PagSeguro, o pedido deixa de receber pagamento?** Não. Sem o PagSeguro, o pedido oferece só os outros meios de pagamento, como os registrados à mão.
