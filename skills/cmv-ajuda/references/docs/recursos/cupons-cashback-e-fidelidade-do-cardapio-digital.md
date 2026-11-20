# Cupons, Cashback e Fidelidade do Cardápio Digital

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/cupons-cashback-e-fidelidade-do-cardapio-digital
- **Categoria:** Recursos
- **Menu:** PDV › Cupons, Cashback e Fidelidade do Cardápio Digital

---

🧩 Quer dar um desconto no primeiro pedido, lembrar do aniversário do cliente e premiar quem volta sempre, sem fazer conta na mão? Os **Cupons de desconto** e o **Cashback** do **Cardápio Digital** fazem isso na sacola da loja: o cupom tira um valor do pedido, e o cashback devolve ao cliente uma parte de cada pedido entregue, para ele usar como desconto na próxima compra.

O cartão fidelidade é um tipo de cupom: o tipo **Fidelidade** vale uma vez a cada tantos pedidos entregues do cliente.

Ideal para:

☑️ **Primeira compra:** o cupom de boas-vindas vale uma vez, só para quem ainda não fez pedido na loja.

☑️ **Data especial:** o cupom de aniversário vale uma vez por ano, perto do aniversário do cliente.

☑️ **Cliente que volta:** a fidelidade e o cashback dão um motivo para o próximo pedido.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **PDV  ›  Cardápio digital** e desça até **Cupons de desconto**.
>
> ➡️ Clique em **Novo cupom**, preencha o **Código**, o **Tipo** e o desconto, e clique em **Salvar**.
>
> ➡️ Para o cashback, preencha o bloco **Cashback**, na mesma tela, e clique no **Salvar** da loja.

## Os tipos de cupom

O campo **Tipo**, na janela **Novo cupom**, define quem pode usar o cupom:

🔘 **Por código:** *"Vale para quem digitar o código na sacola, até o limite de usos por cliente."*

🔘 **Boas-vindas:** *"Vale uma vez, só para quem ainda não fez nenhum pedido na loja."*

🔘 **Aniversário:** *"Vale uma vez por ano, perto do aniversário cadastrado no contato do cliente."* O campo **Dias antes e depois do aniversário** diz quantos dias em volta da data o cupom vale.

🔘 **Fidelidade:** *"Vale uma vez a cada tantos pedidos entregues do cliente; depois do uso, a contagem recomeça."* O campo **A cada quantos pedidos entregues** diz quantos pedidos o cliente precisa completar.

A tela avisa que os cupons de boas-vindas e de aniversário *"aparecem sozinhos na sacola de quem pode usar."*

## Os campos do cupom

🔘 **Código:** de 3 a 30 letras, números, `-` ou `_`. O código é gravado em maiúsculas.

🔘 **Desconto em:** **Porcentagem (%)** ou valor em reais.

🔘 **Desconto:** o tamanho do desconto, em porcentagem até 100.

🔘 **Desconto máximo (R$, opcional):** só no desconto em porcentagem, o teto em reais do desconto.

🔘 **Pedido mínimo (R$, opcional):** o valor que o pedido precisa alcançar para o cupom valer.

🔘 **Vale a partir de** e **Vale até:** o período de validade do cupom.

🔘 **Limite de usos no total (opcional):** quantas vezes o cupom pode ser usado, somando todos os clientes.

🔘 **Usos por cliente (vazio: sem limite):** só no tipo **Por código**.

🔘 **Descrição (opcional, o cliente vê):** o texto do cupom para o cliente.

🔘 **Ativo:** liga ou desliga o cupom.

## A lista de cupons

Cada cupom mostra o código, o tipo, o desconto, os usos, como *"0 de ∞ usos"*, e a descrição, com o interruptor, **Editar** e **Remover**.

**Remover** pergunta *"Excluir o cupom PROMO10?"* e avisa: *"Os pedidos que já usaram o cupom continuam com o desconto e o código."*

## Como ligar o cashback

O bloco **Cashback** fica na tela do Cardápio Digital. A tela explica: *"Devolva ao cliente uma parte de cada pedido entregue, para ele usar como desconto na próxima compra pela loja. Deixe o percentual vazio para desligar."*

🔘 **Cashback em cada pedido (%):** a parte do pedido entregue que volta para o cliente.

🔘 **Saldo mínimo para usar (R$):** o saldo que o cliente precisa ter para usar o cashback.

🔘 **Expira após quantos dias sem pedido:** quantos dias sem pedido até o saldo expirar.

Clique no **Salvar** da loja, e a tela confirma *"Loja salva"*.

## O que o cliente vê na sacola

Os cupons e o cashback aparecem para o cliente que entrou na loja com o código do WhatsApp. Para quem não entrou, a página não mostra cupom nem cashback. A sacola da loja traz:

🔘 **Cupom de desconto:** o campo para digitar o código, com o botão **Aplicar**.

🔘 **Cupons para você:** os cupons de boas-vindas e de aniversário que o cliente pode usar.

🔘 **Usar meu cashback:** a opção com o saldo do cliente, como *"Usar meu cashback (R$ 12,00)"*. Abaixo do saldo mínimo, a sacola mostra *"Seu cashback: R$ 3,00 · dá para usar a partir de R$ 5,00"*.

🔘 **Fidelidade:** o andamento do cliente no cupom de fidelidade, como *"Fidelidade: 3 de 5 pedidos · faltam 2 para ganhar"* e o desconto.

⚠️ Cupom e cashback valem para a sacola da loja. A sacola da mesa não tem cupom nem cashback.

## Avisos para o seu sistema

Com o **Webhook do PDV** preenchido no menu **Configurações  ›  Opções**, o seu sistema recebe também os avisos de cupom e de cashback: `cupom-criado`, `cupom-alterado`, `cupom-removido`, `cupom-usado`, `cashback-creditado`, `cashback-usado`, `cashback-estornado` e `cashback-expirado`. Eles estão na lista **Eventos enviados**, logo abaixo do campo do **Webhook do PDV**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Como desligo o cashback do Cardápio Digital?** Deixe vazio o campo **Cashback em cada pedido (%)** e clique no **Salvar** da loja.
>
> **O cliente da mesa pode usar cupom ou cashback do Cardápio Digital?** Não. A sacola da mesa não tem cupom nem cashback: eles valem para a sacola da loja.
>
> **Onde cadastro o cartão fidelidade do Cardápio Digital?** Em **Novo cupom**, com o **Tipo** **Fidelidade**. Preencha **A cada quantos pedidos entregues** e o desconto. Depois do uso, a contagem do cliente recomeça.
>
> **Excluí um cupom do Cardápio Digital. O que acontece com os pedidos que já usaram?** Eles continuam com o desconto e o código.
>
> **O cupom de aniversário do Cardápio Digital vale para quem não tem a data cadastrada?** Não. O cupom vale perto do aniversário cadastrado no contato do cliente. Sem a data, a sacola avisa *"Este cupom é de aniversário, e a loja ainda não tem a sua data."*

> **[ERROS]**
>
> #### Erros Comuns
>
> **Código de cupom repetido:** a tela avisa *"Já existe um cupom com esse código."* **Solução:** escolha outro código ou edite o cupom que já existe.
>
> **Código de cupom fora do formato:** a tela avisa *"O código do cupom precisa ter de 3 a 30 letras, números, - ou _."* **Solução:** ajuste o tamanho e tire espaços e outros sinais.
>
> **Desconto acima de 100%:** a tela avisa *"Informe um desconto maior que zero (em %, até 100)."* **Solução:** ponha um valor de até 100 no **Desconto**.
>
> **Validade invertida:** a tela avisa *"Confira as datas do cupom: o início não pode passar do fim."* **Solução:** ponha em **Vale a partir de** uma data anterior à de **Vale até**.
>
> **Limite de cupons da loja:** a tela avisa *"A loja chegou ao limite de 200 cupons. Exclua os que não usa mais."* **Solução:** remova os cupons que não usa mais.
>
> **Cashback acima do permitido:** a tela avisa *"O cashback precisa ser um percentual de 0 a 50."* **Solução:** ponha um valor de até 50 em **Cashback em cada pedido (%)**.
