# Visão Geral FlowBuilder

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/visao-geral-flowbuilder
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Visão Geral FlowBuilder

---

🧩 A tela **FlowBuilder Nativo** lista os fluxos da empresa. Cada card é um fluxo, com os botões para abrir o editor, ver os erros daquele fluxo e cuidar dele: renomear, exportar, duplicar ou excluir.

A tela é do administrador. No mesmo grupo do menu lateral ficam **Categorias**, que organiza os fluxos em grupos, e **Webhooks | Triggers**, com os endereços que fazem um sistema externo iniciar um fluxo.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo**.
>
> ➡️ Clique em **Adicionar Fluxo**, dê um nome e, se quiser, escolha uma categoria.
>
> ➡️ No card do fluxo, clique no ícone de ferramenta para abrir o editor e montar os blocos.

####  

![Visão Geral da Tela de escolha de fluxos do FlowBuilder](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ada3df588bda.png)

## O que tem no topo

🔘 **Categoria:** mostra só os fluxos de uma categoria. Além das categorias da empresa, a lista tem **Todas as categorias** e **Sem categoria**.

🔘 **Buscar fluxos:** filtra a lista pelo nome do fluxo.

🔘 **Automações rápidas:** abre modelos prontos de automação. O modelo escolhido cria um fluxo e um Setor com o mesmo nome, já ligados um ao outro, para você revisar o texto no editor e depois apontar a conexão para esse Setor.

🔘 **Importar:** abre direto a escolha do arquivo. Escolha um arquivo exportado de um fluxo, e ele entra na lista com o nome *Fluxo Importado* seguido de um número. Renomeie em **Editar Nome**.

🔘 **Adicionar Fluxo:** cria um fluxo novo.

## O que cada card mostra

◽ **Nome do fluxo** e o selo de situação, como **Ativo**.

◽ A **categoria** do fluxo, quando ele tem uma, com a cor cadastrada para ela.

À direita do card ficam três ícones:

🔘 **Editar fluxo** (ferramenta): abre o editor, onde o fluxo é desenhado.

🔘 **Ver erros deste fluxo**: abre a lista de erros que o fluxo registrou ao rodar, com filtro de período (**24 horas**, **7 dias** ou **30 dias**) e de nível (**Todos**, **Parou o fluxo** ou **Tolerado**).

🔘 **Mais opções** (três pontos): **Editar Nome**, **Editar Fluxo**, **Exportar Fluxo**, **Duplicar**, **Ver erros** e **Excluir**.

## O que faz cada opção do Mais opções

◽ **Editar Nome:** renomeia o fluxo sem mexer nos blocos.

◽ **Exportar Fluxo:** baixa um arquivo com o fluxo, com o nome dele e a extensão *.json*, para guardar uma cópia ou importar em outra conta.

◽ **Duplicar:** cria uma cópia do fluxo na mesma empresa. Use antes de uma mudança arriscada num fluxo que já atende clientes.

◽ **Excluir:** apaga o fluxo. A plataforma pede confirmação e avisa que as integrações ligadas a ele serão perdidas.

## Como criar um fluxo

Acesse o menu **FlowBuilder Nativo  ›  Adicionar Fluxo**

🔘 **Nome do Fluxo:** um nome que diga para que o fluxo serve, como *Triagem do site* ou *Segunda via*.

🔘 **Categoria (opcional):** agrupa fluxos parecidos. As categorias são cadastradas no menu **Categorias**.

🔲 Clique em **Adicionar**. O fluxo aparece na lista e já pode ser aberto no editor.

⚠️ Fluxo criado não roda sozinho. Ele começa a atender quando é ligado a um ponto de entrada: o Setor de uma conexão, uma tag, uma resposta rápida, uma campanha ou um sistema externo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Não encontro o menu FlowBuilder Nativo.** O menu é do administrador da empresa. Supervisor e atendente não têm acesso a ele.
>
> **Qual a diferença entre Duplicar e Exportar Fluxo?** **Duplicar** cria a cópia dentro da mesma empresa, pronta para editar. **Exportar Fluxo** baixa um arquivo, que serve de cópia de segurança ou para importar o fluxo em outra conta.
>
> **Importei um fluxo e ele apareceu com outro nome.** O fluxo importado entra como *Fluxo Importado* seguido de um número. Use o menu **Mais opções  ›  Editar Nome** para dar o nome certo.
>
> **Usei uma Automação rápida e apareceu um Setor novo.** O modelo cria o fluxo e um Setor com o mesmo nome, ligados entre si. Revise o texto do fluxo no editor e aponte a conexão para esse Setor quando quiser que a automação comece a valer.
>
> **Excluir um fluxo apaga o que estava ligado a ele?** A plataforma avisa que as integrações relacionadas serão perdidas. Antes de excluir, confira onde o fluxo é usado e, se tiver dúvida, exporte uma cópia.
