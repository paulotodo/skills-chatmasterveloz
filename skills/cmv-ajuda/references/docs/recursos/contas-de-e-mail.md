# Contas de E-mail

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/contas-de-e-mail
- **Categoria:** Recursos
- **Menu:** E-mails › Contas de E-mail

---

🧩 No menu **Contas de E-mail** o administrador liga as caixas de e-mail da empresa à plataforma. Cada conta de e-mail é uma caixa do servidor: a plataforma recebe as mensagens por **IMAP** e envia por **SMTP**, com o usuário e a senha da própria caixa.

Depois de cadastrada, a conta de e-mail é usada no menu **E-mails** por quem a cadastrou e pelas pessoas escolhidas em **Usuários vinculados**.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Contas de E-mail** e clique em **Adicionar conta**.
>
> ➡️ Escolha o **Provedor (modelo)** e preencha **Nome**, **E-mail**, **Usuário** e **Senha**.
>
> ➡️ Clique em **Testar conexão** e confira se **IMAP** e **SMTP** deram **OK**.
>
> ➡️ Escolha os **Usuários vinculados** e clique em **Adicionar**.

## A lista de contas de e-mail

🔘 Cada linha mostra o **Nome**, o **E-mail**, o servidor de **IMAP** e o de **SMTP** (com **(SSL)** quando ligado), os **Usuários** vinculados e o **Status**: **Ativa** ou **Inativa**.

🔘 **Restrita**, no **Status**, marca a conta de e-mail cadastrada por outro administrador em que você não está vinculado: você vê a linha, mas não usa a conta no menu **E-mails**.

🔘 Em **Ações** ficam **Editar** e **Excluir**, nas contas de e-mail que você cadastrou: enquanto quem cadastrou for administrador, só ele altera e exclui a conta. Na conta de outro administrador, a linha aparece sem os dois botões, mesmo que você esteja vinculado a ela. Se quem cadastrou deixar de ser administrador ou for excluído da equipe, os dois botões passam a aparecer para todos os administradores.

## Como cadastrar uma conta de e-mail

Acesse o menu **Contas de E-mail  ›  Adicionar conta**

🔘 **Provedor (modelo):** preenche o host, a porta e o **SSL/TLS** de IMAP e de SMTP dos provedores mais comuns e mostra a dica daquele provedor. Depois da escolha o campo volta a ficar em branco: o que vale é o que ele preencheu nos campos abaixo. Aparece só ao cadastrar.                                              

| Provedor | O que a dica pede |
|---|---|
| Gmail | verificação em 2 etapas e uma senha de aplicativo no campo **Senha** |
| Outlook / Hotmail / Live | senha de aplicativo, se a verificação em 2 etapas estiver ativa |
| Microsoft 365 / Office 365 | IMAP ativado nas configurações da Exchange; com MFA, senha de aplicativo |
| Yahoo Mail | senha de aplicativo, gerada nas configurações da conta |
| iCloud Mail | senha de aplicativo, gerada em appleid.apple.com |
| Zoho Mail | IMAP ativado em Configurações › Mail Accounts; pode exigir senha de aplicativo |
| UOL Host e Locaweb | conferir com o provedor se IMAP e SMTP estão habilitados na conta |
| Hostinger / cPanel | trocar os dois hosts pelo `mail.` do seu domínio e usar o e-mail completo como usuário |
| Custom (preencher manualmente) | preencher host, porta e SSL/TLS à mão |

🔘 **Nome:** como a conta de e-mail aparece na lista e na coluna **Contas** do menu **E-mails**, como *Comercial* ou *Suporte*.

🔘 **E-mail:** o endereço da caixa.

🔘 **Host IMAP**, **Porta IMAP** e **SSL/TLS:** o servidor de onde a plataforma busca as mensagens.

🔘 **Host SMTP**, **Porta SMTP** e **SSL/TLS:** o servidor pelo qual as mensagens são enviadas.

🔘 **Usuário** e **Senha:** o acesso da própria caixa. Muitos provedores pedem uma **senha de aplicativo** no lugar da senha de entrar no site, e a dica do **Provedor (modelo)** avisa quando.

🔘 **Usuários vinculados:** as pessoas da equipe que usam a conta de e-mail no menu **E-mails**. Quem cadastra a conta não precisa se incluir: ele usa a conta enquanto for administrador.

🔘 **Assinatura:** o texto que entra no fim de todo e-mail enviado pela conta: os novos, as respostas e os encaminhamentos. Aceita HTML; o botão **Inserir imagem** acrescenta uma imagem, como o logotipo, e a **Prévia** mostra o resultado.

🔘 **Pastas sincronizadas** e **Endereços aceitos:** servem para a caixa usada por mais de uma equipe. As pastas aparecem só ao editar uma conta de e-mail já cadastrada.

🔘 **Sincronização ativa:** ligada, a conta de e-mail busca as mensagens novas sozinha. Desligada, a conta para de buscar mensagens novas e continua enviando; ao religar, as que chegaram nesse meio-tempo aparecem. Para desligar, não é preciso redigitar a senha.

🔘 **Conta ativa:** desligada, a conta de e-mail aparece como **Inativa** na lista e para de receber e de enviar: **Nova mensagem** e **Sincronizar agora** ficam desativados no menu **E-mails**. Ao religar, as mensagens que chegaram nesse meio-tempo aparecem.

⚠️ **Nome**, **E-mail**, **Host IMAP**, **Host SMTP**, **Usuário** e **Senha** são obrigatórios. Sem um deles, a tela avisa *"Preencha os campos obrigatórios"* e não salva.

⚠️ O plano da empresa define quantas contas de e-mail ela pode ter. No limite, a plataforma recusa a conta nova com *"Limite de conexões de E-mail alcançado: 2 de 2."*. Só as contas de e-mail ativas entram no limite: a conta **Inativa** não ocupa vaga.

Logo depois de cadastrada, a conta de e-mail traz para o menu **E-mails** as 30 últimas mensagens que chegaram à **Caixa de entrada**. As anteriores continuam no servidor de e-mail, e o botão **Buscar anteriores no servidor**, no fim da lista do menu **E-mails**, traz as que ainda não estão na plataforma, de 50 em 50, inclusive as que faltam no meio da lista.

## Testar conexão

🔘 **Testar conexão** confere o IMAP e o SMTP com os dados preenchidos e mostra o resultado de cada um acima dos botões: **OK**, ou **ERRO** seguido do motivo.

⚠️ O teste não é exigido para salvar: uma conta de e-mail com dados errados é salva do mesmo jeito. Clique em **Testar conexão** antes de **Adicionar** e só salve com IMAP e SMTP em **OK**.

## Editar e excluir

🔘 **Editar** abre a mesma janela, sem o **Provedor (modelo)**. A senha vira **Nova senha (opcional)**: em branco, a senha salva continua valendo.

🔘 **Excluir** pede confirmação, *"Confirma a exclusão da conta … ? Essa ação não pode ser desfeita."*, e com **OK** a conta de e-mail some da lista. Excluir a conta tira a caixa da plataforma, mas não apaga nada no servidor de e-mail: as mensagens continuam na caixa.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O Testar conexão deu ERRO no IMAP ou no SMTP.** Confira o host, a porta e o **SSL/TLS** daquele lado, e depois o **Usuário** e a **Senha**. No Gmail, no Yahoo, no iCloud e nas contas com verificação em 2 etapas, a senha certa é a **senha de aplicativo**, não a de entrar no site.
>
> **Na hospedagem com cPanel, posso usar o endereço do servidor em vez do mail. do meu domínio?** Pode. O endereço do servidor que a hospedagem informa nas configurações de e-mail funciona em **Host IMAP** e **Host SMTP**, com o e-mail completo em **Usuário**. Confira com **Testar conexão**.
>
> **Preciso me incluir em Usuários vinculados para usar a conta de e-mail que cadastrei?** Não. Quem cadastra a conta de e-mail usa a conta enquanto for administrador; **Usuários vinculados** é para as outras pessoas.
>
> **Outro administrador pode alterar a conta de e-mail que eu cadastrei?** Enquanto você for administrador, não: só quem cadastrou altera e exclui a conta de e-mail. Para o administrador que não está em **Usuários vinculados**, ela aparece com o selo **Restrita**; vinculado, ele usa a conta no menu **E-mails**, mas continua sem **Editar** e **Excluir**. Se você deixar de ser administrador ou for excluído da equipe, a conta de e-mail continua funcionando para quem está vinculado, e qualquer administrador passa a alterá-la e excluí-la.
>
> **Quem cadastrou a conta de e-mail deixou de ser administrador. O que muda?** Ele perde a conta na hora, e os outros administradores passam a ter **Editar** e **Excluir**. As pessoas em **Usuários vinculados** continuam usando a conta. Se ele voltar a ser administrador, recupera os dois botões, e os outros administradores voltam a ficar sem eles.
>
> **Qual a diferença entre desligar a Sincronização ativa e a Conta ativa?** Com a **Sincronização ativa** desligada, a conta de e-mail para de buscar mensagens novas e continua enviando. Com a **Conta ativa** desligada, ela para de buscar e de enviar. Nos dois casos, religar traz as mensagens que chegaram nesse meio-tempo.
>
> **Desativar uma conta de e-mail libera vaga no limite do plano?** Libera. Só as contas de e-mail ativas contam no limite do plano: com a **Conta ativa** desligada, a conta fica **Inativa** e não ocupa vaga.
>
> **Troquei a senha da caixa de e-mail. O que mudo na plataforma?** Edite a conta no menu **Contas de E-mail** e preencha **Nova senha (opcional)** com a senha nova. Em branco, a plataforma continua com a senha antiga e, depois de alguns minutos sem conseguir entrar, a conta de e-mail fica **Inativa**.
>
> **Excluir a conta de e-mail apaga os e-mails da caixa?** Não. Excluir a conta no menu **Contas de E-mail** só tira a caixa da plataforma; as mensagens continuam no servidor de e-mail, e a caixa pode ser cadastrada de novo.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Preencha os campos obrigatórios:** a conta de e-mail não salva. **Solução:** preencha **Nome**, **E-mail**, **Host IMAP**, **Host SMTP**, **Usuário** e **Senha**.
>
> **A conta de e-mail ficou Inativa sozinha:** a caixa recusou a senha, por exemplo porque ela foi trocada no provedor, e depois de alguns minutos sem conseguir entrar a plataforma desativa a conta. **Solução:** no menu **Contas de E-mail**, clique em **Editar**, preencha **Nova senha (opcional)** com a senha atual, clique em **Testar conexão**, ligue **Conta ativa** e clique em **Atualizar**.
