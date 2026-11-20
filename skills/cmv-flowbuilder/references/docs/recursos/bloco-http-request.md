# HTTP Request

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-http-request
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › HTTP Request

---

🧩 O bloco **HTTP Request** faz o fluxo conversar com outro sistema sem escrever código: ele chama o endereço de uma API, envia os dados do atendimento e guarda a resposta em variáveis para os próximos blocos usarem. É o caminho para consultar um pedido no seu sistema, cadastrar um lead no CRM externo ou avisar uma automação.

Tudo é configurado em três abas: **Requisição**, **Autenticação** e **Resposta**.

**🏷️ Categoria: Dados - Integração**

Ideal para:

☑️ **Consulta de pedido:** busca o status no sistema da loja e responde ao cliente com ele.

☑️ **Cadastro externo:** envia nome e telefone do cliente para um CRM ou planilha.

☑️ **Aviso para automação:** dispara um fluxo do n8n, Make ou outra ferramenta.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **HTTP Request**.
>
> ➡️ Preencha **Requisição**, **Autenticação** e **Resposta**, use **Testar Requisição** e clique em **Adicionar**.

## A aba Requisição

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  HTTP Request**

🔘 **Método:** **GET**, **POST**, **PUT**, **PATCH** ou **DELETE**, conforme a API pede.

🔘 **URL:** o endereço chamado. Ex.: *[https://api.exemplo.com/endpoint](https://api.exemplo.com/endpoint)*.

🔘 **Headers:** pares de nome e valor enviados junto, como *Content-Type* e *application/json*.

🔘 **Corpo da Requisição:** aparece nos métodos que enviam dados. O **Tipo do Corpo** pode ser **JSON**, **Form URL-Encoded**, **Form-Data (multipart)**, **Texto Raw** ou **Sem corpo**.

📌 Use `{{variavel}}` ou `%variavel%` para mandar dados do atendimento, na URL ou no corpo. Ex.: *[https://api.com/users/](https://api.com/users/)%number%* ou `{"name": "{{name}}"}`.

## A aba Autenticação

🔘 **Tipo de Autenticação:** **Sem Autenticação**, **Bearer Token**, **Basic Auth (Usuário/Senha)** ou **API Key**. Escolha o que a API exige; sem autenticação, a requisição vai sem credenciais.

## A aba Resposta

🔘 **Formato da Resposta:** como o retorno da API é guardado.

◽ **Variável Única (resposta inteira):** a resposta completa vai para uma variável só, informada em **Nome da Variável**, e fica guardada como texto. O nome sugerido é *httpResponse*, e nos blocos seguintes o valor é usado com `%httpResponse%`. Numa mensagem, uma resposta em JSON aparece sem os sinais `{` e `}`.

◽ **Objeto (mapear para N variáveis):** cada campo da resposta vai para uma variável própria. Em **Mapeamentos**, cada linha liga um **JSON Path** a um **Nome da Variável**: com o JSON Path `nome` e o nome `nome_cliente`, o valor entra nos blocos seguintes como `%nome_cliente%`. Use ponto no **JSON Path** para campos dentro de campos, como *data.user.name*.

Na **Variável Única**, um campo da resposta também se lê direto na mensagem, com o nome dele depois de um ponto: com a resposta em `%httpResponse%`, o campo `nome` entra como `%httpResponse.nome%`.

⚠️ No texto de uma mensagem, só a forma entre `%` mostra o valor: com chaves, como `{{httpResponse}}`, o lugar da variável fica em branco.

## Testar antes de adicionar

O painel **Testar Requisição**, no rodapé da janela, executa a chamada com o que foi preenchido. Use antes de clicar em **Adicionar**, para conferir se a API responde e o que ela devolve.

🔲 Para finalizar, clique em **Adicionar**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual a diferença entre o bloco HTTP Request e o bloco Execução de Código JS?** O **HTTP Request** monta a chamada pelos campos, sem código. O **Execução de Código JS** é para quem prefere escrever a chamada, ou outro tratamento, em JavaScript.
>
> **Como uso a resposta do HTTP Request num bloco de mensagem?** Pelo nome da variável escolhida na aba **Resposta**, escrito entre `%`. Com **Variável Única**, use `%httpResponse%` (ou o nome que você deu); com **Objeto**, use o nome de cada variável mapeada, como `%nome_cliente%`.
>
> **Preciso de um bloco Variável depois do HTTP Request para guardar a resposta?** Não. A resposta fica guardada pelo próprio **HTTP Request**, na variável da aba **Resposta**, e já pode ser usada nos blocos seguintes. Nas palavras da aba **Resposta**, o bloco **Variável** *"guarda a última mensagem do contato, não esta resposta"*.
>
> **A resposta do HTTP Request é um JSON. Como uso um campo só, como o nome?** Escreva o campo depois de um ponto, direto na mensagem: `%httpResponse.nome%`. O formato **Objeto** também serve, se você preferir dar ao campo uma variável própria, como `nome` → `nome_cliente`.
>
> **Posso mandar o telefone do cliente para a API no HTTP Request?** Pode. Use as variáveis do atendimento na URL ou no corpo, como `%number%`.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Esquecer o Content-Type:** a API recusa o corpo em JSON. **Solução:** em **Headers**, informe *Content-Type* com o valor *application/json*.
>
> **Mapear o caminho errado:** a variável fica vazia porque o **JSON Path** não existe na resposta. **Solução:** use **Testar Requisição**, veja a resposta real e copie o caminho dela.
>
> **Resposta em branco na mensagem:** a resposta foi usada com chaves, como `{{httpResponse}}`, e o lugar dela fica vazio. **Solução:** escreva o nome entre `%`, como `%httpResponse%`.
