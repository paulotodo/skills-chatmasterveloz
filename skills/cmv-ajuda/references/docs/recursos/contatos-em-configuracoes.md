# Contatos em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/contatos-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Contatos em Configurações

---

🧩 A aba **Contatos** reúne o que a empresa decide sobre os contatos: quem pode compartilhar, importar e exportar, se o número é validado no cadastro, os campos extras da ficha e a **carteira de clientes**, o modelo em que cada contato tem um atendente responsável.

A aba tem duas seções, **Contatos** e **Carteiras de Clientes**, e este artigo segue as duas na ordem da tela.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Contatos**.
>
> ➡️ Na seção **Contatos**, ajuste o compartilhamento, a importação e a exportação, a validação e os campos adicionais.
>
> ➡️ Na seção **Carteiras de Clientes**, escolha **Sim** em **Carteira de Clientes** para ligar o modelo.

## Contatos

Acesse o menu **Configurações  ›  Opções  ›  Contatos**, seção **Contatos**.

🔘 **Compartilhar todos os contatos:** ligado, qualquer atendente pode enviar o cartão de qualquer contato da empresa, sem precisar marcar um a um. Desligado, valem só os contatos marcados como compartilhados.

🔘 **Operador Importa / Exporta Contatos?:** em **Não**, o atendente perde os botões de importar e exportar da tela de **Contatos**. É a opção que impede alguém de levar a lista inteira de clientes embora num arquivo. Ela tira **os botões**, não o acesso à área: quem decide se a pessoa entra em **Contatos** é o campo **Acesso a Contatos** do cadastro dela, no menu **Equipe  ›  editar o usuário**.

🔘 **Ignorar Validação de Contatos?:** com **Sim**, a plataforma deixa de validar o número ao cadastrar um contato.

🔘 **Campos Adicionais do Contato (JSON):** a definição dos campos extras da ficha do contato, escrita em JSON. Os campos definidos aqui passam a aparecer no cadastro de todo contato.

⚠️ O texto de **Campos Adicionais do Contato (JSON)** é código: um caractere fora do lugar invalida a definição inteira e os campos somem da ficha. Altere com cuidado e confira a ficha de um contato depois.

## Carteiras de Clientes

Acesse o menu **Configurações  ›  Opções  ›  Contatos**, seção **Carteiras de Clientes**. A carteira liga cada contato a um atendente responsável e define o que o atendente pode fazer com contatos que não são da carteira dele.

🔘 **Carteira de Clientes:** liga ou desliga o vínculo entre contato e atendente responsável.

🔘 **Operador Pode Alterar Carteiras?:** com **Sim**, o próprio atendente muda de quem é o contato; com **Não**, só administrador e supervisor.

🔘 **Operador Pode Iniciar Chats com Leads sem Carteira Definida?:** com **Não**, contato sem responsável fica fora do alcance do atendente até alguém definir a carteira.

⚠️ Com **Carteira de Clientes** ligada e **Operador Pode Iniciar Chats com Leads sem Carteira Definida?** em **Não**, um contato novo pode ficar sem ninguém podendo abrir conversa com ele. Defina quem cuida dos contatos sem dono antes de ligar.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Um atendente não consegue enviar o cartão de um contato.** Ou **Compartilhar todos os contatos** está desligado e aquele contato não foi marcado como compartilhado, ou o atendente não tem acesso a Contatos no cadastro dele.
>
> **Desliguei "Operador Importa / Exporta Contatos?" e o atendente ainda entra em Contatos. Está errado?** Não. Essa opção remove os botões de importar e exportar, não o acesso à área. Quem controla a entrada em **Contatos** é o campo **Acesso a Contatos** no cadastro do usuário, no menu **Equipe  ›  editar o usuário**.
>
> **Um atendente não consegue abrir conversa com um contato.** Confira se o contato tem carteira e se **Operador Pode Iniciar Chats com Leads sem Carteira Definida?** está em **Não**.
