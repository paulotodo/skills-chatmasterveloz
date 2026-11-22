# Base de Conhecimento do GPT Assistant

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/base-de-conhecimento-do-gpt-assistant
- **Categoria:** Recursos
- **Menu:** Inteligência Artificial › GPT Assistant › Base de Conhecimento do GPT Assistant

---

🧩 A IA do seu atendimento chuta o horário de funcionamento ou não sabe a política de trocas? A **Base de Conhecimento** é o material que a IA consulta antes de responder: horários, endereço, preços, políticas e perguntas frequentes da sua empresa, escritos uma vez e usados em todas as conversas.

Nas palavras da tela: *"Cadastre aqui o que a IA precisa saber: horários, políticas, preços, perguntas frequentes. Depois vincule a base a um prompt."* Com a base ligada ao prompt, a IA responde com o que está nela: se a base diz que a loja fecha aos sábados, é isso que a IA responde a quem pergunta se vocês abrem no sábado.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Prompts OPEN.AI** e clique em **BASE DE CONHECIMENTO**.
>
> ➡️ Clique em **NOVA BASE**, preencha o **Nome da base** e clique em **SALVAR**.
>
> ➡️ Abra a base e acrescente as informações em **NOVO ITEM** ou **ENVIAR ARQUIVO**.
>
> ➡️ No prompt, escolha a base no campo **Base de conhecimento** e clique em **Salvar**.

## Como criar a Base de Conhecimento

Acesse o menu **Prompts OPEN.AI  ›  BASE DE CONHECIMENTO  ›  NOVA BASE**

🔘 **Nome da base:** como a base aparece na lista e no campo do prompt. Sem nome, a tela avisa *"Dê um nome à base"*.

🔘 **Descrição (opcional):** para lembrar o que a base reúne.

Ao salvar, a tela confirma *"Base salva!"*. A lista mostra cada base com o nome, a descrição, quantos itens ela tem e o tamanho aproximado do material, em tokens. Sem nenhuma base, a lista avisa *"Nenhuma base cadastrada ainda. Crie a primeira para começar."*

## Como acrescentar informações à base

Cada informação da Base de Conhecimento é um **item**. Com a base aberta e ainda vazia, a tela avisa *"Nenhuma informação nesta base. Digite um item ou envie um arquivo."*

🔘 **NOVO ITEM:** abre os campos **Título** e **Conteúdo**. Nas palavras da tela: *"O título pesa mais na busca que o conteúdo — use as palavras que o cliente usaria."* Sem título ou sem conteúdo, a tela avisa *"Preencha o título e o conteúdo"*.

🔘 **ENVIAR ARQUIVO:** lê um arquivo **.pdf**, **.docx**, **.txt**, **.md** ou **.csv**, um por vez, e abre um item novo com o texto do arquivo no **Conteúdo**, para você dar o **Título**, conferir e salvar. Imagem não é lida: a tela responde, por exemplo, *"Não sei ler .png. Envie PDF, DOCX ou texto (.txt, .md, .csv)."*

⚠️ Confira o texto extraído do arquivo antes de salvar. Nas palavras da tela: *"PDF com colunas ou digitalizado costuma sair embaralhado, e o que estiver aqui é o que a IA vai afirmar ao cliente."*

🔘 **Editar** e **Excluir:** os ícones de cada item, para corrigir ou tirar uma informação da base.

## Como ligar a base ao prompt

Acesse o menu **Prompts OPEN.AI  ›  editar o prompt**

🔘 **Base de conhecimento:** a base que o prompt consulta, ou **Nenhuma**. Nas palavras da tela: *"O material que a IA consulta antes de responder."* Clique em **Salvar** no prompt.

Cada prompt consulta uma base, e a mesma base pode ser escolhida em vários prompts. A base vale em toda conversa que o prompt atende: quando o FlowBuilder Nativo leva a conversa ao Setor do prompt pelo bloco **GPT Assistant (OpenAI)**, ou direto no Setor que tem o prompt.

## Como excluir uma base

O ícone **Excluir** da base pede confirmação. Quando a base está em uso, o aviso diz quais prompts a usam: *"Esta base é usada por 1 prompt(s): [nome do prompt]. Eles continuam funcionando, mas deixam de consultar este material. A base e todos os itens dela serão removidos."*

Ao confirmar, a tela avisa *"Base removida"*, e o prompt que usava a base fica sem base: a IA continua respondendo, sem aquele material.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Onde fica a Base de Conhecimento da IA?** No menu **Prompts OPEN.AI**, no botão **BASE DE CONHECIMENTO**. O menu **Prompts OPEN.AI** aparece para o administrador.
>
> **A IA respondeu sem usar a Base de Conhecimento. O que confiro?** Confira se a base está escolhida no campo **Base de conhecimento** do prompt e se o prompt foi salvo. Confira também o **Título** dos itens: ele pesa mais na busca, então use as palavras que o cliente usaria.
>
> **Que arquivos a Base de Conhecimento aceita?** **ENVIAR ARQUIVO** aceita .pdf, .docx, .txt, .md e .csv, e o texto do arquivo vira um item. Imagem não é lida. Confira o texto antes de salvar: PDF com colunas ou digitalizado costuma sair embaralhado.
>
> **Se eu excluir a Base de Conhecimento, o prompt para de responder?** Não. Nas palavras da tela, os prompts que usavam a base *continuam funcionando, mas deixam de consultar este material*.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Criar a base e não ligar ao prompt:** a IA continua respondendo sem o material. **Solução:** escolha a base no campo **Base de conhecimento** do prompt e salve.
