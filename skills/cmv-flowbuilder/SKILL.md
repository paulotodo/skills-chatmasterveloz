---
name: cmv-flowbuilder
description: "Fluxo do FlowBuilder do Chat Master Veloz (chatmasterveloz, CMV) travado, mudo ou com defeito? Use esta skill: depura o fluxo, lê o .json exportado, acha o bloco onde a conversa para, a saída sem ligação, o \"Sem resposta\" vazio ou a variável perdida, e diz como corrigir no editor. Quem tem esta skill usa o CMV: pergunta sobre fluxo, bloco, robô ou chatbot que não cite outra ferramenta é do FlowBuilder; carregue-a antes de responder (blocos, variáveis e limites vêm dela), também se colarem ou anexarem um fluxo. Use também para criar fluxos de chatbot ou menu automático (triagem, lead, agendamento, cobrança, pós-venda, remarketing por tag, Instagram, sistema externo), como roteiro bloco a bloco ou .json importável, e para escolher bloco ou gatilho. Não cobre: prompt e recursos de IA (cmv-agente-ia), API e webhooks (cmv-api), textos de template, campanha e resposta rápida (cmv-mensagens), o resto do painel (cmv-ajuda), CSS/JS (cmv-painel-css-js), nem outras plataformas."
---

# FlowBuilder do Chat Master Veloz: desenhar e gerar fluxos

A pessoa descreve um atendimento que quer automatizar. Você pergunta o que falta, desenha o fluxo e entrega de um de dois jeitos:

- **Roteiro de montagem no editor:** sempre possível. Lista numerada, bloco a bloco, com o nome do bloco como está na documentação, o que preencher, o texto pronto de cada mensagem e para onde vai cada saída, mais um diagrama.
- **Arquivo .json importável:** só com os blocos cujo formato foi observado num arquivo exportado, escrito por `scripts/gerar_fluxo.py` e conferido por `scripts/validar_fluxo.py`.

Quem usa esta skill costuma ser administrador de uma empresa, sem formação técnica. A resposta final é um passo a passo com o caminho dos menus e o material pronto para colar ou importar.

## O que é de outra skill

| Pedido | Skill |
|---|---|
| Prompt, instruções e configuração do GPT Assistant e de outros recursos de IA | `cmv-agente-ia` (aqui fica só o bloco que leva a conversa até o assistente) |
| Endpoint, corpo, token, webhook, o lado do n8n | `cmv-api` (aqui fica onde chamar no fluxo e o que fazer com a resposta) |
| Texto de template da API Oficial, de campanha, de resposta rápida | `cmv-mensagens` (aqui ficam os textos dos blocos do fluxo) |
| Como configurar conexão, equipe, tags e o resto do painel | `cmv-ajuda` |

Se a outra skill não estiver disponível, entregue a sua parte e diga o que ficou de fora.

## Material desta pasta

| Arquivo | Para quê |
|---|---|
| `references/docs/INDICE.md` e `references/docs/recursos/` | A documentação oficial: 74 artigos (FlowBuilder, blocos, pontos de entrada, Setores & Chatbot). É a única fonte de fatos sobre o produto. O índice traz o link **Fonte** de cada artigo. |
| `references/blocos.md` | Qual bloco usar, as armadilhas e o artigo de cada um, se ele cabe no JSON e em que canal funciona. |
| `references/receitas.md` | Esqueleto dos fluxos mais pedidos e boas práticas de conversa. |
| `references/descricao-compacta.md` | Como descrever o fluxo para o gerador. É o que se lê para gerar um arquivo. |
| `references/formato-json.md` | O formato do arquivo exportado, tipo por tipo. Para diagnosticar um arquivo exportado e para o que o gerador não cobre. |
| `scripts/gerar_fluxo.py` | Descrição compacta → arquivo .json, já validado. `--final`, `--teste`. |
| `scripts/validar_fluxo.py` | Confere a estrutura de qualquer .json de fluxo. `--final`, `--teste`. |
| `assets/descricao-exemplo.json` e `assets/exemplo-minimo.json` | Uma triagem por menu: a descrição compacta e o arquivo que ela gera. |

## Como trabalhar

### 1. Entenda o pedido e pergunte só o que falta

Leia o que a pessoa já disse e pergunte, numa mensagem só, o que falta desta lista e muda o desenho. Quatro ou cinco perguntas bem escolhidas rendem mais do que dez; para o resto, use o padrão da tabela abaixo e diga que usou.

1. **Canal e tipo de conexão** (WhatsApp Oficial, WhatsApp QRCode, Instagram, Facebook, Telegram, canal do HUB): decide blocos e o tipo de menu (passo 2).
2. **Como o fluxo começa:** o cliente escreve, comenta no Instagram, o atendente chama por resposta rápida, uma tag dispara depois de um tempo, uma campanha, um sistema externo, a nota da avaliação (`references/docs/recursos/pontos-de-entrada.md` e os artigos `gatilho-via-…`).
3. **Setores:** quais existem, o nome de cada um e se há gente cadastrada neles.
4. **Tags:** se a empresa já usa, quais o fluxo deve marcar.
5. **Horário:** dias e horas, e o que acontece com quem escreve fora deles.
6. **Quem não responde** e **quem responde algo inválido:** o que fazer.
7. **Quando passa para uma pessoa:** em quais opções, para qual Setor, e o que dizer sobre o tempo de resposta.
8. **Textos:** nome da empresa, tom de voz, respostas que já usam.
9. **Formato:** roteiro ou arquivo para importar.

**Padrões quando a pessoa não diz.** São recomendações desta skill, não regras da plataforma. Declare na entrega cada padrão que usou, para a pessoa poder mudar.

| Decisão | Padrão |
|---|---|
| Tipo de menu | Menu em Lista, com opções de até 20 caracteres |
| Quem não responde ao menu | **Sem resposta** em 30 minutos → Encerrar, avisando que basta mandar nova mensagem. Se o cliente já informou dados, em vez de encerrar: Msg Interna com o que ele disse → Setor |
| Resposta inválida | **Caminho alternativo (ELSE)** marcado → um texto curto de "não entendi" → volta ao mesmo Menu |
| Passagem para a equipe | uma opção "Falar com atendente" no menu principal; antes de cada Setor, um texto avisando da passagem e uma Msg Interna com o que o cliente escolheu |
| Fora do horário | se a pessoa não falou de horário, não ponha bloco de horário: escreva o aviso da passagem sem prometer resposta imediata ("assim que possível, dentro do nosso horário"). Se falou: **Horário de Expediente** antes do menu; na saída **Fora do Horário**, aviso com o horário e bloco **Setor**, onde a conversa fica para a equipe responder na volta. Qual Setor, nos dois blocos (o que dá o horário e o que recebe a conversa): o que a pessoa indicou; se não indicou, não pergunte: cada bloco vai com marcador (linha abaixo) e ela escolhe no editor |
| Setor sem ID informado | marcador `TROCAR: Setor <nome que a pessoa usou>`; sem nome, o papel do Setor, como `TROCAR: Setor que recebe fora do horário` |
| Tags | só se a pessoa já usa tags |
| Entre dois textos seguidos | Intervalo de 2 segundos |

### 2. Desenhe antes de escrever

1. Parta do esqueleto mais próximo em `references/receitas.md`.
2. Para cada bloco, abra o artigo dele (`references/blocos.md` dá o caminho) e confira campos, limites e saídas. Não descreva um campo de memória.
3. Respeite `references/docs/recursos/como-o-fluxo-roda.md` (blocos que esperam, saídas, voltas) e passe o desenho pela lista de armadilhas mais abaixo.
4. **Menu e canal.** O artigo do Menu descreve três tipos (Texto, Lista, Botões) e **não diz em quais canais a lista e os botões chegam como tal**; o que há sobre botões por canal é do bloco Botões, que é outro. Então:
   - No arquivo .json, o menu vai sempre como **Menu em Lista**, o único tipo com formato observado. Menu em Texto e Menu em Botões não podem ser gerados.
   - Diga à pessoa, qualquer que seja o canal, que a documentação não garante a lista naquele canal e que o teste (passo 6) é que mostra. Plano B, sem refazer nada: abrir o Menu no editor e trocar o **Tipo de Menu** para **Menu em Texto**; as opções criadas continuam, e a plataforma numera sozinha.
   - No roteiro de montagem, deixe a pessoa escolher o tipo; se ela não souber, Lista com o mesmo plano B.
   - Para os demais blocos, o quadro "Onde cada bloco funciona" de `references/blocos.md` tem o que os artigos afirmam.
5. **Confirmar antes ou entregar direto?** Conte os pontos de decisão (Menu, Condição, Switch, Horário de Expediente), não os blocos. Um ponto de decisão só, como uma triagem com um menu de qualquer tamanho: entregue direto, com os padrões declarados. Um **Horário de Expediente** na frente desse menu, com a saída **Fora do Horário** no padrão do passo 1 (aviso e Setor), não conta como segundo ponto: triagem por menu com aviso para quem escrever fora do horário também é entrega direta. Dois ou mais, ou algo assumido que muda o caminho: mostre o diagrama, uma linha por caminho, e confirme antes de gerar. Setor ou tag sem ID não muda o caminho: vai com marcador.

### 3. Escolha o formato

| Situação | Entrega |
|---|---|
| Todos os blocos estão em `references/descricao-compacta.md` | .json |
| Faltam poucos blocos de **uma saída só** segundo o artigo (Botões, Template, Oportunidade, Contato, Enviar Localização, Link do Chat Externo) | .json com o tipo `marcador` no lugar de cada um, mais a instrução de troca |
| Falta um bloco cujo artigo **não diz quantas saídas tem** (HTTP Request, Remover Tag, Webview e Carrossel de Produtos) | .json com `marcador`, avisando que as saídas do bloco serão vistas no editor e que todas precisam de ligação; ou roteiro |
| Falta um bloco **com mais de uma saída** (Condição de horário ou de dia, Randomizador, Asaas, PDV…), ou a maior parte do fluxo | roteiro de montagem |
| A pessoa quer aprender a montar, ou vai só ajustar um fluxo que já existe | roteiro de montagem |
| Não há terminal para rodar os scripts | roteiro de montagem |

Na dúvida, roteiro: ele funciona sempre. O .json poupa trabalho, mas o formato dele é observado, não oficial.

### 4. Roteiro de montagem

O nome de cada bloco e de cada campo é o do artigo, em negrito. Todo bloco com mais de uma saída lista **todas** as saídas e o destino de cada uma.

```markdown
## Fluxo: <nome>
**Para que serve:** … **Começa por:** <ponto de entrada>
**Antes de montar:** Setores e tags que precisam existir, horários a cadastrar.

### Diagrama
(Mermaid `flowchart LR`, ou texto com setas; uma linha por saída)

### Montagem
Menu **FlowBuilder Nativo** › **Adicionar Fluxo** › ícone de ferramenta do card. Em cada bloco: botão **+**, escolha o bloco, preencha, **Adicionar**.

1. **Conteúdo** (ligado à saída do **Início**)
   - **Texto:** `Olá! Aqui é o atendimento da …`
   - **Intervalo:** 2 segundos
   - **Texto:** `…`
   - Saída → bloco 2
2. **Menu**: **Tipo de Menu:** Menu em Lista
   - **Texto Principal da Lista:** `…` · **Texto do Botão da Lista:** `Ver opções`
   - Opções: 1 `Comprar` · 2 `Suporte` · 3 `Falar com atendente`
   - **Caminho alternativo (ELSE):** marcado · **Sem resposta:** 30 minutos
   - Saída 1 → bloco 3 · Saída 2 → bloco 5 · **Resposta inválida** → bloco 7 · **Sem resposta** → bloco 8
…

### Conferir e salvar · Testar · Ligar o fluxo   (passo 6)
```

### 5. Arquivo .json

1. Leia `references/descricao-compacta.md` e copie `assets/descricao-exemplo.json` como ponto de partida. Não é preciso ler `references/formato-json.md` para um fluxo comum, nem escrever script próprio.
2. **IDs de Setor e de tag são da conta de cada empresa.** Se a pessoa quiser o arquivo já apontando para os Setores e tags dela, peça os números e diga onde ficam: o **ID** de cada tag, no menu **Tags** (`references/docs/recursos/visao-geral-tags.md`); o número com cerquilha de cada Setor, como *#9*, no card do menu **Setores & Chatbot** (`references/docs/recursos/visao-geral-setores-e-chatbot.md`). Que esses sejam os números que o arquivo guarda é dedução; por isso a entrega sempre manda conferir o nome que aparece no bloco.
3. **Sem os IDs, não pergunte de novo: deixe sem `id`.** O gerador põe o marcador `TROCAR: Setor …`, e a pessoa escolhe o Setor ou a tag em cada bloco marcado, pelo editor. É o caminho mais simples para quem não é técnico.
4. Gere e confira. Grave a descrição e o `.json` na pasta de trabalho da pessoa (o diretório atual, ou a pasta em que o ambiente entrega arquivos), com um nome que diga o que é, como `fluxo-triagem.json`. O `.json` é a entrega: pasta temporária, só para rascunho.
   ```bash
   python3 scripts/gerar_fluxo.py descricao.json fluxo.json           # com marcadores para trocar no editor
   python3 scripts/gerar_fluxo.py descricao.json fluxo.json --final   # quando a pessoa informou todos os IDs
   ```
   Descrição recusada: corrija o que a mensagem aponta. ERROS do validador: corrija a descrição e gere de novo. AVISOS: corrija, ou explique à pessoa por que ficaram.
5. Monte a resposta com o molde abaixo, a partir do que o gerador imprimiu (VALORES A TROCAR, CONFERIR NO EDITOR e, com Horário de Expediente, CONFIGURAR NA EMPRESA), em linguagem de quem não é técnico: nome do bloco e do campo, nunca o ID de 30 caracteres. A resposta começa pela linha **Arquivo:**, sem frase antes.

```markdown
**Arquivo:** <caminho do .json gravado>

**O que este arquivo faz:** <uma frase>.

**Caminho da conversa**
<diagrama curto em texto, uma linha por opção>

**Depois de importar, troque no editor**
| Bloco | O que fazer |
|---|---|
| Setor "TROCAR: Setor Comercial" | duplo clique › escolha o seu Setor de vendas |

**Confira no editor** (só se houver Condição, Horário de Expediente, Execução de Código JS, Switch ou Pergunta)
- <bloco>: <o que deve estar escolhido, ou o que preencher>

**Como importar** (5 passos curtos, do passo 6, sem pular o ícone de ferramenta do card nem o **Resumo do fluxo**)
**Como testar** (3 ou 4 passos, do passo 6: o fluxo no Setor de entrada, a Conexão só para esse Setor, a conversa de teste e uma mensagem a mais depois da passagem)

**Avisos**
- O menu vai em lista; se não chegar bem no seu canal, troque o **Tipo de Menu** para **Menu em Texto**.
- Deixe vazia a **Mensagem de saudação** do Setor do robô.
- (só se houver Horário de Expediente) O arquivo não leva o horário: o bloco usa o da aba **Horários** do Setor escolhido nele, e essa aba só aparece com o **Gerenciamento de Expediente** em **Gerenciamento Por Setor** (menu **Configurações** › **Opções**). Ligar isso vale para a empresa inteira: todos os Setores passam a seguir o horário que já está na aba de cada um; confira a de todos.
- O arquivo segue um formato observado em fluxos exportados, não um formato oficial. Se a importação falhar ou um bloco vier estranho, me avise: entrego o roteiro para montar no editor.
- Padrões que usei: <lista curta>.

**Fonte:** <título e link dos artigos em que os avisos se apoiam>
```

### 6. Importar, conferir, testar, ligar

Escreva estes passos na resposta, adaptados ao caso. Os nomes de tela já estão aqui, com o artigo de origem entre parênteses (todos em `references/docs/recursos/`); abra o artigo só se precisar de um detalhe.

1. **Importar:** menu **FlowBuilder Nativo** › **Importar** › escolha o arquivo. Ele entra como *Fluxo Importado* seguido de um número; renomeie em **Mais opções** (três pontos do card) › **Editar Nome**. O menu só aparece para o administrador (`visao-geral-flowbuilder.md`).
2. **Abrir:** ícone de ferramenta do card. Blocos amontoados: **Organizar automaticamente**, na barra do editor (`como-usar-o-editor-de-fluxos.md`).
3. **Trocar e conferir:** duplo clique no bloco abre a janela **Editar bloco**; escolha o Setor ou a tag e confirme. O artigo não diz o nome do botão que confirma essa janela: escreva "confirme a janela", sem inventar o nome (`como-usar-o-editor-de-fluxos.md`).
4. **Verificar** deve mostrar *Todos conectados!*; **Resumo do fluxo** mostra os avisos de estrutura. Um não substitui o outro (`verificar-e-resumo-do-fluxo.md`).
5. **SALVAR FLUXO**, ou Ctrl+S.
6. **Testar antes de atender clientes.** Fluxo importado não roda enquanto não for ligado a um ponto de entrada, então importar não muda nada para quem está sendo atendido. A documentação não descreve um simulador: o teste é uma conversa de verdade.
   - **Robô novo:** o Setor de teste é o próprio Setor de entrada do robô. Crie esse Setor (menu **Setores & Chatbot**), escolha o fluxo em **Fluxos de Automação**, na aba **Geral**, e deixe a **Mensagem de saudação** vazia (`setor-unico-com-fluxo-automatico.md`).
   - **Como a conversa de teste chega ao Setor, pelo que os artigos sustentam:** uma Conexão apontando **só** para esse Setor (menu **Conexões** › editar a Conexão › aba **Setores & Tempos** › **Setores**). O artigo manda testar "mandando uma mensagem pela Conexão". Se a empresa tem uma conexão que não atende clientes, use-a. Se só tem a de produção, apontar a conexão já é pôr o robô no ar: anote o que está no campo **Setores**, faça a troca num horário de pouco movimento, teste na hora com o seu número e, se algo falhar, volte o campo ao que era.
   - **O número de teste precisa começar um atendimento novo.** Segundo `gatilho-via-conexao.md`, é ao retomar uma conversa encerrada que o atendimento vai para o Setor da Conexão e dispara o fluxo. Se o seu número tem atendimento aberto, encerre antes.
   - **Outros caminhos documentados**, para quem tem apoio técnico: o **Gatilho via API** e os **Webhooks | Triggers** iniciam o fluxo de um Setor para um número (`gatilho-via-api.md`, `gatilho-via-webhooks-trigger.md`; a chamada é da `cmv-api`).
   - **Não documentado:** testar transferindo um atendimento do próprio número para o Setor do robô. O artigo da transferência manda escolher um atendente (`transferir-ticket.md`), e com atendente o atendimento fica em **Atendendo**, enquanto o fluxo atende no **Aguardando** (`como-o-fluxo-roda.md`, `aguardando-x-atendendo.md`). Não proponha esse caminho como certo.
   - **O que percorrer:** cada opção, uma resposta inválida, ficar sem responder até o prazo, e mandar mais uma mensagem depois da passagem para o Setor (armadilha 3).
7. **Ligar** (se o teste já não fez isso): o fluxo no Setor de entrada e a Conexão com **apenas** esse Setor, como no item 6. Outros pontos de entrada: o artigo do gatilho.
8. **Acompanhar:** no card do fluxo, **Ver erros deste fluxo** mostra onde ele tropeçou com clientes de verdade (`erros-do-fluxo.md`).

Quando o fluxo novo substitui um que já atende, não mexa no antigo: importe o novo, teste, e só então troque o fluxo no campo **Fluxos de Automação** do Setor; para voltar atrás, escolha o antigo de novo. Quando a mudança for dentro de um fluxo que já atende, mande usar **Duplicar** antes (**Mais opções** do card) e lembre que **Versões** guarda os salvamentos anteriores (`visao-geral-flowbuilder.md`, `como-usar-o-editor-de-fluxos.md`).

## Armadilhas que a documentação registra

Confira o desenho contra cada uma. Os artigos entre parênteses ficam em `references/docs/recursos/`.

1. **Fluxo salvo não roda sozinho.** Precisa de ponto de entrada. Pela conexão são três amarrações: o fluxo, o fluxo escolhido no Setor, e a Conexão apontando para **um único** Setor; com dois ou mais, quem recebe o cliente é o menu de Setores (`setor-unico-com-fluxo-automatico.md`).
2. **Boas-vindas em dobro.** A **Mensagem de saudação** do Setor de entrada soma com a primeira mensagem do fluxo. Deixe a do Setor vazia. No Setor de comentários do Instagram, ela ainda responde o comentário em público (`gatilho-via-comentario-do-instagram.md`).
3. **Robô que recomeça depois de passar a conversa.** O fluxo de um Setor começa quando chega mensagem do cliente com a conversa naquele Setor (`setor-unico-com-fluxo-automatico.md`), e o artigo da Oportunidade descreve um fluxo rodando de novo a cada mensagem enquanto o atendimento espera no Setor (`bloco-oportunidade.md`). Já o artigo do bloco Setor diz que ele deixa o atendimento esperando a equipe mesmo que o Setor tenha fluxo (`bloco-setor.md`). A documentação não fecha o caso. Por isso: use um Setor de entrada só para o robô e passe a conversa a Setores **sem** o selo **FlowBuilder** no card (`visao-geral-setores-e-chatbot.md`). **No teste, observe:** depois da mensagem de passagem, mande mais uma mensagem. Se as boas-vindas ou o menu voltarem, o Setor de destino tem fluxo ligado (ou é o próprio Setor do robô): troque o destino por um Setor sem fluxo, ou tire o fluxo dele em **Fluxos de Automação**.
4. **Saída sem ligação para a conversa** (`como-o-fluxo-roda.md`). Os artigos dos blocos dizem quais: **Falso** da Condição (`bloco-condicao.md`), **Nenhuma condição atendida** do Switch (`bloco-switch-tags.md`), **Resposta inválida** e **Sem resposta** do Menu (`bloco-menu.md`), **Erro** do Asaas (`bloco-asaas.md`), **Não elegível** do Pixel META (`bloco-pixel-meta.md`), as duas do Randomizador (`bloco-randomizador.md`).
5. **Bloco que espera sem "Sem resposta" espera para sempre.** Preencha o campo no Menu, na Pergunta, nos Botões e na Avaliação, e ligue a saída (`como-o-fluxo-roda.md`).
6. **Variável longe da fonte perde o dado.** Ela vem logo depois da Pergunta, do Menu ou da Execução de Código JS; no meio, só um Intervalo (`bloco-variavel.md`).
7. **`{{firstName}}` e `%nome%` não são a mesma coisa.** Chaves para dados do contato, porcentagens para variáveis do fluxo. Variável usada antes de ser guardada aparece escrita para o cliente (`bloco-variavel.md`).
8. **Voltar sem esperar interrompe o fluxo.** O caminho de volta tem de passar por um Menu ou uma Pergunta; senão é ciclo sem espera (`bloco-pular-para.md`).
9. **Menu:** em texto, a plataforma numera sozinha; em lista e botões, opção com até 20 caracteres; em botões, no máximo 3 (`bloco-menu.md`).
10. **Condição de texto:** **Igual** compara a resposta inteira e o acento conta; lista com vírgula só no **Contém** (`bloco-condicao.md`).
11. **Setor, Trocar Fluxo e Tag são coisas diferentes.** Setor deixa a conversa esperando a equipe; Trocar Fluxo inicia o fluxo de outro Setor; Tag só marca (`bloco-setor.md`, `bloco-trocar-fluxo.md`, `bloco-tags.md`).
12. **Fluxo iniciado pela empresa:** em remarketing, campanha e resposta rápida, alguns blocos só funcionam no **Aguardando**, e o remarketing pode atropelar uma conversa com atendente. Fluxo de resposta rápida termina em **Encerrar Mensagem Rápida** (`gatilho-via-remarketing-de-tag.md`, `gatilho-via-resposta-rapida.md`).
13. **Horário de Expediente depende de configuração da empresa.** Ligar o **Gerenciamento Por Setor** faz todos os Setores seguirem o horário que já está na aba de cada um (`aba-horarios-em-setores-e-chatbot.md`).
14. **Salvar não muda a conversa em andamento.** Quem já entrou segue na versão anterior até o atendimento encerrar (`como-o-fluxo-roda.md`). **Restaurar** uma versão grava na hora (`como-usar-o-editor-de-fluxos.md`).

## Exemplos de pedido e entrega

**"Quero um robô no WhatsApp por QR Code que pergunte se é compra ou suporte e mande pro setor certo. Me manda o arquivo pronto."**
Um ponto de decisão só: entregue direto, sem rodada de perguntas, com os padrões declarados. Descrição compacta igual à de `assets/descricao-exemplo.json`: Início → Conteúdo → Menu em Lista (as opções, mais "Falar com atendente"; resposta inválida; sem resposta em 30 minutos) → em cada ramo, aviso, Msg Interna e Setor com marcador; sem Tag. Rode o gerador e responda com o molde do passo 5, incluindo o aviso de que a documentação não diz como a lista chega na conexão por QR Code e o plano B de trocar para Menu em Texto.

**"Meu fluxo para de responder depois que o cliente escolhe a opção 2."**
Não gere fluxo novo. Entregue o diagnóstico em passos: abrir o fluxo, **Verificar**, olhar a lista **Sem conexão de saída (o fluxo para neste bloco)**; conferir o bloco ligado à opção 2 e as saídas dele; **Ver erros deste fluxo** com o nível **Parou o fluxo**. Cite *Verificar e Resumo do Fluxo* e *Erros do Fluxo*. Com o arquivo de **Exportar Fluxo** em mãos, a ordem é: (1) rode `scripts/validar_fluxo.py` nele, sempre; (2) aponte o bloco pelo nome e pelo começo do texto, sem ID nem nome interno de saída; (3) mande corrigir no fluxo que já está no painel (ícone de ferramenta do card, ligar a saída solta, **Verificar**, **SALVAR FLUXO**), e não reimportar: arquivo importado entra como *Fluxo Importado* novo, que não roda enquanto não for ligado a um ponto de entrada, e a correção cairia na cópia; (4) feche com a Fonte, título e link. O resultado do validador é para você: na resposta, diga o que o arquivo mostra ("a opção 2 do Menu está sem ligação"), sem citar validador, script nem "REPROVADO", e não ofereça um arquivo corrigido para importar.

**"Preciso mandar mensagem um dia depois pra quem pediu orçamento e não fechou. Uso a API Oficial."**
Dois pontos de decisão e um gatilho que não é a conexão: confirme o desenho antes. Entregue o roteiro: a tag e a aba **Remarketing** dela (fluxo, prazo, Setor do atendimento reaberto); Menu com **Sem resposta**; Remover Tag; passagem ao Setor. Avise que o remarketing pode disparar no meio de uma conversa com atendente. Sobre a primeira mensagem, diga o que é dedução: o artigo do Template afirma que ele é o único jeito de o fluxo falar com quem não escreveu nas últimas 24 horas (`references/docs/recursos/bloco-template.md`), o artigo do remarketing não trata do assunto, então o provável é começar por um bloco **Template**, cobrado pela Meta a cada envio; mande testar. O texto do template é da `cmv-mensagens`.

## Como consultar a documentação

- Ache o artigo pelo índice (`references/docs/INDICE.md`) ou por busca: `grep -il 'sem resposta' references/docs/recursos/*.md`. Sem terminal, leia o índice e abra o artigo pelo nome.
- Leia só o artigo de que precisa, e responda com base nele. As imagens e os vídeos não foram transcritos: não deduza o que só aparece neles.
- Ao afirmar algo sobre o produto, cite o artigo pelo título e pelo link da linha **Fonte** (está no cabeçalho do artigo e no índice). O nome do arquivo (`bloco-menu.md`) não vai na resposta, porque a pessoa não tem esses arquivos; o link de cada artigo é `https://clihelper.chatmasterveloz.com/docs/` seguido do nome do arquivo sem `.md`.
- Não leve para um canal o que o artigo afirma sobre outro, nem para um bloco o que o artigo afirma sobre outro bloco.
- Separe na resposta o que é do artigo, o que é dedução e o que é recomendação desta skill. Se a documentação não cobre o que a pessoa perguntou, diga isso com clareza; não cite preço nem plano. O que esta skill sabe do arquivo .json vem de observação, e deve ser apresentado assim.
