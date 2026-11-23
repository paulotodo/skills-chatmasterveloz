# Formato do arquivo .json de fluxo (observado)

> **Isto não é documentação oficial.** É o formato **observado em um arquivo exportado** pela plataforma (um fluxo real com 193 blocos e 269 ligações, 14 tipos de bloco), cruzado com os artigos de `references/docs/recursos/`. A documentação só diz que **Exportar Fluxo** baixa um `.json` e que **Importar** aceita "um arquivo exportado de um fluxo" (Visão Geral FlowBuilder (`references/docs/recursos/visao-geral-flowbuilder.md`)); ela não descreve o conteúdo do arquivo. O formato pode mudar entre versões da plataforma.
>
> Duas consequências práticas:
> 1. Só gere JSON com o que está nesta página. Campo, tipo ou valor que não aparece aqui não foi observado: não invente.
> 2. Importar um arquivo **escrito fora da plataforma** não foi testado por quem escreveu esta skill. Por isso todo JSON entregue vai com a conferência no editor e o teste descritos no `SKILL.md`.
>
> Se a pessoa tiver um fluxo exportado da própria conta com um bloco que não está aqui, peça o arquivo: ele mostra o formato daquele bloco na versão dela, e vale mais do que esta página.

**Quando ler esta página:** para entender ou diagnosticar um arquivo exportado, e para gerar algo que o gerador não cobre. Para gerar um fluxo comum, basta `references/descricao-compacta.md`: o `scripts/gerar_fluxo.py` já escreve neste formato.

## Sumário

1. [Estrutura geral](#1-estrutura-geral)
2. [Campos de cada bloco](#2-campos-de-cada-bloco-nodes)
3. [Ligações](#3-ligações-connections)
4. [IDs](#4-ids)
5. [Bloco da documentação ↔ `type`](#5-bloco-da-documentação--type)
6. [Tipo por tipo: `data` e saídas](#6-tipo-por-tipo-data-e-saídas)
7. [Números e enums: o que foi confirmado](#7-números-e-enums-o-que-foi-confirmado)
8. [IDs de Setor e de tag](#8-ids-de-setor-e-de-tag-são-da-conta)
9. [Blocos sem formato observado](#9-blocos-sem-formato-observado)
10. [Como gerar e conferir](#10-como-gerar-e-conferir)

## 1. Estrutura geral

```json
{ "nodes": [ ...blocos... ], "connections": [ ...ligações... ] }
```

Só essas duas chaves. O nome do fluxo não está no arquivo: ao importar, ele entra como *Fluxo Importado* seguido de um número.

## 2. Campos de cada bloco (`nodes`)

```json
{
  "id": "Xk3mPq7RtY2wZa9BcD4eFg6HjK8LnM",
  "position": { "x": 300, "y": 200 },
  "data": { },
  "type": "singleBlock",
  "width": 198,
  "height": 95,
  "style": { "backgroundColor": "#13111C", "padding": 0, "borderRadius": 8 }
}
```

| Campo | Observado |
|---|---|
| `id` | texto único; ver [IDs](#4-ids) |
| `position` | `x` e `y`, inteiros ou decimais, positivos ou negativos |
| `data` | o conteúdo do bloco; muda por tipo (seção 6) |
| `type` | o tipo do bloco (seção 5) |
| `width`, `height` | medidas do bloco na tela, em todos os 193 blocos |
| `style` | sempre com `backgroundColor`, `padding` e `borderRadius`; em 190 blocos é o do exemplo acima (3 blocos tinham `#000000` e `padding` 1; significado não confirmado) |
| `selected`, `positionAbsolute`, `dragging` | presentes em só 77 dos 193 blocos: opcionais. Não gere. |

Medidas vistas por tipo (largura × altura): `start` 155×58; `singleBlock` 198×95 com um item, crescendo cerca de 54 por item; `menu` 155×145 com duas opções, crescendo cerca de 24 por opção e por saída extra (**Resposta inválida**, **Sem resposta**); `tag` e `queue` 195×92; `question`, `variable` e `internal` 198×92; `interval` 195×92; `wbh` 208×92; `condition` 198×216; `switch` 210×266 com quatro regras; `away` 195×169; `close` 197×94; `email` 178×136.

Posição: no arquivo observado, o bloco seguinte fica em geral 300 à direita do anterior, e os ramos de um mesmo bloco se espalham na vertical. Depois de importar, o botão **Organizar automaticamente** do editor rearruma tudo (Como Usar o Editor de Fluxos (`references/docs/recursos/como-usar-o-editor-de-fluxos.md`)).

## 3. Ligações (`connections`)

```json
{
  "style": { "stroke": "#667eea", "strokeWidth": 3 },
  "animated": false,
  "type": "smoothstep",
  "source": "<id do bloco de origem>",
  "sourceHandle": "a",
  "target": "<id do bloco de destino>",
  "targetHandle": null,
  "id": "reactflow__edge-<source><sourceHandle>-<target>"
}
```

- `style`, `animated` e `type` são idênticos nas 269 ligações. `targetHandle` é sempre `null`. `selected` aparece em 7 delas: não gere.
- `sourceHandle` diz **de qual saída** do bloco a ligação parte. Os valores possíveis dependem do tipo do bloco (seção 6).
- Nenhuma ligação chega ao bloco `start`, e nenhum par (bloco, saída) tem mais de uma ligação.
- Um mesmo bloco pode receber várias ligações. Voltar a um bloco anterior (por exemplo, da mensagem de "não entendi" de volta ao menu) é uma ligação comum.

## 4. IDs

- **Bloco Início:** `"1"`.
- **Demais blocos:** 30 caracteres, letras maiúsculas, minúsculas e números, sem repetição no arquivo. Como a plataforma os gera não é conhecido; para um arquivo novo, sorteie 30 caracteres de `A-Z a-z 0-9` para cada bloco.
- **Ligação:** o texto `reactflow__edge-`, o `source`, o `sourceHandle`, um hífen e o `target`, tudo colado. Vale para as 269 ligações observadas.
- **Regra do Switch (tags):** `r` seguido de 12 letras minúsculas e números (4 regras observadas). A saída da regra é `regra-` mais esse id.

A janela do bloco **Pular para** mostra um ID curto de seis caracteres, como *(#rSseSA)* (Pular para (`references/docs/recursos/bloco-pular-para.md`)). A relação entre esse ID curto e o `id` do arquivo não foi confirmada.

## 5. Bloco da documentação ↔ `type`

| Bloco (nome na documentação) | `type` | Em que a correspondência se apoia |
|---|---|---|
| Início | `start` | `data.label` é "Início"; único bloco sem entrada |
| Conteúdo (`references/docs/recursos/bloco-conteudo.md`) | `singleBlock` | itens `message`, `interval` e `img` com `caption`, como os itens Texto, Intervalo e Imagem com Legenda (Caption) do artigo |
| Menu (`references/docs/recursos/bloco-menu.md`) | `menu` | opções numeradas, `enableElse`, `semResposta`, textos de lista e de botões, como os campos do artigo |
| Pergunta (`references/docs/recursos/bloco-pergunta.md`) | `question` | texto da pergunta; nos 3 casos, seguida de um bloco `variable`, como o artigo manda |
| Variável (`references/docs/recursos/bloco-variavel.md`) | `variable` | `data.message` é sempre um nome entre `%` |
| Condição (`references/docs/recursos/bloco-condicao.md`) | `condition` | campos `key`, `condition`, `value` e duas saídas |
| Switch (tags) (`references/docs/recursos/bloco-switch-tags.md`) | `switch` | regras com nome, operador e tags; uma saída por regra e a saída `fallback` |
| Tag (`references/docs/recursos/bloco-tags.md`) | `tag` | um ID e um nome de tag; os mesmos IDs aparecem nas regras do `switch` |
| Intervalo (`references/docs/recursos/bloco-intervalo.md`) | `interval` | `sec` "1" com o rótulo "Intervalo 1 seg." |
| Msg Interna (`references/docs/recursos/bloco-msg-interna.md`) | `internal` | um texto e uma saída |
| Execução de Código JS (`references/docs/recursos/bloco-execucao-de-codigo-js.md`) | `wbh` | `data.message` é código JavaScript com `return`; o campo do artigo se chama **Webhook (JS Script)** |
| Horário de Expediente (`references/docs/recursos/bloco-horario-de-expediente.md`) | `away` | um Setor e duas saídas |
| Enviar e-mail (`references/docs/recursos/bloco-enviar-e-mail.md`) | `email` | visto no editor em 23/11/2026, não num arquivo exportado: os campos do bloco e as saídas **Enviado** e **Não enviado** |
| Setor (`references/docs/recursos/bloco-setor.md`) | `queue` | **hipótese, pelo nome e pela estrutura:** um ID e um nome de Setor, sem saída; *queue* é fila, o nome antigo de Setor (Setores & Chatbot (`references/docs/recursos/setores-e-chatbot.md`)). Conferir no editor. |
| Encerrar (`references/docs/recursos/bloco-encerrar.md`) | `close` | **hipótese, pelo nome e pela estrutura:** uma mensagem, sem saída. Conferir no editor. |

`queue` e `close` são hipótese porque outros blocos têm a mesma forma: **Trocar Fluxo** também pede um Setor e não tem saída, e **Encerrar Mensagem Rápida** também tem uma mensagem e não tem saída; o `type` desses dois não foi observado. Depois de importar, confira no desenho se os blocos aparecem mesmo como **Setor** e **Encerrar**.

## 6. Tipo por tipo: `data` e saídas

Em todos os tipos de uma saída só, o `sourceHandle` é `"a"`.

### `start` (Início)

```json
{ "id": "1", "type": "start", "data": { "label": "Início" }, "width": 155, "height": 58 }
```

Saída: `a`. Um por fluxo.

### `singleBlock` (Conteúdo)

```json
"data": {
  "seq": ["message0", "interval0", "message1"],
  "elements": [
    { "type": "message",  "value": "Olá! Tudo bem?", "number": "message0" },
    { "type": "interval", "value": "2",              "number": "interval0" },
    { "type": "message",  "value": "Como posso ajudar?", "number": "message1" }
  ]
}
```

- `elements` guarda os itens; `seq` guarda a **ordem de envio**, pelos `number`. Nos blocos salvos pelo editor, `elements` vem agrupado por tipo (textos, depois intervalos, depois imagens) e só `seq` intercala. Em um arquivo novo, escreva as duas listas na mesma ordem.
- `number` é o tipo do item mais um contador que começa em 0 **por tipo** (`message0`, `message1`, `interval0`…). Há blocos com salto no contador; o que importa é não repetir e bater com `seq`.
- `message`: `value` é o texto (item **Texto**).
- `interval`: `value` é o tempo em segundos, **como texto** (item **Intervalo**). Vistos: "1", "2" e "60".
- `img`: `value` é um nome de arquivo dado pela plataforma (13 dígitos mais a extensão), `original` é o nome do arquivo enviado e `caption` é a legenda. O arquivo em si não está no JSON. **Não gere itens de imagem:** deixe a instrução para a pessoa incluir a imagem no editor.
- Itens **Áudio**, **Vídeo** e **Arquivo**: não observados.

Saída: `a`.

### `menu` (Menu)

```json
"data": {
  "message": "Com qual assunto podemos ajudar?",
  "arrayOption": [
    { "number": 1, "value": "Comprar", "description": "Orçamentos e pedidos novos" },
    { "number": 2, "value": "Suporte", "description": "" }
  ],
  "botfiles": "",
  "menuType": "list",
  "listButtonText": "Ver opções",
  "listHeaderText": "",
  "listFooterText": "",
  "buttonHeaderText": "",
  "buttonFooterText": "",
  "enableElse": true,
  "semResposta": { "minutos": 30 }
}
```

- `message`: o texto do menu. `arrayOption[].value` é o título da opção e `description`, a descrição (pode ser vazia). `number` é inteiro, de 1 em diante, em ordem.
- `menuType`: só `"list"` foi observado. Com os campos de lista preenchidos e opções com descrição, corresponde ao **Menu em Lista** do artigo. Os valores de **Menu em Texto** e **Menu em Botões** não foram observados. Por isso esses dois tipos **não podem ser gerados em JSON**: o menu vai como Lista, e quem preferir texto ou botões troca o **Tipo de Menu** no editor depois de importar (o artigo diz que as opções já criadas continuam na troca).
- `listButtonText`, `listHeaderText`, `listFooterText`: **Texto do Botão da Lista**, **Cabeçalho** e **Rodapé da Lista**. `buttonHeaderText` e `buttonFooterText` (título e rodapé dos botões) e `botfiles` (provavelmente a imagem de capa) estavam sempre vazios.
- `enableElse`: `true` ou `false`, o **Caminho alternativo (ELSE)**.
- `semResposta`: presente só quando o **Sem resposta** está ligado, com `minutos` inteiro (vistos: 120, 1320, 1440 e 2880). Para desligar, omita a chave.
- Limites do artigo para a lista: opção até 20 caracteres, descrição até 72, botão da lista até 20, cabeçalho e rodapé até 60, texto principal até 1024.

Saídas:

| `sourceHandle` | Saída no editor | Existe quando |
|---|---|---|
| `a1`, `a2`, … `aN` | opção de `number` N | sempre, uma por opção |
| `else` | **Resposta inválida** | `enableElse` é `true` (11 de 11 casos) |
| `semResposta` | **Sem resposta** | há `semResposta.minutos` (11 de 11 casos) |

### `question` (Pergunta)

```json
"data": { "message": "Qual é o seu nome?", "arrayOption": [] }
```

Saída: `a`. Os campos **Sem resposta** e **Mover de setor por inatividade** do artigo **não aparecem** nos 3 blocos observados (nenhum usava): como ficam no JSON não é conhecido. Se o fluxo precisa deles, instrua a pessoa a abrir a Pergunta no editor e preencher.

### `variable` (Variável)

```json
"data": { "message": "%nome%", "arrayOption": [] }
```

`message` é o nome da variável entre `%`. Saída: `a`. Posição no fluxo: logo depois da fonte do dado (Pergunta, Menu, Execução de Código JS ou Início), só com Intervalo no meio.

### `condition` (Condição)

```json
"data": { "key": 1, "condition": 1, "value": "sim" }
```

- `key` é o **Tipo**, `condition` é a **Condição** e `value` é o **Valor**. Só três combinações foram observadas; veja a seção 7 antes de usar.
- No tipo Anúncio há mais um objeto: `"anuncio": { "campo": "id", "operador": "igual", "valor": "<ID do anúncio>" }`, e `value` traz um resumo em texto que contém esse ID.

Saídas: `a` e `b`. Hipótese forte, não confirmada: `a` = **Verdadeiro**, `b` = **Falso** (seção 7). Conferir no editor.

### `switch` (Switch (tags))

```json
"data": { "rules": [
  { "id": "r8k2m5x9q1w3e", "label": "VIP", "operator": "possui", "tagIds": [123] }
] }
```

- `label` é o **Nome da saída**; `tagIds` é a lista de IDs de tag; `operator` só foi visto como `"possui"`, sempre com uma tag (corresponde a **possui a tag**). Os outros três tipos de comparação do artigo não foram observados.
- A ordem das regras na lista é a prioridade (Switch (tags) (`references/docs/recursos/bloco-switch-tags.md`)).

Saídas: `regra-<id da regra>` para cada regra e `fallback` para **Nenhuma condição atendida**.

### `tag` (Tag)

```json
"data": { "sec": 123, "secName": "Pediu orçamento" }
```

`sec` é o ID da tag, inteiro; `secName` é o nome dela. Saída: `a`.

### `interval` (Intervalo)

```json
"data": { "label": "Intervalo 2 seg.", "sec": "2" }
```

`sec` é o tempo em segundos, como texto; `label` repete o tempo. Saída: `a`. O artigo aceita hoje de 1 segundo a 24 horas, em **Segundos**, **Minutos** ou **Horas**, e dá ao bloco com mais de 2 minutos a saída **Janela expirada**; os arquivos observados são de antes disso, então a **Unidade**, a escolha **Se o cliente responder durante a espera** e essa saída não têm formato observado. O gerador fica em até 120 segundos.

### `internal` (Msg Interna)

```json
"data": { "message": "Cliente %nome% escolheu a opção Financeiro.", "arrayOption": [] }
```

Saída: `a`.

### `wbh` (Execução de Código JS)

```json
"data": { "message": "return \"%cpf%\".replace(/\\D/g, '');", "condition": 2, "arrayOption": [] }
```

`message` é o código. `condition` foi sempre 2 (seção 7). Saída: `a`. Para guardar o `return`, o bloco seguinte é um `variable` (pode haver um `interval` entre os dois).

### `away` (Horário de Expediente)

```json
"data": { "sec": 45, "secName": "Suporte" }
```

`sec` e `secName` são o ID e o nome do Setor de onde vem o horário. A opção **Setor vinculado ao fluxo** não foi observada num arquivo exportado; num bloco importado com `"sec": 0`, a janela do bloco abriu com ela escolhida (22/11/2026). Saídas: `a` = **Dentro do Horário**, `b` = **Fora do Horário** (seção 7).

### `queue` (Setor)

```json
"data": { "sec": 45, "secName": "Suporte" }
```

`sec` é o ID do Setor, inteiro; `secName` é o nome. Sem saída.

### `close` (Encerrar)

```json
"data": { "message": "Até mais!", "arrayOption": [] }
```

`message` é a **Mensagem** final; nos 2 blocos observados estava vazia. Sem saída.

### `email` (Enviar e-mail)

```json
"data": { "origem": "conta", "contaId": 12, "provedorId": null, "para": "", "assunto": "Seu pedido, {{name}}", "corpo": "Recebemos o seu pedido." }
```

`origem` `"conta"` com `contaId` é o envio por uma conta do menu **Contas de E-mail**, escolhida em **Enviar por**. O valor de `origem` para um provedor de envio por API e o uso de `provedorId` não foram observados: não gere. `para` vazio é o e-mail do contato; `assunto` e `corpo` são **Assunto** e **Mensagem**. Saídas: `a` = **Enviado**, `b` = **Não enviado** (o editor mostra o rótulo ao lado de cada saída).

Visto em 23/11/2026 no que o editor grava ao salvar um fluxo com o bloco, não num arquivo exportado. No mesmo dia, um arquivo do gerador com `"contaId": 0` foi importado: o bloco apareceu com as duas saídas ligadas e abriu com **Enviar por** vazio e os outros campos preenchidos. O que acontece numa conversa que chega ao bloco sem conta escolhida não foi testado.

## 7. Números e enums: o que foi confirmado

"Confirmado" quer dizer: o valor do arquivo bate diretamente com um campo que o artigo do bloco descreve. O resto está como **observado, significado não confirmado**, com os valores vistos e, quando há, a hipótese e o indício. Hipótese não é fato: todo bloco gravado com valor de hipótese vai para a lista **Conferir no editor** da entrega.

| Campo | Valor | Situação |
|---|---|---|
| `condition.data.key` | `1` | Observado (7 blocos), significado não confirmado. Hipótese forte: **Resposta da Pergunta**. Os 7 blocos estão em cadeias que começam logo depois de Execução de Código JS → Intervalo → Variável, e em 5 deles o `value` é igual a um texto que um bloco de código do fluxo devolve no `return`; o artigo diz que esse tipo, depois de uma Variável, compara o valor que ela guardou. É lastro indireto: conferir no editor. |
| `condition.data.key` | `12` | **Confirmado: Anúncio.** Vem com o objeto `anuncio` e `campo` igual a `id`, um dos dados que o artigo lista para esse tipo. |
| `condition.data.key` | `2` | Observado (1 bloco), significado não confirmado. Indício de que é **Tag**: o `value` é uma lista separada por vírgula, e um dos itens é o nome de uma tag usada no mesmo fluxo. |
| `condition.data.key` | demais | Não observados: Horário, É Dia Útil?, É Feriado?, Qual Dia da Semana?, ID da Conexão, Status do Atendimento, Protocolo Fechado, Postagem, Tipo de Postagem. |
| `condition.data.condition` | `1` (com `key` 1) | Observado (7 blocos), significado não confirmado. Hipótese: **Igual**. O `value` é idêntico ao texto comparado, o que também serviria a **Contém**. |
| `condition.data.condition` | `3` (com `key` 2) | Observado (1 bloco), significado não confirmado. Hipótese: **Contém**, a única condição de Tag que o artigo descreve com lista separada por vírgula. |
| `condition.data.condition` | `11` (com `key` 12) | Observado (8 blocos), significado não confirmado. A comparação de fato parece estar em `anuncio.operador` (`"igual"`). |
| saídas de `condition` | `a`, `b` | Observado (16 blocos), significado não confirmado: o artigo não diz qual saída é qual no arquivo. Hipótese forte: `a` = **Verdadeiro**, `b` = **Falso**. Em 12 dos 16 blocos, `b` leva a outra Condição e `a` leva à ação (uma Tag), o desenho da "condicional aninhada" do artigo, em que a próxima verificação fica no caminho do "se não for". Conferir no editor, como no Horário de Expediente. |
| `wbh.data.condition` | `2` | Observado (12 blocos), significado não confirmado. Hipótese: o campo **Tipo** (**MENU** ou **REQUISIÇÃO**). |
| saídas de `away` | `a`, `b` | Visto numa conversa de teste em 22/11/2026, com um fluxo gerado e importado: com o Setor fechado no dia, o fluxo seguiu por `b` (**Fora do Horário**); com o dia aberto, por `a` (**Dentro do Horário**). O arquivo sozinho não diz qual é qual. |
| `menu.data.menuType` | `"list"` | **Confirmado: Menu em Lista.** Outros valores não observados. |
| `switch` `operator` | `"possui"` | **Confirmado: possui a tag** (uma tag por regra, e o nome da regra igual ao da tag). Outros valores não observados. |
| `interval.data.sec` e item `interval` | texto com número | **Confirmado: segundos** (o `label` do bloco repete o número com "seg."). |

Regra de uso: valor "não confirmado" só entra em um JSON gerado se a combinação inteira foi observada, e o bloco vai para a lista **Conferir no editor** da entrega, com o que deve estar escolhido em cada campo. Para qualquer outra Condição, use o roteiro de montagem ou um marcador (seção 10).

## 8. IDs de Setor e de tag são da conta

`sec` (em `tag`, `queue` e `away`) e `tagIds` (em `switch`) são números da conta de cada empresa. Um arquivo com os IDs de outra conta aponta para Setores e tags que não existem ali, ou para os errados.

Onde a pessoa encontra os números, segundo a documentação:

- **Tag:** no menu **Tags**, cada tag mostra, do lado direito, o **ID**, "número ID da tag, utilizado para automações" (Visão Geral Tags (`references/docs/recursos/visao-geral-tags.md`)).
- **Setor:** no menu **Setores & Chatbot**, o card de cada Setor mostra um número com cerquilha, como *#9*, "o identificador do Setor no sistema" (Visão Geral Setores & Chatbot (`references/docs/recursos/visao-geral-setores-e-chatbot.md`)).

Que esses números sejam exatamente os que o arquivo guarda em `sec` é uma dedução (o nome dos campos e os valores são compatíveis), não algo que a documentação afirme. Por isso, com ou sem os IDs, a entrega sempre pede para conferir no editor se cada bloco **Setor**, **Tag**, **Horário de Expediente** e **Switch (tags)** mostra o nome certo.

Sem os IDs, use marcadores: `"sec": 0` e `"secName": "TROCAR: Setor Comercial"` (em `switch`, `"tagIds": [0]` e o `label` normal). É o que o gerador grava quando a descrição não traz `id`. No `email`, o `contaId` também é da conta e o artigo do bloco não diz onde ver esse número: sem `conta_id` na descrição, o gerador grava `"contaId": 0` e a pessoa escolhe a conta em **Enviar por**. O validador lista cada um em **VALORES A TROCAR**. O que acontece ao importar um bloco com ID que não existe na conta não foi testado; a instrução para a pessoa é abrir cada bloco marcado com duplo clique e escolher o Setor ou a tag na lista.

## 9. Blocos sem formato observado

Para estes, **não gere JSON**. Use o roteiro de montagem, ou importe o que dá e complete no editor.

Asaas, Avaliação do Atendimento, Botões, Carrossel de Produtos, Contato, É Seguidor?, Encerrar Mensagem Rápida, Enviar Figurinha, Enviar Localização, GPT Assistant (OpenAI), HTTP Request, Link do Chat Externo, Operador, Oportunidade, PDV (pedido no fluxo), Pixel META, Pular para, Randomizador, Remover Tag, Reservas (agendar no fluxo), Responder Comentário, Retornar último atendimento, Rodízio, Template, Trocar Fluxo, Typebot, Webview.

Também sem formato observado, dentro de blocos conhecidos: Menu em Texto e Menu em Botões; itens Áudio, Vídeo e Arquivo do Conteúdo; os tipos de Condição fora dos três da seção 7; as comparações do Switch (tags) fora de **possui a tag**; **Sem resposta** na Pergunta; **Setor vinculado ao fluxo** no Horário de Expediente; Intervalo com mais de 2 minutos (saída **Janela expirada**), em **Minutos** ou **Horas**, ou com **Cancelar a espera (o fluxo para aqui)**.

## 10. Como gerar e conferir

1. **Use o gerador.** `scripts/gerar_fluxo.py` recebe uma descrição compacta (blocos com apelido e ligações por apelido) e escreve o arquivo neste formato, com IDs, posições e campos de topo, e já roda o validador. A descrição está explicada em `references/descricao-compacta.md`. Não escreva o JSON à mão nem refaça um script para isso: um fluxo de 20 blocos tem 20 IDs de 30 caracteres e dezenas de ligações cujo `id` repete os IDs dos blocos.
2. **Onde o fluxo pede um bloco sem formato observado** e de uma saída só segundo o artigo (Botões, Template, Oportunidade, Contato, Enviar Localização, Link do Chat Externo), use o tipo `marcador` do gerador: ele grava um bloco `internal` com o texto `TROCAR NO EDITOR: …`. Se alguém esquecer de trocar, é uma nota interna que o cliente não vê, e a conversa segue. Para HTTP Request, Remover Tag, Webview e Carrossel de Produtos, o artigo não diz quantas saídas o bloco tem: o marcador guarda o lugar, com o aviso de conferir as saídas no editor. Para bloco com mais de uma saída (Condição de horário, Randomizador, Asaas…), não há substituto: use o roteiro de montagem para o fluxo todo, ou gere o trecho antes dele e descreva o resto.
3. **Confira um arquivo que não veio do gerador** (um fluxo exportado pela pessoa, por exemplo) com o validador:

   ```bash
   python3 scripts/validar_fluxo.py caminho/do/fluxo.json          # marcadores aparecem em VALORES A TROCAR
   python3 scripts/validar_fluxo.py caminho/do/fluxo.json --final  # marcador vira erro
   ```

   Ele confere: um único Início, IDs únicos, ligações que apontam para blocos existentes, saídas coerentes com o tipo (opções do menu, regras do switch), saídas sem ligação, blocos não alcançáveis, ciclo sem espera, limites de texto do Menu em Lista, Variável longe da fonte do dado e valores a trocar. Código de saída diferente de zero quer dizer erro. Tipo de bloco que não está nesta página vira aviso, não erro. `python3 scripts/validar_fluxo.py --teste` roda o autoteste.
4. **Só edite o JSON direto** quando precisar de algo que está nesta página e o gerador não cobre (a Condição de Anúncio, por exemplo). Gere o resto com o gerador, altere o arquivo e rode o validador de novo.
5. **Sem terminal**, não há como rodar gerador nem validador: prefira o roteiro de montagem. Se ainda assim entregar um JSON, confira à mão a lista do item 3 e diga na resposta que nenhum script foi executado.

O validador confere a **estrutura**. Ele não sabe se o texto está bom, se o Setor é o certo ou se a plataforma aceita o arquivo: isso é a conferência no editor (**Verificar** e **Resumo do fluxo**) e o teste.
