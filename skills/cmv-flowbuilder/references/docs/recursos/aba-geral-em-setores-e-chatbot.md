# Aba Geral em Setores & Chatbot

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-geral-em-setores-e-chatbot
- **Categoria:** Recursos
- **Menu:** Setores & Chatbot › Aba Geral em Setores & Chatbot

---

🧩 A aba **Geral** é a identidade e o comportamento do Setor. É aqui que você dá nome e cor, define quanto tempo uma conversa espera antes de ser transferida, escolhe quem é avisado e liga a automação que vai atender antes de um humano.

É a única aba obrigatória do cadastro, e dentro dela três campos precisam ser preenchidos: **Nome**, **Ordenação do BOT** e **Cor**. O sistema recusa o salvamento sem eles. Todo o resto tem função específica e pode ficar vazio até você precisar.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Setores & Chatbot**.
>
> ➡️ Clique em **ADICIONAR SETOR**, ou no lápis de um Setor existente.
>
> ➡️ Preencha **Nome**, **Ordenação do BOT** e **Cor** e ajuste o que for necessário. Clique em **Adicionar** (Setor novo) ou **Salvar** (Setor existente).

## Identificação

🔘 **Nome:** como o Setor aparece para a equipe, nos relatórios e nas listas de transferência. Campo obrigatório e não pode repetir o nome de outro Setor.

🔘 **Cor:** a cor de identificação do Setor na lista de atendimentos. Permite ao atendente reconhecer a origem da conversa sem ler o nome. Campo obrigatório.

🔘 **Categoria:** agrupa Setores que têm a ver entre si, para organizar a lista quando ela cresce. As categorias são cadastradas na tela **Categorias**, logo abaixo de **Setores & Chatbot** no menu.

🔘 **Ordenação do BOT:** um número que define a posição do Setor na lista da tela **Setores & Chatbot** e no menu de Setores que a Conexão envia ao cliente quando aponta para dois ou mais Setores. O número menor vem primeiro. Na lista, ele aparece como prioridade **Alta** (1 a 3), **Média** (4 a 6) ou **Baixa** (7 em diante). Campo obrigatório.

🔘 **Arquivo de Capa:** imagem de capa do Setor, escolhida entre os arquivos do **Gerenciador de Arquivos**.

## Campos extras

🔘 **Campo extra 1** e **Campo extra 2:** dois campos livres para guardar a informação do Setor que não tem lugar próprio no cadastro — a unidade, o centro de custo, um código interno. Cada um aceita até 1.000 caracteres.

🔘 **A variável de cada campo** vem escrita embaixo dele. Nas palavras da tela: *Nas mensagens e no fluxo, use* `{{queue_extra1}}` — e `{{queue_extra2}}` para o **Campo extra 2**. A variável é trocada pelo valor do Setor na **Mensagem de saudação** do Setor, no texto do fluxo, na mensagem que o atendente envia (digitada ou pela resposta rápida) e no agendamento feito com o Setor.

## Distribuição do atendimento

🔘 **Rodízio de Atendentes:** passado o **Tempo de Escala**, sorteia a conversa entre os atendentes do Setor escolhido em **Mover** e a entrega ao sorteado já em atendimento. Funciona quando o cliente chega a este Setor pelo menu do chatbot.

🔘 **Notificar Operador no WhatsApp:** avisa no WhatsApp pessoal os usuários do Setor que têm **Telefone** cadastrado quando uma conversa nova chega a ele e fica em **Aguardando**, e também quando o rodízio entrega a conversa ao atendente sorteado.

🔘 **Tempo de Escala:** tempo que o sistema aguarda antes de escalar o atendimento. As opções vão de **Desativado** a **60 minutos** (2, 5, 10, 15, 30, 45 ou 60).

🔘 **Mover:** para qual Setor a conversa é transferida quando o tempo se esgota.

⚠️ **Mover para um Setor sem atendentes** é o erro clássico: a conversa é transferida corretamente e fica parada, porque ninguém tem acesso ao destino. Antes de escolher o Setor de destino, confirme que há gente cadastrada nele.

## Comportamento do atendimento

🔘 **Motivo de Encerramento Obrigatório:** exige que o atendente escolha uma tag de encerramento ao finalizar a conversa. Serve para você saber depois **por que** cada atendimento terminou, e não só quantos terminaram.

⚠️ Este campo só funciona se existirem tags do tipo **Encerramento** cadastradas no menu **Tags**. Sem elas, o atendente é obrigado a escolher de uma lista vazia.

🔘 **Ativar Transcrição de Áudio:** transforma em texto os áudios que o cliente enviar neste Setor, se disponível no seu plano.

🔘 **Grupos de templates:** limita quais templates ficam disponíveis neste Setor. Deixando vazio, o Setor mostra todos os templates da Conexão. O campo lista **grupos**, não templates avulsos — e os grupos são criados fora daqui, no menu **Conexões  ›  editar a Conexão oficial  ›  Gestão de Templates  ›  GRUPOS**. Sem nenhum grupo criado, este campo abre vazio.

🔘 **URL do Webhook:** endereço para o qual o sistema envia os eventos deste Setor, quando você quer integrar com um sistema próprio.

## Automação: os caminhos desta aba

⚠️ Esta aba oferece **quatro formas diferentes** de colocar um robô para atender, e a aba **Integrações**, quando o seu plano a inclui, oferece outras. Escolha **uma** e conheça as outras antes de decidir — o recomendado hoje é montar a automação no construtor de fluxos.

🔘 **Fluxos de Automação:** escolhe qual fluxo do construtor entra em ação quando chega uma mensagem do cliente com a conversa neste Setor. É o caminho mais completo: dentro do fluxo você monta menus, condições, envio de mídia e até um assistente de inteligência artificial.

🔘 **Prompt OPEN.AI (ChatGPT):** coloca um assistente de inteligência artificial direto no Setor, sem passar por um fluxo, se disponível no seu plano. Os assistentes são criados no menu **Prompts OPEN.AI**.

🔘 **Opções do Chatbot:** monta um menu numerado que o cliente recebe depois de escolher este Setor no menu da Conexão. Cada opção responde com um texto ou encaminha a conversa. É o caminho mais simples e o mais antigo.

🔘 **ChatBot Externo:** liga o atendimento deste Setor a um robô de fora da plataforma.

## Próximo Passo

🧭 Escrever a mensagem que o cliente recebe ao chegar, na aba **Mensagens** do mesmo cadastro.

🧭 Cadastrar quem atende este Setor, no menu **Equipe  ›  editar o usuário**.

🧭 Se for usar o expediente, escolher **Gerenciamento Por Setor** em **Gerenciamento de Expediente**, no menu **Configurações  ›  Opções**, e voltar à aba **Horários**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Quais campos são obrigatórios?** Três, todos na aba Geral: **Nome**, **Ordenação do BOT** e **Cor**. O sistema não deixa salvar sem eles. O restante do cadastro pode ficar vazio e ser ajustado depois.
>
> **Liguei o Motivo de Encerramento Obrigatório e o atendente não consegue finalizar. Por quê?** Provavelmente não existem tags do tipo **Encerramento** cadastradas. O campo obriga a escolher um motivo, e se a lista está vazia não há o que escolher. Crie as tags no menu **Tags**, com o tipo **Encerramento**.
>
> **Posso ligar mais de uma automação no mesmo Setor?** Não recomendamos. Existem quatro caminhos nesta aba e outros na aba Integrações, e preencher dois ao mesmo tempo torna difícil prever qual responde. Escolha um.
>
> **Qual a diferença entre Fluxos de Automação e Prompt OPEN.AI?** O **Fluxo** é um roteiro que você desenha no construtor, com etapas, perguntas e condições — e dentro dele cabe também um assistente de inteligência artificial. O **Prompt OPEN.AI** coloca o assistente direto no Setor, sem roteiro em volta. O fluxo é mais completo; o prompt é mais direto.
>
> **O que é "Ordenação do BOT"?** É o número que define a posição do Setor na lista da tela **Setores & Chatbot** e no menu de Setores que a Conexão envia ao cliente quando aponta para dois ou mais Setores. O número menor vem primeiro.
>
> **Para que serve deixar "Grupos de templates" vazio?** Vazio, o Setor mostra todos os templates da Conexão. Preencher só faz sentido quando você quer que aquele Setor use apenas parte deles.
>
> **O campo "Grupos de templates" abre vazio. Por quê?** Porque nenhum grupo foi criado ainda. Ele lista grupos, e não os templates em si. Crie os grupos no menu **Conexões  ›  editar a Conexão oficial  ›  Gestão de Templates  ›  GRUPOS** e eles passam a aparecer aqui.
>
> **Como tiro o grupo que escolhi?** Abra o campo e clique de novo no grupo que está marcado — ele desmarca. Não existe uma opção "sem grupo" na lista.
>
> **Vinculei um grupo e não apareceu selo no card do Setor.** É o esperado. Grupos de templates não geram selo na tela de lista, diferente do fluxo ou do webhook.
>
> **Para que servem o Campo extra 1 e o Campo extra 2 do Setor?** Guardam uma informação do Setor que o cadastro não tem, como a unidade ou o centro de custo, para usar nas mensagens e no fluxo com as variáveis `{{queue_extra1}}` e `{{queue_extra2}}`.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Configurar Mover para um Setor sem atendentes:** a conversa é transferida no tempo certo e fica parada no destino, porque ninguém ali tem acesso para assumir. **Solução:** antes de escolher o destino, confirme em **Equipe** que há gente cadastrada naquele Setor.
>
> **Ligar o Motivo de Encerramento sem criar as tags antes:** o atendente é obrigado a escolher um motivo de uma lista vazia e não consegue finalizar. **Solução:** crie as tags do tipo **Encerramento** no menu **Tags** antes de ligar a opção.
>
> **Preencher dois motores de automação achando que se completam:** eles não se somam. Com dois caminhos preenchidos, fica difícil prever qual atende. **Solução:** escolha um caminho por Setor.
>
> **Criar o Setor com tudo preenchido de uma vez:** quando algo não funciona, não dá para saber qual dos dez campos causou. **Solução:** salve com os três campos obrigatórios, confirme que a conversa chega, e só então acrescente automação, tempos e integração.
