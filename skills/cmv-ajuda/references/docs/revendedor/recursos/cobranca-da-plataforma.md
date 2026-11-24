# Cobrança da plataforma

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/cobranca-da-plataforma
- **Categoria:** Recursos
- **Menu:** Configurações › Plataforma em Configurações › Cobrança da plataforma

---

🧩 O grupo **Cobrança da plataforma** guarda o que você usa para cobrar as faturas das empresas da sua instância: as credenciais de cada meio de cobrança — **ASAAS**, **Stripe**, **Mercado Pago**, **PAYPAL** e **Pix Efí** — e, na seção **PATIBILL**, as mensagens enviadas pelo WhatsApp sobre a fatura. Tudo aqui vale para todas as empresas da instância.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Plataforma**, grupo **Cobrança da plataforma**.
>
> ➡️ Preencha a seção de cada meio de cobrança que você usa.
>
> ➡️ Cada campo grava assim que você muda o valor. O certificado da Efí é a exceção: tem o botão **ENVIAR CERTIFICADO**.

## ⚡ ASAAS

A seção **ASAAS** guarda a chave e as regras de cobrança usadas para gerar as faturas das empresas pela Asaas.

➡️ Na sua conta Asaas, gere uma chave de API de **produção**.

➡️ Cole a chave em **Token Asaas** e digite os códigos nos três campos de regra.

🔘 **Token Asaas:** a chave de API da conta que recebe.

🔘 **Forma de Pagamento Permitida:** o meio que a fatura aceita. Digite `PIX`.

🔘 **Forma de Cobrança:** como a cobrança é criada na Asaas. Digite `RECURRENT`.

🔘 **Ciclo de Cobrança:** a periodicidade da cobrança. Digite `MONTHLY`.

⚠️ Os três campos de regra são texto livre, sem lista de opções: `PIX`, `RECURRENT` e `MONTHLY` são digitados no campo, exatamente como a Asaas reconhece.

## ⚡ Stripe

A seção **Stripe** guarda a chave e a moeda usadas para cobrar as faturas das empresas pelo Stripe.

➡️ No painel do Stripe, em chaves de API do modo de **produção**, copie a chave secreta.

➡️ Cole em **Stripe Private Key** e informe a moeda em **Moeda Stripe**.

🔘 **Stripe Private Key:** a chave **secreta** da conta Stripe, do modo de **produção** — não a chave publicável.

🔘 **Moeda Stripe:** o código da moeda das cobranças, por exemplo `brl`.

## ⚡ Mercado Pago

A seção **Mercado Pago** guarda a credencial usada para cobrar as faturas das empresas pelo Mercado Pago.

➡️ Nas credenciais de **produção** da sua conta no Mercado Pago, copie o **Access Token** e cole no campo de mesmo nome.

🔘 **Access Token:** a credencial de **produção** da conta que recebe. Credencial de teste gera cobrança que ninguém consegue pagar.

## ⚡ PAYPAL

A seção **PAYPAL** guarda a conta e a moeda usadas para cobrar as faturas das empresas pelo PayPal.

🔘 **E-Mail Paypal:** o e-mail da conta PayPal que recebe os pagamentos.

🔘 **Moeda Paypal:** o código da moeda das cobranças, por exemplo `BRL`.

## ⚡ Configuração Pix Efí (GerenciaNet)

A seção **Configuração Pix Efí (GerenciaNet)** guarda as credenciais e o certificado da conta Efí usados para cobrar as faturas das empresas por PIX.

➡️ No painel da Efí, crie uma aplicação com a API Pix, copie **Client ID** e **Client Secret** e gere o certificado `.p12` da mesma aplicação.

➡️ Preencha **Client ID**, **Client Secret** e **Chave PIX**.

➡️ Em **Tipo de certificado**, selecione **Certificado Efí p12 - API PIX**, escolha o arquivo em **Escolher Certificado .p12** e clique em **ENVIAR CERTIFICADO**.

🔘 **Client ID** e **Client Secret:** as credenciais da aplicação criada na Efí.

🔘 **Chave PIX:** a chave da conta Efí que recebe os pagamentos.

Os três campos gravam assim que você muda o valor. Só o certificado tem botão próprio.

### O certificado

Logo abaixo dos campos, no bloco **Configure o certificado Efí para API PIX**, fica o envio do certificado digital — a segunda metade da cobrança por PIX.

🔘 **Tipo de certificado:** hoje há uma única opção, **Certificado Efí p12 - API PIX**.

🔘 **Escolher Certificado .p12:** o arquivo do certificado. Só arquivo `.p12` é aceito.

🔘 **ENVIAR CERTIFICADO:** envia o arquivo escolhido.

Nas palavras da tela: *"🔒 Segurança: O certificado digital (.p12) é necessário para autenticar comunicações com a API PIX da Efí (antiga Gerencianet). Mantenha este arquivo seguro e não compartilhe com terceiros. O certificado possui senha e é único para sua conta Efí. Certifique-se de que o arquivo está atualizado e dentro do prazo de validade para evitar problemas de integração."*

⚠️ Credencial sem certificado não funciona. As duas partes precisam ser da mesma aplicação da Efí: o `.p12` tem que ser da aplicação de onde saíram o **Client ID** e o **Client Secret**.

## ⚡ PATIBILL

A seção **PATIBILL** configura as mensagens que a plataforma envia pelo WhatsApp sobre a fatura de cada empresa: o agradecimento quando ela paga e os lembretes de vencimento e atraso. Não é um meio de pagamento — é a comunicação em volta dele.

🔘 **Mensagem de Agradecimento pelo Pagamento:** o texto enviado quando a fatura é paga.

🔘 **Enviar Lembrete de Vencimento e Atraso por WhatsApp?:** com **Sim**, os dois lembretes abaixo passam a ser enviados. Com **Não**, só o agradecimento existe.

🔘 **Mensagem de Lembrete enviada a partir de 2 dias do vencimento:** o texto do aviso que começa dois dias antes de a fatura vencer.

🔘 **Mensagem de Lembrete enviada para contas vencidas:** o texto do aviso para fatura já vencida.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A fatura não aparece na Asaas.** Confira o **Token Asaas** (produção, não sandbox) e os três campos de regra, que precisam bater com os códigos da Asaas.
>
> **Colei a Stripe Private Key e a fatura não gera cobrança.** Confira se a chave é a secreta de produção e se a **Moeda Stripe** está preenchida. Chave de teste ou moeda vazia param a cobrança sem mensagem clara.
>
> **O pagamento pelo PayPal caiu em outra conta.** O **E-Mail Paypal** informado é o que define a conta de destino. Confira se é o da conta comercial certa.
>
> **Preenchi a Configuração Pix Efí e o PIX não gera.** Falta o certificado, ou ele é de outra aplicação da Efí. Envie o `.p12` da mesma aplicação de onde saíram o **Client ID** e o **Client Secret**.
>
> **O certificado da Efí vence?** Vence: a própria tela pede que o arquivo esteja atualizado e dentro do prazo de validade. Anote a data ao gerar o certificado.
>
> **Onde a empresa paga a fatura?** Os administradores de cada empresa têm acesso ao menu **Financeiro** quando a configuração **Exibir Fatura para Clientes?**, da seção **Configurações Globais** no grupo **Marca e acesso**, está em **Sim**.
>
> **Qual número envia as mensagens da PATIBILL?** A conexão definida como **padrão** no SuperAdmin.
>
> **O lembrete da PATIBILL não chegou.** Confira se **Enviar Lembrete de Vencimento e Atraso por WhatsApp?** está em **Sim** e se o telefone da empresa está preenchido no cadastro dela, no menu **Configurações  ›  Empresas**.
