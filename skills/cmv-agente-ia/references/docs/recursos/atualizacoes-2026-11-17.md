# 17/11/2026

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-11-17
- **Categoria:** Recursos
- **Menu:** Atualizações › Novembro 2026 › 17/11/2026

---

🧩 Atualizações de 17 de novembro de 2026.

Todas as novidades abaixo estão disponíveis a partir da versão **WS-30.70.0**. Para ver a sua, clique no ícone do perfil, no topo da tela: a versão aparece no fim do menu.

#### Novidades

⚡️ **Avisos e automações nos Links de agendamento:** em cada link, a marcação já põe a conversa do cliente no Setor escolhido, com as tags, cria a oportunidade no CRM e envia até 10 avisos pelo WhatsApp: ao marcar, antes, no dia e depois da reunião.

⚡️ **Avisos das tarefas ao cliente:** em **Tarefas**, o cliente é avisado pelo WhatsApp quando a tarefa é criada e antes do horário, também quem ainda não tem cadastro.

⚡️ **Unidades responsáveis:** no CRM, a oportunidade pode ter mais de uma unidade, e a empresa escolhe como essa venda conta nas metas e no Ranking das unidades.

⚡️ **Login automático:** nas Configurações, para quem liga a plataforma a outro sistema, o outro sistema abre o painel já logado, também dentro de uma janela embutida.

#### Melhorias

☑️ **Assistente de IA em tabela:** o **Assistente de IA** responde de novo em tabela, com a contagem de linhas e **EXPORTAR CSV**, com os números do momento e sem símbolos de formatação.

☑️ **Provedor de IA:** no menu **Integrações**, escolher o provedor com o campo **Modelo** vazio já preenche o modelo, e o Assistente de IA diz o que falta quando não responde.

☑️ **Remarketing da tag no atendimento encerrado:** no Atendimento, a mensagem do remarketing é enviada e o atendimento continua encerrado até o cliente responder.

☑️ **Remarketing vencido:** ainda no Atendimento, o remarketing vencido há mais de um dia não é mais enviado.

☑️ **Janela do Instagram e do Facebook:** a conversa explica quando o Instagram ou o Facebook não deixam responder.

◽ **Despedida obrigatória fora da janela:** no Instagram e no Facebook, com a janela de mensagens fechada, o atendimento encerra normalmente, e a despedida vira uma nota na conversa.

☑️ **Pesquisa de atendimentos:** a **Pesquisa de atendimentos** ficou mais rápida e avisa quando a busca demora demais, para você reduzir o período.

◽ **Áudio com qualquer nome:** o áudio com acento, espaço ou símbolo no nome do arquivo é enviado.

#### Correções

◽ **Uma notificação por entrada no Setor:** pela API, o sistema da empresa recebe uma notificação só por entrada no Setor, e só quando o atendimento muda de Setor de fato.

## Avisos e automações nos Links de agendamento

No menu **Links de agendamento**, a janela de cada link ganhou a seção **Avisos e automações**, que diz o que acontece quando o cliente marca a reunião.

➡️ **Conexão dos avisos:** a conexão por onde os avisos são enviados. Vazia, vale a conversa do cliente ou a conexão padrão.

➡️ **Setor da conversa** e **Tags da conversa:** a conversa do cliente ganha o Setor e as tags ao marcar. A resposta do cliente cai nesse Setor, sem tirar a conversa de quem já a atende.

➡️ **Oportunidade no CRM** e **Etapa:** a oportunidade nasce nesse funil e nessa etapa, com o cliente e quem atende, e a reunião vira uma atividade dela.

➡️ **Avisos ao cliente:** até 10 avisos, cada um com o seu texto, em quatro momentos: **Ao marcar**, **Antes da reunião**, **No dia, a uma hora** e **Depois da reunião**. O texto aceita as variáveis da reunião, como a data, a hora e o link da sala. Sem nenhum aviso, o cliente só vê a confirmação na página.

➡️ Se a reunião for remarcada, os lembretes acompanham o horário novo.

➡️ Com uma conexão oficial, o aviso pode usar um modelo aprovado, para chegar fora da janela de 24 horas.

## Avisos das tarefas ao cliente

➡️ No menu **Tarefas**, o botão **AVISOS AO CLIENTE**, do administrador, abre a janela **Avisos das tarefas ao cliente**: a conexão por onde os avisos são enviados e os textos de **Quando a tarefa é criada** e de **Antes do horário**, que já vêm prontos.

➡️ Na tarefa, **Avisar o cliente pelo WhatsApp** liga o aviso. O cliente é um **Contato cadastrado** ou um **Contato novo**, só com o nome e o WhatsApp.

➡️ **Avisar ao criar a tarefa** e **Avisar antes do horário** já vêm marcados. O lembrete vai de 15 minutos a 1 dia antes do horário.

➡️ Na tarefa já criada, cada aviso mostra quando foi enviado.

## Unidades responsáveis no CRM

➡️ Na oportunidade, aba **Dados Gerais**, o campo **Unidades responsáveis** aceita mais de uma unidade, com o atalho **Selecionar todas**.

➡️ No menu **Configurações  ›  Opções**, aba **Vendas**, a opção **Venda em várias unidades conta** escolhe como essa venda entra nas metas e no Ranking das unidades: **O valor inteiro em cada unidade**, **O valor dividido igualmente entre elas** ou **Só na primeira unidade escolhida**.

➡️ O bloco **Oportunidade** do FlowBuilder também escolhe as unidades responsáveis.

## Login automático

No menu **Configurações  ›  Opções**, aba **Integrações e segurança**, a seção **Segurança** ganhou o bloco **Login automático (integrações e iframes)**, para quem liga a plataforma a outro sistema.

➡️ **Ligar o login automático** deixa o outro sistema abrir o painel já logado, também dentro de uma janela embutida. Quem entra vê o painel com as permissões dele e passa pelas mesmas regras do login.

➡️ **Link de uso único (recomendado):** o servidor do outro sistema pede o link pela API, com o token da empresa, e abre o endereço recebido. O link vale uma vez só e expira em 60 segundos, ou no prazo pedido, até 5 minutos.

➡️ **Permitir também o link fixo (chave + e-mail):** para quando o outro sistema não consegue pedir o link de uso único. Quem vir o link fixo entra no painel daquele usuário; se a chave vazar, **TROCAR A CHAVE** faz os links com a chave antiga deixarem de entrar.

## Assistente de IA em tabela

➡️ Toda resposta de lista do **Assistente de IA** vem com a tabela abaixo do balão, a contagem de linhas e **EXPORTAR CSV**.

➡️ Os números são os do momento, e o texto vem sem símbolos de formatação.

➡️ A tela de entrada diz sobre o que dá para perguntar.

## Provedor de IA

➡️ No menu **Integrações**, card **Provedor de IA**: com o campo **Modelo** vazio, escolher o provedor já preenche o modelo dele.

➡️ Fora do provedor padrão, o **Modelo** é obrigatório.

➡️ Quando o **Assistente de IA** não responde, o aviso diz o que falta, como o campo **Modelo** vazio ou a chave recusada pelo provedor, e onde conferir.

## Remarketing da tag no atendimento encerrado

➡️ Quando a tag vence com o atendimento encerrado, a mensagem do remarketing é enviada e o atendimento continua encerrado. Ele volta para **Aguardando** quando o cliente responde.

➡️ Nos **Logs de Remarketing**, esse disparo aparece como silencioso: o atendimento fica encerrado até o contato responder.

## Despedida obrigatória fora da janela

➡️ No Instagram e no Facebook, com a despedida obrigatória e a janela de mensagens fechada, o atendimento encerra normalmente.

➡️ A despedida que não pode ser enviada vira uma nota na conversa, que explica por quê e pede para aguardar o contato responder.

## Uma notificação por entrada no Setor

Os webhooks da conexão e do Setor avisam o sistema da empresa uma vez só por entrada no Setor, e só quando o atendimento muda de Setor de fato. Antes, a entrada chegava em dobro.

#### O que você precisa fazer

➡️ Para avisar o cliente das tarefas: no menu **Tarefas**, o administrador confere os textos em **AVISOS AO CLIENTE**, e a equipe liga **Avisar o cliente pelo WhatsApp** em cada tarefa.

➡️ Para os avisos dos Links de agendamento: no menu **Links de agendamento**, abra cada link e preencha **Avisos e automações**.

➡️ Com venda de várias unidades: escolha a regra em **Venda em várias unidades conta**, no menu **Configurações  ›  Opções**, aba **Vendas**.

➡️ O login automático é só para quem integra outro sistema: fica no menu **Configurações  ›  Opções**, aba **Integrações e segurança**.

O resto não exige ação.
