# Cloudflare R2 em Armazenamento Remoto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/cloudflare-r2-em-armazenamento-remoto
- **Categoria:** Recursos
- **Menu:** Configurações › Opções em Configurações › Cloudflare R2 em Armazenamento Remoto

---

🧩 Este é o passo a passo para guardar os arquivos da sua operação no **Cloudflare R2**. São três etapas: criar o bucket com um domínio próprio, gerar as credenciais e ligar os dois na plataforma.

Contrate em **[cloudflare.com](https://www.cloudflare.com)**.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Crie um **bucket** e o **domínio** dele.
>
> ➡️ Gere as **credenciais**.
>
> ➡️ Ligue os dois na plataforma, no menu **Configurações  ›  Opções**, seção **Armazenamento Remoto de Arquivos**.

## Criar um bucket

O **bucket** é o container onde os arquivos ficam — pense numa pasta no provedor.

⚡ Na sua conta da Cloudflare, acesse o menu **Build  ›  Storage & Databases  ›  R2 Object Storage  ›  Overview  ›  Create Bucket**.

![Menu da Cloudflare com o caminho até Create Bucket](https://clihelper.chatmasterveloz.com/docs-imagem/25831-cloudflare-criar-bucket-scaled.jpg)

⚡ Escolha um **nome** para o bucket.

![Tela de configuração do nome do bucket na Cloudflare](https://clihelper.chatmasterveloz.com/docs-imagem/25831-cloudflare-configurar-bucket.jpg)

## Criar um domínio para o bucket

Abra o bucket recém-criado, vá na aba **Settings** e clique em **+ Add** na seção **Custom Domains**.

Adicione — ou crie — um subdomínio para esse bucket.

![Seção Custom Domains do bucket, na aba Settings](https://clihelper.chatmasterveloz.com/docs-imagem/25831-cloudflare-domains-bucket-scaled.jpg)

## Criar uma credencial

As **API Keys** são as chaves que permitem à plataforma gravar no seu bucket com segurança.

⚡ Em **Account Details**, abra **Manage** e clique em **Create Account API Token**.

![Botão Create Account API Token na seção Account Details](https://clihelper.chatmasterveloz.com/docs-imagem/25831-cloudflare-criar-key-scaled.jpg)

⚡ Dê um **nome** ao token e escolha a permissão **Object Read & Write** antes de criar.

![Tela de criação do token, com a permissão Object Read and Write selecionada](https://clihelper.chatmasterveloz.com/docs-imagem/25831-cloudflare-api-token-create.jpg)

⚠️ **Copie as chaves agora e guarde em lugar seguro.** A Cloudflare não mostra a Secret Key de novo depois que você fecha esta tela — perdeu, é preciso gerar outra.

São três valores: a **Access Key**, a **Secret Key** e a **URL S3 API** da sua conta.

![Tela com as chaves geradas e a URL S3 API](https://clihelper.chatmasterveloz.com/docs-imagem/25831-cloudflare-api-token.jpg)

## Integrar o armazenamento na plataforma

Acesse o menu **Configurações  ›  Opções** e localize a seção **Armazenamento Remoto de Arquivos**.

![Campos do Armazenamento Remoto de Arquivos na plataforma](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ab17c4666160.png)

➡️ **R2 URL:** a URL do Custom Domain que você criou no bucket.

➡️ **Minio URL / S3 Custom Api URL:** a URL S3 API da sua conta.

➡️ **Nome do Bucket:** o mesmo nome que você deu ao bucket.

➡️ **S3 Key:** a **Access Key** da credencial.

➡️ **S3 Secret:** a **Secret Key** da credencial.

#### 📌 Pronto!

A partir de agora, todos os arquivos recebidos na plataforma passam a ser enviados para o seu bucket depois de alguns minutos.

⚠️ **Confira que funcionou.** Abra o seu bucket e veja se os arquivos estão chegando. Enquanto a ligação não estiver certa, a plataforma segue apagando os arquivos antigos no prazo de sempre — e o que foi apagado não volta.
