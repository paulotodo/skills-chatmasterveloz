# Variável

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-variavel
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Variável

---

🧩 O bloco **Variável** é a memória do fluxo. Ele grava uma informação importante para a automação usar mais tarde, criando conversas personalizadas e inteligentes.

**🏷️ Categoria: Dados, Mensagem**

☑️ **Personalização:** chamar o cliente pelo nome (`%nome%`) ou confirmar um dado (`%cpf%`).

☑️ **Integração:** guardar o resultado de uma consulta a outro sistema, como o status de um pedido.

☑️ **Contexto:** lembrar exatamente o que o cliente escreveu para iniciar a conversa.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Variável**.
>
> ➡️ Escreva o nome da variável entre `%` e clique em **Adicionar**.

## Vídeo Tutorial

[Vídeo Voomly — id XeJRGchlGFOF2eAN1BRnj4YI0l1DNwDJHGYqpTJ-BMw6FieUU, tipo v]  

## Como configurar o bloco Variável

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Variável**

![FlowBuilder Formulário Bloco Variável](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6adb96e573871.png)

🔘 **Variável %nome_da_variavel%:** o nome da variável, escrito entre `%`, como `%nome%`.

🔲 Para finalizar, clique em **Adicionar**.

## Como guardar um valor numa variável

No bloco **Variável**, use o formato `%nome_variavel%` para dar nome à variável. Para guardar o nome de um lead, por exemplo, escreva `%nome%`.

O valor guardado depende do bloco que vem logo antes:  
- **Depois de uma Pergunta:** a variável guarda a resposta que o cliente escreveu.
- **Depois de um Menu:** a variável guarda a opção que o cliente escolheu.
- **Depois de uma Avaliação do Atendimento:** a variável guarda a nota que o cliente escolheu.
- **Depois de uma Execução de Código JS:** a variável guarda o que o código devolveu no `return`, com a **Variável** logo depois da **Execução de Código JS**.
- **Depois do Início:** a variável guarda a última mensagem que o cliente enviou antes de o fluxo começar.

A resposta de um **HTTP Request** é guardada pelo próprio bloco **HTTP Request**, na aba **Resposta**. O **Formato da Resposta** tem dois caminhos:  
- **Variável Única (resposta inteira):** a resposta completa, como texto, vai para a variável escrita em **Nome da Variável**. Com o nome `http_retorno`, por exemplo, ela entra nos blocos seguintes como `%http_retorno%`.
- **Objeto (mapear para N variáveis):** cada linha de **Mapeamentos** liga um **JSON Path** a um **Nome da Variável**. Com o JSON Path `nome` e o nome `nome_cliente`, o valor entra nos blocos seguintes como `%nome_cliente%`. Para um campo dentro de outro, use ponto no JSON Path, como `data.user.name`.

Para usar um campo só de uma resposta em JSON, escreva o nome do campo depois de um ponto: com a resposta em `%http_retorno%`, o campo `nome` entra como `%http_retorno.nome%`. O formato **Objeto** serve para dar a cada campo uma variável com nome próprio.

Não é preciso um bloco **Variável** depois do **HTTP Request**. Nas palavras da aba **Resposta**, a **Variável** *"guarda a última mensagem do contato, não esta resposta"*.

## Como usar o valor em outros blocos

Num bloco **Conteúdo**, **Msg Interna** ou **Execução de Código JS** (dentro do próprio código), escreva o mesmo `%nome_variavel%` que você usou para guardar. No exemplo acima, `%nome%`.

Quando a variável guarda um JSON, cada campo se lê com um ponto depois do nome: `%dados.nome%`, e um campo dentro de outro, `%dados.cidade.nome%`. Escrita inteira numa mensagem, como `%dados%`, a variável aparece sem as chaves do JSON.

No bloco **HTTP Request**, a variável também entra na **URL** e no **Corpo da Requisição**, no mesmo formato entre `%`, como no exemplo da própria janela do bloco: `https://api.com/users/%number%`.

Um bloco **Condição** logo depois da **Variável**, no tipo **Resposta da Pergunta**, compara o valor que essa **Variável** guardou, venha ele de onde vier: de uma **Pergunta**, ou de uma **Execução de Código JS** num fluxo sem nenhuma pergunta. É assim que o fluxo escolhe o caminho pelo valor.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso usar espaços no nome da variável?** Não é recomendado. Use `_` para separar palavras, como `%data_nascimento%` em vez de `%data nascimento%`. Espaços podem quebrar o código.
>
> **A variável do fluxo expira ou é apagada?** A variável fica gravada no atendimento, na conversa daquele cliente com aquela conexão. Ela não expira e não pode ser apagada, mas pode ser sobrescrita ao passar de novo pelo fluxo.
>
> **Posso sobrescrever uma variável?** Pode. Se você usa `%opcao%` no começo do fluxo e de novo mais adiante, o valor antigo é trocado pelo novo.
>
> **A variável continua valendo depois de um bloco Pular para?** Sim. O **Pular para** leva o atendimento ao bloco escolhido com o mesmo contato, as mesmas tags e as mesmas variáveis.
>
> **A variável continua valendo depois de um bloco Trocar Fluxo?** Sim. A variável fica gravada no atendimento, e o fluxo novo usa o mesmo `%nome%` sem precisar guardar o valor de novo.
>
> **Posso escrever `{{nome}}` no lugar de `%nome%` para usar uma variável do fluxo?** Não. A variável do fluxo só é trocada pelo valor quando está escrita entre porcentagens, como `%nome%`. Com chaves, como `{{nome}}`, o lugar da variável fica em branco na mensagem.
>
> **Meu retorno é um JSON, com nome e sobrenome. Como uso só o nome?** Escreva o campo depois de um ponto, direto na mensagem. Com o JSON guardado em `%dados%`, o nome entra como `%dados.nome%`; na resposta de um **HTTP Request** guardada em `%http_retorno%`, como `%http_retorno.nome%`. O formato **Objeto (mapear para N variáveis)** do **HTTP Request** também funciona, se você preferir dar ao campo uma variável própria, como `%nome_cliente%`.
>
> **Como guardo um JSON inteiro numa variável pela Execução de Código JS?** Devolva o JSON como texto, com `return JSON.stringify(dados);`, e ponha uma **Variável** logo depois. Um objeto devolvido sem o `JSON.stringify` aparece como *[object Object]* no texto. A resposta de um **HTTP Request** em **Variável Única** já fica guardada como texto e pode ser lida da mesma forma, com `JSON.parse('%http_retorno%')`.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Sintaxe errada:** definir ou usar a variável com `{{nome}}` ou só `nome`. Com chaves, o lugar da variável fica em branco na mensagem. **Solução:** escreva sempre entre porcentagens, `%nome%`, no bloco **Variável** e nos blocos que usam o valor.
>
> **Variável vazia:** usar a variável antes de guardá-la, como em *Olá %nome%* na primeira mensagem. O cliente recebe o texto `%nome%` escrito. **Solução:** guarde a variável antes de usá-la.
>
> **[object Object] no texto:** a mensagem mostra *[object Object]* no lugar do valor guardado. A **Execução de Código JS** devolveu um objeto no `return`, e a **Variável** guardou o objeto inteiro. **Solução:** devolva só o valor que vai usar, como `return dados.nome`, ou o JSON como texto, com `return JSON.stringify(dados);`.
>
> **Bloco no meio:** pôr um texto ou um menu entre a **Pergunta** e a **Variável**, ou entre a **Execução de Código JS** e a **Variável**. O fluxo perde a referência da resposta. **Solução:** a **Variável** precisa vir logo depois da fonte do dado; a única peça que pode ficar entre eles é um **Intervalo**.
