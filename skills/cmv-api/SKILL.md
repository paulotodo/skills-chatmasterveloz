---
name: cmv-api
description: "Integra sistemas externos ao Chat Master Veloz (CMV, chatmasterveloz) pela API REST e por webhooks: acha o endpoint certo para o tipo de conexão (WhatsApp Básica, Pro, Oficial, Hub, Instagram, Facebook, Webchat) e entrega o pedido pronto em cURL, Node, Python, PHP ou nó HTTP Request do n8n. Use quando a pessoa quiser enviar mensagem, mídia, template, lista ou botões por código; criar, transferir ou encerrar ticket; cadastrar contato; aplicar tag; mexer no CRM; agendar mensagem; receber eventos por webhook; ligar o CMV ao n8n, Make ou Zapier; ou quando o código que chama a API esbarra em token, endpoint, payload ou erro 400/401. Quem tem esta skill usa o CMV: sistema, ERP ou script que precisa agir no atendimento, sem citar outra API, é com ela, mesmo sem a palavra API. Não cobre erro que aparece na tela do painel, mesmo técnico, nem configurar recursos (cmv-ajuda), fluxos (cmv-flowbuilder), redigir templates e campanhas (cmv-mensagens) nem CSS/JS (cmv-painel-css-js)."
---

# Integrações por API e webhooks do Chat Master Veloz

Esta skill transforma um pedido de integração ("quero que meu sistema mande uma mensagem", "quero ser avisado quando chegar mensagem") em material pronto para colar: o pedido HTTP completo, onde pegar o token e como testar sem risco.

Todo fato sobre o produto vem da cópia da Central de Ajuda em `references/docs/`. A API do CMV tem particularidades que não dá para adivinhar (o mesmo recurso muda de endereço e de nomes de campo conforme a conexão), então o trabalho é sempre **achar o artigo, ler e montar a partir dele**. O que não estiver nos artigos, diga que não está documentado.

## Mapa do material

| Arquivo | Para quê |
|---|---|
| `references/mapa-da-api.md` | Tabela de decisão: operação × tipo de conexão → artigo; webhooks; de onde vem cada identificador. Comece por aqui. |
| `references/moldes-de-codigo.md` | A mesma chamada em cURL, Node, Python, PHP e n8n, com token em variável de ambiente e tratamento de erro; variações (GET, multipart, Token da Empresa) e a receita de receber um aviso de webhook e responder (n8n ou receptor próprio), com a tabela sintoma → causa → artigo. |
| `scripts/buscar_endpoint.py` | Busca endpoints por palavra, método e tipo de conexão. Existe porque o índice de endpoints não mostra o selo da conexão; o script lê o selo em cada artigo. |
| `references/docs/INDICE-api-endpoints.md` | Os 309 endpoints, uma linha por artigo, com método e endereço. |
| `references/docs/INDICE-api.md` | Os 357 artigos de API por assunto, incluindo webhooks e conceitos. |
| `references/docs/api/` e `references/docs/recursos/` | Os artigos. As páginas de seção (`api/api-mensagem.md`, `api/api-midias.md`, `api/api-botoes.md`…) listam os artigos com o selo de conexão ao lado. |

Daqui em diante, caminhos escritos como `api/...` e `recursos/...` ficam dentro de `references/docs/`.

## Fluxo de trabalho

### 1. Entenda em que sentido a informação anda

| A pessoa quer… | É… | Onde olhar |
|---|---|---|
| que o sistema dela **faça** algo no CMV (enviar, criar, alterar, consultar) | chamada de API | seções 2 a 6 do mapa |
| **ser avisada** quando algo acontece no CMV | webhook que sai do CMV | seção 7 do mapa |
| que um sistema externo **inicie um fluxo** do chatbot | Webhook Trigger (com variáveis) ou API de iniciar fluxo | `api/webhook-triggers.md`, `recursos/gatilho-via-api.md` |
| ficar consultando a API para saber se chegou algo | isso é polling; a documentação recomenda webhook | `api/api-x-webhook.md` |

Uma integração completa costuma usar os dois: o webhook avisa, a API responde.

### 2. Descubra o tipo de conexão antes de procurar o endpoint

O tipo de conexão decide o artigo. Enviar uma imagem, por exemplo, tem um endereço e um payload na Básica, outros na Pro e outros na Oficial; o payload de uma não funciona na outra. Pergunte em linguagem simples, uma vez:

> "A conexão por onde isso vai sair é WhatsApp por QR Code, WhatsApp API Oficial da Meta, Instagram, Messenger ou Web Chat? Se for QR Code, é a conexão Básica ou a Pro? Se for a API Oficial, é direta ou pelo Hub?"

- Pule a pergunta quando a operação tiver selo **Todas** (tickets, contatos, tags, CRM, produtos, agendamento, Quadro de Atendimentos, Reservas: seção 5 do mapa) ou quando o artigo valer para as duas de QR Code (texto e arquivo anexado têm selo "Básica, Pro").
- A documentação não descreve como ver na tela se uma conexão de QR Code é Básica ou Pro. Se a pessoa não souber, diga isso, entregue as duas versões em blocos separados e rotulados, e sugira confirmar com o Suporte. Nunca funda as duas num pedido só.
- Na Oficial, pergunte também se a conversa está dentro da janela de atendimento: texto, mídia, lista e botões exigem a janela aberta; fora dela o caminho é template. Exceção: quando a integração responde a uma mensagem que acabou de chegar (um webhook que dispara a resposta), não pergunte. A regra do artigo é de 24 horas contadas da última mensagem do cliente (`api/api-janela-de-atendimento.md`), então a janela está aberta.
- Na Oficial pelo **Hub**, só existe um artigo: o de template sem variável (seção 4 do mapa). Para texto, mídia, lista, botões e template com variáveis pelo Hub não há artigo: diga que não está documentado se as chamadas da Oficial direta valem. Em template, direta ou Hub muda o pedido inteiro: a direta usa `/api/messages/sendMetaCustom`, com `template` em componentes (`header`, `body`, `button`); pelo Hub, o template sem variável usa `/api/messages/sendOfficial`, só com `number`, `name` e `language` (`api/api-oficial-template-sem-variavel-hub.md`). Se a pessoa não disser qual das duas é, entregue o da Oficial direta e avise, em uma linha, que pelo Hub o endereço e o payload são outros.
- Para CRM, a pergunta é outra: CRM novo (múltiplos funis) ou antigo (funil único). Os artigos são diferentes (seção 5 do mapa).

### 3. Ache o artigo

1. `references/mapa-da-api.md` cobre as operações mais pedidas.
2. Para o resto, a partir da pasta da skill:

```bash
python3 scripts/buscar_endpoint.py audio url --conexao oficial   # palavras + tipo de conexão
python3 scripts/buscar_endpoint.py pedido --metodo POST          # palavras + método
python3 scripts/buscar_endpoint.py --conexao empresa             # as que só aceitam o Token da Empresa
python3 scripts/buscar_endpoint.py --conexoes                    # valores possíveis do selo
grep -n -i 'reserva' references/docs/INDICE-api.md               # busca simples no índice por assunto
grep -rn -i 'ERR_' references/docs/api/                          # frases e códigos de erro citados nos artigos
```

`--conexao pro` traz os artigos com selo Pro e também os de selo Todas; acrescente `--exato` para ver só os específicos. Sem terminal (claude.ai), abra `references/docs/INDICE-api.md`, vá à seção do assunto e escolha o artigo pelo título; os títulos com "Oficial", "(Hub)", "WebChat", "Instagram", "Facebook" e "Chat Externo" já indicam a conexão, e os iguais (dois "API Mensagem de Lista") se separam pelo nome do arquivo (`-pro`) e pelo selo dentro do artigo.

### 4. Leia o artigo inteiro antes de escrever

Os artigos são curtos. Confira, nesta ordem:

- a linha `**API:**` (o selo): tem de bater com a conexão da pessoa. Valores: `Básica`, `Pro`, `Oficial`, `Oficial Hub`, `Todas`, `Empresa`, `WebChat`, `Instagram`, `Facebook`, `Chat Externo`, `Gupshup`, `RCS`. O de Hub traz `Oficial Hub` no selo e "(Hub)" no título;
- avisos no topo, como "Esta chamada usa o Token da Empresa";
- `Endpoint`, `Método` e `Payload`, e a explicação de **cada** campo: o que é obrigatório, o formato e, principalmente, o efeito de `openTicket` e `queueId`, que muda de artigo para artigo;
- as linhas com ⚠️ e ◽ depois do payload: é ali que estão os limites, os erros nomeados e os efeitos colaterais;
- o exemplo em cURL no fim, que serve de conferência do seu pedido.

### 5. Monte a entrega

- **Forma:** cURL por padrão. Node, Python, PHP ou a configuração do nó HTTP Request do n8n quando a pessoa pedir ou o contexto indicar. Parta de `references/moldes-de-codigo.md` e troque endereço, método e payload. O cURL do fim do artigo é para conferir, não para entregar: não tem tempo limite, não mostra o status e leva o token dentro do comando. O que você entrega tem a forma do molde (exemplo no fim deste passo).
- **Payload exatamente como o artigo descreve:** mesmos nomes de campo (maiúsculas contam: a lista da Pro usa `Desc`, `ButtonText`, `List`), mesmo tipo (o artigo de texto usa `"openTicket": "1"` como texto; o de template usa `1` como número; copie o que está lá) e só os campos documentados. A própria documentação diz: na dúvida, mande só o que está no exemplo, porque há chamadas que gravam o que não reconhecem.
- **Valores de exemplo ficam marcados para trocar:** número, `queueId`, `ticketId`, nome do template. Todo ID usado no exemplo vai acompanhado, na própria resposta, de como obtê-lo (seção 8 de `references/mapa-da-api.md`). O `queueId`, por exemplo, é o ID do Setor e sai da chamada que lista os Setores: `GET https://api2.chatmasterveloz.com/api/company/queues`, só com o token (`api/api-listar-setores-da-empresa.md`; o artigo não descreve o formato da resposta).
- **Token fora do código**, em variável de ambiente (ver Segurança).
- **Tratamento de erro:** conferir o status, mostrar o corpo da resposta, tempo limite, e nenhuma repetição automática em envio de mensagem. No cURL, isso são as opções `-sS --max-time 30 -w '\nHTTP %{http_code}\n'` do molde: elas vão em todo cURL entregue. A maioria dos artigos não descreve os códigos de status nem o formato da resposta de sucesso: não invente campos de resposta; mostre a resposta crua e trate só o que o artigo citar.
- **Onde pegar o token**, com o caminho do menu (tabela abaixo).
- **Teste seguro primeiro:** a documentação recomenda a chamada de Status da Conexão (`api/api-status-das-conexoes.md`), que só exige o token. Entregue o comando pronto (primeiro bloco abaixo), não o nome do arquivo. Avise que a resposta dela traz o token de cada conexão e não deve ser colada em lugar nenhum.

O teste seguro, já na forma do molde (`POST`, sem payload):

```bash
curl -sS --max-time 30 -w '\nHTTP %{http_code}\n' \
  -X POST 'https://api2.chatmasterveloz.com/api/whatsapp-status' \
  -H "Authorization: Bearer $CMV_TOKEN"
```

E um envio na mesma forma: o template com variáveis pela Oficial direta, com o payload de exemplo de `api/api-oficial-mensagem-template.md`:

```bash
: "${CMV_TOKEN:?defina a variável CMV_TOKEN antes de rodar}"

curl -sS --max-time 30 -w '\nHTTP %{http_code}\n' \
  -X POST 'https://api2.chatmasterveloz.com/api/messages/sendMetaCustom' \
  -H "Authorization: Bearer $CMV_TOKEN" \
  -H 'Content-Type: application/json' \
  --data '{"number":"5511955892164","name":"vars_001","language":"pt_BR","openTicket":1,"queueId":100,"template":[{"type":"header","parameters":[{"type":"text","text":"Texto cabeçalho"}]},{"type":"body","parameters":[{"type":"text","text":"Maria"},{"type":"text","text":"Festa do Peão"},{"type":"text","text":"15/01/2028"}]},{"type":"button","sub_type":"quick_reply","index":"0","parameters":[{"type":"payload","payload":"Contato"}]}]}'
```

A última linha da saída é o status HTTP; acima dela vem o corpo da resposta. Em `template` ficam só os componentes que existem no template aprovado na Meta, e as variáveis do `body` seguem a ordem do template.

### 6. Feche com a fonte e com os limites

Cite o artigo usado: título e o link da linha **Fonte** do cabeçalho. Se algo que a pessoa pediu não está documentado (uma variante de conexão sem artigo, o formato de uma resposta, um limite de envio), diga com todas as letras e sugira o Suporte do Chat Master Veloz.

## Conceitos transversais confirmados na documentação

| Conceito | O que a documentação diz | Artigo de origem |
|---|---|---|
| Endereço base | Todas as chamadas partem do endereço da instalação, no formato `https://api2.chatmasterveloz.com/api/...`; o artigo de cada chamada traz o endereço completo. Use o do artigo. | `api/apis.md`, `api/pre-requisitos-apis.md` |
| Autenticação | Cabeçalho `Authorization: Bearer <token>`. O token prova a autorização e define por qual conexão a chamada sai. | `api/estrutura-de-api.md` |
| Token da Conexão | Um por conexão, definido pela própria pessoa em **Conexões › editar a Conexão › aba Integrações › Token**. Tem de ser único por conexão. Se a conexão for excluída e recriada, o token antigo é recusado. | `api/pre-requisitos-apis.md`, `recursos/token-da-conexao.md` |
| Token da Empresa | Um só para a empresa, em **Configurações › Token da Empresa** (**GERAR UM NOVO**, **COPIAR**, **REVOGAR**). Gerar ou revogar derruba o anterior na hora. Como não carrega a conexão, a chamada precisa informar `whatsappId`, `connectionId` ou `whatsappName` (query string ou corpo); sem isso, 400. As exceções são as chamadas que só aceitam este token e a que lista as Conexões (`api/api-status-das-conexoes.md`), que vão sem Conexão. | `recursos/token-da-empresa-em-configuracoes.md` |
| Chamadas só do Token da Empresa | Algumas chamadas só aceitam o Token da Empresa, sem informar conexão (selo `Empresa`); com token de conexão respondem 401 "Acesso não permitido". | `recursos/token-da-empresa-em-configuracoes.md`, `api/estrutura-de-api.md` |
| Pré-requisito do plano | A **API Externa** precisa estar habilitada; pede-se ao Suporte. Os **Botões** são habilitados à parte. | `api/pre-requisitos-apis.md`, `api/pre-requisitos-botoes.md` |
| Tipos de conexão | Três bibliotecas de WhatsApp: **Pro** e **Básica** (por QR Code) e **Oficial** (API Oficial da Meta). Nem toda chamada existe nas três. O Webchat não é uma das três e tem artigos próprios. | `api/bibliotecas.md` |
| Formato do número | Telefone com DDI, DDD e número, só dígitos (ex.: `5511955892164`). Grupo, LID, Instagram, Facebook e Web Chat usam outros identificadores. | `api/api-mensagem-de-texto.md`; seção 8 do mapa |
| `ticketId` × protocolo | O `ticketId` é o número entre parênteses no cabeçalho da conversa; o número depois de `#` é o protocolo e não serve nas chamadas que pedem `ticketId`. Para o sistema achar o `ticketId` sem ninguém olhar a tela: o `chamadoId` que vem no webhook da conexão ou, a partir do telefone do contato, a API Listar Tickets do Contato (`GET /api/contacts/alltickets`, com `number`). | `api/api-atualizar-ticket.md`, `api/webhooks-da-conexao.md`, `api/api-listar-tickets-do-contato.md` |
| Formato do corpo | JSON na maior parte das chamadas. Nas que enviam arquivo anexado, o corpo é um formulário e o `Content-Type` não é informado à mão. | `api/estrutura-de-api.md` |
| API × webhook | A API a pessoa chama quando quer algo; o webhook chama o sistema dela quando algo acontece. O Webhook Trigger é o sentido contrário: um endereço do CMV que o sistema externo chama. | `api/api-x-webhook.md`, `api/webhooks.md` |
| Erro de autorização | Conferir token e endereço, nessa ordem; com Token da Empresa, conferir se a conexão foi informada; e se a chamada é das que só aceitam o Token da Empresa. | `api/estrutura-de-api.md` |

Outras credenciais que aparecem na conversa e não são token de API: o **Token de Validação** para incorporar um atendimento por iframe (`recursos/incorporar-atendimento-em-outro-sistema.md`) e as chaves de serviços de terceiros que se colam no CMV, como OpenAI, Meta, Asaas, Mercado Pago, PagSeguro, PagGPix e Google Maps (`recursos/integracoes.md` e os artigos `recursos/token-*.md`, `recursos/access-token-*.md`, `recursos/credenciais-paggpix.md`, `recursos/chave-google-maps.md`).

## Segurança

- **Token sempre em variável de ambiente ou no cofre de credenciais da ferramenta.** Quem tem o token da conexão envia mensagens por ela; quem tem o Token da Empresa fala por qualquer conexão. Por isso ele não entra em código-fonte, repositório, print ou planilha.
- **Nunca em JavaScript que roda no navegador** (site, landing page, JS personalizado do painel). Tudo o que o navegador carrega pode ser lido por qualquer visitante. Se a pessoa quer disparar algo a partir de um formulário do site, o caminho é o site chamar um servidor dela (ou o n8n, ou um Webhook Trigger), e esse servidor guardar o token.
- **Se a pessoa colar o token na conversa,** não o repita na resposta, use `$CMV_TOKEN` no código e recomende trocá-lo: o da conexão no campo Token; o da empresa em **GERAR UM NOVO**, lembrando que o anterior para de funcionar na hora.
- **Não dispare pedidos contra a API real por conta própria.** Um POST de mensagem envia de verdade, para clientes reais, e não tem como desfazer; mesmo uma consulta pode devolver dados sensíveis (a de status devolve tokens). O padrão é entregar o comando para a pessoa rodar. Só execute se ela pedir explicitamente; nesse caso mostre antes o comando exato, confirme o destinatário (de preferência o número de teste dela), rode uma chamada por vez e não exiba o token na saída.
- **Chamadas em bloco ou sem volta pedem confirmação dupla e aviso claro:** apagar todos os contatos, apagar ticket, apagar tag do cadastro, encerrar tickets em massa, transferir todos os tickets de uma conexão, definir tags ou `extraInfo` (substituem o conjunto). Antes de entregar, pergunte se é isso mesmo e ofereça a alternativa que mexe em um item só.
- **Webhooks carregam segredo.** Os avisos da Conexão e do Setor trazem o token da conexão e dados do contato; o de Usuários traz e-mail, telefone e hash de senha. O destino tem de ser um endereço da própria pessoa, em HTTPS, e o corpo inteiro não deve ir para log. A URL de um Webhook Trigger é pública: quem a conhece dispara o fluxo.

## Armadilhas que a documentação revela

- **"Transferir ticket" tem dois artigos com efeitos opostos.** Transferir **um** atendimento é `api/api-atualizar-ticket.md` (muda `queueId` e `userId`). `api/api-transferir-tickets-para-um-setor.md` move **todos** os atendimentos da conexão, inclusive encerrados.
- **Tags: adicionar × definir × apagar.** `api/api-adicionar-tags-ao-ticket.md` soma; `api/api-atualizar-tags-do-ticket.md` substitui todas; `api/api-deletar-tag.md` apaga a tag da empresa inteira.
- **`openTicket` não significa a mesma coisa em todo lugar.** Em vários artigos `0` é "não abre ticket"; no de template com variáveis da Oficial, `0` encerra o ticket; em lista e botões da Oficial, sem `openTicket` o atendimento fica como estava. Explique o efeito segundo o artigo da chamada.
- **Na Oficial, `ticketId` não substitui `number`.** O `number` continua obrigatório.
- **Nos botões da Pro, sucesso na resposta não é entrega.** Os artigos de botões da Pro avisam que a recusa do envio vira nota interna e a resposta ainda volta como sucesso. Os outros artigos não dizem isso: não estenda o aviso a outras chamadas.
- **O efeito de uma chamada é o que o artigo dela diz.** Não a iguale a um botão da tela ("é o mesmo que clicar em Resolver") nem diga o que o cliente recebe, se o artigo não disser.
- **Botões da Básica** não abrem atendimento nem gravam a mensagem no painel, e os parâmetros vão como texto JSON com aspas escapadas.
- **Mensagem chegou sem os botões:** costuma faltar a opção Botões no plano.
- **CRM novo × antigo:** as chamadas `/crm/v2/` exigem o CRM novo ativado, e a de criar oportunidade V1 é recusada quando a empresa já está no CRM novo.
- **Artigos com o mesmo título:** há pares "API Mensagem de Lista", "API Enviar Imagem por URL", "API Botão URL". O arquivo com `-pro` é o da Pro; o outro, da Básica. `api/api-listar-contatos-por-tag.md` tem o título "API Listar Tickets por Tag".

## Webhooks

Escolha o webhook pelo alcance (`api/qual-webhook-usar.md`), diga onde colar o endereço e descreva o payload a partir do artigo. A lista completa de webhooks, de avisos que quebram integrações e do que não está documentado fica na seção 7 de `references/mapa-da-api.md`; a receita de receber e responder, em `references/moldes-de-codigo.md`.

## n8n, Make, Zapier

- **Receber eventos no n8n:** nó Webhook em POST; a URL de produção vai no campo de webhook da Conexão, do Setor ou de Webhook Eventos (`recursos/n8n-via-webhook.md`).
- **Chamar a API a partir do n8n:** nó HTTP Request com o endpoint do artigo e o token (molde em `references/moldes-de-codigo.md`).
- **Chamar o n8n no meio de um fluxo do chatbot:** bloco HTTP Request do FlowBuilder (`recursos/n8n-via-flowbuilder.md`). O desenho do fluxo em si é da skill `cmv-flowbuilder`.
- **Iniciar um fluxo a partir de outra ferramenta:** Webhook Trigger, que exige `nome`, `celular` e `email` no JSON (`api/webhook-triggers.md`, `recursos/gatilho-via-webhooks-trigger.md`), ou a API de iniciar fluxo (`recursos/gatilho-via-api.md`). Para Make e Zapier a documentação só os cita como exemplos de uso do Webhook Trigger; não há passo a passo.

## Exemplos de pedido → entrega

**"Preciso que meu sistema de pedidos mande um WhatsApp pro cliente quando o pedido for aprovado."**
Pergunte o tipo de conexão. Se for QR Code: `api/api-mensagem-de-texto.md` (vale para Básica e Pro). Se for Oficial: explique a janela de atendimento; como o cliente pode não ter falado nas últimas 24 horas, o caminho seguro é template (`api/api-oficial-mensagem-template.md`; pelo Hub, só o template sem variável tem artigo). Entregue: (1) onde definir o token; (2) como guardar em `CMV_TOKEN`; (3) o cURL com o payload do artigo e os valores a trocar; (4) o comando do teste com Status da Conexão; (5) a fonte.

**"Como transfiro um atendimento pro setor Financeiro pela API?"**
Selo Todas: não precisa perguntar a conexão. Use `api/api-atualizar-ticket.md` com `ticketId` e `queueId`, e avise que existe uma chamada de nome parecido que move todos os tickets da conexão e não é a que ela quer. Diga de onde vêm o `ticketId` (número entre parênteses no cabeçalho da conversa; se é um sistema que precisa achá-lo sozinho, o `chamadoId` do webhook ou a API Listar Tickets do Contato) e o `queueId` (a chamada que lista os Setores).

**"Quero que toda mensagem que chega caia no meu n8n."**
Webhook da Conexão (tudo da conexão) ou do Setor (só um Setor). Passos numerados: criar o nó Webhook em POST no n8n, copiar a URL de produção, colar em **Conexões › editar a Conexão › aba Integrações**, campo **Webhook**. Depois siga a receita de `references/moldes-de-codigo.md` para dizer qual aviso tratar e como responder.

**"No n8n as mensagens chegam duplicadas e o áudio vem vazio. Minha conexão é a Oficial."**
É diagnóstico: use a tabela sintoma → causa → artigo de `references/moldes-de-codigo.md` e o formato de diagnóstico abaixo. Não pergunte da janela: a integração responde a quem acabou de escrever.

## Formato da resposta para a pessoa

Muita gente que pede integração não programa. Entregue nesta ordem, em passos numerados:

1. **O que vai acontecer**, em uma frase, incluindo o efeito sobre o atendimento (abre ticket? muda de Setor?).
2. **Antes de começar:** onde pegar o token (caminho do menu) e os pré-requisitos (API Externa, nas chamadas da API; Botões, se for o caso). Os artigos de webhook não citam a API Externa: não a ponha como pré-requisito para receber webhook.
3. **O material pronto para colar** (um bloco só), com os valores a trocar listados logo abaixo e de onde vem cada um.
4. **Como testar sem risco**, com o comando do teste, e o que esperar; se der erro, o que conferir primeiro.
5. **Avisos** do artigo que se aplicam ao caso.
6. **Fonte:** título do artigo e link.

Caminho de arquivo da skill (`api/...`, `recursos/...`, `references/...`) não vai na resposta, nem entre parênteses no meio do texto: a pessoa não tem esses arquivos. Onde este arquivo escreve `api/api-encerrar-ticket.md`, a resposta escreve "API Encerrar Ticket" e o link da linha **Fonte**, que é `https://clihelper.chatmasterveloz.com/docs/` seguido do nome do arquivo sem `.md`.

### Quando o pedido é um diagnóstico ("está duplicado", "vem vazio", "dá erro")

A pessoa já tem algo montado e quer saber por que falha. A ordem muda, porque ela precisa primeiro da causa:

1. **Causa provável**, uma por sintoma, com o artigo que a explica. Se houver mais de uma causa documentada, liste-as e diga como distinguir (por exemplo, olhando o campo `acao` dos dois avisos repetidos).
2. **Correção**, em passos numerados, com o material pronto quando houver.
3. **O que a documentação não diz** sobre o caso, separado do resto e marcado como tal. Dedução sua entra aqui, com a palavra "inferência", nunca misturada à causa documentada.
4. **Como confirmar:** o que a pessoa deve olhar (um aviso real, o corpo do erro) e, se não bater, o Suporte.
5. **Fonte.**

Para erro em chamada de API, comece pelo que `api/estrutura-de-api.md` manda conferir (token, endereço, conexão informada com o Token da Empresa, tipo de token) e pelas linhas ⚠️ do artigo da chamada.

## Onde termina esta skill

| Assunto | Skill |
|---|---|
| Desenhar ou gerar o fluxo do chatbot, blocos e variáveis do FlowBuilder | `cmv-flowbuilder` |
| Redigir o texto de templates, respostas rápidas, campanhas e agendamentos | `cmv-mensagens` |
| Configurar um recurso pela tela, dúvidas de uso e erros do painel | `cmv-ajuda` |
| Prompts e configuração de IA | `cmv-agente-ia` |
| CSS e JS personalizados do painel | `cmv-painel-css-js` |
