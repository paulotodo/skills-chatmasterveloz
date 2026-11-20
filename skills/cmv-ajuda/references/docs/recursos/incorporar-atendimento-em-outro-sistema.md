# - Incorporar Atendimento em Outro Sistema

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/incorporar-atendimento-em-outro-sistema
- **Categoria:** Recursos
- **Menu:** Configurações › Integrações e segurança em Configurações › - Incorporar Atendimento em Outro Sistema

---

🧩 Sua equipe trabalha em outro sistema e precisa trocar de tela toda vez que vai responder um cliente? Com o **Token de Validação**, a tela de um atendimento aparece dentro do seu sistema, como uma janela aberta para aquela conversa, sem o operador precisar entrar na plataforma.

Essa janela se chama **iframe**: um pedaço de página que mostra outra página dentro dela. Para usar, basta montar um link e colar um código no seu sistema.

Ideal para:

☑️ **Atendimento no sistema da equipe:** mostra a conversa na mesma tela em que o operador já trabalha.

☑️ **Abertura direta pelo número do ticket:** leva àquela conversa sem passar pelas listas da plataforma.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**.
>
> ➡️ Em **Token de Validação (incorporar atendimento)**, clique em **GERAR** e copie o token.
>
> ➡️ Pegue o **número do ticket** no topo da conversa e o **ID do operador** no card dele, no menu **Equipe**.
>
> ➡️ Monte o link com esses dados e teste numa aba nova do navegador.
>
> ➡️ Deu certo? Cole o código do iframe na página do seu sistema.

## Como gerar o Token de Validação

Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**. Essa tela é do perfil **Administrador**.

🔘 **Token de Validação (incorporar atendimento):** é a senha que libera o link do atendimento. **Com o campo vazio, o recurso fica desligado** e todo link é recusado. Se a empresa não usa o atendimento incorporado, deixe o campo vazio. Para desligar um token que já existe, apague o campo: ao sair dele, a mudança já fica gravada.

🔘 **GERAR:** cria um token novo e já grava, sem botão de salvar. **O token anterior para de funcionar na hora**, e os links montados com ele passam a ser recusados.

⚠️ **Trate o Token de Validação como senha.** Com ele e o ID de um Administrador, qualquer pessoa abre os atendimentos da empresa e responde em nome desse operador. Se desconfiar que vazou, clique em **GERAR**.

## Como montar o link do atendimento

O link tem sempre este formato. Copie e troque as partes em MAIÚSCULAS:

```
https://{FRONTEND_URL}/embed/ticket/NUMERO_DO_TICKET?token=SEU_TOKEN&userId=ID_DO_OPERADOR
```

🔘 **Endereço do painel:** o começo do link, `{FRONTEND_URL}`, é o endereço em que você entra na plataforma. Se ele aparecer como `{FRONTEND_URL}`, troque pelo endereço que aparece na barra do navegador quando você está na plataforma.

🔘 **NUMERO_DO_TICKET:** o número entre parênteses no topo da conversa, ao lado do nome do contato. Em `Maria Silva (417) | #755`, o ticket é **417**. O `#755` é o protocolo, que é outro número. Se o nome aparecer cortado, feche o painel **Informações**. O código comprido do endereço da conversa no navegador, o que vem depois de `/tickets/`, também funciona no lugar do número.

🔘 **SEU_TOKEN:** o Token de Validação que você gerou.

🔘 **ID_DO_OPERADOR:** no menu **Equipe**, o card de cada pessoa mostra o **ID**. É com esse operador que a conversa abre, e o que for respondido ali fica em nome dele.

Exemplo preenchido, para o ticket 417 e o operador de ID 18:

```
https://{FRONTEND_URL}/embed/ticket/417?token=SEU_TOKEN&userId=18
```

Para testar, cole o link na barra de endereço de uma aba nova. A conversa abre sem pedir login, mesmo com a plataforma aberta em outra aba.

## Como colocar a conversa no seu sistema

Cole este código no HTML da página, no lugar em que a conversa deve aparecer, e troque o endereço pelo link que você montou:

```
<iframe allow="microphone; clipboard-write" src="https://{FRONTEND_URL}/embed/ticket/417?token=SEU_TOKEN&userId=18" width="100%" height="700" style="border:0"></iframe>
```

🔘 **width:** a largura da janela. `100%` ocupa todo o espaço disponível.

🔘 **height:** a altura da janela, em pixels. Com `700`, a conversa e a caixa de mensagem aparecem inteiras.

🔘 **allow:** libera o microfone para gravar áudio e a cópia de texto dentro da conversa. Sem ele, gravar áudio não funciona.

Quando a página é gerada por programação, este exemplo em PHP monta o mesmo código:

```php
<?php

$painel   = 'https://{FRONTEND_URL}';
$token    = 'SEU_TOKEN';
$ticket   = 417; // número do ticket
$operador = 18;  // ID do operador

$link = $painel . '/embed/ticket/' . $ticket . '?token=' . urlencode($token) . '&userId=' . $operador;

echo '<iframe allow="microphone; clipboard-write" src="' . htmlspecialchars($link) . '" width="100%" height="700" style="border:0"></iframe>';
```

⚠️ **O link leva o Token de Validação junto.** Quem vê o código da página vê o token. Use o iframe só em página protegida por login do seu sistema, nunca em site público.

## Do seu sistema até o link

O seu sistema conhece o cliente pelo telefone, não pelo número do ticket. Não é preciso ligar cada contato à mão: com a API da plataforma, o seu sistema acha o ticket pelo telefone, cria o que faltar e monta o link na hora, em até três comandos.

Os comandos usam o token de uma **Conexão** no lugar de `TOKEN_DA_CONEXAO`. Com o **Token da Empresa**, a busca pelo telefone pede também o campo `whatsappId`, com o ID da Conexão. O Token de Validação não funciona na API.

### Buscar os tickets pelo telefone

Troque o número do exemplo pelo telefone do cliente, com o código do país e o DDD, só os dígitos:

```
curl -X GET "https://api2.chatmasterveloz.com/api/contacts/alltickets" -H "Authorization: Bearer TOKEN_DA_CONEXAO" -H "Content-Type: application/json" -d '{"number":"5511999998888"}'
```

A resposta é a lista de tickets do contato. Em cada ticket, os campos que importam para o link:  
- `id` — o número do ticket, que vai no link.
- `whatsappId` — a Conexão do ticket.
- `status` — `pending` quando está aguardando, `open` em atendimento, `closed` encerrado.
- `queueId` — o Setor do ticket, vazio quando ele não está em nenhum Setor.

### Criar o contato, se a busca não achou

```
curl -X POST "https://api2.chatmasterveloz.com/api/contacts" -H "Authorization: Bearer TOKEN_DA_CONEXAO" -H "Content-Type: application/json" -d '{"name":"Maria Silva","number":"5511999998888"}'
```

A resposta traz o `id` do contato novo. Se o telefone já estiver cadastrado, o contato não é duplicado: a resposta traz `alreadyExists` e, em `existingContact`, o contato que já existia, com o `id` dele.

### Abrir o ticket, se o contato ainda não tem

Troque `123` pelo `id` do contato:

```
curl -X POST "https://api2.chatmasterveloz.com/api/tickets/createTicketAPI" -H "Authorization: Bearer TOKEN_DA_CONEXAO" -H "Content-Type: application/json" -d '{"contactId":123}'
```

A resposta traz o ticket, e o número dele vem no campo `id`. Abrir o ticket pela API não envia nenhuma mensagem ao cliente.

Com o número do ticket e o ID do operador, o seu sistema monta o link no formato `https://{FRONTEND_URL}/embed/ticket/NUMERO_DO_TICKET?token=SEU_TOKEN&userId=ID_DO_OPERADOR`.

### Outros jeitos de pegar os números

➡️ **Pelos webhooks:** quando o seu sistema já recebe os webhooks da Conexão ou do Setor, o número do ticket vem no campo `ticketData.id`, sem precisar buscar pelo telefone.

➡️ **ID do operador:** o comando abaixo lista a equipe com o `id` de cada pessoa. Troque `TOKEN_DA_API` pelo token de uma Conexão ou pelo Token da Empresa.

```
curl "https://api2.chatmasterveloz.com/api/company/users" -H "Authorization: Bearer TOKEN_DA_API"
```

### Cuidados ao buscar e criar pela API

➡️ **Telefone com os mesmos dígitos do cadastro:** a busca só acha o contato quando o telefone tem os mesmos dígitos gravados na plataforma. Se a resposta voltar com o erro `ERR_NO_CONTACT_FOUND`, tente o número com e sem o 9 depois do DDD.

➡️ **Mais de um ticket por contato:** o contato pode ter tickets em várias Conexões, e mais de um na mesma. Escolha pelo `whatsappId` o ticket da Conexão em que a sua equipe atende.

➡️ **Ticket aberto pela API fica sem Setor:** o Administrador e o Supervisor abrem o link na hora. O operador de perfil **Usuário** só abre depois que o ticket é colocado num Setor dele.

➡️ **Abrir o ticket de novo devolve o mesmo:** repetir o comando de abrir o ticket não cria outro. Se o ticket estiver encerrado, ele continua encerrado e sem Setor, por isso só Administrador e Supervisor abrem o link.

⚠️ **Faça essas chamadas no servidor do seu sistema, nunca no navegador.** Com o token da Conexão, qualquer pessoa lê os atendimentos e envia mensagens por ela. No código de uma página, o token fica à vista de quem abrir.

## O que o operador vê no atendimento incorporado

A tela mostra só aquela conversa, com a caixa de mensagem e as ações do topo do atendimento, sem o menu lateral e sem as listas da plataforma.

➡️ **Ticket aguardando:** clique em **ACEITAR** para liberar a caixa de mensagem. O ticket passa a ser do operador do link.

➡️ **Mensagens novas:** aparecem na hora, sem recarregar a página.

➡️ **Respostas:** são enviadas e registradas em nome do operador do link.

➡️ **Tela aberta por horas seguidas:** o acesso se renova sozinho na hora de responder, sem recarregar a página.

## Quem consegue abrir cada ticket

O link respeita o perfil e os Setores do operador informado nele:

➡️ **Administrador e Supervisor:** abrem qualquer ticket da empresa.

➡️ **Usuário:** abre os tickets dos Setores dele, mesmo os que estão com outro operador.

➡️ **Usuário convidado para a conversa:** abre aquele ticket, mesmo sem ser do Setor.

➡️ **Ticket encerrado:** fica sem Setor, por isso só Administrador e Supervisor abrem.

## Quando o seu sistema precisa do painel inteiro

O **Token de Validação** abre a tela de um atendimento e nada além dela. Quando o seu sistema precisa abrir o painel inteiro já logado, com as listas, os menus e as permissões da pessoa, o caminho é o **Login automático**, no menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**, bloco **Login automático (integrações e iframes)**.

Com o **Login automático** ligado, o servidor do seu sistema pede à plataforma, com o **Token da Empresa**, um link de uso único para a pessoa que vai entrar, e abre esse link, também dentro de um iframe. O link vale uma vez só e expira em 60 segundos, ou em até 5 minutos se o pedido escolher. A pessoa entra com o status que já tinha, ou com o que o pedido escolher: **Online**, **Ausente** ou **Offline**.

O pedido do link leva o e-mail de quem vai entrar. No lugar de `TOKEN_DA_EMPRESA` vai o **Token da Empresa**, gerado no menu **Configurações  ›  Token da Empresa**:

```
curl -X POST "https://api2.chatmasterveloz.com/api/login-automatico" -H "Authorization: Bearer TOKEN_DA_EMPRESA" -H "Content-Type: application/json" -d '{"email":"atendente@empresa.com","destino":"/tickets"}'
```

A resposta traz o link no campo `url`. Use esse link como `src` do iframe, no lugar do link do atendimento, antes que ele vença. No lugar do `email` vale o `userId`, com o **ID** do card da pessoa no menu **Equipe**. O `destino` é a tela em que a pessoa chega; sem ele, ela chega à **Página inicial após o login** escolhida no cadastro dela, ou aos **Chats** quando não há uma escolhida.

⚠️ **Peça o link no servidor do seu sistema, nunca no navegador.** O Token da Empresa dá acesso à empresa inteira, e no código de uma página ele fica à vista de quem abrir.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Token de Validação é o mesmo Token da Empresa?** Não. O **Token de Validação** só abre o link do atendimento e não funciona na API. Para a API, use o **Token da Empresa** ou o token de uma Conexão.
>
> **Qual a diferença entre o Token de Validação e o Login automático?** O **Token de Validação** abre só a tela de um atendimento, com o operador informado no link. O **Login automático** abre o painel inteiro já logado, com as permissões da pessoa que entra, por um link que o seu sistema pede à plataforma com o **Token da Empresa**.
>
> **O operador precisa entrar na plataforma para abrir o link do atendimento?** Não. O link já abre a conversa com o operador informado nele.
>
> **O operador pode deixar a plataforma aberta no mesmo navegador do sistema com o iframe?** Pode. A conversa abre dentro do iframe e a sessão da plataforma continua como estava.
>
> **Um link serve para todos os tickets?** Não. Cada link aponta para um ticket e um operador. Para abrir outro atendimento, troque o número do ticket no link.
>
> **Preciso cadastrar à mão o número do ticket de cada contato do meu sistema?** Não. O seu sistema busca o ticket pelo telefone do contato com a API, cria o contato e o ticket quando faltam e monta o link do atendimento na hora.
>
> **Gerar outro Token de Validação derruba os links que já montei?** Sim. Todo link com o token antigo passa a ser recusado. Troque o token nos links e no seu sistema.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Link incompleto:** aparece *"Link incompleto: falta o token de validação ou o usuário."*. Falta o `token` ou o `userId` no link. **Solução:** confira se o link tem os dois, no formato do exemplo.
>
> **Token inválido:** aparece *"Token de validação inválido ou recurso desativado para esta empresa."*. O token do link está errado, foi trocado por um novo ou o campo está vazio. **Solução:** acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**, copie o token atual e atualize o link.
>
> **Atendimento não encontrado:** aparece *"Atendimento não encontrado para esta empresa."*. O número não é de um ticket desta empresa. **Solução:** confira se você não usou o protocolo, que é o número com `#`, no lugar do número entre parênteses.
>
> **Usuário inválido:** aparece *"Usuário inválido ou inativo."*. O ID não existe ou a pessoa está inativa. **Solução:** confira o **ID** no card da pessoa, no menu **Equipe**.
>
> **Operador sem Setor:** a tela diz que a pessoa *"não está em nenhum setor"*. **Solução:** no menu **Equipe**, edite o operador e inclua o Setor do ticket na aba **Setores e Conexões**, ou monte o link com o ID de um Administrador.
>
> **Operador de outro Setor:** a tela diz que a pessoa *"não participa do setor"* do ticket. **Solução:** no menu **Equipe**, inclua esse Setor no operador, ou monte o link com o ID de quem atende esse Setor.
>
> **Ticket sem Setor:** aparece *"Este atendimento não está em nenhum setor."*. O ticket não tem Setor ou já foi encerrado. **Solução:** coloque o ticket em um Setor do operador, ou monte o link com o ID de um Administrador ou Supervisor.
