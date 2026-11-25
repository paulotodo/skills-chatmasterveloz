---
name: cmv-painel-css-js
description: "Use quando alguém quer mudar a aparência ou o comportamento do painel do Chat Master Veloz (CMV, chatmasterveloz) além do que as configurações oferecem: pôr as cores da empresa, consertar o modo escuro ilegível, esconder ou reordenar menus e botões, aumentar fontes, trocar textos, mostrar avisos na tela, na aba do navegador ou por som, mudar o login, as janelas e o Chat Externo. Quem tem esta skill usa o CMV: pedido sobre o painel ou a tela de atendimento que não cite outro site ou ferramenta é dela, mesmo sem dizer CMV, CSS ou JS (\"deixar com a cara da minha empresa\", \"qual seletor uso\"); carregue-a antes de responder: os seletores custom-css, onde colar e o que é seguro pôr no script vêm dela. Fora do escopo: configurar recursos, permissões e as cores do Web Chat do site (cmv-ajuda), API e webhooks (cmv-api), fluxos (cmv-flowbuilder), IA (cmv-agente-ia), textos para clientes (cmv-mensagens), e CSS de outros sites ou plataformas (WordPress, Chatwoot, WhatsApp Web)."
---

# CSS e JS personalizados do painel Chat Master Veloz

O painel `app.chatmasterveloz.com` aceita CSS e JS personalizados em campos próprios. Cada tela, cada janela e boa parte do que há dentro delas têm uma classe `custom-css-*` e atributos `data-*` feitos para isso: são os únicos nomes que continuam os mesmos quando a plataforma é atualizada. O catálogo completo desses nomes está em `references/docs/` (versão WS-30.141.0, cerca de 670 KB).

O trabalho desta skill é transformar um pedido em linguagem comum ("muda as cores", "esconde tal coisa") em código que usa **só** nomes do catálogo, dizer onde colar e como desfazer, e reconhecer quando o que a pessoa quer não tem âncora.

## Limites com as outras skills

| O pedido é… | Skill |
|---|---|
| mudar aparência, esconder, reordenar, reagir a algo na tela com CSS ou JS | esta |
| como usar ou configurar um recurso do painel (inclusive permissões por perfil e a Cor Principal) | `cmv-ajuda` |
| chamar a API, webhooks, tokens, n8n | `cmv-api` |

JS do painel não é lugar para chamar a API com token: todo usuário logado consegue ler o script (ver Segurança). Se o pedido exige token, a solução é uma integração fora do painel, com a `cmv-api`.

## O material

`references/docs/` tem os 15 arquivos numerados (`00` a `14`) mais o `INDICE.md` gerado, que é só a lista dos títulos, e a pasta `revendedor/recursos/`, com seis artigos da documentação do revendedor (Super Admin) sobre as telas onde ficam os campos, as cores e os logotipos. Não leia tudo: os grandes são listas para buscar. Leia `01` e `02` inteiros na primeira vez (são curtos) e busque nos demais. O `00-LEIA-PRIMEIRO.md` não precisa ser lido: o mapa e as regras dele estão aqui embaixo, e ele cita dois arquivos que não fazem parte desta skill (`catalogo-css.pt.json`, a cópia bruta do catálogo, e `_gerar.py`, que a regenera); não os procure nem os cite para a pessoa. O mapa:

| Preciso de… | Arquivo em `references/docs/` | Como achar |
|---|---|---|
| uma solução pronta para um pedido comum | `references/receitas.md` (fora de `docs/`) | ler o sumário |
| regras básicas e convenções de nome | `01-fundamentos.md` | ler inteiro |
| em que campo escrever, ordem de carga, regras do JS | `02-campos-css-js.md` | ler inteiro |
| variável CSS que muda comportamento (ordem do menu, ações do ticket, barra do topo…) | `03-propriedades-css.md` | `grep -n -A3 -- '--menu-ordem' references/docs/03-propriedades-css.md` |
| cores e variáveis do tema escuro (`--mui-*`) e a `--app-primary` | `04-tema-escuro.md` | ler inteiro |
| eventos que o JS pode ouvir | `05-eventos-js.md` | ler inteiro (hoje são dois: `sip:state` e `atendimentos:buscado`) |
| um atributo de estado `data-*`: onde existe e que valores tem | `06-atributos-data.md` | ``grep -n -A3 '^### `data-status`' references/docs/06-atributos-data.md`` |
| o id de uma tela (`#custom-css-<página>`) | `07-paginas.md` | `grep -n -i palavra` |
| a classe de uma janela (`.custom-css-modal-<nome>`) | `08-modais.md` | `grep -n -i palavra` |
| as âncoras de uma área ou componente | `09-ancoras-por-area.md` | ``grep -n -A2 '^### `Login`' references/docs/09-ancoras-por-area.md`` |
| em que área uma classe aparece, ou classes por palavra | `10-ancoras-indice-az.md` | `grep -n palavra` (uma classe por linha) |
| classes antigas do chat sem prefixo (`.ticket-name`, `.message-quoted`…) | `11-classes-sem-prefixo.md` | ler inteiro |
| a página pública do Chat Externo (Modo Alternativo) | `12-chat-externo.md` | ler inteiro |
| o que mudou em cada versão (um seletor parou de funcionar?) | `13-historico.md` | `grep -n 'seletor'` |
| as URLs do painel, para `location.pathname` | `14-rotas.md` | `grep -n palavra` |
| as telas de quem administra a instância: Cores, Logotipos / Ícones, Editar Empresa, Plataforma | `revendedor/recursos/` | ler o artigo da tela (são curtos) |

Buscar em tudo de uma vez: `grep -rn 'termo' references/docs/`. Os nomes misturam português e inglês (`ticket`, `quadro`, `funil`, `contact`, `contato`, `user`, `usuario`): se a primeira busca não achar, tente o outro idioma.

## As regras que valem sempre

São as sete do `00`, que o resto desta skill detalha:

1. Selecione por `custom-css-*` e por `data-*`. Nunca por `.Mui*` ou `.jss123`: mudam a cada atualização.
2. Página: `#custom-css-<página>`. Janela: `.custom-css-modal` (todas) mais `.custom-css-modal-<nome>` (aquela).
3. Classe diz **onde**; atributo `data-*` diz **quando** (estado). Tema escuro: `body[data-theme="dark"]`.
4. Para vencer o Material-UI às vezes é preciso `!important`.
5. CSS do painel vai no campo pós-login; o pré-login é público. Nenhum segredo em campo de JS.
6. O JS roda uma vez por carregamento, numa SPA: as telas e os elementos aparecem depois.
7. Se o elemento não tem âncora no catálogo, o alvo não existe. Não invente nome: confira antes de usar.

## Fluxo de trabalho

1. **Entenda o alvo.** Qual tela ou janela, qual elemento, para quem deve valer (todas as empresas, uma empresa, quem ainda não fez login, o cliente final no Chat Externo) e quais cores ou textos. Pergunte só o que falta para escrever; se a pessoa não deu a cor, use um exemplo e diga onde trocar.
2. **Veja se há receita.** `references/receitas.md` cobre os pedidos mais comuns, com os seletores já conferidos. Adapte em vez de começar do zero.
3. **Localize no catálogo.** Página em `07`, janela em `08`, o que há dentro em `09` (por área) e `10` (por palavra), estado em `06`, variáveis em `03` e `04`. As convenções do `01` (cabeçalho de página, corpo de janela, cartão de número, estado vazio, menus, popovers) resolvem muita coisa sem busca.
4. **Prefira CSS; JS só quando CSS não resolve.** CSS vale assim que o elemento aparece, não depende de quando o script rodou e não quebra o painel. Antes de pensar em JS, veja se uma variável do `03` já faz o que se quer (ordem do menu, quantas ações na barra, cor da barra do topo) ou se um atributo `data-*` já expõe o estado (o `<body>` muda com a chamada do ramal, por exemplo). JS é para o que CSS não alcança: reagir a clique, criar um aviso próprio, ouvir o evento do `05`.
5. **Escolha o campo** (tabela abaixo) e diga por que é esse.
6. **Escreva o código comentado**, entre `/* CMV-INICIO nome */` e `/* CMV-FIM */`, para a pessoa conseguir achar e apagar depois. No painel (CSS pós-login e da empresa), cubra os dois temas: toda cor fixa de fundo ou de texto pede a regra normal e a `body[data-theme="dark"] …` correspondente, senão um fundo claro fixo fica com texto claro por cima no escuro. Nas telas de entrada (pré-login) e no Chat Externo a referência não documenta tema escuro: ali, defina fundo e texto juntos na mesma regra, diga que o tema escuro dessas telas não está documentado e não entregue o par `body[data-theme="dark"]` como se fosse garantido. Dê escopo a cada seletor (`#custom-css-<página>` ou `.custom-css-modal-<nome>` na frente) quando o pedido é para uma tela só: o `10` mostra em quantas áreas uma classe aparece, e uma classe compartilhada sem escopo muda mais telas do que a pessoa pediu.
7. **Confira cada nome** com o script (seção seguinte). Só entregue o que passar.
8. **Entregue** no formato da seção "A resposta para a pessoa".

### Conferir antes de entregar

Salve o código num arquivo (pode ser temporário: a entrega é o bloco de código na resposta, então não cite o caminho do arquivo) e rode:

```bash
python3 scripts/conferir_seletores.py meu.css            # também aceita .js, .md (blocos css/js) e vários arquivos
python3 scripts/conferir_seletores.py --tipo js < meu.js   # ou pela entrada padrão
python3 scripts/conferir_seletores.py --detalhe meu.css    # mostra em que arquivo do catálogo cada nome está
```

O script confere um a um toda classe e id `custom-css-*`, todo atributo `data-*`, toda variável `--*`, as classes sem prefixo do chat e os eventos do `addEventListener`; acusa `.Mui*` e `.jss<número>`; sugere nomes parecidos; e sai com código diferente de zero se há problema. Variável e atributo que o próprio código cria não geram alarme. Além dos nomes:

- **Valor de atributo.** Em `[data-x="valor"]`, compara o valor com a linha Valores do atributo no `06` (e no `12`). Valor fora de uma lista fechada é **PROBLEMA** (`data-link="signup"`, quando o catálogo lista `cadastro`). Quando o catálogo não lista os valores (`data-menu`) ou a lista é aberta, sai um **AVISO** de "valor não conferido": o valor só pode ser confirmado pelo Inspecionar, e a resposta tem de dizer isso. A lista conferida é a união de todos os elementos que usam o atributo; se o valor vale **naquele** elemento, quem lê a entrada é você.
- **JS, pelas regras do `02`.** `return` no nível de cima é PROBLEMA (é erro de sintaxe, e código com erro não é injetado). O que parece segredo (`token`, `apikey`, `Bearer`, `Authorization`, senha atribuída a um texto) é PROBLEMA.
- **JS, por precaução desta skill** (o `02` não fala disso): `innerHTML` e chamadas de rede (`fetch`, `XMLHttpRequest`…) saem como AVISO, para você conferir que não há HTML montado com texto de cliente nem dado de cliente saindo do painel.
- Um AVISO de "só aparece no histórico" pede leitura da entrada indicada do `13` antes de usar o nome.

Isso existe porque inventar um nome ou um valor plausível (`.custom-css-menu-lateral`, `data-perfil`, `--mui-text`, `data-link="signup"`) é o erro mais fácil de cometer aqui, e o resultado é um CSS que não faz nada sem dar erro nenhum. Passar no script quer dizer só que os nomes existem no catálogo. Se o seletor está no elemento certo, se pega só a tela pedida e qual é o efeito visual, o script não sabe: isso é leitura sua do catálogo e teste da pessoa no painel. Não diga "conferido" querendo dizer "testado".

**Sem terminal:** confira cada nome por busca nos arquivos. Classe: `10-ancoras-indice-az.md` (uma por linha) ou a tabela de Convenções do `01`. Id de página: `07`. Janela: `08`. Atributo: o título ``### `data-nome` `` em `06` (e leia Onde e Valores). Variável: `03` e `04`. Sem prefixo: `11`. Chat Externo: `12`. Nome que você não encontrou escrito por inteiro não vai para a resposta.

## Em que campo colar

Os detalhes estão em `references/docs/02-campos-css-js.md`. O resumo para decidir:

| O que o código muda | Campo | Caminho no painel |
|---|---|---|
| telas públicas: login, cadastro, recuperar a senha | CSS pré-login (JS pré-login) | Configurações → Cores |
| o painel, para todo mundo que fez login | CSS pós-login (JS pós-login) | Configurações → Cores |
| o painel, só para uma empresa | CSS desta empresa (JS desta empresa) | Configurações → Empresas → editar a empresa → aba Configurações |
| a página de chat que o cliente final abre pelo link | CSS do Chat Externo (Modo Alternativo) | Configurações → Empresas → editar a empresa → aba Configurações |

- **Quem tem os campos.** Os dois caminhos são telas de quem administra a instância (o Super Admin, quem fornece a plataforma): Configurações → Cores vale para todas as empresas, e Configurações → Empresas → card da empresa → aba Configurações guarda o **CSS desta empresa** e o **JS desta empresa** (`revendedor/recursos/configuracoes-cores.md`, `revendedor/recursos/configuracoes-editar-empresa.md`). O `revendedor/recursos/configuracoes.md` diz que Configurações é onde a instância inteira é administrada e que, dos cards dela, o administrador de cada empresa vê na tela dele as **Opções**. O administrador de uma empresa cliente não chega nessas telas: para ele, entregue o código do mesmo jeito e diga que quem cola é quem fornece a plataforma. Link do site do revendedor só quando quem pergunta é o revendedor.
- A ordem de carga é pré-login → pós-login → empresa; em empate, vence o da empresa.
- Na dúvida entre pré e pós-login, é pós-login: o pré-login é público, e só deve ter o visual das telas públicas.
- Ao salvar, a página recarrega. O JS da empresa vale no próximo carregamento. No campo **CSS desta empresa**, num teste de 22/11/2026, salvar a empresa não recarregou a página: a regra só apareceu depois de recarregar à mão. Mande recarregar (F5) para conferir. No mesmo dia, no **JS desta empresa**: salvar também não recarregou a página; depois de recarregar, o script estava em `<script id="custom-js-company">`, no fim do `<body>`, depois do `custom-js-poslogin`, rodou uma vez e não rodou de novo ao trocar de tela. Depois de apagar o código do campo e salvar, o primeiro recarregamento ainda rodou o script e só no segundo ele não existia mais: ao desfazer um JS da empresa, mande recarregar duas vezes. No **CSS pré-login**, salvar recarregou a página, e a regra chegou à tela de login aberta sem sessão.

## Segurança, e o porquê de cada regra

- **O campo pré-login é público.** Ele é servido sem login: qualquer pessoa na internet lê o que está nele. Por isso vai ali só cor, fundo e logo das telas de entrada. Regra do painel, nome de fila, lógica de operação ou qualquer coisa que revele como a empresa trabalha vai no pós-login.
- **Nenhum segredo em nenhum campo de JS**: nem token de API, nem senha, nem chave. O pré-login é lido por qualquer pessoa sem login; o pós-login e o da empresa rodam no navegador de todo usuário autenticado, e qualquer um deles lê o script (`02`). O roteiro para esse pedido está logo abaixo.
- **O JS roda uma vez por carregamento, numa SPA.** Trocar de tela não roda o script de novo, e a tela que a pessoa quer mudar ainda não existe quando ele roda. Todo script precisa esperar o elemento (delegação de evento no `document`, `MutationObserver`, ou o evento do `05`); um `querySelector` solto no topo quase sempre devolve nada.
- **Não ler dados de clientes para enviar a terceiros, nem alterar dados.** Um script no painel enxerga nomes, telefones e mensagens de todo atendimento aberto. O que a regra permite: ler o que já está na tela para mostrar na própria tela, a quem já está vendo (destacar um cartão pelo `data-*` dele, pôr o número de quem liga no título da aba, como na receita 18). O que ela não permite: mandar esse conteúdo para fora do painel (outro servidor, planilha, webhook), guardar cópia dele, preencher ou enviar mensagens sozinho, ou clicar em botões pela pessoa. Se pedirem, diga que não faz e por quê; o caminho para integrar dados é a API (`cmv-api`). Esta é uma regra desta skill; o `02` não trata do assunto.
- **Use `textContent`, não `innerHTML`**, ao criar elementos, e nunca injete na página texto que veio de mensagem de cliente. Também é precaução desta skill, não regra do `02`.
- **Remover o script não desfaz o que ele ligou** (evento, temporizador). Só o recarregamento da página desliga. Diga isso no "como desfazer".
- **Esconder não é bloquear.** `display: none` tira o botão da vista, mas a tela continua abrindo pelo endereço e a ação continua permitida. Quando o pedido é de permissão, diga isso e explique que permissão por perfil se configura no painel (assunto da `cmv-ajuda`; o nome da skill não vai na resposta).

### Quando pedem para pôr token, senha ou chave no JS

É um pedido comum ("dá pra pôr o token da API no script pra puxar o nome do cliente?"). Responda nesta ordem:

1. **Recuse essa parte, com o porquê**: tudo o que está num campo de JS é lido por quem abre o painel (e, no pré-login, por qualquer pessoa na internet). Um token ali deixa de ser segredo: quem o copiar usa a API em nome da empresa.
2. **Se o token já foi colado em algum campo**, mesmo que por pouco tempo: mande apagar do campo e trocar o token (gerar outro e desativar o antigo). Como se troca é assunto da `cmv-api` e da `cmv-ajuda`; esta referência não descreve.
3. **Ofereça o que resolve a necessidade real.** Quase sempre a pessoa quer buscar ou enviar um dado. Isso é uma integração, feita num servidor ou numa ferramenta de automação, onde o token fica guardado: é o trabalho da `cmv-api`. O JS do painel não chama essa integração levando dado de cliente (regra acima).
4. **Entregue o resto do pedido normalmente.** A recusa vale para o token, não para o CSS e o JS que não dependem dele.

O script acusa como PROBLEMA o que parece segredo, mas não substitui esta conversa.

## Armadilhas que a referência esconde

- **`09` e `10` dão só o nome da âncora, sem descrição.** O significado vem do nome, da área e, quando há, do `06` e do `13` (busque o nome neles). Se o nome não deixa claro o que o elemento é, diga que deduziu pelo nome e peça para a pessoa confirmar pelo Inspecionar (botão direito no elemento → Inspecionar → procurar uma classe `custom-css-…` ou um atributo `data-…`).
- **Não existe âncora para o perfil de quem está logado.** "Esconder para o atendente", "só para o admin": não há atributo no `<body>` com o perfil, e os campos separam por público e por empresa, não por perfil. Diga que o alvo não existe; não invente `data-perfil`.
- **Os valores de `data-menu` não estão listados** (o catálogo diz "o identificador do item"). Seções (`data-menu-section`) e submenus (`data-menu-group-box`) têm lista. Para um item, peça o valor pelo Inspecionar.
- **O mesmo atributo muda de vocabulário conforme o elemento.** `data-status` é `pending`/`sent`/`delivered`/`read` no balão, o status do atendimento no cartão, outra lista na tarefa, outra no agendamento. Leia a entrada do `06` inteira.
- **Página é id (`#custom-css-contacts`); quase todo o resto é classe.** O script acusa a troca.
- **Tema escuro:** trocar `--mui-primary` não muda os botões (eles leem `--mui-button-primary*`); o fim do `04` diz o que as variáveis não alcançam. `--app-primary` é a Cor Principal configurada pelo super admin: a variável existe nos dois temas, mas no escuro a plataforma continua pintando com o cinza das `--mui-*` (`04`), então não diga que trocar a Cor Principal muda os dois temas; use-a como valor de origem. O catálogo não diz em que tela ela é configurada; o artigo do revendedor diz: Configurações → Cores, bloco **Cores Principais**, com **Cor Principal**, **Barra de Rolagem** e **Barra Superior** (`revendedor/recursos/configuracoes-cores.md`). É tela de quem administra a instância (ver "Quem tem os campos", em "Em que campo colar").
- **Tema claro: quatro `--mui-*` também valem nele.** O `04` ainda diz "As `--mui-*` existem só no tema escuro"; a frase vem do site e está desatualizada. O histórico (`13-historico.md`, versão 29.923.0, "Tema claro com as variáveis do papel") diz que no tema claro o papel do Material-UI (janelas, menus, popups, cartões), o fundo da página, as seções e os blocos das telas leem `--mui-paper`, `--mui-background`, `--mui-paper-2` e `--mui-paper-3`, e `revendedor/recursos/configuracoes-cores.md` confirma. Na divergência, valem o histórico e o artigo do revendedor. Para o claro, escreva as quatro em `body[data-theme="light"]`, sem `!important`; escritas no `:root` elas não mudam o tema claro (o `:root` muda o escuro). Só essas quatro: o artigo põe `--mui-divider` e `--mui-dashboard-card` na mesma lista de áreas, mas, ao falar do tema claro, ele e o histórico só nomeiam as quatro, e nenhuma fonte diz que o claro lê `--mui-primary*`, `--mui-button-primary*` ou `--mui-secondary*`. Esta correção vem da documentação, não de teste no painel: peça para a pessoa conferir o resultado no tema claro.
- **Logotipo não é por empresa.** Logotipo é da instância: as imagens (tela de login, tela de registro, logotipo do menu de cada tema, favicon e ícones) são enviadas em Configurações → Logotipos / Ícones, só em PNG (`revendedor/recursos/configuracoes-logotipos-icones.md`). Por empresa, o que existe é o **CSS desta empresa**, que troca cores e esconde elementos (`revendedor/recursos/configuracoes-editar-empresa.md`). A um pedido de "logotipo só para esta empresa", diga que não existe e ofereça o que o CSS da empresa alcança; o catálogo não documenta trocar a imagem do logotipo por CSS.
- **Variáveis de ler × de mandar.** `--queue-color`, `--lane-color`, `--appbar-cor`, `--section-header-gradiente` e `--flow-node-cor` servem para **ler** a cor que a plataforma pôs; `--appbar-fundo`, `--section-header-fundo`, `--menu-ordem`, `--ticket-actions-*`, `--ticket-min-height` e as `--quadro-tempo-*` são para **definir**. O `03` diz qual é qual e em que seletor cada uma vale.
- **O catálogo às vezes cita uma classe `.Mui*`** ao descrever onde um atributo fica (o `data-aba` das abas, por exemplo). Continue sem usá-la: selecione pelo próprio atributo, debaixo de uma âncora.
- **Altura do campo de digitação:** `height` não vence o que o Material-UI grava no campo; `max-height` e `min-height` vencem (aviso no fim do `06`).
- **Chat Externo é outra página:** campo próprio, âncoras próprias (`custom-css-chat-*`), e as classes `out`/`in` de lá são invertidas (use `data-autor`). A referência não documenta campo de JS nem tema escuro para ela.
- **JS:** o código vira o corpo de um `try`, então `return` solto no nível de cima é erro de sintaxe, e código com erro de sintaxe não é injetado. Erro dentro de ouvinte de evento ou `setTimeout` não cai nesse `catch`. Envolva o script numa função `(function () { … })();`.
- **"JS geral" só está definido em parte.** O `02` diz que a chave "Usar a customização geral (CSS e JS)", no cadastro da empresa, desliga para aquela empresa "o CSS pré-login, o CSS pós-login e o JS geral". O artigo `revendedor/recursos/configuracoes-editar-empresa.md` descreve a opção: ligada, a empresa usa o CSS e o JS do card **Cores**; desligada, nas palavras da tela, "esta empresa fica com o layout padrão: sem o CSS geral do painel e sem o JS geral. Não afeta as telas de login e cadastro, que são gerais."; ao entrar, a aba recarrega uma vez para o código geral sair. O **CSS desta empresa** e o **JS desta empresa** continuam valendo. O que continua sem resposta: nenhum artigo diz se "JS geral" inclui o JS pré-login ou só o pós-login. Não adivinhe: diga que esse ponto não está documentado e que o comando de console do `02` mostra quais campos de fato carregaram.
- **O CSS pré-login chega a todas as telas**, inclusive o painel depois do login (`01`), e não só às telas de entrada. Regra sem escopo ali vaza para o painel.
- **`14-rotas.md` não liga rota a página:** o catálogo não publica qual `#custom-css-<página>` pertence a qual URL. Em JS, prefira testar se o id da página existe a comparar `location.pathname`.
- **`!important`:** às vezes é preciso para vencer o Material-UI; nas variáveis do `03` e do `04`, não.

## Quando o alvo não existe

Se o elemento não tem `custom-css-*`, `data-*` nem classe sem prefixo no catálogo, o alvo não existe. Diga isso com todas as letras, mostre o que procurou e ofereça o que existe por perto (a âncora do contêiner, uma variável, a regra para a página inteira). Não use `.Mui*`, `.jss123`, seletor por posição (`div > div:nth-child(3)`) nem por texto: funcionam hoje e quebram na próxima atualização, e a pessoa não vai saber por quê. O `01` orienta a pedir a âncora nova à plataforma.

## "Meu CSS parou de funcionar"

1. Peça o código que está no campo e em qual campo ele está.
2. Rode `python3 scripts/conferir_seletores.py --historico arquivo.css`. Nome acusado como inexistente ou proibido é a causa mais provável: classe do Material-UI que mudou, ou âncora que nunca existiu. O `--historico` lista em que versões cada nome válido foi citado no `13`.
3. Para cada nome suspeito, `grep -n 'nome' references/docs/13-historico.md`. As versões vão da mais nova para a mais antiga. Leia a entrada: "ACRESCENTADOS" e "Nada foi trocado nem renomeado" são acréscimos e não quebram nada; "⚠️", "passa a", "não traz mais", "saiu do `style`", "trocado" e "renomeado" marcam mudança que pode ter derrubado a regra, e a entrada costuma dizer o que usar no lugar.
4. Se os nomes estão certos, confira o resto, tudo do `02`: o campo certo (pré × pós-login); a chave "Usar a customização geral (CSS e JS)" desligada no cadastro da empresa (o `<style>` aparece com `media="not all"`; quais campos de JS ela desliga não está documentado, veja Armadilhas); empate perdido para o CSS da empresa, que carrega por último; falta de `!important`; JS com erro de sintaxe (não é injetado) ou que procurou o elemento antes de ele existir. O `02` traz o comando de console que mostra quais campos carregaram e os prefixos de erro de cada campo de JS (`[custom-js]`, `[custom-js-poslogin]`, `[custom-js-empresa]`).
5. Diga a versão desta referência (WS-30.141.0). O histórico copiado (`13`) para na 30.53.0: o que entrou daí até a 30.141.0 está no catálogo, mas não no histórico. Se o painel da pessoa é mais novo, o histórico daqui não cobre a mudança: o catálogo vivo fica em <https://app.chatmasterveloz.com/css-docs>. Em instância própria (a de um revendedor), o catálogo vivo é o `/css-docs` do endereço dela: `https://seu-frontend/css-docs`, trocando `seu-frontend` pelo endereço da instância (`revendedor/recursos/ancoras-css.md`). A página é atualizada a cada versão da plataforma, então a de lá pode estar em outra versão que a desta referência.

## A resposta para a pessoa

Quem pede geralmente não é técnico. Entregue nesta ordem, sem jargão:

1. **O que o código faz**, em uma ou duas frases, e o que ele **não** faz (o que não tinha âncora, o que é só visual e não permissão, o que você recusou e por quê).
2. **Onde colar**: o nome do campo, o caminho do menu e o motivo de ser esse campo.
3. **O código**, num bloco só, comentado em português, entre `CMV-INICIO` e `CMV-FIM`.
4. **Passo a passo para aplicar**, numerado: abrir o caminho, copiar antes o que já está no campo (cópia de segurança), colar no fim sem apagar o resto, salvar, conferir o resultado (no painel, nos dois temas). Esses campos ficam com quem administra a instância: se quem pede é o administrador de uma empresa cliente, ou se você não sabe quem é, diga que, sem acesso a essa tela, o bloco deve ser enviado a quem fornece a plataforma, que é quem cola.
5. **Como desfazer**: apagar o bloco entre os marcadores e salvar; se for JS, recarregar a página em quem estava com o painel aberto.
6. **O que não pôde ser confirmado**: cada aviso do script (valor não conferido, nome só no histórico), cada significado deduzido só pelo nome da âncora e cada ponto que a referência não documenta, com o que a pessoa deve olhar no Inspecionar.
7. **Fonte**: as partes do catálogo usadas, pelo título e não pelo nome do arquivo (por exemplo "Tema escuro e Atributos data, catálogo WS-30.141.0") e o link <https://app.chatmasterveloz.com/css-docs> (se o painel da pessoa fica em outro endereço, o `/css-docs` desse endereço). O `02` e o `14` não vêm do catálogo: foram lidos do código do painel, e isso está dito no topo de cada um. `references/receitas.md` e os demais arquivos desta skill (este `SKILL.md`, o script) não são fonte nem assunto da resposta: não escreva "a receita 3", "a receita que a skill usa" nem "o script de conferência". O que se diz é "os nomes foram conferidos contra o catálogo". As partes que não vêm do catálogo (o `02` e o `14`) são citadas como "lido do código do painel", sem número de versão do catálogo.

Diga que os nomes foram conferidos contra o catálogo e que o código **não** foi testado no painel dela: peça para avisar se algo não mudou.

**Pedido que usa mais de um campo** (por exemplo, aviso numa tela do painel mais visual da tela de login): os itens 2 e 3 se repetem, um par por campo, e o resto é comum.

- Um bloco de código por campo, cada um com o seu título ("Bloco 1: CSS pré-login", "Bloco 2: JS pós-login"), o seu "onde colar" com o caminho e o motivo, e os seus marcadores `CMV-INICIO`/`CMV-FIM`. Nunca junte num bloco só código de campos diferentes: CSS e JS não se misturam, e o que é do painel não pode ir para o campo público.
- Um único passo a passo de aplicar, na ordem dos blocos ("repita os passos 1 a 4 para cada bloco"), e um único como desfazer, dizendo qual bloco apagar de qual campo.
- Confira cada bloco no script (pode passar os arquivos juntos).

### Exemplo

Pedido: "Queria esconder o menu de Campanhas pros atendentes e deixar a letra das mensagens maior."

Entrega (resumo do raciocínio):

- Campanhas é um submenu: `06` documenta `data-menu-group-box="campaigns"` em `.custom-css-menu-grupo-caixa`. A letra das mensagens é `.custom-css-msg-bubble` (área `MessagesList` do `09`). As duas regras são CSS do painel, então vão no **CSS pós-login** (ou no **CSS desta empresa**, se for só para uma).
- "Só para os atendentes" não tem âncora: a resposta diz que o menu some para todos que recebem aquele campo, que esconder não bloqueia o acesso pelo endereço, e que permissão por perfil é configuração do painel (`cmv-ajuda`).
- Código entregue, depois de passar no script:

```css
/* CMV-INICIO esconder Campanhas e aumentar a letra das mensagens */
.custom-css-menu-grupo-caixa[data-menu-group-box="campaigns"] { display: none !important; }
.custom-css-msg-bubble { font-size: 16px !important; line-height: 1.5 !important; }
/* CMV-FIM */
```

- Em seguida, o passo a passo (Configurações → Cores → CSS pós-login → colar no fim → salvar), o como desfazer e a fonte. Como quem pediu não disse se administra a instância, o passo a passo avisa que esse campo fica com quem fornece a plataforma: sem acesso à tela, é a ele que o bloco deve ser enviado.
