---
name: cmv-ajuda
description: "Use para dúvidas de uso do painel do Chat Master Veloz (chatmasterveloz, CMV): \"como faço\", \"onde fica\", \"o que é\", \"por que não funciona\" e \"o que mudou\". Vale para todo recurso da tela: conexões (WhatsApp oficial e QR, Instagram, Web Chat), setores e chatbot, equipe e permissões, tickets, tags, contatos, campanhas, Mail Marketing, Dashboard, Consultório, Reservas, Links de agendamento, ligações (VoIP, PABX), CRM, PDV, configurações. Cobre conexão caída, mensagem sumida e aviso ou erro que aparece na tela, mesmo técnico ou em inglês. Quem tem esta skill usa o CMV: pergunta sobre o painel ou o atendimento que não cite outra ferramenta é dela, mesmo sem citar o CMV; carregue-a antes de responder: o passo a passo vem da Central de Ajuda. NÃO use para o app WhatsApp Business nem outras plataformas (Chatwoot, Blip, ManyChat). Produzir material é das irmãs: API e webhooks (cmv-api), fluxos (cmv-flowbuilder), IA (cmv-agente-ia), textos e templates (cmv-mensagens), CSS/JS (cmv-painel-css-js)."
---

# Ajuda do Chat Master Veloz

Esta skill responde dúvidas de uso do Chat Master Veloz (CMV) com base na cópia da Central de Ajuda que está em `references/docs/`: 513 artigos (496 de recursos, 14 de trilhas, 3 fora do menu) e a lista de vídeos, copiados em 20/11/2026. Quem pergunta costuma ser administrador, supervisor ou atendente sem formação técnica.

A documentação é grande. Ler tudo gasta contexto e não melhora a resposta: o trabalho é achar o artigo certo, ler o trecho que responde e passar isso adiante em linguagem simples, dizendo de onde veio.

## Como trabalhar

### 1. Entenda o que a pessoa quer

Antes de buscar, identifique três coisas, porque elas mudam o artigo certo:

- **O tipo de pedido:** como fazer, o que é, por que não funciona, por onde começar, o que mudou.
- **O canal**, quando o assunto é conexão ou envio: WhatsApp oficial, WhatsApp por QR Code, Instagram, Messenger, Telegram, Web Chat, Chat Externo. Vários assuntos têm um artigo para cada canal, com passos opostos (veja "Armadilhas").
- **O perfil de quem vai fazer:** administrador, supervisor ou atendente. Muitas telas só existem para o administrador.

O mesmo vale para qualquer outra bifurcação que mude os passos. Exemplo: "cadastrar uma atendente para ver só as conversas do financeiro" muda conforme ela só responde ou também inicia conversas, e conforme deve ver todas as conversas do Setor ou só as dela.

Se a resposta muda e a pessoa não disse, pergunte em uma linha. Quando as alternativas são poucas e curtas, é melhor responder cobrindo as duas ("se for X, faça assim; se for Y, assim") do que fazer a pessoa esperar. Se não muda, não pergunte.

### 2. Ache o artigo

Nesta ordem, parando assim que achar:

1. `references/mapa-por-objetivo.md`: os objetivos mais comuns já apontam para os artigos.
2. Os índices, pelo título: `INDICE-recursos.md` (hierarquia do menu), `INDICE-trilhas.md`, `INDICE-outros.md`.
3. Busca no texto dos artigos.

Com terminal, a partir de `references/docs/`:

```bash
grep -n -i 'rodízio' INDICE-recursos.md INDICE-trilhas.md INDICE-outros.md  # pelo título
grep -rci 'rod[ií]zio' recursos trilhas outros | sort -t: -k2 -nr | head     # artigos que mais falam do assunto
grep -rn -i 'encerrar por inatividade' recursos trilhas outros                # a frase exata, com a linha
grep -rn -F 'Missing Body in Payload' recursos                                # mensagem de erro copiada da tela
grep -rli 'clonar' recursos/atualizacoes-2026-*.md                            # novidade recente
```

Sem terminal (claude.ai): leia `references/mapa-por-objetivo.md`; se não bastar, leia `references/docs/INDICE-recursos.md` (cabe numa leitura) e abra o artigo pelo título. O nome do arquivo é o título sem acentos e com hifens.

### 3. Leia só o necessário

Todo artigo começa com título, **Fonte** (o link no site), **Categoria** e **Menu**. A maioria tem blocos marcados: `[RESUMO]` (o passo a passo em poucas linhas), `[DUVIDAS]` (perguntas comuns), `[ERROS]` (erros comuns e a solução), além de `[ATENCAO]`, `[DICA]` e `[PREREQUISITO]`.

```bash
head -3 recursos/ARTIGO.md                                         # título e linha Fonte (o link): os comandos abaixo pulam o cabeçalho
grep -n '^#' recursos/ARTIGO.md                                    # as seções do artigo
sed -n '/\[RESUMO\]/,/^$/p' recursos/ARTIGO.md                     # só o resumo
sed -n '/\[DUVIDAS\]/,/^$/p;/\[ERROS\]/,/^$/p' recursos/ARTIGO.md  # dúvidas e erros comuns
```

Para "como faço", o `[RESUMO]` mais a seção do passo costumam bastar. Para "por que não funciona", vá direto a `[DUVIDAS]` e `[ERROS]` do artigo do recurso: é ali que estão as causas mais comuns, na voz de quem pergunta. Sempre leia o `[ATENCAO]` do artigo, quando houver, antes de mandar a pessoa fazer algo que não tem volta (excluir conexão, excluir contato, encerrar tickets em massa).

### 4. Confira atualizações e divergências

Os artigos `recursos/atualizacoes-AAAA-MM-DD.md` registram o que mudou a cada dia, e nem toda mudança foi levada ao artigo do recurso. Quando o assunto for IA, PDV, CRM, FlowBuilder, conexões, Dashboard, Consultório ou algo que a pessoa chama de "novo", busque também nas atualizações. Busque pelo nome do recurso ou do botão ("Clonar conexão", "Limitador de Mensagens"), não por um termo genérico: "QR Code", por exemplo, aparece nas atualizações quase só em assuntos do PDV e traz ruído. Se a atualização e o artigo divergirem, vale a atualização: diga isso e cite a data.

Dois artigos do mesmo assunto também podem dar passos diferentes (o caso conhecido é reconectar o WhatsApp por QR Code: veja "Armadilhas"). A documentação não diz qual dos dois vale, então não funda os dois num procedimento único como se ele estivesse documentado. Apresente os dois caminhos, cada um com a sua fonte, comece pelo menos destrutivo (o que não apaga sessão, conexão nem dados) e diga que a documentação diverge.

### 5. Responda

Formato e exemplos estão em "Como responder", mais abaixo.

### 6. Quando a documentação não cobre

Antes de concluir que não está documentado, abra todos os artigos que o mapa ou a busca apontaram para o assunto, não só o primeiro; se leu um só, o que dá para dizer é "este artigo não explica". Então diga com clareza: "a Central de Ajuda não documenta isso". Conte o que procurou, ofereça o artigo mais próximo, se existir, e indique o suporte escrevendo o título e o link do artigo: Contato para Suporte, https://clihelper.chatmasterveloz.com/docs/contato-para-suporte. Não complete com suposição: um caminho de menu inventado faz a pessoa perder tempo procurando um botão que não existe.

## Mapa do material

| Arquivo | Para quê |
|---|---|
| `references/mapa-por-objetivo.md` | "Quero fazer isto" → artigos, para os pedidos mais comuns |
| `references/glossario.md` | O que significa cada termo do produto, com o artigo de origem |
| `references/docs/00-LEIA-PRIMEIRO.md` | Convenções dos artigos (ver aviso abaixo) |
| `references/docs/INDICE-recursos.md` | Os 496 artigos de recursos, na hierarquia do menu do site |
| `references/docs/INDICE-trilhas.md` | As 3 trilhas (14 artigos), em ordem de leitura |
| `references/docs/INDICE-outros.md` | 3 artigos que não estão em nenhum menu |
| `references/docs/INDICE.md` | Lista corrida de tudo, título e caminho |
| `references/docs/videos.md` | 17 vídeos tutoriais no YouTube |

**Aviso sobre o `00-LEIA-PRIMEIRO.md`:** ele descreve a documentação completa e cita `INDICE-api.md`, `INDICE-api-endpoints.md`, a pasta `api/`, a pasta `../docs-css-chatmasterveloz/` e o script `_gerar.py`. Nada disso está nesta skill. A referência da API fica na skill `cmv-api` e a de CSS e JS, na `cmv-painel-css-js`.

### Áreas do menu (primeiro nível de `INDICE-recursos.md`)

Os arquivos de entrada ficam em `references/docs/recursos/`. A coluna "Artigos" conta a entrada e os filhos.

| Área | Entrada | Artigos | O que tem |
|---|---|---|---|
| Meu Perfil | `meu-perfil.md` | 5 | status, senha, recuperar senha, favoritos |
| Chats / Tickets | `chats-tickets.md` | 20 | ticket × protocolo, Aguardando × Atendendo, transferir, devolver, encerrar, editar mensagem enviada, videochamada, alertas vermelhos, Pesquisar, Gestão de atendimentos |
| Atendimento Otimizado | `atendimento-otimizado.md` | 13 | mensagens de ausência, encerramento e aniversário, Mustaches, Mover após, inatividade, Avise-me, Siga-me, Avaliações, carteira, rodízio por Setores |
| Quadro de Atendimentos | `quadro-de-atendimentos.md` | 6 | colunas, visão por tags, regras, permissões |
| Dashboard | `dashboard.md` | 18 | números de agora e do período, filtros, metas e limites, relatórios, alertas, resumo automático, Meus números do atendente |
| E-mails | `e-mails.md` | 6 | contas, escrever e responder, caixa compartilhada, permissões |
| Mail Marketing | `mail-marketing.md` | 9 | e-mail em massa: listas, modelos, campanhas de e-mail, relatório, descadastros |
| Ligações | `ligacoes.md` | 7 | VoIP, PABX, ramais, ligação pelo WhatsApp |
| Rodízios | `rodizios.md` | 3 | cadastro de rodízios, relatório |
| Contatos | `contatos.md` | 11 | adicionar, editar, bloquear, importar, exportar |
| Tags | `tags.md` | 10 | tipos de tag, Kanban de Tags, Pixel Meta, remarketing |
| Respostas Rápidas | `respostas-rapidas.md` | 9 | texto, mídia, contato, localização, fluxo |
| Links de Agendamento | `links-de-agendamento.md` | 1 | página em que o cliente marca reunião; a reunião entra nas Tarefas |
| Agendamentos | `agendamentos.md` | 5 | mensagens programadas |
| Campanhas | `campanhas.md` | 5 | configurar, listas, nova campanha (um artigo por canal) |
| Conexões | `conexoes.md` | 39 | WhatsApp oficial (templates, forma de pagamento, nome de exibição, qualidade e limite, erros de entrega) e por QR Code, Instagram, Messenger, Web Chat, Chat Externo, migrar, Concatenador |
| Setores & Chatbot | `setores-e-chatbot.md` | 9 | abas do Setor, categorias, menu do chatbot na conexão |
| FlowBuilder | `flowbuilder.md` | 60 | editor, 9 pontos de entrada (`gatilho-via-*.md`), blocos (`bloco-*.md` e `reservas-agendar-no-fluxo.md`) |
| Equipe | `equipe.md` | 11 | tipos de perfil, abas do cadastro, permissões, ações sobre o usuário, Registro de Atividades |
| Chat Interno | `chat-interno.md` | 2 | conversas e chamadas entre a equipe |
| Gravações das Chamadas | `gravacoes-das-chamadas.md` | 1 | página Gravações |
| Configurações | `configuracoes.md` | 30 | busca de opção, uma entrada por aba de Configurações › Opções (Geral, Atendimento, Contatos, Automação, Chamadas, Vendas, Integrações e segurança) e suas seções, armazenamento remoto, webhooks, 2FA, Token da Empresa |
| Tarefas | `tarefas.md` | 10 | criar, editar, comentar, compartilhar, concluir, avisos ao cliente |
| Projetos | `projetos.md` | 8 | modelos, criar projeto, quadro do projeto, avisos ao cliente |
| CRM | `crm.md` | 32 | funis, oportunidades, Board, propostas, relatórios, ranking, Minha evolução |
| PDV | `pdv.md` | 25 | produtos, caixa, balcão, pedido na conversa, pagamentos, entregas, setores de produção, clientes, cardápio, mesas e conta da mesa, reservas de mesa, garçom, loja |
| Consultório | `consultorio.md` | 23 | clínica: cadastros, agenda, recepção, pacientes, prontuário, documentos e receitas, cobrança, teleconsulta, repasse |
| Reservas | `reservas.md` | 20 | profissional, mesa, sala ou quarto com hora marcada ou diária: agenda, página do cliente, lista de espera, pagamento, pacotes |
| Gerenciador de Arquivos | `gerenciador-de-arquivos.md` | 1 | biblioteca de arquivos da empresa |
| Inteligência Artificial | `inteligencia-artificial.md` | 11 | pré-requisitos, transcrição, análise, GPT Assistant e Base de Conhecimento, Sugestão de resposta, Copiloto |
| Assistente de IA | `assistente-de-ia.md` | 4 | perguntas sobre os dados da plataforma (atendimentos, CRM, reservas, vendas perdidas) |
| Avaliação pela IA | `avaliacao-pela-ia.md` | 13 | nota da IA para atendimentos encerrados: como ligar, processos, alertas, aulas, relatório, vendas perdidas |
| Gestão de Links | `gestao-de-links.md` | 6 | links curtos com relatório de cliques |
| Link na Bio | `link-na-bio.md` | 1 | página de links |
| Integrações | `integracoes.md` | 12 | tokens e chaves (conexão, OpenAI, Meta, pagamentos, Google Maps), Provedor de IA, n8n |
| Perguntas Frequentes | `perguntas-frequentes.md` | 2 | só "Como atualizar o cache" |
| Problema / Solução | `problema-solucao.md` | 8 | 7 problemas conhecidos |
| Aplicativo | `aplicativo.md` | 3 | PWA, notificações push |
| Vídeos | `../videos.md` | 1 | lista de vídeos |
| Contato para Suporte | `contato-para-suporte.md` | 1 | canal do suporte |
| Atualizações | `atualizacoes.md` | 36 | 2 índices de mês e 33 dias |

### Para quem está começando

`INDICE-trilhas.md` tem três trilhas: **Primeiros Passos** (visão geral, primeira conexão, setor, equipe: leia e indique nessa ordem), **A cobrança do WhatsApp Oficial mudou** (o que a Meta cobra e as formas de gastar menos) e **Organizando quem atende** (o que o atendente enxerga). A trilha da cobrança é um resumo: cada etapa aponta para o artigo de `recursos/` que tem o passo a passo completo.

### Dúvidas e problemas

- **Problema / Solução** tem só 7 artigos e **Perguntas Frequentes**, só 1. A maior parte das respostas a "por que não funciona" está nos blocos `[DUVIDAS]` (400 artigos) e `[ERROS]` (122 artigos) do artigo de cada recurso.
- "Vermelho" são dois sintomas diferentes; pergunte qual, se não estiver claro. **Recado vermelho dentro da conversa** é erro de envio: `recursos/alertas-vermelhos-no-chat.md` lista os textos, a maioria em inglês. **Conversas com fundo vermelho na lista** é conexão desconectada, segundo `recursos/conexao-desconectada.md`: vá para a linha "Conexão caiu" da tabela em "Armadilhas".
- Pessoa que não consegue entrar: `recursos/usuario-nao-consegue-entrar-na-plataforma.md`.
- Mensagem ou template do WhatsApp Oficial que não chega ao cliente: `recursos/erros-de-entrega-do-whatsapp-oficial.md` (códigos de erro da Meta) e `recursos/template-recusado-pausado-ou-desabilitado.md`.
- "A tela está vazia" ou "o item não aparece": quase sempre é permissão. Veja `recursos/tipos-de-perfil.md` e o artigo de permissões do módulo (em `recursos/`: `permissoes-configuracoes.md`, `permissoes-dashboard.md`, `permissoes-e-mails.md`, `permissoes-mail-marketing.md`, `permissoes-pdv.md`, `permissoes-consultorio.md`, `permissoes-reservas.md`, `permissoes-projetos.md`, `permissoes-avaliacao-pela-ia.md`, `permissoes-quadro-de-atendimentos.md`, `quem-visualiza-o-que-no-crm.md`).

### O que mudou

`recursos/atualizacoes.md` → índice do mês (`atualizacoes-2026-11.md`, `atualizacoes-2026-10.md`) → um arquivo por dia, de 15/10/2026 a 19/11/2026. Para "o que mudou esta semana", liste os arquivos dos dias e leia o topo de cada um (Novidades, Melhorias, Correções). A seção "O que você precisa fazer", no fim, diz se a mudança exige ação. Não há registro anterior a 15/10/2026 nem posterior à data da cópia: diga isso se perguntarem.

### Vídeos

`videos.md` traz título, link do YouTube e uma linha de descrição. Indique o vídeo como complemento, sem descrever o que ele mostra: o conteúdo não foi transcrito. Dentro dos artigos, `[Vídeo Voomly — id …]` marca um vídeo sem endereço público; não há link para passar.

## Armadilhas

Nesta seção, arquivo citado sem pasta está em `references/docs/recursos/`.

**A linha "Menu" do cabeçalho é o caminho na Central de Ajuda, não no painel.** "Atendimento Otimizado", por exemplo, não é um menu do painel. O caminho que a pessoa vai clicar está no corpo do artigo, escrito de dois jeitos conforme o artigo: "Acesse o menu **Conexões  ›  editar a Conexão**…" ou "menu → Conexões > Editar > Mensagens". Passe adiante o do corpo.

**O nome da área na ajuda nem sempre é o nome do menu no painel.** Confirmados nos artigos: FlowBuilder → menu **FlowBuilder Nativo**; GPT Assistant → menu **Prompts OPEN.AI**; pesquisar atendimentos → menu **Pesquisar**; Gravações das Chamadas → menu **Gravações**. Há dois itens **Categorias** no painel: um para Setores (`categorias-de-setores.md`), outro para fluxos (`categorias-de-fluxos.md`).

**Algumas telas não estão no menu lateral.** Gestão de Templates, Limitador de Mensagens, Concatenador, Modo Híbrido e Perfil do número abrem por botões no card da conexão. O Relatório do Rodízio abre pelo botão **Ver relatório** na tela Rodízios, que só aparece com a opção **Exibir o Relatório do Rodízio (botão Ver relatório, na tela Rodízios)?** em **Sim** em Configurações › Opções › Atendimento, seção Distribuição e rodízio (`relatorio-do-rodizio.md`).

**Um mesmo assunto, um artigo por canal.** Misturar os dois dá instrução errada:

| Assunto | WhatsApp por QR Code | WhatsApp Oficial |
|---|---|---|
| Conectar | `adicionar-whatsapp-qrcode.md`, `adicionar-whatsapp-sem-aparelho-celular.md` | `adicionar-whatsapp-oficial.md`, `trazer-um-numero-da-api-oficial-de-outra-plataforma.md` |
| Conexão caiu | `adicionar-whatsapp-qrcode.md` (seção "Quando a conexão cai"), `conexao-desconectada.md`, `conexao-nao-le-o-qr-code.md` | `verificar-agora-e-reconectar.md`, `avisos-da-meta-na-conexao.md` |
| Campanha | `nova-campanha.md` | `nova-campanha-api-oficial.md` |
| Ligação pelo PABX | `pabx-ligacao-whatsapp-qr-code.md` | `pabx-whatsapp-oficial.md` |

**No QR Code, dois artigos dão passos diferentes para a conexão que caiu.** `adicionar-whatsapp-qrcode.md`, seção "Quando a conexão cai", lista três botões do card: **Reconectar** (tenta retomar a sessão), **Novo QR** (gera outro código) e **Excluir Sessão** (apaga a sessão e começa do zero), este "quando os dois anteriores não resolvem". `conexao-desconectada.md` começa direto por **Excluir Sessão**, depois **Reiniciar Conexões** (nos três pontinhos; reinicia todas as conexões da empresa) e **Ver QR Code**, e avisa para não clicar na lixeira. Apresente os dois, começando pelo primeiro, que não apaga a sessão, e diga que a documentação diverge.

Janela de atendimento, templates e Limitador só existem na conexão oficial. Em artigos que valem para os dois (botões do fluxo, agendamento, número bloqueado), procure a tabela por canal ou a seção "API Oficial" dentro do artigo.

**As etiquetas `[Básica]`, `[Pro]`, `[Oficial]`, `[Hub]`, `[Webchat]` citadas no `00-LEIA-PRIMEIRO.md` são da referência da API e não aparecem nestes artigos.** Aqui o canal vem escrito por extenso: "conexão oficial", "API Oficial", "WhatsApp Oficial" ou "canal oficial" de um lado; "conexão por QR Code", "WhatsApp QRCode" ou "canal não oficial" do outro. Estes artigos não explicam o que é cada etiqueta. Se a pessoa usar um desses nomes (Básica, Pro, Hub) e a resposta depender do canal, pergunte se o número foi conectado lendo um QR Code ou pela conta da Meta.

**Títulos parecidos, telas diferentes:**

- Quadro de Atendimentos (atendimentos em colunas) × Kanban de Tags × Board (CRM) × Quadro do Projeto.
- Web Chat (código colado no site) × Chat Externo (página aberta por link) × Modo Alternativo (continua numa página a conversa que começou no WhatsApp Oficial).
- Avaliações (o cliente dá a nota) × Avaliação pela IA (a IA dá a nota) × Análise de Atendimento.
- Rodízios (menu, usado pelo bloco Rodízio do fluxo) × Rodízio de Atendimento (montado com dois Setores).
- Agendamentos (mensagem programada) × Links de agendamento (o cliente marca uma reunião) × Reservas (módulo de hora marcada ou diária) × Reservas de mesa (PDV) × Agenda do Consultório.
- Campanhas × Mail Marketing (e-mail em massa); GPT Assistant (responde clientes) × Assistente de IA (responde perguntas da equipe sobre os dados); Dashboard × Dashboard (legado), que conta diferente.
- Token da Conexão × Token da Empresa; Produtos do CRM × Produtos do PDV; Tarefas × tarefas de um Projeto × Atividades da Oportunidade.
- `X.md` × `X-em-configuracoes.md`: o primeiro explica o recurso, o segundo descreve a aba ou a seção em Configurações › Opções. Ex.: `avaliacoes.md` × `avaliacoes-em-configuracoes.md`; `carteira-de-clientes.md` × `contatos-em-configuracoes.md` (seção Carteiras de Clientes); `mensagem-de-aniversario.md` × `mensagens-automaticas-em-configuracoes.md`.

**Três artigos ficam em `outros/` e não aparecem em `INDICE-recursos.md`:** Adicionar Tag, Tipos de Tags e Telegram. Por isso as buscas incluem `outros`.

**Busca com e sem acento.** O texto dos artigos tem acento; os nomes de arquivo, não. `grep -i 'rodizio'` acha 7 artigos, `grep -i 'rodízio'` acha 31. Busque com acento ou com `rod[ií]zio`. Termos curtos casam dentro de outras palavras: use `grep -w`.

**Mensagens de erro vêm em inglês.** Busque o texto exato com `grep -F`, sem traduzir.

**Os artigos usam palavras diferentes para a mesma coisa.** Parte deles diz "Fila" ou "Departamento", parte diz "Setor". A aba da conexão aparece como "Setores & Tempos" em 14 artigos e como "Filas & Tempos" em 1. `setores-e-chatbot.md` diz que hoje a plataforma chama de **Setor** em todo lugar (a palavra "fila" fica para o sentido de espera); "Filas & Tempos" é o nome antigo, que sobrou em `encerrar-por-inatividade.md`. Ao responder, use **Setor** e **Setores & Tempos**, e avise do nome antigo quando o artigo lido ainda o usar. Os títulos em `videos.md` também usam nomes diferentes dos artigos ("Filas & Chatbot").

**Os artigos quase não têm links entre si.** Quando um artigo manda ver outro pelo nome ("saiba como em Pré-Requisitos de IA"), ache-o pelo título no índice.

**Onde fica uma opção.** `recursos/configuracoes.md` dá a regra: o que vale para a empresa inteira fica em Configurações; o que é por pessoa, no cadastro em Equipe; o que é por canal, em Conexões. Em Configurações › Opções, as abas são Geral, Atendimento, Contatos, Automação, Chamadas, Vendas e Integrações e segurança, e o campo **Pesquisar opção**, acima das abas, acha a opção pelo nome (`visao-geral-configuracoes.md`). A maioria das opções grava sozinha; alguns blocos têm botão próprio, como **SALVAR**.

**Item que não aparece pode ser plano, não permissão.** `recursos/tipos-de-perfil.md` diz que o que o plano da empresa não libera não aparece para ninguém. A documentação não lista planos nem preços: não cite nenhum. Sobre a cobrança da Meta no WhatsApp Oficial, repita só o que o artigo diz, com as datas dele.

## Sinônimos: o que a pessoa diz × como a documentação chama

| A pessoa diz | Procure por | Onde |
|---|---|---|
| fila, departamento | Setor | `setores-e-chatbot.md` |
| atendente, operador, usuário | a mesma pessoa; o perfil dela se chama **User** ("agente", nos artigos, é o assistente de IA) | `tipos-de-perfil.md` |
| conversa, chat, atendimento | ticket (protocolo é outra coisa) | `ticket-x-protocolo.md` |
| finalizar, fechar, concluir | encerrar; o botão é **Resolver** | `encerrar-ticket.md` |
| chatbot, robô, menu automático | menu de Setores na conexão, ou fluxo do FlowBuilder | `chatbot-e-menu-de-setores-na-conexao.md`, `flowbuilder.md` |
| disparo, envio em massa | Campanhas | `campanhas.md` |
| etiqueta | Tag | `tags.md` |
| variável, nome do cliente na mensagem | Mustaches `{{ }}`; no fluxo, `%nome%` | `mustaches.md`, `bloco-variavel.md` |
| modelo de mensagem | Template | `mensagem-template.md` |
| BM, Business Manager | Portfólio Empresarial (BM) | `portfolio-empresarial-bm.md` |
| WhatsApp normal, WhatsApp Web, QR | conexão por QR Code, canal não oficial | `adicionar-whatsapp-qrcode.md` |
| API do WhatsApp, WABA, Cloud API | API Oficial, conexão oficial | `entenda-a-api-oficial.md` |
| kanban, quadro | mais de uma tela possível: pergunte qual | ver "Títulos parecidos" |
| pipeline, negócio, lead no funil | Funil, Oportunidade, Board | `funis-do-crm.md`, `oportunidade-no-crm.md` |
| pesquisa de satisfação, nota do atendimento | Avaliações | `avaliacoes.md` |
| horário de atendimento, fora do horário | Expediente, aba Horários do Setor | `aba-horarios-em-setores-e-chatbot.md` |
| distribuição automática | Rodízio | `rodizios.md` |
| indicadores, métricas do atendimento, painel de números | Dashboard; para o atendente, Meus números | `dashboard.md`, `meus-numeros-do-atendente.md` |
| e-mail marketing, newsletter, e-mail em massa | Mail Marketing | `mail-marketing.md` |
| marcar horário, agenda online | depende do que se marca: reunião (Links de agendamento), consulta (Consultório), mesa, sala, quarto ou serviço (Reservas). Pergunte | `links-de-agendamento.md`, `consultorio.md`, `reservas.md` |
| boas-vindas | Mensagem de saudação | `chatbot-e-menu-de-setores-na-conexao.md`, `aba-mensagens-em-setores-e-chatbot.md` |
| aplicativo, app | PWA | `aplicativo.md` |
| chat do site, widget | Web Chat ou Chat Externo | `web-chat.md`, `chat-externo.md` |
| verificação em duas etapas, 2FA | no login do painel: **Habilitar 2FA na empresa**, na seção Segurança de Configurações. No número do WhatsApp: é da Meta, e aparece na migração de número | `seguranca-em-configuracoes.md`, `trazer-um-numero-da-api-oficial-de-outra-plataforma.md` |
| número banido, bloqueado | número bloqueado, restrição | `numero-bloqueado-no-whatsapp.md` |

Os arquivos da última coluna ficam em `references/docs/recursos/`. Mais termos em `references/glossario.md`.

## Como responder

Quem lê não é técnico e está com o painel aberto. A resposta precisa permitir que a pessoa execute sem voltar para perguntar:

1. **Uma frase** dizendo o que vai ser feito e, se couber, onde.
2. **Quem pode fazer**, quando o artigo diz ("só o administrador tem este menu"). Se o artigo não diz, confira o menu em `recursos/tipos-de-perfil.md`; se continuar sem resposta, não afirme.
3. **Para qual canal vale**, quando a resposta muda de um canal para outro.
4. **Passo a passo numerado**, com o caminho do menu e os nomes de botões e campos em negrito, escritos como no artigo. Não traduza nem "melhore" nome de botão: a pessoa vai procurar a palavra exata na tela.
5. **Avisos** do artigo que evitam perda (ação sem desfazer, mensagem que deixa de ser entregue).
6. **Fonte:** título do artigo e o link da linha **Fonte** do cabeçalho. Quando a resposta junta vários artigos, cite os dois ou três que sustentam os passos, não todos os que você consultou. Caminho de arquivo desta skill (`recursos/encerrar-por-inatividade.md`) não vai na resposta, porque a pessoa não tem esses arquivos: vão o título do artigo e o link da linha **Fonte**.

Não descreva o que estaria numa imagem ou num vídeo: eles não foram transcritos. Não copie o artigo inteiro; entregue o trecho que resolve. O que você deduziu e o artigo não diz (a consequência de um problema, a causa provável) fica de fora ou vem marcado como dedução sua, separado do que é do artigo.

**Exemplo 1: como fazer.** Pedido: "como faço pro sistema fechar sozinho a conversa quando o cliente some?"
Busca: mapa por objetivo → `recursos/encerrar-por-inatividade.md`. Entrega: uma frase ("isso é o Encerramento por Inatividade, configurado em cada conexão"); os passos (menu **Conexões** → editar a conexão → aba **Setores & Tempos**, avisando que este artigo ainda a chama de **Filas & Tempos** → campos **Inatividade**; depois a aba **Mensagens** → **Mensagem por Inatividade**); os dois avisos do artigo (o sistema não encerra se a última mensagem foi do cliente; tempo curto demais fecha conversa de quem só demorou); a fonte: "Encerrar por Inatividade (Atendendo)", com o link.

**Exemplo 2: por que não funciona.** Pedido: "meu whatsapp desconectou, como reconecto?"
A resposta depende do canal, então pergunte primeiro: "O número foi conectado lendo um QR Code ou pela conta da Meta (API Oficial)?". QR Code → dois artigos, com passos diferentes: primeiro o de `recursos/adicionar-whatsapp-qrcode.md` (**Reconectar**; se não voltar, **Novo QR**), depois, se não resolver, o de `recursos/conexao-desconectada.md` (**Excluir Sessão**, **Reiniciar Conexões**, **Ver QR Code**, com o aviso de não clicar na lixeira), dizendo que a documentação traz os dois caminhos e citando as duas fontes. Oficial → `recursos/verificar-agora-e-reconectar.md` (**Verificar agora**, **Reconectar**, com o aviso de não excluir a conexão). Os artigos dizem a causa e como reconectar; não dizem o que acontece com as mensagens enquanto a conexão está caída, então isso não entra na resposta como fato.

**Exemplo 3: o que mudou.** Pedido: "teve novidade no PDV esse mês?"
Busca: `grep -l -i 'pdv' recursos/atualizacoes-2026-11-*.md`, depois as seções de PDV de cada dia. Entrega: lista curta por data, uma linha por novidade, o que exige ação e os links dos artigos de cada dia.

**Exemplo 4: não documentado.** Pedido: "como mudo a cor do painel?"
A Central de Ajuda copiada aqui não documenta mudar as cores do painel. Ela trata só da aparência de páginas vistas pelo cliente (Web Chat, Chat Externo, Link na Bio, Cardápio e Loja Digital). Diga isso, confirme se era o painel e encaminhe para a skill `cmv-painel-css-js`; não invente um caminho de menu.

## Onde termina esta skill

| O pedido é… | Skill |
|---|---|
| Escrever código, montar payload, chamar endpoint, configurar webhook no n8n | `cmv-api` |
| Desenhar ou gerar um fluxo de chatbot ou automação | `cmv-flowbuilder` |
| Escrever o prompt do GPT Assistant ou ajustar a IA | `cmv-agente-ia` |
| Redigir respostas rápidas, templates, textos de campanha e de agendamento | `cmv-mensagens` |
| Mudar aparência ou comportamento do painel com CSS e JS | `cmv-painel-css-js` |

Esta skill continua valendo para a parte de "onde fica e como se usa" desses mesmos recursos: onde cadastrar o token da conexão, como abrir o editor de fluxos, onde colar o prompt, como criar uma campanha. Explique o uso e, quando o pedido passar para produzir o material, indique a skill vizinha.
