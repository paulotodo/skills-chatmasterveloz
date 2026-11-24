# Tech Provider

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/tech-provider
- **Categoria:** Trilhas
- **Menu:** Meta › Tech Provider

---

🧩 **Tornar-se um Tech Provider** significa configurar seu próprio Aplicativo dentro da Meta para gerenciar as contas de WhatsApp dos seus clientes.

O resultado prático é que, quando seu cliente clicar para conectar, ele verá o **Seu Logotipo** e o **Nome da Sua Empresa** na janela de permissão do Facebook, garantindo uma experiência 100% White Label.

☑️ **Branding:** Reforçar sua marca durante o processo de conexão (Embedded Signup).

☑️ **Autonomia:** Ter controle total sobre os tokens e a infraestrutura dos seus clientes.

☑️ **Profissionalismo:** Eliminar qualquer menção a terceiros na jornada do usuário.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o portal **Meta for Developers** para criar um novo **Aplicativo de Negócios** com **WhatsApp** e **vincular** à sua BM.
>
> ➡️ Realizar a **Verificação de Acesso** em sua BM.

> **[PREREQUISITO]**
>
> ## **Pré-requisitos Obrigatórios**
>
> Antes de começar, você **precisa** ter:
>
> ◽ Uma **BM (Portfólio Empresarial)** devidamente **Verificada** na Meta.
>
> ◽ Um **site ativo** com uma página de "Política de Privacidade".
>
> ◽ Um **logotipo** da sua empresa (1024x1024 pixels).

## ☁️ Criando um Aplicativo

Acesse [https://developers.facebook.com](https://developers.facebook.com) e faça login usando a mesma conta de facebook utilizada para logar em sua BM.

🔲 Clique em **Criar Aplicativo**.

🔘 Defina um nome para seu app e digite seu e-mail.

🔘 Selecione a opção **Conectar-se com clientes pelo WhatsApp**.

🔘 Selecione a sua BM (Portfólio Empresarial) verificada.

🔲 Clique em **Avançar** e depois **Ir para o Painel**.

## ☁️ Configurando o Aplicativo

### Configurações do app → Básico

É importante preencher os campos **Nome de Exibição**, **Namespace**, mas em especial:

🔘 **URL da Política de Privacidade.**

🔘 **Fazer upload do seu logotipo** 1024x1024 px.

🔘 **Categoria:** selecione "Negócios e Páginas" ou "Mensagens".

🔘 **Domínios do Aplicativo:** adicione todos os domínios de suas instâncias.

🔘 **Adicionar Plataforma:** digite a url de login do seu sistema.

Clique em **Salvar Alterações**.

### Login do Facebook para Empresas → Configurações

Marque como **Sim** a opção "**Entrar com o SDK do JavaScript**" e digite todos os domínios de suas instâncias em "**Domínios permitidos para o SDK do JavaScript**".

📌 **Passo extra:** talvez seja necessário agora acessar o menu **Painel** e clicar no link **Sou um Provedor de Tecnologia**, para que o link de Verificar Acesso apareça na BM.

## **💼** Verificar Acesso

Agora vamos solicitar acesso a tornar a BM Tech Provider.

Acesse a área de sua BM em [https://business.facebook.com](https://business.facebook.com)

No menu Informações da Empresa, logo abaixo do Status de Verificação da Empresa, você vai encontrar a área de **Verificação de Acesso** para iniciar a verificação.

🔘 Selecione a opção **Independent Tech Provider.**

🔘 **Quais opções descrevem melhor a sua empresa?:** escolha "Plataforma de SaaS".

🔘 **Como a sua empresa usará a plataforma de dados:** copie o texto abaixo:

```
O Chat Master Veloz - Plataforma de Atendimento Online utiliza a plataforma de dados da Meta, incluindo informações autorizadas do WhatsApp Business Platform, para permitir que empresas realizem atendimentos e interações automatizadas com seus clientes de forma segura e centralizada.

Nosso sistema conecta a conta comercial do WhatsApp de cada cliente ao painel do Chat Master Veloz, permitindo:

- o envio e recebimento de mensagens entre empresa e consumidor final,
- o gerenciamento de conversas por múltiplos atendentes,
- o uso de mensagens automáticas e modelos aprovados (templates),
- e o acompanhamento de métricas de atendimento, como tempo de resposta e volume de conversas.

Os dados da plataforma da Meta são usados apenas para executar essas funções em nome do cliente, respeitando todas as permissões concedidas por ele no momento da conexão.

O Chat Master Veloz não compartilha, vende ou utiliza dados para outros fins — apenas processa as informações necessárias para que o cliente consiga se comunicar com seus consumidores via WhatsApp de forma eficiente.
```

🔘 **Sua empresa gerencia vários portfólios empresariais?:** selecione "Não".

🔘 **Provide a link to your website:** digite a url da tela de login da plataforma.

🔲 Clique em **Salvar**.

## Próximo Passo

Obter as **permissões avançadas** do App ao enviar vídeos e solicitar análises.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Minha BM não é verificada, posso fazer isso?** Você consegue criar o App, mas **não consegue** deixá-lo público (Live). Seus clientes verão erro ao tentar logar. A verificação da BM é obrigatória para Tech Providers.
>
> **Quanto custa ser Tech Provider?** A Meta não cobra para você criar o App. O custo é apenas o esforço burocrático de aprovação.
>
> **O que é "Embedded Signup"?** É o nome técnico daquele popup bonito onde o cliente faz login. Ao criar esse App, você está habilitando o seu próprio Embedded Signup.
>
> **Quanto tempo demora para realização de acesso para ser Tech Provider?** Em média 2 dias.
