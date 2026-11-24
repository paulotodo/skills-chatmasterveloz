# Facebook Nativo (App próprio)

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/como-habilitar-facebook-nativo-whitelabel
- **Categoria:** Recursos
- **Menu:** Como Habilitar › Facebook Nativo (App próprio)

---

⭐ Módulo WABA Proprietária.

🧩 Ofereça **Facebook Messenger** em modo whitelabel: as mensagens da página do cliente chegam à plataforma como atendimento normal, sob o seu cadastro de provedor.

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
> ➡️ Habilite a opção do **Facebook INC** [para aplicativo próprio] no menu **Configurações  ›  Planos**.

> **[PREREQUISITO]**
>
> ## Pré-requisitos
>
> 🔘 **BM verificada** na Meta.
>
> 🔘 Status de **Tech Provider** junto à Meta.
>
> 🔘 Permissões avançadas analisadas no aplicativo do Facebook.

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

➡️ Finalize em **Publicar**, ou ative no topo da página do aplicativo a opção **Modo do Aplicativo: Ao vivo**.

![config_id Meta Developers](https://revendedor.chatmasterveloz.com/docs-imagem/ed-6a98282c41b6c.png)

## 🖥️ Inserir as chaves na plataforma

➡️ Acesse o menu **Configurações  ›  Plataforma**, seção **WABA**.

Preencha **APP ID**, **CONFIG ID** e **SECRET** com o que foi copiado.

Em **FB_SDK** informe a versão, por ex: `v25.0`.

## ☁️ Assinaturas do webhook na Meta

Depois do setup, volte ao aplicativo da Meta para assinar os campos do webhook.

⚡ No produto **USER**, assine: `about`, `first_name`, `last_name`, `likes`, `name`.

⚡ No produto **Page**, assine: `messages`, `messaging_postbacks`.

#### ☁️ Aprovar o aplicativo na Meta

Envie os vídeos das permissões do aplicativo do Facebook para análise da Meta e aguarde a aprovação.

## 🖥️ Habilitar na plataforma

➡️ No menu **Configurações  ›  Planos**, habilite a opção do **Facebook para aplicativo próprio**. Na tela ela aparece como **Facebook INC**.

➡️ No menu **Conexões**, use os três pontos e escolha **Adicionar Facebook Messenger**. Se a opção não aparecer, reinicie as conexões antes.

➡️ Conclua o login do Facebook na plataforma.

⚠️ Não habilite Facebook INC e Facebook Portal na mesma instância. São caminhos alternativos para a mesma funcionalidade; escolha um.
