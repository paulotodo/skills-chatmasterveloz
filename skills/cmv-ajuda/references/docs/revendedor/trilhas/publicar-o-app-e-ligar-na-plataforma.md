# Publicar o App e Ligar na Plataforma

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/publicar-o-app-e-ligar-na-plataforma
- **Categoria:** Trilhas
- **Menu:** Meta › Publicar o App e Ligar na Plataforma

---

🧩 A Meta aprovou o seu App — e, do lado do cliente, nada mudou ainda. Faltam dois passos: **publicar** o aplicativo, tirando-o do modo de desenvolvimento, e levar as **chaves** dele para a plataforma. É isso que liga a janela de login com a sua marca e libera a conexão de WhatsApp Oficial, Facebook e Instagram para os seus clientes.

☑️ **Virada de chave:** sair do modo de teste, em que só quem tem cargo no App consegue conectar.

☑️ **Whitelabel completo:** o cliente passa a ver o seu nome e o seu logotipo na janela de permissão do Facebook.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No portal **Meta for Developers**, publique o aplicativo.
>
> ➡️ Copie o **APP ID**, o **SECRET** e o **CONFIG ID**.
>
> ➡️ Cole no menu **Configurações  ›  Plataforma**, seção **WABA**.
>
> ➡️ Libere o recurso no plano da empresa e conecte o primeiro cliente.

## ☁️ Publicando o aplicativo

Acesse **Meus Aplicativos** em [https://developers.facebook.com](https://developers.facebook.com) usando a mesma conta de facebook utilizada para logar em sua BM.

🔲 Abra o seu aplicativo e coloque-o em produção. Dependendo da versão do painel, a ação aparece como **Publicar** ou como uma chave para alternar o app de desenvolvimento para **Ao vivo**.

⚠️ Enquanto o aplicativo estiver em desenvolvimento, **somente pessoas com cargo nele conseguem conectar**. O seu cliente vê erro na hora do login, e é esse o sintoma mais comum de quem esqueceu este passo.

## 🔑 As três chaves

🔘 **APP ID** e **SECRET:** em **Configurações do app → Básico**. O SECRET fica escondido até você clicar em mostrar.

🔘 **CONFIG ID:** em **Login do Facebook para Empresas → Configurações**, na configuração do cadastro incorporado (o Embedded Signup) que você criou ao virar Tech Provider. É o ID **daquela configuração**, não o do aplicativo.

📌 Se você também vai oferecer Instagram, existe um par próprio de ID e chave secreta para o login do Instagram.

## Levando as chaves para a plataforma

Acesse o menu **Configurações  ›  Plataforma**, seção **WABA**. Cole cada chave no campo de mesmo nome; o campo grava sozinho ao ser alterado.

⚠️ Essas chaves valem para **todas as empresas** da sua instância: cada número oficial instalado passa a entrar na sua conta de provedor na Meta. Trocar o APP ID ou o SECRET depois, com números já instalados, obriga a reinstalar.

## Liberando para a empresa

Ter as chaves não basta. A empresa que vai usar precisa do recurso liberado no plano dela, no menu **Configurações  ›  Planos**. Sem isso, o botão de adicionar WhatsApp Oficial não aparece para o cliente.

## Próximo Passo

🧭 Conectar o primeiro cliente: no menu **Conexões  ›  3 pontos  ›  Adicionar WhatsApp Oficial**, o popup de login já deve abrir com o seu nome e o seu logotipo.

🧭 Acompanhar a **qualidade e o limite de envio** dos números que forem instalados.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Publiquei o app e o cliente continua vendo erro no login.** Confira três coisas, nesta ordem: o app está mesmo fora do modo de desenvolvimento; as três chaves foram salvas na seção WABA; e a empresa do cliente tem o recurso liberado no plano.
>
> **O popup abriu com o nome de outra empresa.** As chaves antigas ainda estão valendo. Confira se o APP ID e o CONFIG ID salvos são os do **seu** aplicativo aprovado, e não os da estrutura que você usava antes.
>
> **Preciso republicar o app a cada permissão nova aprovada?** Não. A publicação é do aplicativo; cada permissão aprovada passa a valer sem nova virada de chave.
>
> **Onde vejo se o app está em produção?** No painel do aplicativo, o próprio indicador de modo — desenvolvimento ou ao vivo — fica junto ao nome do app.
