# Como Usar o Editor de Fluxos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/como-usar-o-editor-de-fluxos
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Editor de Fluxos › Como Usar o Editor de Fluxos

---

🧩 O **Editor de Fluxos** é o quadro onde o fluxo é desenhado: cada bloco é uma etapa da conversa, e as linhas entre eles dizem o que vem depois. Todo fluxo começa no bloco **Início**, que representa a mensagem vinda do cliente.

O editor abre pelo card do fluxo, no ícone de ferramenta. É nele que você adiciona e liga os blocos, confere se o caminho está completo e salva.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e clique no ícone de ferramenta do fluxo.
>
> ➡️ Clique no botão **+**, escolha um bloco e preencha a janela dele.
>
> ➡️ Ligue o ponto de saída de um bloco ao ponto de entrada do próximo.
>
> ➡️ Clique em **SALVAR FLUXO**.
>
> ![FlowBuilder Tela do Canva Editor Visual de Fluxo](https://clihelper.chatmasterveloz.com/docs-imagem/26795-flowbuilder-canva-editor-de-fluxo.jpg)

## Como adicionar um bloco

O botão **+**, no canto superior esquerdo, abre a janela **Escolha uma Ação**, com todos os blocos disponíveis e o campo **Buscar ação...** para achar um bloco pelo nome.

Clique no bloco: abre a janela **Adicionar bloco**, seguida do nome do bloco, como *Adicionar bloco: Menu*. Preencha e clique em **Adicionar**, e o bloco aparece no desenho. Alguns blocos não têm o que configurar e entram direto no desenho, já com as saídas.

⚠️ Cada fluxo tem limite de **45 MB**, e o selo ao lado do **SALVAR FLUXO** mostra quanto o fluxo já ocupa. A partir de 36 MB, o editor avisa quanto do limite já foi usado a cada bloco novo e a cada vez que você salva. Acima de 45 MB, ele não deixa adicionar blocos nem salvar, e sugere dividir o trabalho em fluxos menores.

## Como mexer nos blocos

◽ **Mover:** clique no bloco e arraste.

◽ **Editar:** duplo clique no bloco abre a janela dele de novo, com o título **Editar bloco**, seguido do nome do bloco.

◽ **Duplicar** e **Excluir:** os dois ícones no canto superior direito do bloco. Para excluir, também dá para clicar no bloco e apertar a tecla **Delete** ou **Backspace**.

◽ **Ligar:** cada bloco tem um ponto de entrada à esquerda e um ou mais pontos de saída à direita. Clique num ponto de saída e arraste até o ponto de entrada do bloco seguinte. Bloco com mais de uma saída, como a **Condição** com **Verdadeiro** e **Falso**, precisa de uma ligação em cada saída.

➡️ Para levar a conversa até um bloco distante sem desenhar uma linha comprida, use o bloco **Pular para**.

## A barra do editor

No alto, à direita, ficam as ferramentas do editor:

🔘 **Desfazer (Ctrl+Z)** e **Refazer (Ctrl+Shift+Z):** o **Desfazer** volta a última mudança no desenho, como um bloco apagado por engano ou movido de lugar, e o **Refazer** devolve o que foi desfeito. O atalho **Ctrl+Y** também refaz.

🔘 **Buscar blocos (Ctrl+F):** procura um bloco por tipo, conteúdo ou ID, útil quando o fluxo já está grande.

🔘 **Resumo do fluxo:** mostra quantos blocos e ligações o fluxo tem, quantos blocos há de cada tipo e os avisos do que está faltando.

🔘 **Organizar automaticamente:** rearruma a posição dos blocos na tela.

🔘 **Verificar:** confere se todos os blocos estão ligados ao caminho que começa no Início e aponta os que não estão.

🔘 **Versões:** abre o **Histórico de Versões** do fluxo.

🔘 **SALVAR FLUXO:** grava o fluxo e confirma com *Fluxo salvo com sucesso (versão de backup criada)*. O atalho **Ctrl+S** faz o mesmo. Com mudança ainda não salva, o botão vira **SALVAR *** e o topo mostra **ALTERAÇÕES NÃO SALVAS** antes do nome do fluxo. Depois de salvar, o topo volta a **Fluxo salvo**.

Ao lado do botão de salvar, o selo mostra o **tamanho do fluxo**.

⚠️ O editor salva mesmo com blocos que nenhum caminho alcança. Nesse caso ele avisa quantos são, como *2 bloco(s) não alcançável(is) a partir do início*, e o **Verificar** mostra quais.

## Versões do fluxo

Cada vez que você salva, o editor cria uma versão de backup do fluxo, até **30 versões por fluxo**. Em **Versões** fica a lista, com a última marcada como **Mais recente**, e cada versão tem a opção **Restaurar esta versão**.

Ao restaurar, a plataforma pede confirmação: *O fluxo atual será substituído. Salve antes se quiser preservar a versão atual.*

⚠️ **Restaurar grava na hora.** O fluxo que atende os clientes passa a ser a versão restaurada assim que você confirma, mesmo que o topo do editor mostre **ALTERAÇÕES NÃO SALVAS**. Se a versão atual ainda pode servir, salve antes de restaurar: ela vira mais uma versão na lista.

Use **Versões** para voltar a um ponto anterior depois de salvar. Antes de salvar, quem desfaz é o **Desfazer (Ctrl+Z)**.

## Se você sair sem salvar

Sair do editor sem clicar em **SALVAR FLUXO** não grava nada: o fluxo que atende os clientes continua sendo o último salvo. Se você tentar fechar a aba ou sair da página com mudanças não salvas, o navegador pergunta se quer mesmo sair.

O editor guarda uma cópia do desenho **no navegador**. Ao reabrir o fluxo, se essa cópia for mais nova que a versão salva e tiver mais blocos que ela, aparece a janela **Recuperação de Fluxo**, com a quantidade de blocos e a data do **Backup local** e a quantidade de blocos do **Servidor**:

🔘 **Restaurar Backup Local:** traz a cópia do navegador de volta para o desenho. Ela ainda não está salva: clique em **SALVAR FLUXO** para valer.

🔘 **Ignorar (usar servidor):** fica com a última versão salva.

⚠️ A cópia existe só no navegador onde você trabalhou. Em outro computador ou outro navegador ela não aparece. E mudança só no texto de um bloco que já existia não é oferecida de volta: salve antes de sair.

## Os controles do desenho

◽ **Canto inferior esquerdo:** aproximar (**+**), afastar (**−**), ajustar o fluxo inteiro na tela e o cadeado, que trava o desenho para nenhum bloco ser arrastado sem querer.

◽ **Canto inferior direito:** o minimapa, uma miniatura do fluxo inteiro.

◽ **Arrastar a tela:** clique num espaço vazio do fundo e arraste. A rolagem do mouse também aproxima e afasta.

## Atalhos de teclado

◽ **Ctrl+S:** salva o fluxo, como o botão **SALVAR FLUXO**.

◽ **Ctrl+Z:** desfaz a última mudança no desenho.

◽ **Ctrl+Shift+Z** ou **Ctrl+Y:** refaz o que foi desfeito.

◽ **Ctrl+F:** abre a busca de blocos.

◽ **Delete** ou **Backspace:** apaga o bloco selecionado.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Saí do editor sem clicar em SALVAR FLUXO. Perdi o que fiz?** O que não foi salvo não chegou ao fluxo que atende os clientes. Se você reabrir o fluxo no mesmo navegador e a cópia guardada tiver mais blocos que a versão salva, a janela **Recuperação de Fluxo** oferece trazê-la de volta.
>
> **Apaguei um bloco do fluxo por engano. Como recupero?** Antes de salvar, use **Desfazer (Ctrl+Z)**. Se já salvou, abra **Versões** e restaure uma versão anterior.
>
> **Restaurei uma versão em Versões. Preciso salvar?** Não para valer: a restauração já grava a versão escolhida no fluxo. O topo do editor continua mostrando **ALTERAÇÕES NÃO SALVAS**, e salvar só cria mais uma versão na lista.
>
> **Movi um bloco de lugar sem querer. O Desfazer volta o bloco?** Volta. Mover um bloco entra no **Desfazer (Ctrl+Z)**, e o bloco volta para onde estava.
>
> **Tem atalho para salvar o fluxo no editor?** Tem: **Ctrl+S** salva, como o botão **SALVAR FLUXO**.
>
> **Como acho um bloco num fluxo grande?** Use **Buscar blocos (Ctrl+F)** na barra do editor. A busca procura pelo tipo do bloco, pelo conteúdo ou pelo ID.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Sair sem salvar:** o topo do editor mostra **ALTERAÇÕES NÃO SALVAS** e o fluxo que atende os clientes continua o antigo. **Solução:** clique em **SALVAR FLUXO** antes de fechar a tela.
>
> **Restaurar sem salvar antes:** a versão que estava no editor some do fluxo assim que a restauração é confirmada. **Solução:** salve primeiro, para a versão atual também ficar na lista de **Versões**.
>
> **Saída de bloco sem ligação:** o cliente chega ao bloco e a conversa não tem para onde seguir. **Solução:** use **Verificar** antes de salvar e ligue cada saída que ele apontar.
