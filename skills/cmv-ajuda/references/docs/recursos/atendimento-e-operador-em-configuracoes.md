# Atendimento e operador em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/atendimento-e-operador-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Atendimento em Configurações › Atendimento e operador em Configurações

---

🧩 A seção **Atendimento e operador**, no menu **Configurações  ›  Opções  ›  Atendimento**, reúne o que o atendente pode ver e fazer no atendimento, a saudação e a despedida enviadas em nome dele e a assinatura das mensagens. Aqui estão todos os campos dela, na mesma ordem em que aparecem na tela. Use quando estiver olhando a configuração e quiser saber o que um campo específico faz.

Vale um aviso sobre alcance: todas as opções desta seção valem para **todos os atendentes da empresa ao mesmo tempo**. Não existe aqui ajuste pessoa a pessoa — isso é feito no cadastro de cada usuário, no menu **Equipe  ›  editar o usuário**, onde ficam o Tipo de Perfil e o Acesso Limitado. As duas camadas se somam, e a da empresa é a única que pode remover uma capacidade da função de atendente. A exceção é a despedida ao encerrar, que tem regra própria por atendente, por Setor e por Conexão (veja **Despedida obrigatória ao encerrar?**, abaixo).

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Atendimento**, seção **Atendimento e operador**.
>
> ➡️ Escolha o valor de cada opção. Ela grava assim que você muda, com o aviso *"Operação atualizada com sucesso."*

## Os campos, na ordem da tela

🔘 **Operador Visualiza Atendimentos Fechados?** — controla o acesso do atendente a atendimentos já encerrados.

🔘 **Operador Visualiza Históricos?** — define se o atendente consegue abrir atendimentos encerrados e ler o que foi conversado antes. Os atendimentos abertos em nome dele continuam acessíveis de qualquer forma.

🔘 **Operador Visualiza Grupos?** — em **Não**, as conversas de grupo de WhatsApp saem da lista do atendente.

🔘 **Operador Visualiza Notificação Global?** — define se os avisos gerais da plataforma chegam ao atendente.

🔘 **Operador Visualiza Prévias?** — em **Não**, o atendente deixa de ver o trecho da última mensagem ao lado de cada conversa na lista. Ele continua vendo que a conversa existe; deixa de ver o conteúdo dela sem abrir.

🔘 **Muda de Aba ao Aceitar o Atendimento?** — em **Sim**, quando o atendente aceita um atendimento a tela dele muda sozinha da aba **Aguardando** para a aba **Atendendo**, já com o atendimento aceito aberto.

🔘 **Operador Escolhe Conexão?** — em **Não**, o sistema define por qual Conexão a mensagem é enviada e o atendente não pode trocar. Faz diferença em empresas com mais de uma Conexão ativa.

🔘 **Operador Inicia Chat Interno?** — controla se o atendente pode iniciar conversa com colegas pelo chat interno da plataforma.

🔘 **Operador Acessa Todos os Atendimentos do Setor?** — em **Sim**, o atendente enxerga todos os atendimentos do **Setor** a que pertence, e não apenas os que estão em nome dele. Em **Não**, ele fica só com os seus.

🔘 **Tags de atendimento visíveis só para quem criou?** Ligado, cada atendente vê apenas as tags de atendimento que ele mesmo criou. Tags antigas, sem autor registrado, continuam visíveis para todos. Não afeta tags de CRM nem de Encerramento, e administrador e supervisor continuam vendo tudo. Ao lado do campo há o botão **VER IMPACTO**: ele mede, no banco da empresa, quantas tags e atendimentos mudariam de visibilidade **antes** de você ligar — e diz quantas tags somem ao ligar agora.

⚠️ Ligar não esconde nada do acervo antigo: a regra vale para as tags criadas daqui em diante. Para segregar o que já existe, cada tag precisa receber um dono na tela **Tags**.

🔘 **Operador Pode Espiar Conversa? (Olhinho)** — em **Não**, some o botão que permite abrir uma conversa em andamento apenas para leitura, sem assumir o atendimento.

🔘 **Botão de Comentário Interno Disponível?** — mostra ou esconde, para o atendente, o botão de comentário que o cliente não vê.

🔘 **Remover convidados ao finalizar o atendimento?** — vale para os operadores convidados a participar de um atendimento. Nas palavras da tela: *"Sim: ao finalizar, os operadores convidados saem da conversa e o registro do atendimento mostra a saída. Não: os convidados continuam na conversa."* A saída aparece no registro do atendimento quando **Registrar Logs de Ação dos Atendimentos?**, no menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Logs e Monitoramento**, está em **Sim**.

🔘 **Despedida obrigatória ao encerrar?** — nas palavras da tela: *"Sim: o atendente só encerra com a mensagem de despedida; a opção "sem despedida" some do atendimento. Os encerramentos automáticos do sistema seguem como estão."* Em **Sim**, o **Resolver sem Mensagem de Encerramento** deixa de aparecer na hora de encerrar; em **Não**, o atendente escolhe.

Esta opção é o último nível da regra da despedida. Antes dela vale o campo **Despedida ao encerrar** do cadastro do atendente, no menu **Equipe  ›  editar o usuário  ›  aba Geral**, do Setor (aba **Mensagens**) e, nas conexões de WhatsApp, da Conexão (aba **Mensagens**). Nas palavras da tela desse campo: *"Vale a primeira que não segue: a do usuário, a do setor, a da conexão; sem nenhuma, a da empresa (Opções)."* Ou seja, a opção da empresa decide quando os três estão em **Seguir…**.

### Saudação e despedida do operador

🔘 **Mensagem de Saudação do Operador?** — em **Sim**, uma mensagem é enviada automaticamente ao cliente no momento em que o atendente **aceita** o atendimento. O texto dessa mensagem vem do campo seguinte.

🔘 **Texto de Saudação** — o conteúdo da mensagem disparada pelo campo acima. Só tem efeito quando a saudação está ligada.

🔘 **Mensagem de Despedida por Operador** — habilita o envio de uma mensagem de despedida ao cliente.

### Assinatura

🔘 **Operador Pode Escolher Enviar a Assinatura?** — define se o atendente pode ligar e desligar a assinatura nas mensagens que envia. Em **Não**, o comportamento fica fixo e ele não decide.

🔘 **Linha em branco entre a assinatura e a mensagem?** — define o formato da assinatura nas mensagens do atendente. Nas palavras da tela: *"Sim: o nome do atendente fica separado do texto por uma linha em branco. Não: o nome fica logo acima do texto."*

🔘 **Assinatura Genérica** — o texto de assinatura usado quando a mensagem é enviada sem o nome do atendente.

🔘 **Atendente vê os próprios números** — nas palavras da tela: *"Ligada, o atendente ganha "Meus números" no menu: os atendimentos, a 1ª resposta, a resolução e a avaliação dele — só os dele."* A página **Meus números** mostra os atendimentos encerrados, os tempos e as avaliações da própria pessoa, sem os números dos colegas. Em **Não**, o item não aparece no menu do atendente, e a página mostra *O administrador ainda não liberou esta página.* A opção aparece só para o administrador.

## Próximo Passo

🧭 Para montar um cenário completo — por exemplo, impedir que um atendente veja conversas de outros — trate as opções em conjunto, e não uma a uma. Três delas governam visualização ao mesmo tempo: **Operador Acessa Todos os Atendimentos do Setor?**, **Operador Pode Espiar Conversa? (Olhinho)** e **Operador Visualiza Prévias?**.

🧭 Para ajustes que valem só para uma pessoa, vá no menu **Equipe  ›  editar o usuário**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Essas opções valem para um atendente só ou para todos?** Para todos os atendentes da empresa ao mesmo tempo. A seção **Atendimento e operador** não tem ajuste individual — para isso, use o cadastro da pessoa no menu **Equipe  ›  editar o usuário**.
>
> **As opções da seção Atendimento e operador têm botão Salvar?** Não. Cada opção grava assim que você muda o valor: a tela mostra *"Atualizando..."* abaixo do campo e depois o aviso *"Operação atualizada com sucesso."*
>
> **Antes eu via "Fila" e "Departamento" — sumiram?** Não sumiu o recurso, mudou o nome. Hoje a plataforma chama de **Setor** em todo lugar: o menu é **Setores & Chatbot** e o bloco do construtor de fluxos também virou Setor. A palavra "fila" continua aparecendo quando quer dizer *espera* — o cliente que aguarda atendimento está na fila de espera do Setor.
>
> **A saudação do atendente é enviada sozinha ou ele precisa escrever?** É enviada sozinha, no momento em que ele aceita o atendimento, usando o conteúdo do campo **Texto de Saudação**.
>
> **Como obrigo o atendente a enviar a despedida ao encerrar o atendimento?** Em **Despedida obrigatória ao encerrar?**, escolha **Sim**: o atendente só encerra com a mensagem de despedida, e a opção sem despedida some do atendimento. Os encerramentos automáticos do sistema seguem como estão. Para obrigar ou dispensar só uma pessoa, um Setor ou uma Conexão de WhatsApp, use o campo **Despedida ao encerrar** do cadastro dela: ele vale antes da opção da empresa.
>
> **Como deixo o nome do atendente logo acima do texto, sem a linha em branco?** Em **Linha em branco entre a assinatura e a mensagem?**, escolha **Não**: o nome fica logo acima do texto. Com **Sim**, uma linha em branco separa o nome da mensagem.
>
> **Como libero para o atendente a página Meus números?** Em **Atendente vê os próprios números**, escolha **Sim**: cada atendente ganha o item **Meus números** no menu, com os números só dele. O Dashboard continua fechado para o perfil de atendente.
>
> **Os operadores que eu convidei para um atendimento continuam na conversa depois que ele é finalizado?** Depende de **Remover convidados ao finalizar o atendimento?**: em **Sim**, eles saem da conversa ao finalizar; em **Não**, continuam nela.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Preencher o Texto de Saudação e achar que já está valendo:** o texto sozinho não dispara nada. **Solução:** ligue também **Mensagem de Saudação do Operador?**, que é o campo que aciona o envio.
>
> **Esperar que uma opção desta tela resolva um caso individual:** desligar um campo aqui para conter uma pessoa específica e acabar afetando a equipe inteira. **Solução:** o que é de uma pessoa se resolve no menu **Equipe  ›  editar o usuário**.
>
> **Ajustar vários campos seguidos antes de testar:** como a tela grava sozinha, você fica sem saber qual mudança causou qual efeito. **Solução:** uma opção por vez, conferindo com um atendente entre uma e outra.
