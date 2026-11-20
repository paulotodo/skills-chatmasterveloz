# Mensagem Template

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/mensagem-template
- **Categoria:** Recursos
- **Menu:** Conexões › WhatsApp › Mensagem Template

---

🧩 A **mensagem template** é um modelo de texto que a Meta aprova antes de você usar. É o único formato de mensagem permitido quando a janela de atendimento está fechada.

Diferente do WhatsApp comum, onde você escreve o que quiser, na API Oficial as mensagens ativas precisam ser **pré-aprovadas** pelo Facebook para garantir que não sejam spam ou golpe.

Ideal para:

☑️ **Primeiro contato:** Alcançar uma lista de interessados que ainda não escreveu para a empresa.

☑️ **Retomada:** Chamar de volta o cliente que parou de responder e cuja janela já fechou.

☑️ **Avisos automáticos:** Confirmação de pedido, aviso de entrega, lembrete de vencimento.

## O que cabe dentro de um modelo

✔️ **Texto e mídia** — a mensagem pode levar imagem, documento ou vídeo junto.

✔️ **Variáveis** — os espaços escritos como `{{1}}`, `{{2}}` são preenchidos na hora do envio com os dados daquele cliente, como o nome ou o número do pedido.

✔️ **Botões** — links, respostas rápidas e outros elementos que o cliente toca em vez de digitar.

## As quatro categorias

A Meta divide as conversas em 4 categorias, com preços diferentes:

🟢 **Serviço** — a conversa que o **cliente** começa, quando ele escreve para tirar uma dúvida. Não é um modelo: é o atendimento comum dentro da janela.

🔵 **Utilidade** — a empresa avisa sobre algo que o cliente já espera, porque ele fez alguma coisa antes: pedido confirmado, entrega a caminho, fatura a vencer. É a categoria mais barata das que a empresa inicia.

🟡 **Marketing** — a empresa quer despertar interesse: promoção, novidade, carrinho abandonado, felicitação. É a mais cara.

🔴 **Autenticação** — o código de verificação para entrar em algum lugar. Barata e extremamente restrita: não aceita nada além do código.

## A diferença que custa dinheiro

Duas mensagens quase idênticas podem custar preços bem diferentes, e o que decide é a **categoria** do modelo. Entender a diferença entre **Utilidade** e **Marketing** não serve só para o modelo ser aprovado: serve para a conta no fim do mês não surpreender.

A diferença, para a Meta, é de intenção. **Utilidade** é informar algo que o cliente já espera, porque ele fez alguma coisa antes. **Marketing** é chamar a atenção dele para algo que você quer mostrar.

## 📦 Utilidade

É a categoria do **serviço e da transação**. São mensagens que confirmam, alteram ou suspendem algo que o cliente já pediu.

A pergunta que resolve: **o cliente está esperando isto porque fez alguma coisa antes?** Se a resposta é sim, é Utilidade.

Serve para envio de fatura e boleto, atualização de status de pedido, confirmação de agendamento, aviso de problema na conta.

💲 Custa **menos** que a conversa de Marketing.

## 📢 Marketing

É a categoria da **venda, da promoção e do relacionamento**. São mensagens que despertam interesse, oferecem algo novo ou simplesmente mantêm a marca por perto.

A pergunta que resolve: **o cliente pediu isto agora, ou sou eu que quero mostrar?** Se é você querendo mostrar, é Marketing.

Serve para oferta e cupom, lançamento de produto, recuperação de carrinho abandonado, felicitação de aniversário, convite para evento.

💲 É a categoria **mais cara**.

## O que separa uma da outra

🔘 **Objetivo:** Utilidade informa sobre algo já combinado. Marketing convence ou vende algo novo.

🔘 **Custo:** Utilidade é a faixa intermediária. Marketing é a faixa mais alta.

🔘 **Flexibilidade do texto:** Utilidade é rígida, e a Meta recusa se houver propaganda dentro. Marketing aceita linguagem vendedora à vontade.

## ⚠️ A armadilha da mensagem misturada

Muita gente tenta economizar embutindo uma oferta numa mensagem de serviço. A Meta detecta, e a regra é dura: **se o modelo for quase todo de Utilidade mas tiver uma única frase de Marketing, ele inteiro vira Marketing.**

O exemplo clássico:

> Olá João, sua fatura de julho está fechada. Aproveite e veja nossas ofertas com desconto.

A primeira frase é Utilidade. A segunda contamina tudo, e você paga preço de Marketing para enviar uma fatura.

📌 Se o objetivo é economizar, mande a fatura seca. A oferta vai noutra mensagem, noutro momento.

## 📝 Modelos de Utilidade para copiar

**Confirmação de agendamento**

```
Olá, {{1}}! Confirmamos sua consulta para o dia {{2}} às {{3}}. Para reagendar, responda a esta mensagem.
```

**Confirmação de pedido**

```
Olá {{1}}, seu pedido #{{2}} foi confirmado e já está sendo separado. Avisaremos quando sair para entrega.
```

**Envio de código de pagamento**

```
Segue o código para pagamento do seu pedido {{1}}. O código expira em 30 minutos: {{2}}
```

**Aviso de vencimento**

```
Oi {{1}}, sua mensalidade vence hoje. Segue o link para pagamento: {{2}}
```

## 📝 Modelos de Marketing para copiar

**Promoção**

```
Olá {{1}}! Aproveite 20% de desconto em toda a loja usando o cupom {{2}}. Clique abaixo!
```

**Reativação**

```
Oi {{1}}, faz tempo que não nos falamos! Selecionamos uma oferta especial para você voltar: {{2}}
```

**Carrinho abandonado**

```
Olá {{1}}, seus produtos ainda estão no carrinho. Finalize agora e garanta 5% de desconto.
```

**Aniversário**

```
Parabéns, {{1}}! Hoje é o seu dia e o presente é nosso. Venha até a loja e ganhe um brinde.
```

## Um caso que mora nas duas

O modelo que pede **permissão para ligar** ao cliente, com o botão de escolher preferências do próprio WhatsApp, pode ser criado também como **Utilidade**. É a exceção que confirma a lógica: pedir autorização é serviço, não propaganda.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preciso de um modelo para responder meu cliente?** Não, se ele escreveu nas últimas vinte e quatro horas. Dentro da janela você responde livremente. O modelo é para falar primeiro ou para voltar depois que a janela fechou.
>
> **Quanto tempo a Meta leva para aprovar um modelo?** Costuma ser rápido, em geral algumas horas, mas pode ser dias. A análise é dela, e a plataforma só mostra o resultado.
>
> **Posso mudar um modelo já aprovado?** Pode, mas ao editar ele volta para análise e para de funcionar até ser aprovado de novo.
>
> **Onde crio e acompanho meus modelos?** No menu **Conexões**, no card da Conexão de API Oficial, pelo botão de gestão de templates.
>
> **Quantas variáveis posso usar?** Quantas o texto pedir, numeradas em sequência. Cada uma precisa receber um valor no momento do envio, senão a Meta recusa a mensagem.
>
> **A Meta classificou meu modelo na categoria errada. Dá para mudar?** Dá para contestar logo depois de criar. Se a Meta negar, o modelo fica naquela categoria para sempre, e a saída é apagar e criar outro com texto diferente.
>
> **Uma mensagem de bom dia é o quê?** Marketing, quase sempre. Texto vago e de relacionamento é visto como engajamento, e engajamento é Marketing.
>
> **Código de verificação entra em qual das duas?** Em nenhuma. É uma terceira categoria, Autenticação, a mais barata e a mais restrita: não aceita nada além do código.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Enviar um modelo com variável vazia:** a Meta recusa e a mensagem não chega, com um erro sobre parâmetro faltando. **Solução:** confira se a integração ou a campanha está preenchendo todas as variáveis do modelo.
>
> **Criar só um modelo de boas-vindas e achar que está pronto:** com a janela fechada e um único modelo, a equipe não tem como tratar os casos reais. **Solução:** monte um modelo por situação recorrente da operação antes de migrar o número.
>
> **Pendurar uma oferta no fim de um aviso de serviço:** a mensagem inteira muda de categoria e o custo sobe. **Solução:** separe em dois envios, ou abra mão da oferta naquele modelo.
>
> **Escrever modelo de Utilidade com linguagem vendedora:** a Meta recusa na análise, e o modelo volta sem aprovação. **Solução:** no modelo de Utilidade, informe e pare. Sem adjetivo, sem chamada para ação de venda.
