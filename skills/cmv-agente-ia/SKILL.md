---
name: cmv-agente-ia
description: "Use para o atendente de IA que roda dentro do atendimento do Chat Master Veloz (CMV, chatmasterveloz), o GPT Assistant do menu Prompts OPEN.AI. Use quando a pessoa quiser colocar IA ou \"o ChatGPT\" para responder clientes no WhatsApp ou no painel, pedir o prompt pronto para colar (com os comandos de transferir, tag e encerrar), o passo a passo da configuração e os testes, ou consertar uma IA do CMV que inventa, não transfere ou gasta demais. Também vale para os outros recursos de IA do painel: Token OpenAI, transcrição de áudio, Análise de Atendimento, Avaliação pela IA, Copiloto, Sugestão de resposta IA e GPT em grupos. Não use para GPTs personalizados criados no próprio site ou app do ChatGPT, para a API da OpenAI em código próprio nem para bots de outras plataformas. Fluxos do FlowBuilder ficam com a cmv-flowbuilder, API e webhooks com a cmv-api, textos de campanha e respostas rápidas com a cmv-mensagens e as outras dúvidas do painel com a cmv-ajuda."
---

# Agente de IA no Chat Master Veloz

Esta skill serve a quem quer um atendente de IA dentro do Chat Master Veloz (CMV) para tirar dúvidas, qualificar lead, agendar, vender ou dar suporte, e a quem tem dúvida sobre os demais recursos de IA do painel. Quem pede costuma ser dono ou gestor, sem formação técnica, e escreve pouco. A resposta tem de ser proporcional: curta quando a pessoa escreveu duas linhas, completa quando ela já trouxe os dados.

## Comece por aqui: que pedido é este

Leia só os arquivos do caso. O material é extenso, e ler tudo antes de responder atrasa e dilui a resposta.

| Pedido | O que fazer | Leia |
|---|---|---|
| Criar um atendente, e a pessoa só disse o ramo e o objetivo | Etapa 1: resposta curta com perguntas | Só a seção "Primeira rodada" de `references/entrevista-briefing.md`; os fatos e as fontes da resposta já estão na Etapa 1, abaixo |
| Criar um atendente, e os dados do negócio já estão na conversa | Etapa 2: prompt e configuração | `assets/modelo-prompt.md`; `references/comandos-e-capacidades.md`, seções 3 a 7; `references/configuracao-painel.md`; a seção final ("O que entendi") de `references/entrevista-briefing.md` |
| O prompt definitivo, sem marcadores, já está no painel | Etapa 3: plano de testes | `assets/plano-de-testes.md` |
| Consertar uma IA que já existe | Triagem e correção pontual | `references/configuracao-painel.md`, "Quando algo não funciona"; `assets/plano-de-testes.md`, "Do resultado ao ajuste"; a seção de `references/comandos-e-capacidades.md` que tratar do sintoma |
| Dúvida sobre outro recurso de IA | Resposta curta com base no artigo | O artigo do recurso (tabela "Outros recursos de IA") e as atualizações que o citam |

## Regras de base

Todo fato sobre o produto (nome de menu, botão, campo, comando, limite) precisa estar em `references/docs/`, a cópia da Central de Ajuda. Um nome de menu inventado faz a pessoa procurar o que não existe; um comando inventado faz a IA "transferir" sem que nada aconteça no painel.

- **Ache o artigo** pelo índice `references/docs/INDICE.md` ou por busca: `grep -rn -i 'transbordo' references/docs`. Sem terminal, leia o índice e abra o artigo pelo título. Os resumos em `references/` ajudam a achar, mas o artigo é a fonte: confira nele antes de escrever um nome de menu ou de campo.
- **Cite o artigo**: título e o link da linha **Fonte** do cabeçalho (o índice traz o link de cada artigo). Exemplo: "Fonte: Tipo Prompt, https://clihelper.chatmasterveloz.com/docs/tipo-prompt".
- **Confira as atualizações do recurso antes de responder.** Os arquivos `references/docs/recursos/atualizacoes-2026-*.md` são as notas de versão, e há fatos de IA que só estão nelas ou que mudaram depois do artigo. Busque pelo nome do recurso, não por termo genérico: `grep -n -i 'comandos da ia' references/docs/recursos/atualizacoes-2026-*.md` (ou "agente openai", "avaliação pela ia", "sugestão de resposta", "transcrever áudio", "token"). Sem terminal, abra as atualizações pelo índice, da mais recente para a mais antiga. Quando artigo e atualização divergirem, diga as duas coisas, cada uma com a sua fonte, trate a atualização como a mais recente e não descreva a tela além do que os dois textos dizem: peça à pessoa que conte o que está vendo.
- **Três rótulos, sempre visíveis para a pessoa:** o que está documentado; o que é recomendação ou inferência desta skill; o que não está documentado. `references/comandos-e-capacidades.md` já separa os três.
- **Imagens e vídeos** dos artigos não foram transcritos: não descreva posição de botão, cor ou ícone.
- **Não cite preços nem planos.** A documentação só diz que há recursos que dependem do plano e que o consumo é cobrado pela OpenAI.
- **Canais:** os artigos de IA não trazem etiqueta de tipo de conexão (`[Básica]`, `[Pro]`, `[Oficial]`, `[Hub]`, `[Webchat]`). Não afirme que o GPT Assistant funciona, ou deixa de funcionar, em um canal específico. O que dá para dizer é que o painel tem o recurso e que o assistente responde aos atendimentos do Setor em que for ligado (`references/docs/recursos/tipo-prompt.md`); se isso vale para o canal da pessoa, o primeiro teste mostra. No prompt, o canal é um marcador: serve para a IA ajustar o jeito de escrever, não é afirmação sobre a plataforma.
- **Nunca peça o token da OpenAI.** Ele dá acesso à conta e à parte financeira dela (`references/docs/recursos/token-openai.md`); se a pessoa colar, recomende gerar outro.

## Criar um atendente de IA, em etapas

A entrega completa tem prompt, passo a passo no painel, plano de testes e limites e custos. Ela é feita em etapas, porque despejar centenas de linhas em quem escreveu duas faz a pessoa desistir. Se ela pedir tudo de uma vez, entregue tudo.

### Etapa 1: primeira resposta, curta

Vale quando a pessoa só disse o ramo e o objetivo. Em até umas vinte linhas. Os fatos e as fontes desta seção já foram conferidos nos artigos e nas atualizações incluídas: nesta etapa, o único arquivo a abrir é a "Primeira rodada", e a busca nas atualizações está dispensada.

1. Diga que o painel tem o recurso e como ele se chama: GPT Assistant, criado no menu **Prompts OPEN.AI**, que responde aos atendimentos do Setor em que for ligado. Não prometa um canal específico (regra "Canais").
2. Liste os três pré-requisitos, em uma linha cada: a opção de IA ativada pelo suporte do Chat Master Veloz, um token criado na OpenAI e esse token colado no menu **Integrações**. Acrescente que o menu **Prompts OPEN.AI** só aparece para o perfil Administrador.
3. Faça as cinco ou seis perguntas da "Primeira rodada" de `references/entrevista-briefing.md`, adaptadas ao ramo.
4. Ofereça a alternativa: "Se preferir, já te mando um rascunho com as lacunas marcadas para você completar."
5. Se o pedido incluir agendamento, diga o limite em uma frase: a IA anota os dados e a preferência de dia e horário, e a equipe confirma. O motivo, para dizer à pessoa: o comando de agenda da IA só aparece em uma nota de atualização, que não explica se ele confere horário livre nem o que faz quando dois clientes pedem o mesmo horário.
6. Cite as fontes no fim, título e link:
   - * Pré-Requisitos IA: https://clihelper.chatmasterveloz.com/docs/pre-requisitos-ia
   - Token OpenAI: https://clihelper.chatmasterveloz.com/docs/token-openai
   - Tipos de Perfil: https://clihelper.chatmasterveloz.com/docs/tipos-de-perfil
   - 11/11/2026 (só se falar de agendamento): https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-11-11

Não entregue ainda prompt, passo a passo nem plano de testes. Não espere os pré-requisitos ficarem prontos para seguir: eles viram a primeira parte do passo a passo.

### Etapa 2: prompt e configuração

Vale quando há respostas, ou quando a pessoa pediu com todas as letras um rascunho para ir preenchendo. "Cria o prompt" só com o ramo e o objetivo ainda é Etapa 1: as perguntas vêm antes, porque rascunho cheio de marcadores não serve para colar. A resposta começa por "O que entendi"; o relato de que o arquivo foi salvo ou de que a conferência passou não abre a resposta.

1. Abra com "o que entendi", em cinco ou seis linhas (modelo no fim de `references/entrevista-briefing.md`).
2. Escreva o prompt a partir de `assets/modelo-prompt.md`:
   - comandos só os documentados, na forma exata do artigo (`references/comandos-e-capacidades.md`, seção 3);
   - o que a pessoa não informou fica como marcador `[[...]]`, nunca como dado de exemplo; com marcadores, chame de rascunho;
   - sem variáveis `{{...}}` e sem regra que dependa da hora atual: nada disso está documentado para o campo **Prompt**;
   - só os comandos que o objetivo pede; cada comando a mais é um ponto a testar.
3. Confira com `python3 scripts/conferir_prompt.py arquivo.txt` (modo rascunho: marcador é pendência e não reprova). Ordem única: os marcadores de dados do negócio são preenchidos antes de colar; o prompt pode ir ao painel levando só marcadores de ID de comando (e o do comando de agenda), que se trocam lá, pela janela **Comandos da IA**; o `--final` roda na versão definitiva, que é a que a pessoa devolve depois do **Inserir no prompt** ou a que você monta quando ela informa os IDs, antes dos testes. Sem terminal, use a lista do fim de `assets/modelo-prompt.md`.
4. Entregue o prompt em bloco de código e a tabela "o que falta preencher e onde achar". Para o ID do Setor, que não tem tela documentada, o caminho é a janela **Comandos da IA** (`references/configuracao-painel.md`, etapa 5).
5. Dê o passo a passo do painel seguindo `references/configuracao-painel.md`, etapas 1 a 7: um passo por linha, caminho de menu em negrito, valor de cada campo, pulando o que a pessoa já fez. Apontar a Conexão para o Setor da IA (etapa 9) fica para depois dos testes; a entrega diz isso em uma linha: "O último passo, fazer os clientes chegarem à IA pela Conexão, fica para depois dos testes."
6. Feche com limites e custos em três ou quatro linhas (seção "Limites e custos" do mesmo arquivo) e com o convite: "Quando o prompt estiver no painel, com os IDs inseridos, cole aqui o texto final: eu confiro e mando o roteiro de testes."

Tamanho: fora o bloco do prompt, a resposta fica em cerca de quarenta linhas. Para caber, corte nesta ordem: as etapas que a pessoa já fez; os porquês de cada campo (fica só o valor); os itens opcionais (voz, grupo); a tabela de diagnóstico, que só entra quando algo falha; e, por último, reduza as fontes aos três ou quatro artigos principais.

### Etapa 3: plano de testes

Vale quando o prompt definitivo, sem marcadores, está no painel. Use `assets/plano-de-testes.md`: explique como levar a conversa de teste ao Setor da IA sem mexer na Conexão, escreva as falas com o vocabulário do negócio e inclua sempre pedido de humano, pergunta fora do escopo, tentativa de mudar as instruções e um cenário por comando. A tabela de cenários do plano é o esqueleto, não a entrega: entregue as mensagens do cliente escritas uma a uma, prontas para enviar. Se o prompt não está na conversa, escreva com `[...]` onde entra o negócio e peça o prompt para personalizar. Prefira poucas conversas bem escolhidas a uma lista longa: roteiro grande demais não é seguido.

### Formato de cada entrega

```markdown
(Etapa 2)
O que entendi: ...
## Prompt para colar            (bloco de código; "rascunho" se houver marcadores)
## O que falta preencher        (tabela, se houver marcadores)
## Passo a passo no painel      (numerado, com caminho de menu)
## Limites e custos             (só o documentado)
## O que presumi e o que não está documentado
Fontes: título e link de cada artigo usado

(Etapa 3)
## Como chegar ao Setor da IA para testar
## Conversas de teste           (mensagem do cliente, esperado na conversa, esperado no painel)
## Se algo sair diferente       (onde mexer)
## Fontes                        (título e link de cada artigo citado)
```

## Consertar uma IA que já existe

Peça o prompt atual, os valores dos campos e um trecho de conversa em que o problema aparece. Separe a causa antes de reescrever: problema de **configuração** (Setor, status, token, temperatura, tokens, histórico) se resolve no painel; problema de **texto** (inventa, sai do escopo, não segue o roteiro) se resolve no prompt. Devolva só o trecho corrigido, o que conferir no painel e quais cenários repetir. Mude uma coisa por vez.

## Outros recursos de IA

Respostas curtas, com base no artigo e nas atualizações que o citam.

| Recurso | O que é | Onde fica | Artigo |
|---|---|---|---|
| Transcrever Áudios | Transforma em texto uma mensagem de áudio. | Na mensagem de áudio, seta superior direita › **Transcrever Áudio**. | `references/docs/recursos/transcrever-audios.md` |
| Análise de Atendimento | Avalia um atendimento: objeções, pontos de melhoria, sentimento geral e KPIs. O resultado é visível só na plataforma. | No chat, ações do Ticket › **Analisar Atendimento com IA**. | `references/docs/recursos/analise-de-atendimento.md` |
| Avaliação pela IA | Dá nota de 0 a 10 aos atendimentos encerrados, gera relatório para a gestão e aulas para cada atendente. Nada vai ao cliente. Depende do plano. | Liga em **Configurações › Opções** (só administrador); resultados no menu **Avaliação pela IA**, que também aparece para Supervisor e Atendente. | `references/docs/recursos/avaliacao-pela-ia.md` |
| Copiloto de mensagens | Botão que sugere a próxima resposta ou melhora o texto digitado; nunca envia sozinho. Depende do plano e consome créditos de IA. | Na conversa, botão ✨ ao lado do **+**. | `references/docs/outros/copiloto-de-mensagens.md` |
| Sugestão de resposta IA | Tela que governa o Copiloto: instruções das duas funções, **Modelo**, **Mensagens de contexto** (1 a 50) e **Extrato de tokens**. | Menu **Sugestão de resposta IA** (só administrador). | `references/docs/outros/sugestao-de-resposta-ia.md` |
| GPT Assistant em Grupos | O assistente responde em um grupo quando chamado por um gatilho que começa com `!`. | Campo **Gatilho para Grupo** do prompt e **Editar Contato do Grupo**. | `references/docs/recursos/gpt-assistant-em-grupos.md` |
| Token OpenAI | A chave que alimenta os recursos de IA; o consumo é cobrado na conta dona dela. | Menu **Integrações**, card **OPEN.AI**. | `references/docs/recursos/token-openai.md` |
| Assistente de IA (menu) | Responde a perguntas da equipe sobre atendimentos, contatos, oportunidades e tarefas. Só consulta. | Menu **Assistente de IA**. | `references/docs/recursos/atualizacoes-2026-11-11.md` |
| IA nas gravações das chamadas | Transcreve, legenda e analisa as gravações das chamadas. Usa o **Token OpenAI**. | Liga em **Configurações › Opções**, opção **IA nas gravações das chamadas**; resultado na página **Gravações**. | `references/docs/recursos/gravacoes-das-chamadas.md` |

Se pedirem para "dar a cara da empresa" ao Copiloto, escreva os dois textos da tela **Sugestão de resposta IA** (**Instruções para sugerir a resposta** e **Instruções para melhorar o texto**) com o tom e os limites da empresa. Mantenha a regra de não inventar preço, prazo, endereço ou política: o artigo avisa que é ela que impede a IA de prometer o que a empresa não cumpre. Lembre a pessoa de clicar em **SALVAR**.

## Armadilhas

Cada uma está explicada por inteiro em um só lugar; aqui fica o lembrete.

- **Forma do código e aspas curvas; turno da tag:** `references/comandos-e-capacidades.md`, seção 3.
- **Agente OpenAI desligado:** seção 1 do mesmo arquivo.
- **Janela Comandos da IA, comando de agenda e ID do Setor:** seções 4 e 5; roteiro em `references/configuracao-painel.md`, etapa 5.
- **Quando a IA atua, dois Setores, dois motores no mesmo Setor, primeira mensagem:** seção 6.
- **Transbordo e comando de transferir ao mesmo tempo:** seção 7.
- **Nomes que mudaram.** O campo **GPT Model** virou **Modelo da IA**; o menu aparece como "Prompts Open.Ai" em um artigo e **Prompts OPEN.AI** nos outros. Cite os dois nomes para a pessoa reconhecer o que vê.
- **Nomes parecidos.** GPT Assistant (atende o cliente), **Assistente de IA** (menu de consultas da equipe), Análise de Atendimento (um atendimento, sob demanda), Avaliação pela IA (rodadas automáticas com nota) e a pesquisa de avaliação respondida pelo cliente são cinco coisas diferentes.
- **Créditos do Copiloto e conta da OpenAI.** O saldo de créditos é da plataforma; mesmo com **ILIMITADO**, o consumo continua cobrado na conta da OpenAI (`references/docs/outros/copiloto-de-mensagens.md`).
- **Avaliação pela IA mudou depois do artigo.** As atualizações de 07/11 e 11/11/2026 trazem o que há de novo (abas **Hoje** e **Evolução**, processo ideal de atendimento, rodar só quando ligada).
- **Token escondido.** Desde 10/11/2026 o token aparece escondido no card **OPEN.AI**, com o olho **Mostrar a chave**.

## Limites com as skills vizinhas

| O pedido é... | Skill |
|---|---|
| Desenhar ou gerar o fluxo do FlowBuilder (menus, condições, onde entra o bloco da IA) | `cmv-flowbuilder`. Aqui só se explica o que o bloco **GPT Assistant (OpenAI)** faz e se escreve o prompt do assistente que ele chama. |
| Integrar por API REST, webhook ou n8n (inclusive o webhook da Avaliação pela IA e a listagem de Setores) | `cmv-api` |
| Redigir respostas rápidas, templates da API Oficial, campanhas | `cmv-mensagens` |
| Usar o painel em geral: Setores em detalhe, conexões, equipe, chamadas, erros que não são de IA | `cmv-ajuda` |
| Mudar a aparência ou o comportamento do painel com CSS e JS | `cmv-painel-css-js` |

Quando o pedido mistura os dois lados ("quero um fluxo com menu e IA no final"), faça a parte de IA por inteiro e diga qual skill cuida do resto.

## Exemplos de pedido e entrega

**"oi, tenho uma clínica de estética e queria colocar o chatgpt pra responder o whatsapp, tirar dúvida de preço e já deixar a avaliação agendada. como faço?"**
Etapa 1. Resposta de umas vinte linhas: dá para fazer; os três pré-requisitos; seis perguntas (nome e serviços, o que pode informar e quais preços, o que não pode dizer, quando passar para uma pessoa e para qual equipe, que dados a recepção precisa para a avaliação e quem confirma o horário, o que já está pronto); a frase sobre agendamento (a IA anota a preferência e a equipe confirma); a oferta do rascunho.

**A mesma pessoa responde às perguntas.**
Etapa 2: "o que entendi", prompt com a variante A de agendamento e um só comando, o de transferir para a recepção (o objetivo não pede tag), tabela do que falta (o ID do Setor da recepção), passo a passo do painel até a saudação do Setor, a linha sobre a Conexão ficar para depois dos testes, limites e custos, e o convite para o roteiro de testes.

**"Minha IA não transfere pro atendente quando o cliente pede."**
Peça o prompt e os campos de **Transbordo**. Confira o código contra a forma do artigo, a regra de manter o código, o Setor de destino e se há atendentes nele. Devolva o trecho corrigido, o que conferir no painel e os cenários de pedido de humano para repetir três vezes.

**"O que é esse Avaliação pela IA que apareceu no menu?"**
Resposta curta com base no artigo e nas atualizações de 07/11 e 11/11/2026: o que faz, quem vê o quê, onde liga, que depende do plano e que nada vai ao cliente. Link da Fonte no fim.
