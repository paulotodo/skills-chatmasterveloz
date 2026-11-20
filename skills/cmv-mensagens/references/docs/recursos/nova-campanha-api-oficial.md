# Nova Campanha API Oficial

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/nova-campanha-api-oficial
- **Categoria:** Recursos
- **Menu:** Campanhas › Nova Campanha API Oficial

---

🧩 A campanha pela **API Oficial** dispara um template já aprovado pela Meta para uma lista de contatos. Acesse o menu **Campanha** e clique no botão **NOVA CAMPANHA**.

![Tela de criação de uma nova campanha pela API Oficial](https://clihelper.chatmasterveloz.com/docs-imagem/25291-campanhas-nova-oficial.jpg)

## Definindo sua Campanha

### ⚡ PASSO 01

Configurações básicas:

➡️ **Nome:** escolha um nome para essa campanha.

➡️ **Gatilho:** não utilize na API Oficial.

➡️ **Caracteres Ocultos:** não utilize na API Oficial.

➡️ **Usar Proxy:** opção avançada para roteamento de tráfego do envio por um IP intermediário. Normalmente setado como **Não**.

### ⚡ PASSO 02

Defina uma fonte de contatos destinatários escolhendo apenas uma opção entre:

**➡️ Lista de Contato:** que você adicionou no menu **Criar Lista** ou em campanhas anteriores.

**Obs 1:** essa lista não tem relação com o menu principal **Contatos**.

**Obs 2:** para enviar templates com variáveis é preciso escolher essa fonte de contato (veja no final como preencher).

**➡️ Tags:** conversas que possuem uma tag específica.

**➡️ Grupos:** participantes de um grupo específico (a mensagem será enviada no privado para cada participante).

**➡️ Aniversário:** contatos que fazem aniversário em um mês específico.

### ⚡ PASSO 03

Agendando o tempo de envio das mensagens.

**➡️ Agendamento:** data e horário que a campanha iniciará os disparos.

**➡️ Pausar automaticamente:** horário que os disparos devem ser interrompidos no dia atual. Deixe vazio para continuar sem interrupção.

**➡️ Reiniciar Automaticamente:** caso tenha definido um horário para interromper, defina agora um horário para a campanha reiniciar após essa interrupção.

### ⚡ PASSO 04

Ajustando o atendimento ao cliente.

**➡️ Abrir Ticket:** escolha se o ticket da conversa deve permanecer aberto (status Aguardando) após o envio da campanha. Se optar por não abrir ticket, o mesmo será fechado após o envio da campanha, mesmo que ele já esteja em atendimento.

**➡️ Fila:** defina uma fila para o ticket permanecer caso você opte por abrir Ticket. Se optar por utilizar Fluxo de Automação, a Fila deve estar vinculada ao Fluxo.

**➡️ Mensagem de Descadastramento:** não utilize na API Oficial.

**➡️ Conexão:** escolha apenas uma conexão. Não utilize multiconexões quando for API Oficial.

### ⚡ PASSO 05

Escolha um template pré-cadastrado em sua conta business da Meta.

**TEMPLATE SEM VARIÁVEL**

Apenas selecione o template desejado.

**➡️ Fluxos de Automação:** inicia a automação de um fluxo do **Flowbuilder Nativo** após a resposta do contato. (**Importante:** definir no campo Fila, uma fila vinculada ao mesmo Fluxo de Automação selecionado aqui).

**TEMPLATE COM VARIÁVEL**

Para enviar um template **com variáveis** é preciso que a fonte de contato seja exclusivamente uma **Lista de Contato** enviada no menu **Criar Listas**.

Na planilha você deve preencher:

**nome**: nome do contato.

**numero**: telefone no formato internacional, somente números.

**e-mail**: email do contato se desejar.

**extra1**: url da imagem do cabeçalho da mensagem template.

**extra2**: o valor desejado para a variável `{{1}}` de sua mensagem template.

**extra3**: o valor desejado para a variável `{{2}}` de sua mensagem template.

**extra4**: o valor desejado para a variável `{{3}}` de sua mensagem template.

**extra5**: o valor desejado para a variável `{{4}}` de sua mensagem template.

**extra6**: o valor desejado para a variável `{{5}}` de sua mensagem template.

**extra7**: texto do 1º botão.

**extra8**: texto do 2º botão.

**extra9**: texto do 3º botão.
