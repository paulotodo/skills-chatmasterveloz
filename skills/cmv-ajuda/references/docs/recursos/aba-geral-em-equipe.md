# Aba Geral em Equipe

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-geral-em-equipe
- **Categoria:** Recursos
- **Menu:** Equipe › Aba Geral em Equipe

---

🧩 A aba **Geral** é a identidade da pessoa na plataforma: quem ela é, qual o perfil, em que horário trabalha e o que a plataforma responde por ela quando ela não está.

Para criar alguém, basta esta aba, com **Nome**, **E-Mail** e **Senha**. As outras três podem ser preenchidas depois, editando.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Equipe** e clique em **Adicionar usuário**, ou no lápis de uma pessoa.
>
> ➡️ Preencha **Nome**, **E-Mail**, **Senha** e escolha o **Perfil**. Salve.
>
> ➡️ Depois de salvo, volte para enviar a foto e ajustar o resto.

## Dados

🔘 **Foto:** aparece só dentro da plataforma, para a equipe: no card da pessoa e, no lugar das iniciais, nas telas que mostram quem é o responsável. A tela avisa: *"Visível somente dentro da aplicação - não é enviada para o cliente."* **Enviar foto** abre a escolha da imagem, e a foto sobe na hora, com o aviso *"Foto atualizada"*, sem esperar o **Salvar** da janela: fechar a janela em **Cancelar** não desfaz a troca. Com a foto no lugar, os botões viram **Trocar foto** e **Remover**, que tira a foto com o aviso *"Foto removida"*. O botão **Enviar foto** só destrava depois que a pessoa foi salva.

🔘 **Nome**, **Telefone** e **E-Mail:** o e-mail é o login.

🔘 **Senha:** a senha inicial, obrigatória para criar a pessoa. Para trocar depois, use **Trocar Senha** no card. Quando a plataforma exige senha forte (opção **Exigir senha forte**), a senha precisa ter no mínimo 8 caracteres, com maiúscula, minúscula, número e caractere especial.

🔘 **Perfil:** **Admin**, **User** ou **Supervisor** e, quando estão disponíveis no seu plano, **Entregador** e **Garçom**. Define o menu inteiro. **Entregador** e **Garçom** são os perfis de quem só faz entregas ou só atende as mesas: a pessoa entra direto numa tela só, sem o menu. No cadastro novo o campo já vem como **User**: quem cria um administrador sem mudar o campo cria um atendente.

🔘 **Restringir acesso apenas aos setores específicos:** aparece só quando o perfil é **Supervisor**, logo abaixo do campo **Perfil**. Com **SIM**, o supervisor vê só os atendimentos dos Setores marcados para ele na aba **Setores e Conexões** — os atendimentos sem Setor, por exemplo, deixam de aparecer para ele. Com **NÃO**, ele vê também esses.

🔘 **Ocultar números (mostrar só os 4 últimos):** com **SIM**, a pessoa vê os telefones dos contatos mascarados, só com os quatro últimos dígitos — por exemplo, `********7154`.

⚠️ Contato sem nome salvo aparece com o próprio número no lugar do nome, e esse número continua inteiro mesmo com **Ocultar números** em **SIM**.

## Campos extras

🔘 **Campo extra 1** e **Campo extra 2:** dois campos livres para guardar a informação da pessoa que não tem lugar próprio no cadastro — a matrícula, a unidade, o centro de custo. Cada um aceita até 1.000 caracteres.

🔘 **A variável de cada campo** vem escrita embaixo dele. Nas palavras da tela: *Nas mensagens e no fluxo, use* `{{user_extra1}}` — e `{{user_extra2}}` para o **Campo extra 2**.

## Mensagens

🔘 **Despedida ao encerrar:** a regra da despedida nos atendimentos desta pessoa. **Seguir a do setor, da conexão e da empresa** deixa a decisão para o Setor, a Conexão e a empresa; **Sempre enviar a despedida (obrigatória)** faz a pessoa só encerrar com a despedida, e o **Resolver sem Mensagem de Encerramento** some; **Nunca enviar despedida** encerra sem enviar a despedida ao cliente. Nas palavras da tela: *"Vale a primeira que não segue: a do usuário, a do setor, a da conexão; sem nenhuma, a da empresa (Opções)."* A regra da pessoa vence a do Setor e a da Conexão.

🔘 **Mensagem de Despedida:** o texto enviado ao cliente quando esta pessoa encerra um atendimento com a despedida. Vale antes da **Mensagem de despedida do setor** e do texto de encerramento da Conexão.

🔘 **Mensagem de Ausência:** o texto enviado quando o cliente escreve e a pessoa não está disponível.

🔘 **Ativar Siga-Me:** encaminha as mensagens dos atendimentos desta pessoa para o WhatsApp particular dela, que responde de lá sem entrar na plataforma. Exige o número preenchido em formato internacional.

## Horário de Trabalho

🔘 **Horário de Trabalho:** um horário para cada dia da semana, com **Hora Inicial** e **Hora Final**. Nas palavras da tela: *Use o + para dividir o dia em mais de um horário. Dia em branco não bloqueia; 00:00 às 00:00 é folga.*

🔘 **Adicionar outro intervalo de trabalho** (o **+** de cada dia): divide o dia em mais de uma faixa, para quem trabalha em turnos — por exemplo, das 8h às 12h e das 14h às 18h. A pessoa entra dentro de qualquer uma das faixas.

**Para o perfil User, o horário é controle de acesso:** fora da faixa do dia — e no dia de folga — a pessoa não consegue entrar, e lê *Acesso fora do horário permitido!*. Administrador e supervisor entram mesmo fora do horário.

**O horário daqui vence o padrão da empresa:** quem tem **Horário de Trabalho** preenchido continua com o seu mesmo quando a empresa liga o **Horário padrão para todos os usuários**, no menu **Configurações  ›  Opções  ›  Geral**, seção **Gerenciamento de Expediente**. Quem não tem horário próprio segue o padrão da empresa.

⚠️ Dia preenchido pela metade não salva: a tela avisa *Confira o horário de trabalho: cada dia precisa do horário inicial e do final, ou ficar em branco.*

🔘 **Limite de atendimentos simultâneos:** quantos atendimentos abertos a pessoa pode ter ao mesmo tempo. Nas palavras da tela: *Vazio = sem limite. Ao chegar neste número de atendimentos abertos, o operador sai do rodízio até fechar algum.* Com a opção **Bloquear aceitar acima do limite de atendimentos** ligada no menu **Configurações  ›  Opções  ›  Atendimento**, seção **Distribuição e rodízio**, a pessoa no limite também não aceita atendimento do **Aguardando** nem abre conversa nova.

## Interface

🔘 **Medidor de conectividade:** mostra o indicador de conexão na barra superior. Nas palavras da tela: *desligado, o indicador some e o teste de conexão a cada 30 segundos também para*.

🔘 **Página inicial após o login:** a tela que abre assim que a pessoa entra — por exemplo **Chats**, **Quadro de atendimentos**, **Dashboard**, **CRM — Board**, **Tarefas**, **Contatos** ou **Agendamentos**. O **Dashboard** só aparece na lista quando o perfil da pessoa é **Admin** ou **Supervisor**. **Padrão (Chats)** mantém os Chats. Nas palavras da tela: *só aparecem as páginas que o perfil dele e o plano da empresa abrem — e, se alguma delas deixar de valer depois, o login volta a abrir os Chats em vez de mostrar uma tela vazia*.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A pessoa não consegue entrar e a senha está certa.** Veja o **Horário de Trabalho** dela no dia de hoje: fora da faixa do dia, ou com o dia em **00:00 às 00:00** (folga), o login do perfil User é barrado com *Acesso fora do horário permitido!*. Se ela não tem horário próprio, veja o **Horário padrão para todos os usuários** da empresa, no menu **Configurações  ›  Opções  ›  Geral**, seção **Gerenciamento de Expediente**.
>
> **A pessoa trabalha de manhã e à tarde, com intervalo de almoço.** No dia, use o **+** e cadastre as duas faixas.
>
> **A pessoa folga no sábado.** Deixe o sábado em **00:00 às 00:00**. Dia em branco não bloqueia: ela entraria a qualquer hora.
>
> **O supervisor entrou fora do horário de trabalho.** É o esperado: o horário só barra a entrada do perfil **User**.
>
> **Cadastrei um administrador e ele entrou com o menu de atendente.** O **Perfil** do cadastro novo vem como **User**. Troque para **Admin** e salve: o menu dele muda na hora.
>
> **Salvei sem senha e o cadastro não foi criado.** A **Senha** é obrigatória: sem ela, a plataforma recusa o cadastro com o aviso *password is a required field* e a janela fecha. Abra **Adicionar usuário** de novo e preencha a senha.
>
> **Não consigo enviar a foto.** A pessoa ainda não foi salva. Salve primeiro; o botão destrava depois.
>
> **Troquei a foto do usuário e fechei a janela em Cancelar. A foto antiga voltou?** Não. A foto sobe na hora em que é escolhida, com o aviso *"Foto atualizada"*, sem depender do **Salvar**. Para tirar, use **Remover**.
>
> **O que muda para quem tem o Perfil Entregador ou Garçom?** A pessoa entra numa tela só, sem o menu: o **Entregador** vê as entregas que estão com ele, e o **Garçom**, as mesas e as comandas do salão.
>
> **Os perfis Entregador e Garçom não aparecem no campo Perfil.** Os dois só aparecem quando estão disponíveis no seu plano. Sem eles, o campo **Perfil** mostra **Admin**, **User** e **Supervisor**.
>
> **Quero que a pessoa não veja o telefone completo dos clientes.** **Ocultar números** em **SIM**.
>
> **A pessoa reclama que o indicador de conexão pisca o tempo todo.** Desligue o **Medidor de conectividade** no cadastro dela. O teste a cada 30 segundos para junto.
>
> **Quero que o vendedor já entre no CRM.** Em **Página inicial após o login**, escolha **CRM — Board**. Se o perfil ou o plano deixar de abrir o CRM, o login volta a abrir os Chats.
>
> **Quero que o supervisor já entre no Dashboard.** Em **Página inicial após o login**, escolha **Dashboard**. A opção só aparece quando o perfil da pessoa é **Admin** ou **Supervisor**.
>
> **Para que servem o Campo extra 1 e o Campo extra 2 do usuário?** Guardam uma informação da pessoa que o cadastro não tem, como a matrícula ou a unidade, para usar nas mensagens e no fluxo com as variáveis `{{user_extra1}}` e `{{user_extra2}}`.
>
> **A empresa ligou o horário padrão. O Horário de Trabalho do cadastro da pessoa ainda vale?** Sim. O **Horário de Trabalho** do cadastro vence o **Horário padrão para todos os usuários** da empresa: quem tem horário próprio continua com o seu.
>
> **Como faço um atendente sempre enviar a despedida ao encerrar?** Em **Despedida ao encerrar**, escolha **Sempre enviar a despedida (obrigatória)**: nos atendimentos dele, o **Resolver sem Mensagem de Encerramento** some, mesmo que o Setor ou a Conexão estejam em **Nunca enviar despedida**.
