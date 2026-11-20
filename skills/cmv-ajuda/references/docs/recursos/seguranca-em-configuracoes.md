# Segurança em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/seguranca-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Integrações e segurança em Configurações › Segurança em Configurações

---

🧩 A seção **Segurança** reúne o que controla o acesso à empresa: por onde o usuário recebe o código quando esquece a senha, a liberação da autenticação em dois fatores (2FA) no login, o token que permite incorporar a tela de um atendimento em outro sistema e o **Login automático**, que deixa outro sistema abrir o painel já logado.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**.
>
> ➡️ Em **Modo de Recuperação de Senha**, escolha por onde o código chega.
>
> ➡️ Escolha **Sim** em **Habilitar 2FA na empresa** para liberar a autenticação em dois fatores.
>
> ➡️ Para outro sistema abrir o painel já logado, ligue **Ligar o login automático**, no bloco **Login automático (integrações e iframes)**.

## Os campos, na ordem da tela

🔘 **Modo de Recuperação de Senha:** por onde o usuário recebe o código ao esquecer a senha — **Somente E-Mail**, **Somente WhatsApp** ou **E-Mail & WhatsApp**. Para WhatsApp, precisa de uma Conexão marcada como **Padrão**.

🔘 **Habilitar 2FA na empresa:** quando habilitado, os usuários **poderão** configurar a autenticação em dois fatores nas contas deles. Habilitar aqui libera a opção — não obriga ninguém.

⚠️ **Habilitar 2FA na empresa** não ativa o 2FA de ninguém sozinha. Cada usuário configura o próprio, depois que a empresa liberou.

🔘 **Token de Validação (incorporar atendimento):** com um token preenchido, a tela de um atendimento pode ser incorporada em outro sistema por iframe, no endereço `/embed/ticket/{id}?token=SEU_TOKEN&userId=ID_DO_OPERADOR`. No lugar de `{id}` vai o número do ticket, e no lugar de `ID_DO_OPERADOR`, o **ID** que aparece no card da pessoa, no menu **Equipe**. Com o campo vazio, o recurso fica desligado. Para desligar um token que já existe, apague o campo: ao sair dele, a mudança já fica gravada.

O botão **GERAR**, junto do campo, cria um token novo e já grava, sem botão de salvar. **O token anterior para de funcionar na hora**, e todo link montado com ele passa a ser recusado.

⚠️ **Trate o Token de Validação como senha:** ele dá acesso às conversas da empresa. Se desconfiar que vazou, clique em **GERAR**.

## Login automático (integrações e iframes)

O bloco **Login automático (integrações e iframes)** fica no fim da seção **Segurança**. Ele deixa outro sistema abrir o painel já logado com uma pessoa da equipe, inclusive dentro de um iframe, a janela que mostra uma página dentro de outra. Nas palavras da tela: *"Quem entra vê o painel inteiro, com as permissões dele, e passa pelas mesmas regras do login (horário, IP, conta ativa), sem senha e sem o código de duas etapas."*

🔘 **Ligar o login automático:** liga o recurso para a empresa. Desligado, a plataforma recusa todo pedido de link. Cada mudança grava na hora, e a tela avisa *"Login automático atualizado."*

### Link de uso único

O **link de uso único** é o jeito que a própria tela recomenda. O servidor do outro sistema pede o link à plataforma, com o **Token da Empresa**, e abre o endereço recebido. O link do login automático vale uma vez só e expira em 60 segundos; a validade pode ir de 10 segundos a 5 minutos.

O exemplo que aparece na tela, com `TOKEN_DA_EMPRESA` no lugar do **Token da Empresa**:

```
curl -X POST "https://api2.chatmasterveloz.com/api/login-automatico" -H "Authorization: Bearer TOKEN_DA_EMPRESA" -H "Content-Type: application/json" -d '{"email": "atendente@empresa.com", "destino": "/tickets"}'
```

No pedido do link, o outro sistema informa:  
- `email` ou `userId` — quem entra. Pessoa inativa, ou que não é desta empresa, não entra.
- `destino` — a tela de chegada, como `/tickets`. Um endereço de fora da plataforma abre a tela inicial da pessoa.
- `validadeSegundos` — a validade do link, de 10 a 300 segundos.
- `status` — o status de entrada: `online`, `away` (Ausente) ou `offline`. Sem ele, a pessoa entra com o status que já tinha.

Ao abrir o link, a tela mostra *"Entrando no painel…"* e leva ao destino. Aberto de novo, ou depois da validade, o link mostra *"Este link de acesso venceu ou já foi usado. Peça um novo na plataforma de origem."*

⚠️ **Peça o link do login automático no servidor do outro sistema, nunca no navegador.** O **Token da Empresa** dá acesso à empresa inteira, e no código de uma página ele fica à vista de quem abrir.

### Link fixo

🔘 **Permitir também o link fixo (chave + e-mail):** libera um link que não vence, montado com a chave da empresa e o e-mail da pessoa. A tela mostra o modelo:

```
https://{FRONTEND_URL}/login-automatico#chave=CHAVE&email=EMAIL_DO_USUARIO&destino=/tickets&status=offline
```

Troque `CHAVE` pela chave e `EMAIL_DO_USUARIO` pelo e-mail de quem entra. O começo do link, `{FRONTEND_URL}`, é o endereço em que você entra na plataforma; se ele aparecer como `{FRONTEND_URL}`, troque pelo endereço que aparece na barra do navegador quando você está na plataforma. O `status` do fim é opcional: sem ele, a pessoa entra com o status que já tinha.

🔘 **COPIAR A CHAVE:** copia a chave do link fixo. A tela avisa *"Chave copiada."*

🔘 **TROCAR A CHAVE:** cria uma chave nova. Nas palavras da tela, *"Chave trocada. Os links com a chave antiga deixaram de entrar."*

Com a chave errada, ou com um e-mail que não é de ninguém da empresa, o link fixo mostra *"Este link de acesso não é válido. Confira a chave e o e-mail."*

⚠️ Nas palavras da tela: *"Atenção: quem vir o link fixo entra no painel daquele usuário. Use só se a plataforma não consegue pedir o link de uso único, e troque a chave se ela vazar."*

### Status de quem entra

Pelo login automático, a pessoa entra com o status que já tinha: quem estava **Offline** continua **Offline**, e quem estava **Online** continua **Online**. Para escolher, o pedido do link de uso único leva o campo `status`, e o link fixo, o `&status=` no fim do endereço, com `online`, `away` (**Ausente**) ou `offline`. Como avisa a tela de login, *"Ausente e Offline não recebem atendimentos do rodízio."*

### Dentro de um iframe

O link do login automático também abre dentro de um iframe, na página do outro sistema: a pessoa entra já logada, com o painel inteiro dentro da janela.

```
<iframe src="LINK_DO_LOGIN_AUTOMATICO" width="100%" height="800" style="border:0"></iframe>
```

No lugar de `LINK_DO_LOGIN_AUTOMATICO` vai o endereço que a plataforma devolveu no pedido, ou o link fixo. Depois de entrar, o painel continua logado naquele navegador, também aberto fora do iframe, como num login normal.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Habilitei o 2FA na empresa e o login continuou só com senha.** É o esperado: habilitar libera a opção para cada usuário configurar. Enquanto o usuário não configurar o dele, o login segue como antes.
>
> **Onde escolho se o código de recuperação de senha vai por e-mail ou WhatsApp?** Em **Modo de Recuperação de Senha**, nesta seção. Para WhatsApp, marque uma Conexão como **Padrão** no menu **Conexões**.
>
> **O Token de Validação é o mesmo Token da Empresa?** Não. O **Token de Validação** só abre o link do atendimento e não funciona na API. Para a API, use o **Token da Empresa** ou o token de uma Conexão.
>
> **Qual a diferença entre o Token de Validação e o Login automático?** O **Token de Validação** abre só a tela de um atendimento, com o operador informado no link. O **Login automático** abre o painel inteiro já logado, com as permissões da pessoa que entra.
>
> **Entrar pelo Login automático deixa a pessoa Online?** Só se o link pedir. Sem o `status`, a pessoa entra com o status que já tinha; com ele, entra **Online**, **Ausente** ou **Offline**.
>
> **Recarreguei a página do meu sistema e o Login automático mostrou que o link venceu.** É o esperado no link de uso único: ele vale uma vez só. A página do seu sistema precisa pedir um link novo cada vez que abre o painel.
>
> **Entrar pelo Login automático pede a senha ou o código de duas etapas?** Não. Nas palavras da tela, quem entra passa pelas mesmas regras do login *"sem senha e sem o código de duas etapas"*.

> **[ERROS]**
>
> #### Erros Comuns
>
> **"Este link de acesso venceu ou já foi usado":** o link de uso único do Login automático foi aberto pela segunda vez, ou depois da validade. **Solução:** peça um link novo à plataforma a cada entrada e abra logo depois de receber.
>
> **"Este link de acesso não é válido. Confira a chave e o e-mail.":** o link fixo do Login automático tem a chave antiga ou errada, ou o e-mail não é de ninguém da empresa. **Solução:** no bloco **Login automático (integrações e iframes)**, clique em **COPIAR A CHAVE**, monte o link de novo e confira o e-mail da pessoa.
