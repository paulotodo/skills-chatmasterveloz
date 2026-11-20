# Erros de Entrega do WhatsApp Oficial

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/erros-de-entrega-do-whatsapp-oficial
- **Categoria:** Recursos
- **Menu:** Conexões › WhatsApp › Erros de Entrega do WhatsApp Oficial

---

🧩 Quando a Meta não entrega uma mensagem do WhatsApp Oficial, ela devolve um **código de erro** com o motivo. O código diz se o problema está na janela de atendimento, no cliente, no template, no pagamento ou na conta, e cada um pede uma ação diferente.

No card da conexão oficial, o botão **Erros de template** lista os templates que a Meta recusou no envio, com o código e a mensagem da Meta. Este artigo traduz os códigos mais comuns.

Ideal para:

☑️ **Mensagem que não chegou:** descobrir pelo código se é para corrigir, esperar ou falar com o cliente por outro canal.

☑️ **Template que falha no envio:** achar a diferença entre o que foi enviado e o que está aprovado.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões** e, no card da conexão oficial, clique em **Erros de template**.
>
> ➡️ Ache o código do erro na lista abaixo.
>
> ➡️ Faça o que a linha do código indica.

## Janela de atendimento e cliente

🔘 **131047 · Janela de atendimento fechada:** passaram mais de 24 horas desde a última mensagem do cliente. **O que fazer:** envie um template aprovado.

🔘 **131049 · Mensagem segurada pela Meta:** em geral é o limite de marketing por cliente, que a Meta ajusta para cada pessoa conforme o quanto ela lê. **O que fazer:** espere pelo menos 24 horas para reenviar a essa pessoa. Insistir dentro das 24 horas bloqueia novas tentativas a ela.

🔘 **131050 · Cliente pediu para não receber marketing:** o cliente parou de aceitar marketing da sua empresa. **O que fazer:** não reenvie.

🔘 **130472 · Cliente no experimento da Meta:** uma pequena parte dos usuários do WhatsApp não recebe marketing de nenhuma empresa, e não há cobrança. **O que fazer:** peça, por outro canal, que o cliente envie uma mensagem, e responda dentro da janela.

🔘 **131026 · Não deu para entregar:** o número pode não ter WhatsApp, o cliente pode não ter aceitado os termos novos do WhatsApp, ou o aplicativo dele está desatualizado. **O que fazer:** por outro canal, peça que o cliente confirme que consegue enviar mensagem ao seu número e atualize o aplicativo.

## Template

🔘 **132000 · Quantidade de variáveis errada:** o envio trouxe menos ou mais valores do que as variáveis do template. **O que fazer:** preencha todas as variáveis.

🔘 **132001 · Template não encontrado:** o template não existe naquele idioma ou ainda não foi aprovado. **O que fazer:** confira a aprovação, o nome e o idioma.

🔘 **132012 · Variável no formato errado:** o valor enviado não segue o formato definido no template. **O que fazer:** ajuste o valor.

🔘 **132015 · Template pausado:** a qualidade caiu e a Meta pausou o template por algumas horas. **O que fazer:** espere a pausa acabar.

🔘 **132016 · Template desabilitado:** o template foi pausado vezes demais. **O que fazer:** crie um template novo, com outro texto.

🔘 **131064 · Envio limitado por categoria errada:** a Meta limitou os envios porque templates estavam na categoria errada. **O que fazer:** corrija a categoria dos templates. O limite cai sozinho no fim do período.

## Pagamento e conta

🔘 **131042 · Problema na forma de pagamento:** falta forma de pagamento na conta de mensagens, ou faltam a moeda e o fuso horário, entre outros motivos de cobrança. **O que fazer:** confira **Cobrança e pagamentos**, na Meta.

🔘 **131031 e 368 · Conta restrita ou desativada:** a Meta restringiu a conta por violação de política. **O que fazer:** veja a violação na **Página Inicial do Suporte para Empresas**, na Meta, e peça a revisão.

## Volume e ritmo

🔘 **131048 · Envio restrito por spam:** muitas mensagens anteriores foram bloqueadas ou denunciadas. **O que fazer:** confira a qualidade do número no **Gerenciador do WhatsApp** e reveja os templates e a lista de envio.

🔘 **131056 · Mensagens demais para o mesmo cliente:** o número enviou muitas mensagens à mesma pessoa em pouco tempo. **O que fazer:** espere um pouco. Para os outros clientes, o envio segue normal.

🔘 **130429 · Ritmo acima do permitido:** o número passou do máximo de mensagens por segundo. **O que fazer:** reduza o ritmo e tente de novo.

## Mídia

🔘 **131053 · Arquivo não carregado:** a Meta não conseguiu carregar o arquivo enviado, por exemplo por um tipo que ela não aceita. **O que fazer:** confira o formato do arquivo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O template foi aprovado e o envio falha. Por quê?** Quase sempre o envio não bate com o template aprovado: falta uma variável (132000), o idioma é outro (132001) ou o formato do valor está errado (132012). O código em **Erros de template** diz qual.
>
> **Mensagem que a Meta não entregou é cobrada?** A cobrança é por mensagem entregue. No experimento de marketing (130472) e no template pausado (132015), a Meta diz expressamente que não cobra.
>
> **O erro 131049 aparece só para alguns clientes. É bloqueio do meu número?** Não. É o limite de marketing de cada cliente, que a Meta ajusta pessoa a pessoa. Os outros clientes continuam recebendo.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Reenviar logo depois do 131049:** a tentativa repetida bloqueia novos envios àquele cliente por até 24 horas. **Solução:** espere 24 horas antes de tentar de novo.
>
> **Responder fora da janela sem template:** a Meta devolve o 131047. **Solução:** fora das 24 horas, o primeiro envio é sempre um template aprovado.
