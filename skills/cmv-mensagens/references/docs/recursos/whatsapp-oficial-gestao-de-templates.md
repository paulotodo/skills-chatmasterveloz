# Gestão de Templates

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/whatsapp-oficial-gestao-de-templates
- **Categoria:** Recursos
- **Menu:** Conexões › WhatsApp › Gestão de Templates

---

🧩 Template é a mensagem aprovada pela Meta que a conexão oficial usa para começar uma conversa. A tela **Gestão de Templates** é o painel onde você acompanha a saúde deles: quais foram aprovados, quais foram recusados, e quem enxerga o quê na hora de enviar.

Ela se alcança **só pelo card da conexão oficial**, e não pelo menu lateral. Quem procura por ela na barra da esquerda não acha.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões** e, no card da conexão oficial, clique em **Gestão de Templates**.
>
> ➡️ A tela abre já filtrada por essa conexão.
>
> ➡️ Em **GRUPOS**, crie um grupo e marque os templates dele. Depois, no Setor, escolha o grupo.

## O topo da tela

🔲 **NOVO TEMPLATE:** inicia o cadastro de um modelo novo.

🔲 **SINCRONIZAR:** conversa com a Meta e traz os modelos que ainda não apareceram aqui, atualizando o estado dos que já existem.

🔲 **GRUPOS:** abre o painel que junta modelos e liga os grupos aos Setores.

Logo abaixo ficam os filtros:

🔘 **Status:** mostra só os modelos naquele estado — pendente, submetido, aprovado ou rejeitado.

🔘 **Categoria:** marketing, utilidade ou autenticação.

🔘 **Conexão WABA:** troca entre as suas conexões oficiais, quando há mais de uma.

🔲 **ATUALIZAR:** recarrega a lista com os filtros escolhidos.

## A lista

Cada modelo é um card, e ele mostra:

◽ **O nome** do modelo, do jeito que foi cadastrado.

◽ **A categoria e o idioma**, lado a lado.

◽ **A situação** na Meta, em destaque no canto.

◽ **CONEXÃO:** por qual conexão oficial ele responde.

◽ **CRIADO POR:** de onde ele veio. Modelo feito no Gerenciador da Meta aparece como **BM**; modelo criado por integração aparece como **API**.

◽ **GRUPOS:** a que grupo ele pertence, ou **Sem grupo**.

◽ **MENSAGEM:** uma prévia do texto. Onde você vê `{{1}}` e `{{2}}` são os espaços preenchidos na hora do envio com os dados do cliente.

E quatro botões de ícone:

🔲 **Visualizar:** abre o modelo inteiro — categoria, idioma, data de criação, texto, variáveis.

🔲 **Ver JSON:** mostra o modelo no formato que a integração usa.

🔲 **Editar:** altera o modelo.

🔲 **Excluir:** apaga o modelo daqui **e da Meta**.

⚠️ Editar um modelo aprovado **manda ele de volta para análise**. Programe a alteração para um momento em que ela não faça falta, e evite mexer no modelo que a operação usa todo dia.

⚠️ A exclusão alcança os dois lados. Não é só tirar da nossa lista.

## Grupos de templates

O painel **GRUPOS** existe para cada equipe ver só o que interessa a ela. Nas palavras da tela: *agrupe templates e vincule os grupos aos setores, e ao abrir um atendimento por um setor só aparecem os templates dos grupos dele.*

Dentro do painel você dá um nome, clica em **ADICIONAR**, e o grupo nasce com zero modelos. Depois marca quais entram. Um modelo pode estar em mais de um grupo, e clicar de novo tira.

Do outro lado, no cadastro do Setor, o campo **Grupos de templates** escolhe o que aquela equipe enxerga. Deixando vazio, o Setor mostra **todos** os modelos da conexão.

## Erros de Template

O botão vizinho no card abre uma tela própria, com os modelos que a Meta recusou nesta conexão. Cada linha traz o nome do modelo, de onde veio o envio, o código do erro e a mensagem da Meta — coisas como parâmetro de texto sem valor, ou cabeçalho maior do que o permitido.

É onde se descobre por que um modelo aprovado falhou no envio: quase sempre a diferença entre o que foi mandado e o que está aprovado.

## O modelo que pede permissão para ligar

Existe um tipo de modelo que leva o botão **Escolher preferências**, do próprio WhatsApp: o cliente escolhe se aceita receber ligações, e a resposta atualiza a ficha dele na hora. Esse modelo pode ser criado na categoria **Utilidade**, e o botão aparece na prévia, inclusive nos modelos feitos direto no Gerenciador da Meta. Editar o modelo não faz o botão sumir.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A equipe não vê os templates na conversa.** O Setor não tem grupo, ou tem um grupo vazio. Edite o Setor e preencha **Grupos de templates**, ou deixe o campo vazio para mostrar todos.
>
> **O template foi aprovado e o envio falha.** Abra **Erros de Template** no card: a diferença entre o que foi enviado e o que está aprovado está lá, com o código do erro.
>
> **Posso usar o mesmo template em duas conexões?** Cada conexão tem os seus. O mesmo texto precisa ser aprovado em cada número.
>
> **Criei um modelo na Meta e ele não aparece aqui.** Clique em **SINCRONIZAR**. A tela busca na Meta o que ainda não tinha chegado.
>
> **Qual a diferença entre BM e API no Criado por?** BM é o modelo que alguém criou no Gerenciador da Meta. API é o que entrou por integração.
>
> **Excluí um modelo aqui. Ele sumiu da Meta também?** Sim. A exclusão vale nos dois lados.
