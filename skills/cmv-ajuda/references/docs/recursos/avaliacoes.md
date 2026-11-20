# Avaliações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/avaliacoes
- **Categoria:** Recursos
- **Menu:** Atendimento Otimizado › Avaliações

---

**Avaliações** de clientes permitem o gestor mensurar a qualidade do atendimento, produtos ou serviços de seu negócio.

Você pode implementar uma solicitação de **avaliação** ao seu cliente no final de um atendimento. Podendo inclusive criar mais de um modelo de avaliação, para enviar o respectivo conforme cada tipo de atendimento.

**Passos para configurar uma Avaliação**

**➡️** Criar uma Avaliação

**➡️** Definir Mensagem de pós Avaliação

**➡️** Configurações: -> enviar avaliações -> obrigatório avaliar? -> avaliação externa? -> tempo de espera

## Criar uma Avaliação

No menu Avaliações

Clique em Adicionar

➡️ Defina um **nome para sua avaliação** (apenas para sua referência)

➡️ Defina a **Mensagem de Avaliação**. Ex: "Como você avalia nosso atendimento?"

➡️ Em **Enviar como Lista de Opções**, escolha se as opções serão enviadas como lista ou como texto.

➡️ **Sempre enviar pelo WhatsApp:** nas palavras da tela, *"No atendimento pelo Chat Externo, a avaliação vai para o WhatsApp do cliente, onde ele costuma responder. Sem WhatsApp do cliente, ela continua indo para a página."*

**➡️ NPS Interno (Operador)** - Em breve

**➡️ Opções de Avaliação** clique em "+ Adicionar Opção" para criar as opções de respostas à sua avaliação.

➡️ Em cada opção, o campo **Fluxo após esta nota** escolhe o fluxo que começa quando o cliente responde com aquela nota. Em **Nenhum (envia a Mensagem de Avaliação da conexão)**, a nota não começa fluxo e o cliente recebe a **Mensagem de Avaliação** da conexão.

## ![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/20817-avaliacao-adicionar.jpg)Definir Mensagem de pós Avaliação

No menu Conexões

Ao editar uma conexão, defina sua mensagem de pós avaliação no campo "**Mensagem de Avaliação**". Essa mensagem é enviada depois que o cliente escolhe a nota, quando a opção dessa nota está em **Nenhum** no campo **Fluxo após esta nota**. A nota com fluxo começa o fluxo, e a **Mensagem de Avaliação** não é enviada.

## Configurar Avaliação

No menu Configurações

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/20817-config-avaliacoes.jpg) ![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/20817-configs-tempo.jpg)

## Enviar Avaliações

Ativando essa funcionalidade, ao encerrar um atendimento aparecerá um botão "**Resolver e Enviar Avaliação**".

Para utilizar esse novo botão é obrigatório escolher **um menu de avaliação** (que deve ser previamente cadastrado no menu principal → Avaliações)

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/20817-configs-avaliar-sim.jpg)

## Obrigatório Avaliar?

Com essa função ativa, ao encerrar um atendimento o atendente terá apenas como opção o botão "**Resolver e Enviar Avaliação**".

Ou seja, para encerrar o atendimento é obrigatório utilizar esse botão combinado com a escolha de **um menu de avaliação** (que deve ser previamente cadastrado no menu principal → Avaliações)

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/20817-configs-avaliar-obrigatorio.jpg)

## Avaliação Externa? (URL da Avaliação Externa)

Quer utilizar uma pesquisa externa para medir seus atendimentos?

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/20817-config-avaliar-externa.jpg)Sem problemas, ative a opção "**Avaliação Externa**" e no campo **URL da Avaliação Externa** digite seu link completo, podendo inclusive utilizar **mustaches**, que são variáveis do sistema, para levar a informação do ticket para seu sistema de avaliação próprio.

➡️ Exemplo: `https://avaliachat.com.br/{{ticket_id}}/{{number}}`

Será enviado ao cliente algo como: `https://avaliachat.com.br/23453/5511999998888`

> **[ATENCAO]**
>
> #### Atenção
>
> Mesmo sendo uma avaliação externa, para encerrar o atendimento, o sistema também obrigará escolher um menu de avaliação (que deve ser previamente cadastrado no menu principal Avaliações )
>
> O sistema irá ignorar a avaliação interna, e enviar a sua URL.

## Tempo de Espera para Receber Avaliação

Defina seu tempo de espera para receber uma avaliação.

Após o envio de uma avaliação interna, a **primeira resposta** que o cliente enviar não irá aparecer na plataforma caso esteja dentro do tempo definido nessa opção.

Garantindo que o atendente não tenha acesso direto a resposta da avaliação.

Para ver a avaliação, o administrador acessa o menu **Relatório de Avaliações**.

## Relatório de Avaliações

Acesse o menu **Relatório de Avaliações**. Cada linha traz a **Data**, o **Cliente**, o **Operador**, o **Setor**, o **Modelo** de avaliação, a **Opção** escolhida e a **Nota**.

Quando o fluxo da nota guarda a resposta de uma **Pergunta** num bloco **Variável** logo depois, a resposta fica na avaliação. A coluna **Nota** ganha um selo com o número de respostas, com a dica *"1 resposta(s) do cliente no fluxo da nota"*, e o botão **Ver detalhes**, na coluna **Ações**, abre a janela **Detalhes da avaliação**: o bloco **Respostas do fluxo da nota** mostra a pergunta, a **Variável** e a data de cada resposta, e embaixo o que o cliente respondeu.

O botão **Exportar CSV** baixa as avaliações num arquivo, que traz também a coluna **Respostas do fluxo**.
