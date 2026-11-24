# API Oficial Nativa (App próprio)

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/como-habilitar-api-oficial-nativa-whitelabel
- **Categoria:** Recursos
- **Menu:** Como Habilitar › API Oficial Nativa (App próprio)

---

⭐ Módulo WABA Proprietária.

🧩 Ofereça **API Oficial** em modo whitelabel: o cadastro junto à Meta é seu, e os números dos seus clientes ficam sob a sua conta de provedor.

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
> ➡️ Habilite **WABA WL** no menu **Configurações  ›  Planos**.

> **[PREREQUISITO]**
>
> ## Pré-requisitos
>
> 🔘 **BM verificada** na Meta.
>
> 🔘 Status de **Tech Provider** junto à Meta.
>
> 🔘 Permissões avançadas analisadas no aplicativo do WhatsApp.

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

Em **FB_SDK** informe a versão, por ex: `v25.0`. Em **Habilitar COEX para novas conexões?**, escolha **Sim** se quiser oferecer coexistência.

O campo **Prazo de resposta da Meta (segundos)**, logo abaixo, é quanto tempo cada envio pela API Oficial espera a Meta responder antes do aviso de que ela não respondeu a tempo: de 5 a 120 segundos, valendo para todas as empresas.

## ☁️ Assinaturas do webhook na Meta

Depois do setup, volte ao aplicativo da Meta para assinar os campos do webhook.

⚡ No produto **USER**, assine: `about`, `first_name`, `last_name`, `likes`, `name`.

⚡ No produto **WhatsApp Business Account**, assine: `calls`, `flows`, `message_template_components_update`, `message_template_quality_update`, `message_template_status_update`, `messages`, `smb_message_echoes`, `template_category_update`, `template_correct_category_detection`.

#### ☁️ Aprovar o aplicativo na Meta

Envie os vídeos das permissões do aplicativo do WhatsApp para análise da Meta e aguarde a aprovação.

## 🖥️ Habilitar na plataforma

➡️ Habilite **WABA WL** no menu **Configurações  ›  Planos**.

➡️ No menu **Conexões**, use os três pontos e escolha **Adicionar WhatsApp Oficial**. Se a opção não aparecer, reinicie as conexões antes.

➡️ Conclua o login do Facebook na plataforma e instale o número como API Oficial.

⚠️ Para migrar um número que está em outro provedor, pode ser necessário adicionar o seu ID de parceiro na gestão do número.

⚠️ **Não habilite WABA WL e WABA INC na mesma instância.** São caminhos alternativos para a mesma funcionalidade; escolha um.
