<!-- gerado por _gerar.py · fonte: https://app.chatmasterveloz.com/catalogo-css/pt.json · versão WS-29.930.0 -->

# Histórico

O que MUDOU em elemento que já tinha gancho, e se foi acréscimo ou troca. De fora não há como saber se um atributo novo substituiu algo — e a diferença é um realce que some sem ninguém entender por quê.

### 29.930.0

- Quadro de Atendimentos: o tempo do card (`.custom-css-quadro-tempo`) não traz mais a cor no `style` — ela vem do CSS, pelo `data-elapsed-status`, e lê `--quadro-tempo-atrasado`, `--quadro-tempo-atencao` e `--quadro-tempo-em-dia`. No tema escuro, o atrasado passou a um vermelho legível sobre o card (`#ff7a7a`).

### 29.929.0

- Tema escuro: os componentes na cor secundária leem `--mui-secondary` (com `--mui-secondary-dark` e `--mui-secondary-contrast`), como os da cor principal leem `--mui-primary` — o botão "Enviar Template" da faixa da janela de 24h (`.custom-css-conversation-bar-btn-template`), os botões, chips, selos, interruptores, caixas de marcar, rádios, abas, barras de progresso, ícones e textos na cor secundária. Sem customização, o `#eee` de sempre.

### 29.928.0

- Menu lateral: cada seção ganhou um contêiner com nome — `.custom-css-menu-secao` com `data-menu-section` (`principal`, `atendimentos`, `ferramentas`, `administracao`, `automacao`, `sistema`…) —, com o título (`.custom-css-menu-secao-titulo`, o mesmo `data-menu-section`), o divisor e os itens dentro; dá para destacar uma seção inteira. Cada submenu é uma caixa só (`.custom-css-menu-grupo-caixa` com `data-menu-group-box`; a lista de dentro é `.custom-css-menu-grupo-itens`), e a caixa do menu é `.custom-css-menu-lista`. Propriedade nova: `--menu-ordem` — a ordem do menu pelos nomes do `data-menu`, dos submenus e das seções.

### 29.927.0

- Recolhimento no celular: os contêineres que antes só se achavam pelos filhos ou pela posição ganharam nome — a caixa de fora da faixa Ticket / Atendimentos (`.custom-css-mobile-tabs-caixa`), a caixa da foto e a do nome no cabeçalho do atendimento (`.custom-css-ticket-info-avatar` · `.custom-css-ticket-info-nome`) e o papel que guarda as etiquetas (`.custom-css-ticket-tags-papel`, na conversa e no modal do ticket).

### 29.926.0

- Painel de Pedidos: o aceite automático dos pedidos das mesas é uma chave à parte — "Mandar direto para a produção os pedidos das mesas" — ao lado da dos pedidos de fora. As duas com `.custom-css-painel-de-pedidos-aceite` e `data-aceite` (`fora` · `mesa`); a das mesas só aparece para quem tem mesas no salão.

### 29.925.0

- Seletores: o rótulo sobe quando o valor chega depois de a janela abrir (o setor carregado, o fluxo do setor…). Antes ele ficava por cima do valor, sem `.MuiInputLabel-shrink`, e o recorte da borda fechado — o Material-UI decidia uma vez só, ao abrir, se o campo era controlado. Vale para todo seletor das telas e janelas (o `Select` e o `TextField` com `select`).
- Âncoras em todo seletor: `.custom-css-select` na raiz, `.custom-css-select-label` no rótulo, `.custom-css-select-input` na caixa e `.custom-css-select-border` na borda (o contornado), com `data-preenchido="true"`/`"false"` na raiz, no rótulo e na caixa. Ex.: `.custom-css-select[data-preenchido="false"] .custom-css-select-border { border-style: dashed; }`. Não é mais preciso ler o input oculto nem as classes internas do Material-UI.

### 29.924.0

- Tema escuro: os componentes na cor principal leem `--mui-primary`, como o "escolhido" e os cabeçalhos já liam — o chip e o selo de número (fundo `--mui-primary`, texto `--mui-primary-contrast`), o chip contornado, o avatar do chip (`--mui-primary-dark`), o interruptor ligado (bolinha, trilho e o halo do mouse), a aba escolhida e o sublinhado, a barra e o círculo de progresso, a caixa de marcar e o rádio marcados. Basta `:root { --mui-primary: #2DDD7F; --mui-primary-contrast: #fff; }`, sem `.Mui*-colorPrimary`, `.MuiSwitch-*` ou `.MuiTabs-indicator`. Sem customização, as cores de sempre; os tons sob o mouse saem da variável por `color-mix()` (o navegador sem `color-mix` fica com o tom de antes).

### 29.923.0

- Tema claro com as variáveis do papel, como o escuro: o papel do Material-UI (janelas, menus, popups, cartões), o fundo da página, as seções e os blocos das telas leem `--mui-paper`, `--mui-background`, `--mui-paper-2` e `--mui-paper-3`, cada um com a cor de antes como reserva. Para trocar só no claro: `body[data-theme="light"] { --mui-paper: #f7f7f2; }` (sem `!important` e sem `.MuiPaper-root`). O `:root` de quem customizou o escuro não vaza para o claro (no claro o `<body>` zera as quatro).

### 29.920.0

- Reserva de mesa: nas Comandas, a aba Reservas `.custom-css-reservas-da-mesa` (com o `data-dia` do dia aberto), a navegação dos dias `.custom-css-reservas-da-mesa-dia`, cada reserva `.custom-css-reservas-da-mesa-reserva` (com o `data-reserva-id` e o `data-situacao`: `pendente` · `confirmada` · `cancelada` · `compareceu` · `nao-compareceu`), a situação `.custom-css-reservas-da-mesa-situacao`, os botões `.custom-css-reservas-da-mesa-acoes`, a janela da reserva `.custom-css-reservas-da-mesa-janela` e a do cancelamento `.custom-css-reservas-da-mesa-cancelar`; no cartão da mesa, o aviso "Reservada às…" `.custom-css-comandas-reservada`; no Cardápio Digital, a regra da reserva pela loja `.custom-css-cardapio-reservas`.

### 29.919.0

- Comissão do garçom: nas Opções do PDV, a regra `.custom-css-opcoes-comissao-do-garcom` (a parte da taxa de serviço e o % sobre o consumo); no Relatório do PDV, a seção `.custom-css-relatorio-pdv-comissao`, a regra aplicada `.custom-css-relatorio-pdv-comissao-regra` e cada garçom `.custom-css-relatorio-pdv-comissao-linha` (com o `data-garcom-id`); no painel do garçom, a comissão de hoje e do mês `.custom-css-mesas-do-garcom-comissao`.

### 29.918.0

- Comandas: as operações de salão na janela da conta, no bloco `.custom-css-salao-da-mesa` (com o `data-comanda-id`): cada rodada `.custom-css-salao-da-mesa-rodada` (com o `data-pedido-id`), cada item `.custom-css-salao-da-mesa-item` (com o `data-item-id`) e o botão de tirar o item `.custom-css-salao-da-mesa-tirar`, mover a rodada para outra conta `.custom-css-salao-da-mesa-mover`, os itens tirados `.custom-css-salao-da-mesa-tirados` (cada um `.custom-css-salao-da-mesa-tirado`), as ações da conta `.custom-css-salao-da-mesa-acoes` (transferir a mesa e juntar com outra), a janela de tirar o item `.custom-css-salao-da-mesa-tirar-janela` e a de escolher a mesa ou a conta `.custom-css-salao-da-mesa-acao-janela`.

### 29.917.0

- Comandas: a busca pelo número, mesa ou cliente `.custom-css-comandas-busca`, o cliente e as pessoas no cartão `.custom-css-comandas-cliente`, as pessoas e o nome do cliente ao abrir a mesa `.custom-css-comandas-abrir-inicio` e, na conta, o consumo `.custom-css-comandas-consumo`, a taxa de serviço `.custom-css-comandas-taxa` e o desconto `.custom-css-comandas-desconto`. O bloco da conta da mesa `.custom-css-conta-da-mesa` (com o `data-comanda-id`): as pessoas `.custom-css-conta-da-mesa-pessoas`, o cliente `.custom-css-conta-da-mesa-cliente`, o cliente escolhido `.custom-css-conta-da-mesa-cliente-escolhido`, cada cliente sugerido `.custom-css-conta-da-mesa-cliente-sugerido` (com o `data-contato-id`), a taxa de serviço `.custom-css-conta-da-mesa-taxa`, o desconto na conta `.custom-css-conta-da-mesa-desconto`, dividir `.custom-css-conta-da-mesa-dividir`, o valor por pessoa `.custom-css-conta-da-mesa-por-pessoa` e imprimir a conta `.custom-css-conta-da-mesa-imprimir`. Nas opções do PDV, a taxa de serviço da mesa `.custom-css-opcoes-taxa-de-servico`.

### 29.916.0

- Cadastro da empresa (super), aba Integrações: a chave da OpenAI `.custom-css-empresa-chave-de-ia` (com o `data-modo`), a escolha entre a chave própria e a da plataforma `.custom-css-empresa-chave-de-ia-modo`, o campo da chave da plataforma `.custom-css-empresa-chave-de-ia-chave`, o Salvar `.custom-css-empresa-chave-de-ia-salvar`, o Tirar `.custom-css-empresa-chave-de-ia-tirar` e o aviso de antes de criar a empresa `.custom-css-empresa-chave-de-ia-depois`. Nas Integrações da empresa, o aviso de que a chave é da plataforma `.custom-css-integracoes-chave-subsidiada`.

### 29.914.0

- E-mails: a busca por assunto ou remetente `.custom-css-emails-busca`, em cima da lista. A imagem de cada conta `.custom-css-email-conta-imagem` (na caixa de entrada e na lista de contas). No cadastro da conta, o seletor da imagem `.custom-css-email-account-imagem`, com o Escolher `.custom-css-email-account-imagem-escolher` e o Tirar `.custom-css-email-account-imagem-tirar`.

### 29.913.0

- Projetos: o botão das situações `.custom-css-projetos-situacoes` abre a janela `.custom-css-modal-situacoes-do-projeto`, com cada situação em `.custom-css-situacao-do-projeto` (a cor `.custom-css-situacao-do-projeto-cor`, o nome `.custom-css-situacao-do-projeto-nome`, o subir `.custom-css-situacao-do-projeto-subir`, o descer `.custom-css-situacao-do-projeto-descer` e o tirar `.custom-css-situacao-do-projeto-tirar`), a nova `.custom-css-situacao-do-projeto-nova` e o salvar `.custom-css-situacoes-do-projeto-salvar`. No cartão do projeto, a foto do responsável `.custom-css-projetos-cartao-responsavel` e a situação `.custom-css-projetos-cartao-situacao`. Na página do projeto, a situação `.custom-css-projeto-situacao`, o responsável com a foto `.custom-css-projeto-responsavel`, o filtro das tarefas por responsável `.custom-css-projeto-filtro-responsavel`, a foto do responsável da tarefa `.custom-css-projeto-tarefa-responsavel` e a engrenagem `.custom-css-projeto-engrenagem` com o menu `.custom-css-projeto-engrenagem-menu` (Nova etapa `.custom-css-projeto-acao-nova-etapa`, Salvar como modelo `.custom-css-projeto-acao-modelo`, Editar `.custom-css-projeto-acao-editar` e Apagar `.custom-css-projeto-acao-apagar`).

### 29.912.0

- Ranking: na tabela das equipes e das unidades, a imagem de cada uma em `.custom-css-crm-ranking-grupo-imagem` (no pódio, no lugar da foto). Na janela das unidades e equipes de Minha Evolução, o seletor da imagem `.custom-css-minha-evolucao-imagem` (`.custom-css-minha-evolucao-imagem-unidade` ou `.custom-css-minha-evolucao-imagem-equipe`), com o Escolher `.custom-css-minha-evolucao-imagem-escolher` e o Tirar `.custom-css-minha-evolucao-imagem-tirar`. No cadastro do usuário, a permissão de ver o Ranking `.custom-css-usuario-ver-ranking`.

### 29.911.0

- Oportunidades: os botões de visão `.custom-css-view-toggle` (`data-view="card"` ou `"list"`) alternam entre os cartões e a tabela `.custom-css-oportunidades-tabela` (cada linha `.custom-css-oportunidades-linha`, com `data-situacao`; a situação no chip `.custom-css-oportunidades-situacao`; os botões `.custom-css-oportunidades-linha-editar` e `.custom-css-oportunidades-linha-excluir`). No topo, a barra `.custom-css-oportunidades-filtros`, com cada filtro em `.custom-css-oportunidades-filtro` mais o próprio (`.custom-css-oportunidades-filtro-tipoDeData`, `-dataInicial`, `-dataFinal`, `-userId`, `-productId`, `-contactId`, `-motivoPerdaId`, `-origemVendaId`, `-situacao`) e o Limpar `.custom-css-oportunidades-filtros-limpar`.

### 29.910.0

- Oportunidade e Tarefa: no topo da janela da oportunidade, o ícone da posição dos comentários e o X ficam juntos à direita, no grupo `.custom-css-oportunidade-acoes-do-topo`; no rodapé da janela da tarefa, o Cancelar saiu (o X do topo fecha) e o Finalizar `.custom-css-tarefa-btn-finalizar` fica à direita, ao lado do Atualizar.

### 29.909.0

- Atendimento: na barra, o botão da consulta de preço e estoque (`data-action="pdv-consulta"`, ao lado do pedido do PDV) abre a janela `.custom-css-modal-consulta-de-produtos`, com a busca `.custom-css-consulta-de-produtos-busca`, a tabela `.custom-css-consulta-de-produtos-tabela` (cada linha `.custom-css-consulta-de-produtos-linha`, o preço `.custom-css-consulta-de-produtos-preco`, o estoque `.custom-css-consulta-de-produtos-estoque` e os alertas `.custom-css-consulta-de-produtos-esgotado` e `.custom-css-consulta-de-produtos-baixo`), o Copiar `.custom-css-consulta-de-produtos-copiar` e o aviso de nada encontrado `.custom-css-consulta-de-produtos-nenhum`.

### 29.908.0

- Garçom: a tela do login do salão `.custom-css-page-mesas-do-garcom` (o topo `.custom-css-mesas-do-garcom-topo` e o Sair `.custom-css-mesas-do-garcom-sair`), com as Mesas e Comandas no modo do garçom — sem o pagamento e sem o Fechar mesa, que ficam com o caixa.

### 29.906.0

- CRM: na janela da oportunidade, a confirmação de descartar o que mudou `.custom-css-modal-confirmation-oportunidade-descartar` (ao fechar pelo X ou clicando fora); no Copilot da raia, o campo Tempo `.custom-css-copilot-tempo` (vermelho com 0 ou vazio).

### 29.905.0

- Conexões e Painel de Pedidos: no card do RCS, o Copiar URL do webhook `.custom-css-conexao-copiar-url-rcs` e, enquanto o provedor não confirmou a credencial, o estado `.custom-css-conexao-rcs-credencial-nao-conferida`; no Modo TV do Painel de Pedidos, o Sair do modo TV dentro da tela cheia `.custom-css-painel-sair-do-modo-tv`.

### 29.902.0

- Moeda da empresa: em Opções, a escolha da moeda `.custom-css-opcao-moeda` (o formato dos valores no PDV, no CRM, no Cardápio e na Loja); no pagamento do pedido, o aviso `.custom-css-pedido-sem-pagamento-online`, quando a moeda não é o real e o pagamento online fica indisponível.

### 29.901.0

- Mesas e Comandas (a página que era Comandas): as abas `.custom-css-comandas-abas` (Mesas, Comandas e Histórico, em `data-aba`), em cada aba as seções `.custom-css-comandas-secao` (`data-secao` `abertas` e `fechadas`), a conta aberta `.custom-css-comandas-aberta` (`data-comanda-id`), a mesa ou comanda fechada `.custom-css-comandas-fechada` (`data-mesa-id`), o aviso sem cadastro `.custom-css-comandas-sem-cadastro`, a janela de abrir a mesa `.custom-css-comandas-abrir`, o botão Configurar `.custom-css-comandas-configurar-botao` e a janela de configuração `.custom-css-comandas-configurar`, com o criar de uma vez `.custom-css-comandas-lote` (a frase em `data-exemplo-do-lote`).

### 29.897.0

- Ranking do CRM: o filtro "Ranking por" (`.custom-css-crm-ranking-visao`) troca o ranking dos vendedores pelo ranking entre equipes, unidades ou funis — a caixa `.custom-css-crm-ranking-grupos` (com `data-visao`), o pódio de sempre e cada linha `.custom-css-crm-ranking-grupo` (com `data-grupo-id` e `data-colocacao`), o nome em `.custom-css-crm-ranking-grupo-nome`; sem equipes cadastradas, o aviso `.custom-css-crm-ranking-grupos-vazio`.

### 29.896.0

- Editar Oportunidade (`.custom-css-modal-oportunidades`): o "Cancelar" do rodapé saiu, e o X no topo da janela (`.custom-css-oportunidade-btn-fechar`) é que fecha; o botão de gravar diz "Salvar" na oportunidade que já existe.
- Chat Interno: editar a mensagem carrega o texto no próprio campo de mensagem, como no atendimento. Acima do campo aparece a barra `.custom-css-chat-interno-editando`, com o texto de antes (`.custom-css-chat-interno-editando-texto`), a ajuda (`.custom-css-chat-interno-editando-ajuda`) e o X `[data-action="cancelar-edicao"]`. ⚠️ A janela `.custom-css-modal-editar-mensagem-chat-interno` e o botão `salvar-edicao` saíram: o Enter e o `send` salvam, o Esc desiste.

### 29.895.0

- Pedido do PDV (entrega): `.custom-css-pedido-pdv-enderecos-salvos` traz a lista `.custom-css-pedido-pdv-endereco-salvo` com os endereços salvos do cliente e o botão `.custom-css-pedido-pdv-gerenciar-enderecos`; o endereço novo tem a caixa `.custom-css-pedido-pdv-salvar-endereco`.
- Janela dos endereços do cliente (`.custom-css-modal-enderecos-do-cliente`): a lista `.custom-css-enderecos-do-cliente-lista` com cada `.custom-css-endereco-do-cliente` (ou o aviso `.custom-css-enderecos-do-cliente-vazio`), o formulário `.custom-css-endereco-do-cliente-form` e os botões `.custom-css-endereco-do-cliente-novo` e `.custom-css-endereco-do-cliente-salvar`.
- Pedidos (gestão): os botões `.custom-css-planilha-de-enderecos-modelo` e `.custom-css-planilha-de-enderecos-importar`; o resultado da importação abre `.custom-css-modal-resultado-enderecos`, com `.custom-css-resultado-enderecos-resumo`, `.custom-css-resultado-enderecos-erros` ou `.custom-css-resultado-enderecos-faltando`.

### 29.894.0

- Conversa (`.custom-css-msg-bubble` do cliente): ao lado da hora, o aparelho de onde o cliente mandou a mensagem — `.custom-css-plataforma-da-mensagem`, com `.custom-css-plataforma-ios`, `.custom-css-plataforma-android` ou `.custom-css-plataforma-web`.

### 29.893.0

- Resumo do caixa: a seção `.custom-css-caixa-recebido-online` lista, só para conferência, os pagamentos online (Asaas, Mercado Pago, PagSeguro, Pix) recebidos no turno — eles não entram no esperado da gaveta.

### 29.891.0

- Janela do RCS (`.custom-css-modal-rcs`): o botão `.custom-css-rcs-copiar-webhook` copia a URL do webhook da conexão salva e, com o provedor Gupshup, aparece o quadro de instruções `.custom-css-rcs-instrucoes`.

### 29.885.0

- Conexões: o canal WhatsApp Gupshup — `whatsapp_gupshup` no `data-channel` (o cartão da conexão e o ícone `.ticket-channel-icon`, verde-petróleo), o chip de filtro `data-channel-filter="gupshup"`, o item do menu "Ações" com `data-menu-action="adicionar-gupshup"` e `data-conexao="gupshup"` (só com o canal no plano) e, no cartão, o botão `data-connection-action="copiar-url-gupshup"`. O cadastro é a janela `.custom-css-modal-gupshup`, com o quadro de instruções `.custom-css-gupshup-instrucoes` e o da URL `.custom-css-gupshup-url`.

### 29.884.0

- Comentários em aba ou na lateral direita, na tarefa, na oportunidade e no projeto: o botão `.custom-css-comentarios-modo` (com `data-modo` e, por lugar, `.custom-css-tarefa-comentarios-modo`, `.custom-css-oportunidade-comentarios-modo` e `.custom-css-projeto-comentarios-modo`) troca entre os dois. Na lateral, a tarefa ganha `.custom-css-tarefa-lado-a-lado` e o bloco de comentários `.custom-css-tarefa-comentarios` passa a ter também `.custom-css-tarefa-comentarios-lateral`; a oportunidade ganha `.custom-css-oportunidade-lado-a-lado` e a coluna `.custom-css-oportunidade-comentarios-lateral`; no projeto, `.custom-css-projeto-comentarios` passa a ter também `.custom-css-projeto-comentarios-lateral` e o painel ganha `.custom-css-projeto-sobre-lado-a-lado`. Em aba, o projeto mostra as abas `.custom-css-projeto-sobre-abas` (Descrição e anexos · Comentários).

### 29.882.0

- Painel do contato (o painel lateral do atendimento): os cartões Oportunidades e Projetos ganharam âncoras próprias — antes só tinham as classes do MUI, que mudam a cada build. Oportunidades: o cartão `.custom-css-contato-oportunidades`, com o título (`-titulo`) e o resumo das abertas e ganhas (`-resumo`); cada oportunidade `.custom-css-contato-oportunidade` (com `data-situacao`: `aberta`, `ganha` ou `perdida`), com o nome e o valor (`.custom-css-contato-oportunidade-nome`), o funil e a etapa (`-funil`), o selo da situação (`-situacao`) e o botão de criar projeto (`-criar-projeto`). Projetos: o cartão `.custom-css-contato-projetos`, com o topo (`-topo`), o título (`-titulo`), o botão Novo projeto (`-novo`) e o aviso de nenhum projeto (`-vazio`); cada projeto `.custom-css-contato-projeto` (com `data-situacao`: `planejamento`, `andamento`, `pausado` ou `concluido`), com o nome (`.custom-css-contato-projeto-nome`), o progresso (`-progresso`) e o selo da situação (`-situacao`). A classe de layout que o painel já passava continua no cartão.

### 29.876.0

- Chamadas (a janela da chamada e a página do convidado): a tela compartilhada ganhou zoom. O quadro da tela (`.custom-css-chamada-participante-tela`) agora tem a área que aproxima (`.custom-css-chamada-tela-area`, com `data-zoom` em porcentagem e `.custom-css-chamada-tela-aproximada` quando passa de 100%), a imagem que se move (`.custom-css-chamada-tela-conteudo`) e a barra do zoom (`.custom-css-chamada-tela-zoom`), com afastar (`-zoom-afastar`), a porcentagem (`-zoom-valor`), aproximar (`-zoom-aproximar`), tamanho real (`-zoom-real`), ajustar (`-zoom-ajustar`) e o botão "Mostrar só a tela" (`.custom-css-chamada-so-a-tela`, com `-ligado`). No "só a tela", a área dos vídeos ganha `.custom-css-chamada-grade-so-a-tela` e a faixa das câmeras (`.custom-css-chamada-faixa`) sai da página.

### 29.693.0

- Editor de fluxo, com o PDV: o bloco PDV (o menu de produtos com quantidade) — no desenho, `.custom-css-flow-node-pdv`, com um `.custom-css-flow-node-item` por produto e as saídas "Pedido confirmado" e "Desistiu" (`data-tipo="saida"`); a janela do bloco é `.custom-css-modal-flow-pdv`.

### 29.692.0

- Painel do contato, com o PDV: o cartão `.contact-pedidos-card`, logo abaixo do cartão do contato, com os últimos pedidos do cliente, o total gasto e o botão "Repetir pedido" em cada um.

### 29.687.0

- Chamadas do chat interno: a chamada de voz (aberta pelo telefone, pelo "Entrar" ou pelo "Atender") marca a janela com `.custom-css-chamada-voz` e, no lugar dos quadros de vídeo, mostra a lista de quem está na sala (`.custom-css-chamada-voz-lista`), com cada pessoa em `.custom-css-chamada-voz-participante` (e `-falando` em quem está falando). Novos também: o aviso de que há vídeo na chamada (`.custom-css-chamada-ha-video`), o botão "Ver vídeo" (`.custom-css-chamada-ver-video`) e, na videochamada do chat interno, o "Voltar para a chamada de voz" (`.custom-css-chamada-voltar-para-voz`).

### 29.683.0

- Chamadas (a janela da chamada e a página do convidado): com alguém compartilhando a tela, a área dos vídeos ganha `.custom-css-chamada-grade-palco`, com o palco (`.custom-css-chamada-palco`, onde fica a tela) e a faixa das câmeras (`.custom-css-chamada-faixa`). A tela e a câmera de quem compartilha são quadros separados — só o da tela tem `-participante-tela`. Novos também: o botão e o estado de tela cheia (`.custom-css-chamada-tela-cheia-botao`, `.custom-css-chamada-tela-cheia`), os cantos que mudam o tamanho (`.custom-css-chamada-redimensionar`, com `-esquerdo` ou `-direito`) e a janela separada — o botão (`.custom-css-chamada-soltar`), a chamada lá (`.custom-css-chamada-solta`), o botão de voltar (`.custom-css-chamada-recolher`) e o aviso que fica no painel (`.custom-css-chamada-separada`). Na janela separada, o CSS da página vale do mesmo jeito.

### 29.682.0

- Chamadas (a janela da chamada e a página do convidado): o botão do fundo da câmera (`.custom-css-chamada-fundo`, que também tem `.custom-css-chamada-botao`), o menu dele (`.custom-css-page-menu.custom-css-menu-chamada-fundo`) e cada opção do menu — sem fundo, desfoque, as imagens da empresa e a imagem própria (`.custom-css-chamada-fundo-opcao`).

### 29.681.0

- Chamadas (a janela da chamada e a página do convidado, `#custom-css-sala-convidado`): âncoras novas — `.custom-css-chamada` (com `-cliente` ou `-equipe` e `-mini` ou `-grande`), `-topo`, `-titulo`, `-fase`, `-gravando`, `-grade` (a área dos vídeos, que recebe o plano de fundo: `.custom-css-chamada-grade { background: url(https://exemplo.com/fundo.jpg) center / cover; }`), `-participante` (com `-falando`, `-local`, `-tela` e `-sem-microfone`), `-participante-video`, `-participante-avatar`, `-participante-nome`, `-controles`, `-botao`, `-sair`, `-convite` e `-ativar-som`; e as janelas `.custom-css-modal-chamada-toque` e `.custom-css-modal-chamada-convidados`. A página do convidado, que abre sem login, passa a receber o CSS da empresa.

### 29.614.0

- Conversa (`.message-avatar`): a mensagem escrita pelo assistente de IA ganha o avatar `data-avatar="ia"` (o selo IA, no lugar do círculo cinza) e o nome do assistente no rodapé, como o do operador.

### 29.607.0

- Barra de ações do atendimento (`.custom-css-ticket-actions`) e a do celular: o "Marcar como não lido" (`data-action="mark-as-unread"`, com `aria-label` traduzido) fica no lugar do "Marcar como lido" quando não há mensagem não lida — fora do atendimento encerrado. ⚠️ Com isso, a primeira posição da barra está sempre ocupada por um dos dois (no encerrado sem não lidas, por nenhum).

### 29.585.0

- Tela nova: o cadastro de rodízios (`#custom-css-rodizios`), com a janela de criar e editar (`.custom-css-modal-rodizio`) e a confirmação de excluir (`.custom-css-modal-confirmation-rodizio-excluir`). No relatório do rodízio, o grupo de um rodízio cadastrado tem `data-flow-id` e `data-node-id` vazios.

### 29.578.0

- Lista de atendimentos, com a configuração "Aguardando com dono: só ele vê" ligada: `data-aba` ganhou o valor `pending-meus`, a aba "Aguardando (MEUS)" (os aguardando atribuídos a mim), com o mesmo contador em `data-carregados` e `data-total` no `.MuiBadge-root`.

### 29.572.0

- Quadro de atendimentos, visão por tags (o alternador "Ver o quadro por: Colunas | Tags" na barra): `data-coluna-tipo` ganhou os valores `TAG` (cada tag marcada como Kanban vira uma coluna, com a cor da tag em `--lane-color`) e `SEM_TAG` (a coluna de quem não tem nenhuma delas). As classes da coluna e do card são as mesmas da visão de colunas.

### 29.567.0

- Tempo real: quando a tela passa mais de um minuto sem atualização em tempo real, aparece a faixa `.custom-css-tempo-real-faixa` ("Sem atualização em tempo real — reconectando…") no topo do conteúdo, com o botão `.custom-css-tempo-real-recarregar`. Ela some sozinha quando a conexão volta.

### 29.564.0

- Setor de IA fora da tela de tickets: o cartão da tela de Setores ganha `data-queue-chatbot` e a etiqueta "Chatbot" dele, o nome `.custom-css-queue-card-chatbot`; as opções do "Filtrar por Setores" e das listas de escolher setor (transferir e novo atendimento) ganham `data-queue-id` e `data-queue-chatbot`. A aba AGUARDANDO ganha o `data-total-chatbot`, e a lista aceita `queueChatbot=true|false`. Na mensagem interativa do atendimento: `.custom-css-msg-interativa-cabecalho`, `.custom-css-msg-interativa-rodape` e `.custom-css-msg-interativa-botoes` nas partes, `.custom-css-msg-botao` com `data-tipo` em cada botão e `.custom-css-msg-lista-item` em cada item da lista.

### 29.527.0

- Chat Externo, na página do canal (o link com `h=`): com a conversa bloqueada pelo atendimento (`.custom-css-chat-app` com `data-canal-estado="bloqueada"`), o botão "Começar nova conversa" (`.custom-css-chat-canal-nova-conversa`) some do topo, junto com o campo, que fica travado — a conversa bloqueada não oferece começar outra. Já era assim desde a 29.525.0 e faltava aqui: uma regra de `display` com `!important` no botão o traz de volta nesse estado.

### 29.525.0

- Chat Externo: a página de entrada do canal — o link público da conexão, com `e=` — mostra o cartão `.custom-css-chat-entrada` (com `data-etapa`: `formulario` · `pergunta`) dentro da tela `.custom-css-chat-screen`, com o país (`.custom-css-chat-entrada-pais`), o telefone (`.custom-css-chat-entrada-telefone`), o nome (`.custom-css-chat-entrada-nome`), o aceite (`.custom-css-chat-entrada-consentimento`), o "Prefiro não informar meu telefone" (`.custom-css-chat-entrada-sem-telefone`) e o botão Entrar (`.custom-css-chat-entrada-enviar`). De volta ao link com uma conversa lembrada neste navegador, a pergunta: `.custom-css-chat-entrada-continuar` e `.custom-css-chat-entrada-comecar-nova`.
- Chat Externo, na página do canal (o link com `h=`): o topo da conversa (`.custom-css-chat-header`) ganha, no fim, o botão "Começar nova conversa" (`.custom-css-chat-canal-nova-conversa`) quando a conexão tem a página de entrada. No link do modo alternativo (`t=`), o topo não muda.
- Conexões, no canal Chat Externo: a janela `.custom-css-modal-chat-externo-canal` ganha a aba da página de entrada, `.custom-css-chat-externo-canal-entrada` (desligada até a conexão existir), com o link (`.custom-css-chat-externo-canal-entrada-link`), o botão de copiá-lo (`.custom-css-chat-externo-canal-entrada-copiar`) e o de gerar um link novo (`.custom-css-chat-externo-canal-entrada-gerar-novo`), que pede confirmação na janela `.custom-css-modal-confirmation-chat-externo-novo-link`. No cartão da conexão do canal, o botão "Copiar link de entrada": `data-connection-action="copiar-link-entrada"`.

### 29.524.0

- Chat Externo: a mesma página abre a conversa do canal próprio, pelo link com `h=` (o do modo alternativo, com `t=`, não muda). Nela, a tela inteira (`.custom-css-chat-app`) ganha `data-canal-estado` (`aberto` · `encerrado` · `avaliacao` · `bloqueada`), e há duas faixas novas logo acima da barra de digitação: `.custom-css-chat-canal-encerrado` (o atendimento encerrado, com o campo livre para começar outro) e `.custom-css-chat-canal-bloqueada` (a conversa encerrada pelo atendimento, com o campo travado).
- Chat Externo, na página do canal: na conversa retomada num atendimento novo, as mensagens do atendimento anterior que continuam na tela ganham `data-atendimento="anterior"` na linha (`.custom-css-chat-row`) e perdem o botão de reagir e responder (`.custom-css-chat-actions-btn`); com a conversa bloqueada pelo atendimento, as mensagens interativas ficam com `data-aberta="false"`. As duas faixas do canal só existem no link com `h=` — no do modo alternativo, a página não ganha elemento nenhum.
- Atendimento do canal Chat Externo (`externalchat_inc`), no painel: o selo `.custom-css-ticket-selo-nao-verificado` ("Telefone informado, não verificado", com a explicação no `title`) no começo da linha de baixo do cabeçalho, sempre — no canal, o telefone é o que o cliente digitou na página, e ninguém confere se é dele. Na barra de ações (e no menu de Ações do celular), em qualquer status, a ação de bloquear a conversa, com o nome em `data-action` e em `data-acao`: `bloquear-conversa` · `desbloquear-conversa` (o que o clique faz); recolhida no menu `⋯` da barra, o item leva só o `data-action`. Bloquear pede confirmação, na janela `.custom-css-modal-confirmation-atendimento-bloquear-conversa`.
- Atendimento do canal Chat Externo: o compositor não tem o "Somente chat externo" (`data-action="external-only"`), e a mensagem do atendente não leva o `.custom-css-message-chat-externo` com `data-chat-externo="somenteExterno"` — no canal tudo vai para a página, e o cliente não tem WhatsApp do outro lado. Nos outros canais, nada muda.

### 29.523.0

- Conexões: o canal Chat Externo — `externalchat_inc` no `data-channel` (o cartão da conexão e o ícone `.ticket-channel-icon`, um balão duplo índigo), o chip de filtro `data-channel-filter="chatExterno"`, e o item do menu "Ações" com `data-menu-action="adicionar-chat-externo"` e `data-conexao="chat-externo"` (só com o canal no plano). O cadastro é a janela `.custom-css-modal-chat-externo-canal`, com uma classe por aba: `.custom-css-chat-externo-canal-geral`, `-mensagens`, `-comportamento` (com `.custom-css-chat-externo-canal-redirecionamento`) e `-integracoes`. Quando a conexão não carrega, o formulário dá lugar ao aviso `.custom-css-chat-externo-canal-erro`.

### 29.521.0

- Tela de Usuários: no cartão de cada pessoa, o botão de status e sessão `.custom-css-user-btn-presenca` (`data-acao="presenca"`, com o status em `data-status`), que abre o menu `.custom-css-user-menu-presenca` (`data-menu-action`: `online` · `away` · `offline` · `derrubar-sessao`); a confirmação de derrubar a sessão é `.custom-css-modal-confirmation-usuario-derrubar-sessao`.

### 29.518.0

- Campo de mensagem do atendimento (os dois compositores): com o atendimento na página do Chat Externo, o "Somente chat externo" (`data-action="external-only"`) começa ligado, mas deixa de ser travado — perde o `aria-disabled`, e o clique o desliga para a mensagem sair pelo WhatsApp; `aria-pressed` diz o estado.

### 29.517.0

- Chat Externo: a folha de uma lista mostra o título de cada seção (`.custom-css-chat-sheet-section`), antes da primeira opção dela — as listas que a API manda à página têm seções, como no WhatsApp.
- Campo de digitação do atendimento: a altura que o Material-UI grava no campo a cada letra, e como mudá-la com `max-height` e `min-height` (ver "Atributos de estado").

### 29.515.0

- Telas de entrada: no login, os campos com nome (`.custom-css-login-email` e `.custom-css-login-password`, com `-label` no rótulo e `-input` na caixa; o do código do 2FA, `.custom-css-login-totp`), a linha dos links (`.custom-css-login-links`) com cada link em `.custom-css-login-link` e `data-link`, e o idioma em `.custom-css-login-idioma`. No recuperar a senha: o cartão (`.custom-css-forgotpassword-card`), o logo (`-logo`), o título (`-title`), o campo do e-mail (`-email`, com `-label` e `-input`) e a linha do link (`-links`, com `-link`).
- A linha de copyright com `.custom-css-copyright` no login, no cadastro, no recuperar a senha e na pesquisa de satisfação. A cor saiu do `style` para a classe — antes, só com `!important`.
- O olho de mostrar a senha (login e troca de senha) diz o que faz no idioma da pessoa ("Mostrar senha" / "Ocultar senha", no `aria-label`) e se a senha está à vista (`aria-pressed`); com nome em `.custom-css-login-password-toggle` e `.custom-css-reset-password-toggle`.
- Chat Externo: o botão dos emojis (`.custom-css-chat-emoji-btn`), o de anexar (`.custom-css-chat-attach-btn`), a caixa do campo (`.custom-css-chat-input-wrap`), a caixa dos emojis (`.custom-css-chat-emoji-pop`, com `data-aberto`), a barra da gravação (`.custom-css-chat-recbar`, com `data-gravando`, e as partes `-rec-dot`, `-rec-time`, `-rec-cancel` e `-rec-send`) e a caixa da folha da lista (`.custom-css-chat-sheet-box`). O fundo branco da caixa do campo lê `--wa-input`, e o da caixa dos emojis e o da folha, `--wa-popup` — sem customização, o branco de sempre.

### 29.514.0

- Janelas: `.custom-css-dialog-header`, `.custom-css-dialog-body` e `.custom-css-dialog-footer` no cabeçalho, no corpo e no rodapé de TODAS as janelas — eram só as quatro de Criar Ticket, e o corpo não tinha nome. Valem também nas que montam o cabeçalho à mão (o bloco com gradiente) e no corpo das janelas do editor de fluxo. Por estarem em toda janela, saem da lista por área e ficam nas Convenções, como o `.custom-css-modal`.
- ⚠️ Quem já pintava `.custom-css-dialog-header` ou `.custom-css-dialog-footer` contando com as quatro janelas de Criar Ticket: a regra passa a valer em todas. Para manter só nelas, ponha o nome da janela na frente (`.custom-css-modal-newticket .custom-css-dialog-header`, por exemplo).
- Dentro das janelas: `.custom-css-dialog-tabs` na faixa de abas (Editar Usuário, Nova Tag, Novo Setor, Links Curtos e as outras com abas); `.custom-css-dialog-secao` (com `data-secao`) e `.custom-css-dialog-secao-titulo` nas seções de Tag, de Categoria e de Webhook; e, no campo Setores (Editar Usuário, conexões…), o chip de cada setor com `.custom-css-queue-select-chip`, `data-queue-id`, `data-queue-color` e `--queue-color`.
- Encerramento com venda: `.custom-css-encerramento-corpo` e `.custom-css-encerramento-cartao`; no cartão do motivo, `-tag-cor` (a bolinha), `-tag-nome`, `-tag-chips`, `-tag-tipo` e `-tag-valor`; no indicador, `-etapa-numero` e `-etapa-nome`. No escuro, os dois chips do cartão deixaram de ser manchas claras; no celular (390px), os nomes das etapas cabem na janela.
- Respostas Rápidas (Adicionar): os cartões de tipo com `.custom-css-quick-message-tipo`, `data-tipo` (`texto` · `arquivo`) e `aria-pressed`; as bolinhas das etapas com `.custom-css-quick-message-etapa`, `data-etapa` e `data-estado`. Links Curtos: as caixas de explicação com `.custom-css-short-link-info` (com `data-tipo`) e `.custom-css-short-link-aviso` — e legíveis no escuro.
- Tema escuro: o botão principal (Salvar, Adicionar, Confirmar…) lê `--mui-button-primary`, `--mui-button-primary-hover` e `--mui-button-primary-contrast` (ver "As cores do tema escuro") — sem customização, o cinza de sempre. E o rodapé da Busca Avançada deixou de ser uma faixa clara no escuro.
- Botões de ação dos cadastros com `data-acao` (o verbo, em português): Tags, Setores, Respostas Rápidas, Categorias, Usuários, Contatos, Webhooks, Templates WABA, Arquivos do Bot, Contas de e-mail e Avaliações. Os valores estão no atributo.
- Usuários: o cartão da pessoa com `.custom-css-users-card` (`data-user-id`, `data-user-profile`) e as partes `-nome`, `-super`, `-perfil`, `-status` (com `-presenca`, `-ausente` e `-sigame`), `-id`, `-email`, `-conexao`, `-setores` e `-setor`. Templates WABA: o cartão com `.custom-css-waba-template-card` (`data-template-id`, `data-template-status`) e as partes `-icone`, `-nome`, `-categoria`, `-status`, `-detalhes`, `-mensagem` e `-acoes`; no Criar Template, `.custom-css-waba-template-form-secao` (com `data-secao`) e `-titulo`.
- Painel do contato: no cartão, `.contact-card-foto`, `.contact-card-nome`, `.contact-card-telefone`, `.contact-card-email` e `.contact-card-editar` (com `data-action="editar"`); a caixa do campo das anotações, `.contact-note-input`; a caixa do iframe da integração, `.contact-drawer-iframe`; e o painel diz em `data-aberto` se está aberto.
- Telas de lista: `.custom-css-page-panel` no painel logo abaixo do cabeçalho da página — Tags, Setores, Configurações, os quatro Kanbans e as outras telas com o mesmo desenho. Como as janelas, fica nas Convenções.

### 29.513.0

- Cartão do ticket (lista e grupos): `.ticket-primary` (a parte de cima), `.ticket-primary-line` e `.ticket-primary-name` (a linha e o nome dentro dela), `.ticket-avatar` (a coluna da foto) e `.ticket-divider` (o divisor entre cartões). A faixa das etiquetas diz quantas são em `data-total`, e cada etiqueta a posição dela em `data-posicao`. A altura mínima de 115px virou a variável `--ticket-min-height`.
- Conversa: `.message-internal-title` e `.message-internal-text` no balão da nota interna, e `.message-date-divider-label` na data do divisor.
- Fotos com nome fora do Chat: `.custom-css-quadro-card-avatar` (Quadro), `.custom-css-contacts-avatar` (Contatos), `.custom-css-users-card-avatar` (Usuários) e, no Chat Interno, `.custom-css-chats-avatar` em todas, mais o lugar: `-item-avatar`, `-conversa-avatar`, `-msg-avatar`, `-participante-avatar`, `-mencao-avatar` e `-popover-avatar`.
- Barra do topo: os menus da conta, do status e do idioma com nome no papel (`.custom-css-menu-usuario`, `-status`, `-idioma`) e `data-menu-action` nos itens; o botão do status com `data-status`; os popovers das notificações, dos atendimentos, dos informativos, do Chat Interno e do som com `.custom-css-popover` e o nome na raiz, e `.custom-css-popover-paper` no papel — que o das notas internas também ganhou; o som com `data-volume`; o sino do push com `data-appbar="push"` e `aria-pressed`; a barra com `.custom-css-appbar-toolbar` e a cor em `--appbar-fundo` e `--appbar-cor`; no "+" do celular, o atualizar e o tema com `data-appbar`.
- Menu lateral: a caixa do ícone dos grupos (Kanban, CRM…) com `.custom-css-icon`, como os outros itens, e a seta com `.custom-css-menu-group-chevron`. O ícone do servidor em `--custom-css-favicon` e `--custom-css-favicon-256`, no `:root`.
- Quadro e Kanbans: `.custom-css-ticket-conversa` na coluna da conversa (no modal do Quadro e na tela de atendimentos); nos quatro Kanbans, o "Carregar Mais Tickets do Servidor" com `-btn-load-more`, o "Carregar mais" da coluna com `-col-load-more` e o olho do card com `data-action="spy"`. ⚠️ Em `/kanban`, a caixa de dentro também tinha `id="custom-css-kanban"` — id repetido, e `#custom-css-kanban` pegava as duas. O id fica só na página, e a caixa vira `.custom-css-kanban-conteudo`.
- Celular: a faixa Ticket / Atendimentos com `.custom-css-mobile-tabs`, e cada aba com `.custom-css-mobile-tab`, `data-aba` e `aria-selected`; a caixa das ações do atendimento com `.custom-css-ticket-actions-mobile` — e sem as caixas vazias entre os botões, que eram as janelas do Agendar e da Oportunidade; o botão que abre o menu de Ações com `data-action="mais-acoes"`; o X que tira todas as etiquetas com `.custom-css-ticket-tags-limpar`.
- Valores que o catálogo não tinha: `data-status` do balão (`delivered` e `unknown`; `received` e `played` nunca saíram); `data-action` (`finish`, `pin`, `ver-notas-internas` e os do CRM, do Google Calendar e da conciliação); `data-appbar` (`tickets`, `internal-chat` — o antigo `msgs` —, `status`, `extension`, `dialer` e o novo `push`); `data-icon` (`notifications`, `extension`, `dialer`); `data-acao` (`acessos`); e a lista completa do `data-channel`. `#custom-css-instagram-posts` também na tela com o módulo no plano.

### 29.512.0

- `data-mode` do campo de digitação: com a Comunicação interna ligada, passa a ser `internal` também no atendimento que está no chat externo — antes ficava `external`, e o campo tinha a cor do só canal externo, embora a mensagem saísse como nota interna. A cor do campo acompanha: é a da nota interna.

### 29.511.0

- Pontos por quantidade, na janela de Pontuação e níveis (`.custom-css-gamificacao-config`, em Minha Evolução): cada regra é `.custom-css-gamificacao-regra`, com `data-regra` (`venda` · `valor` · `meta` · `encerramento` · `funil` · `etiqueta`). As regras por funil e por etiqueta ficam nas seções `.custom-css-gamificacao-config-funis` e `.custom-css-gamificacao-config-etiquetas`, uma linha por alvo (`data-alvo-id`), com os botões em `data-gamificacao-action` (`adicionar-funil` · `adicionar-etiqueta` · `remover-regra`). No quadro de atendimentos, `data-regra="fila"` continua como estava.
- Extrato de Minha Evolução: `data-motivo` ganhou `funil`, `etiqueta` e `encerramento`, e `data-causa` ganhou `outroFunil`, `semEtiqueta` e `encerramentoDesfeito`. No lançamento por funil ou por etiqueta, o nome do funil ou da etiqueta aparece em `.custom-css-minha-evolucao-movimento-alvo`.

### 29.510.0

- Período personalizado e campanhas: Minha Evolução, Ranking de Vendas e Ranking do CRM ganharam o seletor de período `.custom-css-seletor-periodo`, com `data-periodo` (`mes` · `personalizado` · `campanha`). As partes são `.custom-css-seletor-periodo-tipo` (a lista), `.custom-css-seletor-periodo-de` e `.custom-css-seletor-periodo-ate` (os dias, no personalizado) e, na lista, o título do grupo é `.custom-css-seletor-periodo-grupo` e cada campanha é `.custom-css-seletor-periodo-campanha`, com `data-campanha-id`. Os campos de mês de cada tela continuam onde estavam, e aparecem quando o período é o mês.
- Janela de Campanhas (o botão `.custom-css-minha-evolucao-campanhas`, em Minha Evolução, só para gestor): `.custom-css-modal.custom-css-gamificacao-campanhas`, com o formulário `.custom-css-gamificacao-campanha-form` (`data-editando`), cada campanha `.custom-css-gamificacao-campanha` (`data-campanha-id` e `data-situacao`) e os botões em `data-gamificacao-action`. A confirmação de apagar é `.custom-css-modal-confirmation-gamificacao-campanha-excluir`.
- Minha Evolução: a linha `.custom-css-minha-evolucao-contagem`, acima do nível, diz de onde ele conta (`data-contagem`: `campanha` ou `livre`). Fora do mês, o cartão da meta dá lugar a `.custom-css-minha-evolucao-vendido-periodo` (`data-stat="vendido"`), porque a meta é cadastrada por mês.

### 29.509.0

- Minha Evolução: cada linha do extrato é `.custom-css-minha-evolucao-movimento`, com `data-motivo`, `data-estorno` e, no estorno, `data-causa`. O estorno é a linha nova de quando uma venda que pontuou deixa de contar (apagada, reaberta, perdida, reprovada…): ela devolve os pontos, e o motivo aparece em `.custom-css-minha-evolucao-movimento-causa`. Os pontos de cada linha ficam em `.custom-css-minha-evolucao-movimento-pontos`, com o sinal (`+160`, `−160`) e, no estorno, a cor de erro do tema.

### 29.508.0

- As cores fixas do tema escuro (13.1) agora leem as variáveis, com a cor de antes como reserva — a tabela de "As cores do tema escuro" diz quem lê cada uma. O papel (`#1C1C1C`) vai para `--mui-paper` (ou `--mui-background`, onde a tela usava o fundo da página); os campos, o rodapé das janelas e as células, para `--mui-paper-2`; o que era mais claro (`#2a2a2a`, `#2d2d2d`, `#333333`), para `--mui-paper-3`.
- Variável nova: `--mui-divider` (`#363636`), lida por todo `.MuiDivider-root` do tema escuro. E o cabeçalho fixo das tabelas (a célula `stickyHeader`) passa a ler `--mui-background`.
- ⚠️ Sem customização, quase nada muda na tela: o que era `#1C1C1C` continua igual, e o resto fica a 1 ou 2 tons — menos o rodapé das janelas de agendamento e do relatório de chamadas (`#1e1e1e` → `#1a1a1a`), a hora no cartão do ticket (`.ticket-datetime`, `#333333` → `#2b2b2b`) e o botão do Dashboard legado no hover (`#242424` → `#2b2b2b`). A regra que acertava esses lugares um a um pode sair.
- Editor de fluxo (13.2): nos blocos de várias saídas — Randomizador, HTTP Request, Asaas, Condição, Horário Escolhido, IXC, É Seguidor? e Menu — a alça de cada saída (`.react-flow__handle.source`) é FILHA da linha dela (`.custom-css-flow-node-item`, agora `position: relative`) e fica no meio dela, como no Switch. Mexer no respiro ou na fonte do bloco não descola mais a alça da linha. ⚠️ O texto da saída fica num `<span>` dentro da linha, e no É Seguidor? a linha troca `width: 160` por `min-width: 160`.
- Editor de fluxo (13.3): `.custom-css-flow-topo-novo` (a linha do "+"), `.custom-css-flow-topo` (a do estado e da barra), `.custom-css-flow-palco` (a do canvas), `.custom-css-flow-busca-resultados` e, em cada resultado, `.custom-css-flow-busca-resultado` com `data-node-id`; na janela de Conteúdo, `.custom-css-flow-conteudo-lista` (no mesmo nó do `.body-card`). E a classe comum `.custom-css-modal-flow` nas 41 janelas de editar bloco, junto da de cada tipo (`.custom-css-modal-flow-<tipo>`, que continua).
- Lista de fluxos (13.4): o cartão de cada fluxo é `.custom-css-flow-card`, com `data-flow-id` e `data-ativo`; as partes são `-icone`, `-nome`, `-etiquetas`, `-status` (com `data-ativo`), `-categoria` e `-acoes`; as ações têm `data-flow-action` `editar` e `mais` (o `logs` já existia); e o botão Importar do cabeçalho é `.custom-css-btn-flow-importar`.

### 29.505.0

- ⚠️ `data-queue-chatbot` no cartão do ticket (`.custom-css-ticket-item`, também o de grupo): no perfil Usuário vinha `false` em toda fila de chatbot — a lista desse perfil chegava sem a informação. Agora o valor é o mesmo para admin, supervisor e Usuário. Em qualquer perfil, o atributo também podia virar `false` depois de uma atualização em tempo real (uma mensagem nova, por exemplo); isso não acontece mais. O cabeçalho da conversa aberta passa a publicar `data-queue-chatbot` desde a abertura: antes, numa conversa com fila, ele ficava ausente.

### 29.504.0

- Gerenciador de Arquivos (`#custom-css-bot-files`): a prévia de cada imagem e vídeo, grande, no card — `.custom-css-bot-files-previa`, com `data-media-type` (`image` · `video`) e, no vídeo, o ícone `.custom-css-bot-files-previa-play`. Clicar abre a janela `.custom-css-modal-botfile-previa`, com a imagem ampliada ou o vídeo tocando. ⚠️ O cabeçalho do card mostra só o ícone do tipo: a miniatura de 48px da imagem saiu, porque a imagem agora aparece grande logo abaixo.

### 29.502.0

- Cards de atendimento — Quadro (`.custom-css-quadro-card`), lista (`.custom-css-ticket-item`, também o de grupo) e os quatro Kanban: `data-operator-id` e `data-operator-name` (novos), o id e o nome do operador, para destacar ou contar os cards de um atendente sem ler o texto da pílula. Card sem operador fica sem os dois. O nome é o que o operador já tinha no cabeçalho do atendimento (`.ticket-operator`), no ranking e no relatório do rodízio; `data-user-id` continua sendo o convidado.

### 29.501.0

- Balão da nota de erro (`.message-internal-error`): quando o corpo é um código que a API do canal devolveu e que a tela sabe traduzir — hoje, `recipient_not_on_whatsapp` —, o balão mostra a frase no idioma de quem atende (Este número não está no WhatsApp. A mensagem não foi enviada.), e o código vai no atributo novo `data-erro-da-api`. ⚠️ O texto do balão muda; o banco continua guardando o código.

### 29.500.0

- Chat (/tickets): os ganchos que faltavam. Nada foi trocado nem renomeado: as classes que já existiam continuam nos mesmos elementos.
- A página ganhou âncora: `#custom-css-tickets-page`, no computador e no celular. O `-page` no fim é porque `.custom-css-tickets` já é a classe do painel da lista.
- Lista de atendimentos: `data-action` nos botões de cima — `new-ticket` (o Novo), `sort` (o Ordenar), `more-filters` (o "+" dos filtros, nas três visões) e `advanced-search` (a Busca Avançada). O menu do Ordenar é `.custom-css-page-menu` + `.custom-css-menu-ordenar-atendimentos`, com `data-menu-action` (`newest` · `oldest`), `role="menuitemradio"` e o escolhido em `aria-checked`; a janela dos filtros é `.custom-css-page-menu` + `.custom-css-menu-mais-filtros`.
- Abas Atendendo e Aguardando: o contador, que já tinha `data-carregados` e `data-total`, ganhou a classe `.custom-css-ticket-tabs-contador`, e a bolinha do número, `.custom-css-ticket-tabs-contador-valor`. A bolinha recebe classe, mas não atributo: o Material-UI 4 não repassa.
- Cartão do ticket: `data-action="spy"` no olho do Espiar, e o selo das não lidas é `.custom-css-ticket-unread`, com a bolinha do número em `.custom-css-ticket-unread-valor` (quantas são continua no cartão, em `data-unread-count`). No cartão de grupo, o nome ganhou o `.ticket-name` do cartão individual — antes era texto solto.
- A foto do contato tem o mesmo nome nos três lugares: `.custom-css-contact-avatar`, no cartão do ticket, no cabeçalho do atendimento e no painel do contato.
- ⚠️ Conversa: `.message-date-divider` estava só no PRIMEIRO divisor de data — os dos outros dias não tinham a classe. Agora está em todos, e a regra escrita para ela passa a valer em todos os dias da conversa.
- Barra de ações do atendimento: duas propriedades novas, `--ticket-actions-ordem` (quais ações vêm primeiro, pelos nomes do `data-action`) e `--ticket-actions-no-menu` (as que ficam sempre no menu `⋯`); a `--ticket-actions-visiveis` conta na ordem pedida, sem as do menu. ⚠️ Com a ordem pedida, os botões trocam de lugar também no DOM, e um `:nth-child` na barra conta na ordem nova; sem as duas propriedades, a ordem é a de sempre. O `accept` (o Aceitar do atendimento aguardando), que já estava na barra, entrou na tabela do `data-action`.
- ⚠️ A `--ticket-actions-visiveis` passa a contar só AÇÕES. O "Marcar como lido", que não desenha nada quando não há mensagem não lida, e os modais que moram na barra comiam uma vaga calados: com `3`, apareciam duas ações. Agora aparecem as três.
- Seção nova, Classes sem prefixo: as partes do Chat que já tinham nome antes do `custom-css-` (`ticket-*`, `message-*` e `contact-*`) entram no catálogo, cada uma com o que é. Os nomes continuam os mesmos.

### 29.498.0

- Os ganchos que faltavam (a terceira lista: 9.7, 11.7, 11.8 e 12.1 a 12.12). Nada foi trocado nem renomeado: tudo o que existia continua no mesmo elemento.
- Respostas rápidas (11.8), nos dois campos de mensagem: a lista do "/" é `.custom-css-quick-replies`, e cada opção é `.custom-css-quick-reply`, com `data-quick-message-id` e a mensagem inteira em `data-quick-message`, e as partes `.custom-css-quick-reply-atalho`, `-categoria` (quando a resposta tem uma) e `-mensagem`. O texto da opção é o mesmo de antes. A resposta rápida não tem título: o que aparece entre o atalho e a mensagem é a categoria.
- Lista de atendimentos (12.1): `data-aba` (`open` · `pending`) em cada aba, e o contador em atributo — `data-carregados` e `data-total` no `.MuiBadge-root` da aba, o pai do `.MuiBadge-badge`. ⚠️ No `-badge` não deu sem mudar a tela: o Material-UI 4 não repassa atributo para ele, e trocar o número por um elemento faria o `0` aparecer.
- Quadro de Atendimentos (11.7, 12.2): as partes do card — `.custom-css-quadro-card-cabecalho`, `-card-nome`, `-card-previa` e `-card-pilulas` — e a cor de cada pílula em atributo, com os nomes do cartão da lista: `data-connection-color` em `.custom-css-quadro-conexao`, `data-user-color` em `-quadro-operador` e `data-queue-color` em `-quadro-fila`.
- Quadro e Kanban (12.7): `data-connection-status` nos cards do Quadro (`.custom-css-quadro-card`) e dos três Kanban (`.custom-css-kanban-card`, `-kanban-team-card`, `-kanban-filas-card`), com o mesmo cálculo e os mesmos valores do cartão da lista.
- Conexões (12.3), nos dois modos: `.custom-css-connection-topo`, `-connection-nome`, `-connection-canal` (o selo do ícone) e `-connection-acoes` nas fileiras de ações, com `data-tipo="texto"` (os botões com texto) ou `"icone"`. Na barra de filtros, `.custom-css-connection-filters-rotulo` no "Canais:".
- Configurações (12.4): `.custom-css-settings-menu-item-icone` e `-menu-item-rotulo` nas duas partes de cada cartão do menu. Painel do contato (12.5): `.contact-drawer-topo` na primeira linha, `.contact-drawer-titulo` no título e `data-action="fechar"`, com `aria-label`, no X. Cabeçalho do atendimento (12.6): `.ticket-collaborator`, com `data-user-id`, em cada convidado, e `.ticket-collaborators-more`, com `data-count`, no "+N" dos que não couberam.
- Editor de fluxo, os blocos (12.8): todos seguem o esquema do Switch — `.custom-css-flow-node` e `.custom-css-flow-node-<tipo>` no cartão (o tipo com hífen: `-menu`, `-single-block`, `-http-request`…), `-node-cabecalho`, `-node-icone`, `-node-titulo`, `-node-acoes` (com `data-action="copiar"` e `"excluir"`), `-node-corpo` e `-node-item` em cada item de lista, com `data-tipo` (ver a tabela). A cor do tipo fica em `--flow-node-cor`, e o fundo, a borda e a sombra do cartão leem `--flow-node-fundo`, `--flow-node-borda` e `--flow-node-sombra`, com as cores de hoje como reserva (ver Propriedades). Enviar Contato e Enviar Localização foram redesenhados no mesmo modelo dos outros blocos. ⚠️ No Switch, as linhas das regras e a da saída padrão ganharam `-node-item`; no Pular para, o destino ganhou `-node-corpo` — as classes de antes continuam.
- Editor de fluxo, a barra e as janelas (12.9 a 12.11): `.custom-css-flow-barra` na fileira dos botões, `.custom-css-flow-btn-novo` no "+", `.custom-css-flow-status` com `data-salvo`, `data-action` em cada botão da barra e `.custom-css-flow-tamanho` com `data-nivel` no chip do tamanho. A janela de escolher o bloco é `.custom-css-modal` + `.custom-css-modal-flow-escolher-bloco`, com `.custom-css-flow-escolher-titulo`, `-escolher-busca`, `-escolher-item` (com o `data-action` de sempre) e `-escolher-rotulo`; os blocos não têm grupo, e por isso não há `data-grupo`. As janelas do Menu e dos Botões Interativos passam a ter o `.custom-css-modal-flow-menu` e o `-modal-flow-button` que já estavam no código e não chegavam à tela. Na janela do Conteúdo, `.custom-css-flow-conteudo-item` com `data-tipo` em cada item (a classe numerada continua).
- Editor de fluxo, os painéis (12.12): `.custom-css-flow-versoes` na gaveta de Versões e `.custom-css-flow-versao`, com `data-mais-recente`, em cada versão; `.custom-css-flow-resumo-linha` em cada linha do Resumo; e `.custom-css-flow-verificar-item`, com `data-problema`, em cada bloco do Verificar. ⚠️ O Verificar ganhou uma seção, a dos blocos sem saída (`.custom-css-flow-verificador-sem-saida`), entre os sem entrada e os saltos sem destino.
- Arquivos da Conversa (9.7): no tema escuro, a área da miniatura (`.custom-css-ticket-files-miniatura`) deixa de ser um quadrado claro e passa a usar `--mui-paper-3`. A faixa do total já tinha nome: `.custom-css-ticket-files-resumo`.

### 29.495.0

- Barra de ações do atendimento (`.custom-css-ticket-actions`) e a do celular: o "Marcar como lido" (`data-action="mark-as-read"`, com `data-unread-count`). Ele só existe enquanto há mensagem não lida, e entra em PRIMEIRO na barra. ⚠️ Quando aparece, as outras ações andam uma posição: numa barra apertada a última vai para o menu `⋯`, e com `--ticket-actions-visiveis` ele ocupa uma das vagas.

### 29.493.0

- Mensagem represada pelo concatenador (`.custom-css-message-aguardando`, com `data-aguardando-envio`): ganha os botões `.custom-css-message-cancelar-envio`, em cada bolha que quem está vendo pode cancelar (quem escreveu, admin e supervisor), e `.custom-css-message-cancelar-todas`, só na última delas quando há duas ou mais aguardando. ⚠️ O selo fica mais largo: os botões entram depois da barra de espera (`.custom-css-message-barra-concat`).

### 29.489.0

- Chat Externo: a página ganha as mensagens com botões, lista e cartão, para o fluxo que continua nela (a chave "Continuar o fluxo no chat externo" do bloco do link) — as âncoras `.custom-css-chat-interactive*`, os cartões de contato, localização e produto, e a folha da lista (`.custom-css-chat-sheet*`). ⚠️ O balão (`.custom-css-chat-bubble`) de uma figurinha passa a vir sem fundo e sem sombra, como no WhatsApp; a linha continua com `data-media-type="image"`.
- Campo de mensagem do atendimento (os dois compositores): com o atendimento na página do Chat Externo, o "Somente chat externo" (`data-action="external-only"`) aparece ligado e com `aria-disabled="true"` — o clique não o desliga.
- Janela do bloco Link do Chat Externo (`.custom-css-modal-flow-external-chat-link`): a chave "Continuar o fluxo no chat externo" (`.custom-css-flow-external-chat-link-continuar`), embaixo das explicações. No desenho do fluxo, o bloco com a chave ligada mostra o selo `.custom-css-flow-node-external-chat-continua`.

### 29.483.0

- Pixel da Meta no formato de mensagens: a aba Pixel da janela da tag (`.custom-css-modal-tag`) e a janela do bloco Pixel do fluxo (`.custom-css-modal-flow-pixel`) ganham no topo o campo "Formato do evento" (`.custom-css-tag-pixel-formato` e `.custom-css-flow-pixel-formato`), e os campos de sempre descem. O bloco Pixel no desenho do fluxo passa a ter gancho (`.custom-css-flow-node-pixel`, com `data-pixel-formato`) e, no formato de mensagens, duas saídas (`.custom-css-flow-node-pixel-elegivel` e `.custom-css-flow-node-pixel-nao-elegivel`). Na tela de logs do Pixel, o cartão de cada evento do formato de mensagens ganha a situação (`.custom-css-pixel-logs-status`, com `data-pixel-status`) e, quando o evento não saiu, o motivo (`.custom-css-pixel-logs-motivo`).

### 29.481.0

- Tela de login: um campo "Entrar como" entre a senha e o botão Entrar (`.custom-css-login-status`), com `data-status` valendo o status escolhido — `online` · `away` (Ausente) · `offline`. As opções abrem no menu `.custom-css-login-status-menu`; cada uma é `.custom-css-login-status-opcao`, com o próprio `data-status` e a bolinha colorida `.custom-css-login-status-cor`. Embaixo do campo, a explicação `.custom-css-login-status-ajuda`. ⚠️ O cartão do login (`.custom-css-login-card`) fica mais alto: o botão Entrar desce o tanto do campo novo.

### 29.479.0

- Modal do ticket, no celular: uma faixa de 40px no topo (`.custom-css-ticket-fechar-faixa`), com o botão de fechar à direita (`.custom-css-ticket-fechar`) — até aqui o modal não tinha como ser fechado no celular. O X some enquanto o painel do contato está aberto, que tem o fechar dele. No computador e no modo incorporado, nada muda. ⚠️ No celular, a linha da foto deixa de encostar no topo do modal: fica logo abaixo da faixa.

### 29.478.0

- Os ganchos que faltavam (décima leva, 10.1 e 10.26 a 10.28; 11.1 a 11.6; e as linhas de metadado de Conexões). Nada foi trocado nem renomeado: tudo o que existia continua no mesmo elemento.
- Chat Interno (11.1): no item da lista, `.custom-css-chats-item-nome`, `-item-previa` e `-item-data`, e `data-action` (`edit` · `delete`, com `data-chat-id`) nos dois botões que não tinham; `.custom-css-chats-cabecalho-icone` no ícone do topo da lista; no cabeçalho da conversa, `.custom-css-chats-conversa-titulo`, `-conversa-subtitulo` e `.custom-css-chats-btn-participantes`; nos dois balões, `.custom-css-chats-msg-autor`, `-msg-texto` e `-msg-hora`; no campo de mensagem, `data-action` `record-audio` · `upload` · `send`; e, no celular, `.custom-css-chats-topo` no bloco do cabeçalho e das abas "Conversas / Mensagens".
- Campo de mensagem do atendimento (os dois compositores): `data-action="send"` no botão de enviar, que vira `forward` enquanto o modo de selecionar mensagens está ligado. Até aqui o botão não tinha nome.
- Kanban (11.2): `.custom-css-kanban-card-tag` com `data-tag-id` e `data-tag-color` em cada etiqueta do card, no Kanban e no Kanban da equipe. Os Kanban de Filas e de Grupos não mostram etiqueta no card (no de Grupos, a etiqueta é a própria coluna).
- Quadro de Atendimentos (11.3): `--lane-color` também na coluna (`.custom-css-quadro-coluna`), com a cor da bolinha — o Quadro pode ter o mesmo desenho dos Kanban (ver Propriedades).
- Agendamentos (11.4): `.custom-css-agenda-dia-numero` no número de cada dia do calendário (o que vira a pastilha do dia de hoje) e `.custom-css-agenda-titulo` no título da barra — o mês, ou o dia na visualização Dia.
- Ícone dos cabeçalhos de página (11.5): `.custom-css-page-header-icone` no Ranking de Vendas, no Chat Interno (junto do `-chats-cabecalho-icone`), em Traduções (junto do `-section-header-icone`) e no Dashboard. No Dashboard o ícone não tem caixa: a classe fica no próprio `<svg>`, dentro do título.
- Pesquisar (11.6): `.custom-css-atendimentos-buscar` no bloco do botão "Buscar Atendimentos".
- Conexões: `.custom-css-connection-meta-rotulo` e `-meta-valor` nas duas partes de cada linha de metadado do cartão ("Número:", "ID:"…). Nas três linhas de uma parte só do modo lista — o número, a data da última atualização e o "Pausada desde" —, o texto inteiro é `-meta-valor`.
- Conexões (10.27): `data-connection-action="delete-session"` no Excluir Sessão e `"disconnect"` no Desconectar, os dois botões do cartão que ainda não tinham ação nomeada.
- Conexões (10.26): a janela de confirmação ganha o nome da ação ao lado do `.custom-css-modal-confirmation-conexao`, que continua: `-conexao-excluir`, `-conexao-excluir-sessao`, `-conexao-desconectar`, `-conexao-fechar-todos`, `-conexao-fechar-pendentes`, `-conexao-pausar` e `-conexao-retomar`. Achar a janela de uma ação vira CSS puro, sem anotar por JS qual botão a abriu.
- Dashboard legado (10.1): `.custom-css-page-header` (e `.custom-css-dashboard-legado-barra`) na barra do topo, a do botão de filtros — a tela não tem título, e a barra é o cabeçalho dela, como no Quadro. ⚠️ Regra escrita para `.custom-css-page-header` passa a valer também aqui — era o pedido.
- Cartão do ticket (10.28): `data-names` no selo dos convidados (`.ticket-collaborators`, com o `data-count` de sempre) — os nomes existiam só no balão do :hover.
- Na tabela dos atributos de estado, `data-action` e `data-connection-action` ganharam os valores que já estavam no código e faltavam aqui: `upload`, `record-audio`, `send-contact`, `quick-favorites` e `contact-notes` no campo de mensagem (e `emoji` também no compositor que não é o do Hub); `favorite` e `mark-unread` no Chat Interno; `template-errors`, `restart-pro`, `validate-code`, `send-limit`, `concatenador`, `meta-recheck`, `meta-reconnect` e `ig-check-subscription` no cartão da conexão. `data-favorite` ganhou o lugar dele no Chat Interno.

### 29.475.0

- Página das classes (`/css-docs`): este catálogo nos seis idiomas da plataforma, aberto com ou sem login, com o link na aba Cores. A raiz dela (`#custom-css-documentacao-css`) leva `data-estado` e `data-idioma`, como a da documentação da API, e `data-empty` ganhou o valor `documentacao-css` (a busca sem resultado). ACRESCENTADO: os valores que já existiam continuam.
- No exemplo dos atributos de estado, a nota interna aparecia como `[data-mode="private"]`, um valor que não existe: agora é `[data-mode="internal"]`, o que o campo de digitação usa.
- Na tabela dos atributos de estado, `data-aguardando-envio` aparecia como selo do limitador de envio: o selo é do concatenador, que segura a mensagem enquanto espera se vem mais texto.

### 29.473.0

- Cartão de número (`.custom-css-stat-card` com `data-stat`, e as partes `-icone`, `-rotulo`, `-valor` e `-detalhe`) em mais 47 cartões de 8 telas: o Relatório da Campanha, o Relatório de Ligações, o Relatório da Empresa, Grupos, Consumo de Voz, Minha Evolução, e as estatísticas das Tags e dos Contatos. Os valores de `data-stat` de cada tela estão na tabela de atributos. ACRESCENTADO: as classes que esses elementos já tinham continuam (em Minha Evolução, o cartão do nível segue `.custom-css-minha-evolucao-nivel` e o da meta, `.custom-css-minha-evolucao-meta`).
- Onde o cartão tem mais de uma linha secundária, `-detalhe` fica na primeira: em Enviados (Relatório da Campanha), o "% de sucesso" — a linha das falhas, quando aparece, é a seguinte; em Franquia (Consumo de Voz), o selo "Bloqueado", que só aparece com a franquia bloqueada. Em Minha Evolução, o rótulo "pontos" fica DENTRO do valor do cartão do nível, como já era desenhado.

### 29.472.0

- Agendamentos: o botão da visualização escolhida (Mês, Dia ou Histórico — `.custom-css-view-toggle[aria-pressed="true"]`, que já levava a classe `active`) passa a ser pintado com a cor principal, como o escolhido de Conexões e Tarefas; no escuro, pelas variáveis `--mui-primary*`. Antes os três ficavam iguais. Quem já destacava o escolhido pelo CSS personalizado continua vencendo: a regra dele entra depois.
- Os menus de Ações de Conexões (`.custom-css-menu-conexoes-acoes`) e dos Fluxos (`.custom-css-menu-fluxo-acoes`) abrem logo abaixo do botão. Antes abriam em cima dele, cobrindo-o.

### 29.471.0

- ⚠️ No escuro, o texto em cima da cor principal deixou de ser branco em todas as telas e segue `--mui-primary-contrast` (a 29.470.0 tinha feito isso em poucos lugares): o cabeçalho das janelas — o título, o subtítulo, o X e o ícone do círculo —, os selos com número (os filtros de atendimento, o Chat Interno), os botões e os destaques escolhidos (o "Não lidas", o calendário de Tarefas, o de tocar a gravação), os números das etapas, os selos das empresas nos Informativos, o cabeçalho da tabela da Pesquisa de Satisfação, os painéis Resumo e Histórico de versões do editor de fluxo, os ícones do menu de Configurações e o destaque ao passar o mouse. Quem já pintava esses fundos com a cor da marca contando com o texto branco: defina `--mui-primary-contrast: #fff` (ou aponte as três `--mui-primary*` para a marca, como na seção "As cores do tema escuro").
- No escuro, esses fundos — e o fim do gradiente, e o passar do mouse nos botões na cor principal — leem `--mui-primary` e `--mui-primary-dark`: sem customização, a mesma cor de antes. A exceção visível é o destaque ao passar o mouse nas variáveis do Novo Ticket e do Agendamento, que era um tom mais claro calculado (`#E3E3E3`) e passou ao da `--mui-primary`.
- Ficam com a cor de marca, iguais a antes: o ícone verde do WhatsApp no cabeçalho das duas janelas da conexão oficial e o verde de concluído da importação.

### 29.470.0

- As cores do tema escuro em variáveis no `:root` (décima leva, 10.6 e 9.9): `--mui-background`, `--mui-paper`, `--mui-paper-2`, `--mui-paper-3`, `--mui-dashboard-card`, `--mui-primary`, `--mui-primary-dark` e `--mui-primary-contrast` (ver "As cores do tema escuro"). Sem customização, nada muda: cada uma vale a cor de antes.
- A Cor Principal configurada em `--app-primary`, `--app-primary-dark` e `--app-primary-contrast`, nos dois temas (2.1). O escuro continua com o cinza de sempre, e a seção mostra como apontá-lo para a cor da marca.
- No escuro, o papel do Material-UI (`.MuiPaper-root`: janelas, menus, cartões) e o `<body>` leem as variáveis: uma regra no `:root` troca o fundo de todas as janelas (9.9).
- Legíveis no escuro, sem nada na customização: o selo "LIVE" das Conexões, os campos de data do Dashboard legado, o divisor de data da conversa, a barra do editor do Novo Informativo, e o texto sobre a cor principal (abaixo).
- Sem o claro fixo no escuro: a prévia do Criar Template, os quadradinhos dos ícones dos números nos Kanban, o painel "Selecionar ticket" do celular (o `#EEE`) e o item do Anexar Arquivos.
- ⚠️ No escuro, o texto em cima da cor principal (o cinza-claro) deixou de ser branco e segue `--mui-primary-contrast`: o botão de visualização escolhido (Tarefas, Conexões, Webhooks; em Equipe, o ícone), o balão próprio e o selo "admin" do Chat Interno, o título do popup de notificações e o "marcar todas", e o cabeçalho da janelinha da chamada. Quem já pintava esses fundos com a cor da marca contando com o texto branco: defina `--mui-primary-contrast: #fff` (ou aponte as três `--mui-primary*` para a marca).
- Dashboard no celular: o "Filtrar por Conexão" desce para a linha de baixo, e a página não fica mais larga que a tela.

### 29.469.0

- O ramal SIP (décima leva, 1.1 a 1.8).
- A janela da chamada — a do receptor (`.custom-css-modal-sip-receiver`) e a do discador (`.custom-css-modal-sip-dialer`) — leva `data-call-status`, `data-call-direction`, `data-muted`, `data-on-hold` e `data-video`.
- O widget minimizado é `.custom-css-sip-widget` (com `data-call-status`, `data-muted` e `data-on-hold`), e o cabeçalho dele `.custom-css-sip-widget-header` — junto do `widget-header` que já existia.
- O `<body>` leva `data-sip-registration` e `data-sip-call`, e a `window` dispara o evento `sip:state` (ver Eventos) a cada mudança.
- O botão do ramal leva `data-status` (`connecting` · `connected` · `failed` · `disconnected`) e `data-in-call`; o `data-connected` continua.
- Os botões da chamada levam `data-sip` com a ação, nas duas janelas e no widget (o `abrir-teclado` do widget continua). O status e o cronômetro são `.custom-css-sip-status` e `.custom-css-sip-timer`.
- Os textos fixos do widget ("Chamando...", "Em chamada", "Mudo"…) passaram para o i18n (`sipWidget.*`), nos seis idiomas.
- Os botões Mudo e Espera do widget minimizado passaram a funcionar: as duas telas que o usam passavam as funções com outro nome, e o clique não fazia nada.

### 29.468.0

- As janelas e os comportamentos (décima leva, 9.1 a 9.8, 10.19 a 10.22, 10.24 e os extras 2.2 a 2.6).
- ⚠️ `.custom-css-modal-rating` SAIU da janela de avaliação (o cadastro de NPS, na página Avaliações): ela é só `.custom-css-modal-rating-form`. O `-rating` fica só no popup de encerrar (junto de `-rating-close`), e o desenho dele não vaza mais para o cadastro. Quem pintava o cadastro por `-rating` passa a usar `-rating-form`.
- ⚠️ No olho (`.custom-css-modal-espiar-conversa`), a nota interna e o registro do atendimento vêm SEM `data-fromme`, como na conversa aberta. Até aqui vinham com `true`, e toda regra de "mensagem minha" os pintava só no olho. Os balões do olho também ganharam `data-message-id`.
- ⚠️ No celular (abaixo de 600px), a latência saiu da barra do topo e virou item do menu do "+" (`[data-appbar="mais"]`), logo abaixo do idioma. O medidor leva `data-ping-ms` e `data-ping-status`.
- Janela da conexão, aba Setores & Tempos: `name`, `id` e o rótulo ligado nos campos "Após" (`selectedInterval`), "Mover" (`selectedMoveQueueId`), "Inatividade" (`inatividade`) e "Inatividade Sem Setor" (`inatividadeNQ`), e no "Arquivo de Capa" (`coverImage`), como já era no "Resposta na Volta". Valem também nas outras janelas que usam os mesmos campos (Docker, Chat Externo e Setor).
- Campo de mensagem (os dois compositores): `data-action="external-only"` com `aria-pressed` no "Somente chat externo"; `data-action="extras"` com `aria-expanded` no "+" do painel de extras; `data-action="fechar-extras"` no X desse painel.
- Criar Ticket (as quatro janelas: a do "+" do Quadro, a do atendimento, a alternativa e a da API oficial): `.custom-css-dialog-header` no cabeçalho e `.custom-css-dialog-footer` no rodapé. Ficam fora do prefixo `custom-css-modal-`, que é o NOME de cada janela.
- Menu `⋯` da barra do atendimento: o item de uma ação que é interruptor ("Permitir Áudio?") é `role="menuitemcheckbox"` com `aria-checked`. E o clique nele passou a ligar e desligar: antes fechava o menu sem fazer nada.
- Celular: `.custom-css-mobile-shell` no papel da tela de atendimentos. O painel "Selecionar ticket" é o mesmo `.custom-css-chat-empty` do computador, com `-texto` e `-acao`.
- Arquivos da Conversa: `.custom-css-ticket-files-resumo` na faixa "Total de arquivos / Página" e `.custom-css-ticket-files-miniatura` (com `data-media-type`) na miniatura de cada cartão. Janela de tarefa: `.custom-css-tarefa-contato` no cartão do contato.
- Anexar Arquivos (Hub): `.custom-css-file-upload-hub-item` (com `data-file-type`), `-remover`, `-legenda` e `-nome`.
- Cartão do ticket: `.ticket-collaborators` (com `data-count`) no selo dos convidados, e `--queue-color` (ver Propriedades) no cartão da lista e no do Quadro. Cabeçalho do atendimento: `.custom-css-ticket-info` no bloco do contato, e o nome inteiro em `data-full-name` e no `title` de `.ticket-title-name`.

### 29.467.0

- Tela a tela e o cartão de número (décima leva, 10.2, 10.8 a 10.18, 10.23 e 10.25).
- Cartão de número: `.custom-css-stat-card` (com `data-stat`) e as partes `-icone`, `-rotulo`, `-valor` e `-detalhe` em 81 cartões de 19 telas. ACRESCENTADO nos que já tinham classe — `.custom-css-kanban[-team|-filas|-grupos]-stat-card` e o `.custom-css-dash-card` do Pipeline e dos cartões de status do Dashboard continuam; o `.custom-css-dash-card` segue servindo aos três tipos (status, navegação e Pipeline), e agora o `data-stat` e o `data-dash-view` os separam.
- Quadro: `.custom-css-quadro-embrulho`, `.custom-css-quadro-barra` (junto do `.custom-css-page-header`), e, no cabeçalho da coluna, `-coluna-cor`, `-coluna-titulo` e `-coluna-contagem`.
- Kanban: a cor da etapa vai também na COLUNA, em `--lane-color` (ver Propriedades); o cabeçalho continua com a cor dele. No cartão: `.custom-css-kanban-card-id` (o `#3930`) e `.custom-css-kanban-card-status` com `data-ticket-status`, que também passa a existir no cartão inteiro — os mesmos nomes nos quatro Kanban.
- Chat Interno: `.custom-css-chats-lista`, `-conversa`, `-cabecalho`, `-btn-nova`, `-item` (com `data-chat-id`, `data-unread`, `data-unread-count` e `aria-current`), `-msg` (com `data-fromme`, junto do `data-apagada` que já existia), `-conversa-cabecalho`, `-mensagens` e `-composer`.
- Tarefas: `.custom-css-todolist-filtros` e `.custom-css-task-card` (com `data-prioridade`, `data-status` e `data-atrasada`). Agendamentos: `.custom-css-agenda-dia` (com `data-dia`, `data-hoje`, `data-outro-mes` e `data-total`), `.custom-css-agenda-navegacao` e `.custom-css-agenda-evento` (com `data-status`) nas três visualizações.
- Listas: `data-contact-id` na linha de Contatos e `.custom-css-contact-status` (com `data-status`) no chip; `.custom-css-tag-card`, `-quickmessage-card`, `-product-card`, `-oportunidade-card`, `-queue-card` e `-category-card`, cada um com o id do item; na Pesquisar, `data-ticket-id` na linha e no cartão do celular (`.custom-css-atendimentos-cartao`), e `.custom-css-atendimentos-resumo` (com `data-resumo`) nos blocos do topo.
- Dashboard: `.custom-css-dashboard-secao` nos títulos de seção, `data-status` nos cartões de status e `.custom-css-dashboard-painel` (com o `data-dash-view` do cartão que o abre) nos blocos de cada seção. Configurações: `.custom-css-settings-secao` com `data-settings-secao` em cada uma das 35 seções — e o mesmo `data-settings-secao` na faixa dela. Webhooks: `.custom-css-webhooks-visualizacao` no grupo dos botões de visualização.
- Conexões: o selo do modo da conta Meta (o "LIVE") é `.custom-css-connection-badge`, com `data-badge` e `data-nivel`. Criar Template: `.custom-css-waba-template-form-cabecalho`, `-corpo`, `-previa`, `-rodape`, `-etapas` e `-etapa` (com `data-etapa` e `aria-current="step"`). Editor de fluxo: `.custom-css-flow-busca` (e `-busca-campo`), `-painel-esquerdo`, `-painel-direito` e `-minimapa-rotulo`.
- Pesquisar: `.custom-css-atendimentos-filtros` no bloco e `.custom-css-atendimentos-filtro` com `data-filtro` em cada um dos 15 filtros (`-filtro-data-por` e `-filtro-valor-minimo` continuam). ⚠️ O ÚNICO item desta build que muda o desenho: todos os filtros passam a ter o mesmo respiro (`0 10px 10px`). Origem, Tags, Contato, Encerramento e Incluir transferências perdem os 10px de cima — era o que desalinhava os campos no tablet. Quem compensava isso por CSS pode tirar o ajuste.
- Atributos com lugar novo, e o valor de sempre: `data-status`, `data-atrasada`, `data-dia`, `data-chat-id`, `data-unread`, `data-unread-count`, `data-fromme`, `data-ticket-status`, `data-ticket-id`, `data-contact-id`, `data-tag-id`, `data-tag-color`, `data-queue-id`, `data-queue-color`, `data-lane-type`, `data-nivel`, `data-etapa` e `data-dash-view` — os lugares e os valores novos estão na tabela. Nada foi trocado nem renomeado.

### 29.466.0

- Convenções para todas as telas (décima leva, 10.1 a 10.7).
- `.custom-css-page-header` ACRESCENTADO em elementos que já existiam: a barra do Quadro de Atendimentos (a do seletor e da busca), o cartão do título do Ranking de Vendas, o topo de Minha evolução, o topo da lista do Chat Interno (no computador e no celular), o cabeçalho do Dashboard e o cartão do título de Traduções. `.custom-css-page-title` ACRESCENTADO nos títulos de Minha evolução, do Dashboard e de Traduções. ⚠️ Regra escrita para `.custom-css-page-header` ou `.custom-css-page-title` passa a valer também nessas telas — era o pedido; quem as listava por nome pode encurtar a lista. O Dashboard legado continua sem cabeçalho: a tela não tem título.
- Id de página novo, no contêiner que já tinha a classe (nada foi trocado): `#custom-css-quadro-de-atendimentos` (junto do `.custom-css-quadro-pagina`), `#custom-css-minha-evolucao`, `#custom-css-crm-cadastros`, `#custom-css-crm-funis`, `#custom-css-crm-board`, `#custom-css-crm-ranking`, `#custom-css-crm-auditoria`, `#custom-css-relatorio-vendas`, `#custom-css-relatorio-anuncios`, `#custom-css-relatorio-rodizio`, `#custom-css-answer-from-ia`, `#custom-css-error-logs` e `#custom-css-consumo-de-voz`. O `#custom-css-relatorio-rodizio` citado na 29.414.0 era, até aqui, só classe; agora existe como id.
- Estado vazio: `.custom-css-empty-state` (com `data-empty`), `-icone`, `-titulo`, `-texto` e `-acao` nos 41 blocos "Nenhum … encontrado" de 35 telas. Acréscimo: as classes da plataforma continuam no mesmo elemento.
- O escolhido como atributo: `aria-pressed` e `data-view` nos botões de visualização (`.custom-css-view-toggle`) de Tarefas, Conexões, Equipe, Webhooks, Prompts e Agendamentos (Mês / Dia / Histórico — a classe `active` continua); `aria-pressed` e `role="button"` nos quatro cartões que filtram Contatos; `aria-expanded` e `data-dash-view` nos cartões de seção do Dashboard; `data-categoria` e `data-selected` no cartão de categoria do Criar Template (a classe `selected` continua). `data-filter` ganhou um segundo lugar (os filtros do histórico de Agendamentos, com `aria-pressed`) e `data-selected` também (o cartão de categoria), com valores próprios descritos na tabela. Quem achava o escolhido pela cor, com `mix-blend-mode`, pode aposentar o contorno.
- Menus das páginas: `.custom-css-page-menu` no papel de todos, com o nome próprio ao lado (`.custom-css-menu-conexoes-acoes`, `-menu-fluxo-acoes`, `-menu-contatos-importar-exportar`, `-menu-contato-acoes`, `-menu-saltos-do-fluxo`), e `data-menu-action` nos itens. O menu da mensagem do Chat Interno mantém `.custom-css-menu` e `.custom-css-menu-mensagem-chat-interno` onde estavam (na raiz, e não no papel) e ganha `.custom-css-page-menu` no papel. Conexões não tem ⋮ por cartão — o menu de lá é só o "Ações" do cabeçalho.
- Faixa em gradiente: `.custom-css-section-header` (`-icone`, `-titulo`, `-subtitulo`) nas faixas de Traduções, das 35 seções de Configurações, do Criar Template e das três janelas de Criar Ticket que têm faixa. ⚠️ O gradiente das seções de Configurações saiu do `style` inline e foi para `--section-header-gradiente`, lido pelo `background` da classe: o desenho é o mesmo, e agora uma regra sem `!important` o vence. Para trocar todas as faixas de uma vez: `--section-header-fundo` (ver Propriedades).

### 29.454.0

- Regras do quadro. Na barra do quadro de atendimentos, botão novo `.custom-css-quadro-btn-regras`, logo depois do de configurar (para todos, e não só para o gestor). Janela nova `.custom-css-modal-regras-do-quadro` (`.custom-css-regras-quadro-titulo`, `-corpo`, `-ajuda`, `-abas`, `-lista-minhas`, `-lista-equipe`, `-lista-equipe-travada`, `-regra` com `data-regra-id`, `data-regra-ativa` e `data-regra-travada`, `-btn-nova`, `-btn-executar`, `-btn-fechar`) e o editor de regra `.custom-css-modal-regra-do-quadro` (`.custom-css-regra-editor-*`, com cada condição em `.custom-css-regra-editor-condicao` e `data-condicao-tipo`).
- Card do quadro: na linha de cima, entre o nome do contato e o balão de não lidas, entra o ícone `.custom-css-quadro-card-regra` (com `data-regra-id`) quando uma regra pôs o card na coluna em que ele está. ⚠️ Quem acertou a largura do nome contando só com o balão ao lado: com o ícone, a linha perde mais uns 20px. Nada foi trocado nem renomeado.

### 29.453.0

- Pausar a conexão. `data-connection-status` ganhou o valor `paused` — no cartão da conexão, no cartão do ticket e no cabeçalho da conversa aberta. ⚠️ Regra que pintava de vermelho todo status diferente de `connected` agora pinta também a conexão pausada; para separar, use `[data-connection-status="paused"]` (a lista de atendimentos passou a pintá-la de amarelo, e não de vermelho).
- Cartão da conexão: botões `data-connection-action="pause"` e `"resume"` (só para admin, junto do editar) e a linha `.custom-css-connection-paused-since` ("Pausada desde"). Pausada, a conexão esconde os botões de sessão — importar e excluir sessão, e reiniciar a whatsmeow_pro.
- Atendimento aberto (e o modal que o quadro abre): faixa nova `.custom-css-ticket-conexao-pausada` acima do compositor, com `data-connection-status="paused"`. O compositor fica dentro de uma caixa que, fora da pausa, não existe para o layout (`display: contents`); na pausa ela ganha `.custom-css-compositor-travado`, com `inert` e `aria-disabled="true"`. Nada foi trocado nem renomeado.

### 29.452.0

- Editor de imagem, aberto pela janela de anexar do compositor do Hub. Janela nova `.custom-css-modal-editor-de-imagem` (com `data-ferramenta`, `data-alterada` e `data-carregando`), com a barra de cima `.custom-css-editor-de-imagem-topo` (`-fechar`, `-ferramentas`, `-ferramenta` com `data-ferramenta` e `data-ativa`, `-desfazer`, `-refazer`, `-concluir`), o palco `.custom-css-editor-de-imagem-palco` com a foto em `-tela`, a caixa de texto `-texto`, e a barra de baixo `.custom-css-editor-de-imagem-opcoes` (`-paleta`, `-cor` com `data-cor` e `data-ativa`, `-espessura`, `-tamanho`, `-dica`, `-girar`, `-redefinir`, `-cancelar-recorte`, `-aplicar-recorte`, `-editar-texto`, `-excluir`, `-texto-cancelar`, `-texto-pronto`). Os seletores de emoji e de figurinha abrem em `.custom-css-editor-de-imagem-emojis` e `.custom-css-editor-de-imagem-figurinhas`; a confirmação de descartar é `.custom-css-modal-confirmation-editor-de-imagem-descartar`.
- Janela de anexar do compositor do Hub (`.custom-css-modal-file-upload-hub`): cada imagem editável ganhou o botão `.custom-css-file-upload-hub-editar`, e a miniatura, `.custom-css-file-upload-hub-miniatura` (clicar nela também abre o editor). Nada foi trocado nem renomeado.
- `data-ativa` e `data-carregando` ganharam lugares novos no editor, com os valores de sempre (`true` · `false`).

### 29.442.0

- Chat Externo (página pública): layout novo, no desenho do WhatsApp Web — a lista de conversas (os protocolos do visitante com a empresa) à esquerda e a conversa à direita; no celular, uma coluna de cada vez. **`.custom-css-chat-app` mudou de papel**: deixa de ser a coluna única de 720px, centralizada, e passa a ser a moldura das duas colunas (com `data-tela` e `data-conversa`). Regra que limitava a largura dela agora aperta as duas colunas juntas.
- O topo da conversa (`.custom-css-chat-header`) fica claro, com texto escuro, como no WhatsApp Web (antes era verde, com texto branco), e ganhou a seta `.custom-css-chat-back` (só no celular). ⚠️ Quem pintou o fundo do topo de escuro precisa pôr também a cor do texto: `color` no `.custom-css-chat-header` e no `.custom-css-chat-subtitle` — sem isso, o texto escuro some no fundo escuro.
- A página ganhou tela de carregamento: `.custom-css-chat-loading`, com `-loading-logo`, `-loading-bar`, `-loading-text` e `-loading-footer`. `.custom-css-chat-screen` continua sendo a de erro e a de senha.
- Âncoras novas: `.custom-css-chat-sidebar`, `-sidebar-header`, `-sidebar-avatar`, `-sidebar-title`, `-list`, `-list-item` (com `data-protocolo`, `data-atual`, `data-encerrado`, `data-ativo`, `data-canal` e `data-nao-lidas`), `-list-avatar`, `-list-title`, `-list-channel`, `-list-time`, `-list-preview`, `-list-badge`, `-list-unread`, `-conversation`, `-history`, `-history-notice`, `-readonly` e `-readonly-button`. Nada foi renomeado.

### 29.439.0

- Encerramento com valor de venda. Janela nova do encerramento em 3 passos: `.custom-css-modal-encerramento` (com `data-etapa`), `.custom-css-encerramento-cabecalho`, `-etapas`, `-etapa` (com `data-etapa` e `data-estado`), `-busca`, `-tags`, `-tag` (com `data-selecionada` e `data-pede-valor`), `-vazio`, `-valor`, `-atalho` (com `data-atalho`), `-observacao`, `-resumo`, `-resumo-valor`, `-avaliacao`, `-saidas`, `-sucesso`, `-sucesso-texto`, `-rodape` e `-proximo`. As três saídas da Tela 3 reusam os `data-action` do popup de encerramento (`resolve-message`, `resolve-silent`, `resolve-rating`).
- Editar Tag: bloco de venda `.custom-css-tag-venda`, com `.custom-css-tag-venda-pedir-valor`, `-obrigatorio` e `-conta-como-venda` (aparece só com o tipo Encerramento).
- Pesquisa de atendimentos: filtros `.custom-css-atendimentos-filtro-data-por` e `-filtro-valor-minimo`, a célula `.custom-css-atendimentos-valor` (com `data-conta-como-venda`) e o rodapé `.custom-css-atendimentos-rodape-vendas`.
- Ranking do CRM v2: `.custom-css-crm-ranking-opcao-encerramento` (a opção do filtro de funil), `.custom-css-crm-ranking-fila`, `.custom-css-crm-ranking-conversao` (o cartão), `.custom-css-crm-ranking-linha-conversao` e `.custom-css-crm-ranking-funil-encerramento` (a linha do encerramento na quebra por funil).
- `data-estado` ganhou um segundo lugar (a etapa do indicador do encerramento, com valores próprios, descritos na tabela). Nada foi trocado nem renomeado.

### 29.438.0

- Documentação da API (Swagger): página nova `#custom-css-documentacao-api` na rota `/api-docs` (fora de qualquer menu), com `data-estado` e `data-idioma` na raiz e as âncoras `.custom-css-documentacao-api-topo`, `-titulo`, `-versao`, `-json`, `-idioma`, `-subtitulo`, `-estado` e `-swagger` (a caixa onde o Swagger UI desenha; o que há dentro dela é do Swagger, com as classes dele — `.swagger-ui`, `.opblock`…). Nada foi trocado nem renomeado.

### 29.434.0

- Minha evolução: o cartão da meta do mês ganhou `.custom-css-minha-evolucao-meta`, com `data-meta-batida` e `data-percentual-da-meta`, e a linha do vendido `.custom-css-minha-evolucao-vendido`. Nada foi trocado nem renomeado.

### 29.432.0

- `data-active` do item do menu lateral (e `.Mui-selected` e `aria-current="page"`, que andam juntos) passa a ser `true` em **um item só**. Em rota filha de outra que também está no menu (`/ratings/report` dentro de `/ratings`) os dois acendiam; agora só o mais específico. Nada foi trocado nem renomeado — quem escolhia "o `href` mais longo entre os acesos" por JS pode aposentar o contorno.

### 29.419.0

- Figurinhas (stickers). Tela nova `#custom-css-figurinhas` (`.custom-css-figurinhas-pastas`, `-pasta`, `-grade`, `-figurinha`, `-btn-nova-pasta`, `-btn-enviar`) e o seletor no compositor do Hub (`.custom-css-composer-figurinhas` no botão, `data-action="figurinhas"`, `data-aberto`; `.custom-css-figurinhas-seletor`, `-seletor-pastas`, `-seletor-pasta`, `-seletor-grade`, `-seletor-figurinha`, `-seletor-vazio`, `-seletor-gerenciar`). Atributos novos: `data-figurinha`, `data-animada`, `data-fora-do-padrao`, `data-ativa`; `data-pasta` e `data-carregando` ganharam um segundo lugar (valores descritos na tabela).
- Balão da mensagem: figurinha (`data-media-type="sticker"`, recebida ou enviada) passou a ser desenhada só como imagem (`.custom-css-msg-sticker`), sem botão de download e sem o nome do arquivo embaixo. Antes caía no ramo genérico de arquivo.

### 29.416.0

- Chat Externo (página pública): reações e respostas com citação. Âncoras novas `.custom-css-chat-quote`, `.custom-css-chat-reactions` / `-reaction`, `.custom-css-chat-actions-btn`, `.custom-css-chat-actions` / `-action-react` / `-action-reply`, `.custom-css-chat-reply-bar` / `-reply-cancel`. `data-id` e `data-reacted` ACRESCENTADOS na `.custom-css-chat-row`; `data-autor` ganhou o valor `ambos` (só na `.custom-css-chat-reaction`) e passou a existir também na `.custom-css-chat-quote`. Nada foi substituído.
- O balão (`.custom-css-chat-bubble`) passou a ficar dentro de uma coluna (balão + reações) ao lado do botão de ações: seletores descendentes (`.custom-css-chat-row .custom-css-chat-bubble`) continuam valendo; só `>` (filho direto) entre a linha e o balão deixaria de casar.
- A página do Chat Externo entrou neste catálogo, em seção própria lida do HTML. A tabela escrita à mão do Customizacao-CSS-JS.md saiu — estava duas âncoras atrás da página (`-pass` e `-aviso`).

### 29.414.0

- Tela nova: relatório do rodízio (`#custom-css-relatorio-rodizio`), com `data-flow-id`, `data-node-id` e `data-transbordos` no bloco de cada nó e `data-operator-id` / `data-fora-do-no` na linha de cada operador. `data-operator-id` já existia na linha do ranking; o valor é o mesmo (o id do operador).

### 29.413.0

- `data-queue-chatbot` e `data-queue-id` ACRESCENTADOS nos cards do quadro de atendimentos e dos quatro kanbans (`/kanban`, equipe, filas e grupos); `data-queue-chatbot` também no cartão de grupo e no cabeçalho da conversa aberta. Nada foi substituído — o cartão da lista continua exatamente como estava.
- `data-flow-status` e `data-bot-ativo` (novos) no cartão do ticket, no cartão de grupo, no cabeçalho da conversa aberta e nos cards do quadro e dos kanbans.
- `.custom-css-quadro-coluna-cabecalho`, `.custom-css-quadro-coluna-corpo` e `.custom-css-quadro-coluna-vazia` (novas) dentro da coluna do quadro, e `data-vazia` na própria `.custom-css-quadro-coluna`.
- Cartão do menu de Configurações ganhou `id="simple-tab-<aba>"`, `role="tab"`, `aria-selected`, `aria-controls="simple-tabpanel-<aba>"`, `data-settings-tab`, `data-active` e `.custom-css-settings-menu-item`; a lista dos cartões, `role="tablist"` e `.custom-css-settings-menu`. O anzol por texto do rótulo pode ser aposentado.
- `data-coluna-tipo` ganhou o valor `PENDENTE_FILA` (coluna automática por fila). `PENDENTE_LIVRE` existia desde a 29.410.0 e faltava nesta tabela.
- `data-regra="fila"` (novo) no ícone `.custom-css-quadro-coluna-regra`, no cabeçalho da coluna automática.
- Dezessete atributos que já estavam no código sem descrição aqui (o catálogo não era gerado desde 17/09) ganharam descrição: `data-answer-from-ia-camada`, `data-apagada`, `data-chat-id`, `data-emoji`, `data-fixado`, `data-forcar-hibrido`, `data-minha`, `data-mostra-encerrar`, `data-nota-id`, `data-pisca`, `data-pode-espiar`, `data-prefixo`, `data-prefixos`, `data-so-os-meus`, `data-so-sem-resposta`, `data-tem-contato`, `data-usuario-id`. Nada mudou neles nesta build — só passaram a existir no catálogo.
