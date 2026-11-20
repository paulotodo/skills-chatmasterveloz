# Ticket x Protocolo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/ticket-x-protocolo
- **Categoria:** Recursos
- **Menu:** Chats / Tickets › Ticket x Protocolo

---

🧩 O **ticket** é a conversa de um **contato** com uma **conexão** da sua empresa. O **protocolo** é cada ciclo de abertura e fechamento dentro desse ticket.

Se o ticket é a conversa, os protocolos são os **capítulos** dela.

☑️ **Histórico unificado:** todo o relacionamento com o contato em uma conexão fica em um único ticket.

☑️ **Identidade preservada:** o número do ticket é estável, o que facilita referência interna ("o ticket 18069 do João") mesmo após várias reaberturas.

☑️ **Métricas precisas por atendimento:** cada protocolo é um atendimento numerado, então você sabe quantas vezes precisou reiniciar a conversa.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Um ticket por par **contato + conexão**➡️ Vários protocolos por ticket.➡️ Avaliações e tags de encerramento ficam atrelados ao protocolo. ### 📘 Como funciona a relação Ticket x Protocolo
>
> **Quando o ticket nasce:** na primeira mensagem do contato por uma conexão, o sistema cria um **ticket** com número único e abre o seu **primeiro protocolo**.
>
> **Quando um protocolo fecha:** ao encerrar o atendimento, o **protocolo é fechado**, o ticket tem seu status alterado para "Fechado" mas continua existindo. Ele **nunca expira**.
>
> **Quando um novo protocolo nasce:** quando o contato envia uma nova mensagem **após o ticket fechado**, o ticket é reaberto (status "Aguardando") e um **novo protocolo** é criado dentro dele.
>
> **⚠️ O número do ticket não muda.**
>
> **⚠️ Um protocolo aberto por vez.** Em um mesmo ticket só existe **um protocolo aberto** simultaneamente. Para abrir um novo, é preciso encerrar o atual.
>
> **Quando vira outro ticket:** se o mesmo contato falar com sua empresa por **outra conexão** (ex.: antes WhatsApp Vendas, agora Instagram), aí sim um **novo ticket** é criado, com número diferente. Cada par contato + conexão tem seu próprio ticket.

## **Número do Ticket e do Protocolo**

No chat, ao lado do nome do contato, aparecem os dois identificadores:  
- **Número do ticket**, entre parênteses. Exemplo: `(18069)`.
- **Número do protocolo**, precedido de `#`. Exemplo: `#24954`.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual a diferença entre ticket e protocolo?** O ticket é a conversa do contato com a conexão; o protocolo é cada ciclo de abertura e fechamento dessa conversa. Um ticket tem N protocolos ao longo do tempo.
>
> **Por que o número do ticket não muda quando reabro a conversa?** Porque o ticket representa a relação contato + conexão. Reabrir não cria uma nova relação — só um novo protocolo dentro dela.
>
> **Se o mesmo cliente me chama por outra conexão, vira o mesmo ticket?** Não. Cada conexão tem seu próprio ticket com aquele contato. Mesmo cliente em duas conexões = dois tickets distintos.
>
> **Como conto "atendimentos" para métrica?** Conte **protocolos**, não tickets. Cada protocolo é um atendimento real (uma vez que abriu e fechou). Tickets contam relações distintas, não atendimentos.
>
> **Posso ter vários protocolos abertos ao mesmo tempo no mesmo ticket?** Não. Em um ticket só existe **um protocolo aberto por vez**. Ao encerrar o atual, ele fecha; quando o contato voltar a falar, um novo protocolo nasce.
>
> **Avaliação e tag de encerramento ficam no ticket ou no protocolo?** No **protocolo**. Cada protocolo tem sua própria avaliação e suas próprias tags de encerramento — porque cada um é um atendimento independente.
>
> **Um ticket fechado pode "expirar" e sumir?** Não. O ticket **nunca expira**. Mesmo que fique meses sem atividade, ao receber uma nova mensagem do contato pela mesma conexão, ele reabre com o mesmo número.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Chamar protocolo de ticket (e vice-versa):** dizer "abri um novo ticket" quando na verdade reabriu uma conversa antiga (o que gera apenas um novo protocolo). Isso bagunça relatórios e conversas internas. *Forma correta:* ticket = a conversa contato + conexão; protocolo = cada atendimento dentro dela.
>
> **Esperar número novo a cada reabertura:** alguns usuários reabrem o atendimento e procuram pelo "novo número do ticket". Esse número **não muda**. O que muda é o número do protocolo (`#24954`). *Forma correta:* se quer identificar o atendimento específico, use o número do protocolo, não o do ticket.
