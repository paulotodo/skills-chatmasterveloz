# Access Token Mercado Pago

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/access-token-mercado-pago
- **Categoria:** Recursos
- **Menu:** Integrações › Access Token Mercado Pago

---

🧩 O **Access Token do Mercado Pago** é a credencial de produção da conta Mercado Pago da sua empresa. É com ele que a plataforma cria o link de pagamento de um pedido do PDV na sua conta Mercado Pago e fica sabendo quando o cliente pagou. O dinheiro cai direto na sua conta, com as tarifas do seu contrato com o Mercado Pago.

Na página do Mercado Pago, o cliente escolhe como pagar: Pix, cartão ou boleto. O Access Token do Mercado Pago pode ficar ligado junto com o token do Asaas, e aí você escolhe na hora de cobrar qual link gerar.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No Mercado Pago, em **Suas integrações**, copie o **Access Token** das **Credenciais de produção** da sua aplicação.
>
> ➡️ Na plataforma, acesse o menu **Configurações  ›  Opções**, cole o token em **Access Token do Mercado Pago da empresa (links de pagamento do PDV)** e clique em **Salvar**.

## Como pegar o Access Token no Mercado Pago

➡️ Entre na sua conta em [https://www.mercadopago.com.br/developers](https://www.mercadopago.com.br/developers) e abra **Suas integrações**.

➡️ Abra a aplicação da sua empresa. Se ainda não tiver uma, crie a aplicação por ali.

➡️ No menu lateral da aplicação, clique em **Credenciais** e escolha **Produção**. Na primeira vez, clique em **Ativar ambiente de produção**, informe o setor e o site da empresa, aceite os termos e clique em **Ativar**.

➡️ Copie o **Access Token**.

⚠️ O campo da plataforma pede o **Access Token de produção**. A **Public Key**, que aparece na mesma tela, não serve.

## Como integrar o Mercado Pago à nossa plataforma

Acesse o menu **Configurações  ›  Opções**

🔘 **Access Token do Mercado Pago da empresa (links de pagamento do PDV):** cole o Access Token e clique em **Salvar**. A tela confirma que o Mercado Pago foi conectado.

🔘 **Trocar o Access Token do Mercado Pago:** cole o token novo no mesmo campo e clique em **Salvar**.

🔘 **Desconectar:** tira o Mercado Pago dos pedidos. Sem o Access Token, o pedido oferece só os outros meios de pagamento.

⚠️ Só o administrador da empresa vê e muda o campo do Mercado Pago.

Não há endereço de aviso para cadastrar no Mercado Pago: a baixa do pedido não depende de nenhum passo seu na conta do Mercado Pago.

## Conectar a conta do Mercado Pago

Quando a plataforma oferece a conexão da conta, as Opções trazem também o botão **Conectar conta do Mercado Pago**. Com ele, a empresa autoriza a plataforma na própria conta do Mercado Pago. Conectada, a tela mostra *"Conta do Mercado Pago conectada: …"*, com o nome da conta, e o botão **Desconectar conta**.

Quando a plataforma cobra uma taxa nos pagamentos do PDV, as Opções mostram *"Taxa da plataforma em cada cobrança: …"*, com o percentual ou o valor fixo combinado com a sua empresa. Sem a conta conectada, as Opções avisam *"Conecte a conta do Mercado Pago para continuar gerando links de pagamento."*

## Como fica no pedido

☑️ Com o Access Token salvo, o pedido confirmado ganha o botão **Gerar link do Mercado Pago** na parte de pagamentos. O cliente recebe o link na conversa e escolhe como pagar na página do Mercado Pago.

☑️ Quando o cliente paga, o pedido fica **Pago** sozinho. Para a plataforma buscar o pagamento na hora, clique em **Conferir**, na linha do link: a tela responde *"Pagamento do Mercado Pago recebido e baixado."* ou *"O Mercado Pago ainda não registrou o pagamento deste link."*

☑️ Para mandar o mesmo link de novo ao cliente, use **Reenviar link do Mercado Pago**.

## Boas práticas para gerenciar o Access Token

➡️ **Não compartilhe o Access Token:** com ele, qualquer sistema age na sua conta do Mercado Pago pela API, como se fosse você.

➡️ **Access Token vazado:** renove as credenciais da aplicação no Mercado Pago e cole o token novo no campo **Access Token do Mercado Pago da empresa**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Ao salvar o Access Token do Mercado Pago, a tela diz que o token não foi aceito. O que fazer?** A tela mostra *"O Mercado Pago não aceitou este token. Copie de novo o Access Token de produção."* Volte em **Credenciais de produção**, copie o **Access Token** inteiro, sem espaço no começo ou no fim, e cole de novo.
>
> **O cliente pagou pelo link do Mercado Pago e o pedido continua Não pago. Por quê?** Clique em **Conferir**, na linha do link, para a plataforma buscar o pagamento. Se as Opções mostram *"O servidor não tem um endereço público configurado: o pagamento não baixa sozinho"*, a baixa sozinha não está disponível na sua plataforma, e o pedido baixa pelo **Conferir**.
>
> **Posso usar o Asaas e o Mercado Pago ao mesmo tempo nos pedidos?** Pode. Com os dois tokens salvos nas Opções, você escolhe na hora de cobrar qual link gerar.
>
> **O que é a Taxa da plataforma em cada cobrança, nas Opções do Mercado Pago?** É a parte de cada cobrança pelo Mercado Pago que fica com a plataforma, combinada com a sua empresa: um percentual do valor ou um valor fixo.
>
> **A tela diz que a taxa da plataforma é maior que o valor desta cobrança. O que fazer?** A taxa combinada passa do valor que você quer cobrar pelo link do Mercado Pago. Registre esse pagamento em outra forma, como Pix ou dinheiro.
>
> **Sem o Access Token do Mercado Pago, o pedido deixa de receber pagamento?** Não. Sem o Mercado Pago, o pedido oferece só os outros meios de pagamento, como os registrados à mão.
