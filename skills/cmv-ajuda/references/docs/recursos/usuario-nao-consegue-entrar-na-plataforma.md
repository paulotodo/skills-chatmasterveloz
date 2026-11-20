# Usuário Não Consegue Entrar na Plataforma

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/usuario-nao-consegue-entrar-na-plataforma
- **Categoria:** Recursos
- **Menu:** Equipe › Usuário Não Consegue Entrar na Plataforma

---

🧩 A pessoa digita e-mail e senha e a plataforma não deixa entrar? Na maioria das vezes não é a senha: é uma regra do cadastro dela — conta inativada, endereço de rede fora da lista ou horário fora do expediente. A mensagem que aparece na tela de login diz qual é, e o **Registro de Atividades** guarda o motivo de cada tentativa barrada.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Pergunte à pessoa qual mensagem aparece ao tentar entrar.
>
> ➡️ Ache a mensagem abaixo e corrija o que ela indica no cadastro da pessoa, no menu **Equipe**.
>
> ➡️ Sem a mensagem, filtre a pessoa no menu **Registro de Atividades** e leia o **Motivo** da tentativa recusada.

## O que cada mensagem quer dizer

🔘 *Erro de autenticação. Por favor verifique seu EMAIL e SENHA e tente novamente.* — o e-mail ou a senha não conferem. **Solução:** use **Trocar Senha** no card da pessoa para definir uma nova, ou peça que ela use **Recuperar Senha** na tela de login.

🔘 *Sua conta está inativa. Procure o administrador para reativá-la.* — o cadastro está com **Inativar Usuário** em **SIM**, e o card dela mostra **Inativo**. **Solução:** edite a pessoa, aba **Permissões**, e volte **Inativar Usuário** para **NÃO**.

🔘 *Acesso negado. Seu IP não está autorizado para este usuário.* — a pessoa tem **Restrição por IP (CIDR)** e está tentando entrar de outro endereço, como de casa ou do celular fora da rede do escritório. **Solução:** na aba **Permissões**, inclua o endereço ou a faixa de onde ela vai entrar, ou deixe o campo em branco para liberar de qualquer lugar.

🔘 *Acesso fora do horário permitido!* — a hora atual está fora do **Horário de Trabalho** dela naquele dia da semana, ou o dia está como folga (**00:00 às 00:00**). Com o dia dividido em mais de uma faixa, ela entra dentro de qualquer uma. **Solução:** na aba **Geral**, ajuste o horário daquele dia, use o **+** para acrescentar uma faixa, ou deixe o dia em branco — dia em branco não bloqueia. Essa regra vale para o perfil **User**: administrador e supervisor entram fora do horário.

## Como achar o motivo no Registro de Atividades

Acesse o menu **Registro de Atividades** e escolha a pessoa no filtro **Usuário**. Cada tentativa barrada por uma regra aparece com o **Motivo** — **Conta desativada**, **IP fora da lista permitida** ou **Fora do horário de trabalho** — e entra na contagem de **Ações Bloqueadas**, no topo. Senha errada aparece com o motivo **Senha inválida** e não conta como bloqueio.

⚠️ Tentativa com um e-mail que não existe na plataforma não gera registro. Se a pessoa não aparece no filtro, confira se ela está digitando o e-mail do cadastro.

## Quem já está dentro

➡️ **Inativar Usuário** com a pessoa na plataforma não a tira na hora: ela continua na tela até mudar de página, e aí cai no login. Para tirar na hora, use **Derrubar sessão**, em **Status e sessão**, no card dela.

➡️ **Uma sessão por pessoa:** entrar com o mesmo e-mail em outro navegador encerra a sessão que estava aberta, em poucos segundos.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A pessoa entrava ontem e hoje não entra.** Veja o horário de hoje: cada dia da semana tem o seu no **Horário de Trabalho**, e **00:00 às 00:00** é folga. Se ela mudou de lugar, veja também a **Restrição por IP (CIDR)**.
>
> **Inativei a pessoa por engano. Perdi alguma coisa?** Não. **Inativar Usuário** só impede a entrada; o cadastro e as conversas dela continuam. Volte para **NÃO** e ela entra de novo.
>
> **Só um atendente não consegue entrar, os outros sim.** A regra é do cadastro dele: confira a aba **Geral** (horário) e a aba **Permissões** (inativação e IP).
>
> **Entrei em outro computador e o primeiro saiu da plataforma.** É o esperado: cada pessoa tem uma sessão por vez, e entrar de novo encerra a anterior. Para usar em dois lugares, cada um precisa do próprio usuário.
>
> **Como libero a pessoa para entrar de qualquer lugar e a qualquer hora?** Deixe em branco a **Restrição por IP (CIDR)** e os dias do **Horário de Trabalho**.
