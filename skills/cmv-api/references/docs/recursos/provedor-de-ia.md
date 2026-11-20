# Provedor de IA

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/provedor-de-ia
- **Categoria:** Recursos
- **Menu:** Integrações › Provedor de IA

---

🧩 O card **Provedor de IA**, no menu **Integrações**, escolhe o serviço de inteligência artificial da sua empresa. Nas palavras da tela: *"Escolha qual serviço de IA responde os prompts de chat. Deixe em OpenAI para manter o comportamento atual."*

Com um provedor diferente da OpenAI, o card guarda também o modelo e a chave desse serviço. Para quem tem um servidor de IA próprio, a opção **Local (Ollama / vLLM)** aponta para o endereço dele.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Integrações** e localize o card **Provedor de IA**.
>
> ➡️ Escolha o **Provedor**.
>
> ➡️ Confira o **Modelo**, que muda junto com o provedor escolhido, e cole a **Chave de API do provedor**: fora da OpenAI, os dois são obrigatórios. Com **Local (Ollama / vLLM)**, preencha também a **URL do servidor**.
>
> ➡️ Não há botão Salvar: o **Provedor** grava assim que é escolhido, e a **Chave de API do provedor** quando você sai do campo, com o aviso *"Configuração atualizada com sucesso!"*.

## Como configurar o Provedor de IA

Acesse o menu **Integrações**

🔘 **Provedor:** o serviço de IA. As opções são **OpenAI**, **Groq**, **DeepSeek**, **Mistral**, **xAI (Grok)**, **OpenRouter** e **Local (Ollama / vLLM)**.

🔘 **Modelo:** o nome do modelo, como o provedor o publica. A tela avisa: *"O modelo precisa existir no provedor escolhido."* Ao trocar o **Provedor**, o **Modelo** muda sozinho para um modelo do provedor novo, mesmo que você tenha digitado outro antes. Fora da OpenAI, o **Modelo** é obrigatório. Na **OpenAI**, o campo fica vazio, e a tela explica: *"Na OpenAI vale o modelo padrão e a chave da seção OpenAI, acima."*

🔘 **Modelo de transcrição:** nas palavras da tela, *"Usado para transcrever áudios recebidos. Vazio, usa o padrão do provedor. Provedores sem transcrição continuam usando a OpenAI."*

🔘 **Chave de API do provedor:** a chave criada na sua conta do provedor escolhido. O campo esconde a chave, e o ícone **Mostrar a chave** a deixa à vista. A chave é gravada quando você sai do campo, uma vez só, e não a cada letra digitada. Fora da OpenAI, a chave é obrigatória. Nas palavras da tela: *"Obrigatória para este provedor: sem ela a IA não responde."*

🔘 **URL do servidor:** aparece só com o provedor **Local (Ollama / vLLM)**. Nas palavras da tela, *"Endereço do seu servidor de IA, incluindo /v1 no final."* O exemplo do campo é `http://192.168.0.10:11434/v1`.

## O Provedor de IA no prompt e nas falhas

Na janela do prompt, no menu **Prompts OPEN.AI**, o campo **Modelo da IA** abre com a opção **Modelo do provedor**, que mostra entre parênteses o modelo do provedor que vale para a empresa.

Quando a IA falha, por exemplo porque o provedor recusou a chave, o motivo fica registrado no menu **Erros do Sistema**, com o recurso e o atendimento, como *"o provedor recusou a chave de acesso"*.

Quando falta alguma coisa no card **Provedor de IA**, a própria IA avisa o motivo e aponta o card:

➡️ **Chave vazia:** *"Preencha a Chave de API do provedor em Integrações → Provedor de IA (o campo está vazio)."*

➡️ **Chave recusada:** *"O provedor de IA recusou a chave de API. Confira a chave em Integrações → Provedor de IA."*

➡️ **Modelo vazio:** *"Escolha o modelo do provedor em Integrações → Provedor de IA (o campo Modelo está vazio)."*

⚠️ **Uma chave para todos os provedores.** O card guarda uma única **Chave de API do provedor**. Trocar o **Provedor** não apaga a chave, mas ela continua sendo a do provedor anterior: depois de trocar, cole a chave do provedor novo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Troquei o Provedor de IA. Preciso colar a chave de novo?** Sim. O card guarda uma chave só, e ela continua sendo a do provedor anterior. Cole a chave do provedor novo em **Chave de API do provedor**.
>
> **Troquei o Provedor de IA e o Modelo mudou sozinho. Está certo?** Está. Ao trocar o **Provedor**, o campo **Modelo** passa para um modelo do provedor novo, mesmo que você tenha digitado outro antes. Para usar outro modelo, digite o nome dele depois de escolher o provedor.
>
> **Com a OpenAI, preciso preencher o Modelo e a Chave de API do provedor?** Não. Na OpenAI, os dois campos do card **Provedor de IA** não são obrigatórios, e a tela explica: *"Na OpenAI vale o modelo padrão e a chave da seção OpenAI, acima."*
>
> **Como volto para a OpenAI no Provedor de IA?** Escolha **OpenAI** no campo **Provedor**. Nas palavras da tela, deixar em OpenAI mantém o comportamento atual.
>
> **O campo URL do servidor não aparece no Provedor de IA.** Ele só aparece com o provedor **Local (Ollama / vLLM)**.
>
> **A IA parou de responder depois que troquei o Provedor de IA. Onde vejo o motivo?** No menu **Erros do Sistema**, que registra as falhas da IA com o motivo. Confira também se a **Chave de API do provedor** é a do provedor novo.
>
> **O card Provedor de IA não aparece no menu Integrações.** Fale com o suporte.
