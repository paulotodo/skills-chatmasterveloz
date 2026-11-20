# Entendendo PABX

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/entendendo-pabx
- **Categoria:** Recursos
- **Menu:** Ligações › Entendendo PABX

---

🧩 **O PABX (Private Automatic Branch Exchange)** é o "cérebro" da telefonia da sua empresa. Antes de sair clicando e configurando o sistema, é fundamental entender a lógica de como as ligações entram, circulam e saem da sua plataforma.

☑️ **Organização Lógica:** Entenda o fluxo da chamada para nunca deixar um cliente "cair no vazio" quando ligar para você.

☑️ **Economia e Inovação:** Crie rotas inteligentes usando números **VoIP** tradicionais ou até mesmo **WhatsApp** direto na plataforma.

☑️ **Segurança:** Saiba como bloquear chamadas indesejadas e restringir para onde seus funcionários podem ligar.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ O **Tronco** é a conexão com o mundo exterior (seja uma Operadora SIP ou o seu número de WhatsApp).
>
> ➡️ O **Ramal** é a linha individual de cada atendente da sua equipe.
>
> ➡️ A **Rota de Entrada** dita o que acontece quando alguém liga *para* a sua empresa.
>
> ➡️ A **Rota de Saída** dita por onde a ligação passa quando um atendente realiza uma chamada.

## **O Mapa Lógico do PABX**

Para configurar qualquer PABX, você precisa dominar estes quatro elementos principais. Eles funcionam como "blocos" que se conectam.

#### ⚡ **TRONCO (A Porta para a Rua)**

É a sua linha de comunicação com o mundo exterior. Tradicionalmente, é uma conexão fornecida por uma operadora de telefonia (SIP/VoIP). **A grande inovação é que, no nosso sistema, o WhatsApp (API Oficial Cloud ou QR Code) também funciona como um Tronco!**

◽ **O que estamos configurando:** A porta de entrada e saída das chamadas. Sem um tronco ativo, o PABX é um sistema fechado.

**◽ Exemplo prático:** Você pode ter um tronco VOIP, outro WhatsApp, e até mesmo mais de um desses com outros números.

#### ⚡ **RAMAL (O Telefone na Mesa)**

É a extensão interna da sua empresa. É a conta que o atendente usa na plataforma (Perfil do Usuário), ou no aplicativo do computador (Softphone) ou no aparelho de mesa (Telefone IP).

◽ **O que estamos configurando:** O número de identificação do usuário.

**◽ Exemplo prático:** Ramal 200 para o Vendedor A, Ramal 201 para o Vendedor B. Os ramais podem atender e receber ligações externas, e podem conversar entre si também.

#### ⚡ **ROTA DE ENTRADA (A Recepcionista)**

Também chamada de *Inbound Route*. É a regra que o PABX obedece no exato momento em que um Tronco recebe uma ligação externa.

◽ **O que estamos configurando:** O destino inicial do cliente. Se o cliente ligar, quem deve atender primeiro?

**◽ Exemplo prático:** Você cria uma regra dizendo: "Quando ligarem para o did/número X, mande a chamada para a URA (Menu de Voz) ou direciona direto para um ramal.

#### ⚡ **ROTA DE SAÍDA (O Porteiro / Segurança)**

Também chamada de *Outbound Route*. É a regra que o PABX obedece quando o atendente tenta ligar para um cliente.

◽ **O que estamos configurando:** As permissões e a escolha inteligente de qual Tronco usar para fazer aquela ligação, visando economia e segurança.

◽ **Exemplo prático:** Você cria regras de discagem, formatação de números, backup de troncos, entre outros."

> **[DUVIDAS]**
>
> ### Dúvidas Comuns
>
> **Qual é a ordem correta para começar a configurar um PABX do zero?** Existe uma ordem lógica universal: 1º Crie os **Ramais** (para ter quem atenda). 2º Configure os **Troncos** (para ter conexão com o mundo). 3º Crie as **Rotas de Saída e Entrada** (para ligar os ramais aos troncos).
>
> **Posso ter um PABX só com ramais e sem tronco?** Sim. Funciona como um intercomunicador interno. Ideal para hospitais, hotéis ou fábricas grandes onde os funcionários precisam se falar rapidamente e de graça, mas não precisam ligar para clientes na rua.
>
> **O que é a URA nessa história?** A URA (Atendimento Automático) é um "destino" interno. Quando a ligação vem do Tronco, a Rota de Entrada geralmente joga o cliente na URA, e a URA distribui para os Ramais.
