# Pular para

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-pular-para
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Pular para

---

🧩 O bloco **Pular para** leva a conversa até outro bloco do mesmo fluxo sem desenhar uma linha até ele. É o atalho para voltar ao menu principal, repetir uma etapa ou chegar a um ponto distante do desenho, sem linhas atravessando o fluxo inteiro.

O atendimento continua no bloco escolhido com o mesmo contato, as mesmas tags e as mesmas variáveis. O bloco de destino não é copiado: é o mesmo bloco, alcançado por outro caminho.

**🏷️ Categoria: Roteador**

Ideal para:

☑️ **Volta ao menu:** devolve o cliente ao menu principal ao fim de cada assunto, sem uma linha por opção.

☑️ **Repetição de etapa:** pede de novo uma informação que veio errada, voltando à pergunta.

☑️ **Fluxo grande organizado:** liga partes distantes do desenho sem linhas cruzando a tela.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Pular para**.
>
> ➡️ Escolha o bloco de destino, clicando nele no desenho ou na lista da janela, e clique em **Adicionar**.
>
> ➡️ Ligue a saída do bloco anterior ao **Pular para**.

## Como escolher o destino do Pular para

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Pular para**

A janela **Adicionar bloco: Pular para** pede o **Destino**, e há dois jeitos de escolher:

🔘 **Escolher clicando no bloco:** a janela some e o editor mostra *Clique no bloco de destino do "Pular para". Esc cancela.* Clique no bloco que deve receber a conversa, e a janela volta com o destino preenchido.

🔘 **Lista de blocos:** a janela lista os blocos do fluxo, cada um com o tipo, o começo do conteúdo e o ID entre parênteses, como *Pergunta: Qual o seu nome? (#rSseSA)*. Use o campo **Buscar bloco por tipo, conteúdo ou ID** para filtrar e clique no bloco.

🔲 Para finalizar, clique em **Adicionar**. Sem destino escolhido, o botão fica desativado.

🔘 **Localizar bloco:** fecha a janela e leva o desenho até o bloco de destino, que fica selecionado. Use ao editar um **Pular para** que já está no fluxo, para conferir aonde ele leva.

⚠️ Ao criar um **Pular para**, clique em **Adicionar** antes de usar o **Localizar bloco**. Como ele fecha a janela, o bloco novo não chega a entrar no desenho.

Se o bloco escolhido não puder ser destino, a tela avisa *Esse bloco não pode ser destino. Escolha outro.* O **Início** pode ser destino, para recomeçar o fluxo.

## Como o Pular para aparece no desenho

O bloco mostra a seta e o destino, como *→ Pergunta: Qual o seu nome? (#rSseSA)*. Ele só tem ponto de entrada: a conversa segue dele direto para o destino, sem linha.

O bloco de destino ganha o selo **Recebe saltos de N ponto(s)**. Clique no selo para ver a lista dos **Pular para** que levam até ele; escolha um e o desenho vai até ele.

## O que o editor faz pelos saltos

◽ Um **Pular para** sem destino válido impede de salvar o fluxo: *Não foi possível salvar: N "Pular para" sem destino válido. Corrija os blocos marcados antes de salvar.*

◽ Apagar um bloco que era destino também avisa: *O bloco apagado era destino de N "Pular para". Escolha outro destino para eles antes de salvar.*

◽ O **Verificar** conta o bloco de destino como alcançável e lista os **"Pular para" sem destino** e os **Ciclos sem espera**.

## Ciclos sem espera

Um caminho que volta a um bloco sem nenhum bloco no meio que espere a resposta do contato é um **ciclo sem espera**. O editor avisa: *N caminho(s) voltam a um bloco sem esperar resposta do contato. Na execução, o fluxo é interrompido ao voltar ao mesmo bloco.*

Para repetir uma etapa com o **Pular para**, garanta que o caminho de volta passe por um bloco que espera o cliente, como uma pergunta ou um menu. Voltar ao menu principal funciona porque o menu espera a escolha do cliente.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Pular para leva a conversa para outro fluxo?** Não. O destino é sempre um bloco do mesmo fluxo. Para passar a conversa para outro fluxo, use o bloco **Trocar Fluxo**.
>
> **Depois do Pular para, as variáveis e tags do atendimento continuam valendo?** Sim. O atendimento segue no bloco de destino com o mesmo contato, as mesmas tags e as mesmas variáveis.
>
> **Posso apontar vários Pular para para o mesmo bloco?** Pode. O bloco de destino mostra quantos saltos recebe no selo **Recebe saltos de N ponto(s)**, e o selo lista cada um deles.
>
> **Posso usar o Pular para para recomeçar o fluxo do Início?** Pode. O **Início** aparece na lista de destinos.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Pular para sem destino:** o fluxo não salva e o editor marca o bloco. **Solução:** abra o **Pular para** com duplo clique e escolha o destino, ou exclua o bloco.
>
> **Localizar bloco antes de Adicionar:** a janela fecha e o **Pular para** novo não entra no desenho. **Solução:** escolha o destino, clique em **Adicionar** e só depois use **Localizar bloco**, abrindo o bloco com duplo clique.
>
> **Ciclo sem espera:** o caminho volta a um bloco sem esperar o cliente, e na execução o fluxo é interrompido. **Solução:** coloque uma pergunta ou um menu no caminho de volta, ou leve o **Pular para** até um bloco que espera a resposta do cliente.
