# Atualizações 08/11/2026

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/atualizacoes-2026-11-08
- **Categoria:** Recursos
- **Menu:** Atualizações › Novembro 2026 › Atualizações 08/11/2026

---

🧩 Atualizações de 8 de novembro de 2026.

Todas as novidades abaixo estão disponíveis a partir da versão **WS-29.899.0**. Para ver a sua, clique no ícone do perfil, no topo da tela: a versão aparece no fim do menu.

#### Novidades

⚡️ **Endereços do cliente:** no PDV, cada cliente passa a ter vários endereços, com um marcado como principal, e o botão **ENDEREÇOS DO CLIENTE** cadastra, edita e apaga sem sair do pedido.

⚡️ **Taxa no pedido:** ainda no PDV, escolher um endereço salvo já preenche a taxa de entrega pelo bairro, e o endereço digitado na hora pode ficar no cadastro do cliente.

⚡️ **Endereços por planilha e pela API:** ainda no PDV, o administrador e o supervisor importam os endereços por planilha, com o modelo pronto para baixar, e quem integra lê e grava os endereços pela API, com aviso no webhook a cada mudança.

☑️ **Recebido online no caixa:** ainda no PDV, o caixa mostra à parte o que foi recebido pelos links de pagamento, fora do total esperado, e o botão de colocar dinheiro na gaveta passou a se chamar **Suprimento**.

☑️ **Aviso de estorno:** ainda no PDV, o aviso **Pagamento estornado** manda uma mensagem ao cliente assim que o pedido é estornado.

☑️ **Estorno pelo Asaas:** ainda no PDV, a atualização anuncia que o estorno pelo Asaas é acompanhado enquanto espera a autorização, e o pagamento continua valendo até o dinheiro voltar.

◽ **Adicional indisponível:** ainda no PDV, no Balcão, o adicional sem insumo no estoque aparece como **Indisponível**.

◽ **Pedido na mesa sem estoque:** ainda no PDV, se faltar estoque, o pedido na mesa é recusado inteiro, sem ficar pela metade.

◽ **Pergunta do Tenho interesse:** na Loja digital, a pergunta do **Tenho interesse** não some mais enquanto o cliente navega.

◽ **Hora dos pagamentos antigos:** ainda no PDV, a atualização anuncia a hora real nos pagamentos antigos, que apareciam todos ao meio-dia.

⚡️ **Ranking por equipe, unidade e funil:** no CRM, o Ranking ganhou a escolha **Ranking por**: vendedores, equipes, unidades ou funis, com pódio, vendas, ticket médio, meta e total. A meta da equipe e da unidade é a soma das metas do mês das pessoas.

☑️ **Janela da oportunidade:** ainda no CRM, a janela da oportunidade fecha pelo **X**, no topo, e o botão de gravar se chama **Salvar**, no lugar de **Editar**.

⚡️ **Aparelho do cliente:** no Atendimento, a mensagem do cliente mostra, ao lado da hora, de qual aparelho ele escreveu: iPhone, Android ou computador.

◽ **Ordem do Aguardando:** ainda no Atendimento, a lista **Aguardando** volta a obedecer a ordem que você escolhe, e mensagem nova não muda o lugar de ninguém.

⚡️ **WhatsApp pela Gupshup:** em Conexões, chegou um novo canal de WhatsApp, pela Gupshup. A atualização anuncia templates na conversa mesmo depois das 24 horas, botões, listas, FlowBuilder Nativo e campanhas.

⚡️ **RCS pela Gupshup:** ainda em Conexões, chegou a conexão RCS pela Gupshup, para mensagens ricas direto no aplicativo de mensagens do celular.

☑️ **Concatenador em todas as conexões:** ainda em Conexões, o **Concatenador** passa a valer em todas as conexões, com o botão no card de cada uma: enquanto a mensagem aguarda, você cancela e escreve de novo.

⚡️ **Aplicativo do celular:** no aplicativo do celular, chegaram o PDV, com venda de balcão, categorias, variações e adicionais, o viva-voz na chamada, a videochamada pela ficha do contato e, no Chat Interno, editar, buscar, figurinhas e ver quem leu.

#### Melhorias

☑️ **Editar no Chat Interno:** no Chat Interno, editar a mensagem acontece no próprio campo de digitação, sem janela por cima.

☑️ **Datas na API:** na API, os relatórios de avaliações, de anúncios, do PDV e de e-mails aceitam a data em dia/mês/ano.

#### Correções

◽ **Notificação da tarefa:** nas Tarefas, a notificação chega na hora, em qualquer tela, sem recarregar a página, e clicar no aviso abre a tarefa ou os comentários.

◽ **Atendimento incorporado:** no atendimento incorporado, a conversa atualiza em tempo real, e a sessão se renova sozinha.

## Endereços do cliente

No pedido feito na conversa, ao marcar **Entrega**, aparecem a lista **Endereço salvo do cliente** e o botão **ENDEREÇOS DO CLIENTE**. O botão abre a janela **Endereços do cliente**, com os endereços daquele cliente e o botão **NOVO ENDEREÇO**.

➡️ Cada endereço tem **Apelido**, **Endereço**, **Bairro** e **CEP**, e a caixa **Usar como endereço principal**. O primeiro endereço do cliente já nasce principal.

➡️ Em cada linha, a estrela marca o principal (**Tornar principal**), o lápis edita e a lixeira apaga, depois da confirmação *Apagar este endereço do cliente?*. Apagado o principal, o endereço usado por último passa a ser o principal.

➡️ O mesmo endereço não entra duas vezes: a tela avisa *Este endereço já está na lista do cliente.* Bairro fora da tabela de entrega recebe o aviso *Ainda não entregamos neste bairro.*

## Taxa e endereço no pedido

Escolher um endereço na lista **Endereço salvo do cliente** preenche a **Taxa de entrega** pela tabela de bairros, junto com o endereço e o bairro.

➡️ A lista também tem **Outro endereço (digitado abaixo)**, para o endereço que o cliente passa na hora.

➡️ Para endereço novo, aparece a caixa **Salvar este endereço no cadastro do cliente**, já marcada. Marcada, o endereço digitado vai para o cadastro e fica na lista nas próximas vendas; desmarcada, vale só para aquele pedido.

## Endereços por planilha

No menu **PDV  ›  Pedidos**, os botões **MODELO DE ENDEREÇOS** e **IMPORTAR ENDEREÇOS** aparecem para o administrador e o supervisor.

➡️ O modelo é uma planilha com as colunas **Telefone**, **Nome**, **Apelido**, **Endereço**, **Bairro**, **CEP** e **Principal**, e uma aba de instruções: o telefone vai com DDI e DDD, e cada cliente aceita até 10 endereços.

➡️ Ao importar, a janela **Importação de endereços** mostra quantos endereços entraram, quantos já existiam e quantos clientes novos foram cadastrados, como *2 de 2 endereços importados.*

➡️ Planilha sem a coluna **Endereço** é recusada, com o pedido para baixar o modelo e preencher nele.

## Endereços pela API

Na API, a rota `/api/pdv/enderecos` lê os endereços de um cliente, pelo número ou pelo contato, com o principal primeiro, e grava endereço novo.

➡️ A cada endereço salvo ou apagado, pelo painel, pela planilha ou pela API, o webhook avisa com os eventos `cardapio-endereco-salvo` e `cardapio-endereco-removido`, e o campo `origem` diz por onde a mudança veio.

## Recebido online e Suprimento no caixa

No menu **PDV  ›  Caixa**, o **Meu caixa** ganhou o bloco **Recebido online (fora do caixa)**: os pagamentos pelos links gerados com o caixa aberto, um por linha, e o **Total online**. O dinheiro cai na conta do provedor, e não na gaveta, por isso fica fora do **Total esperado**.

➡️ O link estornado aparece com *— Estornado* e não entra na soma.

➡️ O botão de colocar dinheiro na gaveta, que se chamava **Reforço**, agora é **Suprimento**, e o movimento aparece com esse nome: *Suprimento registrado.*

## Aviso de estorno ao cliente

No menu **Configurações  ›  Opções**, os **Avisos do pedido ao cliente** ganharam **Pagamento estornado**, com o texto *Estornamos o pagamento do pedido #`{{numero}}`. O valor volta pela mesma forma de pagamento.*

➡️ Ligado, o cliente recebe a mensagem assim que o pedido é estornado. Desligado, nada é enviado.

## Balcão, Mesa e Loja

No Balcão, o adicional cujo insumo acabou aparece como **Indisponível** e não pode ser escolhido.

➡️ No pedido da mesa, se faltar estoque de algum item, o pedido é recusado inteiro com o aviso *Um dos produtos acabou. Revise a sacola.*, sem criar o pedido e sem abrir a comanda.

➡️ Na Loja digital, o texto escrito em *Quer perguntar alguma coisa? (opcional)* fica no campo enquanto o cliente troca a variação, o adicional e a quantidade, e chega junto com o interesse.

## Ranking por equipe, unidade e funil

No menu **CRM  ›  Ranking**, o seletor **Ranking por** tem **Vendedor**, **Equipe**, **Unidade** e **Funil**, e a tela abre em **Vendedor**.

➡️ Em **Equipe**, **Unidade** e **Funil**, o pódio e a tabela mostram cada grupo, com **vendas**, **Ticket médio**, **Meta** e **Total**. Os cards do topo não mudam.

➡️ Quem está em duas equipes conta nas duas, e uma vez só na unidade. Quem não está em nenhuma equipe conta nas vendas totais.

➡️ A meta de cada equipe e de cada unidade é a soma das metas do mês das pessoas dela. Com um funil escolhido, valem as metas do funil.

➡️ **Funil** aparece com **Todos os funis**. Com **Encerramento de atendimentos**, só **Vendedor**.

## Janela da oportunidade

A janela **Editar Oportunidade** fecha pelo **X**, no topo, e o rodapé ficou com **GERAR PROPOSTA**, **EXCLUIR** e **SALVAR**. A janela **Adicionar Oportunidade** fica só com **SALVAR**.

➡️ **SALVAR** grava e fecha a janela. Fechar pelo **X** não grava o que você mudou.

## Aparelho do cliente

No Atendimento, a mensagem do cliente mostra, à esquerda da data e hora, o ícone do aparelho de onde ela foi enviada: uma maçã para o iPhone e um monitor para o computador.

➡️ Parar o mouse sobre o ícone mostra *Enviada de um iPhone*, *Enviada de um Android* ou *Enviada do WhatsApp Web ou Desktop*.

## Ordem do Aguardando

No Atendimento, o botão **Ordenar tickets** volta a mudar a lista **Aguardando**.

➡️ **Mais recentes primeiro** põe quem acabou de chegar em cima.

➡️ **Mais antigos primeiro** põe em cima quem espera há mais tempo, na ordem de chegada.

➡️ Mensagem nova do cliente não muda o lugar de ninguém na lista, nas duas ordens.

## Concatenador em todas as conexões

No menu **Conexões**, o botão **CONCATENADOR** passa a aparecer no card de cada conexão, e não só no da oficial. A janela é a mesma: **Juntar mensagens em rajada**, **Modo** (*Simples* ou *Com IA*) e **Janela de espera (segundos)**, de 2 a 60.

➡️ Na conversa, a mensagem que aguarda mostra **aguardando** e **cancelar**. Com mais de uma, aparece **cancelar todas**. Cancelada, a mensagem some da conversa e nunca chega ao cliente.

➡️ No Chat Externo, o cliente não vê a mensagem que ainda aguarda, e a atualização anuncia o mesmo no WebChat. Depois da janela de espera, ele recebe tudo num balão só.

➡️ O Concatenador vale só para texto. Mídia, áudio e resposta a uma mensagem específica são enviados na hora e liberam o que estiver esperando.

## Editar no Chat Interno

Em **Ações da mensagem**, **Editar** leva o texto para o campo de digitação, com a barra **Editar mensagem** em cima: *Todos na conversa veem o texto novo, com a marca "editada". Enter salva; Shift+Enter quebra a linha.*

➡️ **Enter** salva, e a mensagem ganha a marca **editada** para todos na conversa, sem recarregar.

➡️ O **X** ou o **Esc** cancelam, e o rascunho que estava no campo volta.

➡️ Só a sua mensagem tem **Editar** e **Apagar**.

## Datas na API

Na API, aceitam a data em dia/mês/ano, como `01/10/2026`, e continuam aceitando ano-mês-dia, como `2026-10-01`: a lista de avaliações, o relatório de anúncios, o relatório e os lançamentos do PDV e a consulta de e-mails. Uma data que não existe, como `31/02/2026`, é recusada.

➡️ Nas outras rotas da API, continue usando ano-mês-dia.

## Notificação da tarefa

Quando alguém cria uma tarefa para você ou comenta numa tarefa sua, o aviso aparece na hora, em qualquer tela, e o sino sobe sem recarregar: *Nova tarefa para você* ou *Novo comentário na tarefa*.

➡️ Clicar no aviso abre a tarefa na aba **TAREFA** ou, quando o aviso é de comentário, nos **Comentários**.

## Atendimento incorporado

No atendimento incorporado, a conversa que fica dentro de outro sistema mostra as mensagens na hora, sem recarregar, e o **ACEITAR** atualiza a tela.

➡️ O atendimento incorporado abre no mesmo navegador do painel sem perder o login, e a sessão se renova sozinha.

➡️ O link incorporado aceita também o código do atendimento, e as chaves secretas da empresa aparecem só para o administrador.

#### O que você precisa fazer

Três coisas pedem atenção:

➡️ Sua equipe deve conferir a ordem escolhida em **Ordenar tickets**, no **Aguardando**, porque ela volta a valer.

➡️ Quem usa o caixa do PDV vai encontrar o **Reforço** com o nome **Suprimento**.

➡️ Quem edita oportunidade no CRM agora clica em **Salvar** para gravar: fechar pelo **X** não grava.

O WhatsApp pela Gupshup e o RCS dependem do plano.
