---
name: cmv-agente-ia
description: "Use para o atendente de IA do Chat Master Veloz (CMV, chatmasterveloz), o GPT Assistant do menu Prompts OPEN.AI. Use quando a pessoa quiser colocar IA ou \"o ChatGPT\" para responder clientes no WhatsApp, pedir o prompt pronto (com comandos de transferir, tag, agenda e CRM), configurar, testar ou consertar IA que inventa, não transfere ou gasta demais. Vale também para outros recursos de IA: Provedor de IA, Token OpenAI, Base de Conhecimento, transcrição de áudio, Análise de Atendimento, Avaliação pela IA (Processo ideal), Copiloto, Sugestão de resposta IA e GPT em grupos. Quem tem esta skill usa o CMV: pedido sobre IA ou assistente do atendimento (prompt, comandos, base, avaliação) sem citar outra ferramenta é dela, mesmo sem citar o CMV; carregue-a antes de responder. Não use para GPTs feitos no site ou app do ChatGPT, código próprio na API da OpenAI nem bots de outras plataformas. Fluxos: cmv-flowbuilder; API e webhooks: cmv-api; textos para clientes: cmv-mensagens; resto do painel: cmv-ajuda."
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
| Recurso de IA que não aparece, de quem é a chave da OpenAI, créditos do Copiloto, ou revendedor perguntando como liberar | Resposta curta, conforme o público (regra "Dois públicos") | `references/configuracao-painel.md`, "O que libera cada recurso de IA"; para o revendedor, também o artigo de `references/docs/revendedor/recursos/` |

## Regras de base

Todo fato sobre o produto (nome de menu, botão, campo, comando, limite) precisa estar em `references/docs/`: a cópia da Central de Ajuda e, na pasta `revendedor/`, os artigos da documentação do revendedor sobre IA (plano, chave e créditos). Um nome de menu inventado faz a pessoa procurar o que não existe; um comando inventado faz a IA "transferir" sem que nada aconteça no painel.

- **Ache o artigo** pelo índice `references/docs/INDICE.md` ou por busca: `grep -rn -i 'transbordo' references/docs`. Sem terminal, leia o índice e abra o artigo pelo título. Os resumos em `references/` ajudam a achar, mas o artigo é a fonte: confira nele antes de escrever um nome de menu ou de campo.
- **Cite o artigo**: título e o link da linha **Fonte** do cabeçalho (o índice traz o link de cada artigo). Exemplo: "Fonte: Tipo Prompt, https://clihelper.chatmasterveloz.com/docs/tipo-prompt".
- **Confira as atualizações do recurso antes de responder.** Os arquivos `references/docs/recursos/atualizacoes-2026-*.md` são as notas de versão, e há fatos de IA que só estão nelas ou que mudaram depois do artigo. Busque pelo nome do recurso, não por termo genérico: `grep -n -i 'comandos da ia' references/docs/recursos/atualizacoes-2026-*.md` (ou "agente openai", "avaliação pela ia", "sugestão de resposta", "transcrever áudio", "token"). Sem terminal, abra as atualizações pelo índice, da mais recente para a mais antiga. Quando artigo e atualização divergirem, diga as duas coisas, cada uma com a sua fonte, trate a atualização como a mais recente e não descreva a tela além do que os dois textos dizem: peça à pessoa que conte o que está vendo.
- **Três rótulos, sempre visíveis para a pessoa:** o que está documentado; o que é recomendação ou inferência desta skill; o que não está documentado. `references/comandos-e-capacidades.md` já separa os três.
- **Imagens e vídeos** dos artigos não foram transcritos: não descreva posição de botão, cor ou ícone.
- **Não cite preços.** A documentação não traz valores; só diz que o consumo é cobrado pela OpenAI, na conta dona da chave em uso. Os nomes das opções de plano que liberam os recursos de IA estão documentados e podem ser citados, com o nome literal: **AI**, **GPT Assistant**, **GPT Análises**, **Sugestão de resposta IA**, **Provedores de IA**, **Avaliação pela IA** e **Copilot CRM** (`references/docs/revendedor/recursos/configuracoes-planos.md`).
- **Dois públicos.** O padrão é o cliente, administrador de uma empresa: ele não tem as telas **Configurações › Planos**, **Empresas** e **Tokens de IA**. Quando um recurso de IA não aparece para ele, diga o nome da opção de plano que o libera e que quem liga é quem fornece a plataforma (o suporte); não o mande a essas telas nem cite o site do revendedor. O revendedor (Super Admin, dono da instância) se reconhece porque diz que é ou fala em "meus clientes", "liberar para a empresa", plano, instância, chave da plataforma, créditos das empresas: para ele, responda com os artigos de `references/docs/revendedor/recursos/` e cite o título e o link da linha **Fonte** deles. Se a resposta muda conforme o público e não dá para saber quem é, dê a do cliente e acrescente uma linha para quem administra a instância.
- **Canais:** os artigos de IA não trazem etiqueta de tipo de conexão (`[Básica]`, `[Pro]`, `[Oficial]`, `[Hub]`, `[Webchat]`). Não afirme que o GPT Assistant funciona, ou deixa de funcionar, em um canal específico. O que dá para dizer é que o painel tem o recurso e que o assistente responde aos atendimentos do Setor em que for ligado (`references/docs/recursos/tipo-prompt.md`); se isso vale para o canal da pessoa, o primeiro teste mostra. No prompt, o canal é um marcador: serve para a IA ajustar o jeito de escrever, não é afirmação sobre a plataforma.
- **Nunca peça o token da OpenAI.** Ele dá acesso à conta e à parte financeira dela (`references/docs/recursos/token-openai.md`); se a pessoa colar, recomende gerar outro.

## Criar um atendente de IA, em etapas

A entrega completa tem prompt, passo a passo no painel, plano de testes e limites e custos. Ela é feita em etapas, porque despejar centenas de linhas em quem escreveu duas faz a pessoa desistir. Se ela pedir tudo de uma vez, entregue tudo.

### Etapa 1: primeira resposta, curta

Vale quando a pessoa só disse o ramo e o objetivo. Em até umas vinte linhas. Os fatos e as fontes desta seção já foram conferidos nos artigos e nas atualizações incluídas: nesta etapa, o único arquivo a abrir é a "Primeira rodada", e a busca nas atualizações está dispensada.

1. Diga que o painel tem o recurso e como ele se chama: GPT Assistant, criado no menu **Prompts OPEN.AI**, que responde aos atendimentos do Setor em que for ligado. Não prometa um canal específico (regra "Canais").
2. Liste os pré-requisitos, em uma linha cada: um token criado na OpenAI, colado no campo **Token OpenAI** do card **OPEN.AI**, no menu **Integrações** (se o card avisar que a conta usa a chave da plataforma, não há chave a cadastrar); e o perfil Administrador, o único que vê o menu **Prompts OPEN.AI**. Se o menu não aparecer para o Administrador, o que o libera é a opção de plano **GPT Assistant**, que precisa também da **AI**: quem liga as duas é quem fornece a plataforma (o suporte do Chat Master Veloz).
3. Faça as cinco ou seis perguntas da "Primeira rodada" de `references/entrevista-briefing.md`, adaptadas ao ramo.
4. Ofereça a alternativa: "Se preferir, já te mando um rascunho com as lacunas marcadas para você completar."
5. Se o pedido incluir agendamento, diga as duas formas em uma frase: a IA anota os dados e a preferência de dia e horário e a equipe confirma, ou a IA marca pelo comando **Marcar ou desmarcar na agenda**, que confirma o dia e a hora com o cliente e confere se o horário está livre antes de marcar.
6. Cite as fontes no fim, título e link:
   - * Pré-Requisitos IA: https://clihelper.chatmasterveloz.com/docs/pre-requisitos-ia
   - Token OpenAI: https://clihelper.chatmasterveloz.com/docs/token-openai
   - Tipos de Perfil: https://clihelper.chatmasterveloz.com/docs/tipos-de-perfil
   - Comandos GPT Assistant (só se falar de agendamento): https://clihelper.chatmasterveloz.com/docs/comandos-gpt-assistant

Não entregue ainda prompt, passo a passo nem plano de testes. Não espere os pré-requisitos ficarem prontos para seguir: eles viram a primeira parte do passo a passo.

### Etapa 2: prompt e configuração

Vale quando há respostas, ou quando a pessoa pediu com todas as letras um rascunho para ir preenchendo. "Cria o prompt" só com o ramo e o objetivo ainda é Etapa 1: as perguntas vêm antes, porque rascunho cheio de marcadores não serve para colar. A resposta começa por "O que entendi"; o relato de que o arquivo foi salvo ou de que a conferência passou não abre a resposta.

1. Abra com "o que entendi", em cinco ou seis linhas (modelo no fim de `references/entrevista-briefing.md`).
2. Escreva o prompt a partir de `assets/modelo-prompt.md`:
   - comandos só os documentados, cada um como marcador a trocar pela janela **COMANDOS DA IA**, com o texto de **Quando a IA deve fazer isso** já escrito (`references/comandos-e-capacidades.md`, seção 3);
   - o que a pessoa não informou fica como marcador `[[...]]`, nunca como dado de exemplo; com marcadores, chame de rascunho;
   - sem variáveis `{{...}}` e sem regra que dependa da hora atual: nada disso está documentado para o campo **Prompt**;
   - só os comandos que o objetivo pede; cada comando a mais é um ponto a testar.
3. Confira com `python3 scripts/conferir_prompt.py arquivo.txt` (modo rascunho: marcador é pendência e não reprova). Ordem única: os marcadores de dados do negócio são preenchidos antes de colar; o prompt pode ir ao painel levando só os marcadores de comando, que se trocam lá, pela janela **COMANDOS DA IA**; o `--final` roda na versão definitiva, que é a que a pessoa devolve depois do **INSERIR NO PROMPT**, antes dos testes. Sem terminal, use a lista do fim de `assets/modelo-prompt.md`.
4. Entregue o prompt em bloco de código e a tabela "o que falta preencher e onde achar". Cada comando entra pela janela **COMANDOS DA IA**, que escolhe o Setor, o operador ou a tag pelo nome e escreve os ids (`references/configuracao-painel.md`, etapa 5).
5. Dê o passo a passo do painel seguindo `references/configuracao-painel.md`, etapas 1 a 7: um passo por linha, caminho de menu em negrito, valor de cada campo, pulando o que a pessoa já fez. Apontar a Conexão para o Setor da IA (etapa 9) fica para depois dos testes; a entrega diz isso em uma linha: "O último passo, fazer os clientes chegarem à IA pela Conexão, fica para depois dos testes."
6. Feche com limites e custos em três ou quatro linhas (seção "Limites e custos" do mesmo arquivo) e com o convite: "Quando o prompt estiver no painel, com os comandos inseridos, cole aqui o texto final: eu confiro e mando o roteiro de testes."

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

Caminho de arquivo desta skill (o que começa por `references/` ou `assets/`) não vai na resposta, nem entre parênteses no meio do texto: a pessoa não tem esses arquivos. No lugar dele vão o título do artigo e o link, que é `https://clihelper.chatmasterveloz.com/docs/` seguido do nome do arquivo sem `.md` (por exemplo, Transferir Ticket: https://clihelper.chatmasterveloz.com/docs/transferir-ticket). Artigo de `references/docs/revendedor/` tem outro endereço, o da linha **Fonte** dele, e só é citado na resposta ao revendedor. Também não escreva "o plano de testes da skill" nem "a tabela da skill".

## Consertar uma IA que já existe

Peça o prompt atual, os valores dos campos e um trecho de conversa em que o problema aparece. Separe a causa antes de reescrever: problema de **configuração** (Setor, status, token, temperatura, tokens, histórico) se resolve no painel; problema de **texto** (inventa, sai do escopo, não segue o roteiro) se resolve no prompt. Devolva só o trecho corrigido, o que conferir no painel e quais cenários repetir. Mude uma coisa por vez.

## Outros recursos de IA

Respostas curtas, com base no artigo e nas atualizações que o citam.

| Recurso | O que é | Onde fica | Artigo |
|---|---|---|---|
| Transcrever Áudios | Transforma em texto o áudio do cliente: sozinha, no Setor com a transcrição ligada (com prompt no Setor, a IA responde ao que foi falado), ou quando alguém pede. | Setor › **Ativar Transcrição de Áudio**; na mensagem de áudio, seta superior direita › **Transcrever Áudio**. | `references/docs/recursos/transcrever-audios.md` |
| Análise de Atendimento | Avalia um atendimento (objeções, pontos de melhoria, sentimento geral e KPIs) ou resume um período da conversa. Chega como nota interna; o cliente não recebe nada. Depende das opções de plano **AI** e **GPT Análises**. | No topo da conversa, **Analisar Atendimento com IA** ou **Resumo do período** (agrupados, no botão **Mais**); instrução da análise no menu **GPT Análises**. | `references/docs/recursos/analise-de-atendimento.md`; o que libera: `references/docs/revendedor/recursos/como-habilitar-gpt-analises.md` |
| Avaliação pela IA | Dá nota de 0 a 10 aos atendimentos encerrados, em rodadas, gera relatório para a gestão e aulas para cada atendente. Nada vai ao cliente. Depende da opção de plano **Avaliação pela IA**. | Liga em **Configurações › Opções › Automação**, seção **Avaliações** (só administrador); resultados no menu **Avaliação pela IA**: Administrador e Supervisor veem a equipe, o Atendente só **Minhas aulas**. | `references/docs/recursos/avaliacao-pela-ia.md`; dúvida de uso, o artigo da Armadilha "Avaliação pela IA" |
| Copiloto de mensagens | Botão que sugere a próxima resposta ou melhora o texto digitado; nunca envia sozinho. Depende da opção de plano **Sugestão de resposta IA** e consome créditos de IA. | Na conversa, botão ✨ ao lado do **+**. | `references/docs/recursos/copiloto-de-mensagens.md` |
| Sugestão de resposta IA | Tela que governa o Copiloto: instruções das duas funções, **Modelo**, **Mensagens de contexto** (1 a 50) e **Extrato de tokens**. | Menu **Sugestão de resposta IA** (só administrador). | `references/docs/recursos/sugestao-de-resposta-ia.md` |
| Base de Conhecimento | Material que o prompt consulta antes de responder (horários, políticas, preços, perguntas frequentes), em itens digitados ou lidos de arquivo .pdf, .docx, .txt, .md ou .csv. | **Prompts OPEN.AI › BASE DE CONHECIMENTO**; ligada no campo **Base de conhecimento** do prompt. | `references/docs/recursos/base-de-conhecimento-do-gpt-assistant.md` |
| GPT Assistant em Grupos | O assistente responde em um grupo de WhatsApp; com gatilho, só às mensagens que começam com ele. Antes disso, o grupo precisa entrar na plataforma: há até três travas de grupo (`references/configuracao-painel.md`, "Opcional: usar o assistente em um grupo"). | Campo **Gatilho para Acionar em Grupos** do prompt; prompt do grupo em **Contatos** › editar o grupo › **Prompt OPEN.AI (ChatGPT)**. | `references/docs/recursos/gpt-assistant-em-grupos.md` |
| Token OpenAI | A chave que alimenta os recursos de IA; o consumo é cobrado na conta dona dela. | Menu **Integrações**, card **OPEN.AI**. | `references/docs/recursos/token-openai.md` |
| Provedor de IA | Escolhe o serviço de IA que responde os prompts de chat (**OpenAI**, **Groq**, **DeepSeek**, **Mistral**, **xAI (Grok)**, **OpenRouter** ou **Local (Ollama / vLLM)**). Fora da OpenAI, **Modelo** e **Chave de API do provedor** são obrigatórios. **Modelo de transcrição** é opcional (provedor sem transcrição continua usando a OpenAI), e **URL do servidor** só aparece no **Local (Ollama / vLLM)**. Quando falta algo no card, a própria IA avisa o motivo. Depende da opção de plano **Provedores de IA**. | Menu **Integrações**, card **Provedor de IA**. | `references/docs/recursos/provedor-de-ia.md` |
| Assistente de IA (menu) | Responde a perguntas da equipe sobre atendimentos, contatos, tarefas, oportunidades do CRM, reservas e produtos em falta, cada perfil só com o que já acessa. Só consulta. | Menu **Assistente de IA**. | `references/docs/recursos/assistente-de-ia.md` |
| IA nas gravações das chamadas | Transcreve, legenda e analisa as gravações das chamadas. Usa a chave de IA da conta: o **Token OpenAI** ou, quando a conta usa a chave da plataforma, essa chave. | Liga em **Configurações › Opções › Chamadas**, opção **IA nas gravações das chamadas**; resultado na página **Gravações**. | `references/docs/recursos/gravacoes-das-chamadas.md` |

Se pedirem para "dar a cara da empresa" ao Copiloto, escreva os dois textos da tela **Sugestão de resposta IA** (**Instruções para sugerir a resposta** e **Instruções para melhorar o texto**) com o tom e os limites da empresa. Mantenha a regra de não inventar preço, prazo, endereço ou política: o artigo avisa que é ela que impede a IA de prometer o que a empresa não cumpre. Lembre a pessoa de clicar em **SALVAR**.

## Armadilhas

Cada uma está explicada por inteiro em um só lugar; aqui fica o lembrete.

- **Forma do código e aspas curvas; turno da tag:** `references/comandos-e-capacidades.md`, seção 3.
- **Agente OpenAI desligado:** seção 1 do mesmo arquivo.
- **Janela COMANDOS DA IA, comando de agenda e ID do Setor:** seções 4 e 5; roteiro em `references/configuracao-painel.md`, etapa 5. A Central não mostra a forma dos blocos `agenda` e `oportunidade`; a seção 4 traz a forma observada num painel, que serve para explicar a seção e reconhecer um bloco inteiro, não para escrevê-lo. Diga para inserir pelo botão da janela e não editar o bloco à mão; o conferidor só avisa neles, e o teste é que prova.
- **Quando a IA atua, Setor de transbordo sem prompt, dois motores no mesmo Setor, primeira mensagem:** seção 6.
- **Transbordo e comando de transferir ao mesmo tempo:** seção 7.
- **Nomes que mudaram.** O campo **GPT Model** virou **Modelo da IA** (a imagem do artigo Tipo Prompt ainda mostra o nome antigo); o gatilho de grupo agora se chama **Gatilho para Acionar em Grupos**, e o exemplo da tela é `#meubot`. Cite os dois nomes para a pessoa reconhecer o que vê.
- **Nomes parecidos.** GPT Assistant (atende o cliente), **Assistente de IA** (menu de consultas da equipe), Análise de Atendimento (um atendimento, sob demanda), Avaliação pela IA (rodadas automáticas com nota) e a pesquisa de avaliação respondida pelo cliente são cinco coisas diferentes. A **Conexão com assistentes de IA**, anunciada em 22/11/2026, é uma sexta: liga o assistente de IA que a empresa já usa aos dados do atendimento, precisa estar liberada para a empresa e ainda não tem artigo, só a nota (`references/docs/recursos/atualizacoes-2026-11-22.md`). Diga isso e não descreva a tela.
- **Só nas notas de 20 a 22/11/2026.** Nas **Vendas perdidas**, o filtro por **Conexão** e o botão **Abrir a configuração**; nas **Gravações**, o **Gerar ATA**, com a transcrição pronta; no **Assistente de IA**, as respostas sobre os atendimentos abertos num dia, com os nomes da tela, e a contagem de abertos igual à do painel. Cada nota vale a partir da versão que ela cita, e a versão instalada aparece no fim do menu do ícone do perfil: se a pessoa não acha a novidade, confira a versão primeiro (`references/docs/recursos/atualizacoes-2026-11-20.md`, `references/docs/recursos/atualizacoes-2026-11-21.md`, `references/docs/recursos/atualizacoes-2026-11-22.md`).
- **Créditos do Copiloto e conta da OpenAI.** O saldo de créditos é da plataforma; mesmo com **ILIMITADO**, o consumo continua cobrado na conta da OpenAI (`references/docs/recursos/copiloto-de-mensagens.md`). Quem recarrega, o que o saldo trava e as duas explicações, em conflito, para o **Ilimitado**: `references/configuracao-painel.md`, "Créditos do Copiloto".
- **Avaliação pela IA: um artigo por dúvida de uso**, todos com "Avaliação pela IA" no título, espalhados no índice (que segue a ordem dos arquivos). Abas e menu: `visao-geral-avaliacao-pela-ia.md`; ligar e horários das rodadas: `como-ligar-a-avaliacao-pela-ia.md`; quem vê o quê: `permissoes-avaliacao-pela-ia.md`; aba **Hoje**: `aba-hoje-da-avaliacao-pela-ia.md`; aba **Evolução**: `aba-evolucao-da-avaliacao-pela-ia.md`; aulas: `aulas-da-avaliacao-pela-ia.md`; ler o **Relatório**: `relatorio-da-avaliacao-pela-ia.md`; alertas no sino: `alertas-da-avaliacao-pela-ia.md`; processo ideal, o geral e os por Setor ou Conexão: `processos-de-atendimento-da-avaliacao-pela-ia.md`; tirar colega da avaliação: `contatos-internos-na-avaliacao-pela-ia.md`; produtos em falta: `vendas-perdidas-na-avaliacao-pela-ia.md`; webhook: `webhook-da-avaliacao-pela-ia.md` (integração, `cmv-api`). Ajustes recentes: atualizações de 12/11 a 21/11/2026.
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
Etapa 1. Resposta de umas vinte linhas: dá para fazer; os três pré-requisitos; seis perguntas (nome e serviços, o que pode informar e quais preços, o que não pode dizer, quando passar para uma pessoa e para qual equipe, que dados a recepção precisa para a avaliação e quem confirma o horário, o que já está pronto); a frase sobre agendamento (a IA anota a preferência e a equipe confirma, ou marca pelo comando de agenda); a oferta do rascunho.

**A mesma pessoa responde às perguntas.**
Etapa 2: "o que entendi", prompt com a variante A de agendamento e um só comando, o de transferir para a recepção (o objetivo não pede tag), tabela do que falta (o comando a inserir pela janela **COMANDOS DA IA**), passo a passo do painel até a saudação do Setor, a linha sobre a Conexão ficar para depois dos testes, limites e custos, e o convite para o roteiro de testes.

**"Minha IA não transfere pro atendente quando o cliente pede."**
Peça o prompt e os campos de **Transbordo**. Confira se a instrução do comando está no fim do campo **Prompt** e foi salva, o texto de **Quando a IA deve fazer isso**, o código contra a forma do artigo, o Setor de destino e se há atendentes nele. Devolva o trecho corrigido, o que conferir no painel e os cenários de pedido de humano para repetir três vezes.

**"O que é esse Avaliação pela IA que apareceu no menu?"**
Resposta curta com base no artigo principal, em Permissões Avaliação pela IA e em Como Ligar a Avaliação pela IA: o que faz, quem vê o quê, onde liga, que depende do plano e que nada vai ao cliente. Link da Fonte no fim.
