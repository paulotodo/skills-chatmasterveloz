# Alertas Vermelhos no Chat

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/alertas-vermelhos-no-chat
- **Categoria:** Recursos
- **Menu:** Chats / Tickets › Alertas Vermelhos no Chat

---

🧩 Recados com **fundo vermelho dentro do chat** são avisos do sistema para orientar o atendente sobre algum erro. Muitos desses alertas são em inglês pois vem direto da Meta ou outras integrações. Veja abaixo uma lista de retornos de erro, seus significados e possíveis soluções:

#### 🚨 Missing Phone in Payload ou Could not parse Phone

O sistema está tentando enviar alguma **mensagem automática** para o WhatsApp particular do atendente operador, porém o **número** digitado no Perfil está **vazio**, incompleto ou com espaços extras.

☑️ No menu **Perfil**, no campo **Número**, digite o número do WhatsApp no formato internacional, usando apenas números e testando com 8 ou 9 dígitos.

#### 🚨 Missing Body in Payload

O sistema está tentando enviar alguma **mensagem automática**, porém essa mensagem está com o **campo de texto vazio**, ou seja, sem texto definido.

☑️ A **solução** é desativar o contexto / condição da automação de envio de mensagem, ou então preencher a mensagem com um texto.

Segue uma lista de condições e campos de mensagens que você deve observar:

➡️ No menu **Configurações**, a opção **Mensagem de Saudação do Operador** marcada como **Sim** e o **Texto de Saudação** vazio.

#### 🚨 "#1 Error sending message to LID: failed to encrypt message: can't encrypt message for device: no signal session established with xxxxxxxxxxx"

O sistema tentou enviar uma mensagem, mas **não** encontrou a "chave de criptografia" da sua conexão WhatsApp nessa conversa.

☑️ Tente resolver no menu **Conexões  ›  3 pontinhos  ›  Reiniciar Conexões**.

Se não resolver será necessário **Reler o QR Code** dessa conexão.

#### 🚨 Erro ao montar mensagem: if a ButtonReply is present, other button types are not allowed

Você tentou enviar uma mensagem que contém **Botões de Resposta Rápida** (ButtonReply ou Quick Reply - aqueles que o usuário clica para responder texto) junto com outro tipo de botão (como Botão de Link, Botão de Telefone ou Lista) no mesmo balão.

☑️ Botões do tipo Quick Reply não aceitam envio junto com outros botões - utilize somente Quick Reply nessa chamada API.

#### 🚨 Este número não está no WhatsApp. A mensagem não foi enviada.

O número do cliente **não tem conta de WhatsApp**. A plataforma passou a avisar isso com todas as letras, no idioma de cada atendente — antes, esse mesmo caso aparecia como um código técnico. O aviso aparece também nas conversas antigas, ao espiar um atendimento e no relatório do atendimento.

☑️ Confirme o número com o cliente por outro canal. Confira o código do país e o DDD — e, em DDD acima de 30, se não sobrou um nono dígito, que transforma o número em outro.

#### 🚨 Message Undeliverable.

Este é um erro genérico de **falha na entrega**. Significa que a mensagem foi enviada pelo servidor, chegou na Meta, mas **não pôde ser entregue** ao dispositivo do cliente final. Aqui o problema está no **destinatário**. As causas mais comuns (90% dos casos) são:  
- **Bloqueio:** O cliente bloqueou o seu número/empresa no WhatsApp.
- **Número Inválido:** O número não possui uma conta de WhatsApp ativa no momento. Quando a plataforma consegue identificar esse caso, ela mostra o aviso próprio **Este número não está no WhatsApp**, descrito acima.

#### 🚨 Re-engagement message Message failed to send because more than 24 hours have passed since the customer last replied to this number.

Janela de Atendimento ao Cliente está **fechada**.

☑️ Você pode enviar uma **Mensagem Template** nesse cenário, mas a janela abrirá somente quando o cliente enviar uma mensagem.

#### 🚨 This message was not delivered to maintain healthy ecosystem engagement. In order to maintain a healthy ecosystem engagement, the message failed to be delivered.

A Meta decidiu bloquear a entrega dessa mensagem de propósito (Código 131049).  
1. O sistema anti-spam deles detectou que o número **remetente** está com uma taxa muito alta de rejeição. Em operações de disparo em massa, isso geralmente significa que os clientes finais estão bloqueando o número, denunciando como spam, ou simplesmente ignorando as mensagens. (verifique a saúde do seu número no Gerenciador de WhatsApp da Meta)
2. Ou se esse erro acontece logo nos **primeiros disparos** de uma conta legítima que não faz spam, o algoritmo da Meta não está te punindo por um histórico ruim, mas sim agindo de forma superprotetora por causa de um **comportamento atípico**. Como a conta é nova (ou estava parada), a Meta ainda não "confia" nesse número.
3. Ou o que você presenciou é o efeito de uma regra oficial (porém um pouco silenciosa) do WhatsApp chamada **Limite de Mensagens de Marketing por Usuário** (*Per-User Marketing Limits*).

O algoritmo não avalia apenas a sua empresa, ele avalia a **saturação do usuário**. A Meta rastreia quantas mensagens promocionais aquele número específico recebeu recentemente de *todas* as empresas no WhatsApp. Se o sistema entender que aquele usuário já atingiu o limite de propagandas toleráveis para o dia ou para a semana, a Meta cria um "escudo" para proteger aquele usuário do excesso de ofertas no geral.

**Nessa situação** normalmente é aceitável o envio de **Mensagem Template de Utilidade**, pois a Meta entende que esse tipo de mensagem é crítica - afinal, é o aviso de rastreio de produto, um boleto a vencer, ou um código de acesso.

#### 🚨 Unsupported post request. Object with ID 'xxxxxxxxxx' does not exist, cannot be loaded due to missing permissions, or does not support this operation. Please read the Graph API documentation at developers.facebook.com/docs/graph-api

Provavelmente aconteceu uma **perda de conexão** com o token de acesso da Meta.

☑️ **Reconectar** sua Conexão na plataforma normalmente revalida esse token e volta a funcionar.

#### 🚨 (#131008) Required parameter is missing

Você **deixou** de enviar um campo que é obrigatório para que a mensagem seja processada.

☑️ Verifique se preencheu todas as **Variáveis** definidas na Mensagem Template aprovada pela Meta.

#### 🚨 (#132000) Number of parameters does not match the expected number of params

A **quantidade** de variáveis que você enviou não é igual à quantidade que o Template exige.

☑️ Verifique se a quantidade de **Variáveis** enviadas corresponde a quantidade definida na Mensagem Template aprovada pela Meta.

#### 🚨 (#132012) Parameter format does not match format in the created template

Há um conflito entre o **tipo de dado** que a Mensagem Template espera e o que você enviou.

☑️ Certifique-se de que os componentes (HEADER, BODY) e seus parâmetros (image, text, currency, etc.) correspondem exatamente à configuração do modelo aprovado na Meta.

#### 🚨 Media upload error Downloading media from weblink failed with http code 403, status message Forbidden

Você tentou enviar uma **Mensagem Template** que contém uma imagem ou arquivo no cabeçalho (Header). O sistema precisa baixar essa mídia de um link público que você forneceu, mas o servidor onde a imagem está hospedada **bloqueou** o acesso para baixar o arquivo.

☑️ **Teste Anônimo:** Copie o link e tente abrir em uma **Guia Anônima** do navegador. Se der erro ou pedir login, é esse o problema.

☑️ **Permissões de Cloud:** Se a imagem está em um bucket (S3, Google Cloud, Firebase), altere a permissão do arquivo para **"Public Read"** (Leitura Pública).

☑️ **Links Temporários:** Se você usa links assinados (que expiram), verifique se ele não expirou antes do envio.

#### 🚨 "message": "Request failed with status code 404"

O sistema tentou acessar uma página inexistente, gerando um **Erro 404**. O alerta traz um bloco de detalhes; nele, o endereço exato que falhou está no campo **"url"**, e o campo **"data"** contém os detalhes do evento disparado.

☑️ Acesse o menu **Configurações  ›  Opções  ›  Webhooks | Eventos** e identifique qual evento está vinculado a essa URL problemática.
