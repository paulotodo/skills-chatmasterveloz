# Listas de Envio do Mail Marketing

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/listas-de-envio-do-mail-marketing
- **Categoria:** Recursos
- **Menu:** Mail Marketing › Listas de Envio do Mail Marketing

---

🧩 A lista é quem recebe a campanha. Cada lista do **Mail Marketing** guarda os endereços de e-mail, o nome de cada pessoa e, quando os contatos vêm de uma planilha, outras informações que o modelo do e-mail pode usar, como a cidade ou o plano.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Mail Marketing** e abra a aba **Listas**.
>
> ➡️ Clique em **Nova lista**, preencha o **Nome da lista** e clique em **Salvar**.
>
> ➡️ Na linha da lista, clique em **Contatos**.
>
> ➡️ Coloque os contatos por **Adicionar um**, **Colar ou abrir CSV** ou **Do atendimento**.

## Criar a lista

Acesse o menu **Mail Marketing  ›  Listas  ›  Nova lista**

🔘 **Nome da lista:** o nome que aparece na escolha das listas da campanha. Sem ele, o **Salvar** fica desativado.

🔘 **Descrição:** um texto para a equipe saber o que a lista reúne. Aparece embaixo do nome, na aba **Listas**.

Ao salvar, a tela confirma com *"Lista salva."* e a lista aparece na aba **Listas** com as colunas **Contatos** e **Descadastrados** e os botões **Contatos**, **Editar** e **Remover**.

## Colocar os contatos na lista

O botão **Contatos**, na linha da lista, abre a janela *Contatos da lista* com o nome dela no título. Os contatos entram por três abas:

🔘 **Adicionar um:** o **E-mail** e o **Nome** de uma pessoa, e o botão **Adicionar**.

🔘 **Colar ou abrir CSV:** um e-mail por linha, ou uma planilha com cabeçalho. Nas palavras da tela: *"Um e-mail por linha, ou uma planilha com cabeçalho (email; nome; e as outras colunas, que viram variáveis como {{cidade}}). Separe por ponto e vírgula, vírgula ou tabulação."* O botão **Abrir arquivo CSV** traz o arquivo para o campo de texto, sem colocar ninguém na lista ainda; quem coloca é o botão **Colocar na lista**.

🔘 **Do atendimento:** nas palavras da tela, *"Traz os contatos do atendimento que têm e-mail cadastrado. Quem já está na lista não duplica."* O campo **Só quem tem atendimento com estas tags (opcional)** limita aos contatos com atendimento nessas tags; em branco, vêm todos os contatos com e-mail. O botão é **Trazer os contatos**.

Depois de cada inclusão, a tela avisa quantos contatos entraram, quantos já estavam na lista e quantas linhas foram ignoradas, como *"2 adicionados, 0 já estavam na lista, 1 linhas sem e-mail válido."*, e volta para a aba **Contatos**. Um endereço inválido não dá erro: ele só não entra na lista e aparece na conta das linhas sem e-mail válido.

## As colunas da planilha viram variáveis

A planilha tem um cabeçalho com **email**, **nome** e as outras colunas que a empresa quiser. Cada coluna a mais vira uma informação do contato: uma planilha com `email;nome;cidade;plano` guarda a cidade e o plano de cada pessoa, que aparecem na coluna **Outras informações** da lista, como *plano: Ouro · cidade: Londrina*.

No modelo do e-mail, essas colunas entram como variáveis, com o nome da coluna entre chaves duplas: `{{cidade}}` vira a cidade de cada pessoa no e-mail enviado. Quem não tem a informação na lista recebe o e-mail com o espaço em branco.

## A aba Contatos da lista

🔘 A aba **Contatos** mostra o total entre parênteses e, para cada pessoa, o **E-mail**, o **Nome** e as **Outras informações**.

🔘 **Buscar:** filtra os contatos da lista pelo e-mail.

🔘 **Tirar da lista:** o contato deixa a lista na hora, sem pedir confirmação.

🔘 Quem se descadastrou continua na lista com o selo **descadastrado** e conta na coluna **Descadastrados** da aba **Listas**, mas não recebe as campanhas.

## Editar e remover a lista

🔘 **Editar:** muda o nome e a descrição da lista.

🔘 **Remover:** pede confirmação, e a tela avisa: *"A lista e os contatos dela somem. As campanhas que já começaram não mudam."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Como coloco no Mail Marketing os contatos de uma planilha?** Salve a planilha em CSV com o cabeçalho **email**, **nome** e as outras colunas. Na aba **Listas**, clique em **Contatos** na linha da lista, abra a aba **Colar ou abrir CSV**, clique em **Abrir arquivo CSV** e depois em **Colocar na lista**. Também dá para colar o conteúdo direto no campo de texto.
>
> **Coloquei um e-mail inválido na lista do Mail Marketing e não apareceu erro.** O endereço que não parece válido não entra na lista; ele aparece na conta de *"linhas sem e-mail válido"* do aviso que a tela mostra depois de cada inclusão.
>
> **A mesma pessoa pode estar em duas listas do Mail Marketing?** Pode. Numa campanha com as duas listas, ela recebe o e-mail uma vez só.
>
> **O que acontece com o contato descadastrado que está numa lista do Mail Marketing?** Ele continua na lista, com o selo **descadastrado**, e fica fora de todas as campanhas da empresa. Para ele voltar a receber, o endereço precisa deixar a aba **Descadastros**.
>
> **Tirar da lista descadastra o contato no Mail Marketing?** Não. **Tirar da lista** tira o contato só daquela lista, e ele continua recebendo as campanhas das outras listas em que estiver. Para a pessoa não receber mais nada, use a aba **Descadastros**.
