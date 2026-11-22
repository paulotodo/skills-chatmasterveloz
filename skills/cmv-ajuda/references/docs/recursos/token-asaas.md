# Token Asaas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/token-asaas
- **Categoria:** Recursos
- **Menu:** Integrações › Token Asaas

---

🧩 O **token do Asaas** é a chave de API da conta Asaas da sua empresa. É ela que deixa a plataforma criar o link de pagamento de um pedido na sua conta Asaas, saber quando o cliente pagou e devolver o pagamento estornado. O dinheiro cai direto na sua conta, com as tarifas do seu contrato com o Asaas.

A mesma chave serve aos dois recursos que usam o Asaas, se estiverem disponíveis no seu plano: o **link de pagamento do pedido do PDV** e o bloco **Asaas** do FlowBuilder Nativo, que envia ao cliente a segunda via de uma cobrança. O PDV lê a chave das **Opções** da empresa; o bloco tem o próprio campo de token.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No Asaas, gere a chave de API em **Integrações → Chaves de API**.
>
> ➡️ Na plataforma, acesse o menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**, cole a chave em **Token do Asaas da empresa (links de pagamento do PDV)** e clique em **Salvar**.
>
> ➡️ Copie o endereço do campo **Aviso do Asaas para o PDV (webhook)** e cadastre nos webhooks do Asaas.

## Como criar a chave de API no Asaas

➡️ Entre na sua conta em [https://www.asaas.com](https://www.asaas.com) com um usuário **administrador** da conta Asaas: só ele vê **Integrações** e gera a chave. O aplicativo do Asaas não gera chave.

➡️ Abra o **menu do usuário** e clique em **Integrações**.

➡️ Na aba **Chaves de API**, clique em **Gerar chave de API** e preencha a janela:

🔘 **Nome da chave:** um nome que diga onde a chave é usada, como *Plataforma*.

🔘 **Data de expiração** e **Hora de expiração:** são opcionais. Se você definir, a chave para de funcionar nessa data e hora, e o PDV só volta a gerar link de pagamento quando você colar uma chave nova no **Token do Asaas da empresa**.

🔘 **Permitir que esta chave execute operações de saque via API (Pix, Ted, Pague Contas e Recarga de celular):** deixe desmarcada. O link de pagamento do pedido e o estorno do pagamento não precisam dessa permissão.

➡️ Clique em **Avançar** e siga até o Asaas mostrar a chave.

➡️ Copie a chave na hora e guarde em local seguro: o Asaas mostra a chave inteira uma vez só.

⚠️ Use a chave da conta de **produção**, que começa com `$aact_prod_`. A chave do ambiente de testes do Asaas (sandbox), que começa com `$aact_hmlg_`, não gera link de pagamento na plataforma.

⚠️ O Asaas desabilita a chave que fica **3 meses sem uso** e a expira de vez depois de **6 meses**. Se a loja passar esse tempo sem gerar link nem conferir pagamento, confira na aba **Chaves de API** se a chave continua **Habilitado**.

## Como integrar o Asaas à nossa plataforma

Acesse o menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**.

🔘 **Token do Asaas da empresa (links de pagamento do PDV):** cole a chave e clique em **Salvar**. O botão ao lado do campo mostra ou esconde o token.

🔘 **Aviso do Asaas para o PDV (webhook):** é o endereço que avisa a plataforma quando o cliente paga. Copie o endereço deste campo para o próximo passo.

⚠️ Só o administrador da empresa vê e muda esses dois campos.

### Cadastrar o aviso no Asaas

➡️ No Asaas, em **Integrações**, abra a aba **Webhooks** e clique em **Adicionar Webhook**.

🔘 **Este Webhook ficará ativo?:** deixe ligado.

🔘 **Nome do Webhook:** até 50 caracteres, como *Pedidos da plataforma*.

🔘 **URL do Webhook:** cole o endereço do campo **Aviso do Asaas para o PDV (webhook)**.

🔘 **E-mail:** informe o seu. O Asaas avisa nesse e-mail quando falha ao enviar um aviso.

🔘 **Versão da API:** escolha a **v3**.

🔘 **Token de autenticação:** a plataforma não pede esse token. Se o Asaas não deixar salvar com o campo vazio, clique em **Gerar Token**.

🔘 **Tipo de envio:** escolha o envio **sequencial**, que entrega os avisos na ordem em que aconteceram.

🔘 **Fila de sincronização ativada?:** deixe ligado. Com a fila interrompida, o Asaas continua registrando os pagamentos, mas só avisa a plataforma depois que você ativar a fila de novo.

🔘 **Adicionar Eventos:** abra o grupo **Cobranças** e marque os eventos de cobrança. Os outros grupos não são necessários, e quanto menos eventos, mais eficiente o envio.

➡️ Clique em **Salvar**.

## Como fica no pedido

☑️ Com o token salvo, o pedido confirmado ganha o botão **Gerar link do Asaas** na parte de pagamentos. O cliente recebe na conversa *"Pague o pedido #N (R$ X) por este link:"* com o link, e escolhe como pagar na página do Asaas.

☑️ Com o aviso cadastrado, o pedido fica **Pago** sozinho poucos segundos depois do pagamento. Sem o aviso, clique em **Conferir no Asaas**, na linha do link, para a plataforma buscar o pagamento.

☑️ Depois do pagamento, a plataforma desativa o link no Asaas, e o cliente não consegue pagar o mesmo link de novo.

⚠️ O Asaas só gera link a partir de **R$ 10,00**.

## Boas práticas para gerenciar a chave

➡️ **Não compartilhe a chave:** ela dá acesso total para ver e mudar os dados da sua conta Asaas, como uma senha.

➡️ **Uma chave por integração:** com uma chave para a plataforma e outra para cada sistema, você apaga uma sem parar as outras.

➡️ **Chave vazada:** apague a chave no Asaas, gere uma nova e cole a nova no campo **Token do Asaas da empresa**, e também no bloco **Asaas** do FlowBuilder Nativo, se usar a mesma chave lá.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O botão Gerar link do Asaas mostra "Não foi possível falar com o servidor". O que fazer?** A mesma mensagem aparece quando o Asaas recusa o pedido. Confira se o pedido tem pelo menos R$ 10,00 e se o **Token do Asaas da empresa** é a chave de produção, que começa com `$aact_prod_`. Confira também, na aba **Chaves de API** do Asaas, se a chave continua **Habilitado**: a chave sem uso por 3 meses é desabilitada e pode ser reativada ali. Depois de 6 meses sem uso, ou passada a data de expiração que você definiu, gere uma chave nova e cole no **Token do Asaas da empresa**.
>
> **O cliente pagou pelo link do Asaas e o pedido continua Não pago. Por quê?** O aviso do Asaas não chegou: confira se o webhook com o endereço do **Aviso do Asaas para o PDV (webhook)** aparece como **Ativado** na aba **Webhooks** do Asaas, com os eventos de cobrança e a **Fila de sincronização** ativada. A aba **Logs de Webhooks** mostra os avisos que o Asaas enviou. Enquanto isso, **Conferir no Asaas**, na linha do link, dá a baixa.
>
> **Estornei no pedido um pagamento feito pelo link do Asaas. O dinheiro volta para o cliente?** Sim. **Estornar** pede a devolução ao Asaas, e o pedido volta a **Não pago**. Se a sua conta Asaas pede autorização para ações críticas, a devolução só é feita depois que você digita o token no painel do Asaas, que dá 24 horas para isso.
>
> **Posso testar o link de pagamento do pedido com a conta de testes do Asaas?** Não. O link de pagamento do pedido usa só o Asaas de produção, e a chave do ambiente de testes não gera link.
