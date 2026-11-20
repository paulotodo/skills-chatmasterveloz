# Opções do PDV

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/opcoes-do-pdv
- **Categoria:** Recursos
- **Menu:** PDV › Opções do PDV

---

🧩 As **Opções do PDV** decidem como o PDV se comporta na sua empresa: se vende sem estoque, por onde o cliente paga a distância, o desconto ou a taxa de cada forma de pagamento, até quanto de desconto o atendente pode dar, o que o cliente recebe a cada etapa do pedido, quanto custa a entrega em cada bairro, faixa de CEP ou pelos Correios, como o painel da cozinha marca os pedidos atrasados, o nome de cada etapa do painel, como o pedido é impresso na impressora térmica e, nas mesas do salão, a taxa de serviço e a comissão do garçom.

As **Opções do PDV** ficam juntas no menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**, menos o **Webhook do PDV**, que fica na aba **Integrações e segurança**. Só o administrador abre esse menu e as muda.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**. A fileira de subtítulos no topo da aba leva direto a cada parte.
>
> ➡️ Ajuste cada opção e clique no **Salvar** dela. Os avisos são salvos juntos, em **Salvar avisos**.

## Vídeo Tutorial

[Vídeo Voomly — id kZUfA119QhPVl_1RmlYYSM7B0latVijI0sizeNQRVhjLxKYrR, tipo v]  

## As opções

🔘 **PDV: vender sem estoque:** com **Sim**, o pedido confirma mesmo sem estoque suficiente, e o saldo do produto fica negativo. Com **Não**, o pedido só confirma com estoque.

🔘 **Cardápio Digital: mostrar "Indisponível" quando o estoque zerar:** aparece com **PDV: vender sem estoque** em **Sim**. A tela explica: *"Vale quando o PDV vende sem estoque. Sim: o produto aparece como Indisponível no Cardápio e não pode ser pedido por lá. Não: continua à venda."*

🔘 **Token do Asaas da empresa (links de pagamento do PDV):** a chave de API da conta Asaas da sua empresa. Com ela, o pedido do PDV gera o link de pagamento, e o dinheiro cai na sua conta. O botão ao lado mostra ou esconde o token.

🔘 **Aviso do Asaas para o PDV (webhook):** o endereço que você cadastra nos webhooks da sua conta Asaas, para o pedido pago pelo link dar baixa sozinho.

🔘 **Access Token do Mercado Pago da empresa (links de pagamento do PDV):** o Access Token de produção da conta Mercado Pago da sua empresa. Com ele, o pedido gera o link de pagamento do Mercado Pago (Pix, cartão ou boleto), o dinheiro cai na sua conta e o pedido baixa sozinho quando o cliente paga.

🔘 **Token do PagSeguro (PagBank) da empresa (links de pagamento do PDV):** o token de segurança da conta PagBank da sua empresa. Com ele, o pedido gera o link do PagSeguro (Pix, cartão ou boleto) e baixa sozinho quando o cliente paga. O token de uma conta de testes do PagBank também é aceito, e a tela avisa que esses links não cobram de verdade.

🔘 **Client ID da PaggPix** e **Client Secret da PaggPix:** as credenciais que a PaggPix entregou no cadastro. Com elas, o pedido gera o Pix com QR Code e Pix copia e cola, e baixa sozinho quando o cliente paga. Se a conta PaggPix tem mais de um CNPJ ou CPF, escolha em **CNPJ/CPF que recebe os pagamentos** qual recebe e salve de novo.

O Mercado Pago, o PagSeguro e a PaggPix têm cada um o seu **Desconectar**. Sem as credenciais de um deles, o pedido oferece só os outros meios de pagamento, como os registrados à mão.

🔘 **Desconto e taxa por forma de pagamento:** a tela explica: *"Dê um desconto ou cobre uma taxa conforme a forma de pagamento, em valor ou em %. A janela do pagamento, o balcão e a loja online (dinheiro, cartão e Pix na entrega) já mostram quanto cobrar. Em branco: sem desconto nem taxa."* Cada forma — **Dinheiro**, **Pix**, **Cartão**, **Boleto** e **Outro** — tem um **Desconto** e uma **Taxa**, em **%** ou em **Valor**. O campo vazio mostra *Sem*. Clique em **Salvar**.

◽ Com a regra salva, a lista **Forma** do **Balcão** já mostra o ajuste de cada forma, como *Pix · 5% de desconto* ou *Cartão · taxa de R$ 2,00*. Escolhida a forma, a venda ganha a linha **Desconto da forma de pagamento** ou **Taxa da forma de pagamento**, o **Total** já vem ajustado, e a tela avisa, como *"Pix: R$ 1,45 de desconto já no valor"*.

◽ No pedido que o próprio cliente faz, a escolha do pagamento na entrega mostra o ajuste ao lado de cada forma, e o total da sacola muda com a forma escolhida, como *Desconto (Pix) - R$ 1,77*.

◽ O desconto em % vai até 100, com até duas casas, e a taxa aceita até duas casas. Fora disso, a tela avisa *"Use um número com até duas casas (o % vai até 100)."* e o **Salvar** fica desativado.

🔘 **Desconto máximo do atendente (%):** em branco, sem limite. Acima do limite, o atendente salva o rascunho e um supervisor ou administrador confirma o pedido. Aceita de 0 a 100, com até duas casas, como 10 ou 12,5. O limite vale também para o **Desconto na conta** da mesa.

🔘 **Taxa de serviço da mesa (%):** em branco, sem taxa. A tela explica: *"A conta da mesa abre com este percentual sobre o consumo, e o caixa pode tirar a taxa de cada conta antes de receber."* Aceita de 0 a 30, com até duas casas, como 10 ou 12,5.

🔘 **Comissão do garçom:** a tela explica: *"Calculada sobre as rodadas que cada garçom lançou nas mesas. Aparece no Relatório do PDV, e o garçom vê a dele. Mudar a regra vale para as rodadas confirmadas daqui para a frente."* **Parte da taxa de serviço (%)** vai de 0 a 100, e em branco 100% da taxa vai para quem lançou. **Comissão sobre o consumo (%)** vai de 0 a 30, e em branco não há comissão sobre o consumo. Clique em **Salvar comissão**.

🔘 **Webhook do PDV:** fica no menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Webhooks e integrações**. É o endereço do seu sistema que recebe os eventos de pedidos, pagamentos, caixa, estoque e entregas. Em branco, nada é enviado.

🔘 **Taxa de entrega por bairro:** a tabela de bairros e taxas. No pedido com entrega, escolher o bairro preenche a taxa, e o atendente ainda pode ajustar o valor. Para incluir, preencha **Bairro** e **Taxa (R$)** e clique em **Acrescentar**.

🔘 **Frete por faixa de CEP:** fica logo abaixo da **Taxa de entrega por bairro**. A tela explica: *"No pedido de entrega, o CEP que cai numa faixa usa o frete e o prazo dela; fora das faixas, vale a taxa do bairro. Deixe o CEP final vazio para uma faixa de um CEP só."* Cada faixa tem **Região (opcional)**, **CEP inicial**, **CEP final**, **Frete (R$)** e **Prazo (opcional)**, como *até 40 min* ou *3 dias úteis*. Para incluir, preencha a linha e clique em **Acrescentar**. Cada faixa gravada tem o seu **Salvar** e o seu **Remover**, que pede confirmação antes de apagar.

◽ O CEP aceita o número com ou sem o traço, e o frete aceita vírgula, como `7,50`. Com o **CEP final** vazio, a faixa fica com um CEP só, igual ao inicial.

◽ **Acrescentar** fica desativado com um CEP incompleto ou com o **CEP final** antes do **CEP inicial**. A faixa que cobre CEPs de outra faixa já cadastrada não é salva, e a tela avisa *"Essa faixa cobre CEPs de outra faixa já cadastrada."*

◽ **Frete por faixa de CEP com a Taxa de entrega por bairro:** o CEP que cai numa faixa usa o frete e o prazo dela, mesmo com o bairro na tabela de bairros. O CEP fora das faixas usa a taxa do bairro. No pedido de **Retirada**, nem o CEP nem o frete entram. Sem nenhuma faixa cadastrada, vale só a tabela de bairros.

◽ No pedido que o próprio cliente faz, com faixas cadastradas, ele informa o CEP antes do endereço e vê o frete e o prazo da faixa, como *"R$ 7,50 · até 40 min"*. O CEP fora das faixas e sem um bairro da tabela fica fora da área de entrega, e o cliente vê *"Ainda não entregamos neste CEP."*

🔘 **Frete pelos Correios (Loja Digital):** a tela explica: *"Use o contrato da sua empresa nos Correios: o cliente da Loja Digital vê o preço e o prazo do PAC e do SEDEX pelo CEP."* Ligue **Calcular o frete pelos Correios na loja** e preencha o contrato: **Usuário (Meu Correios)**, **Código de acesso à API**, **Cartão de postagem** e **CEP de origem**.

◽ **Serviços:** cada serviço dos Correios tem o **Código**, com 5 dígitos, e o **Nome na loja**. O **PAC** (03298) e o **SEDEX** (03220) já vêm preenchidos; **Adicionar serviço** e **Remover** mudam a lista.

◽ **Dias de manuseio:** aceita de 0 a 30 dias.

◽ **Peso padrão (g)**, **Altura padrão (cm)**, **Largura padrão (cm)** e **Comprimento padrão (cm):** as medidas usadas no frete do produto que não tem as dele. O peso vai até 30.000 g, e cada medida, até 100 cm.

◽ **Salvar** confere o contrato com os Correios na hora. Contrato recusado não é gravado, e a tela avisa *"Os Correios recusaram o usuário, o código de acesso ou o cartão de postagem."*

◽ **Testar cotação:** fica ativo com o frete ligado e pede o **CEP para testar** e o **Peso (g)**.

🔘 **Painel de pedidos:** **Atenção (minutos)** e **Atraso (minutos)** mudam a cor do card do pedido no painel, contando desde a confirmação: amarelo na atenção, vermelho no atraso. **Antecedência do agendado (minutos)** diz quanto tempo antes do horário combinado o pedido agendado entra em **Novo**. O atraso tem de ser maior que a atenção.

🔘 **Segmento do negócio:** escolhe os termos de partida do PDV. Em **Alimentação (restaurante, lanchonete, pizzaria)**, valem os nomes de sempre, como **Em preparo** e **Adicionais**. Em **Varejo (loja)** e **Farmácia**, a etapa vira **Separando**, os adicionais viram **Opcionais**, e a impressão e o botão da venda de balcão passam a falar em separação, como *Via da separação* e *Mandar para a separação*. Em **Outro negócio**, a etapa vira **Em andamento**, os adicionais viram **Opcionais**, e a impressão e o botão passam a falar em painel. O **Segmento do negócio** é salvo junto com o **Painel de pedidos**, e o que você escrever em **Nomes das etapas** vale por cima dele.

🔘 **Nomes das etapas:** os nomes que aparecem no painel de pedidos — **Novo**, **Em preparo**, **Pronto**, **Saiu**, **Entregue** e **Agendados** — e o texto do **Botão da venda de balcão** (em branco, *Enviar para o painel de pedidos*). Cada nome tem até 30 caracteres, e o campo em branco fica com o nome padrão. O nome novo aparece na coluna do painel e no botão do card que leva o pedido para ela. Os **Nomes das etapas** são salvos junto com o **Painel de pedidos**, no **Salvar** dele.

🔘 **Impressão térmica:** como o pedido é impresso pelo **Painel de pedidos** numa impressora térmica. **Largura da bobina** escolhe **80 mm** ou **58 mm**; **Vias da cozinha** e **Vias do cliente** dizem quantas de cada são impressas a cada vez, de 0 a 3. A via da cozinha traz só os itens, sem preço e com letra grande; a do cliente traz os preços, o total e o aviso *"Este documento não é nota fiscal."*. Pelo menos uma via precisa ser impressa: com as duas em 0, a impressão não é salva. Clique no **Salvar** da **Impressão térmica**.

🔘 **Imprimir sem a janela de impressão:** os passos que a tela dá para o computador da cozinha imprimir cada pedido sem perguntar nada: deixar a impressora térmica como a impressora padrão do Windows; criar um atalho do Google Chrome e, em *Propriedades > Destino*, acrescentar no fim `--kiosk-printing`; abrir o sistema por esse atalho, entrar no **Painel de pedidos** e ligar **Imprimir sozinho**.

🔘 **Mapa do rastreio da entrega:** o mapa que o cliente vê no rastreio e a loja vê no **Mapa dos entregadores**. O **OpenStreetMap (grátis)** não pede chave; o **Google Maps** usa a **Chave da API do Google** da sua empresa.

⚠️ Com o **Google Maps**, ative na sua conta do Google as APIs Maps JavaScript, Geocoding e Distance Matrix. A chave aparece para o cliente no rastreio: restrinja-a ao endereço do seu painel.

## Os avisos do pedido ao cliente

Os **Avisos do pedido ao cliente** são mensagens enviadas sozinhas na conversa do pedido, cada uma quando está ligada. Cada aviso tem o interruptor para ligar e o texto, com até 2000 caracteres:

◽ **Pedido confirmado:** quando o pedido é confirmado.

◽ **Pagamento recebido:** quando o pedido fica pago.

◽ **Em preparo:** quando a cozinha começa o preparo no painel de pedidos.

◽ **Pronto para retirada:** quando o pedido fica pronto. Vale só para o pedido de retirada no local.

◽ **Saiu para entrega:** quando o pedido é despachado. O link do rastreio da entrega vai junto, no fim da mensagem.

◽ **Pedido entregue:** quando o pedido é entregue.

◽ **Pagamento estornado:** quando o valor do pagamento é devolvido ao cliente, também no estorno de um pagamento registrado à mão, como o em dinheiro. Com o texto que vem na tela, o cliente recebe *"Estornamos o pagamento do pedido #75. O valor volta pela mesma forma de pagamento."*

◽ **Pedido cancelado:** quando o pedido é cancelado ou recusado no **Painel de pedidos**, com o motivo escolhido ali. A tela avisa que ele vale para o pedido de entrega ou de retirada, e que o de mesa ou comanda não recebe. O texto que vem na tela leva o número do pedido e o motivo, como *"Olá! Seu pedido nº 38 foi cancelado. Motivo: Cliente desistiu. Se precisar, é só responder esta mensagem."*

Os textos aceitam as variáveis `{{numero}}` (o número do pedido), `{{total}}`, `{{itens}}`, `{{endereco}}`, `{{bairro}}`, `{{agendado}}`, `{{rastreio}}`, `{{name}}` e `{{firstName}}` (o nome do cliente) e `{{ms}}`, que vira a saudação do horário, como *Bom dia*. O aviso **Pedido cancelado** aceita também `{{motivo}}`, o motivo escolhido no cancelamento. **Voltar ao texto padrão** desfaz a mudança de um aviso.

📌 Exemplo: o aviso **Pedido confirmado** com o texto que vem na tela chega ao cliente como *"Bom dia! Seu pedido #11 foi confirmado. Total: R$ 43,40."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Liguei a opção Pronto para retirada e o cliente com entrega não recebeu o aviso.** É o esperado: o aviso **Pronto para retirada** vale só para o pedido de retirada no local. No pedido com entrega, o cliente recebe o aviso **Saiu para entrega**.
>
> **O aviso Pedido cancelado manda o motivo ao cliente?** Manda. O texto que vem na tela já traz `{{motivo}}`, que vira o motivo escolhido no **Painel de pedidos**, como *Cliente desistiu*, ou o que foi escrito em **Outro**.
>
> **A taxa de entrega por bairro trava o valor no pedido?** Não. Escolher o bairro preenche a taxa, e o atendente pode mudar o valor naquele pedido. A tabela continua igual.
>
> **Posso deixar o Asaas, o Mercado Pago e o PagSeguro ligados ao mesmo tempo nas Opções do PDV?** Pode. Com os três salvos, o atendente escolhe na hora de cobrar qual link gerar.
>
> **Como volto ao nome padrão de uma etapa em Nomes das etapas?** Apague o nome do campo e clique no **Salvar** do **Painel de pedidos**: a etapa volta ao nome padrão.
>
> **Quantas vias são impressas quando eu imprimo um pedido do Painel de pedidos?** As que estão na **Impressão térmica**, nas Opções do PDV: a quantidade de **Vias da cozinha** e de **Vias do cliente**, numa impressão só.
>
> **A via da cozinha mostra o preço do pedido?** Não. A via da cozinha traz só os itens, em letra grande. O preço, o total e o aviso de que o documento não é nota fiscal vão na via do cliente.
>
> **A opção Cardápio Digital: mostrar "Indisponível" quando o estoque zerar não aparece nas Opções do PDV. O que falta?** Ela só aparece com **PDV: vender sem estoque** em **Sim**. Com **Não**, o produto zerado já aparece como Indisponível no Cardápio Digital.
>
> **Cadastrei o Frete por faixa de CEP. A Taxa de entrega por bairro deixa de valer?** Não. A taxa do bairro vale para o CEP que fica fora de todas as faixas. O CEP que cai numa faixa usa o frete dela, mesmo com o bairro na tabela.
>
> **Como cadastro o frete de um CEP só no Frete por faixa de CEP?** Preencha o **CEP inicial** e deixe o **CEP final** vazio: a faixa fica com um CEP só.
>
> **Deixei a Comissão do garçom em branco. O garçom ganha comissão?** Com a **Parte da taxa de serviço (%)** em branco, 100% da taxa de serviço de cada rodada vai para quem lançou. Com a **Comissão sobre o consumo (%)** em branco, não há comissão sobre o consumo.
>
> **O Testar cotação dos Correios está desativado. Por quê?** O **Testar cotação** fica desativado com **Calcular o frete pelos Correios na loja** desligado. Ligue o frete, preencha o contrato dos Correios e clique em **Salvar**.
>
> **Quem pode mudar as Opções do PDV?** O administrador da empresa.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Desconto máximo com vírgula errada:** o campo recusa e avisa *"Use um número de 0 a 100, com até duas casas (ex.: 10 ou 12,5)."* **Solução:** digite só o número, sem o sinal de porcentagem.
>
> **Taxa de serviço da mesa fora da faixa:** a taxa não é salva, e a tela avisa *"Use um número de 0 a 30, com até duas casas (ex.: 10 ou 12,5)."* **Solução:** use um número de 0 a 30, sem o sinal de porcentagem.
>
> **Atraso menor que a atenção:** o painel não salva e pede *"Use minutos de 1 a 1440, com o atraso maior que a atenção."* **Solução:** ponha no **Atraso (minutos)** um valor maior que o da **Atenção (minutos)**.
>
> **Faixa de CEP sobreposta:** a faixa não é salva, e a tela avisa *"Essa faixa cobre CEPs de outra faixa já cadastrada."* **Solução:** ajuste o **CEP inicial** e o **CEP final** para não cobrir a outra faixa, ou mude a faixa que já existe e clique no **Salvar** dela.
>
> **Acrescentar desativado no Frete por faixa de CEP:** a linha não é incluída. **Solução:** confira se os CEPs têm os 8 números e se o **CEP final** não vem antes do **CEP inicial**.
>
> **Frete pelos Correios sem os dados do contrato:** ligar o frete com algum campo vazio não salva, e a tela pede *"Para ligar o frete pelos Correios, preencha o usuário, o código de acesso, o cartão e o CEP de origem."* **Solução:** preencha os quatro campos do contrato e clique em **Salvar**.
>
> **Serviço dos Correios recusado:** a tela avisa *"Cada serviço dos Correios precisa de um código de 5 dígitos e um nome, sem repetir."* **Solução:** confira o **Código** de 5 dígitos e o **Nome na loja** de cada serviço, sem dois iguais.
