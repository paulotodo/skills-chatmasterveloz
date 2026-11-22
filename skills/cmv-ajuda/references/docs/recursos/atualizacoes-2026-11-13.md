# Atualizações 13/11/2026

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-11-13
- **Categoria:** Recursos
- **Menu:** Atualizações › Novembro 2026 › Atualizações 13/11/2026

---

🧩 Atualizações de 13 de novembro de 2026.

Todas as novidades abaixo estão disponíveis a partir da versão **WS-30.15.0**. Para ver a sua, clique no ícone do perfil, no topo da tela: a versão aparece no fim do menu.

#### Novidades

⚡️ **Avisos ao cliente nos Projetos:** em **Projetos**, o botão **AVISOS AO CLIENTE** liga uma mensagem para cada situação do projeto, e o cliente recebe a mensagem quando o projeto entra naquela situação.

☑️ **Filtros da lista de projetos:** ainda em **Projetos**, o responsável, a situação e a busca continuam escolhidos ao sair da tela e voltar, enquanto a aba do navegador estiver aberta.

⚡️ **Alertas da Avaliação pela IA por usuário:** em **Equipe**, o cadastro de cada usuário tem, na aba **Permissões**, o campo **Alertas da Avaliação pela IA**.

☑️ **Rodadas da Avaliação pela IA:** no menu **Configurações  ›  Opções**, na seção **Avaliações**, aparece quando é a próxima rodada e, depois de cada rodada, o resultado dela.

☑️ **Mensagens seguidas na IA do Setor:** quando o cliente manda várias mensagens curtas, uma logo atrás da outra, a IA do Setor junta as mensagens e responde uma vez só, ao pedido inteiro.

◽ **Áudio no WebChat e no Chat Externo:** a IA do Setor responde ao que o cliente falou no áudio.

◽ **Nome da IA no balão:** o balão da mensagem deixa de repetir o *(IA)* quando o nome da IA já termina em IA.

◽ **Avaliação sem repetição:** cada atendimento é avaliado uma vez só, mesmo quando várias pessoas pedem a avaliação ao mesmo tempo.

⚡️ **Quem vê qual agenda:** no **Consultório**, a aba **Quem vê qual agenda** escolhe, para cada usuário, as agendas que ele enxerga.

☑️ **O que o lembrete faz:** ainda no Consultório, você escolhe o que acontece quando o lembrete é enviado e o que fazem os botões **Cancelar** e **Remarcar**.

☑️ **Webhook do Consultório:** o sistema da clínica tem 15 segundos para responder a cada aviso.

#### Melhorias

☑️ **Opções em sete abas:** no menu **Configurações  ›  Opções**, as opções ficam em sete abas por assunto, com busca, um endereço próprio para cada aba e seção, e um índice no topo da aba **Vendas**.

☑️ **Janela da oportunidade mais larga:** no CRM, a oportunidade abre numa janela mais larga, e a tabela de itens rola para o lado em vez de cortar colunas.

☑️ **QR Code sem recarregar:** em **Conexões**, ao conectar um WhatsApp por QR Code, o card da conexão passa sozinho para **QR Code**, sem recarregar a página. O card fica verde assim que o login é confirmado e avisa para reconectar quando o login não completou.

☑️ **Pesquisa mais rápida:** a pesquisa de atendimentos fica mais rápida em períodos longos e com muitos filtros.

#### Correções

◽ **Pizza com Preço Delivery:** no PDV, o site mostra cada sabor com a diferença do **Preço Delivery** do tamanho, e o *a partir de* mostra o preço da pizza mais barata que dá para pedir. Mesa e Balcão seguem no preço de venda.

◽ **Estoque pela API com o autor:** o lançamento de estoque pela API devolve o nome de quem lançou.

## Avisos ao cliente nos Projetos

Em **Projetos**, o botão **AVISOS AO CLIENTE** fica no topo da tela, entre **SITUAÇÕES** e **MODELOS**. A configuração vale para a empresa toda, e quem tem o botão é o administrador e o supervisor.

➡️ **Enviar pela conexão** escolhe por onde a mensagem é enviada. Vazio, ela vai pela conversa do cliente: a aberta, a última ou a conexão padrão.

➡️ Cada situação tem a sua chave, **Avisar quando entrar em "Planejamento"**, **"Em andamento"**, **"Pausado"** e **"Concluído"**. Ligada, ela abre a **Mensagem** daquela situação.

➡️ A mensagem aceita os dados do projeto: `{{cliente}}`, `{{projeto}}`, `{{etapa}}` (o nome da situação), `{{responsavel}}` e `{{prazo}}`.

➡️ Quando o projeto entra numa situação com a chave ligada, o cliente recebe a mensagem dela. Mover o projeto para a situação em que ele já está não envia de novo; se ele sair dela e voltar, a mensagem é enviada outra vez.

## Filtros da lista de projetos

Na lista de **Projetos**, o **Responsável**, a **Situação** e a busca escolhidos continuam valendo quando você vai para outra tela e volta, e também depois de recarregar a página. Numa aba nova do navegador, ou com o navegador fechado e aberto de novo, a lista volta a mostrar todas as situações e todos os responsáveis.

## Alertas da Avaliação pela IA por usuário

No menu **Equipe**, ao editar um usuário, a aba **Permissões** tem o campo **Alertas da Avaliação pela IA**. Ele escolhe quais alertas de nota baixa ou de atendimento fora do processo aquela pessoa recebe.

➡️ As opções são **Padrão do perfil**, **Todos os atendentes**, **Só os meus** e **Nenhum**.

➡️ No **Padrão do perfil**, o administrador e o supervisor recebem os alertas da equipe, menos os próprios, e os outros perfis não recebem.

➡️ **Todos os atendentes** vale só para administrador e supervisor.

## Rodadas da Avaliação pela IA

No menu **Configurações  ›  Opções**, aba **Automação**, seção **Avaliações**, logo abaixo de **Horários das rodadas**, aparece a **Próxima rodada**, com data e hora.

➡️ Depois de cada rodada, a linha mostra quando ela foi, quantos atendimentos foram avaliados, quantos ficaram sem conversa para avaliar e quantos falharam, com o motivo da falha.

## Mensagens seguidas na IA do Setor

Quando o cliente escreve em pedaços, uma mensagem logo atrás da outra, como *quanto custa*, *500 cartões* e *de visita?*, a IA do Setor junta as mensagens e responde uma vez só, ao pedido inteiro.

## Áudio e nome da IA

➡️ No WebChat e no Chat Externo, o áudio do cliente é transcrito e a IA do Setor responde ao que ele falou.

➡️ Um prompt chamado *Bia IA* aparece no balão da mensagem como *Bia IA*, sem o *(IA)* depois do nome. O *(IA)* continua quando o nome do prompt não termina em IA.

## Quem vê qual agenda

No menu **Consultório  ›  Cadastros**, a aba **Quem vê qual agenda** escolhe, para cada usuário, as agendas que ele enxerga: **Todas**, **Só a minha**, **Estas** (as agendas marcadas, ao menos uma) ou **Nenhuma**. O administrador vê todas.

➡️ Fora das agendas liberadas, a agenda, os pacientes, o prontuário, os documentos e as cobranças não aparecem para o usuário, nem pela busca, nem pelo endereço.

## O que o lembrete faz

No menu **Consultório  ›  Cadastros**, aba **Confirmação**, a parte **Ao enviar** decide o que acontece quando a confirmação e o lembrete são enviados:

➡️ **Atendimento:** **Não abrir atendimento** envia a mensagem e não abre nada até o paciente responder. **Aguardando** e **Em atendimento** abrem o atendimento no Setor, já nessa situação.

➡️ **Quando o paciente responder, mandar para o setor:** a resposta ao lembrete vai para esse Setor, por 7 dias depois do envio.

➡️ Em **O que cada botão faz**, **Cancelar: perguntar antes se o paciente tem certeza** faz o paciente confirmar antes de cancelar, e **Remarcar: abrir o atendimento no setor** leva o paciente ao Setor, com a consulta ainda marcada, para combinar o novo horário.

## Opções em sete abas

No menu **Configurações  ›  Opções**, as opções ficam em sete abas por assunto: **Geral**, **Atendimento**, **Contatos**, **Automação**, **Chamadas**, **Vendas** e **Integrações e segurança**.

➡️ **Pesquisar opção** acha a opção pelo nome, mesmo digitado sem acento: *concatenacao* acha *Concatenação*. Cada resultado mostra *Aba › Seção › Campo*, e o clique leva direto à opção, em destaque.

➡️ Cada aba e cada seção tem um endereço próprio. Para mostrar uma opção a quem vai configurar, copie o endereço do navegador e mande.

➡️ A aba **Vendas** tem um índice no topo, com os assuntos dela.

## Janela da oportunidade mais larga

No CRM, a janela da oportunidade ficou mais larga e, com os comentários abertos na lateral, ocupa quase a tela toda. A tabela dos itens da proposta rola para o lado quando não cabe, em vez de cortar colunas.

## QR Code sem recarregar

Em **Conexões**, logo depois de criar uma conexão de WhatsApp por QR Code, o card passa sozinho de **Desconectado** para **QR Code**, com o botão **VER QR CODE**, sem recarregar a página.

## Pizza com Preço Delivery

No site do Cardápio digital, cada sabor já aparece com a diferença do **Preço Delivery** do tamanho. Com a Média a R$ 40,00 e o Preço Delivery dela a R$ 44,00, a Calabresa de R$ 42,00 aparece por R$ 46,00, e a Portuguesa de R$ 46,00, por R$ 50,00.

➡️ O *a partir de* mostra o preço da pizza mais barata que dá para pedir naquele canal: R$ 46,00 no site e R$ 42,00 na mesa.

➡️ A mesa e o Balcão continuam no preço de venda.

## Estoque pela API com o autor

O lançamento de entrada ou saída de estoque pela API devolve, na resposta, o usuário que lançou, com o id e o nome. O histórico do estoque traz o mesmo usuário.

#### O que você precisa fazer

➡️ Para avisar o cliente pelos Projetos: em **AVISOS AO CLIENTE**, ligue as situações que devem avisar, escreva a mensagem de cada uma e escolha a conexão.

➡️ Se alguém da equipe deve receber alertas da Avaliação pela IA diferentes do padrão do perfil: escolha no menu **Equipe**, no cadastro do usuário, aba **Permissões**.

➡️ Para achar uma opção: use **Pesquisar opção** no menu **Configurações  ›  Opções**.

O resto não exige ação.
