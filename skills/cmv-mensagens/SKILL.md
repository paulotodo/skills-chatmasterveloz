---
name: cmv-mensagens
description: "Redige mensagens prontas para colar no Chat Master Veloz (CMV, chatmasterveloz): respostas rápidas, templates da API Oficial do WhatsApp, campanhas, agendamentos, mensagem de aniversário, saudação e fora de expediente do setor, ausência e encerramento, com as variáveis certas. Quem tem esta skill instalada atende pelo CMV: carregue-a antes de escrever, melhorar ou revisar qualquer texto que a empresa envia a clientes e contatos (aviso, cobrança, lembrete, confirmação, reativação, pós-venda, boas-vindas, mensagem automática), por mais simples que pareça e mesmo sem citar o CMV, \"resposta rápida\" ou \"template\"; não use para texto que não vai por mensagem (e-mail, roteiro de ligação, post, impresso) nem para outra ferramenta. Vale também para template reprovado, categoria utilidade ou marketing, janela de 24h, cobrança da Meta e risco de bloqueio. Não cobre desenho de fluxo de chatbot (cmv-flowbuilder), envio de template por API (cmv-api) nem prompt de IA (cmv-agente-ia)."
---

# cmv-mensagens: redigir mensagens para o Chat Master Veloz

Esta skill transforma um pedido como "cria respostas rápidas para minha clínica" em material pronto: o texto de cada mensagem, com as variáveis na sintaxe que o campo aceita, o lugar exato do painel onde cadastrar e os avisos de risco que a documentação registra.

Quem pede costuma não ser técnico. A resposta precisa poder ser seguida por alguém que só sabe abrir o painel e colar.

## Fluxo de trabalho

### 1. Descubra o tipo de conexão antes de escrever

É a primeira pergunta porque muda quase tudo: o que pode ser enviado, se precisa de aprovação, se custa e qual é o risco.

| | Conexão oficial (API Oficial) | Conexão por QR Code (não oficial) |
|---|---|---|
| Falar primeiro ou depois de 24h sem resposta do cliente | Só por template aprovado pela Meta | Texto livre |
| Dentro da janela de atendimento | Texto livre | Não se aplica |
| Cobrança por mensagem enviada | Sim, pela Meta | Não |
| Risco principal | Template reprovado, mensagem que não é entregue, custo | Bloqueio do número, que pode ser definitivo |

Se a pessoa não souber qual usa, ensine a conferir: no menu **Conexões**, o card da conexão oficial tem os botões **Gestão de Templates** e **Limitador de Mensagens**; a conexão por QR Code não tem. Se ela usa as duas, ou não respondeu, entregue as duas versões identificadas, em vez de escolher por ela.

Artigos: `references/docs/recursos/whatsapp-oficial-x-nao-oficial.md`, `references/docs/recursos/entenda-a-api-oficial.md`, `references/docs/recursos/janela-de-atendimento.md`.

### 2. Levante o contexto com poucas perguntas

Pergunte de uma vez só, e apenas o que falta:

1. Negócio e o que vende (segmento, produto ou serviço).
2. Para quem é a mensagem (cliente novo, cliente ativo, inadimplente, quem sumiu).
3. Objetivo: o que o cliente deve fazer depois de ler.
4. Tom (formal, próximo, descontraído) e nome da empresa.

Em pedido de cobrança, ou de qualquer aviso que se repete, pergunte também, porque as respostas decidem entre agendamento e campanha (armadilha 9):

5. Qual é o dia do vencimento e em que dia a mensagem deve sair (no dia, antes ou depois).
6. Se o valor ou o link de pagamento mudam de um cliente para outro.
7. Quantos clientes recebem.

Se o pedido já traz o suficiente, não trave: escreva, declare as suposições em uma linha e deixe entre colchetes o que só o usuário sabe (`[link]`, `[data]`, `[valor]`).

### 3. Escolha o tipo de mensagem

| O usuário quer… | Tipo no CMV | Observação |
|---|---|---|
| Textos que o atendente dispara no meio da conversa | Resposta rápida | Texto, mídia, contato, localização ou fluxo |
| Avisar ou abordar clientes pela conexão oficial fora da janela | Template | Utilidade ou Marketing |
| Mandar a mesma mensagem para muita gente | Campanha | Por QR Code: 5 variações de texto. Oficial: um template |
| Mandar algo para um contato em data futura, ou todo mês | Agendamento | Na oficial, só com template |
| Parabenizar no dia do aniversário | Mensagem de Aniversário | Um texto só, enviado às 10h |
| O que o cliente lê ao chegar ou fora do horário | Mensagens do Setor (e da Conexão) | Saudação, fora de expediente |
| Aviso de que o atendente saiu; despedida | Mensagem de Ausência; Mensagem de Conclusão/Despedida | Campos do Perfil e da Conexão |

Um pedido pode render mais de um tipo. "Campanha de reativação" na oficial, por exemplo, é um template de Marketing mais a lista com os campos extras preenchidos.

### 4. Redija consultando o material, nesta ordem

1. `references/regras-por-tipo-de-mensagem.md` — a ficha do tipo: campos, variáveis aceitas, limites. É a fonte para qualquer afirmação sobre o produto. Abra a ficha antes de escrever, mesmo em pedido que parece simples: a ordem dos passos da tela, os nomes exatos dos campos, os valores que o artigo recomenda e os links para citar estão nela, não neste arquivo.
2. `assets/modelos.md` — ponto de partida por objetivo. Adapte; não entregue o modelo cru.
3. `references/boas-praticas-de-redacao.md` — revisão de texto. São recomendações gerais de comunicação, não regras da plataforma: ao falar com o usuário, não as apresente como exigência do CMV ou da Meta.
4. O artigo de origem em `references/docs/`, quando precisar de um detalhe que a ficha não traz.

### 5. Entregue no formato padrão, com passo a passo e avisos

Veja "Formato de entrega" abaixo. Toda entrega termina com os riscos que se aplicam àquele caso, cada um com o artigo citado.

## Como consultar a documentação

A cópia da Central de Ajuda está em `references/docs/` (um arquivo por artigo). Não leia tudo.

1. Abra `references/docs/INDICE.md` e localize o artigo pelo título. Cada linha traz o título, o caminho do arquivo e o link da **Fonte**: dá para citar um artigo sem abri-lo.
2. Com terminal, busque o termo: `grep -il 'descadastramento' references/docs/recursos/*.md` e depois `grep -n -i 'descadastramento' references/docs/recursos/nova-campanha.md`. Sem terminal, abra o artigo indicado pelo índice.
3. Leia só o artigo necessário. Os blocos `> **[RESUMO]**`, `> **[DUVIDAS]**` e `> **[ERROS]**` concentram o passo a passo e as armadilhas.
4. Ao afirmar algo sobre o produto, cite o **título do artigo** e o link da **Fonte** (está no `INDICE.md`, no cabeçalho do artigo e, já ao lado do título, nas linhas **Artigos:** das fichas). A linha **Menu** do cabeçalho do artigo é o caminho na Central de Ajuda, não no painel: o caminho que a pessoa clica está no corpo do artigo, e, quando o artigo não diz por onde se chega à tela, diga que isso não está documentado.

Regras de honestidade, e o motivo de cada uma:

- **Só afirme o que está no artigo.** O usuário vai colar o texto e disparar para clientes; uma variável inventada chega ao cliente como texto literal com chaves, e um caminho de menu errado faz a pessoa desistir.
- **Imagens não foram transcritas.** Vários formulários (como o de **NOVO TEMPLATE**) só aparecem em imagem. Não descreva campos que você não leu em texto.
- **Diga "a documentação não cobre isso"** quando for o caso, e proponha um teste antes do envio real (ver "Teste antes do envio").
- **Não misture variantes de conexão.** O que vale para a oficial não vale para a por QR Code, e vice-versa. Os artigos dizem por extenso a que conexão se aplicam ("conexão oficial", "por QR Code"); a comparação está em `references/docs/recursos/whatsapp-oficial-x-nao-oficial.md`.
- **Não cite preços nem planos.** A cobrança é da Meta e muda; diga que existe, quem cobra e o que conta (ver "Quando perguntarem quanto custa").
- **Não afirme regra da Meta de memória.** Aprovação de template é decisão da Meta e não pode ser garantida; o que os artigos dizem sobre reprovação está reunido numa lista única na ficha de template.
- **Variável `{{...}}` se copia, não se digita de memória.** A referência da sintaxe e da lista de códigos é `references/docs/recursos/mustaches.md`. Antes de entregar, confira cada variável do texto contra a lista desse artigo, letra por letra.

## Mapa do material

| Preciso de… | Onde |
|---|---|
| Campos, variáveis, limites e avisos de cada tipo | `references/regras-por-tipo-de-mensagem.md` |
| Sintaxe e lista oficial das variáveis `{{...}}` (mustaches) | `references/docs/recursos/mustaches.md` |
| As três sintaxes de variável e o que cada campo confirma | `references/regras-por-tipo-de-mensagem.md`, seção 0 |
| O que causa reprovação de template, pausa ou bloqueio (lista única) | `references/regras-por-tipo-de-mensagem.md`, seção 2 |
| Roteiro de custo da API Oficial, sem valores | `references/regras-por-tipo-de-mensagem.md`, seção 9 |
| Pontos em que os artigos se contradizem | `references/regras-por-tipo-de-mensagem.md`, seção 10 |
| Modelos por objetivo (saudação, ausência, cobrança, confirmação, lembrete, pós-venda, pesquisa, reativação, aniversário, carrinho) | `assets/modelos.md` |
| Critérios de redação e lista de conferência | `references/boas-praticas-de-redacao.md` |
| Resposta rápida de texto e como usar o atalho | `references/docs/recursos/resposta-rapida-envio-de-texto.md` |
| Resposta rápida de mídia, contato, localização e fluxo | `references/docs/recursos/resposta-rapida-envio-de-midia.md`, `references/docs/recursos/resposta-rapida-envio-de-contato.md`, `references/docs/recursos/resposta-rapida-envio-de-localizacao.md`, `references/docs/recursos/resposta-rapida-de-fluxo.md` |
| Banco de ideias de respostas rápidas por área | `references/docs/recursos/ideias-de-respostas-rapidas.md` |
| Template: categorias, modelos, erros | `references/docs/recursos/mensagem-template.md` |
| Template: onde criar, sincronizar, grupos, erros de envio | `references/docs/recursos/whatsapp-oficial-gestao-de-templates.md` |
| Campanha por QR Code | `references/docs/recursos/nova-campanha.md`, `references/docs/recursos/configurar-campanhas.md` |
| Campanha oficial e a planilha com extras | `references/docs/recursos/nova-campanha-api-oficial.md` |
| Listas de contatos | `references/docs/recursos/fontes-de-contatos-para-campanhas.md` |
| Agendamentos | `references/docs/recursos/adicionar-agendamento.md` |
| Aniversário | `references/docs/recursos/mensagem-de-aniversario.md`, `references/docs/recursos/mensagem-de-aniversario-em-configuracoes.md` |
| Saudação e fora de expediente do Setor | `references/docs/recursos/aba-mensagens-em-setores-e-chatbot.md`, `references/docs/recursos/aba-horarios-em-setores-e-chatbot.md` |
| Mensagens da Conexão (saudação, conclusão, fora de expediente, avaliação, inatividade) e menu de Setores | `references/docs/recursos/adicionar-whatsapp-qrcode.md`, `references/docs/recursos/adicionar-whatsapp-oficial.md`, `references/docs/recursos/chatbot-e-menu-de-setores-na-conexao.md` |
| Ausência, encerramento e despedida | `references/docs/recursos/mensagem-de-ausencia.md`, `references/docs/recursos/mensagem-de-encerramento.md` |
| Pesquisa de satisfação (Avaliações) | `references/docs/recursos/avaliacoes.md`, `references/docs/recursos/avaliacoes-em-configuracoes.md` |
| Janela de 24h e de 72h | `references/docs/recursos/janela-de-atendimento.md` |
| Cobrança da API Oficial e onde acompanhar o consumo | `references/docs/trilhas/a-cobranca-do-whatsapp-oficial-mudou.md`, `references/docs/trilhas/medir-quanto-voce-ja-enviou-no-mes.md`, `references/docs/recursos/limitador-de-mensagens.md` |
| Bloqueio de número, opt-in, limites de envio | `references/docs/recursos/numero-bloqueado-no-whatsapp.md` |

## Armadilhas encontradas na documentação

Cada uma já causou, ou causaria, uma entrega errada. Confira antes de responder.

1. **Três sintaxes de variável.** `{{firstName}}` (mustache da plataforma), `{{1}}` (template) e `{nome}` / `%variavel%` (preenchimento do bloco Template no FlowBuilder) não são intercambiáveis. `{{nome}}` não existe em nenhuma delas.
2. **Mustache é exato** (`references/docs/recursos/mustaches.md`). Maiúsculas contam (`{{firstName}}`, não `{{firstname}}`), não pode haver espaço dentro das chaves e não dá para inventar código: o que o sistema não reconhece vai literal para o cliente.
3. **Nem todo campo confirma variáveis.** O artigo do Setor confirma `{{name}}` na saudação; o da resposta rápida confirma que há variáveis. Para mensagem simples de campanha, agendamento, aniversário, fora de expediente, ausência e conclusão, o artigo do campo não diz nada. Nesses, escreva sem variável ou avise que é para testar.
4. **Utilidade contaminada.** Uma única frase de oferta num template de Utilidade faz o modelo inteiro virar Marketing; e Utilidade com linguagem vendedora é recusada. Cobrança e aviso: informe e pare. A oferta vai em outro template.
5. **Editar template aprovado tira ele do ar** até nova aprovação, e excluir apaga também na Meta. Ao revisar um template em uso, sugira criar um novo em vez de editar.
6. **Na campanha oficial o extra2 é a `{{1}}`.** O extra1 é a imagem do cabeçalho. Só há campos para `{{1}}` a `{{5}}`: template para campanha não deve ter mais de cinco variáveis no corpo. Template com variável exige **Lista de Contato** com os extras preenchidos; variável vazia faz a Meta recusar.
7. **Campos que não se usam na campanha oficial:** **Gatilho**, **Caracteres Ocultos**, **Mensagem de Descadastramento** e mais de uma conexão. A opção de saída tem de estar no texto do template.
8. **Agendamento na oficial ignora o texto digitado.** É obrigatório escolher um template; o que for escrito por cima é sobrescrito, e texto livre sem template falha mesmo com a janela aberta.
9. **Cobrança recorrente na oficial: no agendamento, template de texto fixo.** Os artigos não dizem como as variáveis `{{1}}`, `{{2}}` de um template são preenchidas num agendamento, então não entregue template com variável para esse uso. O agendamento é descrito com um campo **Contato**, um cliente por agendamento; agendar para vários de uma vez não está documentado. Quando nome, valor ou link mudam por cliente, o caminho documentado é a campanha pela API Oficial, com **Lista de Contato** e campos extras. Mas os artigos de Campanhas só descrevem data e hora de início, pausa e reinício: repetição mensal de campanha não está documentada. Diga isso e explique que, pelo que está descrito, é uma campanha nova a cada mês (a lista pode ser reaproveitada, com os campos extras atualizados).
10. **Mensagem de aniversário na oficial** é texto comum: com a janela fechada, é bloqueada. A alternativa documentada é a lista **Por Aniversário** (aniversariantes do mês) numa campanha com template de Marketing.
11. **Saudação da Conexão e saudação do Setor somam.** Com as duas preenchidas o cliente recebe as duas. Pergunte qual já existe antes de escrever outra.
12. **Mensagem de encerramento não pode terminar em pergunta:** a resposta do cliente abre um ticket novo.
13. **Mensagem de ausência repete** a cada mensagem do cliente enquanto o status estiver Ausente. Escreva um texto que não irrite na terceira vez e diga quando o atendente volta.
14. **Fora de expediente depende de uma opção.** Com **Abrir Tickets Fora do Expediente?** em **Não**, o atendimento é encerrado: não escreva "sua mensagem ficou registrada".
15. **Colchetes em resposta rápida.** No campo **Mensagem**, `[nome do atalho]` é o código das respostas de mídia e de fluxo. Em resposta de texto, avise o usuário para trocar todos os `[...]` antes de salvar.
16. **A cobrança mudou em 1º de outubro de 2026.** Desde então a Meta cobra também o texto livre enviado dentro da janela (há uma franquia mensal por número) e o template de Utilidade com a janela aberta. O artigo de Agendamento ainda traz a regra antiga numa dúvida comum. Na oficial, uma mensagem completa custa menos que três curtas: redija assim.
17. **O Limitador de Mensagens só informa.** Não o apresente como trava de gasto.
18. **A lista de campanha é uma foto.** Quem entrou na tag depois de a lista ser criada não recebe. Em campanha que se repete, oriente a criar a lista de novo.
19. **Risco de bloqueio na conexão por QR Code nunca é zero**, mesmo com intervalos e variações. Não prometa segurança; mostre o que o artigo recomenda e deixe a decisão com o usuário.
20. **O fuso horário da empresa vale para agendamentos e campanhas** (**Configurações › Opções**). Sem escolha, o sistema usa o horário de Brasília. Em envio com hora marcada, lembre de conferir.
21. **Palavra de saída: PARAR, não SAIR.** No menu de opções do chatbot do Setor a plataforma acrescenta a linha **SAIR - Encerrar Atendimento**, e quem responde SAIR encerra o atendimento (`references/docs/recursos/chatbot-e-menu-de-setores-na-conexao.md`). Na **Mensagem de Descadastramento** da campanha e na opção de saída do template, escreva "responda PARAR".

## Quando perguntarem quanto custa

Responda sem valores, seguindo o roteiro da seção 9 de `references/regras-por-tipo-de-mensagem.md`: quem cobra (a Meta, direto na conta dela), o que é cobrado e o que não é, o que conta para a franquia, a ordem de preço entre categorias que os artigos sustentam e onde acompanhar a quantidade enviada (**Limitador de Mensagens**). Diga com clareza o que não está documentado: o valor de cada categoria, onde consultá-lo e qualquer cobrança da plataforma além da Meta.

## Teste antes do envio

Sugerir um teste é recomendação desta skill; os artigos não descrevem um recurso de teste. O que eles sustentam, e serve para montar o teste:

- Agendamento só aceita destinatário já cadastrado em **Contatos**: para testar, o número de teste precisa estar lá.
- Lista de campanha pode ser uma **Lista Manual** com um contato só (botão **Novo**), com os campos extras preenchidos.
- A **Gestão de Templates** mostra uma prévia do texto de cada modelo, e o botão **Erros de Template** mostra por que um envio foi recusado.
- Na oficial, todo template enviado é cobrado, inclusive o do teste.

O resto é prática, e deve ser dito assim: usar um número de teste diferente do número da conexão e conferir a mensagem recebida antes de disparar para clientes.

## Formato de entrega

Use sempre esta estrutura, porque ela separa o que colar, onde colar e o que pode dar errado.

**0. Resposta curta**, só quando a pessoa fez perguntas diretas ("tem como?", "vai custar?", "pode?"). Uma linha por pergunta, na ordem em que foram feitas, com sim, não ou "a documentação não diz", antes de qualquer outra coisa. O detalhe vem nos blocos seguintes.

**1. Contexto em uma linha:** conexão considerada, objetivo e suposições.

**2. Tabela das mensagens** (o resumo):

| Nome / atalho | Tipo | Texto | Variáveis usadas | Onde cadastrar |
|---|---|---|---|---|
| `/confirmar` | Resposta rápida de texto | `{{firstName}}, seu horário de [serviço] está confirmado para [data], às [hora]. Até lá!` | `{{firstName}}` = primeiro nome do contato | **Respostas Rápidas** › **Adicionar** |

- Uma linha por mensagem. Em **Variáveis usadas**, diga o que cada uma vira; escreva "nenhuma" quando não houver.
- Liste à parte o que está entre colchetes, para o usuário preencher antes de salvar.
- Texto com mais de um parágrafo: mantenha a linha na tabela e repita o texto logo abaixo, num bloco de código com o mesmo nome, para a pessoa copiar com as quebras de linha.
- Campanha com variações longas (as cinco da campanha por QR Code, cada uma com mais de um parágrafo): a tabela é opcional, porque o texto não cabe nela. No lugar dela, diga uma vez o tipo, as variáveis usadas e onde cadastrar, e entregue um bloco de código por variação ("Variação 1" a "Variação 5"), mais um para a **Mensagem de Descadastramento**.
- Template: ponha sempre o texto num bloco de código próprio, mesmo com um parágrafo só, e deixe na tabela apenas o resumo (nome, categoria, para que serve). O texto do template é copiado para uma tela de aprovação, e qualquer caractere a mais ou a menos muda o que a Meta analisa.
- Para template, acrescente por mensagem: categoria, nome sugerido, o significado de cada `{{n}}` com um valor de exemplo e, se for para campanha, o campo extra correspondente.

**3. Passo a passo numerado para cadastrar**, com o caminho do menu em negrito, na ordem em que a pessoa clica. Um bloco de passos por tipo de mensagem, não por mensagem.

**4. Avisos**, só os que se aplicam, cada um com o artigo (título e link da **Fonte**).

**5. O que a documentação não cobre**, se algo ficou em aberto, com o teste sugerido.

Caminho de arquivo desta skill (o que começa por `references/` ou `assets/`) não vai na resposta: o usuário não tem esses arquivos. No lugar dele vão o título do artigo e o link da linha **Fonte**.

## Exemplos de pedido e entrega

**Pedido:** "cria umas respostas rápidas pra minha clínica de estética, atendo pelo WhatsApp normal com QR code"

**Entrega:** contexto em uma linha (conexão por QR Code, tom próximo); tabela com oito a dez respostas rápidas (`/saudacao`, `/horario`, `/valores`, `/confirmar`, `/lembrete`, `/localizacao`, `/pix`, `/posvenda`, `/obrigado`), cada uma com tipo, texto e variáveis; a de localização no formato `<endereco> … </endereco> <mapa> … </mapa>`; passo a passo em **Respostas Rápidas** › **Adicionar**, com a dica de começar o atalho com `/` e a opção **Global** (só Admin define); aviso de trocar os colchetes; citação do artigo Resposta Rápida Envio de Texto.

**Pedido:** "migrei pra API oficial e preciso de um template de cobrança de mensalidade que não seja reprovado. tem como mandar automático todo dia 5? e isso vai me custar?"

**Entrega:**
- **Resposta curta:** dá para mandar todo dia 5 por agendamento, cliente a cliente, com um template de texto fixo; com valor e link por cliente, o caminho é campanha, e repetição automática de campanha não está documentada. Custa: todo template enviado é cobrado pela Meta conforme a categoria; o valor não está na documentação.
- **Perguntas que faltam:** vencimento em relação ao dia 5, se valor ou link mudam por cliente, quantos clientes.
- **Template de Utilidade de texto fixo**, em bloco de código, para o agendamento (**Repetir a cada** › **Todo dia...**, com a data inicial num dia 5 e o fuso conferido).
- **Template de Utilidade com `{{1}}` a `{{5}}`** (nome, referência, valor, vencimento, link), em bloco de código, com exemplo de valor e o campo extra de cada variável, para campanha pela API Oficial.
- **"Que não seja reprovado":** a lista única da ficha de template (sem oferta, sem linguagem vendedora, sem link encurtado, sem urgência artificial, categoria certa), dizendo que a aprovação é da Meta e não pode ser garantida, e o que os artigos não trazem sobre formato.
- **Passo a passo:** **Conexões** › card da conexão oficial › **Gestão de Templates** › **NOVO TEMPLATE** (os campos do formulário não estão descritos em texto) e depois **Agendamentos** › **+ Nova Agendamento**.
- **Custo:** o roteiro sem valores e onde acompanhar no **Limitador de Mensagens**.

**Pedido:** "quero disparar uma campanha pra reativar cliente que sumiu"

**Entrega:** primeiro a pergunta da conexão. Por QR Code: cinco variações do texto, o texto do campo **Mensagem de Descadastramento** com "responda PARAR" (não SAIR: armadilha 21), a criação da lista em **Campanhas › Criar Listas** (por exemplo **Por Tag**), a sugestão de intervalos do artigo Configurar Campanhas e o aviso de risco de bloqueio, com o artigo Número bloqueado no WhatsApp. Pela oficial: um template de Marketing com opção de saída no próprio texto, a planilha com `extra2` em diante, o aviso de opt-in, do limite diário de conversas iniciadas e de que a mensagem é cobrada como Marketing.

## Onde termina esta skill

| O pedido é… | Skill |
|---|---|
| Desenhar o fluxo do chatbot, escolher blocos, configurar o bloco Template dentro de um fluxo | `cmv-flowbuilder` |
| Enviar template ou mensagem por API, webhook, n8n, payload | `cmv-api` |
| Escrever o prompt do GPT Assistant ou de outro recurso de IA | `cmv-agente-ia` |
| Dúvida de uso do painel que não envolve redigir mensagem (conectar número, permissões, erro de tela) | `cmv-ajuda` |

Quando o pedido mistura as duas coisas (por exemplo, "campanha que dispara um fluxo"), entregue aqui os textos e a parte de campanha, e diga com clareza qual parte cabe à outra skill. Os textos de dentro de um fluxo podem ser redigidos aqui; a montagem do fluxo, não.
