# Criar Template pela Plataforma

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/criar-template-pela-plataforma
- **Categoria:** Recursos
- **Menu:** Conexões › WhatsApp › Criar Template pela Plataforma

---

🧩 Template é a mensagem aprovada pela Meta que a conexão oficial usa para iniciar uma conversa ou falar com o cliente fora da janela de atendimento. Ele pode ser criado sem sair da plataforma: o botão **NOVO TEMPLATE**, na **Gestão de Templates**, abre um assistente em três passos que monta o template e o envia para a análise da Meta.

Ideal para:

☑️ **Criação no mesmo lugar do atendimento:** O template nasce na conexão em que vai ser usado, sem abrir o Gerenciador do WhatsApp na Meta.

☑️ **Prévia antes do envio:** A **Prévia do modelo** mostra, ao lado dos campos, como a mensagem vai chegar ao cliente.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões** e, no card da conexão oficial, clique em **Gestão de Templates**.
>
> ➡️ Clique em **NOVO TEMPLATE**, escolha a categoria e o tipo, e clique em **PRÓXIMO**.
>
> ➡️ Apague o exemplo que vem nos campos, escreva o seu template e clique em **PRÓXIMO**.
>
> ➡️ Confira o resumo e clique em **ENVIAR PARA APROVAÇÃO**.

## Passo 1: Configurar modelo

Acesse o menu **Conexões**, clique em **Gestão de Templates** no card da conexão oficial e depois em **NOVO TEMPLATE**.

🔘 **Conexão WABA:** a conexão oficial onde o template vai existir. Cada conexão tem os seus templates: o mesmo texto precisa ser aprovado em cada número.

🔘 **MARKETING, UTILIDADE e AUTENTICAÇÃO:** as três abas são as categorias da Meta. **Utilidade** avisa sobre algo que o cliente já espera porque fez alguma coisa antes, como pedido confirmado ou fatura a vencer. **Marketing** chama a atenção para algo que a empresa quer mostrar, como promoção e novidade. **Autenticação** é o código de verificação.

🔘 **Tipo de mensagem:** dentro de cada aba, a tela pede o tipo. **Padrão** é a mensagem com texto, mídia e botões, e existe nas três abas. **Solicitação de permissões para ligação** pergunta ao cliente se a empresa pode ligar para ele pelo WhatsApp, em Marketing e em Utilidade. Só em Marketing aparecem **Catálogo**, que liga a mensagem ao catálogo de produtos, e **Detalhes do pedido**, para o cliente fazer o pagamento.

## Passo 2: Editar modelo

⚠️ Os campos deste passo abrem com um exemplo de promoção já escrito: cabeçalho, corpo, rodapé e dois botões. Apague o que não for usar e escreva o seu texto, conferindo na **Prévia do modelo** antes de clicar em **PRÓXIMO**.

🔘 **Nome do template:** a identificação do template na lista e na hora de enviar. A tela converte o nome enquanto você digita: letra maiúscula vira minúscula e espaço vira sublinhado, então `Pedido Pronto` vira `pedido_pronto`. O **PRÓXIMO** só libera com o nome preenchido.

🔘 **Idioma:** o idioma em que o texto foi escrito.

🔘 **Amostra de mídia:** opcional. **Nenhum**, **Imagem**, **Vídeo**, **Documento** ou **Localização**. Com **Imagem**, por exemplo, aparece o botão para escolher o arquivo, e o **Cabeçalho** passa a ser a imagem, no lugar do texto.

🔘 **Cabeçalho:** a linha de destaque no topo da mensagem. O campo aceita até 60 caracteres.

🔘 **Corpo da mensagem:** o texto principal, com até 1.024 caracteres. As variáveis `{{1}}`, `{{2}}` marcam o que muda a cada envio, como o nome do cliente ou o número do pedido.

🔘 **Exemplo para variável:** para cada variável escrita no corpo, a tela abre um campo de exemplo, e é esse exemplo que a Meta lê na aprovação. Use um valor realista e inventado, como um nome ou um número de pedido, nunca o dado de um cliente de verdade.

🔘 **Rodapé:** uma linha discreta no fim da mensagem, com até 60 caracteres.

🔘 **Botões:** cada botão tem um **Tipo** (**Resposta rápida**, **URL** ou **Telefone**) e o **Texto do botão**. O tipo **URL** pede também o endereço. **ADICIONAR BOTÃO** inclui outro.

## Passo 3: Enviar para análise

A tela resume **Nome**, **Categoria** e **Idioma** e avisa que o template será enviado para aprovação da Meta, num processo que pode levar até 24 horas. Para corrigir algo, use **VOLTAR**. Estando certo, clique em **ENVIAR PARA APROVAÇÃO**.

A situação de cada template aparece no card dele, na lista da **Gestão de Templates**, e o filtro **Status** mostra só os templates numa situação, como aprovado ou rejeitado.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Quanto tempo a Meta leva para aprovar um template criado na plataforma?** O passo **Enviar para análise** avisa que a aprovação pode levar até 24 horas.
>
> **Por que o Nome do template muda enquanto eu digito?** A tela converte o nome para letras minúsculas, com sublinhado no lugar dos espaços. É com esse nome que o template aparece na lista da **Gestão de Templates**.
>
> **Qual categoria escolher no NOVO TEMPLATE, Marketing ou Utilidade?** Pergunte se o cliente está esperando aquela mensagem porque fez alguma coisa antes. Se sim, é **Utilidade**. Se é a empresa querendo mostrar algo, é **Marketing**. Uma única frase de oferta dentro de um template de Utilidade faz a Meta tratar o template inteiro como Marketing.
>
> **O que escrevo no Exemplo para variável?** Um valor que mostre à Meta o que a variável vai receber: um nome para a variável do nome, um número para a do pedido. É o exemplo que a Meta lê para aprovar, e ele não pode ser o dado de um cliente real.
>
> **Criei o template no Gerenciador da Meta. Preciso criar de novo na plataforma?** Não. Na **Gestão de Templates**, clique em **SINCRONIZAR** para trazer da Meta os templates que ainda não apareceram na lista.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Enviar o exemplo da tela no lugar do seu texto:** o passo **Editar modelo** abre com um texto de promoção, botões e um endereço de exemplo já preenchidos, e quem só troca o nome deixa esse conteúdo no template. **Solução:** apague cada campo que não for usar e confira a **Prévia do modelo** antes de clicar em **PRÓXIMO**.
>
> **Escolher Utilidade para uma mensagem com oferta:** o texto vendedor faz a Meta tratar o template como Marketing. **Solução:** no template de Utilidade, informe e pare; a oferta vai num template de Marketing.
