# Blocos do FlowBuilder: quando usar e onde tropeçam

Guia rápido para escolher o bloco. Os campos, os limites e as mensagens de tela estão no artigo de cada bloco, em `references/docs/recursos/`: **abra o artigo antes de escrever o que preencher**. A coluna JSON diz o `type` do bloco no arquivo exportado, quando o formato foi observado (ver `references/formato-json.md`); "não" quer dizer que o bloco só entra pelo roteiro de montagem.

## Sumário

- [Qual bloco para qual necessidade](#qual-bloco-para-qual-necessidade)
- [Regras que valem para todos](#regras-que-valem-para-todos)
- [Falar com o cliente](#falar-com-o-cliente)
- [Guardar e marcar](#guardar-e-marcar)
- [Decidir o caminho](#decidir-o-caminho)
- [Conversar com outros sistemas](#conversar-com-outros-sistemas)
- [Entregar a conversa ou terminar](#entregar-a-conversa-ou-terminar)
- [Onde cada bloco funciona](#onde-cada-bloco-funciona)

## Qual bloco para qual necessidade

| Preciso de… | Bloco |
|---|---|
| mandar texto, imagem, áudio, vídeo ou arquivo | Conteúdo |
| oferecer opções, cada uma com um caminho | Menu |
| botões de link, de copiar código ou de resposta pronta, todos seguindo pelo mesmo caminho | Botões |
| pedir um dado (nome, CPF, e-mail) | Pergunta, e logo depois Variável |
| decidir por texto, tag, horário, dia, conexão, anúncio | Condição |
| decidir por tags com vários caminhos de uma vez | Switch (tags) |
| separar dentro e fora do expediente de um Setor | Horário de Expediente |
| passar para a equipe | Setor (quem estiver livre), Operador (pessoa certa) ou Rodízio (distribuição) |
| passar para outro fluxo | Trocar Fluxo |
| voltar a um ponto do mesmo fluxo | Pular para |
| passar para a IA | GPT Assistant (OpenAI) |
| falar com quem não escreveu nas últimas 24 horas, no WhatsApp Oficial | Template |
| consultar ou avisar outro sistema | HTTP Request (por campos) ou Execução de Código JS (por código) |
| segunda via de cobrança | Asaas |
| registrar o negócio no CRM | Oportunidade |
| o cliente reservar sozinho a oferta, o dia e o horário livre | Reservas (agendar no fluxo) |
| deixar um resumo para o atendente | Msg Interna |
| terminar o atendimento | Encerrar |
| terminar um fluxo chamado por resposta rápida | Encerrar Mensagem Rápida |

## Regras que valem para todos

Lidas em Como o Fluxo Roda (`references/docs/recursos/como-o-fluxo-roda.md`) e Blocos (`references/docs/recursos/blocos.md`):

- **Saída sem ligação é conversa que para.** Todo bloco com duas ou mais saídas precisa de todas ligadas.
- **Blocos que esperam o cliente:** o artigo lista Pergunta, Menu, Botões e Avaliação do Atendimento. Neles, e também no GPT Assistant e no Typebot, o campo **Sem resposta** cria a saída de quem não respondeu. Sem ele, o fluxo fica esperando.
- **Blocos sem saída:** o artigo lista Setor, Operador, Trocar Fluxo, Encerrar e Encerrar Mensagem Rápida. Depois deles, o fluxo acabou.
- **Dois jeitos de escrever dados no texto:** `{{firstName}}` para dados do contato e do atendimento; `%nome%` para variáveis guardadas pelo fluxo. Trocar um pelo outro deixa o lugar em branco ou mostra o código escrito.

## Falar com o cliente

**Conteúdo** · `references/docs/recursos/bloco-conteudo.md` · JSON: `singleBlock` (só Texto, Intervalo e Imagem observados)
- Use para: mensagens e mídia, vários itens no mesmo bloco, enviados em ordem.
- Cuidado: ponha um **Intervalo** entre textos, para não chegarem colados. Mídia acima de 5 MB pode falhar. Imagem não vai dentro do JSON: é incluída no editor.

**Menu** · `references/docs/recursos/bloco-menu.md` · JSON: `menu` (só Menu em Lista observado)
- Use para: a triagem. Uma saída por opção, mais **Resposta inválida** (com o **Caminho alternativo (ELSE)** marcado) e **Sem resposta** (com os minutos preenchidos).
- Cuidado: o artigo não diz em quais canais a lista e os botões do Menu chegam como lista e como botões, salvo o **WebChat**, onde o **Menu em Lista** abre pelo botão da lista e só a última mensagem com opções aceita o toque (ver o quadro no fim desta página). No **Menu em Texto**, não numere as opções na mensagem, porque a plataforma já numera. Na lista e nos botões, opção com até 20 caracteres. **Menu em Botões** vai até 3 opções; com mais, o menu não chega ao cliente. Sem ELSE, a resposta fora das opções só reenvia o menu. Áudio em resposta a um Menu em Texto não conta como escolha. O rodapé da lista pode não aparecer, conforme o canal.

**Pergunta** · `references/docs/recursos/bloco-pergunta.md` · JSON: `question` (sem os campos de inatividade)
- Use para: pedir um dado e esperar. Para guardar a resposta, **Variável logo depois**.
- Cuidado: a Pergunta aceita qualquer texto; validação é com Condição ou Execução de Código JS. **Sem resposta** e **Mover de setor por inatividade** fazem coisas diferentes: leia o artigo antes de escolher.

**Botões** · `references/docs/recursos/bloco-botoes.md` · JSON: não
- Use para: link, ligação, copiar e colar (cupom, PIX) e resposta rápida. **Uma saída só**; para um caminho por botão, é Menu em Botões.
- Cuidado: a quantidade e os tipos mudam por canal (quadro no artigo). No WhatsApp Oficial, o primeiro botão manda na mensagem inteira. Texto do botão com até 20 caracteres. No WhatsApp QRCode depende do recurso de botões liberado.

**Template** · `references/docs/recursos/bloco-template.md` · JSON: não
- Use para: mensagem aprovada pela Meta; é o único jeito de o fluxo falar com quem não escreveu nas últimas 24 horas.
- Cuidado: só conexão do WhatsApp Oficial; só templates aprovados aparecem; todo envio é cobrado pela Meta. O texto do template é assunto da skill `cmv-mensagens`.

**Avaliação do Atendimento** · `references/docs/recursos/bloco-avaliacao-do-atendimento.md` · JSON: não
- Use para: pesquisa de satisfação no meio do fluxo, com uma pesquisa do menu **Avaliações**.
- Cuidado: o bloco **não encerra** o atendimento; ligue a saída a um Encerrar. Preencha **Sem resposta**.

**PDV (pedido no fluxo)** · `references/docs/recursos/pdv-pedido-no-fluxo.md` · JSON: não
- Use para: o cliente montar e confirmar um pedido pela conversa. Saídas **Pedido confirmado**, **Desistiu** e **Sem resposta**.
- Cuidado: o bloco confirma o pedido, mas não envia a nota nem registra o pagamento.

**Reservas (agendar no fluxo)** · `references/docs/recursos/reservas-agendar-no-fluxo.md` · JSON: não
- Use para: o cliente escolher pelo número a oferta, o dia e o horário livre e confirmar a reserva pela conversa. Saídas **Reservou** e **Não reservou**, mais **Sem resposta** com os minutos preenchidos.
- Cuidado: o **0** desiste em qualquer passo e segue pela **Não reservou** sem outra mensagem ao cliente; ligue essa saída. O bloco só cria a reserva: remarcar e cancelar é com a equipe, na **Agenda de reservas**.

**Contato**, **Enviar Localização**, **Enviar Figurinha** · Contato (`references/docs/recursos/bloco-contato.md`), Localização (`references/docs/recursos/bloco-enviar-localizacao.md`), Figurinha (`references/docs/recursos/bloco-enviar-figurinha.md`) · JSON: não
- Use para: cartão de contato, ponto no mapa, figurinha da biblioteca da empresa. Contato e Enviar Localização têm uma saída cada; o artigo da Figurinha não descreve as saídas do bloco (diz só que, quando o bloco é pulado, o fluxo segue para o próximo passo).
- Cuidado: a Figurinha só é enviada no WhatsApp QRCode e no Oficial; nos outros canais o bloco é pulado e o fluxo segue.

**Webview** · `references/docs/recursos/bloco-webview.md` · JSON: não
- Use para: abrir uma página dentro do WhatsApp.
- Cuidado: só WhatsApp QRCode com botões liberados. Em outros canais, use Botões com Botão URL.

**Carrossel de Produtos** · `references/docs/recursos/bloco-carrossel-de-produtos.md` · JSON: não
- Use para: vitrine com produtos do catálogo da Meta.
- Cuidado: só WhatsApp Oficial com catálogo vinculado; até 10 seções e 30 produtos.

**Link do Chat Externo** · `references/docs/recursos/bloco-link-do-chat-externo.md` · JSON: não
- Use para: levar a conversa à página do chat externo por link.
- Cuidado: com **Continuar o fluxo no chat externo** ligado, o que o cliente escreve no WhatsApp não faz o fluxo andar.

**Responder Comentário** · `references/docs/recursos/bloco-responder-comentario.md` · JSON: não
- Use para: responder em público o comentário do Instagram; a mensagem no Direct é o bloco seguinte.
- Cuidado: escreva várias frases, separadas por vírgula e **sem vírgula dentro da frase**.

## Guardar e marcar

**Variável** · `references/docs/recursos/bloco-variavel.md` · JSON: `variable`
- Use para: guardar a resposta de uma Pergunta, a opção de um Menu, a nota de uma Avaliação, o `return` de um código ou a última mensagem antes do Início.
- Cuidado: a Variável vem **logo depois** da fonte do dado; a única peça que pode ficar no meio é um Intervalo. Depois do HTTP Request ela não é necessária (e guardaria outra coisa). Usar a variável antes de guardá-la mostra `%nome%` escrito para o cliente.

**Tag** e **Remover Tag** · Tag (`references/docs/recursos/bloco-tags.md`), Remover Tag (`references/docs/recursos/bloco-remover-tag.md`) · JSON: `tag`; Remover Tag não
- Use para: marcar interesse ou etapa, e limpar a marca anterior. É a tag que dispara o remarketing.
- Cuidado: um bloco, uma tag. A tag precisa existir no menu **Tags**. Tag marca, não move: para mudar de Setor é o bloco Setor. **Remover Todas as Tags** tira também as que a equipe pôs à mão.

**Msg Interna** · `references/docs/recursos/bloco-msg-interna.md` · JSON: `internal`
- Use para: nota que só a equipe vê, com o resumo antes da passagem para uma pessoa. Aceita `%variavel%`.

**Intervalo** · `references/docs/recursos/bloco-intervalo.md` · JSON: `interval`
- Use para: pausa entre dois blocos, folga depois de uma consulta externa ou retorno programado. De 1 segundo a 24 horas, em **Segundos**, **Minutos** ou **Horas**; no arquivo, só até 120 segundos.
- Cuidado: com mais de 2 minutos o bloco ganha a saída **Janela expirada**; ligue-a. Se o atendimento for aceito, transferido para um atendente ou encerrado durante a espera, o fluxo não continua. **Se o cliente responder durante a espera** decide entre **Continuar esperando** e **Cancelar a espera (o fluxo para aqui)**. Para pausar entre mensagens do mesmo Conteúdo, é o item Intervalo de dentro dele (de 1 a 120 segundos).

**Oportunidade** · `references/docs/recursos/bloco-oportunidade.md` · JSON: não
- Use para: criar o negócio no CRM para o contato da conversa.
- Cuidado: **cada passagem cria uma oportunidade nova**; ponha num trecho que o cliente atravessa uma vez, como depois de uma escolha do Menu. O bloco não entrega a conversa ao operador escolhido. Só aparece com o CRM no plano.

**Pixel META** · `references/docs/recursos/bloco-pixel-meta.md` · JSON: não
- Use para: avisar a Meta de um evento (lead, compra).
- Cuidado: no formato **Mensagens do WhatsApp** há duas saídas, **Elegível** e **Não elegível**; sem a segunda ligada, quem não veio de anúncio para ali.

## Decidir o caminho

**Condição** · `references/docs/recursos/bloco-condicao.md` · JSON: `condition` (só três combinações observadas)
- Use para: uma pergunta de sim ou não sobre a resposta, uma tag, o horário, o dia, a conexão, o status, o tempo desde o último encerramento, o anúncio ou a publicação. Saídas **Verdadeiro** e **Falso**.
- Cuidado: **Igual** compara a resposta inteira e o acento conta (*nao* não é *Não*). Lista separada por vírgula só funciona no **Contém**. **Contém** aceita resposta maior do que você queria (*Não realizei* contém *realizei*); para resposta exata, Expressão Regular. Logo depois de uma Variável, a Condição compara o valor da Variável; sem Variável, compara a resposta da Pergunta ou a opção do Menu que veio antes. **É Dia Útil?** não conta o sábado. Horário é o de Brasília. Ligue sempre o **Falso**.

**Switch (tags)** · `references/docs/recursos/bloco-switch-tags.md` · JSON: `switch` (só **possui a tag** observado)
- Use para: vários caminhos por tag num bloco só. Uma saída por regra, mais **Nenhuma condição atendida**.
- Cuidado: a ordem das regras é a prioridade; regra genérica no topo engole as de baixo. Confere as tags do atendimento. Ligue **Nenhuma condição atendida**.

**Horário de Expediente** · `references/docs/recursos/bloco-horario-de-expediente.md` · JSON: `away` (qual saída é qual não foi confirmado)
- Use para: separar **Dentro do Horário** e **Fora do Horário** pelo expediente cadastrado no Setor.
- Cuidado: o horário não fica no bloco. Ele vem da aba **Horários** do Setor, que só existe com o **Gerenciamento de Expediente** em **Gerenciamento Por Setor**. Ligar esse gerenciamento faz **todos** os Setores passarem a seguir o horário que já está na aba de cada um: leia Aba Horários (`references/docs/recursos/aba-horarios-em-setores-e-chatbot.md`) antes de mandar ligar.

**Randomizador** · `references/docs/recursos/bloco-randomizador.md` · JSON: não
- Use para: teste A/B ou divisão por sorteio em dois caminhos.
- Cuidado: é chance, não cota exata. Ligue as duas saídas.

**É Seguidor?** · `references/docs/recursos/bloco-e-seguidor.md` · JSON: não
- Use para: "siga para receber" no Instagram. Saídas **Segue** e **Não segue**, sem janela de configuração.

**Pular para** · `references/docs/recursos/bloco-pular-para.md` · JSON: não (no arquivo, voltar a um bloco é uma ligação comum)
- Use para: voltar ao menu ou repetir uma etapa sem linha atravessando o desenho. O destino é um bloco do mesmo fluxo.
- Cuidado: o caminho de volta precisa passar por um bloco que espera o cliente; senão é **ciclo sem espera** e o fluxo é interrompido. Na janela, sem destino escolhido o botão **Adicionar** fica desativado; e um **Pular para** que ficou sem destino válido (o bloco de destino foi apagado, por exemplo) impede de salvar o fluxo.

## Conversar com outros sistemas

**HTTP Request** · `references/docs/recursos/bloco-http-request.md` · JSON: não
- Use para: chamar uma API pelos campos da janela e guardar a resposta em variáveis, na aba **Resposta**.
- Cuidado: a resposta se usa com `%nome%`, não com chaves. Não precisa de Variável depois. Teste com **Testar Requisição**. O desenho da chamada (endpoint, corpo, token) é assunto da `cmv-api`.

**Execução de Código JS** · `references/docs/recursos/bloco-execucao-de-codigo-js.md` · JSON: `wbh`
- Use para: tratar um dado (limpar CPF, pegar o DDD) ou escrever a chamada à mão. O `return` é o resultado; **Variável logo depois** para guardar.
- Cuidado: devolva texto ou número; objeto vira *[object Object]*. O campo **Tipo** tem **MENU** e **REQUISIÇÃO**; para chamar endereço externo, o artigo manda usar **REQUISIÇÃO**.

**Asaas** · `references/docs/recursos/bloco-asaas.md` · JSON: não
- Use para: segunda via. Peça CPF ou CNPJ numa Pergunta antes; saídas **Sucesso** e **Erro**.
- Cuidado: só números no documento. O bloco envia o link da fatura mais recente, não de todas. Ligue a saída **Erro**.

O artigo n8n via Flowbuilder (`references/docs/recursos/n8n-via-flowbuilder.md`) fala em bloco HTTP Request, mas o exemplo dele é código JavaScript, igual ao do artigo da Execução de Código JS, e termina mandando guardar a resposta numa Variável. Código vai em **Execução de Código JS**, seguido de Variável; no **HTTP Request**, a chamada é montada pelos campos e a resposta é guardada pela aba **Resposta**. Avise a pessoa dessa diferença.

## Entregar a conversa ou terminar

**Setor** · `references/docs/recursos/bloco-setor.md` · JSON: `queue`
- Use para: deixar o atendimento no **Aguardando** do Setor, para quem estiver livre.
- Cuidado: o Setor precisa ter gente cadastrada. Avise o cliente, antes do bloco, do que vai acontecer e de quando alguém responde.

**Operador** · `references/docs/recursos/bloco-operador.md` · JSON: não
- Use para: entregar a uma pessoa específica. Chega em **Atendendo**, ou em **Aguardando (MEUS)** conforme as configurações da empresa.

**Rodízio** · `references/docs/recursos/bloco-rodizio.md` · JSON: não
- Use para: distribuir entre atendentes, por percentual ou por rodada sorteada.
- Cuidado: no modo equilibrado, as porcentagens somam exatamente 100. Escolha sempre o Setor de **Se não encontrar operador disponível**.

**Retornar último atendimento** · `references/docs/recursos/bloco-retornar-ultimo-atendimento.md` · JSON: não
- Use para: devolver ao mesmo Setor e atendente quem voltou logo, junto com a Condição **Protocolo fechado**. Ligue a saída **Sem atendimento anterior**.

**GPT Assistant (OpenAI)** · `references/docs/recursos/bloco-gpt-assistant-openai.md` · JSON: não
- Use para: passar a conversa ao assistente de IA ligado a um Setor.
- Cuidado: o bloco não cria nem configura o assistente; isso é a skill `cmv-agente-ia`. Sem **Sem resposta**, o bloco não tem saída.

**Typebot** · `references/docs/recursos/bloco-typebot.md` · JSON: não
- Use para: passar a conversa a um robô do Typebot ligado a um Setor.

**Trocar Fluxo** · `references/docs/recursos/bloco-trocar-fluxo.md` · JSON: não
- Use para: dividir um fluxo grande em vários, ou levar a conversa ao **Aguardando** em fluxos disparados por resposta rápida, remarketing ou campanha.
- Cuidado: pede um Setor **com fluxo ligado**. Não há volta automática. A manda para B e B manda para A sem condição de parada é laço infinito. Não confunda com o bloco Setor, que deixa a conversa esperando a equipe.

**Encerrar** · `references/docs/recursos/bloco-encerrar.md` · JSON: `close`
- Use para: terminar o fluxo e fechar o atendimento, com mensagem final opcional.

**Encerrar Mensagem Rápida** · `references/docs/recursos/bloco-encerrar-mensagem-rapida.md` · JSON: não
- Use para: terminar o fluxo chamado por uma resposta rápida e devolver a conversa ao atendente. Um Encerrar comum fecharia o atendimento no meio da conversa da equipe.

## Onde cada bloco funciona

Só o que os artigos dizem; para os demais blocos, a documentação não restringe o canal.

| Bloco | Onde |
|---|---|
| Template, Carrossel de Produtos | só conexão do WhatsApp Oficial |
| Webview | só WhatsApp QRCode, com botões liberados |
| Enviar Figurinha | WhatsApp QRCode e WhatsApp Oficial; nos outros o bloco é pulado |
| Botões | todos os canais, com quantidades e tipos diferentes; nos canais do HUB as opções chegam numeradas em texto; no WhatsApp QRCode, depende do recurso de botões liberado no plano; no WebChat, os de **Quick Reply** chegam clicáveis |
| Menu (Texto, Lista, Botões) | **não documentado por canal.** O artigo descreve os três tipos sem dizer onde cada um funciona; as únicas menções a canal são que o **Rodapé da Lista** pode não aparecer e que, no **WebChat**, o **Menu em Lista** abre no chat do site pelo botão da lista. O que os artigos dizem sobre botões por canal é do bloco **Botões**, não do Menu. O **Menu em Texto** é só texto com as opções numeradas, e o cliente responde com o número. |
| É Seguidor?, Responder Comentário, Condição de Postagem e de Tipo de Postagem | conversas do Instagram |
| Pixel META no formato Mensagens do WhatsApp | elegível só no WhatsApp Oficial, para quem veio de anúncio |
| Condição de Anúncio | qualquer conexão de WhatsApp |
