# Qual Webhook Usar

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/qual-webhook-usar
- **Categoria:** APIs
- **Menu:** Webhooks › Qual Webhook Usar

---

🧩 Você já decidiu que quer avisar o seu sistema quando algo acontecer por aqui. Falta escolher **qual** webhook ligar.

Para o atendimento dos clientes são três saídas, e o que separa uma da outra é o **alcance**.

➡️ **Pela Conexão** — avisa tudo o que acontece naquela Conexão: mensagem recebida, mensagem enviada, tag alterada no Ticket e Ticket aberto ou encerrado. É o mais amplo, e a escolha natural de quem quer espelhar a conversa inteira em outro sistema.

➡️ **Pelo Setor** — avisa os mesmos quatro eventos, mas só dos Tickets que estão naquele Setor. É de quem se interessa por uma parte do atendimento: a triagem, o time de vendas, o financeiro.

➡️ **Por evento** — cobre mensagem interna, alteração de tag, mudança de status do usuário e movimentação no CRM. Três desses só existem aqui: **mensagem interna**, **status do usuário** e **CRM**. Se é um deles que você precisa, não adianta ligar os outros dois.

⚠️ **Conexão e Setor ligados ao mesmo tempo disparam os dois.** A regra é: quando o Ticket **não** está no Setor escolhido, chega só o aviso da Conexão; quando está, chegam os dois. Se o seu sistema está processando a mesma mensagem duas vezes, é quase sempre isto.

## A conversa da equipe

➡️ **Pelas conversas internas da equipe** — um webhook à parte avisa o que acontece nas conversas entre colegas: mensagens novas e apagadas, reações, conversas criadas, alteradas ou apagadas, e as chamadas da equipe com as gravações. Ele não vê nada do atendimento dos clientes, e por isso não se sobrepõe à Conexão nem ao Setor.

## O sentido contrário

O **Webhook Trigger** não avisa ninguém — ele é um endereço nosso que o **seu** sistema chama. Um pagamento aprovado, um lead cadastrado no site: a chamada chega aqui e inicia um fluxo de conversa.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preciso escolher um só?** Não. Os três podem ficar ligados ao mesmo tempo, cada um apontando para um endereço diferente do seu sistema. O cuidado é com Conexão e Setor, que se sobrepõem.
