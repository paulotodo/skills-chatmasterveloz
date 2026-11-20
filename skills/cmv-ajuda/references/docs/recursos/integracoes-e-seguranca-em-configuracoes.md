# Integrações e segurança em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/integracoes-e-seguranca-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Integrações e segurança em Configurações

---

🧩 Seu sistema precisa saber na hora quando algo acontece no atendimento? Os arquivos das conversas precisam ficar guardados num armazenamento da sua empresa? E o login da equipe precisa de uma segunda verificação?

A aba **Integrações e segurança** liga a empresa a serviços de fora e protege o acesso: os webhooks que avisam outros sistemas, o armazenamento dos arquivos, a segurança do login, do atendimento aberto em outro sistema e do painel que outro sistema abre já logado, e os logs. A aba é dividida em seções por assunto, e esta parte da documentação segue a mesma divisão.

Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**.

## O que decidir antes de mexer

➡️ **Quem recebe os avisos.** Cada webhook é um endereço do seu sistema que recebe os eventos de um assunto.

➡️ **Onde os arquivos ficam.** No armazenamento da plataforma ou num bucket da sua empresa.

➡️ **Como o acesso é protegido.** Por onde se recupera a senha, se a equipe pode usar a autenticação em dois fatores, se o atendimento pode abrir dentro de outro sistema e se outro sistema pode abrir o painel já logado.

➡️ **O que fica registrado.** Os logs que ajudam a entender o que aconteceu num atendimento.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preencher o Armazenamento Remoto de Arquivos leva os arquivos antigos para o bucket?** Não. A própria tela avisa que trocar não copia os arquivos já guardados.
>
> **Habilitar o 2FA na empresa obriga a equipe a usar?** Não. Habilitar libera a autenticação em dois fatores para os usuários, e cada um configura a sua.
