# Biblioteca de modelos de mensagem para o Chat Master Veloz

Modelos prontos por objetivo, para adaptar ao negócio do usuário. Não entregue como estão: troque o tom, o vocabulário e os dados pelos do negócio, e confira as regras do tipo de mensagem em `references/regras-por-tipo-de-mensagem.md`.

## Sumário

- [Convenções](#convenções)
- [1. Saudação](#1-saudação)
- [2. Ausência e fora de expediente](#2-ausência-e-fora-de-expediente)
- [3. Cobrança](#3-cobrança)
- [4. Confirmação de agendamento](#4-confirmação-de-agendamento)
- [5. Lembrete](#5-lembrete)
- [6. Pós-venda](#6-pós-venda)
- [7. Pesquisa](#7-pesquisa)
- [8. Reativação](#8-reativação)
- [9. Aniversário](#9-aniversário)
- [10. Carrinho abandonado](#10-carrinho-abandonado)
- [Extra: encerramento](#extra-encerramento)

## Convenções

- `[texto entre colchetes]` é para o usuário trocar à mão **antes de cadastrar**. Não é variável. Não deixe colchete sobrando numa resposta rápida de texto: no campo **Mensagem**, o atalho entre colchetes é o código das respostas rápidas de mídia e de fluxo.
- **Resposta rápida:** as variáveis usadas são da lista oficial do artigo Mustaches (`references/docs/recursos/mustaches.md`): `{{firstName}}` primeiro nome do contato, `{{ms}}` saudação conforme a hora, `{{user}}` nome do atendente do ticket, `{{protocol}}` protocolo. O artigo da resposta rápida de texto confirma que há variáveis e dá o primeiro nome como exemplo, sem listar os códigos: recomende testar cada resposta uma vez com o próprio número.
- **Mensagem de saudação do Setor:** `{{name}}`, confirmada no artigo do campo.
- **Template da API Oficial:** `{{1}}`, `{{2}}`… em sequência. Cada modelo traz o que cada número significa e em qual campo extra da lista de campanha ele vai (o **extra2** é a `{{1}}`). Para campanha, no máximo cinco variáveis no corpo.
- **Aviso automático de agenda** (Links de agendamento, Consultório, Reservas): cada módulo tem a sua lista de variáveis, na seção 12 de `references/regras-por-tipo-de-mensagem.md`. As de um módulo não valem no outro, nem em resposta rápida, campanha ou template.
- **Campos sem variável documentada** (mensagem simples de campanha, agendamento, mensagem de aniversário, fora de expediente, ausência, conclusão): os modelos vêm sem variável.
- **Nome do template:** os nomes são sugestões. As regras de formato do nome não estão documentadas; ajuste ao que a tela aceitar.
- **Categoria do template:** é indicada a categoria coerente com o artigo Mensagem Template. Quem decide é a Meta, na análise.
- **Sem emojis** nos modelos. Se a marca usa, acrescente no máximo um, e nunca em cobrança.
- Em template de Marketing e em campanha, o modelo já traz a opção de saída ("responda PARAR"). Combine com o usuário o que a equipe faz quando alguém responde PARAR: o tratamento automático dessa resposta não está documentado.

---

## 1. Saudação

### Resposta rápida (texto)

Atalho: `/saudacao`

```
{{ms}}, {{firstName}}! Aqui é {{user}}, da [Nome da Empresa]. Como posso te ajudar hoje?
```

Atalho: `/saudacao protocolo`

```
{{ms}}, {{firstName}}! Aqui é {{user}}, da [Nome da Empresa]. Seu protocolo de atendimento é {{protocol}}. Me conta em que posso ajudar?
```

### Mensagem de saudação do Setor

Onde: **Setores & Chatbot** › editar o Setor › aba **Mensagens** › campo **Mensagem de saudação**.

```
Olá, {{name}}! Você está no [Suporte] da [Nome da Empresa]. Já vamos te atender. Nosso horário é de segunda a sexta, das 8h às 18h.
```

Duas ou três linhas, com o horário real. Se a Conexão também tem saudação preenchida, o cliente recebe as duas: preencha uma ou outra.

### Mensagem de saudação da Conexão, quando ela abre o menu de Setores

Onde: **Conexões** › editar a Conexão › aba **Mensagens**. O sistema acrescenta sozinho as opções numeradas (uma linha por Setor), então o texto termina chamando a escolha.

```
Olá! Você está falando com a [Nome da Empresa]. Para agilizar, responda com o número do assunto:
```

### Template

Não recomendado. Saudação sem motivo concreto é texto de relacionamento, e o artigo Mensagem Template diz que mensagem vaga ("bom dia") é Marketing quase sempre. Para iniciar conversa com a janela fechada, use o template do objetivo real (lembrete, cobrança, reativação).

---

## 2. Ausência e fora de expediente

### Mensagem de Ausência do atendente

Onde: ícone de pessoa no canto superior direito › **Perfil** › campo **Mensagem de Ausência**. Vale enquanto o status estiver **Ausente** e é enviada a cada mensagem do cliente: lembre o usuário de voltar o status ao retornar.

```
Olá! Estou fora do computador agora e volto às [14h]. Pode deixar sua mensagem aqui que eu respondo assim que voltar. Se for urgente, fale com [canal alternativo].
```

### Mensagem de fora de expediente do Setor

Onde: **Setores & Chatbot** › editar o Setor › aba **Mensagens** › campo **Mensagem de fora de expediente** (só aparece com o expediente por Setor ligado).

Pergunte como está a opção **Abrir Atendimentos Fora do Expediente?** em **Configurações › Opções › Geral**, porque ela muda o que se pode prometer.

Se está em **Sim** (a conversa entra no Setor e espera a equipe):

```
Olá! Nosso atendimento no [Suporte] funciona de [segunda a sexta, das 8h às 18h]. Sua mensagem ficou registrada e vamos responder no próximo horário de atendimento.
```

Se está em **Não** (o atendimento é encerrado em seguida):

```
Olá! No momento estamos fechados. Nosso atendimento no [Suporte] funciona de [segunda a sexta, das 8h às 18h]. Por favor, escreva de novo dentro desse horário para falar com a equipe.
```

### Resposta rápida (texto): pausa no meio do atendimento

Atalho: `/volto`

```
{{firstName}}, preciso conferir isso com [o setor responsável] e volto a falar com você até [hora ou dia]. Combinado?
```

### Template

Não se aplica: são respostas a quem acabou de escrever, com a janela aberta.

---

## 3. Cobrança

### Resposta rápida (texto)

Atalho: `/cobranca`

```
{{ms}}, {{firstName}}. Aqui é {{user}}, do financeiro da [Nome da Empresa].

Consta em aberto a fatura de [referência], no valor de R$ [valor], com vencimento em [data].

Link para pagamento: [link completo]

Se já pagou, pode desconsiderar e me enviar o comprovante por aqui.
```

Atalho: `/cobranca acordo`

```
{{firstName}}, a fatura de [referência] continua em aberto e quero te ajudar a resolver. Prefere pagar hoje pelo link ([link completo]) ou combinar uma nova data?
```

### Template (API Oficial) — aviso de vencimento

- Nome sugerido: `aviso_vencimento`
- Categoria: Utilidade (o cliente contratou e espera a fatura)
- Uso: campanha pela API Oficial, com os valores de cada cliente nos campos extras da lista. Não use em agendamento: o preenchimento de variáveis de template em agendamento não está documentado.

```
Olá, {{1}}. Sua fatura de {{2}}, no valor de {{3}}, vence em {{4}}. Link para pagamento: {{5}}
```

| Variável | Significado | Exemplo | Campo na lista de campanha |
|---|---|---|---|
| `{{1}}` | Nome | Ana | extra2 |
| `{{2}}` | Referência | novembro | extra3 |
| `{{3}}` | Valor | R$ 189,90 | extra4 |
| `{{4}}` | Vencimento | 25/11 | extra5 |
| `{{5}}` | Link de pagamento | endereço completo, sem encurtador | extra6 |

### Template (API Oficial) — fatura em aberto

- Nome sugerido: `fatura_em_aberto`
- Categoria: Utilidade
- Uso: campanha pela API Oficial (mesma observação do modelo anterior).

```
Olá, {{1}}. Não identificamos o pagamento da fatura de {{2}}, vencida em {{3}}. Link para pagamento: {{4}}. Se já pagou, desconsidere esta mensagem.
```

`{{1}}` nome (extra2), `{{2}}` referência (extra3), `{{3}}` data do vencimento (extra4), `{{4}}` link completo (extra5).

### Template sem variável, para agendamento recorrente

Como o preenchimento de variáveis de template em agendamento não está documentado, o caminho seguro para a cobrança recorrente (**Repetir a cada** › **Todo dia...**) é um template de texto fixo.

- Nome sugerido: `lembrete_mensalidade`
- Categoria: Utilidade

```
Olá! Sua mensalidade da [Nome da Empresa] vence nesta semana. Para receber o boleto ou tirar dúvidas, responda a esta mensagem.
```

O nome da empresa é escrito fixo no texto antes de enviar para aprovação. O agendamento é feito contato a contato; se valor ou link mudam por cliente, use um dos modelos com variável acima numa campanha pela API Oficial (repetição automática de campanha não está documentada: é uma campanha a cada mês).

**Cuidados:** nada de oferta, adjetivo ou "aproveite" em template de cobrança: uma frase de Marketing muda a categoria do modelo inteiro. Sem ameaça e sem urgência artificial.

---

## 4. Confirmação de agendamento

### Resposta rápida (texto)

Atalho: `/confirmar`

```
{{firstName}}, confirmando seu horário:

[serviço] com [profissional]
[dia da semana], [data], às [hora]
[endereço]

Posso confirmar? Responda SIM ou me diga outro horário.
```

### Resposta rápida (localização), para enviar junto

Atalho: `/localizacao`. Troque o texto, a latitude e a longitude pelos do endereço (a latitude e a longitude saem da URL do local no Google Maps).

```
<endereco> [Nome da Empresa] - [endereço] </endereco> <mapa> degreesLatitude: [latitude], degreesLongitude: [longitude],18z </mapa>
```

### Template (API Oficial)

- Nome sugerido: `confirmacao_agendamento`
- Categoria: Utilidade
- Texto do próprio artigo Mensagem Template:

```
Olá, {{1}}! Confirmamos sua consulta para o dia {{2}} às {{3}}. Para reagendar, responda a esta mensagem.
```

`{{1}}` nome (extra2), `{{2}}` data (extra3), `{{3}}` hora (extra4). Troque "consulta" pela palavra do negócio (visita, aula, horário) antes de enviar para aprovação.

### Aviso automático das Reservas (aviso **Reserva confirmada**)

Onde: menu **Reservas** › aba **Avisos**. Só variáveis da lista do artigo Aba Avisos em Reservas; não servem em outro módulo.

```
Olá, {{cliente}}! Sua reserva está confirmada.

{{servico}}
{{diaDaSemana}}, {{data}}, às {{hora}}
Código: {{codigo}}

Para acompanhar a reserva: {{link}}

{{empresa}}
```

Em reserva por diária, acrescente a linha do próprio artigo: `Saída: {{dataSaida}} · {{noites}} noite(s)`. Na conexão oficial, o artigo não diz como o aviso sai com a janela fechada: peça um teste.

---

## 5. Lembrete

### Resposta rápida (texto)

Atalho: `/lembrete`

```
{{ms}}, {{firstName}}! Passando para lembrar do seu horário de [serviço] amanhã, [data], às [hora]. Se não puder vir, me avisa por aqui para eu liberar a vaga?
```

### Agendamento (conexão por QR Code)

Onde: **Agendamentos** › **+ Nova Agendamento**, ou o botão **Agendamento** dentro da conversa. Como o agendamento é feito contato a contato, escreva o nome do cliente direto no texto.

```
Olá, [nome]! Aqui é da [Nome da Empresa]. Lembrete do seu horário de [serviço] amanhã, [data], às [hora]. Se não puder vir, é só responder esta mensagem.
```

### Template (API Oficial)

- Nome sugerido: `lembrete_horario`
- Categoria: Utilidade

```
Olá, {{1}}. Lembrete: seu horário de {{2}} é em {{3}}, às {{4}}. Se não puder comparecer, responda a esta mensagem.
```

`{{1}}` nome (extra2), `{{2}}` serviço (extra3), `{{3}}` data (extra4), `{{4}}` hora (extra5).

Para agendamento na conexão oficial, vale o mesmo cuidado da cobrança: prefira uma versão de texto fixo.

```
Olá! Aqui é da [Nome da Empresa]. Você tem um horário marcado conosco nos próximos dias. Para confirmar ou remarcar, responda a esta mensagem.
```

### Aviso automático do Consultório (lembrete automático)

Onde: menu **Consultório › Cadastros do consultório** › aba **Confirmação** › **Lembretes automáticos** › **Adicionar lembrete** › **Texto**. Só variáveis da lista do artigo Aba Confirmação em Cadastros do Consultório. O lembrete vai com os botões **Confirmar**, **Remarcar** e **Cancelar**: o texto não pede resposta digitada.

```
Olá, {{paciente}}! Lembrete da sua consulta: {{servico}} com {{profissional}}, {{diaDaSemana}}, {{data}}, às {{hora}}.

Use os botões desta mensagem para confirmar, remarcar ou cancelar.

{{clinica}}
```

O artigo lista essas variáveis sem descrever o que cada uma vira: confira o resultado num lembrete de teste. Na conexão oficial, fora da janela de 24 horas só sai modelo aprovado (opção **Usar um modelo aprovado da API oficial**): aí o que se redige é um template como o de cima. Se o modelo vale também para os lembretes, o artigo não diz.

---

## 6. Pós-venda

### Resposta rápida (texto)

Atalho: `/posvenda`

```
{{ms}}, {{firstName}}! Aqui é {{user}}, da [Nome da Empresa]. Seu [produto ou serviço] foi entregue em [data]. Deu tudo certo? Se precisar de qualquer ajuste, é só me responder por aqui.
```

### Template (API Oficial) — status do pedido

- Nome sugerido: `pedido_confirmado`
- Categoria: Utilidade
- Texto do próprio artigo Mensagem Template:

```
Olá {{1}}, seu pedido #{{2}} foi confirmado e já está sendo separado. Avisaremos quando sair para entrega.
```

`{{1}}` nome (extra2), `{{2}}` número do pedido (extra3).

### Template (API Oficial) — acompanhamento depois da entrega

- Nome sugerido: `acompanhamento_pos_venda`
- Categoria: conte com Marketing. Pelo critério do artigo, não é algo que o cliente espera porque pediu; é a empresa que quer manter contato.

```
Olá, {{1}}! Aqui é da [Nome da Empresa]. Você recebeu {{2}} há alguns dias e queremos saber se deu tudo certo. Se precisar de ajuda, responda a esta mensagem. Para não receber mais mensagens como esta, responda PARAR.
```

`{{1}}` nome (extra2), `{{2}}` produto ou serviço (extra3).

---

## 7. Pesquisa

### Resposta rápida (texto)

Atalho: `/pesquisa`

```
{{firstName}}, para a gente melhorar: de 0 a 10, quanto você recomendaria a [Nome da Empresa] a um amigo? É só responder com o número.
```

Atalho: `/pesquisa motivo` (depois da nota)

```
Obrigado pela nota! O que mais pesou para você escolher esse número?
```

### Pesquisa nativa da plataforma (Avaliações)

Onde: menu **Avaliações** › **Adicionar** (`references/docs/recursos/avaliacoes.md`). O atendente envia pelo botão **Resolver e Enviar Avaliação** (**Encerrar com avaliação** no pop-up de encerrar, pela nota de atualização de 20/11/2026), depois de ligar **Enviar Avaliações** em **Configurações › Opções › Automação**, seção **Avaliações** (`references/docs/recursos/avaliacoes-em-configuracoes.md`).

Campo **Mensagem de Avaliação**:

```
Como você avalia o atendimento que recebeu hoje?
```

**Opções de Avaliação** (crie cada uma em **+ Adicionar Opção**):

```
Ótimo
Bom
Regular
Ruim
```

Campo **Mensagem de Avaliação** da Conexão (o artigo Avaliações a descreve como a mensagem enviada depois da escolha). Afirmação, sem pergunta:

```
Obrigado pela sua avaliação! Ela ajuda a gente a atender cada vez melhor.
```

### Template (API Oficial)

- Nome sugerido: `pesquisa_satisfacao`
- Categoria: a documentação não diz onde a pesquisa se encaixa. Conte com Marketing.

```
Olá, {{1}}! Aqui é da [Nome da Empresa]. Você foi atendido por nós em {{2}} e sua opinião conta muito. De 0 a 10, quanto você nos recomendaria? Responda com o número. Para não receber mais mensagens como esta, responda PARAR.
```

`{{1}}` nome (extra2), `{{2}}` data do atendimento (extra3).

---

## 8. Reativação

### Resposta rápida (texto), para abordagem individual

Atalho: `/reativar`

```
{{ms}}, {{firstName}}! Aqui é {{user}}, da [Nome da Empresa]. Faz um tempo que você não aparece e separei [benefício concreto] para a sua volta, válido até [data]. Quer que eu te explique como funciona?
```

### Campanha comum (conexão por QR Code): cinco variações

Onde: **Campanhas** › **NOVA CAMPANHA** › campanha via mensagem simples. Sem variável, porque os artigos de Campanhas não documentam variáveis nesse campo.

Variação 1

```
Olá! Aqui é da [Nome da Empresa]. Faz um tempo que a gente não se fala e preparamos [benefício] para quem já é cliente, válido até [data]. Quer saber como usar? É só responder esta mensagem.
```

Variação 2

```
Oi! [Nome da Empresa] por aqui. Sentimos sua falta e separamos [benefício] para a sua volta, até [data]. Responda QUERO que a gente te explica.
```

Variação 3

```
Olá, tudo bem? Aqui é da [Nome da Empresa]. Quem já passou por aqui tem [benefício] até [data]. Posso te mandar os detalhes?
```

Variação 4

```
Oi! Passando para avisar que a [Nome da Empresa] liberou [benefício] para clientes antigos, até [data]. Se fizer sentido para você, responda esta mensagem e eu te explico.
```

Variação 5

```
Olá! Você já foi cliente da [Nome da Empresa] e queremos te receber de novo: [benefício], válido até [data]. Quer aproveitar? Responda SIM.
```

Campo **Mensagem de Descadastramento**:

```
Se não quiser mais receber nossas mensagens, responda PARAR.
```

Acompanhe sempre com o aviso de risco de bloqueio e a sugestão de intervalos do artigo Configurar Campanhas.

### Template (API Oficial)

- Nome sugerido: `reativacao_cliente`
- Categoria: Marketing

```
Olá, {{1}}! Aqui é da [Nome da Empresa]. Faz um tempo que não nos falamos e separamos uma condição para a sua volta: {{2}}, válida até {{3}}. Quer saber como usar? Responda a esta mensagem. Para não receber mais ofertas, responda PARAR.
```

`{{1}}` nome (extra2), `{{2}}` benefício (extra3), `{{3}}` data limite (extra4). Se o benefício e a data são iguais para todos, preencha os campos extras de uma vez pela **Edição em Massa** da lista.

Versão curta do próprio artigo Mensagem Template:

```
Oi {{1}}, faz tempo que não nos falamos! Selecionamos uma oferta especial para você voltar: {{2}}
```

---

## 9. Aniversário

### Mensagem de Aniversário automática

Onde: **Configurações › Opções › Automação** › seção **Mensagens automáticas**, campo **Mensagem de Aniversário**. Enviada às 10h, no fuso da empresa, pela conexão marcada como **Padrão**, para contatos com o campo **Aniversário** preenchido. Sem variável, porque os artigos não documentam variáveis nesse campo.

```
Feliz aniversário! A equipe da [Nome da Empresa] deseja um dia muito especial para você. Para comemorar, separamos [presente], válido até [data]. Quer usar? Responda QUERO.
```

Na conexão oficial, esse texto é mensagem comum: com a janela de 24 horas fechada, é bloqueado. Avise e ofereça a campanha do mês com template (abaixo).

### Resposta rápida (texto)

Atalho: `/parabens`

```
Parabéns, {{firstName}}! Toda a equipe da [Nome da Empresa] deseja um ótimo aniversário. Seu presente: [presente], válido até [data]. Quer que eu já deixe reservado para você?
```

### Template (API Oficial), para campanha com a lista Por Aniversário

A lista **Por Aniversário** reúne quem faz aniversário no mês escolhido; por isso o texto fala do mês, não do dia.

- Nome sugerido: `aniversariante_do_mes`
- Categoria: Marketing (felicitação de aniversário é Marketing, segundo o artigo)

```
Olá, {{1}}! Este é o mês do seu aniversário e a [Nome da Empresa] quer comemorar com você: {{2}}, válido até {{3}}. Para usar, responda a esta mensagem. Para não receber mais ofertas, responda PARAR.
```

`{{1}}` nome (extra2), `{{2}}` presente (extra3), `{{3}}` data limite (extra4). Template com variável exige **Lista de Contato** com os campos extras preenchidos.

Versão do próprio artigo Mensagem Template, para o dia:

```
Parabéns, {{1}}! Hoje é o seu dia e o presente é nosso. Venha até a loja e ganhe um brinde.
```

---

## 10. Carrinho abandonado

### Resposta rápida (texto)

Atalho: `/carrinho`

```
{{ms}}, {{firstName}}! Aqui é {{user}}, da [Nome da Empresa]. Vi que você separou [produto] e não concluiu a compra. Ficou alguma dúvida sobre [frete, pagamento ou prazo]? Posso te ajudar a finalizar por aqui.
```

### Template (API Oficial)

- Nome sugerido: `carrinho_abandonado`
- Categoria: Marketing (recuperação de carrinho é Marketing, segundo o artigo)

```
Olá, {{1}}! Você deixou {{2}} no carrinho da [Nome da Empresa]. Para concluir a compra, acesse: {{3}}. Se tiver alguma dúvida, responda a esta mensagem. Para não receber mais mensagens como esta, responda PARAR.
```

`{{1}}` nome (extra2), `{{2}}` produto (extra3), `{{3}}` link completo do carrinho, sem encurtador (extra4).

Versão do próprio artigo Mensagem Template:

```
Olá {{1}}, seus produtos ainda estão no carrinho. Finalize agora e garanta 5% de desconto.
```

**Cuidados:** prazo e desconto só se forem verdadeiros (urgência artificial aparece como conteúdo proibido no artigo Número bloqueado no WhatsApp). O disparo automático a partir da loja virtual é integração: encaminhe para a skill `cmv-api` (envio de template por API) ou `cmv-flowbuilder` (bloco Template num fluxo).

---

## Extra: encerramento

### Mensagem de conclusão da Conexão

Onde: **Conexões › editar a conexão › aba Mensagens**, campo **Mensagem de conclusão**. Vale quando nem o atendente nem o Setor têm despedida própria. Afirmação final, sem pergunta: se o cliente responder, abre um ticket novo.

```
Agradecemos o seu contato com a [Nome da Empresa]. Este atendimento foi encerrado. Sempre que precisar, é só nos chamar.
```

### Mensagem de Despedida do atendente

Onde: **Equipe › editar o usuário › aba Geral**, campo **Mensagem de Despedida**. Só funciona se a **Mensagem de conclusão** da Conexão também estiver preenchida. Para uma despedida por Setor, o campo é **Mensagem de despedida do setor**, na aba **Mensagens** do Setor.

```
Foi um prazer te atender hoje! Estou encerrando este atendimento. Um ótimo dia para você.
```
