# Regras por tipo de mensagem (o que a documentação diz)

Fichas com o que os artigos da Central de Ajuda do Chat Master Veloz afirmam sobre cada tipo de mensagem. Aqui só entram fatos dos artigos. Onde está escrito **não documentado**, os artigos não dizem: não deduza, avise o usuário e sugira um teste com o próprio número antes de usar com clientes.

Os caminhos `references/docs/...` são relativos à pasta da skill. Ao citar um artigo para o usuário, use o título e o link da linha **Fonte** do cabeçalho dele; nas linhas **Artigos:** de cada ficha os dois já vêm juntos, copiados de lá. O caminho do arquivo serve para você abrir o artigo: não vai na resposta.

## Sumário

- [0. Variáveis: quatro sintaxes que não se misturam](#0-variáveis-quatro-sintaxes-que-não-se-misturam)
- [1. Resposta rápida](#1-resposta-rápida)
- [2. Template da API Oficial](#2-template-da-api-oficial)
- [3. Campanha comum (conexão por QR Code)](#3-campanha-comum-conexão-por-qr-code)
- [4. Campanha pela API Oficial](#4-campanha-pela-api-oficial)
- [5. Agendamento](#5-agendamento)
- [6. Mensagem de aniversário](#6-mensagem-de-aniversário)
- [7. Mensagens do Setor](#7-mensagens-do-setor)
- [8. Complementares: mensagens da Conexão e do Perfil](#8-complementares-mensagens-da-conexão-e-do-perfil)
- [9. Riscos que valem para vários tipos](#9-riscos-que-valem-para-vários-tipos)
- [10. Divergências entre artigos](#10-divergências-entre-artigos)
- [11. E-mail do Mail Marketing](#11-e-mail-do-mail-marketing)

---

## 0. Variáveis: quatro sintaxes que não se misturam

| Onde se usa | Sintaxe | Quem troca pelo valor | Artigo |
|---|---|---|---|
| Textos automáticos e mensagens da plataforma (mustaches) | `{{codigo}}`, por exemplo `{{firstName}}` | O sistema, no momento do envio | `references/docs/recursos/mustaches.md` |
| Texto de um template da API Oficial | `{{1}}`, `{{2}}`, `{{3}}`… numeradas em sequência | Quem envia: a campanha (campos extras da lista), o bloco Template, a integração | `references/docs/recursos/mensagem-template.md` |
| Valor digitado numa variável do bloco Template (FlowBuilder) | `{nome}`, `{email}`, `{extra1}` (campos do webhook) e `%variavel%` (variáveis do fluxo) | O fluxo | `references/docs/recursos/bloco-template.md` |
| Assunto e textos do modelo do Mail Marketing (e-mail) | `{{nome}}`, `{{primeiro_nome}}`, `{{email}}`, `{{descadastro}}` e `{{coluna}}` (colunas a mais da planilha da lista) | O Mail Marketing, no envio de cada e-mail | `references/docs/recursos/modelos-de-e-mail-blocos-e-html.md` (seção 11) |

### Lista oficial de mustaches (artigo Mustaches)

Fonte: `references/docs/recursos/mustaches.md`. Copie os códigos de lá, exatamente como estão.

| Grupo | Códigos |
|---|---|
| Contato | `{{contact_id}}` ID, `{{name}}` nome, `{{firstName}}` primeiro nome, `{{number}}` telefone |
| Setor | `{{queue}}` nome do setor, `{{queue_extra1}}`, `{{queue_extra2}}` campos extras do setor |
| Atendente | `{{user}}` nome do atendente do ticket, `{{user_extra1}}`, `{{user_extra2}}` campos extras do atendente |
| Ticket | `{{ticket_id}}` número do ticket, `{{protocol}}` protocolo rastreável, `{{protocol_random}}` protocolo aleatório |
| Conexão e empresa | `{{connection}}` nome da conexão, `{{name_company}}` nome da empresa |
| Texto e tempo | `{{ms}}` saudação (bom dia, boa tarde, boa noite, boa madrugada), `{{data_hora}}`, `{{date}}`, `{{hour}}`, `{{breakline}}` quebra de linha |
| Avançado (conexão e API) | `{{backendURL}}`, `{{connection_token}}` — não use em mensagem para cliente |

Regras do artigo Mustaches:

- Diferencia maiúsculas de minúsculas: `{{firstName}}` funciona, `{{firstname}}` não.
- Sem espaço dentro das chaves: `{{ ms }}` não é lido.
- Não dá para inventar código: o que não está na lista é enviado ao cliente literalmente, com as chaves.
- `{{firstName}}` sem nome salvo: o sistema tenta o nome público do perfil de WhatsApp do cliente.
- Os campos extras do atendente ficam em **Equipe › editar o usuário**, aba **Geral**; os do setor, em **Setores & Chatbot**, editando o Setor, aba **Geral**.

### O que cada artigo confirma sobre variáveis no seu campo

| Campo | O que o artigo do campo confirma |
|---|---|
| Resposta rápida de texto | "Você pode utilizar algumas Variáveis", com o exemplo `Olá {{firstName}}` trocado por "Olá Rodrigo" (o primeiro nome do contato). O artigo não lista os outros códigos. |
| Mensagem de saudação do Setor | `{{name}}`, com o exemplo `Olá, {{name}}! Você está no Suporte.` |
| URL da Avaliação Externa | Mustaches, com o exemplo `https://avaliachat.com.br/{{ticket_id}}/{{number}}` (`references/docs/recursos/avaliacoes.md`) |
| Mensagem de Encaminhamento (Configurações) | `{{ms}}` e `{{name}}`, com o exemplo `{{ms}} *{{name}}*, em alguns instantes um atendente irá prosseguir com seu atendimento.` (`references/docs/recursos/mensagens-automaticas-em-configuracoes.md`) |
| Template | `{{1}}`, `{{2}}`… |
| Mensagem simples de campanha, agendamento, mensagem de aniversário, mensagem de fora de expediente, mensagem de ausência, mensagem de conclusão/despedida | **não documentado** no artigo de cada campo |

O artigo Mustaches diz, de forma geral, que o mustache é trocado "em algum local que permite texto". Para os campos da última linha, isso não substitui a confirmação do artigo do campo: se usar, diga que é para testar antes.

---

## 1. Resposta rápida

**Onde se cadastra:** menu **Respostas Rápidas** › **Adicionar**. Para alterar, **ícone Lápis**; para apagar, **ícone Lixeira**.

**Como o atendente usa:** no chat, digita `/` seguido da primeira letra do **Atalho**; abre uma lista suspensa para escolher. Dica dos artigos: começar todo atalho com `/` (por exemplo `/saudação`), porque então `//` lista todos os atalhos cadastrados.

**Campos comuns**

| Campo | O que é |
|---|---|
| **Atalho** | Nome usado para chamar a resposta. Os exemplos dos artigos têm barra, espaço e acento: `/catalogo roupa`, `/fluxo apresentação`, `/localização`. |
| **Mensagem** | O texto, ou o código do tipo (tabela abaixo). |
| **Global** | Só Admin define. Ativada: todos os atendentes usam. Desativada: só quem cadastrou. |

**Tipos e o que vai no campo Mensagem**

| Tipo | Campo Mensagem | Extras | Artigo |
|---|---|---|---|
| Texto | O texto, com variáveis se quiser | — | `references/docs/recursos/resposta-rapida-envio-de-texto.md` |
| Mídia/arquivo | O mesmo nome do atalho entre colchetes. Atalho `/catalogo roupa` → mensagem `[/catalogo roupa]` | Botão **Anexar**; depois aparece o campo **Caption** (legenda, opcional) | `references/docs/recursos/resposta-rapida-envio-de-midia.md` |
| Contato | `<nome> Nome do Contato </nome> <telefone> 5511999999999 </telefone>` (WhatsApp no formato internacional) | — | `references/docs/recursos/resposta-rapida-envio-de-contato.md` |
| Localização | `<endereco> Uma mensagem qualquer aqui </endereco> <mapa> degreesLatitude: -22.950762, degreesLongitude: -43.2135083,18z </mapa>` (latitude e longitude tiradas da URL do local no Google Maps, depois do `@`) | — | `references/docs/recursos/resposta-rapida-envio-de-localizacao.md` |
| Fluxo | O mesmo nome do atalho entre colchetes. Atalho `/fluxo apresentação` → mensagem `[/fluxo apresentação]` | Campo **Fluxo de Automação** | `references/docs/recursos/resposta-rapida-de-fluxo.md`, `references/docs/recursos/gatilho-via-resposta-rapida.md` |

**Variáveis aceitas:** ver a seção 0. Confirmado no artigo: existem variáveis e o primeiro nome do contato é uma delas; a lista oficial de códigos está no artigo Mustaches.

**Limites e avisos**

- Legenda (Caption) do arquivo: até 4096 caracteres.
- Áudio: só `.mp3`. Áudio não suporta legenda: sem caption aparece como gravado na hora; com caption aparece como encaminhado.
- Nome do arquivo anexado: sem espaços, sem caracteres especiais e sem nome muito extenso.
- Cartão de contato: compartilhe apenas contatos que estão na agenda do celular daquele WhatsApp, para evitar risco de bloqueio da conta.
- Resposta rápida de fluxo: só Administradores cadastram. No fluxo chamado por ela não funcionam os blocos Menu, Pergunta e Http Request, e ele termina com o bloco **Encerrar Fluxo [Resposta Rápida]** (no artigo do gatilho, **Encerrar Mensagem Rápida**) ou com **Trocar Fluxo**. O desenho do fluxo é assunto da skill `cmv-flowbuilder`.
- Na conexão oficial, resposta rápida é mensagem comum: vale a regra da janela de atendimento (seção 9) e cada mensagem enviada entra na contagem de cobrança.
- Tamanho máximo do texto e do atalho: **não documentado**.

**Banco de ideias pronto:** `references/docs/recursos/ideias-de-respostas-rapidas.md` traz atalhos e textos por área (Vendas, Suporte, Financeiro, Logística, Geral).

---

## 2. Template da API Oficial

Só existe na conexão oficial. É o único formato permitido com a janela de atendimento fechada.

**Onde se cadastra:** menu **Conexões** › no card da conexão oficial, **Gestão de Templates** › **NOVO TEMPLATE**. A tela não está no menu lateral. Template criado no Gerenciador do WhatsApp, na Meta (caminho para tipos que a plataforma não oferece, como **Flows**, e para partir da **Biblioteca de modelos**), aparece depois de clicar em **SINCRONIZAR** (coluna **CRIADO POR** mostra **BM**; criado por integração mostra **API**).

**O assistente NOVO TEMPLATE, em três passos** (artigo Criar Template pela Plataforma):

| Passo | Campo | O que o artigo diz |
|---|---|---|
| 1. Configurar modelo | **Conexão WABA** | A conexão oficial onde o template vai existir. |
| | **MARKETING**, **UTILIDADE**, **AUTENTICAÇÃO** | As abas das categorias. |
| | **Tipo de mensagem** | **Padrão** (texto, mídia e botões, nas três abas); **Solicitação de permissões para ligação** (Marketing e Utilidade); outros só em Marketing, como **Catálogo**. |
| 2. Editar modelo | (todos) | Abrem com um exemplo de promoção já escrito: apague o que não for usar. |
| | **Nome do template** | A tela converte enquanto se digita: maiúscula vira minúscula e espaço vira sublinhado (`Pedido Pronto` vira `pedido_pronto`). |
| | **Idioma** | O idioma do texto. |
| | **Amostra de mídia** | Opcional: **Nenhum**, **Imagem**, **Vídeo**, **Documento** ou **Localização**; com mídia, o **Cabeçalho** passa a ser ela. |
| | **Cabeçalho** | Até 60 caracteres. |
| | **Corpo da mensagem** | Até 1.024 caracteres, com as variáveis `{{1}}`, `{{2}}`. |
| | **Exemplo para variável** | Um campo por variável; é o exemplo que a Meta lê na aprovação. Valor realista e inventado, nunca o dado de um cliente real. |
| | **Rodapé** | Até 60 caracteres. |
| | **Botões** | **Tipo** (**Resposta rápida**, **URL** ou **Telefone**) e **Texto do botão**; **URL** pede o endereço; **ADICIONAR BOTÃO** inclui outro. |
| 3. Enviar para análise | **ENVIAR PARA APROVAÇÃO** | A tela resume **Nome**, **Categoria** e **Idioma**; **VOLTAR** corrige. |

Nas listas, a categoria aparece como `MARKETING`, `UTILITY` ou `AUTHENTICATION`, com o idioma ao lado (`pt_BR`). Na campanha, o **extra1** é a URL da imagem do cabeçalho e os extras a partir do 7 preenchem botões.

**Estados:** o filtro **Status** da **Gestão de Templates** fala em pendente, submetido, aprovado e rejeitado; o artigo Template Recusado, Pausado ou Desabilitado descreve as situações da Meta: **Em análise**, **Ativo** (com qualidade **Pendente**, **Alta**, **Média** ou **Baixa**), **Rejeitado**, **Apelação feita – Em análise**, **Pausado** e **Desabilitado**. Só template aprovado aparece para envio.

**Variáveis:** `{{1}}`, `{{2}}`… quantas o texto pedir, numeradas em sequência. Cada uma precisa receber valor no envio; variável vazia faz a Meta recusar a mensagem (erro de parâmetro faltando). Na campanha só há campos para `{{1}}` a `{{5}}` (seção 4).

**Categorias: a pergunta que decide**

| Categoria | Pergunta do artigo | Serve para | Texto |
|---|---|---|---|
| Utilidade | "O cliente está esperando isto porque fez alguma coisa antes?" Se sim, é Utilidade. | Fatura e boleto, status de pedido, confirmação de agendamento, aviso de problema na conta | Rígido: a Meta recusa se houver propaganda. "Informe e pare. Sem adjetivo, sem chamada para ação de venda." |
| Marketing | "O cliente pediu isto agora, ou sou eu que quero mostrar?" Se é você, é Marketing. | Oferta e cupom, lançamento, carrinho abandonado, felicitação de aniversário, convite, mensagem de bom dia | Aceita linguagem vendedora. É a categoria mais cara. |
| Autenticação | — | Código de verificação | Não aceita nada além do código. |

"Serviço" é a quarta categoria de conversa, mas não é template: é o atendimento comum dentro da janela.

**Limites e avisos**

- Mensagem misturada: um modelo quase todo de Utilidade com uma única frase de Marketing vira Marketing inteiro. Fatura numa mensagem, oferta em outra.
- Aprovação: "em geral algumas horas, mas pode ser dias" (Mensagem Template); "pode levar até 24 horas" (Criar Template pela Plataforma). A análise é da Meta (seção 10).
- Editar um template aprovado manda de volta para análise e ele para de funcionar até ser aprovado de novo. Template recusado pode ser editado quantas vezes for preciso.
- Excluir apaga na plataforma **e na Meta**; o nome de um template aprovado excluído só pode ser reusado depois de 30 dias.
- Pausa: com qualidade **Baixa**, a Meta pausa o template 3 horas na primeira vez e 6 na segunda; na terceira, ele é desabilitado e não volta (crie outro, com outro texto). Pausado, não é enviado nem cobrado.
- Categoria errada: dá para contestar logo depois de criar; se a Meta negar, a saída é apagar e criar outro com texto diferente.
- Cada conexão tem os seus templates: o mesmo texto precisa ser aprovado em cada número.
- O que causa reprovação, pausa ou bloqueio está reunido na lista única logo abaixo.
- Todo template enviado é cobrado pela Meta conforme a categoria (roteiro de custo na seção 9). Não cite valores.
- Grupos de templates: em **GRUPOS** você agrupa modelos; no cadastro do Setor, o campo **Grupos de templates** define o que a equipe enxerga. Vazio mostra todos. Setor com grupo vazio: a equipe não vê nenhum template na conversa.
- Envio falhou com template aprovado: botão **Erros de Template** no card da conexão; o artigo Erros de Entrega do WhatsApp Oficial traduz os códigos (variável faltando, idioma, formato do valor).
- Limite de caracteres dos botões e número máximo de botões: **não documentado**.
- Como o atendente escolhe e preenche o template dentro da conversa: **não documentado** em detalhe.

### "Que não seja reprovado": lista única do que os artigos apontam

Use esta lista quando a pessoa pedir um template "que passe". Diga sempre duas coisas: a análise é da Meta ("a plataforma só mostra o resultado") e a aprovação não pode ser garantida; o que dá para fazer é tirar do texto as causas que os artigos registram.

| O que os artigos apontam | Consequência descrita | Artigo |
|---|---|---|
| Linguagem vendedora em modelo de Utilidade (adjetivo, chamada para ação de venda) | "A Meta recusa na análise, e o modelo volta sem aprovação" | `references/docs/recursos/mensagem-template.md` |
| Propaganda ou oferta dentro de um aviso de serviço | "A Meta recusa se houver propaganda dentro"; com uma única frase de Marketing, o modelo inteiro vira Marketing e o custo sobe | `references/docs/recursos/mensagem-template.md` |
| Marketing cadastrado como Utilidade | Listado entre as causas de bloqueio no canal oficial ("template na categoria errada"). A classificação pode ser contestada logo depois de criar; se a Meta negar, só apagando e criando outro com texto diferente | `references/docs/recursos/numero-bloqueado-no-whatsapp.md`, `references/docs/recursos/mensagem-template.md` |
| Conteúdo proibido: urgência artificial, links encurtados, produtos vedados | Listado entre as causas de bloqueio no canal oficial ("template com conteúdo proibido"). Prevenção do artigo: não usar encurtador de URL | `references/docs/recursos/numero-bloqueado-no-whatsapp.md` |
| Modelo de Autenticação com qualquer coisa além do código | "Não aceita nada além do código" | `references/docs/recursos/mensagem-template.md` |
| Envio para quem não deu opt-in; marketing sem opt-out claro | Queda da qualidade do número e suspensão de conta; opt-in é exigência no canal oficial | `references/docs/recursos/numero-bloqueado-no-whatsapp.md` |
| Destinatários denunciando ou bloqueando o número | Qualidade baixa; template pausado por baixa qualidade. Continuar enviando com o template que derrubou a qualidade piora o índice | `references/docs/recursos/numero-bloqueado-no-whatsapp.md` |
| Variável faltando ou com as chaves erradas, com caracteres especiais (#, $, %), fora de ordem (`{{1}}` e depois `{{3}}`), em número demais para o tamanho do texto, ou no começo ou no fim do texto | A Meta recusa o template. Escreva ao menos uma palavra antes da primeira variável e depois da última | `references/docs/recursos/template-recusado-pausado-ou-desabilitado.md` |
| Pedido de dado sensível completo (número do cartão, conta bancária, documento); texto abusivo, ameaçador ou com cara de spam ou golpe; corpo e rodapé iguais aos de outro template | A Meta recusa o template (os 4 últimos dígitos, por exemplo, são permitidos) | `references/docs/recursos/template-recusado-pausado-ou-desabilitado.md` |
| Variável sem valor na hora do envio | Não é reprovação: é recusa do envio, com erro de parâmetro faltando (código 132000) | `references/docs/recursos/mensagem-template.md`, `references/docs/recursos/erros-de-entrega-do-whatsapp-oficial.md` |
| Envio diferente do que foi aprovado (por exemplo, cabeçalho maior do que o permitido) | Falha no envio; o motivo aparece em **Erros de Template** | `references/docs/recursos/whatsapp-oficial-gestao-de-templates.md` |
| Editar um modelo aprovado | Volta para análise e para de funcionar até nova aprovação | `references/docs/recursos/mensagem-template.md`, `references/docs/recursos/whatsapp-oficial-gestao-de-templates.md` |

**Não documentado nestes artigos** (não afirme regra da Meta de memória; diga que a documentação não traz e que vale o que a tela de criação e a análise da Meta indicarem):

- A proporção exata entre texto e variáveis (o artigo só diz que variáveis "em número demais para o tamanho do texto" levam à recusa) e o número máximo de botões.
- Divergência a avisar: os modelos do artigo Mensagem Template terminam em variável (`...link para pagamento: {{2}}`), e o artigo Template Recusado, Pausado ou Desabilitado diz que variável no fim do texto leva à recusa. Escreva uma palavra depois da última variável.

O motivo de uma recusa chega por e-mail a quem administra a conta de mensagens e aparece na **Página Inicial do Suporte para Empresas**, na Meta; **Erros de Template** trata de envios recusados.

**Onde o template é usado:** campanha pela API Oficial (seção 4), agendamento (seção 5), bloco Template do FlowBuilder (skill `cmv-flowbuilder`), envio por API (skill `cmv-api`).

**Artigos:** [Mensagem Template](https://clihelper.chatmasterveloz.com/docs/mensagem-template) (`references/docs/recursos/mensagem-template.md`), [Gestão de Templates](https://clihelper.chatmasterveloz.com/docs/whatsapp-oficial-gestao-de-templates) (`references/docs/recursos/whatsapp-oficial-gestao-de-templates.md`), [Template](https://clihelper.chatmasterveloz.com/docs/bloco-template) (`references/docs/recursos/bloco-template.md`), [Número bloqueado no WhatsApp](https://clihelper.chatmasterveloz.com/docs/numero-bloqueado-no-whatsapp) (`references/docs/recursos/numero-bloqueado-no-whatsapp.md`), [Criar Template pela Plataforma](https://clihelper.chatmasterveloz.com/docs/criar-template-pela-plataforma) (`references/docs/recursos/criar-template-pela-plataforma.md`), [Criar Template no Gerenciador do WhatsApp](https://clihelper.chatmasterveloz.com/docs/criar-template-no-gerenciador-do-whatsapp) (`references/docs/recursos/criar-template-no-gerenciador-do-whatsapp.md`), [Template Recusado, Pausado ou Desabilitado](https://clihelper.chatmasterveloz.com/docs/template-recusado-pausado-ou-desabilitado) (`references/docs/recursos/template-recusado-pausado-ou-desabilitado.md`), [Erros de Entrega do WhatsApp Oficial](https://clihelper.chatmasterveloz.com/docs/erros-de-entrega-do-whatsapp-oficial) (`references/docs/recursos/erros-de-entrega-do-whatsapp-oficial.md`).

---

## 3. Campanha comum (conexão por QR Code)

**Onde se cadastra:** menu **Campanhas** › botão **NOVA CAMPANHA**. A lista de destinatários é criada antes, no menu **Campanhas › Criar Listas**. Os intervalos de envio ficam nas configurações de campanhas (artigo Configurar Campanhas; o botão exato para chegar à tela é **não documentado**).

**Campos, na ordem dos passos**

| Passo | Campo | O que é |
|---|---|---|
| 01 | **Nome** | Nome da campanha. |
| 01 | **Caracteres Ocultos** | Envia caracteres ocultos (no Android) para diferenciar mensagens repetidas perante os robôs da Meta. |
| 01 | **Usar Proxy** | Opção avançada; normalmente **Não**. |
| 02 | Fonte de contatos | Uma só: **Lista de Contato**, **Tags**, **Grupos** (envia no privado de cada participante) ou **Aniversário** (mês). |
| 03 | **Agendamento** | Data e horário em que os disparos começam. |
| 03 | **Pausar automaticamente** / **Reiniciar Automaticamente** | Horário de parar no dia e de retomar. Vazio: segue sem interrupção. |
| 04 | **Abrir Ticket** | Se o ticket fica aberto (Aguardando) depois do envio. Se não abrir, o ticket é fechado depois do envio, mesmo que já esteja em atendimento. |
| 04 | **Fila** | Fila do ticket, se abrir ticket. |
| 04 | **Mensagem de Descadastramento** | Rodapé explicando ao contato como se descadastrar da campanha. Como palavra de saída, escreva PARAR, não SAIR: no menu de opções do chatbot do Setor, quem responde **SAIR** encerra o atendimento (`references/docs/recursos/chatbot-e-menu-de-setores-na-conexao.md`). |
| 04 | **Conexão** | Uma ou mais. Com mais de uma, o sistema alterna as conexões remetentes. |
| 05 | **Campanha via fluxo** | **Fluxo de Bot** (Typebot) ou **Fluxos de Automação** (FlowBuilder Nativo). |
| 05 | **Campanha via mensagem simples** | **5 variações da mesma mensagem**, enviadas aleatoriamente para evitar texto repetido. |
| 05 | **Gatilho** | Envia antes uma mensagem gatilho e só manda a principal se o contato responder. |
| 05 | **Caption** | Se as mensagens viram legenda quando há **ANEXAR ARQUIVO**. |

**Listas (Campanhas › Criar Listas):** **Lista Manual** (um a um, ou planilha por **Importar**; cada contato tem nome, número, e-mail e **Campos Extras** de 1 a 10), **Por Tag**, **Por Grupo**, **Por Aniversário**, **Por Conexão**. Cada campanha usa uma lista só. A lista guarda os contatos do momento em que foi criada: quem ganhou a tag depois não entra; para atualizar, crie a lista de novo. A lista de campanha não tem relação com o menu **Contatos**. Há planilha modelo para download no artigo.

**Variáveis na mensagem simples:** **não documentado** nos artigos de Campanhas (ver seção 0).

**Intervalos (Configurar Campanhas)**

- Um lote acontece a cada **2 minutos**.
- **Mensagens por Lote**, **Delay Mínimo** e **Delay Máximo** (tempo entre uma mensagem e outra dentro do lote).
- Sugestão cautelosa do artigo: Delay Mínimo 60 segundos, 2 mensagens por lote, Delay Máximo 100 segundos.

**Limites e avisos**

- Risco de a Meta bloquear o chip ao usar envio em massa. Motivos principais citados: denúncia de SPAM, envio de mensagem em massa, negócio fora dos termos de uso da Meta.
- No canal não oficial, causam bloqueio: envio para quem não tem o número salvo na agenda, mensagens idênticas ou muito parecidas em sequência, taxa de denúncia ou bloqueio acima de 2%, volume muito acima do histórico recente, ritmo robótico. O risco nunca é zero, e o bloqueio pode ser permanente.
- Em qualquer canal: nunca enviar para listas compradas ou sem consentimento; não repetir o mesmo texto para muitos contatos em sequência; taxa baixa de resposta é sinal de problema.
- O fuso horário da empresa (**Configurações › Opções › Geral**, seção **Empresa e região**) vale para agendamentos e campanhas (`references/docs/recursos/gerenciamento-de-expediente-em-configuracoes.md`).
- Tamanho máximo da mensagem e como a plataforma trata a resposta de descadastramento: **não documentado**.
- Repetição automática de campanha (toda semana, todo mês): **não documentado**. Os artigos só descrevem a data e hora de início (**Agendamento**), a pausa e o reinício no dia.
- Campanha via fluxo: ver `references/docs/recursos/gatilho-via-campanha.md`; o fluxo é assunto da `cmv-flowbuilder`.

**Artigos:** [Campanhas](https://clihelper.chatmasterveloz.com/docs/campanhas) (`references/docs/recursos/campanhas.md`), [Nova Campanha](https://clihelper.chatmasterveloz.com/docs/nova-campanha) (`references/docs/recursos/nova-campanha.md`), [Configurar Campanhas](https://clihelper.chatmasterveloz.com/docs/configurar-campanhas) (`references/docs/recursos/configurar-campanhas.md`), [Fontes de Contatos para Campanhas](https://clihelper.chatmasterveloz.com/docs/fontes-de-contatos-para-campanhas) (`references/docs/recursos/fontes-de-contatos-para-campanhas.md`), [Número bloqueado no WhatsApp](https://clihelper.chatmasterveloz.com/docs/numero-bloqueado-no-whatsapp) (`references/docs/recursos/numero-bloqueado-no-whatsapp.md`), [Chatbot e Menu de Setores na Conexão](https://clihelper.chatmasterveloz.com/docs/chatbot-e-menu-de-setores-na-conexao) (`references/docs/recursos/chatbot-e-menu-de-setores-na-conexao.md`).

---

## 4. Campanha pela API Oficial

Dispara um template já aprovado para uma lista. Não há texto livre: o que se redige é o template (seção 2) e os valores das variáveis.

**Onde se cadastra:** menu **Campanhas** › **NOVA CAMPANHA** (mesma tela da seção 3).

**O que muda nos campos**

| Campo | Na API Oficial |
|---|---|
| **Gatilho** | Não utilize. |
| **Caracteres Ocultos** | Não utilize. |
| **Mensagem de Descadastramento** | Não utilize (é o que o artigo diz). Recomendação desta skill, para template de Marketing: pôr a opção de saída no próprio texto. |
| **Conexão** | Apenas uma. Não use multiconexões. |
| Passo 05 | Escolha um template pré-cadastrado. |
| **Fluxos de Automação** | Inicia um fluxo do FlowBuilder Nativo depois da resposta do contato; o campo **Fila** precisa ter uma fila vinculada ao mesmo fluxo. |

**Template com variáveis:** a fonte de contatos tem de ser uma **Lista de Contato** criada em **Campanhas › Criar Listas**. Colunas da planilha:

| Coluna | Conteúdo |
|---|---|
| `nome` | Nome do contato |
| `numero` | Telefone no formato internacional, somente números |
| `e-mail` | E-mail, se desejar |
| `extra1` | URL da imagem do cabeçalho do template |
| `extra2` | Valor da variável `{{1}}` |
| `extra3` | Valor da variável `{{2}}` |
| `extra4` | Valor da variável `{{3}}` |
| `extra5` | Valor da variável `{{4}}` |
| `extra6` | Valor da variável `{{5}}` |
| `extra7`, `extra8` | Botões (1º e 2º) |
| `extra9` | Texto do 3º botão, segundo o artigo Nova Campanha API Oficial; "livre", segundo o artigo Fontes de Contatos (seção 10) |
| `extra10` | Livre |

Repare no deslocamento: o **extra2** é a `{{1}}`. **Edição em Massa**, na lista, preenche os Campos Extras de todos os contatos de uma vez (útil quando o valor é igual para todos, como um cupom); recarregue a página antes, se acabou de incluir contatos.

**Limites e avisos**

- Variável sem valor: a Meta recusa e a mensagem não chega.
- Limite de envio do canal oficial: máximo de contatos diferentes com quem a conta inicia conversa por dia, na escala 250 → 2.000 → 10.000 → 100.000 → ilimitado. É da conta, não de cada número. Atingir o limite não é bloqueio: os envios param e retomam no dia seguinte.
- Erro 131049 ("usuário saturado"): o WhatsApp limita quantas mensagens de marketing um contato recebe por dia, de todas as empresas somadas. Só resta tentar no dia seguinte.
- Com a qualidade baixa, o artigo recomenda não mais de um template de marketing por dia para o mesmo contato.
- Número novo: warm-up, começando com volume baixo e aumentando cerca de 20% por dia.
- Opt-in é exigência no canal oficial: só enviar para quem solicitou ou aceitou receber.
- Cobrança: todo template é cobrado conforme a categoria (seção 9).
- Repetição automática de campanha (por exemplo, todo dia 5): **não documentado**. Os artigos só descrevem a data e hora de início (**Agendamento**), a pausa e o reinício no dia. O que está descrito é criar a campanha de novo a cada vez; a lista continua em **Minhas Listas** e pode ser escolhida em outra campanha, com os Campos Extras atualizados (por planilha ou **Edição em Massa**).
- O fuso horário da empresa (**Configurações › Opções › Geral**, seção **Empresa e região**) vale para campanhas (`references/docs/recursos/gerenciamento-de-expediente-em-configuracoes.md`).

**Artigos:** [Nova Campanha API Oficial](https://clihelper.chatmasterveloz.com/docs/nova-campanha-api-oficial) (`references/docs/recursos/nova-campanha-api-oficial.md`), [Fontes de Contatos para Campanhas](https://clihelper.chatmasterveloz.com/docs/fontes-de-contatos-para-campanhas) (`references/docs/recursos/fontes-de-contatos-para-campanhas.md`), [Número bloqueado no WhatsApp](https://clihelper.chatmasterveloz.com/docs/numero-bloqueado-no-whatsapp) (`references/docs/recursos/numero-bloqueado-no-whatsapp.md`), [Mensagem Template](https://clihelper.chatmasterveloz.com/docs/mensagem-template) (`references/docs/recursos/mensagem-template.md`).

---

## 5. Agendamento

Mensagem programada para um contato, única ou recorrente.

**Onde se cadastra:** menu **Agendamentos** › **+ Nova Agendamento**; ou dentro da conversa, no botão **Agendamento** das ações do topo do ticket (o contato já vem preenchido; quando não cabe, fica no botão **⋯**, e com as ações agrupadas, no botão **Mais**, grupo **ATENDIMENTO**).

**Campos**

| Campo | O que é |
|---|---|
| **Contato** | Busca digitando pelo menos 3 letras. O destinatário precisa estar cadastrado em Contatos. Um contato por agendamento. O único envio em lote documentado é a **Mensagem a todos os atendimentos** de um atendente (abaixo). |
| **Conexão** | Qual conexão envia. |
| **Fila** (o artigo Editar Agendamento já chama de **Setor**) | Opcional; só funciona com **Abrir Ticket**. |
| **Mensagem Template** | Aparece quando a conexão é API Oficial (Cloud). |
| **Mensagem** | O texto. |
| **Anexar Arquivo** | Ícone de clipe. |
| **Data e Horário do Envio** | Dia e minuto do primeiro (ou único) disparo. |
| **Abrir Ticket** | Não: envio silencioso. Sim: abre o chat para o atendente. Valor que vem marcado por padrão: **não documentado**. |
| **Criar Anotação** | Sim: o texto não vai ao cliente; vira mensagem interna no ticket. |
| **Repetir a cada** | "Não Repetir", uma frequência (a cada 1 dia, 7 dias…), **Todo dia...** (dia fixo do mês) ou a cada **Ano**. |
| **Repetir todo dia** | O dia do mês, quando **Repetir a cada** está em **Todo dia...**. |
| **Quantas vezes repetir** | Número fixo (por exemplo 12) ou "Ilimitado". |

Botão que grava um agendamento novo: **não documentado** (o artigo Adicionar Agendamento não dá o nome; o de edição manda clicar em **Salvar**).

**Variáveis no campo Mensagem:** **não documentado**. Como as variáveis `{{1}}`, `{{2}}` de um template são preenchidas num agendamento: **não documentado**.

**Cobrança ou aviso que se repete, na conexão oficial**

| Situação | Caminho | O que dizer |
|---|---|---|
| Mesmo texto para o cliente, todo mês | Agendamento com template de **texto fixo** (sem `{{n}}`), **Repetir a cada** › **Todo dia...** | Um agendamento por contato. Não use template com variável aqui: o preenchimento não está documentado. |
| Nome, valor ou link diferentes por cliente | Campanha pela API Oficial com **Lista de Contato** e campos extras (seção 4) | Repetição automática de campanha não está documentada: pelo que os artigos descrevem, é uma campanha a cada mês. |
| Muitos clientes, texto fixo | Agendamento em lote só existe para os atendimentos abertos de um atendente (**Mensagem a todos os atendimentos**, abaixo) | Para uma lista de clientes, ofereça a campanha (seção 4) ou um agendamento por contato. |

**Na conexão oficial**

- É obrigatório escolher um template aprovado. A caixa de texto é preenchida com o nome do template; o que for digitado por cima é ignorado e sobrescrito pelo texto original no envio.
- Texto comum e anexo comum não são enviados de forma agendada pela API Oficial, mesmo com a janela de 24 horas aberta. Sem template, o envio falha.
- Exceção: agendamento só com **Criar Anotação**, que é comunicação interna.

**Mensagem a todos os atendimentos (de um atendente)**

Um aviso só para todos os clientes que estão em atendimento aberto com uma pessoa ("a Ana saiu de férias, quem assume é o Bruno"). Só está descrita na nota de atualização de 21/11/2026 (`references/docs/recursos/atualizacoes-2026-11-21.md`).

- **Onde:** menu **Quadro de atendimentos**, visão **Atendentes**, ícone do avião de papel na coluna da pessoa (**Enviar mensagem a todos os atendimentos deste atendente**). Só administrador e supervisor veem o botão.
- **Quem recebe:** os contatos dos atendimentos abertos daquela pessoa, uma vez cada, mesmo que apareçam em mais de um atendimento. Os filtros e a busca do Quadro valem: só entra o que o Quadro mostra. Atendimento que ainda aguarda a pessoa aceitar não recebe.
- **Campos:** **Enviar pela conexão**, **Mensagem** e **Intervalo entre os envios** (de 15 segundos a 5 minutos). O botão **Agendar para N contato(s)** confirma.
- **Variáveis:** `{{name}}` e `{{firstName}}`. Outras variáveis nesse campo: **não documentado**.
- **Como sai:** cada contato vira um agendamento, um depois do outro, começando em 1 minuto. Aparecem no menu **Agendamentos**, onde **Excluir** cancela cada um.
- **Na conexão oficial:** a nota não diz se a janela pede template. Como o envio vira agendamento, e agendamento na oficial só sai com template (acima), avise a pessoa e peça um teste com um atendimento antes de mandar para todos.
- Anexo, data e hora escolhidas e repetição nessa janela: **não documentado**.

**Limites e avisos**

- A recorrência segue a data inicial: para cobrar todo dia 05, a **Data e Horário do Envio** inicial tem de ser um dia 05.
- Fuso horário: o **Fuso horário da empresa**, em **Configurações › Opções › Geral**, seção **Empresa e região**, vale para agendamentos, campanhas e expediente. Sem escolha, o sistema usa o horário de Brasília; mudar o fuso muda a hora dos agendamentos. Ajuste antes de programar envios (`references/docs/recursos/gerenciamento-de-expediente-em-configuracoes.md`).
- Na oficial, o template agendado é cobrado conforme a categoria (seção 9); a dúvida comum do artigo Adicionar Agendamento sobre Utilidade com a janela aberta traz a regra anterior (seção 10).
- Agendamento enviado não pode ser editado; crie outro.
- Excluir um agendamento recorrente pendente cancela todos os envios futuros do ciclo, sem volta.
- Cancele com antecedência: na virada do horário o status passa a "Processando" e a lixeira é bloqueada.
- Status na lista: **Pendente**, **Agendada**, **Enviada**, **Erro**.
- Tamanho máximo do texto: **não documentado**.

**Artigos:** [Adicionar Agendamento](https://clihelper.chatmasterveloz.com/docs/adicionar-agendamento) (`references/docs/recursos/adicionar-agendamento.md`), [Editar Agendamento](https://clihelper.chatmasterveloz.com/docs/editar-agendamento) (`references/docs/recursos/editar-agendamento.md`), [Excluir Agendamento](https://clihelper.chatmasterveloz.com/docs/excluir-agendamento) (`references/docs/recursos/excluir-agendamento.md`), [Visão Geral Agendamentos](https://clihelper.chatmasterveloz.com/docs/visao-geral-agendamentos) (`references/docs/recursos/visao-geral-agendamentos.md`), [Agendamentos](https://clihelper.chatmasterveloz.com/docs/agendamentos) (`references/docs/recursos/agendamentos.md`), [Gerenciamento de Expediente em Configurações](https://clihelper.chatmasterveloz.com/docs/gerenciamento-de-expediente-em-configuracoes) (`references/docs/recursos/gerenciamento-de-expediente-em-configuracoes.md`).

---

## 6. Mensagem de aniversário

Um texto único, enviado sozinho no dia do aniversário do contato, sempre às 10 horas da manhã, no fuso horário da empresa.

**Onde se cadastra:** menu **Configurações › Opções › Automação**, seção **Mensagens automáticas**, campo **Mensagem de Aniversário (enviada todos os dias às 10 horas, no fuso da empresa)**. Os dois artigos dão o mesmo caminho.

**O que precisa estar pronto**

| Onde | O quê |
|---|---|
| **Contatos › editar o contato**, campo **Aniversário** | **Dia** e **Mês**; o **Ano** é opcional. Data escrita em anotações não vale. |
| **Conexões › Editar › Geral** | Uma conexão marcada como **Padrão**: é ela que envia. Sem conexão padrão, o disparo falha. |
| Campo **Mensagem de Aniversário** | O texto. Vazio, nada é enviado. |

**Variáveis:** **não documentado** nos dois artigos.

**Limites e avisos**

- O horário (10h) não pode ser mudado. Ele segue o **Fuso horário da empresa**, no menu **Configurações › Opções › Geral**, seção **Empresa e região**.
- Na API Oficial, o disparo obedece à janela de 24 horas: com a janela fechada, a mensagem de texto comum é bloqueada pelo WhatsApp. Os artigos não descrevem uso de template nesse campo.
- Alternativa documentada para alcançar aniversariantes: lista **Por Aniversário** (contatos que fazem aniversário no mês escolhido) em **Campanhas › Criar Listas**, usada numa campanha. Felicitação de aniversário, como template, é categoria Marketing.
- Erro comum do artigo: escrever só "Feliz aniversário", sem chamada para ação (um link, um mimo ou uma pergunta).

**Artigos:** [Mensagem de Aniversário](https://clihelper.chatmasterveloz.com/docs/mensagem-de-aniversario) (`references/docs/recursos/mensagem-de-aniversario.md`), [Mensagens automáticas em Configurações](https://clihelper.chatmasterveloz.com/docs/mensagens-automaticas-em-configuracoes) (`references/docs/recursos/mensagens-automaticas-em-configuracoes.md`), [Fontes de Contatos para Campanhas](https://clihelper.chatmasterveloz.com/docs/fontes-de-contatos-para-campanhas) (`references/docs/recursos/fontes-de-contatos-para-campanhas.md`).

---

## 7. Mensagens do Setor

**Onde se cadastra:** menu **Setores & Chatbot** › editar o Setor › aba **Mensagens** › **Salvar**.

**Campos**

| Campo | O que é | Variáveis |
|---|---|---|
| **Mensagem de saudação** | O que o cliente recebe ao chegar no Setor (a Conexão aponta só para ele, ou ele escolheu no menu). É enviada de novo quando o cliente volta depois de o atendimento ter sido encerrado. | `{{name}}` confirmado no artigo |
| **Mensagem de fora de expediente** | O que o cliente recebe ao escrever com o Setor fechado. O campo só aparece com o expediente por Setor ligado: **Configurações › Opções › Geral**, **Gerenciamento de Expediente** em **Gerenciamento Por Setor**. Os horários ficam na aba **Horários** do Setor. | **não documentado** |
| **Despedida ao encerrar** e **Mensagem de despedida do setor** | A regra da despedida nos atendimentos do Setor e o texto dela. A do Setor vale quando o atendente não tem a dele; sem nenhuma, vai a **Mensagem de conclusão** da Conexão (seção 8). | **não documentado** |
| **Palavras-Chave e Gatilhos** | Palavras separadas por vírgula, como `boleto,fatura`. Quem escreve uma delas vai direto para o Setor e recebe a saudação dele. Vale no meio da frase, sem diferença de maiúsculas, minúsculas e acento. | Não se aplica |

**Limites e avisos**

- Saudação vazia não impede o Setor de funcionar, mas o cliente não recebe retorno nenhum.
- Uma boa saudação, segundo o artigo: diz onde a pessoa chegou, avisa que alguém vai atender e, se for o caso, informa o horário. "Duas ou três linhas bastam."
- Não prometa o que o Setor não cumpre ("responderemos em instantes" num Setor que só atende à tarde).
- A saudação do Setor e a da Conexão são textos diferentes e **somam**: com as duas preenchidas, o cliente recebe as duas (`references/docs/recursos/adicionar-whatsapp-qrcode.md`, `references/docs/recursos/adicionar-whatsapp-oficial.md`).
- O que acontece fora do horário depende de **Abrir Atendimentos Fora do Expediente?** em **Configurações › Opções › Geral**, seção **Gerenciamento de Expediente**: em **Sim**, a conversa entra no Setor e o cliente recebe a mensagem de fora de expediente e a saudação; em **Não**, recebe só a de fora de expediente e o atendimento é encerrado (`references/docs/recursos/aba-horarios-em-setores-e-chatbot.md`). Isso muda o que o texto pode prometer.
- Tamanho máximo: **não documentado**.

**Artigo:** [Aba Mensagens em Setores & Chatbot](https://clihelper.chatmasterveloz.com/docs/aba-mensagens-em-setores-e-chatbot) (`references/docs/recursos/aba-mensagens-em-setores-e-chatbot.md`).

---

## 8. Complementares: mensagens da Conexão, do atendente e da empresa

Campos de mensagem automática que ficam fora do Setor: na Conexão, no cadastro e no Perfil do atendente e em **Configurações**.

| Mensagem | Onde se cadastra | Regras do artigo | Artigo |
|---|---|---|---|
| **Mensagem de saudação** da Conexão | **Conexões › editar a Conexão › aba Mensagens** | Quando a conversa começa. Com dois ou mais Setores marcados na Conexão ela é obrigatória e abre o menu: o sistema acrescenta sozinho uma linha por Setor, no formato "1 - Suporte". | `references/docs/recursos/chatbot-e-menu-de-setores-na-conexao.md` |
| **Mensagem de conclusão** | **Conexões › editar a conexão › aba Mensagens**, campo **Mensagem de conclusão** | A despedida base, enviada quando o atendente escolhe **Resolver Com Mensagem de Encerramento** (**Encerrar com despedida** no pop-up de encerrar, pela nota de atualização de 20/11/2026) e nem ele nem o Setor têm texto próprio. Deve ser uma afirmação final, sem pergunta: se o cliente responder, abre um ticket novo. | `references/docs/recursos/mensagem-de-encerramento.md` |
| **Mensagem de Despedida** do atendente | **Equipe › editar o usuário › aba Geral**, campo **Mensagem de Despedida** | Tem prioridade sobre a do Setor e a da Conexão, mas só funciona se a da Conexão também estiver preenchida. Se a despedida é obrigatória, opcional ou desligada, decide o campo **Despedida ao encerrar** do atendente, do Setor e da Conexão de WhatsApp e, por último, **Despedida obrigatória ao encerrar?** em **Configurações › Opções › Atendimento**. Obrigatória, o **Resolver Sem Mensagem de Encerramento** some. | `references/docs/recursos/mensagem-de-encerramento.md` |
| **Mensagem de Ausência** | Ícone de pessoa no canto superior direito › **Perfil** › campo **Mensagem de Ausência** › **Salvar**; depois, status **Ausente** | Só dispara nos tickets em que o usuário já é o atendente, e a cada nova mensagem do cliente enquanto o status estiver Ausente. Diga quando volta. | `references/docs/recursos/mensagem-de-ausencia.md` |
| **Mensagem de fora de expediente** da Conexão | **Conexões › editar a Conexão › aba Mensagens** | Só dispara se o expediente estiver configurado. | `references/docs/recursos/adicionar-whatsapp-qrcode.md` |
| **Mensagem de avaliação** da Conexão | **Conexões › editar a Conexão**, campo **Mensagem de Avaliação** | Os artigos descrevem de dois jeitos: no artigo Avaliações é a mensagem de pós-avaliação, enviada depois que o cliente escolhe a nota, quando a opção dessa nota está em **Nenhum** no campo **Fluxo após esta nota** (nota com fluxo começa o fluxo e não envia a mensagem); no artigo da Conexão é "o convite para o cliente avaliar o atendimento". A pergunta e as opções da pesquisa ficam no menu **Avaliações** (campo **Mensagem de Avaliação** da avaliação, mais **Opções de Avaliação**). Avise da divergência e sugira um teste. | `references/docs/recursos/avaliacoes.md`, `references/docs/recursos/adicionar-whatsapp-qrcode.md` |
| **Mensagem Saída Forçada** | **Configurações › Opções › Automação**, seção **Mensagens automáticas** | Enviada quando o atendimento é encerrado pelo sistema, não pelo atendente. | `references/docs/recursos/mensagens-automaticas-em-configuracoes.md` |
| **Mensagem de Encaminhamento** | Mesma seção | Enviada ao cliente quando a conversa é encaminhada a um atendente (por exemplo, pelo rodízio). Vale para toda a empresa. Aceita `{{ms}}` (saudação do horário) e `{{name}}`, com o exemplo `{{ms}} *{{name}}*, em alguns instantes um atendente irá prosseguir com seu atendimento.` | `references/docs/recursos/mensagens-automaticas-em-configuracoes.md` |
| **Mensagem de encerramento após inatividade** | **Conexões › editar a Conexão › aba Mensagens** | Aviso enviado quando a plataforma fecha a conversa por falta de resposta. | `references/docs/recursos/adicionar-whatsapp-qrcode.md` |

Variáveis nesses campos: **não documentado** no artigo de cada campo, salvo a **Mensagem de Encaminhamento** (ver seção 0).

---

## 9. Riscos que valem para vários tipos

| Risco | O que os artigos dizem | Artigo |
|---|---|---|
| Janela de atendimento (oficial) | Abre quando a plataforma recebe mensagem do cliente (ligação recebida também abre), renova a cada mensagem recebida, fecha 24 horas depois da última mensagem do cliente. Responder não renova. Quem chega por anúncio de clique para o WhatsApp abre janela de 72 horas. Fechada, só template. | `references/docs/recursos/janela-de-atendimento.md` |
| Mensagem fora da janela | Não é entregue. A opção **Bloquear mensagem comum fora da janela de 24h**, na aba **Geral** da Conexão oficial, só muda o aviso (em português, na conversa). | `references/docs/recursos/janela-de-atendimento.md` |
| Cobrança (oficial) | Desde 1º de outubro de 2026 a Meta cobra pelas mensagens que a empresa envia, inclusive texto livre dentro da janela. Franquia de 1.000 mensagens de serviço por número, por mês, sem acumular. Template tem cobrança própria, pela categoria. O que o cliente envia não é cobrado; a janela de 72 horas por anúncio segue gratuita. Quem cobra é a Meta. Atendente, chatbot e IA pagam igual: o que reduz é o número de mensagens. | `references/docs/trilhas/a-cobranca-do-whatsapp-oficial-mudou.md`, `references/docs/recursos/whatsapp-oficial-x-nao-oficial.md` |
| Limitador de Mensagens | Contador da conexão oficial (card da conexão › **Limitador de Mensagens**). Só informa: chegar ao teto não impede nenhum envio. Separa conversa livre, template, celular e híbrida. | `references/docs/recursos/limitador-de-mensagens.md` |
| Bloqueio no canal não oficial | Risco existe desde o primeiro uso, pode ser permanente e sem apelação garantida. | `references/docs/recursos/numero-bloqueado-no-whatsapp.md`, `references/docs/recursos/whatsapp-oficial-x-nao-oficial.md` |
| Bloqueio no canal oficial | Raro e gradual: qualidade baixa por denúncias, template com conteúdo proibido ou em categoria errada, envio sem opt-in. | `references/docs/recursos/numero-bloqueado-no-whatsapp.md` |
| Limite de envio (oficial) | A Meta limita para quantos clientes diferentes a empresa pode iniciar conversa em 24 horas (degraus a partir de 250), por portfólio; responder quem escreveu não conta. Campanha grande pode parar no meio do dia. | `references/docs/recursos/qualidade-do-numero-e-limite-de-envio.md` |
| Mensagem não entregue (oficial) | A Meta devolve um código de erro, listado no botão **Erros de template** do card da conexão; o artigo traduz cada código (janela fechada, limite de marketing por cliente, variável faltando, template pausado, pagamento). | `references/docs/recursos/erros-de-entrega-do-whatsapp-oficial.md` |
| Reprovação de template | Utilidade com linguagem vendedora é recusada; mistura de categorias vira Marketing. | `references/docs/recursos/mensagem-template.md` |

Para reduzir a quantidade de mensagens cobradas, os artigos citam o **Concatenador** (junta mensagens de texto do atendente; `references/docs/recursos/concatenador-de-mensagens.md`) e o **Modo Híbrido** (`references/docs/recursos/whatsapp-modo-hibrido-oficial-e-qrcode.md`). Para a redação, a consequência é direta: uma mensagem completa custa menos que três curtas.

### Roteiro de custo da API Oficial (sem valores)

Para responder "isso vai me custar?". Siga a ordem e não cite preço: nenhum valor está na documentação.

| Pergunta | O que os artigos dizem | Artigo |
|---|---|---|
| Quem cobra? | A Meta, direto no meio de pagamento cadastrado na conta dela. A cobrança das mensagens é "paga por você diretamente, e não à plataforma que você usa para atender". | `references/docs/recursos/entenda-a-api-oficial.md` |
| O que é cobrado? | O que a empresa envia pelo canal oficial: o texto livre dentro da janela (acima da franquia) e os templates, que têm cobrança própria pela categoria, inclusive o de Utilidade com a janela aberta. Não muda conforme quem escreveu (atendente, chatbot ou IA). | `references/docs/trilhas/a-cobranca-do-whatsapp-oficial-mudou.md`, `references/docs/recursos/bloco-template.md` |
| O que não é cobrado? | O que o cliente envia; a janela de 72 horas de quem chega por anúncio de clique para o WhatsApp; a mensagem que não sai (recusada fora da janela). Na conexão por QR Code não há custo por mensagem. | `references/docs/recursos/janela-de-atendimento.md`, `references/docs/recursos/whatsapp-oficial-x-nao-oficial.md` |
| O que conta para a franquia? | A franquia é de 1.000 mensagens de serviço por número, por mês, e não acumula. Vale para as respostas que a equipe escreve dentro da conversa. Template não entra: tem cobrança própria. | `references/docs/trilhas/a-cobranca-do-whatsapp-oficial-mudou.md` |
| Qual categoria custa mais? | Marketing é a mais cara; Utilidade custa menos que Marketing. Sobre qual é a mais barata, o artigo se contradiz (seção 10). | `references/docs/recursos/mensagem-template.md` |
| O que precisa estar em dia? | Um meio de pagamento cadastrado na conta da Meta em que o número está (Meta Business Suite › **Cobrança e pagamentos** › aba **Contas de mensagens** › **Adicionar forma de pagamento**). Sem ele, nenhum template é enviado e as respostas só são entregues até acabar a franquia gratuita do mês. | `references/docs/trilhas/a-cobranca-do-whatsapp-oficial-mudou.md`, `references/docs/recursos/forma-de-pagamento-do-whatsapp-oficial.md` |
| Onde acompanho quanto já enviei? | **Conexões** › card da conexão oficial › **Limitador de Mensagens**: **Mensagens por ciclo** (1.000, se a ideia é acompanhar a franquia), **Dia de corte** e **Mostrar o contador no card**. **Neste ciclo** separa conversa livre, template, celular e híbrida; **Ver meses anteriores** guarda os seis últimos ciclos. O contador soma template junto: para comparar com a franquia, olhe a linha de conversas livres. Ele conta mensagens, não dinheiro, e não bloqueia nenhum envio. | `references/docs/recursos/limitador-de-mensagens.md`, `references/docs/trilhas/medir-quanto-voce-ja-enviou-no-mes.md` |
| Como gasto menos? | Menos mensagens: uma completa em vez de várias curtas, **Concatenador**, fluxo com menos idas e voltas. Em envio de template em volume, "o número de envios é decisão de custo". | `references/docs/recursos/whatsapp-oficial-x-nao-oficial.md`, `references/docs/recursos/bloco-template.md` |

**Não documentado:** o valor de cada categoria e onde consultá-lo; onde ver o gasto em dinheiro (o Limitador conta mensagens); se a plataforma cobra algo além do que a Meta cobra pelas mensagens. Sobre o último ponto, os artigos só afirmam que a cobrança por mensagem é da Meta; preços e planos da plataforma não fazem parte desta skill.

---

## 10. Divergências entre artigos

Quando dois artigos discordam, ou um artigo se contradiz, diga isso ao usuário e mostre os dois trechos.

| Assunto | Artigo A | Artigo B | Como tratar |
|---|---|---|---|
| Template de Utilidade com a janela aberta é cobrado? | Adicionar Agendamento (Dúvidas Comuns): "a Meta não cobrará por esse disparo de Utilidade". | Template (bloco), Oficial x Não Oficial e a trilha da cobrança: é cobrado, inclusive o de utilidade com a janela aberta, desde 1º de outubro de 2026. | Os artigos da cobrança são os específicos do assunto e trazem a data da mudança. Trate como cobrado e avise que o artigo de Agendamento ainda traz a regra anterior. |
| Qual categoria de template é a mais barata? | Mensagem Template, seção "As quatro categorias": Utilidade é "a categoria mais barata das que a empresa inicia"; Autenticação é "barata e extremamente restrita". | O mesmo artigo, adiante: "Utilidade é a faixa intermediária" (seção "O que separa uma da outra") e Autenticação é "a mais barata e a mais restrita" (Dúvidas Comuns). | O que é consistente: Marketing é a mais cara e Utilidade custa menos que Marketing. Não afirme qual das duas, Utilidade ou Autenticação, é a mais barata: diga que o artigo se contradiz e que os valores não estão na documentação. |
| Campos extras 7 a 10 na lista de campanha | Nova Campanha API Oficial: extra7, extra8 e extra9 são o texto do 1º, 2º e 3º botão. | Fontes de Contatos para Campanhas: 7 e 8 são os valores dos botões; 9 e 10 são livres. | Para até dois botões os artigos concordam. Com três botões, avise da divergência e peça um teste com uma lista só com o número do próprio usuário. |
| Fonte de contatos da campanha | Nova Campanha: escolha entre Lista de Contato, Tags, Grupos ou Aniversário. | Fontes de Contatos: a campanha sempre usa uma Lista de Contatos; para alcançar uma tag, cria-se a lista **Por Tag**. | Oriente pelo caminho da lista (**Campanhas › Criar Listas**), que atende aos dois. |
| Prazo de aprovação de template | Mensagem Template (Dúvidas Comuns): "em geral algumas horas, mas pode ser dias". | Criar Template pela Plataforma e Template Recusado, Pausado ou Desabilitado: a análise "pode levar até 24 horas". | Diga que costuma levar horas, que os artigos falam em até 24 horas e em dias, e que o prazo é da Meta. |

---

## 11. E-mail do Mail Marketing

Campanha de e-mail em massa, enviada pelo menu **Mail Marketing** do CMV a partir de uma conta de e-mail da empresa. Não tem relação com conexão de WhatsApp, janela de atendimento, template da Meta nem cobrança da Meta: nada das seções 2, 4 e 9 vale aqui. E-mail enviado fora do Mail Marketing (Gmail, Outlook, outra ferramenta) não é desta skill.

**Quem pode:** o menu **Mail Marketing** é do Administrador e do Supervisor; o atendente não vê o menu. A aba **Configurações** (rodapé e texto do link de descadastro) só o Administrador altera; o Supervisor vê os campos desativados.

**Onde se cadastra:** o texto do e-mail é o **modelo**: **Mail Marketing › Modelos › Novo modelo** › **Salvar**. O envio é a **campanha**: **Mail Marketing › Campanhas › Nova campanha**, que junta a conta que envia, o modelo e uma ou mais listas. As listas ficam em **Mail Marketing › Listas** (não são as listas de **Campanhas › Criar Listas**, que são das campanhas de WhatsApp).

**O que se redige, campo por campo**

| Onde | Campo | O que o artigo diz |
|---|---|---|
| Modelo | **Nome do modelo** | Interno: aparece na escolha do modelo da campanha. Obrigatório para salvar. |
| Modelo | **Assunto** | O assunto do e-mail. Aceita variável. A campanha usa este quando o **Assunto** dela fica em branco. |
| Modelo | **Pré-cabeçalho** | "O texto curto que aparece ao lado do assunto na caixa de entrada." |
| Modelo | **Blocos** ou **HTML** | Alternador do topo: monta o e-mail com blocos, sem código, ou com o HTML de um e-mail pronto colado num campo só. |
| Modelo, blocos | **Título** | Texto, **Tamanho** (Grande, Médio ou Pequeno) e **Alinhamento**. |
| Modelo, blocos | **Texto** | Várias linhas e **Alinhamento**; aceita `**negrito**`, `_itálico_` e `[texto do link](https://...)`. |
| Modelo, blocos | **Botão** | Texto, **Link**, **Alinhamento** e **Cor do botão**. |
| Modelo, blocos | **Imagem** | **Endereço da imagem** (público, começando com `https://`; não recebe arquivo do computador), **Link**, **Descrição da imagem** e **Largura (%)**, de 10 a 100. |
| Modelo, blocos | **Colunas**, **Divisor**, **Espaço**, **HTML livre** | Duas ou três colunas com imagem, título, texto e link; uma linha divisória; um respiro de 4 a 120 px; um trecho de HTML no meio dos blocos. |
| Modelo | Estilo | Cores (**Fundo**, **Conteúdo**, **Texto**, **Destaque**), **Fonte** (Arial, Georgia, Trebuchet MS, Verdana ou Courier New) e **Endereço da logo (opcional)**. Não existe no modo HTML. |
| Campanha | **Assunto** | "Em branco, vale o assunto do modelo." Preenchido, vale o da campanha. |
| Campanha | **Nome do remetente** | O nome que o cliente vê junto do endereço da conta de e-mail. O endereço é o da conta escolhida em **Conta de e-mail que envia** (contas do menu **Contas de E-mail**). |
| Campanha | **Responder para (opcional)** | O endereço que recebe as respostas, quando não deve ser o da própria conta. |
| Configurações | **Rodapé dos e-mails** | "Nome da empresa, endereço e por que a pessoa recebe. Aparece em todo e-mail, acima do link de descadastro." Vale para todos os e-mails da empresa e aparece na prévia. Só o Administrador salva. |
| Configurações | **Texto do link de descadastro** | O texto do link no fim de todo e-mail. Em branco, volta para um texto pronto ao salvar. Só o Administrador salva. |

O modelo novo já abre com blocos de exemplo (**Título**, **Texto**, **Botão**): oriente a trocar o conteúdo, não a somar.

**Variáveis (lista do artigo Modelos de E-mail: Blocos e HTML)**

| Variável | No e-mail enviado |
|---|---|
| `{{nome}}` | O nome da pessoa, como está na lista |
| `{{primeiro_nome}}` | A primeira palavra do nome |
| `{{email}}` | O endereço de e-mail da pessoa |
| `{{descadastro}}` | O link para a pessoa não receber mais (opcional: sem ele, o link entra sozinho no rodapé) |
| `{{cidade}}`, `{{plano}}`… | Cada coluna a mais da planilha da lista, com o nome da coluna entre chaves duplas |

- A variável funciona "no assunto e nos textos do e-mail". O editor mostra as variáveis em botões; clicar copia o código. Copie de lá, não de memória.
- Coluna sem valor para aquela pessoa: o e-mail vai com o espaço em branco. Escreva a frase de modo que continue boa sem o dado.
- Os mustaches da plataforma (`{{firstName}}`, `{{name}}`, seção 0) não aparecem nos artigos do Mail Marketing: não use no e-mail. O primeiro nome aqui é `{{primeiro_nome}}`.
- A coluna precisa existir na planilha com o mesmo nome da variável. Cabeçalho da planilha: `email`, `nome` e as outras colunas, separadas por ponto e vírgula, vírgula ou tabulação (exemplo do artigo: `email;nome;cidade;plano`). Se o nome da coluna diferencia maiúsculas ou aceita acento e espaço: **não documentado**. Recomendação desta skill: nome curto, minúsculo, sem acento e sem espaço.
- As colunas a mais só existem quando os contatos vêm de planilha; quem entrou por **Adicionar um** (e-mail e nome) ou **Do atendimento** recebe o espaço em branco no lugar delas.

**Descadastro**

- Todo e-mail de campanha leva no rodapé o link de descadastro, com o texto das **Configurações**. Se o modelo não tem `{{descadastro}}`, o link entra sozinho no fim; no modo HTML, o rodapé é somado ao fim do HTML colado. Não precisa escrever o link no texto.
- Abrir o link não descadastra: a página pergunta "Não receber mais estes e-mails?" e só o botão **Confirmar o descadastro** conclui.
- O descadastro vale para todas as campanhas da empresa, em qualquer lista, até a equipe usar **Voltar a enviar** (só a pedido da pessoa). **Tirar da lista** não descadastra.
- Não escreva "responda PARAR" no e-mail: o caminho documentado é o link. Que uma resposta ao e-mail descadastre alguém não está documentado; quem pedir por outro canal é descadastrado pela equipe, na aba **Descadastros**.

**Teste (documentado, diferente do WhatsApp)**

- **Prévia** do modelo: mostra o desenho com o rodapé e o link de descadastro, em largura de computador e de celular, mas não troca as variáveis (`{{primeiro_nome}}` aparece escrito).
- **Enviar um teste** (aparece depois de salvar o modelo) e **Enviar teste** (na campanha): o e-mail chega com **[Teste]** na frente do assunto, **Maria** no `{{primeiro_nome}}`, **Maria Silva** no `{{nome}}`, o endereço do teste no `{{email}}` e as colunas da planilha em branco. O link de descadastro não funciona no teste, e o teste não entra no relatório. O teste da campanha usa o **Nome do remetente** e o **Responder para** dela.

**Limites e avisos**

- **E-mails por minuto:** de 1 a 600. A tela orienta: "Comece devagar com uma conta nova e aumente aos poucos" e "O ritmo protege a reputação da sua conta de e-mail."
- Para agendar, a campanha precisa de conta de e-mail, modelo, assunto (do modelo ou da campanha) e listas com contatos (linha "Falta para agendar:").
- Quem está em mais de uma lista recebe uma vez só; quem está nos **Descadastros** fica de fora.
- Os links do modelo em HTML "são rastreados"; o relatório mostra aberturas, cliques, **Links mais clicados** e descadastros por campanha.
- O e-mail da campanha não fica na pasta de enviados da conta; o registro fica no relatório.
- Remover um modelo não muda campanhas já agendadas, que "guardam a cópia delas". **Duplicar** cria uma cópia do modelo ou da campanha (com "(cópia)" no nome): é o caminho documentado para reaproveitar um e-mail já enviado.
- Custo: o artigo Mail Marketing diz que não é preciso contratar serviço de envio à parte, porque o envio sai pelas contas de e-mail da empresa. Preço e plano não fazem parte desta skill.
- **Não documentado:** tamanho máximo do assunto, do pré-cabeçalho e do texto; anexos (não há campo de anexo descrito); se as variáveis funcionam no **Pré-cabeçalho**, no **Nome do remetente**, no **Assunto** da campanha e dentro do HTML colado (o artigo fala em "assunto e textos"); o que vai no lugar de `{{nome}}` quando a lista não tem nome; o texto pronto do link de descadastro; se editar um modelo muda uma campanha já agendada; repetição automática de campanha; o fuso da hora do envio. Nesses casos, diga que a Central não informa e mande conferir com **Enviar teste**.

**Artigos:** [Mail Marketing](https://clihelper.chatmasterveloz.com/docs/mail-marketing) (`references/docs/recursos/mail-marketing.md`), [Visão Geral Mail Marketing](https://clihelper.chatmasterveloz.com/docs/visao-geral-mail-marketing) (`references/docs/recursos/visao-geral-mail-marketing.md`), [Modelos de E-mail: Blocos e HTML](https://clihelper.chatmasterveloz.com/docs/modelos-de-e-mail-blocos-e-html) (`references/docs/recursos/modelos-de-e-mail-blocos-e-html.md`), [Campanhas de E-mail](https://clihelper.chatmasterveloz.com/docs/campanhas-de-e-mail) (`references/docs/recursos/campanhas-de-e-mail.md`), [Listas de Envio do Mail Marketing](https://clihelper.chatmasterveloz.com/docs/listas-de-envio-do-mail-marketing) (`references/docs/recursos/listas-de-envio-do-mail-marketing.md`), [Descadastros do Mail Marketing](https://clihelper.chatmasterveloz.com/docs/descadastros-do-mail-marketing) (`references/docs/recursos/descadastros-do-mail-marketing.md`), [Configurações do Mail Marketing](https://clihelper.chatmasterveloz.com/docs/configuracoes-do-mail-marketing) (`references/docs/recursos/configuracoes-do-mail-marketing.md`), [Permissões Mail Marketing](https://clihelper.chatmasterveloz.com/docs/permissoes-mail-marketing) (`references/docs/recursos/permissoes-mail-marketing.md`), [Relatório da Campanha de E-mail](https://clihelper.chatmasterveloz.com/docs/relatorio-da-campanha-de-e-mail) (`references/docs/recursos/relatorio-da-campanha-de-e-mail.md`).
