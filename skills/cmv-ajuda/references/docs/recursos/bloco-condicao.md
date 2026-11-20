# Condição

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-condicao
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Condição

---

🧩 **O Bloco de Condição** é o "cérebro" lógico da sua automação, capaz de **mudar o caminho** de um fluxo com base em uma condição definida.

**🏷️ Categoria: Roteador**

☑️ **Validar Respostas:** Verificar se o cliente digitou a palavra-chave correta.

☑️ **Segmentação:** Verificar se o cliente é VIP (via Tag) ou por qual número de WhatsApp ele entrou (Conexão).

☑️ **Filtro de Horário:** Direcionar para atendimento apenas em horário comercial.

![FlowBuilder Bloco de Condição](https://clihelper.chatmasterveloz.com/docs-imagem/14336-bloco-condicao.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo**.
>
> ➡️ Em um fluxo, selecione o Bloco **Condição**.
>
> ➡️ Preencha os **campos** e clique no botão **Adicionar**.

## Como adicionar o bloco "Condição" no FlowBuilder

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Condição**

![FlowBuilder Formulário Bloco Condição](https://clihelper.chatmasterveloz.com/docs-imagem/14336-bloco-condicao-formulario.jpg)É preciso configurar a lógica de validação. Na maioria dos tipos, a estrutura é composta por três pilares:

**🔘 Tipo:** O que vamos analisar? (Resposta da Pergunta, Horário, Tag...)

**🔘 Condição:** Qual a regra? (Igual, Contém, Antes das...)

**🔘 Valor:** Qual o alvo da comparação?

🔲 Para finalizar, clique em **Adicionar**.

Com base nessa verificação, o fluxo segue por um caminho se a condição for **verdadeira** ou por outro caminho se for **falsa**.

Abaixo, detalhamos cada **tipo de condicional**:

### ⚡ **RESPOSTA DA PERGUNTA**

![FlowBuilder Formulário Bloco Condição de Texto](https://clihelper.chatmasterveloz.com/docs-imagem/14336-condicao-1-texto-768x341.jpg)✅ Verifica o **conteúdo** de uma variável, uma resposta anterior ou mensagem do cliente.

🔘 **Condição:** escolha entre "**Igual**", "**Diferente**", "**Contém**" ou "**Expressão Regular**" (para regras avançadas).

🔘 **Valor:** digite o texto ou palavra-chave que espera receber.

🔘 **Igual:** a resposta precisa ser o **Valor** inteiro. Maiúscula e minúscula não fazem diferença e os espaços antes e depois da resposta são ignorados, mas o acento conta: *nao* não é igual a *Não*.

🔘 **Diferente:** o contrário do **Igual** — segue pelo **Verdadeiro** quando a resposta não é o **Valor**. Também não diferencia maiúscula de minúscula: *sim* não é diferente de *Sim*.

🔘 **Contém:** segue pelo **Verdadeiro** quando a resposta contém o **Valor**: *Realizei operações agora* contém *Realizei*. Aceita várias opções separadas por vírgula, e basta a resposta conter uma delas; o espaço depois da vírgula não atrapalha, e o ponto e vírgula não separa. Maiúscula e minúscula não fazem diferença, mas o acento conta.

🔘 **Expressão Regular:** compara a resposta com um padrão e diferencia maiúscula de minúscula. Com `^` no começo e `$` no fim, a resposta inteira precisa seguir o padrão; sem eles, basta a resposta conter o padrão.

◽ Logo depois de um bloco **Variável**, a **Resposta da Pergunta** compara o valor que essa **Variável** guardou, venha ele de onde vier: de uma **Pergunta** ou do `return` de uma **Execução de Código JS**, mesmo num fluxo sem nenhuma pergunta.

◽ Sem **Variável** no meio, a **Resposta da Pergunta** logo depois de uma **Pergunta** compara a resposta escrita, e logo depois de um **Menu** compara a opção que o cliente escolheu.

🔘 **Arquivo de Mídia:** escolha esta condição para verificar o **tipo de arquivo** que o cliente mandou, em vez do texto. Marque os tipos aceitos: **Imagem**, **Documento**, **Vídeo**, **GIF**, **Áudio**, **Sticker**, **Contato** e **Outros / Não reconhecidos** — cada opção mostra as extensões que ela cobre.

◽ Um arquivo de um tipo que não foi marcado segue pelo **Falso**.

◽ A mensagem de voz gravada no WhatsApp conta como **Áudio**.

### ⚡ **TAG**

![FlowBuilder Formulário Bloco Condição de Tag](https://clihelper.chatmasterveloz.com/docs-imagem/14336-condicao-2-tag-768x343.jpg)✅ Verifica se o cliente possui (ou não) **etiquetas** específicas.

*Atenção às regras de preenchimento deste campo:*

**🔘 Condição IGUAL:** o valor deve ser o nome completo de **uma única** tag. (Verifica se ele *tem* essa tag).

**🔘 Condição DIFERENTE:** o valor deve ser o nome completo de **uma única** tag. (Verifica se ele *não tem* essa tag).

**🔘 Condição CONTÉM:** o valor pode ser um grupo de tags separadas por **vírgula** (ex: Tag1,Tag2 — o espaço depois da vírgula não atrapalha). O sistema dará "Verdadeiro" se o cliente tiver **pelo menos uma** delas.

◽ Maiúscula e minúscula não fazem diferença no nome da tag: *Teste* encontra a tag *teste*.

### ⚡ **HORÁRIO**

![FlowBuilder Formulário Bloco Condição de Horário](https://clihelper.chatmasterveloz.com/docs-imagem/14336-condicao-3-horario-768x340.jpg)✅ Verifica a **hora** exata em que o cliente passou pelo bloco.

🔘 **Condição:** utilize "**Antes das**" ou "**Depois das**".

🔘 **Valor:** digite o horário no formato 24h (ex: 08:30 ou 18:45).

◽ O bloco compara com o horário de Brasília.

### ⚡ **É DIA ÚTIL?**

![FlowBuilder Formulário Bloco Condição de Dia Útil](https://clihelper.chatmasterveloz.com/docs-imagem/14336-condicao-4-dia-util-768x343.jpg)✅ Verifica se **hoje é dia útil**: de segunda a sexta, fora dos feriados do lugar escolhido no próprio bloco.

🔘 **Condição:** não precisa escolher; o bloco funciona sem ela.

🔘 **Feriados de qual lugar?** Os feriados nacionais valem sempre. Escolha o estado e, se quiser, a cidade, para somar os estaduais e os municipais.

🔘 **Contar ponto facultativo:** marque para tratar Carnaval, Quarta-feira de Cinzas, Corpus Christi, 24/12 e 31/12 como feriado.

◽ O bloco mostra a lista dos **próximos feriados que vai considerar**, para você conferir antes de salvar.

### ⚡ **É FERIADO?**

✅ Verifica se **hoje é feriado** no lugar escolhido no próprio bloco.

🔘 **Feriados de qual lugar?** Escolha **Só feriados nacionais** ou um estado. Os nacionais valem sempre; com o estado, entram também os estaduais.

🔘 **Cidade (opcional):** aparece depois de escolher o estado e soma os feriados municipais. Cidade sem feriado municipal na lista fica com os nacionais e os do estado.

🔘 **Contar ponto facultativo:** marque para que Carnaval, Quarta-feira de Cinzas, Corpus Christi, 24/12 e 31/12 contem como feriado.

◽ A lista **Próximos feriados que o bloco vai considerar** mostra cada data com o tipo — nacional, estadual, municipal ou ponto facultativo.

◽ Este tipo não usa os campos **Condição** e **Valor**.

### ⚡ **QUAL DIA DA SEMANA?**

![FlowBuilder Formulário Bloco Condição de Dia da Semana](https://clihelper.chatmasterveloz.com/docs-imagem/14336-condicao-5-dia-semana-768x340.jpg)✅ Verifica o **dia da semana** em que o cliente passou pelo bloco.

🔘 **Em quais dias o bloco segue pelo "Verdadeiro"?** Marque os dias, de **Segunda-feira** a **Domingo**. Nos dias desmarcados, o bloco segue pelo **Falso**.

🔘 **Atalhos:** trocam a seleção inteira de uma vez. **Segunda a sexta** deixa marcados só os dias de segunda a sexta, **Fim de semana** só sábado e domingo, e **Limpar** desmarca todos.

◽ Sem nenhum dia marcado, o bloco não salva.

◽ Este tipo não usa os campos **Condição** e **Valor**.

### ⚡ **ID DA CONEXÃO**

![FlowBuilder Formulário Bloco Condição de ID da Conexão](https://clihelper.chatmasterveloz.com/docs-imagem/14336-condicao-6-id-conexao-768x340.jpg)✅ Verifica por qual Conexão o cliente entrou em contato. Útil para quem usa mais de uma conexão na plataforma.

*Atenção às regras de preenchimento deste campo:*

O ID da Conexão você encontra no menu **Conexões**.

**🔘 Condição IGUAL:** o valor deve ser o **ID único** de uma conexão. (Verifica se o atendimento veio exatamente desta Conexão).

**🔘 Condição DIFERENTE:** o valor deve ser o **ID único** de uma conexão. (Verifica se o atendimento veio de qualquer outra Conexão, exceto esta).

**🔘 Condição CONTÉM:** o valor pode ser um grupo de IDs separados por **vírgulas sem espaços** (ex: 15,22,40). O sistema dará "Verdadeiro" se o atendimento vier de **qualquer uma** dessas conexões listadas.

### ⚡ **STATUS DO ATENDIMENTO**

✅ Verifica em que **status** está o atendimento quando o cliente passa pelo bloco.

🔘 **Status do Atendimento:** escolha **Aberto**, **Fechado** ou **Aguardando**.

◽ **Aberto** é o atendimento com um atendente (aba **Atendendo**), **Aguardando** é o que ainda não tem atendente e **Fechado** é o encerrado.

🔘 **Condição:** **Igual** segue pelo **Verdadeiro** quando o atendimento está nesse status; **Diferente**, quando está em qualquer outro.

◽ Enquanto o fluxo atende o cliente, o atendimento fica em **Aguardando**: um **Igual** a **Aguardando** segue pelo **Verdadeiro**, e um **Igual** a **Aberto**, pelo **Falso**.

### ⚡ **PROTOCOLO FECHADO**

✅ Verifica **há quanto tempo** o último atendimento encerrado deste contato foi encerrado, sem contar o atendimento atual.

🔘 **Encerrado:** escolha **há menos de** ou **há mais de**.

🔘 **Tempo** e **Unidade:** o número e a unidade — **minutos**, **horas** ou **dias**.

◽ O bloco segue pelo **Verdadeiro** quando o último encerramento cabe no tempo escolhido. Contato sem atendimento anterior segue pelo **Falso**.

### ⚡ **ANÚNCIO**

✅ Confere o **anúncio** que o cliente clicou para abrir a conversa, em qualquer conexão de WhatsApp.

🔘 **O que conferir:** **Veio de um anúncio (qualquer)**, para separar quem chegou por anúncio, ou um dado do anúncio — **ID**, **Título**, **Texto**, **Link** ou **Tipo de mídia do anúncio**.

◽ Sem anúncio, o bloco segue pelo **Falso**.

### ⚡ **POSTAGEM**

✅ Para comentários do **Instagram**: verifica se o comentário veio de uma **publicação específica**.

🔘 Escolha as publicações. O bloco segue pelo **Verdadeiro** quando o comentário veio de uma delas.

◽ Vale só para comentários: mensagem normal do Direct não veio de publicação nenhuma e segue pelo **Falso**.

### ⚡ **TIPO DE POSTAGEM**

✅ Para comentários do **Instagram**: verifica o **formato** da publicação comentada, sem precisar escolher as publicações uma a uma.

🔘 Marque os formatos: **Publicação do feed**, **Reels**, **Story** ou **Anúncio**.

◽ Vale só para comentários: mensagem normal do Direct segue pelo **Falso**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso ligar vários blocos de condição em sequência?** Sim! Isso chama-se "Condicional Aninhada". Você verifica se é 1, se não for, verifica se é 2, se não for, verifica se é 3.
>
> **O que acontece se eu não conectar a saída "se Falso"?** O fluxo para e o cliente fica sem resposta. **Sempre** conecte as duas pontas (verdadeiro e falso), mesmo que a saída falsa seja apenas uma mensagem dizendo "Não entendi, tente novamente".
>
> **Qual a diferença entre É Dia Útil? e É Feriado?** O **É Dia Útil?** separa segunda a sexta dos fins de semana e dos feriados do lugar. O **É Feriado?** olha só os feriados: um sábado comum não é feriado.
>
> **Dá para montar o dia útil com outros blocos?** Sim, com dois blocos **Condição** em sequência: um **Qual Dia da Semana?** com os dias de expediente marcados e, na saída **Verdadeiro** dele, um **É Feriado?** com o seu lugar. A saída **Falso** do **É Feriado?** é o dia útil. É o caminho quando o expediente inclui o sábado, que o **É Dia Útil?** não conta como dia útil.
>
> **Preciso digitar o nome do dia da semana?** Não. No tipo **Qual Dia da Semana?** os dias são marcados nas caixas do próprio bloco; não há campo para digitar.
>
> **Como dar um tratamento diferente para quem voltou logo depois de um atendimento encerrado?** Use o tipo **Protocolo fechado** com **há menos de** e o tempo que faz sentido para você — por exemplo, 24 horas. Quem voltou dentro desse tempo segue pelo **Verdadeiro**.
>
> **Como funciona a "Expressão Regular"?** É um recurso para programadores. Permite validar formatos complexos, como verificar se o cliente digitou um CPF ou um e-mail no formato certo — por exemplo, `^\d{5}-?\d{3}$` aceita um CEP como *80000-000*. Sem o `^` no começo e o `$` no fim, basta a resposta conter o padrão: `Realizei` aceita *Realizei operações agora*.
>
> **Como aceito mais de uma resposta certa no tipo Resposta da Pergunta?** Há dois caminhos. Com a condição **Contém**, escreva no **Valor** as opções separadas por vírgula, como `Sim,Não,Talvez`: o bloco segue pelo **Verdadeiro** quando a resposta contém uma delas, sem diferenciar maiúscula de minúscula, e aceita também uma resposta mais longa — *Realizei operações agora* passa pela opção *Realizei operações*. Só a vírgula separa as opções (ponto e vírgula não), e o espaço depois da vírgula não atrapalha. Para exigir a resposta exata, use a **Expressão Regular** com `^(opção 1|opção 2|opção 3)$`.
>
> **No tipo Resposta da Pergunta, quando o Contém aceita uma resposta que eu não queria?** Quando uma opção está dentro de outra. O **Contém** procura a opção dentro da resposta e não diferencia maiúscula de minúscula, então um **Contém** com `Realizei operações` também segue pelo **Verdadeiro** se o cliente responder *Não realizei operações*. Nesses casos, use a **Expressão Regular** com a resposta exata.
>
> **Como exijo a resposta exata com a Expressão Regular?** Escreva no **Valor** as respostas aceitas entre parênteses, separadas por `|`, com `^` no começo e `$` no fim: `^(opção 1|opção 2|opção 3)$`. O `|` quer dizer "ou", e o `^` e o `$` exigem que a resposta inteira seja uma das opções. Ao contrário do **Contém** e do **Igual**, a **Expressão Regular** diferencia maiúscula de minúscula: uma expressão com `sim` não aceita a resposta `Sim`. Os caracteres `.` `?` `(` `)` têm função própria na expressão e precisam de `\` antes quando fazem parte da resposta: `^Tudo certo\?$` aceita *Tudo certo?*, e sem a barra a mesma resposta segue pelo **Falso**.
>
> **A Resposta da Pergunta diferencia acento e maiúscula?** Depende da condição. No **Igual**, no **Diferente** e no **Contém**, maiúscula e minúscula não fazem diferença (*sim* = *Sim*), mas o acento faz: *nao* não é igual a *Não*, e *operacoes* não contém *operações*. Se o cliente pode escrever sem acento, liste as duas grafias no **Contém**, separadas por vírgula (`Não,Nao`). A **Expressão Regular** diferencia maiúscula de minúscula.
>
> **A condição de Tag "Contém" exige todas as tags?** Não. Se você colocar Vendas,Suporte,Financeiro (separadas por vírgula) e o cliente tiver apenas a tag "Vendas", o resultado será **Verdadeiro**. Ele precisa ter apenas uma das listadas. O mesmo vale para a condição de Conexão.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Expressão Regular escrita errada:** com um `(` sem o `)` que o fecha, por exemplo, a janela avisa *"Expressão regular inválida: confira os parênteses e os colchetes."*, e um bloco que já esteja com a expressão errada segue sempre pelo **Falso**, qualquer que seja a resposta. **Solução:** corrija a expressão: todo parêntese aberto precisa ser fechado, e os caracteres `.` `?` `(` `)` que fazem parte da resposta precisam de `\` antes.
>
> **Lista separada por vírgula no Igual:** o cliente responde uma das opções e o bloco segue pelo **Falso**. O **Igual** compara a resposta com o **Valor** inteiro, e nem a vírgula nem o ponto e vírgula separam opções. **Solução:** use o **Contém** com as opções separadas por vírgula ou a **Expressão Regular** `^(opção 1|opção 2)$`.
