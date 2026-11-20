# Copilot da Raia

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/copilot-da-raia
- **Categoria:** Recursos
- **Menu:** CRM › Board de Oportunidades › Copilot da Raia

---

🧩 Lead que parou de responder, card esquecido na mesma etapa há dias: o **Copilot da raia** cuida disso sozinho. Cada etapa do Board pode ter regras que olham o relógio — há quanto tempo o lead não responde, há quanto tempo o card não se mexe — e, passado o prazo, marcam o card com uma etiqueta, tiram uma etiqueta ou deixam uma nota interna na conversa. Na etapa de ganho, a regra cria o projeto da venda.

Ideal para:

☑️ **Lead sem resposta:** marcar o card depois de algumas horas sem retorno do cliente, para a equipe priorizar.

☑️ **Card esquecido:** deixar uma nota na conversa quando a negociação ficou parada na etapa.

☑️ **Projeto da venda:** abrir o projeto da entrega a partir da venda que chegou à etapa de ganho.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **CRM  ›  Board** e escolha o funil.
>
> ➡️ No cabeçalho da etapa, clique no botão **Copilot da raia**.
>
> ➡️ Clique em **Nova regra** e preencha o prazo e o que fazer.
>
> ➡️ Deixe o **Modo ensaio** ligado nos primeiros dias e clique em **Salvar**.
>
> ➡️ Acompanhe pelo **Histórico** e, quando estiver confiante, desligue o ensaio.

## Os campos da regra

🔘 **Modo ensaio:** a regra decide tudo e registra o que faria, sem fazer nada. A regra nova já vem com ele ligado. Desligado, a tela avisa: *"Atenção: a regra vai agir de verdade nos cards desta raia."*

🔘 **Nome da regra:** como ela aparece na lista da etapa. Sem nome, a tela avisa *"Dê um nome à regra do Copilot."*

🔘 **Quando:** o que conta o prazo — **Lead sem responder**, **Card parado nesta raia**, **Card sem nenhum movimento** ou **Desde que o card foi criado**.

🔘 **Tempo** e **Unidade:** o prazo, em minutos, horas ou dias, a partir de 1. Logo abaixo, a tela mostra quantos cards a regra pegaria agora.

🔘 **O que fazer:** **Marcar o card com etiqueta**, **Tirar etiqueta do card** ou **Deixar comentário interno**. Com **Adicionar ação**, a mesma regra faz mais de uma coisa. Na etapa de ganho, a única ação é **Criar o projeto da venda**.

🔘 **Freios:** **Só dispara a partir de** e **Até** limitam o horário, no fuso da sua empresa — em branco, não há limite de horário. **Máximo por dia** limita quantas vezes a regra age no dia, e **Não dispara em feriado** pula os feriados.

🔘 **Regra ativa:** liga ou desliga a regra.

Como a própria tela avisa, a regra para sozinha quando o lead responde.

## Onde aparece o comentário interno

**Deixar comentário interno** escreve na conversa ligada à oportunidade, como uma mensagem de **Comunicação interna** que começa com *🤖 Copilot:*. O comentário não aparece na aba **Comentários** da oportunidade.

⚠️ Essa ação precisa de uma oportunidade ligada a uma conversa. Sem conversa, a simulação e o histórico avisam *O card não tem conversa*.

## A regra na etapa de ganho

Na etapa de ganho do funil, o **Copilot da raia** só cria o projeto da venda: o campo **Ação** oferece apenas **Criar o projeto da venda**.

🔘 **Modelo do projeto:** o modelo de onde o projeto nasce, com as etapas e as tarefas dele. Sem modelo, a tela avisa *"Escolha o modelo do projeto."*

🔘 **Ocultar o valor de quem executa:** o projeto nasce com o valor da venda escondido de quem trabalha nele, que vê o que foi vendido, mas não por quanto.

No **Histórico**, cada card em que a regra agiu mostra *Criou o projeto*, com o número do projeto criado.

A venda que já tem projeto não ganha outro: no **Histórico**, o card aparece com *A venda já tem o projeto*, com o nome e o número do projeto que ela já tem.

⚠️ Antes de desligar o **Modo ensaio** numa etapa de ganho, clique em **Simular agora**: a lista mostra cada card que a regra pegaria, com *Criaria o projeto*.

## Testar e acompanhar

As regras da etapa aparecem numa lista, com os selos **Ensaio**, **Ativa** ou **Pausada**.

🔘 **Simular agora:** mostra quantos cards seriam avaliados e o que a regra faria com eles, inclusive quando uma ação não vai funcionar. A simulação não grava nada.

🔘 **Histórico:** cada vez que a regra rodou, com **Quando**, **Card**, **Resultado** e **O que aconteceu**.

🔘 **Pausar regra:** o interruptor ao lado da regra pausa e retoma a regra sem apagá-la.

🔘 **Editar** e **Excluir:** ao excluir, o histórico da regra vai junto.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A regra vale para cards que já estavam na etapa?** Sim. Ela olha os cards que estão na etapa quando o prazo é atingido, inclusive os que chegaram antes de a regra existir.
>
> **A regra não fez nada. Por quê?** Abra o **Histórico**: a coluna **O que aconteceu** traz o motivo — por exemplo, *Modo ensaio — nada foi feito*.
>
> **Na etapa de ganho, o Copilot da raia pode marcar o card com etiqueta?** Não. Na etapa de ganho, o campo **Ação** só oferece **Criar o projeto da venda**.
>
> **A venda já tinha projeto quando chegou à etapa de ganho. O Copilot da raia cria outro?** Não. O **Histórico** mostra *A venda já tem o projeto*, e a venda fica só com o projeto que já tinha.
>
> **Simular agora conta como uma rodada da regra?** Não. Como a tela diz, a simulação *"não gasta a passagem do card na raia"*.

> **[ERROS]**
>
> #### Erros Comuns
>
> **O card não tem conversa:** a regra usa **Deixar comentário interno** numa oportunidade sem conversa ligada. **Solução:** use essa ação em etapas onde as oportunidades nascem de conversas, ou troque por uma ação de etiqueta.
