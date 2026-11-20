# Encerrar por Inatividade (Atendendo)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/encerrar-por-inatividade
- **Categoria:** Recursos
- **Menu:** Atendimento Otimizado › Encerrar por Inatividade (Atendendo)

---

🧩 **O Encerramento por Inatividade** fecha automaticamente os tickets que já estão abertos (na aba "**Atendendo**") caso **o cliente pare de responder após um tempo** limite definido por você.

☑️ **Organização do Atendimento:** Evita que a tela do atendente fique poluída com dezenas de conversas "fantasmas", mantendo o foco apenas nos clientes que estão online e engajados.

☑️ **Métricas Reais:** Impede que o "Tempo Médio de Atendimento (TMA)" dos seus relatórios seja distorcido por tickets que ficaram abertos e esquecidos de um dia para o outro.

☑️ **Padronização:** Garante que todos os clientes que sumirem recebam um aviso educado de que o chamado foi encerrado por falta de comunicação.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Em Conexões Editar Filas & Tempos configure os campos de **Inatividade** para ativar essa função.
>
> ➡️ Configure o texto de aviso no campo **Mensagem de Encerramento após Inatividade**.

## Como configurar o Encerramento por Inatividade

No menu → Conexões > Editar > Filas & Tempos

🔘 **Inatividade:** Selecione o tempo que o sistema vai tolerar o silêncio de um cliente que já pertence a um Atendimento em um departamento.

🔘 **Inatividade Sem Fila:** Selecione o tempo de tolerância para clientes que estão em Atendimento sem um departamento definido.

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/24766-encerramento-inatividade.jpg)

## Como configurar uma Mensagem para Encerramento por Inatividade

No menu → Conexões > Editar > Mensagens

🔘 **Mensagem por Inatividade:** Digite a frase que o cliente receberá no momento em que o cronômetro zerar e o ticket for fechado.  
- *Sugestão:* "Como não tivemos mais retorno da sua parte, estamos encerrando este atendimento. Mas não se preocupe! Qualquer dúvida, é só nos chamar novamente por aqui."

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **E se a última mensagem do chat tiver sido enviada pelo cliente? O sistema encerra?** NÃO! Essa é a regra de segurança mais importante. Se o cliente mandou a última mensagem, o sistema entende que é o atendente que deve responder, portanto, a conversa **não será encerrada** automaticamente. O cronômetro da inatividade só começa a girar depois que o atendente envia uma resposta e fica aguardando o cliente.
>
> **Qual a diferença entre o "Mover Após" e a "Inatividade"?** O "Mover Após" atua na coluna "Aguardando" (quando o cliente está na fila, antes de falar com um humano). O "Encerrar por Inatividade" atua na coluna "Atendendo" (quando o atendente já assumiu a conversa).

> **[ERROS]**
>
> #### Erros Comuns
>
> **Definir um tempo muito curto:** Colocar apenas 5 ou 10 minutos de inatividade. O cliente vai pegar um café, responder uma mensagem do chefe e, quando voltar ao WhatsApp, o ticket foi encerrado. O ideal é dar um tempo razoável de respiro (como 60 minutos, 120 minutos ou até 24h, dependendo da urgência do seu negócio).
>
> **Deixar a mensagem de inatividade em branco:** O usuário preenche os minutos, mas não escreve nada no campo da mensagem de encerramento. Resultado: o ticket simplesmente some da tela e a conversa é encerrada "do nada" no WhatsApp do cliente, sem nenhuma explicação, gerando frustração.
