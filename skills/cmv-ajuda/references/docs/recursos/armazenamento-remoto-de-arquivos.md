# Armazenamento Remoto de Arquivos

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/armazenamento-remoto-de-arquivos
- **Categoria:** Recursos
- **Menu:** Configurações › Opções em Configurações › Armazenamento Remoto de Arquivos

---

🧩 A plataforma mantém os **arquivos** recebidos e enviados em backup por alguns poucos dias, apagando-os depois para liberar espaço no **armazenamento interno**. Para que fiquem guardados de forma permanente, é preciso contratar um **armazenamento externo** e vinculá-lo à empresa nesta seção.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Escolha e contrate um provedor de armazenamento de objetos.
>
> ➡️ Crie o **bucket** e gere as **chaves de acesso** no provedor.
>
> ➡️ Acesse o menu **Configurações  ›  Opções**, localize **Armazenamento Remoto de Arquivos** e preencha os campos.

## Provedores compatíveis

➡️ **Amazon Web Services** S3 (Simple Storage Service)

➡️ **Cloudflare** R2

➡️ **MinIO**

➡️ **Hetzner** Object Storage

## Como integrar um armazenamento externo

🔘 Escolha um provedor de armazenamento de objetos.

🔘 Crie um **bucket** na plataforma escolhida. Buckets funcionam como containers — parecidos com pastas — e são onde os arquivos vão ficar.

🔘 Com o bucket criado, gere as **chaves de acesso**. São elas que autorizam a plataforma a gravar e ler no bucket.

## Os campos, na ordem da tela

![Campos do Armazenamento Remoto de Arquivos na plataforma](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ab17c4666160.png)

🔘 **R2 URL:** o endereço do bucket quando o provedor é a Cloudflare.

🔘 **MINIO URL / S3 CUSTOM API URL:** o endereço da API quando o provedor é MinIO, Hetzner ou um S3 com endereço próprio.

🔘 **Nome do Bucket:** o nome exato do bucket criado no provedor.

🔘 **S3 KEY** e **S3 SECRET:** o par de chaves de acesso gerado no provedor.

⚠️ As chaves dão acesso de escrita ao bucket. Gere um par exclusivo para a plataforma, com permissão só naquele bucket — e não reaproveite chaves de outro sistema.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preenchi tudo e os arquivos continuam sumindo.** Confira o **Nome do Bucket** — precisa ser exato — e se a chave tem permissão de escrita. Arquivos anteriores à configuração não são recuperados.
>
> **Preciso de armazenamento externo para gravações de ligação?** Sim. As gravações do PABX são salvas no mesmo bucket configurado aqui.
