# Receitas de fluxo e boas práticas de conversa

Esqueletos para os pedidos mais comuns. Cada um diz o ponto de entrada, a sequência de blocos, o que perguntar a mais e onde costuma dar errado. São pontos de partida: adapte ao que a pessoa descreveu, e confira no artigo de cada bloco o que preencher (`references/blocos.md` aponta os artigos).

Legenda: `→` é a saída única; `[opção]`, `[sim]`, `[não]` são saídas de blocos com mais de uma. **JSON** diz se o esqueleto cabe no arquivo importável, isto é, se o gerador tem todos os blocos (`references/descricao-compacta.md`).

## Boas práticas de conversa

Não são regras da plataforma; são o que faz um robô de atendimento ser tolerável.

- **Uma coisa por mensagem.** Texto curto, uma pergunta de cada vez. Entre dois textos seguidos, um Intervalo de 1 a 3 segundos.
- **Diga logo o que o robô faz.** A primeira mensagem diz quem fala e o que vem a seguir, em duas linhas.
- **Menu curto, com palavras do cliente.** Três a cinco opções, nomeadas pelo que o cliente quer ("Segunda via do boleto"), não pelo organograma ("Financeiro N2").
- **Sempre uma porta para gente.** Uma opção "Falar com atendente" no menu principal, e a mesma saída depois de uma resposta inválida.
- **Resposta inválida sem bronca.** Explique em uma linha como responder e mostre o menu de novo.
- **Quem some também é um caso.** Decida com a pessoa o que acontece com quem não responde: lembrete, passagem para a equipe ou encerramento com aviso.
- **Antes de passar para a equipe, avise.** Diga para onde a conversa vai e quando alguém responde. Se há horário, diga o horário; não prometa "em instantes" de madrugada.
- **Deixe o resumo para o atendente.** Uma Msg Interna com o que o cliente escolheu e respondeu poupa a pessoa de perguntar de novo.
- **Peça só o dado que vai ser usado.** Cada Pergunta a mais é um ponto de abandono.
- **Termine tudo.** Todo caminho acaba num Setor, num atendente, em outro fluxo ou num Encerrar com despedida.

## 1. Triagem por menu

- **Entrada:** conexão apontando para um único Setor com o fluxo (Setor Único com Fluxo Automático (`references/docs/recursos/setor-unico-com-fluxo-automatico.md`)).
- **Esqueleto:**
  ```
  Início → Conteúdo (boas-vindas) → Menu (assuntos; Caminho alternativo (ELSE) marcado e Sem resposta preenchido)
    [opção de equipe]   → Conteúdo (aviso da passagem) → Msg Interna (resumo) → Setor
    [opção informativa] → Conteúdo (resposta) → volta ao Menu, ou Encerrar
    [Resposta inválida] → Conteúdo ("não entendi") → volta ao Menu
    [Sem resposta]      → Encerrar (com aviso)
  ```
- **Este é o padrão da skill para triagem:** aviso, Msg Interna e Setor em cada ramo de equipe. **Tag** só entra (entre o Menu e o aviso) quando a pessoa já usa tags, porque cada uma precisa existir no menu **Tags** e, no arquivo, do ID dela.
- **Perguntar:** quais assuntos, qual Setor recebe cada um, o que responder nos assuntos que o robô resolve sozinho.
- **Cuidado:** deixe vazia a **Mensagem de saudação** do Setor de entrada, senão o cliente recebe duas boas-vindas. Mantenha o Setor de entrada só para o robô e entregue a conversa a Setores sem fluxo ligado (armadilha 3 do `SKILL.md`).
- **JSON:** sim. `assets/descricao-exemplo.json` é esta receita com três opções de equipe, a última "Falar com atendente"; copie e troque textos, opções e Setores.

## 2. Qualificação de lead

- **Entrada:** conexão; ou **Webhooks | Triggers** e API, quando o lead vem de formulário ou anúncio (Pontos de Entrada (`references/docs/recursos/pontos-de-entrada.md`)).
- **Esqueleto:**
  ```
  Início → Conteúdo (abertura) → Pergunta (nome) → Variável %nome%
         → Menu (interesse) → Variável %interesse% → Menu (prazo ou porte) → Variável %prazo%
         → Tag (qualificado) → [Oportunidade] → Msg Interna (resumo com as variáveis) → Conteúdo (aviso) → Setor ou Rodízio
  ```
- **Perguntar:** quais dados qualificam, o que é um lead bom, quem recebe, se há CRM para a Oportunidade.
- **Cuidado:** a Variável vem logo depois da Pergunta ou do Menu. Oportunidade num trecho que roda uma vez. Preencha **Sem resposta** nas Perguntas, no editor.
- **JSON:** sim. Oportunidade entra como `marcador`. Rodízio não tem formato observado, e o artigo não descreve as saídas dele no desenho: ponha um Setor no arquivo e diga para trocar pelo Rodízio no editor.

## 3. Horário de expediente

- **Entrada:** conexão.
- **Esqueleto:**
  ```
  Início → Horário de Expediente (Setor)
    [Dentro do Horário] → segue a triagem normal
    [Fora do Horário]   → Conteúdo (horário de volta e o que dá para adiantar) → Pergunta (recado) → Variável
                        → Msg Interna (recado) → Setor, ou Encerrar
  ```
- **Perguntar:** dias e horas de cada Setor, se há feriados, se fora do horário a conversa fica esperando a equipe ou é encerrada.
- **Cuidado:** o bloco lê o horário da aba **Horários** do Setor, que depende do **Gerenciamento de Expediente** (Horário de Expediente (`references/docs/recursos/bloco-horario-de-expediente.md`), Aba Horários (`references/docs/recursos/aba-horarios-em-setores-e-chatbot.md`)). Ligar esse gerenciamento muda o comportamento de todos os Setores. Alternativa sem mexer nisso: Condição com **Qual Dia da Semana?**, **É Feriado?** e **Horário**, em sequência.
- **JSON:** com ressalva. No bloco `away`, `a` = Dentro do Horário e `b` = Fora do Horário (visto numa conversa de teste em 22/11/2026); a entrega ainda manda conferir no editor. As Condições de dia e horário não têm formato observado: roteiro.

## 4. Agendamento

Com ofertas cadastradas no menu **Reservas**, o bloco **Reservas (agendar no fluxo)** deixa o cliente escolher a oferta, o dia e o horário livre e confirmar sozinho (Reservas (agendar no fluxo) (`references/docs/recursos/reservas-agendar-no-fluxo.md`)): `Início → Conteúdo → Reservas (agendar no fluxo) [Reservou] → Conteúdo (agradecimento) → Encerrar; [Não reservou] → Conteúdo (aviso) → Setor; [Sem resposta] → Encerrar`. Esse bloco não tem formato observado: roteiro. Sem ele, o fluxo coleta o pedido e entrega a uma pessoa, ou consulta um sistema externo.

- **Esqueleto:**
  ```
  Início → Conteúdo → Menu (serviço) → Variável %servico%
         → Pergunta (dia de preferência) → Variável %dia% → Menu (período) → Variável %periodo%
         → Conteúdo ("anotei: %servico%, %dia%, %periodo%; a equipe confirma o horário")
         → Msg Interna (resumo) → Setor
  ```
- **Variação com sistema externo:** no lugar da passagem, HTTP Request ou Execução de Código JS consulta a agenda e uma Condição decide o caminho. A chamada é assunto da `cmv-api`.
- **Cuidado:** não prometa horário confirmado se quem confirma é uma pessoa.
- **JSON:** sim, na versão com passagem para a equipe; não com o bloco Reservas (agendar no fluxo).

## 5. Cobrança e segunda via

- **Entrada:** conexão (opção do menu), remarketing por tag ou campanha.
- **Esqueleto com Asaas:**
  ```
  … → Pergunta ("digite o CPF ou CNPJ, só números") → [Execução de Código JS para limpar] → Asaas
    [Sucesso] → Intervalo → Conteúdo ("mais alguma coisa?") → Menu ou Encerrar
    [Erro]    → Conteúdo ("não consegui consultar") → Setor Financeiro
  ```
- **Sem Asaas:** HTTP Request para o sistema de cobrança (`cmv-api`), ou passagem direta ao Setor.
- **Cuidado:** o Asaas envia só a fatura mais recente; combine o que fazer com as antigas. Ligue a saída **Erro**. Dedução, não frase de artigo: em cobrança iniciada pela empresa no WhatsApp Oficial, a primeira mensagem tende a precisar ser um **Template**, porque o artigo do bloco diz que ele é o único jeito de o fluxo falar com quem não escreveu nas últimas 24 horas (`references/docs/recursos/bloco-template.md`). Avise e mande testar.
- **JSON:** não para o Asaas; roteiro.

## 6. Pós-venda e pesquisa

- **Entrada:** tag com remarketing (por exemplo, 24 horas depois), ou a nota da avaliação do encerramento (Gatilho via Avaliação (`references/docs/recursos/gatilho-via-avaliacao.md`)).
- **Esqueleto por nota:** um fluxo por nota. Nota baixa: `Início → Conteúdo (desculpas) → Pergunta (o que faltou) → Variável → Msg Interna → Setor`. Nota alta: `Início → Conteúdo (agradecimento e link) → Encerrar`.
- **Esqueleto com pesquisa no fluxo:** `… → Avaliação do Atendimento → [resposta] Conteúdo (agradecimento) → Encerrar; [Sem resposta] → Encerrar`.
- **Esqueleto com lembrete:** `… → Menu (pergunta; Sem resposta no prazo) → [resposta] Setor; [Sem resposta] → Menu (lembrete; Sem resposta) → [resposta] Setor; [Sem resposta] → Encerrar`. O lembrete é um segundo Menu, e o Encerrar só vem depois dele: assim quem responde ao lembrete ainda chega ao Setor. Com o Encerrar logo depois do lembrete, a resposta abre outro protocolo no Setor da Conexão e dispara o fluxo de lá (`references/docs/recursos/gatilho-via-conexao.md`) ou, no remarketing, volta ao Setor do campo **Setor do atendimento reaberto** (`references/docs/recursos/gatilho-via-remarketing-de-tag.md`); não diga que ela "volta a este fluxo" nem que "não volta".
- **Cuidado:** a avaliação do encerramento só é enviada com o atendimento em **Atendendo**. O bloco Avaliação do Atendimento não encerra sozinho. No fluxo da nota, a resposta de uma Pergunta seguida de Variável fica guardada na avaliação e aparece no menu **Relatório de Avaliações**.
- **JSON:** sim para os fluxos de nota; a Avaliação do Atendimento não tem formato observado.

## 7. Remarketing por tag

- **Entrada:** menu **Tags**, aba **Remarketing** da tag: o fluxo, o prazo (a partir de 5 minutos) e o **Setor do atendimento reaberto** (Gatilho via Remarketing de Tag (`references/docs/recursos/gatilho-via-remarketing-de-tag.md`)).
- **Esqueleto:**
  ```
  Início → Conteúdo ("oi, ficou alguma dúvida?") → Menu (quero continuar / agora não; ELSE e Sem resposta)
    [quero continuar] → Remover Tag → Conteúdo (aviso) → Setor
    [agora não]       → Remover Tag → Encerrar (despedida)
    [Sem resposta]    → Encerrar
  ```
- **Perguntar:** qual tag dispara, quem a coloca (atendente ou outro fluxo), o prazo, o canal.
- **Cuidado:** o remarketing dispara mesmo com o cliente em conversa com um atendente e pode atropelar a conversa. Alguns blocos só funcionam no **Aguardando**; o artigo indica um Trocar Fluxo no começo, com o aviso de que a conversa sai das mãos da equipe. Dedução, não frase do artigo do gatilho: no WhatsApp Oficial, se o prazo passar de 24 horas desde a última mensagem do cliente, a primeira mensagem do fluxo tende a precisar ser um **Template**, porque o artigo do bloco diz que ele é o único jeito de o fluxo falar com quem não escreveu nas últimas 24 horas (`references/docs/recursos/bloco-template.md`). O artigo do remarketing não trata disso: avise e mande testar. Tirar a tag antes do prazo cancela o disparo.
- **JSON:** sim, com o tipo `marcador` no lugar do Remover Tag (e do Template, se houver), ou roteiro. O artigo do Remover Tag não diz quantas saídas o bloco tem: mande conferir no editor.

## 8. Chamada a sistema externo

- **Consulta no meio da conversa:** `… → Pergunta (número do pedido) → Variável %pedido% → HTTP Request (resposta em variável) → Conteúdo ("seu pedido está %http_retorno.status%") → …`. Com código: `Execução de Código JS → Variável → Condição`.
- **Sistema externo que inicia o fluxo:** Gatilho via API (sem variáveis próprias) ou Webhooks | Triggers (com `{nome}`, `{email}`, `{extra1}`…).
- **Cuidado:** trate a falha. Com código, o `return` do `catch` vira o valor da Variável; uma Condição logo depois separa erro de sucesso. Um Intervalo curto entre a chamada e o uso do resultado é o que o artigo do Intervalo sugere.
- **Limite:** endpoint, corpo, autenticação e o lado do n8n são da `cmv-api`. Aqui fica o desenho: onde chamar, o que guardar, o que dizer ao cliente em cada resultado.
- **JSON:** só a versão com Execução de Código JS; o HTTP Request não tem formato observado, e o artigo dele não descreve as saídas do bloco: no roteiro, mande ligar todas as saídas que aparecerem no desenho.

## 9. Comentário do Instagram

- **Entrada:** Setor próprio para comentários, com **Palavras-Chave e Gatilhos**, e a conexão do Instagram com **Habilitar ação para comentários** (Gatilho via Comentário do Instagram (`references/docs/recursos/gatilho-via-comentario-do-instagram.md`)).
- **Atalho:** as Automações Rápidas (`references/docs/recursos/automacoes-rapidas.md`) criam três modelos prontos, como rascunho. Sugira antes de montar do zero.
- **Esqueleto:** `Início → Responder Comentário (várias frases) → Conteúdo (mensagem no Direct) → [É Seguidor?] → …`
- **Cuidado:** saudação do Setor vazia, senão o comentário recebe duas respostas públicas. O fluxo desse Setor também responde a mensagens do Direct.
- **JSON:** não; roteiro ou Automações rápidas.

## 10. Fluxo chamado pelo atendente (resposta rápida)

- **Entrada:** menu **Respostas Rápidas**, campo **Fluxo de Automação** (Gatilho via Resposta Rápida (`references/docs/recursos/gatilho-via-resposta-rapida.md`)).
- **Esqueleto:** `Início → Pergunta → Variável → … → Msg Interna (dados coletados) → Encerrar Mensagem Rápida`
- **Cuidado:** termine em **Encerrar Mensagem Rápida** (ou Trocar Fluxo). Um Encerrar comum fecha o atendimento do atendente.
- **JSON:** não para o último bloco; roteiro, ou JSON com marcador no fim.
