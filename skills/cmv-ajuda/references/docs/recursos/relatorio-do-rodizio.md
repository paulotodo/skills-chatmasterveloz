# Relatório do Rodízio

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/relatorio-do-rodizio
- **Categoria:** Recursos
- **Menu:** Rodízios › Relatório do Rodízio

---

🧩 O rodízio do seu fluxo está dividindo os atendimentos do jeito que você planejou? O **Relatório do Rodízio** mostra como o bloco **Rodízio** do FlowBuilder Nativo distribuiu os atendimentos entre os operadores, comparando o que cada um recebeu com a meta definida no nó.

O **Relatório do Rodízio** também mostra quantos clientes chegaram num momento sem operador disponível, e para onde eles foram.

Ideal para:

☑️ **Conferência de metas:** compara a participação de cada operador com a porcentagem configurada no nó de rodízio.

☑️ **Furos de escala:** aponta os atendimentos que chegaram sem operador na hora.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Atendimento** e, na seção **Distribuição e rodízio**, escolha **Sim** em **Exibir o Relatório do Rodízio (botão Ver relatório, na tela Rodízios)?**
>
> ➡️ Acesse o menu **Rodízios** e clique em **Ver relatório**, no topo da tela.
>
> ➡️ Escolha o período em **De** e **Até**, filtre pelo **Nó de rodízio** se quiser e clique em **Atualizar**.

## Como ligar o relatório

O **Relatório do Rodízio** fica escondido até um administrador ligar. Acesse o menu **Configurações  ›  Opções  ›  Atendimento** e, na seção **Distribuição e rodízio**, em **Exibir o Relatório do Rodízio (botão Ver relatório, na tela Rodízios)?**, escolha **Sim**. A tela do menu **Rodízios** ganha o botão **Ver relatório** no topo, que abre a **Distribuição do rodízio**.

Com a opção em **Não**, o botão **Ver relatório** some da tela do menu **Rodízios**.

📌 O relatório é visível apenas para administradores e supervisores.

## O que o relatório mostra

🔘 **De** e **Até:** o período. Ele filtra **quando o rodízio entregou** o atendimento ao operador.

🔘 **Nó de rodízio:** um nó específico ou **Todos os nós**.

🔘 **Atualizar** e **Baixar CSV:** recarregam os números e baixam a tabela.

No topo ficam quatro números: **Atendimentos distribuídos**, **Sem operador na hora**, **Operadores que receberam** e **Nós de rodízio com movimento**.

Para cada nó de rodízio, uma tabela traz **Operador**, **Atendimentos**, **Participação**, **Meta**, **Diferença** e **No nó**, e um gráfico compara **Realizado (%)** com **Meta (%)**. Quando houve atendimento sem operador disponível, o nó mostra **Sem operador na hora** e para qual setor esses atendimentos foram. Quem saiu do nó continua na lista, com **Não está mais no nó**.

⚠️ A meta usada é a que está configurada no nó do fluxo **hoje**. Se ela mudou no meio do período, a comparação só vale a partir da mudança.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Não encontro o Relatório do Rodízio no menu.** O relatório não tem item próprio no menu: ele abre pelo botão **Ver relatório**, no topo da tela do menu **Rodízios**. O botão fica escondido até um administrador escolher **Sim** em **Exibir o Relatório do Rodízio (botão Ver relatório, na tela Rodízios)?**, no menu **Configurações  ›  Opções  ›  Atendimento**, seção **Distribuição e rodízio**. Atendentes não veem o menu **Rodízios**.
>
> **O Relatório do Rodízio está vazio.** A mensagem *"Nenhum atendimento distribuído pelo rodízio no período."* aparece quando nenhum atendimento passou por um nó de rodízio nas datas escolhidas. Amplie o período em **De** e **Até**, ou confira se o fluxo usa o bloco **Rodízio**.
>
> **O período do Relatório do Rodízio conta pelo quê?** Pelo momento em que o rodízio entregou o atendimento ao operador.
>
> **Por que a comparação com a meta parece errada num período antigo?** O relatório usa a meta que está no nó hoje. Se a porcentagem foi alterada depois, os dias anteriores à mudança são comparados com a meta nova.
