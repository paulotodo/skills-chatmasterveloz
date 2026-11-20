# Token OpenAI

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/token-openai
- **Categoria:** Recursos
- **Menu:** Integrações › Token OpenAI

---

🔑 O **token da OpenAI** é uma chave de acesso exclusiva que permite nosso sistema se comunicar com os serviços da OpenAI. Funciona como uma espécie de senha, permitindo o uso seguro e privado entre as plataformas.

Essa integração é essencial para ativar as funcionalidades de inteligência artificial em nossa plataforma, a não ser que a sua conta use a chave da plataforma.

#### 💡 Uma chave, vários recursos

O mesmo token alimenta a IA que responde o cliente pelo prompt (**GPT Assistant**), a transcrição de áudio, a análise de atendimento, o resumo do atendimento, a sugestão de resposta do **Copiloto de mensagens** e a IA nas gravações das chamadas, que transcreve, legenda e analisa cada gravação. E é na conta dona desta chave que a OpenAI cobra o consumo: com o token que você cadastra aqui, a cobrança é na sua conta da OpenAI.

Quando a sua conta usa a chave da plataforma, o card **OPEN.AI** do menu **Integrações** avisa: *"A inteligência artificial desta conta usa a chave da plataforma. Não é preciso cadastrar uma chave aqui."* Nesse caso, não há token a criar nem a colar: o campo **Token OpenAI** some do card, e **Model OpenAI** e **Idioma OpenAI** continuam nele. A IA que responde o cliente pelo prompt (**GPT Assistant**), a transcrição de áudio, a análise de atendimento, o resumo do atendimento, o **Copiloto de mensagens** e a IA nas gravações das chamadas passam a usar a chave da plataforma.

## Como criar um Token da OPENAI

**✅** Acesse o site da OpenAI: [https://platform.openai.com](https://platform.openai.com)

**➡️** Faça um login na OpenAI (ou se cadastre antes caso não tenha um login)

**➡️** Navegue até → Dashboard > API Keys

**➡️** Clique em → Create New Secret Key para gerar um novo token

![Painel da OpenAI na área API Keys, com o botão para criar uma nova chave](https://clihelper.chatmasterveloz.com/docs-imagem/22123-openAi-apikey-criar-1024x528.jpg)

**➡️** Digite um nome qualquer para sua chave e clique em Criar (Create)

![Janela da OpenAI para dar um nome à nova chave e criá-la](https://clihelper.chatmasterveloz.com/docs-imagem/22123-openAi-apikey-salvar.jpg)

**➡️** Copie o token gerado e mantenha-o em um local seguro

![Janela da OpenAI com a chave gerada, pronta para copiar](https://clihelper.chatmasterveloz.com/docs-imagem/22123-openAi-apikey-copiar.jpg)

## Como Integrar a OpenAI à nossa plataforma

Em nosso sistema, acesse o menu **Integrações** e, no card **OPEN.AI**, configure os campos. Cada campo grava sozinho quando você cola ou digita o valor, sem botão Salvar.

#### Token OpenAI

Coloque seu token OpenAI. O campo esconde a chave, como um campo de senha: o botão **Mostrar a chave** exibe o que está gravado, e **Esconder a chave** volta a escondê-la.

#### Model OpenAI

O sistema já usa por padrão o modelo “whisper-1” para transcrição de áudio. **Deixe vazio** para manter o padrão, ou coloque o nome de outro modelo se desejar.

#### Idioma OpenAI

**Deixe vazio** para manter o padrão.

⚠️ Na conta que cadastra a própria chave, a IA nas gravações das chamadas usa a chave do campo **Token OpenAI**. Uma chave colocada em outro campo de IA da página **Integrações** não serve para as gravações.

## Boas Práticas para Gerenciar seu Token

**➡️ Não compartilhe seu token com terceiros**: Ele é único, dá acesso direto às funções na OpenAI, inclusive à parte financeira.

**➡️ Regenere o token periodicamente**: Caso suspeite de vazamentos ou uso indevido, gere um novo token no painel da OpenAI e substitua no local desejado.

**➡️ Verifique os limites de uso**: Tokens podem estar associados a custos, dependendo do volume de requisições feitas à API. Consulte sua conta na OpenAI para mais detalhes sobre tarifas.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **As gravações das chamadas não estão sendo transcritas. Onde coloco o Token OpenAI?** No menu **Integrações**, no card **OPEN.AI**, campo **Token OpenAI**. Confira também a opção **IA nas gravações das chamadas**, no menu **Configurações  ›  Opções  ›  Chamadas**. Gravações feitas antes de a chave entrar não são transcritas depois; as seguintes, sim.
>
> **O card OPEN.AI diz que a conta usa a chave da plataforma. Preciso criar um Token OpenAI?** Não. Com a chave da plataforma, não há token a criar nem a colar no card **OPEN.AI**. Se a IA parar de responder nesse caso, fale com o suporte.
