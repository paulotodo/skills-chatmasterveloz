# Atualizações 10/11/2026

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-11-10
- **Categoria:** Recursos
- **Menu:** Atualizações › Novembro 2026 › Atualizações 10/11/2026

---

🧩 Atualizações de 10 de novembro de 2026.

Todas as novidades abaixo estão disponíveis a partir da versão **WS-29.939.0**. Para ver a sua, clique no ícone do perfil, no topo da tela: a versão aparece no fim do menu.

#### Novidades

⚡️ **Marca do produto:** no PDV, cada produto ganha o campo **Marca**, com sugestão das marcas que a empresa já usa. A lista de **Produtos** filtra e busca pela marca, e a planilha de produtos ganhou a coluna **Marca**.

⚡️ **Marca na Loja digital:** ainda no PDV, a Loja digital mostra a marca no card e na página do produto, com busca pela marca e o filtro **Todas as marcas**. O Cardápio digital não mostra a marca.

◽ **Moeda sem centavos:** ainda no PDV, ao trocar para uma moeda sem centavos, como o peso chileno, a tela avisa antes e arredonda os preços cadastrados (6,50 vira 7), e o preço que o cliente vê passa a ser o mesmo da conta e do troco. Os pedidos que já existem não mudam.

⚡️ **Mesas e situações na API:** na API, dá para listar as mesas e as comandas, com a conta aberta de cada uma, e as situações dos projetos, inclusive as criadas pela empresa.

#### Melhorias

☑️ **Opções por assunto:** no menu **Configurações  ›  Opções**, a tela vem em seções por assunto. As configurações são as mesmas, com os mesmos valores, mas mudaram de lugar. Cada seletor mostra o valor que está valendo, e os nomes falam em Atendimento e Setor.

☑️ **Token da OpenAI escondido:** no menu **Integrações**, o token da OpenAI vem escondido, com o olho para mostrar a chave.

☑️ **Intervalo até 24 horas:** no FlowBuilder Nativo, o bloco **Intervalo** espera de 1 segundo a 24 horas, em segundos, minutos ou horas, e acima de 2 minutos ganha a saída **Janela expirada**.

☑️ **Busca vazia no E-mail:** no E-mail, a busca sem resultado avisa que procura só nos e-mails que já vieram para a plataforma e oferece um botão para trazer os anteriores do servidor.

☑️ **Hora no Quadro de atendimentos:** no Quadro de atendimentos, a hora do card atrasado fica legível também no tema escuro.

☑️ **Mesas livres:** em Mesas e Comandas, as mesas sem conta aparecem como **Livres**, e a busca sem resultado diz o que conferir.

## Marca do produto

A janela **Adicionar Produto** ganhou o campo **Marca**, logo depois do **SKU (código do produto)**, com a ajuda *Opcional. A Loja digital organiza, busca e filtra pela marca.*

➡️ Ao digitar, o campo **Marca** sugere as marcas que a empresa já usa. A marca tem até 60 caracteres.

➡️ Na lista de **Produtos**, o card mostra *Marca: …* acima do SKU e do preço. O filtro **Marca** (**Todas**, **Sem marca** e cada marca) aparece quando já existe alguma marca, e a busca *Pesquisar produtos...* também acha pela marca.

➡️ A planilha de produtos tem a coluna **Marca**. Ao atualizar produtos pela planilha, a célula de marca em branco não apaga a marca que já existe.

## Marca na Loja digital

Na Loja digital, a marca aparece em maiúsculas acima do nome do produto, no card e na página do produto.

➡️ A busca *Buscar produtos, marcas e modelos* acha o produto pela marca.

➡️ O filtro **Todas as marcas** lista as marcas da loja em ordem alfabética.

➡️ O Cardápio digital não mostra a marca: ela não aparece no card nem na janela do produto, não há filtro de marca, e a busca do Cardápio não procura pela marca.

## Moeda sem centavos

No menu **Configurações  ›  Opções**, na seção **Empresa e região**, escolher uma moeda sem centavos, como **Peso chileno (CLP)**, abre o aviso *Trocar para Peso chileno (CLP)?*, com o texto *Esta moeda não tem centavos. Os preços cadastrados com centavos (produtos, variações, adicionais, taxas de entrega e pedido mínimo) vão ser arredondados (6,50 vira 7). Os pedidos que já existem não mudam.*

➡️ **CANCELAR** mantém a moeda e os preços como estavam.

➡️ **OK** troca a moeda, arredonda os preços e avisa quantos cadastros mudaram, como *6 cadastros tiveram os preços arredondados.* O custo dos insumos não é arredondado.

➡️ No Cardápio digital, o preço que o cliente vê passa a ser o mesmo da conta e do troco.

➡️ Os pedidos que já existem continuam com o mesmo total.

➡️ Voltar para o real não traz os centavos de volta: os preços continuam arredondados.

## Mesas e situações na API

Na API, duas listas novas ajudam quem integra a plataforma com outro sistema.

➡️ **Listar as mesas e as comandas** (`GET /api/pdv/mesas`): cada mesa vem com o nome, o número, o tipo (mesa ou comanda), se está ativa e a conta aberta, na ordem da tela. A mesa livre vem sem conta aberta. A lista filtra por tipo e por mesa ativa, e o `id` de cada mesa é o mesmo usado nas reservas de mesa.

➡️ **Listar as situações dos projetos** (`GET /api/projetos/situacoes`): cada situação vem com a chave, o nome, a cor e se é uma situação padrão, na ordem do quadro de Projetos. A situação criada pela empresa vem com `padrao: false`, e a chave dela também serve para filtrar a lista de projetos. Esta lista usa o token da empresa.

## Opções por assunto

No menu **Configurações  ›  Opções**, as configurações são as mesmas, com os mesmos valores: só mudaram de lugar, agora em seções por assunto. Nada precisa ser refeito.

➡️ As seções, na ordem da tela: **Empresa e região**, **Gerenciamento de Expediente**, **Atendimento e operador**, **Distribuição e rodízio**, **Transferências**, **Bot e FlowBuilder Nativo**, **Avaliações**, **Chamadas**, **Gerenciamento de Grupos**, **Contatos**, **Mensagens automáticas**, **Sons e Notificações**, **Carteiras de Clientes**, **PDV**, **Webhooks e integrações**, **CRM**, **Armazenamento Remoto de Arquivos**, **Segurança**, **Logs e Monitoramento** e **Configurações de Sistema**.

➡️ Alguns campos que mudaram de lugar: **Tipo de menu**, **Fuso horário da empresa** e **Moeda** ficam em **Empresa e região**; as opções do PDV ganharam a seção **PDV**; **Habilitar 2FA na empresa** fica em **Segurança**; e a mensagem de aniversário, em **Mensagens automáticas**.

➡️ Os seletores que apareciam em branco mostram o valor que está valendo, mesmo sem nunca terem sido mexidos, como **Marcar Como Lida** em *Ao Responder* e **Tempo de Concatenação** em *5 segundos*.

➡️ Os nomes falam em Atendimento e Setor, como *Abrir Atendimentos Fora do Expediente?*, *Operador Visualiza Atendimentos Fechados?* e *Informar a Posição no Setor?*.

➡️ O campo da mensagem de aniversário diz *Mensagem de Aniversário (enviada todos os dias às 10 horas, no fuso da empresa)*.

## Token da OpenAI escondido

No menu **Integrações**, no card **OPEN.AI**, o token vem escondido. O olho **Mostrar a chave** mostra o token, e **Esconder a chave** volta a esconder.

## Intervalo até 24 horas

No FlowBuilder Nativo, a janela *Editar bloco: Intervalo* tem **Tempo de espera** e **Unidade**: **Segundos**, **Minutos** ou **Horas**. O intervalo vai de 1 segundo a 24 horas; fora disso, a janela avisa *O intervalo vai de 1 segundo a 24 horas.*

➡️ No quadro do fluxo, o bloco **Intervalo** mostra o tempo de um jeito fácil de ler, como *⏱ 1 h 30 min*.

➡️ Acima de 2 minutos, o bloco **Intervalo** ganha a saída **Janela expirada**, para os canais em que a mensagem livre só pode ser enviada até 24 horas depois da última mensagem do cliente. A janela do bloco explica que, se a janela de 24 horas fechar durante a espera, o fluxo segue por essa saída e, sem ela ligada, para e deixa um aviso no atendimento.

➡️ A janela do bloco mostra quanto dessas 24 horas a espera usa, como *Esta espera usa 1 h 30 min das 24 horas da janela.*

➡️ O bloco **Intervalo** que já existia abre em segundos, com o tempo que já tinha.

➡️ O item **Intervalo** dentro do bloco **Conteúdo** continua com até 120 segundos.

## Busca vazia no E-mail

No **E-mail**, quando a busca não acha nada, abaixo de *Nenhum e-mail com "…" no assunto ou no remetente.* aparece o aviso *A busca procura nos e-mails que já vieram para a plataforma. Os mais antigos, ainda só no servidor, ficam de fora até serem trazidos.*

➡️ O botão **TRAZER OS ANTERIORES DO SERVIDOR** traz os e-mails anteriores, um lote por clique, e refaz a busca.

➡️ Quando não há mais e-mails para trazer, o botão some e o aviso fica.

## Hora no Quadro de atendimentos

No **Quadro de atendimentos**, a hora de cada card segue a cor do tempo parado: em dia, atenção e atrasado. No tema escuro, a hora do atendimento atrasado fica num vermelho mais claro, legível sobre o fundo escuro.

## Mesas livres

No menu **PDV  ›  Mesas e Comandas**, na aba **Mesas**, as mesas sem conta aparecem em **Livres**, com a contagem, como *Livres (5)*.

➡️ A busca sem resultado diz *Nada encontrado para "…".* e *Confira o que foi digitado ou limpe a busca.*, nas abas **Mesas** e **Comandas**.

➡️ Sem busca e sem nenhuma conta aberta, a aba diz *Nenhuma mesa com conta aberta agora.*

#### O que você precisa fazer

➡️ Quem administra: vale passar os olhos no menu **Configurações  ›  Opções**, porque as configurações mudaram de lugar. Nada precisa ser refeito.

➡️ Quem vende em moeda sem centavos: confira os preços que foram arredondados. Voltar para o real não traz os centavos de volta.

O resto não exige ação.
