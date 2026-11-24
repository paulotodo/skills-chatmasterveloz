# Empresas em Configurações

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/configuracoes-empresas
- **Categoria:** Recursos
- **Menu:** Configurações › Empresas em Configurações

---

🧩 O card **Empresas** abre a lista de todas as empresas da instância — cada uma num card com plano, vencimento, limites e contadores — e o ponto de partida para editar, cobrar e criar usuário em qualquer uma delas.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Empresas**.
>
> ➡️ Use a busca e os filtros para achar a empresa; clique no card para editar.
>
> ➡️ Os botões do card fazem o resto: usuário novo, faturas, relatório.

## Busca e filtros

🔘 **Buscar empresas:** por nome ou e-mail.

🔘 **Deletadas:** **Ativas** (as que existem) ou **Deletadas** (as excluídas, que continuam consultáveis).

🔘 **Status:** filtra por status da empresa. As opções são **Todos**, **Ativa** ou **Inativa**.

🔘 **Acesso:** **Todos**, **Pode Acessar** ou **Sem Acesso** — separa quem está bloqueado de entrar.

🔘 **Plano:** filtra pelo plano assinado.

## O que cada card mostra

Na ordem: nome da empresa, e-mail do responsável, o status (**Ativa** ou **Inativa**), o número da empresa, **Telefone**, **País**, **Conexões** (o total em uso / o limite geral do plano), **Usuários**, **Vencimento**, **Mensagens** (contador), o plano, a recorrência e o valor.

⚠️ **Conexões** mostra o total de conexões da empresa sobre o limite **geral** do plano, e esse limite vale para cada canal. Uma empresa em `5 / 2`, com uma conexão em cada canal, não está acima do plano. Quem diz se a empresa passou do limite é o card **Conciliação de conexões**, no **Excedente** de cada canal.

## As ações do card

🔘 **Clicar no card:** abre **Editar Empresa**, com quatro abas. A opção **Deletar** a empresa aparece ao abrir o card.

🔘 **Adicionar Usuário:** cria um usuário dentro daquela empresa, sem precisar entrar nela. A janela pede **Nome**, **Senha**, **E-Mail**, **Perfil** e **Setores**; **ADICIONAR** cria o usuário.

🔘 **Gerenciar Faturas:** a tabela das faturas da empresa, com **ID**, **Status**, **Valor**, **Vencimento**, **Detalhes** e **Ações**. As ações da linha são **Editar Valor**, **Marcar como Pago** e **Remover Fatura**.

🔘 **Migração:** abre a janela **Migração de empresa — ensaio**, que mostra o que a empresa levaria numa migração para outro servidor, sem migrar nada.

🔘 **Visualizar Relatório:** página nova com um relatório com informações gerais da empresa como: data de registro, conexões usadas, quantidade de mensagens, setor, usuários, grupos, campanhas e agendamentos.

## Migração de empresa — ensaio

A janela **Migração de empresa — ensaio** é uma prévia. Nas palavras da tela: *"Nada foi migrado. Esta tela mostra o que SAIRIA daqui se a migração fosse executada — a empresa segue ativa e as conexões no ar."*

🔘 **Linhas**, **Banco (estimado)**, **Mídias** e **Tabelas com dados:** o tamanho do que a empresa levaria.

🔘 **Avisos:** o que pede atenção antes de migrar — dado cruzado com outras empresas, credenciais das conexões que não vão junto e os e-mails de usuário que precisam estar livres no destino. O e-mail de usuário é único no servidor inteiro, e não por empresa: se algum já existir no servidor de destino, a importação para antes de começar.

🔘 **Servidor de destino:** a **URL do backend de destino** (a do backend, não a do painel) e o botão **TESTAR**, que só pergunta se aquele servidor conseguiria receber a empresa.

🔘 **O que vai:** a tabela das partes da empresa que seguiriam na migração.

🔘 **Mídias:** os arquivos não vão junto com o resto; a janela orienta copiá-los por **rsync**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Uma empresa sumiu da lista.** No filtro **Deletadas**, escolha **Deletadas** e procure lá. Se estiver, foi excluída; se não, confira os filtros de **Status** e **Acesso**.
>
> **A empresa está Ativa, mas o administrador não consegue entrar.** São coisas diferentes: **Status** é a situação da conta; **Acesso** é a permissão de login. Abra o card e veja **Pode Acessar?**.
>
> **Onde crio uma empresa nova?** Não é aqui — é no card **Cadastrar Empresa**.
