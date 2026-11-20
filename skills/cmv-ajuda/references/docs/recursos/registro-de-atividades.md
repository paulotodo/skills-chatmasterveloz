# Registro de Atividades

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/registro-de-atividades
- **Categoria:** Recursos
- **Menu:** Equipe › Registro de Atividades

---

🧩 Alguém alterou uma configuração e ninguém sabe quem foi? Um atendente jura que não excluiu aquele cadastro? Sem um histórico, cada dúvida dessas vira discussão. O **Registro de Atividades** é o diário de bordo da sua plataforma: cada ação relevante feita por alguém da equipe fica anotada com **quem** fez, **quando**, de **qual endereço** de rede e **o que** exatamente foi enviado — para você reconstruir o que aconteceu quando algo sair do esperado.

Pense nele como a caixa-preta de um avião: não existe para vigiar a tripulação no dia a dia, existe para entender um incidente depois que ele acontece. No menu a tela se chama **Registro de Atividades**; o título dentro dela é **Logs de Auditoria** — é a mesma coisa.

Ideal para:

☑️ **Investigação de incidente:** mostra quem mudou uma configuração, apagou um cadastro ou alterou um acesso, e quando.

☑️ **Segurança do acesso:** registra as tentativas de login recusadas — senha errada, código de dois fatores inválido, conta desativada, acesso fora do horário ou de um endereço não autorizado.

☑️ **Prova para auditoria:** exporta o histórico em CSV para guardar fora da plataforma ou anexar a um processo interno.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Registro de Atividades**.
>
> ➡️ Use os filtros — **Buscar por IP ou detalhes**, **Ação**, **Usuário**, **Data Início** e **Data Fim** — para achar o que procura. Eles se somam.
>
> ➡️ Clique em **Carregar Mais** para ver registros mais antigos e em **Atualizar** para trazer os mais novos.
>
> ➡️ Em um registro, abra **Ver payload** para ler o conteúdo exato daquela ação.

## O que a tela mostra

No topo, três cards resumem o histórico: o **Total de Logs**, as **Ações Bloqueadas** — acessos barrados por uma regra sua, como conta desativada, endereço fora da lista permitida ou horário não liberado, que a plataforma separa de um simples erro de senha — e os **Usuários Monitorados**, quantas pessoas têm registro. Os três seguem os filtros: escolhendo uma pessoa, eles contam só os registros dela.

Abaixo vem a lista, do mais recente para o mais antigo. Cada registro é um card com:

🔘 **Ação:** o nome fixo do que aconteceu, no topo do card — por exemplo **LOGIN** para uma entrada bem-sucedida e **LOGIN_FAILED** para uma tentativa recusada. Ao lado, uma etiqueta com o tipo da requisição, como **POST** ou **PUT**.

🔘 **Quem:** o nome da pessoa e o e-mail dela. Nos registros feitos pela própria plataforma, como a reabertura de um atendimento quando o cliente volta a escrever, aparece **Sistema**, com a etiqueta **SISTEMA** no lugar do tipo da requisição e *sistema* no **Endereço IP** e no **User Agent**.

🔘 **Data/Hora:** o momento exato.

🔘 **Endereço IP:** o endereço de rede de onde a ação partiu. É por ele que a busca encontra tudo que veio de um mesmo lugar.

🔘 **Caminho:** o endereço interno que a ação acionou na plataforma.

🔘 **User Agent:** o navegador e o sistema de quem fez.

🔘 **Motivo:** só nas tentativas de acesso recusadas — **Senha inválida**, **Conta desativada**, **IP fora da lista permitida**, **Fora do horário de trabalho**, código de dois fatores inválido ou inativo, ou empresa removida. Erro de credencial e bloqueio por regra aparecem com cores e ícones diferentes.

🔘 **Ver payload:** abre o conteúdo completo do que foi enviado naquela ação, em JSON, com botões para abrir, fechar e copiar. Ele traz inclusive campos que o formulário não mostra na tela.

⚠️ Senhas, tokens e outros segredos **nunca aparecem** no payload — em nenhum nível e em nenhuma grafia do campo, mesmo quando vieram pelo endereço da requisição. Uma tentativa de login com senha errada registra o motivo, não a senha digitada.

⚠️ Tentativa de login com um e-mail que **não existe** na plataforma **não gera registro**. É de propósito: se gerasse, o histórico revelaria quais e-mails têm conta.

## A reabertura de atendimentos

Quando um atendimento encerrado é reaberto — por exemplo, porque o cliente voltou a escrever —, o **Registro de Atividades** ganha um registro **TICKET_REOPENED**, em nome do **Sistema**. Esse registro entra mesmo com a opção **Registrar Logs de Ação dos Atendimentos?** em **Não**.

O **Ver payload** da reabertura traz:  
- `ticketId` — o número do atendimento.
- `de` e `para` — a situação antes e depois: de `closed` (encerrado) para `pending` (aguardando), ou para `open` (em atendimento), quando o atendimento volta direto para o atendente.
- `origem` — o que reabriu o atendimento, como *mensagem recebida*, quando foi o cliente que voltou a escrever.
- `emMassa` — se a reabertura foi feita em massa (`true`) ou não (`false`).

## Os filtros

🔘 **Buscar por IP ou detalhes:** encontra os registros pelo endereço de quem fez a ação ou por um trecho do que foi enviado.

🔘 **Ação:** o tipo do registro. A lista mostra os nomes técnicos das ações registradas na sua empresa — como **LOGIN**, **LOGOUT**, **CREATE_USER**, **CREATE_TAG**, **UPDATE_CONNECTION**, **DELETE_CONTACT** e **TICKET_REOPENED**.

🔘 **Usuário:** só os registros de uma pessoa.

🔘 **Data Início** e **Data Fim:** o período.

## Os botões da tela

🔘 **Exportar CSV:** baixa o histórico em planilha, para guardar fora da plataforma ou anexar a um relatório.

🔘 **Atualizar:** recarrega a lista com os registros mais recentes.

🔘 **Limpar:** limpa a busca e os filtros e devolve a lista completa. **Não apaga registro nenhum** — o histórico continua inteiro.

🔘 **Carregar Mais:** a lista não tem páginas numeradas — cada clique traz o próximo bloco de registros mais antigos.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O botão Limpar apaga o histórico?** Não. Ele só zera a busca e os filtros. O registro de atividades não pode ser apagado pela tela.
>
> **Um atendente errou a senha várias vezes — isso aparece?** Sim: cada tentativa recusada vira um registro **LOGIN_FAILED** com o motivo **Senha inválida** e o endereço de onde veio. A senha digitada não fica gravada em lugar nenhum.
>
> **Alguém não consegue entrar. Como descubro o motivo?** Escolha a pessoa no filtro **Usuário**. A tentativa barrada por uma regra traz o **Motivo** — **Conta desativada**, **IP fora da lista permitida** ou **Fora do horário de trabalho** — e conta em **Ações Bloqueadas**.
>
> **Quero ver o que uma pessoa fez num dia.** Escolha a pessoa em **Usuário** e o mesmo dia em **Data Início** e **Data Fim**.
>
> **Mudanças de configuração aparecem no Registro de Atividades?** Sim. Criar, editar e excluir tags, editar e excluir conexões, excluir contatos, criar usuários, mudar opções das Configurações e mexer em fluxos e oportunidades aparecem, cada um com o nome técnico da ação no filtro **Ação**.
>
> **Alguém tentou entrar com um e-mail que nem existe. Por que não vejo?** Porque a plataforma só registra tentativas em contas que existem — assim o histórico não denuncia quais e-mails têm cadastro.
>
> **Posso ver o que exatamente foi alterado numa ação?** Abra **Ver payload** no registro: ele mostra o conteúdo enviado, campo a campo, inclusive o que o formulário não exibe na tela.
>
> **O menu Registro de Atividades não aparece para mim.** O **Registro de Atividades** é do administrador: supervisor e atendente não têm o item no menu.
>
> **Quem é o Sistema que aparece no Registro de Atividades?** É a própria plataforma: **Sistema** aparece nos registros feitos por ela, como a reabertura de um atendimento quando o cliente volta a escrever (**TICKET_REOPENED**). Nesses registros, a etiqueta é **SISTEMA**, e o **Endereço IP** e o **User Agent** dizem *sistema*.
>
> **Como vejo quando um atendimento encerrado foi reaberto?** No filtro **Ação**, escolha **TICKET_REOPENED**. Cada registro mostra quando o atendimento voltou, e o **Ver payload** traz o número do atendimento, de qual situação para qual ele foi e a origem, como *mensagem recebida*.
