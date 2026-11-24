# Planos em Configurações

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/configuracoes-planos
- **Categoria:** Recursos
- **Menu:** Configurações › Planos em Configurações

---

🧩 No card **Planos** você monta os pacotes que as suas empresas assinam. É o plano que decide quantos usuários, conexões e Setores ela pode ter, quanto paga, e quais recursos aparecem no menu dela.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações** e clique no card **Planos**.
>
> ➡️ Preencha **Dados do Plano**, ajuste os limites por canal se precisar, marque as opções e clique em **Salvar**. **Limpar** esvazia o formulário.
>
> ➡️ Para alterar um plano que já existe, clique no **lápis** no começo da linha.
>
> ⚠️ O formulário de um plano novo já vem com **WhatsApp**, **Campanhas**, **Agendamentos**, **Chat Interno**, **API Externa**, **Kanban** e **Uso Interno** marcados. Confira cada um antes de salvar — o **Uso Interno** decide se o plano aparece na lista da página de cadastro.

## Dados do Plano

🔘 **Nome:** o rótulo do plano.

🔘 **Usuários** e **Setores:** as quantidades máximas.

🔘 **Conexões:** o limite geral de conexões, que vale **para cada canal**, e não como total. Nas palavras da tela: *"Um plano com Conexões = 1 permite 1 WhatsApp e 1 Instagram e 1 Facebook, e assim por diante. Para impedir um canal, escreva 0 nele."*

🔘 **Valor:** o valor do plano.

## Limite de conexões por canal

Ajusta, canal a canal, quantas conexões o plano permite: **WhatsApp (não oficial)**, **WhatsApp Oficial (nativo)**, **HUB (NotificaMe)**, **Telegram (nativo)**, **Facebook (nativo)**, **Instagram (nativo)**, **TikTok (nativo)**, **WebChat**, **Chat Externo**, **RCS** e **E-mail**.

Nas palavras da tela: *"Em branco, o canal usa o limite geral de Conexões acima. Zero proíbe conectar aquele canal. O HUB é um contador só para todos os canais dele."*

## Canais de Comunicação

Define os canais que deseja habilitar ou desabilitar no Plano:

🔘 **WhatsApp:** o canal de WhatsApp não oficial.

🔘 **Telegram INC:** o canal nativo de Telegram.

🔘 **Facebook INC** e **Instagram INC:** o Facebook Messenger e o Instagram ligados pelo **seu próprio aplicativo**, aprovado na Meta.

🔘 **Instagram PORTAL** e **Facebook PORTAL:** os mesmos dois canais ligados pelo **aplicativo da plataforma**, sem precisar aprovar aplicativo nenhum na Meta.

🔘 **Automação Instagram:** habilita automações no Instagram, a seção **Automação** passa a aparecer ao editar uma conexão de Instagram no menu **Conexões**.

🔘 **Tiktok INC:** o canal nativo de TikTok.

🔘 **RCS:** o canal RCS.

🔘 **Provedores de IA:** libera o card **Provedor de IA** no menu **Integrações** da empresa. Nas palavras da tela: *"Escolha qual serviço de IA responde os prompts de chat."*

🔘 **Copilot CRM:** o copiloto das raias do CRM de múltiplos funis.

🔘 **Mobile Docker:** libera **Adicionar WhatsApp (sem aparelho celular)** no menu **Conexões**.

🔘 **Webchat:** o chat para o site da empresa.

🔘 **Chat Externo:** o canal Chat Externo — uma conexão própria, com página de entrada para o site, as redes ou um QR Code.

🔘 **Chamadas no chat interno:** chamadas de áudio e vídeo, com compartilhamento de tela, entre a equipe, nas conversas do **Chat Interno**.

🔘 **Videochamada com o cliente:** a videochamada aberta dentro do atendimento, com o link que o cliente usa para entrar.

🔘 **PDV:** o ponto de venda — produtos com estoque, pedidos montados na conversa, caixa, venda no balcão, painel de pedidos e entregas, com o perfil **Entregador** no cadastro de usuário. Para desmarcar o **PDV**, desmarque também o **Cardápio digital** e a **Loja digital**: com um dos dois marcado, o plano não salva.

🔘 **Cardápio digital:** a loja do PDV na internet — a página com o link e os QR Codes das mesas, onde o cliente faz o pedido. Só liga junto com o **PDV**. Traz também a página **Mesas e Comandas**, no menu **PDV**, o perfil **Garçom** e, no **Painel de pedidos**, a opção separada para os pedidos das mesas.

🔘 **Loja digital:** o catálogo online do PDV — a página com o link da loja e o de cada produto, com fotos e ficha técnica, onde o cliente faz o pedido ou deixa o interesse num produto. Só liga junto com o **PDV**.

🔘 **Consultório:** a agenda de consultas da clínica. Traz os menus **Agenda**, **Recepção**, **Pacientes** e **Cadastros do consultório**, com o prontuário, os documentos e receitas e a cobrança da consulta. Para a teleconsulta, a **Videochamada com o cliente** também precisa estar no plano: sem ela, nas palavras da plataforma, *"o serviço é presencial"*. Sem a opção **Consultório**, as telas do Consultório avisam *"O Consultório não faz parte do plano da sua empresa. Fale com o suporte para liberar."*

🔘 **Reservas:** a agenda de quem trabalha com hora marcada ou por diária — profissionais, mesas, salas, quartos e equipamentos. Traz os menus **Agenda de reservas**, para toda a equipe, e **Reservas**, para o administrador da empresa, com a página em que o cliente reserva sozinho, os avisos ao cliente, a lista de espera, os pacotes e o relatório. Sem a opção **Reservas**, as telas das Reservas avisam *"As Reservas não fazem parte do plano da sua empresa. Fale com o suporte para liberar."*

🔘 **E-mail:** o cliente de e-mail integrado.

🔘 **Notificame HUB:** os canais do hub — API Oficial, Instagram, Telegram e outros.

🔘 **WABA INC** e **WABA WL:** a API Oficial do WhatsApp — **WABA INC** pelo aplicativo da plataforma, **WABA WL** pelo seu próprio aplicativo aprovado na Meta.

⚠️ Cada canal oficial da Meta tem dois caminhos, e eles são alternativos: escolha um e não habilite os dois na mesma instância.

⚠️ A convenção do nome se inverte entre os canais: no WhatsApp o aplicativo próprio é o **WABA WL**, enquanto no Facebook e no Instagram o aplicativo próprio é o **INC**.

## Recursos do Sistema

Define os recursos que deseja habilitar ou desabilitar no Plano:

🔘 **Campanhas:** envio de mensagens em massa.

🔘 **Agendamentos:** agendar mensagens únicas.

🔘 **Chat Interno:** o chat entre os usuários da empresa dentro da plataforma.

🔘 **API Externa:** habilita as APIs (endpoints externos) do sistema — enviar mensagem, atualizar contato e as demais.

🔘 **Kanban:** todos os quadros Kanban.

🔘 **Usar Quadro de Atendimento:** habilita os quadros de Atendimentos.

🔘 **CRM:** o CRM — Board e oportunidades; com múltiplos funis quando a empresa está na versão 2.

🔘 **Projetos:** o módulo Projetos — o trabalho de cada cliente em etapas e tarefas, com equipe, prazo, checklist e modelos.

🔘 **Avaliação pela IA:** o módulo Avaliação pela IA — a nota de 0 a 10 dos atendimentos encerrados, o relatório e as aulas dos atendentes. Depois do plano, o administrador da empresa liga a avaliação no menu **Configurações  ›  Opções  ›  Automação**, seção **Avaliações**, opção **Avaliar os atendimentos pela IA**. Sem a opção, a página da avaliação avisa *"A avaliação pela IA não faz parte do seu plano."*

🔘 **Mail Marketing:** o módulo Mail Marketing — listas de contatos, modelos de e-mail e campanhas de e-mail em massa, agendadas, com relatório de aberturas e cliques. O menu **Mail Marketing** aparece para o administrador e o supervisor da empresa, e as campanhas são enviadas pelas contas de e-mail ativas dela, cadastradas no menu **Contas de E-mail**. Sem a opção, a tela do Mail Marketing avisa *"O Mail Marketing não faz parte do plano da sua empresa. Fale com o suporte para liberar."*

🔘 **FLOW:** o construtor de fluxos (FlowBuilder Nativo).

🔘 **Botões:** o envio de botões pela conexão não oficial.

🔘 **Ligações no Zap:** as ligações pelo WhatsApp na conexão não oficial. Necessário PABX.

🔘 **Ligações VOIP:** a integração com telefonia VoIP. Necessário PABX.

🔘 **Vídeo nas ligações:** a integração com vídeo nas ligações. Necessário PABX.

🔘 **Tarifador de Voz:** a cobrança por minuto das ligações — o que alimenta o menu **Consumo de Voz**.

🔘 **PUSH:** notificações pelo aplicativo instalável.

## Inteligência Artificial

Define os recursos de IA que deseja habilitar ou desabilitar no Plano. Fora desta seção ficam **Provedores de IA** e **Copilot CRM**, em **Canais de Comunicação**, e **Avaliação pela IA**, em **Recursos do Sistema**.

🔘 **AI:** a base da IA da empresa — o card **OPEN.AI** no menu **Integrações**, onde ela cadastra a chave da OpenAI, e, na janela do Setor, os campos **Prompt OPEN.AI (ChatGPT)** e **Ativar Transcrição de Áudio**.

🔘 **GPT Assistant:** a IA que responde o cliente — o menu **Prompts OPEN.AI**, que precisa também do **AI**, o campo **Prompt OPEN.AI (ChatGPT)** na janela do Setor e no contato de grupo, e o bloco **GPT Assistant** do FlowBuilder Nativo.

🔘 **GPT Análises:** no atendimento, o botão **Analisar Atendimento com IA** e o **Resumo do período**; e o menu **GPT Análises**, onde a empresa ajusta o prompt e o modelo da análise.

🔘 **Sugestão de resposta IA:** o **Copiloto de mensagens**, que sugere a resposta e melhora o texto no campo de mensagem, e o menu **Sugestão de resposta IA**, com o saldo em **Tokens de IA**.

🔘 **CHAMA.AI**, **ZAIA.APP** e **DIFY:** as integrações com esses serviços externos de IA.

## Automações e Integrações

Define as integrações que deseja habilitar ou desabilitar no Plano:

🔘 **Typebot / Flowise:** chatbots hospedados por você, ligados aos Setores.

🔘 **WPW:** rastreamento de mensagens pelo Pixel da Meta, via Tags ou FlowBuilder Nativo.

🔘 **Perfex**, **RD Station**, **CV CRM**, **IXC** e **HubSoft:** as integrações com esses sistemas — CRM, marketing e provedores de internet.

## Configurações Gerais

🔘 **Uso Interno:** decide se o plano aparece na lista de planos da página de cadastro de empresa pelo site. Nas palavras da tela: *"Ligado: o plano aparece na lista da página de cadastro. Desligado: o plano só é contratado pelo link de cadastro dele."*

## Link de cadastro

No plano já salvo, aberto pelo **lápis**, o bloco **Link de cadastro** mostra o endereço de cadastro daquele plano. Nas palavras da tela: *"Mande este link (ou ponha no botão "Contratar agora" da sua página de vendas): o cadastro abre com este plano já escolhido, sem a lista dos outros. Vale mesmo com "Uso Interno" desligado."*

🔘 **Copiar link:** copia o endereço do plano.

🔘 **Gerar novo link:** troca o endereço do plano por um novo. Ao gerar, a tela avisa *"Novo link gerado. O link anterior deixou de valer."*

## A tabela de Planos Cadastrados

🔘 Colunas **#**, **ID**, **Nome**, **Usuários**, **Conexões**, **Setores**, **Valor** e **Interno**.

O **lápis** abre o plano para edição e exclusão do plano.

⚠️ Excluir um plano com empresas nele deixa essas empresas sem plano. Altere os planos dessas empresas antes, no card de cada uma no menu **Configurações  ›  Empresas**.

## Monte seu plano

O bloco **Monte seu plano**, na tela de **Planos**, é a tabela de preços da página em que o próprio cliente escolhe o plano. Nas palavras da tela: *"A tabela de preços da página em que o cliente monta o próprio plano: o plano base, o valor de cada usuário, conexão e setor a mais, os módulos à venda e as taxas de implantação. Quem se cadastra por ela ganha um plano só da empresa dele."*

🔘 **Página ligada:** liga a página em que o cliente monta o plano, no endereço da plataforma terminado em `/monte-seu-plano`. Com a página desligada, quem abre esse endereço vê *"Página indisponível — A montagem de planos pelo site não está disponível no momento."*

🔘 **Plano base:** o **Valor mensal do plano base**, quantos **Usuários**, **Conexões** e **Setores** ele já inclui e os **Módulos que já vêm no plano base**.

🔘 **Adicionais e limites:** o valor de cada usuário, conexão e Setor adicional, e o máximo de usuários, conexões e Setores que o cliente pode escolher.

🔘 **Módulos à venda:** os módulos que o cliente pode somar ao plano. **Adicionar módulo** inclui mais um na lista.

🔘 **Taxa de implantação:** nas palavras da tela, *"Cobrada uma vez, na primeira fatura, junto com a primeira mensalidade. Deixe 0 para não cobrar."*

O bloco **Monte seu plano** grava pelo próprio botão, **Salvar tabela**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Marquei a opção no plano e a empresa não visualiza o menu.** Quem já estava com a plataforma aberta precisa recarregar a página. Se ainda assim não aparecer, o recurso pode exigir configuração além do plano — o caminho de cada um está na seção **Como Habilitar**.
>
> **Ao salvar o plano, aparece "Não foi possível confirmar a licença dos módulos…".** O servidor de licenças não respondeu a tempo, e nada foi alterado no plano. Clique em **Salvar** de novo em instantes.
>
> **Preenchi o limite do canal e o cliente continua sem ele.** O número só diz a quantidade. Enquanto a opção daquele canal estiver desabilitada, o canal não existe para o plano.
>
> **Por que o meu plano não aparece na lista da página de cadastro?** Confira o **Uso Interno** do plano. Pela ajuda da tela, só o plano com o **Uso Interno** ligado aparece na lista; desligado, ele só é contratado pelo **Link de cadastro** dele.
>
> **Como mando a um cliente um plano que não está na lista da página de cadastro?** Abra o plano pelo **lápis** e clique em **Copiar link**, no bloco **Link de cadastro**. Pela ajuda da tela, o link abre o cadastro com o plano já escolhido e vale mesmo com o **Uso Interno** desligado.
>
> **Cliquei em Gerar novo link no Link de cadastro. Preciso mandar o endereço de novo?** Precisa: ao gerar, a tela avisa *"Novo link gerado. O link anterior deixou de valer."* Mande o endereço novo a quem tinha o antigo.
>
> **Desmarquei o PDV no plano e ele não salva.** O **Cardápio digital** e a **Loja digital** só funcionam junto com o **PDV**. Desmarque os três e salve.
>
> **Devo criar um plano por cliente?** Não tem necessidade. O plano é o pacote; o que é de uma empresa (vencimento, recorrência, franquia de voz, bloqueios) fica no card dela.
