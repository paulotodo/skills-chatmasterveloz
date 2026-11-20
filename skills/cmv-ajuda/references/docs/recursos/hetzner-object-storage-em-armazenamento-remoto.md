# Hetzner Object Storage em Armazenamento Remoto

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/hetzner-object-storage-em-armazenamento-remoto
- **Categoria:** Recursos
- **Menu:** Configurações › Opções em Configurações › Hetzner Object Storage em Armazenamento Remoto

---

🧩 Este é o passo a passo para guardar os arquivos da sua operação no **Object Storage da Hetzner**. São três etapas: criar o bucket, gerar as credenciais e ligar os dois na plataforma.

Contrate em [**hetzner.com**](https://www.hetzner.com/storage/object-storage/).

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Crie um **bucket**.
>
> ➡️ Gere as **credenciais**.
>
> ➡️ Ligue os dois na plataforma, no menu **Configurações  ›  Opções**, seção **Armazenamento Remoto de Arquivos**.

## Criar um bucket

O **bucket** é o container onde os arquivos ficam — pense numa pasta no provedor.

⚡ Na sua conta da Hetzner, acesse o menu **Object Storage  ›  Create Bucket**.

![Menu da Hetzner com a opção Create Bucket](https://clihelper.chatmasterveloz.com/docs-imagem/20861-hetzner-01-scaled.jpg)

⚡ Escolha um **nome** para o bucket e defina a visibilidade como **Pública**.

![Tela de criação do bucket, com o nome e a visibilidade](https://clihelper.chatmasterveloz.com/docs-imagem/20861-hetzner-02.jpg)

O bucket aparece na lista. Clique nele para criar a credencial.

![Lista de buckets da Hetzner com o bucket recém-criado](https://clihelper.chatmasterveloz.com/docs-imagem/20861-hetzner-03-scaled.jpg)

## Criar uma credencial

As **API Keys** são as chaves que permitem à plataforma gravar no seu bucket com segurança.

⚡ Dentro do bucket, clique em **Manage Credentials**.

![Botão Manage Credentials dentro do bucket](https://clihelper.chatmasterveloz.com/docs-imagem/20861-hetzner-credencial-01-scaled.jpg)

⚡ Na página que abrir, clique em **Generate Credentials**.

![Botão Generate Credentials na página de credenciais](https://clihelper.chatmasterveloz.com/docs-imagem/20861-hetzner-credencial-02-scaled.jpg)

⚡ Escreva uma **descrição** para a credencial — ela serve só para você se lembrar do que é — e clique em **Generate credentials**.

![Janela pedindo a descrição da credencial](https://clihelper.chatmasterveloz.com/docs-imagem/20861-hetzner-credencial-03.jpg)

⚠️ **Copie as chaves agora e guarde em lugar seguro.** A Hetzner não mostra a Secret Key de novo depois que você fecha esta tela — perdeu, é preciso gerar outra.

São dois valores: a **Access Key** e a **Secret Key**.

![Tela com a Access Key e a Secret Key geradas](https://clihelper.chatmasterveloz.com/docs-imagem/20861-hetzner-credencial-04.jpg)

## Integrar o armazenamento na plataforma

Acesse o menu **Configurações  ›  Opções** e localize a seção **Armazenamento Remoto de Arquivos**.

![Caminho até o Armazenamento Remoto de Arquivos na plataforma](https://clihelper.chatmasterveloz.com/docs-imagem/20861-hetzner-credencial-06-scaled.jpg)

![Campos do Armazenamento Remoto de Arquivos na plataforma](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ab17c4666160.png)

➡️ **Minio URL / S3 Custom Api URL:** o endereço do seu bucket. **Escreva o `https://` na frente** — sem ele a ligação não fecha.

➡️ **Nome do Bucket:** o mesmo nome que você deu ao bucket.

➡️ **S3 Key:** a **Access Key** da credencial.

➡️ **S3 Secret:** a **Secret Key** da credencial.

#### 📌 Pronto!

A partir de agora, todos os arquivos recebidos na plataforma passam a ser enviados para o seu bucket depois de alguns minutos.

⚠️ **Confira que funcionou.** Abra o seu bucket e veja se os arquivos estão chegando. Enquanto a ligação não estiver certa, a plataforma segue apagando os arquivos antigos no prazo de sempre — e o que foi apagado não volta.
