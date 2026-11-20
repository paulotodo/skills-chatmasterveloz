# Credenciais PaggPix

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/credenciais-paggpix
- **Categoria:** Recursos
- **Menu:** Integrações › Credenciais PaggPix

---

🧩 As **credenciais da PaggPix**, o **Client ID** e o **Client Secret**, ligam a conta PaggPix da sua empresa aos pedidos do PDV. Com elas, a plataforma gera na sua conta PaggPix o Pix do pedido, com QR Code e Pix copia e cola, e fica sabendo quando o cliente pagou. O dinheiro cai direto na sua conta PaggPix.

Diferente de um link de pagamento, o Pix da PaggPix chega pronto na conversa: o cliente lê o QR Code ou copia o código e paga pelo aplicativo do banco.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Separe o **Client ID** e o **Client Secret** que a PaggPix entregou no cadastro da sua conta.
>
> ➡️ Na plataforma, acesse o menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**, preencha **Client ID da PaggPix** e **Client Secret da PaggPix** e clique em **Salvar**.
>
> ➡️ Se a conta PaggPix tiver mais de um CNPJ ou CPF, escolha em **CNPJ/CPF que recebe os pagamentos** qual deles recebe e clique em **Salvar** de novo.

## Como integrar a PaggPix à nossa plataforma

Acesse o menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**.

🔘 **Client ID da PaggPix** e **Client Secret da PaggPix:** cole as duas credenciais e clique em **Salvar**. A tela confirma que a PaggPix foi conectada e mostra o CNPJ ou CPF que recebe os pagamentos.

🔘 **CNPJ/CPF que recebe os pagamentos:** aparece quando a conta PaggPix tem mais de um documento. Nas palavras da tela: *"Esta conta PaggPix tem mais de um CNPJ/CPF. Escolha qual recebe os pagamentos do PDV e salve de novo."*

🔘 **Trocar as credenciais da PaggPix:** cole de novo o Client ID e o Client Secret e clique em **Salvar**.

🔘 **Desconectar:** tira a PaggPix dos pedidos. Sem as credenciais, o pedido oferece só os outros meios de pagamento.

⚠️ Só o administrador da empresa vê e muda os campos da PaggPix.

## Como fica no pedido

☑️ Com as credenciais salvas, o pedido confirmado ganha o botão **Gerar Pix (PaggPix)** na parte de pagamentos. O Pix é enviado na conversa, com o QR Code e o Pix copia e cola. Na linha do Pix, **Copiar o Pix copia e cola** copia o código para você mandar de novo.

☑️ Quando o cliente paga, o pedido fica **Pago** sozinho. Para a plataforma buscar o pagamento na hora, clique em **Conferir**, na linha do Pix: a tela responde *"Pix da PaggPix recebido e baixado."* ou *"A PaggPix ainda não registrou o pagamento deste Pix."*

☑️ **Reenviar Pix (PaggPix)** manda o Pix de novo na conversa. Se o Pix venceu, um novo é gerado na hora; se o cliente já pagou, o pedido é baixado.

## Boas práticas para gerenciar as credenciais da PaggPix

➡️ **Não compartilhe o Client Secret:** junto com o Client ID, ele dá acesso à sua conta PaggPix pela API.

➡️ **Credenciais vazadas:** peça credenciais novas à PaggPix e cole as duas de novo nas Opções.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente pagou o Pix da PaggPix e o pedido continua Não pago. Por quê?** Clique em **Conferir**, na linha do Pix, para a plataforma buscar o pagamento. Se as Opções mostram *"O servidor não tem um endereço público configurado, ou a PaggPix não aceitou o aviso: o pagamento não baixa sozinho"*, a baixa sozinha não está disponível, e o pedido baixa pelo **Conferir**.
>
> **O Pix da PaggPix venceu antes de o cliente pagar. Preciso fazer outro pedido?** Não. Clique em **Reenviar Pix (PaggPix)**: com o Pix vencido, um novo é gerado na hora e enviado na conversa.
>
> **A conta PaggPix tem dois CNPJs. Qual recebe o Pix do pedido?** O que estiver escolhido em **CNPJ/CPF que recebe os pagamentos**, nas Opções. O campo aparece quando a conta PaggPix tem mais de um documento.
>
> **Sem as credenciais da PaggPix, o pedido deixa de receber pagamento?** Não. Sem a PaggPix, o pedido oferece só os outros meios de pagamento, como os registrados à mão.
