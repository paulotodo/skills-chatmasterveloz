# Instagram Nativo (App próprio)

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/como-habilitar-instagram-nativo-whitelabel
- **Categoria:** Recursos
- **Menu:** Como Habilitar › Instagram Nativo (App próprio)

---

⭐ Módulo WABA Proprietária.

🧩 Ofereça **Instagram** em modo whitelabel: as mensagens diretas do perfil do cliente chegam à plataforma como atendimento normal, sob o seu cadastro de provedor.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Configure o aplicativo na Meta e copie as chaves.
>
> ➡️ Insira as chaves na plataforma.
>
> ➡️ Configure o webhook do aplicativo da Meta.
>
> ➡️ Habilite a opção do **Instagram** [para aplicativo próprio] no menu **Configurações  ›  Planos**.

> **[PREREQUISITO]**
>
> ## Pré-requisitos
>
> 🔘 **BM verificada** na Meta.
>
> 🔘 Status de **Tech Provider** junto à Meta.
>
> 🔘 Permissões avançadas analisadas no aplicativo do Instagram.

## ☁️ Copiar as chaves do aplicativo da Meta

Acesse [**Meus Aplicativos**](https://developers.facebook.com) usando a mesma conta do Facebook que entra na sua BM.

No seu aplicativo, abra **Configurações do app > Básico**:

📝 Copie o **ID do Aplicativo**.

📝 Copie a **Chave Secreta do Aplicativo**.

Depois abra **(Casos de Uso) WhatsApp > Configurador de cadastro incorporado**:  
1. Encontre o box **Início do Cadastro Incorporado**.
2. Em **Escolha uma Configuração de Login**, clique no primeiro campo para adicionar. Pode manter o padrão e criar.
3. Logo abaixo, em **Sua página de destino do Cadastro incorporado hospedado pela Meta**:

📝 Copie o **Config ID** — são os números entre `config_id=` e `&` no endereço.

Depois abra **(Casos de Uso) Instagram > Configuração da API com login empresarial no Instagram**:

📝 Copie o **ID do app do Instagram**.

📝 Copie a **Chave Secreta do app do Instagram**.

Em **Configure o login da empresa no Instagram**, clique em **Configurar** e preencha:

🔘 **URL de Redirecionamento**: `https://{backendURL}/meta/instagram-login/callback`

Salve, entre novamente e preencha:

🔘 **URL de retorno de chamada de desautorização**: `https://{backendURL}/meta/deauthorize`

➡️ Finalize em **Publicar**, ou ative no topo da página do aplicativo a opção **Modo do Aplicativo: Ao vivo**.

![config_id Meta Developers](https://revendedor.chatmasterveloz.com/docs-imagem/ed-6a98282c41b6c.png)

## 🖥️ Inserir as chaves na plataforma

➡️ Acesse o menu **Configurações  ›  Plataforma**, seção **WABA**.

Preencha **APP ID**, **CONFIG ID** e **SECRET** com o que foi copiado.

Preencha também **META IG APP ID (Instagram Login)** e **META IG APP SECRET (Instagram Login)**.

Em **FB_SDK** informe a versão, por ex: `v25.0`.

## ☁️ Assinaturas do webhook na Meta

Depois do setup, volte ao aplicativo da Meta para assinar os campos do webhook.

⚡ No produto **USER**, assine: `about`, `first_name`, `last_name`, `likes`, `name`.

⚡ No produto **Instagram**, assine: `comments`, `live_comments`, `message_edit`, `message_reactions`, `messages`, `messaging_postbacks`, `messaging_referral`, `messaging_seen`.

#### ☁️ Aprovar o aplicativo na Meta

Envie os vídeos das permissões do aplicativo do Instagram para análise da Meta e aguarde a aprovação.

## 🖥️ Habilitar na plataforma

➡️ No menu **Configurações  ›  Planos**, habilite a opção do **Instagram para aplicativo próprio**. Na tela ela aparece como **Instagram INC**.

➡️ No menu **Conexões**, use os três pontos e escolha **Adicionar Instagram**. Se a opção não aparecer, reinicie as conexões antes.

➡️ Conclua o login do Instagram na plataforma.

⚠️ Não habilite Instagram INC e Instagram Portal na mesma instância. São caminhos alternativos para a mesma funcionalidade; escolha um.
