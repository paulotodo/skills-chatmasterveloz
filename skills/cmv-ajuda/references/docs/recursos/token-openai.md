# Token OpenAI

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/token-openai
- **Categoria:** Recursos
- **Menu:** Integrações › Token OpenAI

---

🔑 O **token da OpenAI** é uma chave de acesso exclusiva que permite nosso sistema se comunicar com os serviços da OpenAI. Funciona como uma espécie de senha, permitindo o uso seguro e privado entre as plataformas.

Essa integração é essencial para ativar as funcionalidades de inteligência artificial em nossa plataforma.

#### 💡 Uma chave, todos os recursos

O mesmo token alimenta tudo o que usa IA aqui: transcrição de áudio, análise de atendimento, GPT Assistant, a sugestão de resposta do **Copiloto de mensagens** e a IA nas gravações das chamadas, que transcreve, legenda e analisa cada gravação. E é na conta dona desta chave que a OpenAI cobra o consumo — por isso ela é sua, e não da plataforma.

## Como criar um Token da OPENAI

**✅** Acesse o site da OpenAI: [https://platform.openai.com](https://platform.openai.com)

**➡️** Faça um login na OpenAi (ou se cadastre antes caso não tenha um login)

**➡️** Navegue até → Dashboard > API Keys

**➡️** Clique em → Create New Secrete Key para gerar um novo token

![Painel da OpenAI na área API Keys, com o botão para criar uma nova chave](https://clihelper.chatmasterveloz.com/docs-imagem/22123-openAi-apikey-criar-1024x528.jpg)

**➡️** Digite um nome qualquer para sua chave e clique em Criar (Create)

![Janela da OpenAI para dar um nome à nova chave e criá-la](https://clihelper.chatmasterveloz.com/docs-imagem/22123-openAi-apikey-salvar.jpg)

**➡️** Copie o token gerado e mantenha-o em um local seguro

![Janela da OpenAI com a chave gerada, pronta para copiar](https://clihelper.chatmasterveloz.com/docs-imagem/22123-openAi-apikey-copiar.jpg)

## Como Integrar a OpenAI à nossa plataforma

Em nosso sistema, acesse o menu **Integrações** e, no card **OPEN.AI**, configure os campos. Cada campo grava sozinho quando você cola ou digita o valor, sem botão Salvar.

#### Token OpenAI

Coloque seu token OpenAI.

#### Model OpenAI

O sistema já usa por padrão o modelo “whisper-1” para transcrição de áudio. **Deixe vazio** para manter o padrão, ou coloque o nome de outro modelo se desejar.

#### Idioma OpenAI

**Deixe vazio** para manter o padrão.

⚠️ A IA nas gravações das chamadas usa a chave do campo **Token OpenAI**. Uma chave colocada em outro campo de IA da página **Integrações** não serve para as gravações.

## Boas Práticas para Gerenciar seu Token

**➡️ Não compartilhe seu token com terceiros**: Ele é único, dá acesso direto às funções na OpenAI, inclusive à parte financeira.

**➡️ Regenere o token periodicamente**: Caso suspeite de vazamentos ou uso indevido, gere um novo token no painel da OpenAI e substitua no local desejado.

**➡️ Verifique os limites de uso**: Tokens podem estar associados a custos, dependendo do volume de requisições feitas à API. Consulte sua conta na OpenAI para mais detalhes sobre tarifas.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **As gravações das chamadas não estão sendo transcritas. Onde coloco o Token OpenAI?** No menu **Integrações**, no card **OPEN.AI**, campo **Token OpenAI**. Confira também a opção **IA nas gravações das chamadas**, no menu **Configurações  ›  Opções**. Gravações feitas antes de a chave entrar não são transcritas depois; as seguintes, sim.
