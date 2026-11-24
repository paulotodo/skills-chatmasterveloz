# Marca e acesso em Plataforma

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/marca-e-acesso-em-plataforma
- **Categoria:** Recursos
- **Menu:** Configurações › Plataforma em Configurações › Marca e acesso em Plataforma

---

🧩 O grupo **Marca e acesso** é o primeiro da **Plataforma** e cuida de duas coisas: como a plataforma se apresenta — o nome, o aplicativo instalado, a central de ajuda e a tela de entrada — e quem pode entrar nela — o cadastro público, o login por outros sistemas e a regra de senha. Tudo aqui vale para todas as empresas da instância.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Plataforma**. **Marca e acesso** é o primeiro grupo da página.
>
> ➡️ Cada campo grava assim que você muda o valor. Não há botão Salvar.

## ⚡ Nome da Aplicação

A seção **Nome da Aplicação** define o nome que aparece no título da aba do navegador.

🔘 **Nome da Aplicação:** o nome da plataforma para todas as empresas. Aparece no título da aba do navegador.

⚠️ O nome do aplicativo instalado é outro campo — **Nome do Aplicativo PWA**, na seção **APLICATIVO PWA**. Os dois podem ser iguais; a plataforma não copia um para o outro.

## ⚡ APLICATIVO PWA

A seção **APLICATIVO PWA** define o nome que a plataforma mostra quando é instalada como aplicativo no celular ou no computador, direto pelo navegador.

🔘 **Nome do Aplicativo PWA:** o nome que aparece embaixo do ícone na tela inicial do aparelho e na janela do aplicativo.

## ⚡ CENTRAL DE AJUDA

A seção **CENTRAL DE AJUDA** define para onde o menu **Central de Ajuda** leva cada perfil de usuário. É aqui que você aponta a ajuda da plataforma para a sua própria documentação, com um campo por perfil: atendente, supervisor e administrador. Pode ser o mesmo endereço nos três.

🔘 **URL de Ajuda para Usuários:** o endereço aberto quando um atendente User clica em **Central de Ajuda**.

🔘 **URL de Ajuda para Supervisores:** o mesmo, para o perfil supervisor.

🔘 **URL de Ajuda para Admins:** o mesmo, para o administrador da empresa.

⚠️ A documentação aberta pela **Central de Ajuda** não muda conforme o perfil de quem clica: coloque o mesmo endereço nos três campos.

## ⚡ Configurações Globais

A seção **Configurações Globais** decide o que a tela de entrada (login) mostra, se uma empresa pode se cadastrar sozinha e por quanto tempo pode ser testada, se o administrador vê a própria fatura — e guarda dois campos de integração que valem para todos. Os campos de **Sim/Não** ligam e desligam; **Tempo de Trial?** é um número de dias.

🔘 **Termos de Uso Visível?:** com **Sim**, o link "Concordo com os Termos de Uso" aparece na tela de entrada. O PDF deve ser enviado no menu **Configurações  ›  Documentos**.

🔘 **Política de Privacidade Visível?:** com **Sim**, o link "Concordo com a Política de Privacidade" aparece na tela de entrada. O PDF deve ser enviado no menu **Configurações  ›  Documentos**.

🔘 **Registro (Inscrição) Visível?:** mostra ou esconde o link de cadastro na tela de login.

🔘 **Registro (Inscrição) Permitida?:** com **Não**, o cadastro público é recusado mesmo que o link esteja visível. Os dois campos juntos deixam esconder o link sem desligar o registro, ou desligar o registro sem mexer na tela.

🔘 **Permitir Download Externo?:** com **Sim**, os arquivos dos atendimentos podem ser baixados por endereço direto, fora da tela do atendimento.

🔘 **Permitir Importação de Contatos Automática?:** importa os contatos do aparelho ao conectar. Essa funcionalidade é instável e sobrecarrega o sistema.

🔘 **Exibir Fatura para Clientes?:** habilita o menu **Financeiro** aos usuários Admin, para visualização e pagamento da fatura.

🔘 **Tempo de Trial?:** quantos dias, de **1** a **7**, uma empresa que se cadastra sozinha poderá testar o sistema.

🔘 **CHAMA.AI Nome de Exibição (WhiteLabel):** o nome de exibição usado na integração **CHAMA.AI**, na sua marca.

🔘 **Webhook de Eventos [Conexões]:** URL onde serão enviados os eventos administrativos, como os de monitoramento das conexões de todas as empresas e os de criação de novas empresas na plataforma.

## ⚡ V2 LAYOUT

A seção **V2 LAYOUT** tem um único campo: **URL Frontend V2 (Subdomínio deve pertencer ao mesmo domínio atual)**.

Essa opção foi descontinuada. O campo continua na seção, mas não é preciso preenchê-lo.

## ⚡ Aplicações Externas por Login

Um sistema de fora precisa entrar na plataforma em nome de um usuário — um painel próprio, um app, uma automação. Para isso ele faz login pela API, com o e-mail e a senha de um usuário da empresa, e recebe de volta uma credencial de sessão. A seção **Aplicações Externas por Login** decide se essa entrada pela API é permitida.

#### 💡 Vem ligado, e o campo vazio significa Sim

O login pela API existe desde sempre na plataforma. Esta opção foi criada depois, para dar a você a **possibilidade de desligar** — então uma instância que nunca mexeu no campo está permitindo. Campo em branco é **Sim**.

➡️ Deixe **Permitir Login de Terceiros?** em **Sim** se alguma aplicação precisa entrar pela API.

➡️ Mude para **Não** se nenhuma precisa — é uma porta a menos aberta.

### O que muda na prática

🔘 **Sim (ou campo vazio):** um sistema externo que envie e-mail e senha para o endereço de login da API recebe a **credencial de sessão** junto com os dados do usuário — nome, e-mail, perfil e a empresa a que ele pertence. Com essa credencial em mãos, ele passa a agir como aquele usuário.

🔘 **Não:** a mesma chamada é recusada, com a resposta `Method not allowed`. Nenhuma credencial é emitida, e nada muda para quem usa a plataforma pela tela.

⚠️ **Com Sim, basta o e-mail e a senha de um usuário para obter acesso pela API, de qualquer lugar.** Se a sua instância não integra nada por login, **Não** é a posição mais segura.

### A chamada que este campo libera

##### Endpoint

```
https://api2.chatmasterveloz.com/auth/login
```

##### Método

```
POST
```

##### Autenticação

```
Nenhuma — é esta chamada que gera a credencial
```

##### Payload

```javascript
{
    "email": "usuario@empresa.com.br",
    "password": "a senha desse usuário"
}
```

##### Resposta com Permitir Login de Terceiros em Sim

```javascript
{
    "token": "a credencial de sessão",
    "user": {
        "id": 42,
        "name": "Nome do Usuário",
        "email": "usuario@empresa.com.br",
        "profile": "admin",
        "companyId": 1,
        "company": { }
    }
}
```

##### Resposta com Permitir Login de Terceiros em Não

```javascript
{
    "error": "Method not allowed"
}
```

### Uma limitação que costuma confundir

Mesmo com **Sim**, uma **página web hospedada em outro domínio** não consegue fazer esse login pelo navegador: a API só aceita chamadas vindas do próprio endereço da plataforma, e o navegador barra o resto. Ou seja, este recurso serve para quem chama **de servidor** — a aplicação de fora fazendo a requisição por conta própria, não a página aberta no navegador do usuário.

⚠️ Abrir o painel já logado a partir de outro sistema, sem a senha e inclusive dentro de um iframe, é outra configuração: o **Login automático**, que cada empresa liga nas próprias Opções, no menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**.

## ⚡ Segurança de Senha

A seção **Segurança de Senha** liga, para a instância inteira, a exigência de senha forte.

🔘 **Exigir senha forte:** com **Sim**, uma senha nova só é aceita se tiver no mínimo 8 caracteres, com maiúsculas, minúsculas, números e caracteres especiais. Vale para os usuários de todas as empresas.

⚠️ Senhas já cadastradas não mudam sozinhas. A regra passa a ser cobrada quando alguém cria ou troca uma senha.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Troquei o Nome da Aplicação e a aba do navegador continua com o antigo.** Recarregue a página.
>
> **Troquei o Nome do Aplicativo PWA e no meu celular continua o antigo.** Quem já instalou fica com o nome antigo. Remova e instale de novo.
>
> **Qual a diferença entre a CENTRAL DE AJUDA e o Ajuda do menu Configurações?** O menu **Configurações  ›  Ajuda** cadastra vídeos dentro da plataforma. A seção **CENTRAL DE AJUDA** aponta o menu para um iframe dentro da plataforma com o endereço externo, substituindo a área de vídeos antiga.
>
> **O atendente clica em Central de Ajuda e nada abre.** O campo do perfil dele, na seção **CENTRAL DE AJUDA**, está vazio ou com um endereço incompleto — precisa começar com `https://`.
>
> **O link de Termos de Uso aparece, mas abre vazio.** Falta o PDF: envie no menu **Configurações  ›  Documentos**.
>
> **O administrador da empresa não acha a fatura dele.** É porque **Exibir Fatura para Clientes?**, na seção **Configurações Globais**, está em **Não**.
>
> **Nunca mexi no campo Permitir Login de Terceiros. Estou permitindo login pela API?** Sim. O campo em branco equivale a **Sim**, porque o recurso já existia antes da opção.
>
> **Desliguei o Permitir Login de Terceiros e uma integração parou.** Ela usava o login pela API. Volte para **Sim**, ou peça ao fornecedor um caminho que não dependa disso.
>
> **A chamada em `/auth/login` responde `Method not allowed`. O que fazer?** É o efeito de **Permitir Login de Terceiros?** em **Não**. Mude para **Sim** no menu **Configurações  ›  Plataforma**, seção **Aplicações Externas por Login**.
>
> **Permitir Login de Terceiros faz o iframe do cadastro da empresa entrar logado?** Não. As páginas embutidas recebem só a identificação de quem está usando; esta opção é sobre a chamada à API.
>
> **O Login automático é o mesmo que o Permitir Login de Terceiros?** Não. O **Permitir Login de Terceiros?** trata do login pela API com e-mail e senha. Abrir o painel já logado a partir de outro sistema, inclusive dentro de um iframe, é o **Login automático**, que o administrador da empresa liga no menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**.
>
> **Com Permitir Login de Terceiros em Não, meus usuários deixam de entrar na plataforma?** Não. A tela continua igual — o que muda é só a entrada pela API.
>
> **Liguei o Exigir senha forte e ninguém foi obrigado a trocar a senha.** É o esperado: a opção não força troca. Ela recusa senha fraca daqui para a frente.
>
> **O Exigir senha forte vale só para a minha empresa?** Não. A seção **Segurança de Senha** é da instância; todas as empresas passam a seguir a regra.
