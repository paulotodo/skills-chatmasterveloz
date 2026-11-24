# APIs e Webhook Administrativos: o que é do revendedor (Super Admin)

Use este arquivo quando quem pede administra a instância. Como o mapa, ele só aponta: o payload, os campos e os avisos estão no artigo, que precisa ser aberto antes de escrever qualquer código.

- Todos os caminhos são relativos a `references/docs/`. Os artigos administrativos ficam em `revendedor/api/` e os de tela do revendedor em `revendedor/recursos/`; os da Central continuam em `api/` e `recursos/`.
- Índices: `revendedor/INDICE-api.md` (os 52 artigos, por assunto) e `revendedor/INDICE-api-endpoints.md` (os 35 endpoints). Busca: `python3 scripts/buscar_endpoint.py --conexao admin`, com palavras antes se quiser (`python3 scripts/buscar_endpoint.py empresa --conexao admin`).
- **não documentado** = os artigos não dizem. Diga isso à pessoa; não complete com o que a API do cliente faz.

## Sumário

1. Quando usar
2. Token: leia o aviso de cada artigo
3. O que cada grupo de chamadas faz
4. Avise antes de montar a chamada
5. Chamadas que existem nos dois sites e o `companyId`
6. Webhook Administrativo
7. Planos pela API
8. O que o revendedor libera para o cliente usar a API
9. Incoerências da documentação do revendedor
10. Como entregar

## 1. Quando usar

- **O padrão é cliente.** Quem pede integração é, até prova em contrário, cliente de uma empresa, com token de Conexão ou Token da Empresa dele. Para ele vale o resto da skill, e nada daqui.
- **Revendedor (Super Admin, dono da instância):** a pessoa diz que é, fala em "meus clientes", criar empresa, plano, instância, white label, ou pede algo que só existe aqui: empresas, planos, faturas, avisos do sino, imagens da plataforma, criar Setor, usuário, fluxo, resposta rápida, tag ou conexão **dentro da empresa de um cliente**, ou ser avisado de eventos de todas as empresas.
- **Cliente que pede uma chamada administrativa** ("quero criar empresa por API"): diga que a chamada existe e é de quem administra a instância, porque exige token da empresa do Super Admin. Não entregue o código como se o token dele servisse.
- **Preços ficam fora.** Os nomes das opções de plano (**API Externa**, **Botões**) podem ser citados como estão na tela.

## 2. Token: leia o aviso de cada artigo

O aviso de token fica no começo de cada artigo administrativo, antes da linha `**API:**`. Há quatro textos, e o que vale é o do artigo da chamada: não generalize de um para o outro.

| O aviso diz | Onde | O que a skill afirma |
|---|---|---|
| "Esta chamada exige um token da **empresa do Super Admin**." | 29 artigos | Só isso. Esses artigos não dizem se serve o token de uma Conexão, o Token da Empresa ou os dois. |
| O mesmo, mais: "Serve tanto o token de uma Conexão dela quanto o **Token da Empresa**, gerado em **Configurações → Token da Empresa**. Token de outra empresa não é aceito." | Criar Empresa, Obter Faturas, Pagar Fatura, Reiniciar Conexões como Super Admin | Os dois tipos servem, desde que sejam da empresa do Super Admin. |
| "Esta chamada exige o **Token da Empresa** da **empresa do Super Admin**." | Contar Empresas (`revendedor/api/api-admin-contar-empresas.md`), a única com selo `Empresa` | Só o Token da Empresa. Com token de conexão, mesmo de uma conexão da empresa do Super Admin, a resposta é `403`; o mesmo com o Token da Empresa de outra empresa. Não é o 401 das chamadas de selo `Empresa` do cliente. |
| "Esta chamada **não** depende do token do Super Admin. Funciona com o token da Conexão do Ticket, ou com o Token da Empresa informando a Conexão." | Recuperar Mensagens (`revendedor/api/api-admin-recuperar-mensagens.md`) | O cliente consegue usá-la com o token dele. |

- **O selo `**API:** Todas` desses artigos não quer dizer "qualquer token".** O script mostra as administrativas com o selo `Super Admin (...)` por isso.
- **Não documentado:** se a **API Externa** precisa estar ligada no plano da empresa do Super Admin; se, com o Token da Empresa do Super Admin, as chamadas administrativas pedem a conexão (a regra geral desse token, em `recursos/token-da-empresa-em-configuracoes.md`, é informar a conexão, menos nas de selo `Empresa`); e qual erro volta quando o token de uma empresa cliente chama um endpoint administrativo (só Contar Empresas informa o `403`).

## 3. O que cada grupo de chamadas faz

Endereço base: `https://api2.chatmasterveloz.com`. Todos os artigos desta tabela ficam em `revendedor/api/`.

| Grupo | Chamada | Artigo | Atenção (está no artigo) |
|---|---|---|---|
| Configurações | POST `/api/settings/media-upload?ref=login`: troca logotipo, fundo ou favicon | `api-admin-trocar-imagens-da-plataforma.md` | Formulário com `file` (PNG). O `ref` (destino) vai na **query**: só no formulário, a imagem é gravada com nome inválido e a chamada responde sucesso assim mesmo. Substitui a imagem anterior e vale para a plataforma inteira. |
| Planos | POST `/api/plans`: cria plano | `api-admin-criar-plano.md` | Obrigatórios: `name`, `users`, `connections`, `queues`, `value`. Nome repetido é recusado; campo que não é do plano volta em `camposIgnorados`. Seção 7. |
| Planos | GET `/api/plans` e GET `/api/plans/{planId}`: lista e obtém | `api-admin-listar-planos.md`, `api-admin-obter-um-plano.md` | Só leitura; cada plano vem completo. Plano que não existe responde `404`. |
| Planos | PUT `/api/plans/{planId}`: atualiza só os campos enviados | `api-admin-atualizar-plano.md` | É preciso mandar pelo menos um campo. Vale na hora para todas as empresas do plano. Não existe exclusão de plano pela API. |
| Empresas | POST `/api/companies/add`: cria empresa | `api-admin-criar-empresa.md` | O artigo não marca campo obrigatório nem descreve a resposta. |
| Empresas | GET `/api/companies/all`: lista as empresas da instância | `api-admin-listar-empresas.md` | Sem payload; a resposta não é descrita. |
| Empresas | GET `/api/companies/count`: conta as empresas | `api-admin-contar-empresas.md` | Só números: `total`, `ativas`, `inativas`, `geradoEm`. Só o Token da Empresa (seção 2). |
| Empresas | GET `/api/companies/{companyId}`: cadastro básico | `api-admin-obter-uma-empresa.md` | Não traz CSS, JS, chave de armazenamento, proxy, iframes nem token. |
| Empresas | GET `/api/companies`, com `id` no **corpo**: cadastro completo | `api-admin-obter-uma-empresa-completa.md` | A resposta traz o Token da Empresa (`apiToken`), CSS e JavaScript personalizados e dados do proxy. |
| Empresas | PUT `/api/companies/{companyId}`: atualiza o cadastro | `api-admin-atualizar-o-cadastro-de-uma-empresa.md` | Só o que vier muda; campo desconhecido volta listado; sem campo editável, é recusada. Mexer em plano ou vencimento tem efeito além do cadastro (seção 4). |
| Empresas | POST `/api/companies/{companyId}/block` e `/unblock` | `api-admin-bloquear-empresa.md`, `api-admin-desbloquear-empresa.md` | Não mexem em fatura nem em plano. A empresa do Super Admin não pode ser bloqueada. |
| Empresas | POST e GET `/api/companies/{companyId}/api-token`: gera e confere o Token da Empresa de uma empresa | `api-admin-criar-token-da-empresa.md`, `api-admin-conferir-o-token-da-empresa.md` | O POST devolve o token inteiro, só dessa vez; o GET diz se há token e mostra só o final. Empresa que não existe responde `404`. |
| Faturas | GET `/api/invoices/listar`, com `status` no **corpo** (`all`, `open`, `paid`) | `api-admin-obter-faturas.md` | Lista as faturas "da sua conta Super Admin"; a resposta não é descrita. |
| Faturas | POST `/api/subscription/manualpaid`: registra o pagamento de uma fatura | `api-admin-pagar-fatura.md` | Payload: `invoiceId`, `payment_status` (no exemplo, `Completed`), `paymentId`. A resposta não é descrita. |
| Conexões | POST `/api/companies/{companyId}/whatsapps`: cria conexão de WhatsApp numa empresa | `api-admin-criar-conexao-em-uma-empresa.md` | `name` obrigatório e único em toda a instalação; `greetingMessage` obrigatória com mais de um Setor. Só WhatsApp. Nasce desconectada; o limite de conexões do plano vale. |
| Conexões | POST `/api/application/restart`: reinicia as conexões de toda a instância | `api-admin-reiniciar-conexoes-como-super-admin.md` | Sem payload; a resposta não é descrita. |
| Conexões | POST `/api/messages/recuperar`: repõe no Ticket mensagens que chegaram ao webhook e não foram gravadas | `api-admin-recuperar-mensagens.md` | Até 500 eventos por chamada. Responde `200` mesmo com evento recusado: confira `recusados`. Ticket de outra Conexão: `400` `ERR_TICKET_DE_OUTRA_CONVERSA`. Nada é enviado ao contato. |
| Dentro da empresa de um cliente | POST `/api/queues`, `/api/users`, `/api/flowbuilder`, `/api/quick-messages`, `/api/tags`; GET `/api/quick-messages`; PUT `/api/users/{userId}` | seção 5 | Mesmo endereço das chamadas do cliente; muda o alcance. |
| Avisos (sino do painel) | POST, GET, PUT e DELETE em `/api/announcements`; GET `/api/announcements/show?id=`; PUT `/api/announcements/toggle-status`; POST e DELETE `/api/announcements/media-upload` | `api-admin-avisos.md` lista os oito artigos | `title` é obrigatório ao criar e em toda edição. `scope` `global` mostra em todas as empresas; `company`, só na de `companyId`. O `toggle-status` inverte o estado, não recebe valor. Anexar mídia nova não apaga o arquivo antigo do armazenamento. |

Pares parecidos com endereço diferente: criar conexão é `POST /api/nova-conexao` para o cliente (`api/api-criar-conexao.md`) e `POST /api/companies/{companyId}/whatsapps` para o revendedor; reiniciar conexões é `POST /api/whatsapp-restart` para o cliente (`api/api-reiniciar-conexoes.md`) e `POST /api/application/restart`, da instância inteira, para o revendedor.

## 4. Avise antes de montar a chamada

Estas entram nas duas listas da seção Segurança do `SKILL.md`: confirmação antes de entregar, e resposta que não vai para log nem para a tela.

- **Atualizar o cadastro de uma empresa** (`revendedor/api/api-admin-atualizar-o-cadastro-de-uma-empresa.md`): mexer no plano ou no vencimento sincroniza a fatura em aberto e religa as conexões da empresa que estiverem fora do ar. Não é uma alteração só de cadastro.
- **Atualizar plano** (`revendedor/api/api-admin-atualizar-plano.md`): vale na hora para todas as empresas daquele plano. Diminuir um limite atinge quem já passou dele; desligar um módulo tira o recurso de todas.
- **Criar Token da Empresa** (`revendedor/api/api-admin-criar-token-da-empresa.md`): o único payload de exemplo do artigo é `{"trocar": true}`. Copiado como está numa empresa que já tem token, ele derruba o token antigo na hora, em toda integração que o usa. Não entregue `trocar` por padrão: mande conferir antes com a chamada de Conferir o Token da Empresa e só inclua `"trocar": true` quando a pessoa confirmar que quer substituir. Sem `trocar`, a empresa que já tem token é recusada, de propósito. O artigo não mostra o payload da primeira geração: diga isso.
- **Obter uma Empresa (completa)** (`revendedor/api/api-admin-obter-uma-empresa-completa.md`): a resposta é credencial em trânsito (`apiToken`). Para consultar o cadastro sem credencial, use `GET /api/companies/{companyId}` (`revendedor/api/api-admin-obter-uma-empresa.md`).
- **Bloquear empresa** (`revendedor/api/api-admin-bloquear-empresa.md`): a empresa para de ser processada, a fila de atendimentos deixa de atendê-la e as sessões de WhatsApp não sobem mais. Volta com a chamada de desbloquear.
- **Reiniciar Conexões como Super Admin** (`revendedor/api/api-admin-reiniciar-conexoes-como-super-admin.md`): são as conexões de toda a instância, não de uma empresa.
- **Trocar Imagens da Plataforma** (`revendedor/api/api-admin-trocar-imagens-da-plataforma.md`): substitui a imagem que estava lá, para todas as empresas.
- **Pagar Fatura** (`revendedor/api/api-admin-pagar-fatura.md`): registra o pagamento; o artigo não diz como desfazer.
- **Deletar Aviso** (`revendedor/api/api-admin-deletar-aviso.md`): não há como desfazer, e a mídia anexada não é apagada do armazenamento. O artigo manda tirar a mídia antes (`revendedor/api/api-admin-remover-midia-do-aviso.md`).
- **Atualizar Usuário de uma Empresa** (`revendedor/api/api-admin-atualizar-usuario-de-uma-empresa.md`): o exemplo traz todos os campos; copiado como está, altera todos de uma vez, inclusive a senha. Entregue só os campos que a pessoa quer mudar.
- **Recuperar Mensagens** (`revendedor/api/api-admin-recuperar-mensagens.md`): a plataforma não confere se o evento veio mesmo do webhook. Quem tem o token grava qualquer texto num Ticket da Conexão, em nome do contato ou da equipe, com qualquer data. O artigo pede ao revendedor que a repasse ao cliente só se ele precisar.

## 5. Chamadas que existem nos dois sites e o `companyId`

Sete chamadas têm o mesmo método e o mesmo endereço na Central e no site do revendedor. Na busca por palavra elas voltam duas vezes: a linha com o selo `Super Admin (...)` é a do revendedor.

| Chamada | Revendedor (`revendedor/api/`) | Cliente (`api/`) | O que muda |
|---|---|---|---|
| POST `/api/queues` | `api-admin-criar-setor-em-uma-empresa.md` | `api-criar-setor.md` | `companyId` no corpo |
| POST `/api/tags` | `api-admin-criar-tag-em-uma-empresa.md` | `api-criar-tag.md` | `companyId` no corpo |
| POST `/api/flowbuilder` | `api-admin-criar-fluxo-em-uma-empresa.md` | `api-criar-fluxo.md` | `companyId` no corpo |
| POST `/api/quick-messages` | `api-admin-criar-resposta-rapida-em-uma-empresa.md` | `api-criar-resposta-rapida.md` | `companyId` no corpo |
| GET `/api/quick-messages` | `api-admin-listar-respostas-rapidas-de-uma-empresa.md` | `api-listar-respostas-rapidas.md` | `companyId` na query |
| POST `/api/users` | `api-admin-criar-usuario-em-uma-empresa.md` | `api-criar-usuario.md` | `companyId` no corpo |
| PUT `/api/users/{userId}` | `api-admin-atualizar-usuario-de-uma-empresa.md` | `api-atualizar-usuario.md` | não há campo de empresa: muda o alcance |

- **É o `companyId` que faz a chamada valer para outra empresa.** Sem ele, vale a empresa do próprio token (o texto é igual nos cinco artigos de criar). Por isso, para o cliente, nada muda: ele não manda `companyId`.
- **No PUT de usuário não existe campo de empresa:** com o token da empresa do Super Admin, o `userId` pode ser de qualquer empresa da instalação; com qualquer outro token, só os usuários da própria empresa.
- **Os limites continuam os do plano da empresa de destino** (Setores, usuários), e Setor, conexão, operador e categoria informados precisam ser daquela mesma empresa.
- **Copiar um fluxo de uma empresa para outra:** exportar na empresa de origem (**Mais opções › Exportar Fluxo**), mandar o conteúdo do arquivo como `flow` e apontar o `companyId` da empresa de destino. `flow` junto de `nodes` e `connections` é recusado. O desenho do fluxo em si é da skill `cmv-flowbuilder`.
- **Para montar o payload, leia os dois artigos.** O do revendedor traz o `companyId` e o alcance; o da Central costuma detalhar mais cada campo, como o aviso de `api/api-criar-usuario.md` sobre o `whatsappId`, que é a conexão padrão do usuário e não a conexão da chamada.
- **De onde vem o `companyId` de uma empresa cliente:** do `company.id` do aviso `new_company` do Webhook Administrativo (seção 6), que está documentado; e, por dedução, da chamada que lista as empresas da instância (`revendedor/api/api-admin-listar-empresas.md`), cujo artigo não mostra o formato da resposta: peça para a pessoa conferir o campo no retorno.

## 6. Webhook Administrativo

Artigos: `revendedor/api/webhooks-administrativos.md`, `revendedor/api/habilitar-webhook-administrativo.md`, `revendedor/api/webhook-admin-alteracao-na-conexao.md`, `revendedor/api/webhook-admin-criacao-de-empresa.md`. O campo também está descrito em `revendedor/recursos/marca-e-acesso-em-plataforma.md`.

- **Onde se liga:** menu **Configurações › Plataforma**, seção **Configurações Globais**, campo **Webhook de Eventos [Conexões]**. É um campo só, com uma URL, que recebe os dois eventos. O endereço precisa aceitar POST com corpo em JSON.
- **Alteração na conexão:** chega toda vez que uma conexão de qualquer empresa muda de status, um aviso por conexão. `status`: `connected`, `disconnected`, `pending` ou `qrcode`. No `disconnected`, o campo `event` traz o motivo: `401`, `402`, `403`, `408`, `411`, `428`, `440`, `500` ou `515`; `402` e `403` são banimento, e reconectar não resolve. Campos: `whatsappId`, `companyId`, `event`, `status`, `channel`, `company` (`id`, `name`) e `backendURL`. O exemplo do artigo mostra o aviso dentro do envelope de uma ferramenta de automação: o que interessa está em `body`.
- **Criação de empresa:** `event` igual a `new_company` e o objeto `company` com o cadastro inteiro. Dispara em todo cadastro, feito pelo revendedor ou pela própria pessoa na tela de registro.
- **Separar os dois no mesmo endereço:** pelo campo `event` (`new_company` num, código numérico junto de um `status` no outro).
- **Entrega única.** A plataforma não guarda os avisos que não conseguiu entregar; o artigo manda tratar cada aviso como entrega única e registrar o que receber.
- **Risco a avisar sempre:** endereço preenchido e fora do ar pode interromper a plataforma inteira. Enquanto houver URL no campo, todo evento tenta a entrega, e um destino que não responde afeta todas as empresas. Se o receptor for sair do ar, o campo tem de ser esvaziado antes.
- **Como testar:** menu **Conexões**, **Reiniciar Conexões**; deve chegar um aviso por conexão reiniciada.

O que muda em relação aos webhooks do cliente (seção 7 de `references/mapa-da-api.md`):

| Ponto | Administrativo | Do cliente |
|---|---|---|
| Alcance | Qualquer empresa da instância | Uma empresa: a Conexão, o Setor ou o tipo de evento escolhido |
| Campo que diz o que aconteceu | `event` | Nos da Conexão e do Setor, `acao` (nos avisos de tag, `action`) |
| Aviso perdido | Não é guardado nem reenviado | Nos da Conexão e do Setor: `eventoId`, `sequencia` e busca por até 7 dias |
| Assinatura do aviso | Não documentado | Alguns são assinados (tabela da seção 7 do mapa) |

O aviso de criação de empresa leva dados de cadastro (e-mail, telefone, documento): o destino tem de ser um endereço do próprio revendedor, sem o corpo inteiro em log.

## 7. Planos pela API

Artigos: `revendedor/api/api-admin-criar-plano.md`, `revendedor/api/api-admin-atualizar-plano.md`; a tela está em `revendedor/recursos/configuracoes-planos.md`.

- **O que a documentação sustenta:** `name` é o nome do plano, `users` os usuários, `queues` os Setores, `connections` as conexões, `value` o valor e `connectionLimits` o teto por grupo de canal (`whatsapp`, `whatsappMeta`, `hub`, `telegramInc` "e os demais"; o grupo não informado herda o limite geral de `connections`).
- **Os campos `use…` são os módulos do plano**, cada um `true` ou `false`. O artigo diz que cada um corresponde a uma opção da tela de Planos e **não diz qual é qual**. Não monte tabela de correspondência nem deduza pelo nome (nem para **API Externa** ou **Botões**): se a pessoa quer ligar uma opção pela API, mande consultar um plano que já existe (`GET /api/plans`) e olhar os campos `use` da resposta, como o próprio artigo manda. Qual campo é qual opção da tela se confirma na instância dela, não nesta skill.
- **A lista de módulos cresce sem aviso.** O próprio artigo manda ver a lista de hoje num plano que já existe, pelos campos `use` da resposta. Nem todo módulo do plano tem campo na tela (o artigo cita o `useProducts`).
- **Criar pela API não é igual a criar pela tela.** Na tela, o formulário de um plano novo já vem com sete opções marcadas, entre elas **API Externa**; pela API, o módulo que não for enviado nasce desligado. No PUT, o que não for enviado fica como está.
- **A chamada passa pela mesma conferência da tela:** módulo que a tela de Planos recusa também é recusado.
- **Não existe limite por empresa por cima do plano:** para dar mais a um cliente, o caminho é trocar o plano dele.
- **A tela exclui plano; a API não.**

## 8. O que o revendedor libera para o cliente usar a API

`pre-requisitos-apis.md` existe nas duas documentações, com textos diferentes: `api/pre-requisitos-apis.md` fala com o cliente ("peça ao Suporte"); `revendedor/api/pre-requisitos-apis.md` fala com quem libera.

- **API Externa:** o revendedor habilita no menu **Configurações › Planos**, no plano que a empresa usa (`revendedor/api/pre-requisitos-apis.md`, `revendedor/recursos/como-habilitar-api.md`). Se o cliente diz que a chamada devolve erro de autenticação, o artigo manda conferir também se a opção está marcada no plano daquela empresa, e não em outro.
- **Botões:** além da **API Externa**, a opção **Botões** no plano e a biblioteca escolhida no campo **API Não Oficial** (`revendedor/recursos/como-habilitar-botoes-api.md`). A Central conta três itens para os botões e não cita a biblioteca (`api/pre-requisitos-botoes.md`).
- **Biblioteca de cada empresa:** campo **API Não Oficial**, em **Configurações › Empresas › abrir a empresa › aba Avançado** (`revendedor/recursos/configuracoes-editar-empresa.md`). O campo mostra os nomes técnicos **Baileys** e **APIdoZap Pro**; na documentação do cliente elas são **Básica** e **Pro** (`revendedor/api/pre-requisitos-apis.md`). É aqui que o revendedor confere qual das duas colunas do mapa vale para um cliente.
- **A Baileys (Básica) foi descontinuada:** `revendedor/recursos/canais-e-e-mail-em-plataforma.md` manda migrar para a Pro os clientes que a utilizam. Os artigos de selo Básica continuam na Central, cada biblioteca com os artigos dela: "nem toda chamada existe nas duas bibliotecas" (`revendedor/api/pre-requisitos-apis.md`).
- **O token é passo do cliente:** ele define o da Conexão em **Conexões › editar a Conexão › aba Integrações › Token**. O revendedor pode gerar o Token da Empresa de um cliente pela API (seção 3).
- **Login pela API com e-mail e senha** (`POST /auth/login`): depende de **Permitir Login de Terceiros?**, em **Configurações › Plataforma**, seção **Aplicações Externas por Login**; em **Não**, a chamada responde `Method not allowed`. Campo em branco equivale a **Sim**. Serve para quem chama de servidor (`revendedor/recursos/marca-e-acesso-em-plataforma.md`).

## 9. Incoerências da documentação do revendedor

Os artigos se contradizem ou se calam nestes pontos. Não escolha um lado: diga o que cada artigo afirma e mande conferir na instância.

| Ponto | O que está escrito | O que fazer |
|---|---|---|
| `connections` do plano | `revendedor/api/api-admin-criar-plano.md`: "quantas conexões a empresa pode ter, no total". `revendedor/recursos/configuracoes-planos.md`: o limite geral vale "para cada canal", e não como total | Cite os dois e não afirme qual vale |
| `companyId` e `company.id` no aviso de conexão | O exemplo traz `"companyId": 12` e `"company": {"id": 2}`; o texto diz que `company` repete o identificador da empresa | Não use o exemplo para dizer qual dos dois é a chave; mande conferir num aviso real |
| Payload de criar token | Só `{"trocar": true}` | Seção 4 |
| Formatos em criar × atualizar empresa | `dueDate` como `2025/12/20` (AAAA/MM/DD) ao criar e `2026-12-10` ao atualizar; `planId` como texto num e número no outro; `pais` ao criar, `pais` e `country` ao atualizar | Copie o formato do artigo da chamada, sem levar de um para o outro |
| Campos de criar empresa | Nenhum marcado como obrigatório; `recurrence` só aparece como `MENSAL`, sem a lista de valores | Não invente valores; diga que não está documentado |
| Atualizar aviso | "só o que vier no corpo muda" e, adiante, "O `title` é obrigatório em toda edição" | Mande sempre `id` e `title` |
| Campos explicados e fora do exemplo | `youtubeUrl` e `companyId` em criar aviso; `webhookb` em criar conexão | Use a explicação do campo |
| Recuperar Mensagens | Está só no site do revendedor, embora o cliente possa usá-la | Não há artigo na Central para citar |
| `revendedor/api/pre-requisitos-apis.md` | Anuncia "três itens, e dois deles são seus" e o resumo lista dois; não diz onde fica o campo da biblioteca | O caminho do campo está na seção 8 |
| `revendedor/api/apis-admin.md` | Descreve a API em geral (envio de mensagens, início de fluxos), não a administrativa | Não a use como visão geral das chamadas administrativas |
| Respostas não descritas | Listar empresas, bloquear, desbloquear, criar empresa, criar conexão, reiniciar conexões, obter faturas e pagar fatura | Mostre a resposta crua; não invente campos |
| Obter Faturas | Faturas "da sua conta Super Admin" | O artigo não diz se inclui as das empresas clientes |

## 10. Como entregar

- **A forma é a mesma** do resto da skill: molde de `references/moldes-de-codigo.md`, token em variável de ambiente, status e corpo da resposta à mostra, valores de exemplo marcados para trocar. `GET /api/companies` e `GET /api/invoices/listar` são GET com corpo (variação no fim dos moldes).
- **Diga de quem é o token**, com as palavras do aviso do artigo (seção 2), e que o token de uma empresa cliente não serve.
- **Teste sem risco:** os artigos administrativos não indicam uma chamada de teste. A de listar planos é só de leitura ("nada é alterado") e a de contar empresas devolve só números, mas esta exige o Token da Empresa.

```bash
: "${CMV_TOKEN:?defina a variável CMV_TOKEN com um token da empresa do Super Admin}"

curl -sS --max-time 30 -w '\nHTTP %{http_code}\n' \
  -X GET 'https://api2.chatmasterveloz.com/api/plans' \
  -H "Authorization: Bearer $CMV_TOKEN"
```

- **Nunca rode uma chamada administrativa por conta própria.** A regra da seção Segurança do `SKILL.md` vale em dobro: o alcance é a instância inteira.
- **Fonte:** título do artigo e o link da linha **Fonte** dele, que nos artigos de `revendedor/` é `https://revendedor.chatmasterveloz.com/docs/` seguido do nome do arquivo sem `.md`. Caminho de arquivo não vai na resposta.
