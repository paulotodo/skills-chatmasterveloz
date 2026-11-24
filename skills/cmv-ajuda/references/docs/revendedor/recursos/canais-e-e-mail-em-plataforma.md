# Canais e e-mail em Plataforma

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/canais-e-e-mail-em-plataforma
- **Categoria:** Recursos
- **Menu:** Configurações › Plataforma em Configurações › Canais e e-mail em Plataforma

---

🧩 O grupo **Canais e e-mail** guarda as chaves e versões dos canais que a plataforma conecta — o aplicativo da Meta, para a **API Oficial**, o **Instagram** e o **Facebook**, e a versão do WhatsApp não oficial — e o serviço que envia os e-mails da plataforma. Tudo aqui vale para todas as empresas da instância.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Plataforma**, grupo **Canais e e-mail**.
>
> ➡️ Cada campo grava assim que você muda o valor. Não há botão Salvar.

## ⚡ WABA

A seção **WABA** guarda as chaves do seu aplicativo na Meta — as que permitem instalar números de **API Oficial** e contas de **Instagram e Facebook** pela plataforma, em nome da sua empresa.

➡️ Crie e aprove o aplicativo na Meta.

➡️ Preencha as chaves e escolha se novas conexões nascem com coexistência.

🔘 **APP ID:** o ID do aplicativo da Meta.

🔘 **CONFIG ID:** o ID da configuração de login do cadastro incorporado.

🔘 **SECRET:** a chave secreta do aplicativo.

🔘 **META IG APP ID (Instagram Login)** e **META IG APP SECRET (Instagram Login):** o ID e a chave secreta do aplicativo usado para o login do Instagram.

🔘 **FB_SDK:** a versão da API da Meta que a plataforma usa. Ex: formato `v25.0`.

🔘 **Habilitar COEX para novas conexões?:** com **Sim**, as conexões oficiais criadas a partir de então podem ser instaladas em modo de coexistência — o número continua funcionando no aplicativo do WhatsApp Business ao mesmo tempo.

⚠️ Estas chaves valem para todas as empresas: cada número oficial instalado pela plataforma entra na sua conta de provedor na Meta. Trocar o **SECRET** ou o **APP ID** com números já instalados exige reinstalar.

## ⚡ VERSÃO BAILEYS - FORÇADO

A seção **VERSÃO BAILEYS - FORÇADO** fixa a versão do protocolo usada pelas conexões de WhatsApp não oficial. Em branco, a plataforma escolhe sozinha — e é assim que ela deve ficar no dia a dia.

➡️ Preencha **Versão Forçada da Baileys** apenas quando uma versão específica for necessária para as conexões voltarem a funcionar. Depois, limpe.

🔘 **Versão Forçada da Baileys:** a versão a ser usada por todas as conexões Baileys (básica) da instância. Vazio é o normal.

⚠️ A Baileys foi descontinuada na plataforma, migre os clientes que a utilizam para a Pro.

## ⚡ SMTP API (RESEND)

A seção **SMTP API (RESEND)** define por onde a plataforma envia o e-mail com o código de recuperação de senha; os demais avisos por e-mail também são enviados por aqui.

➡️ Crie uma conta na **[Resend](https://resend.com)**, verifique o seu domínio e gere uma chave de API.

➡️ Cole a chave em **API RESEND** e informe o **Remetente de E-Mail**.

### Como preparar o Resend

Faça o cadastro em [resend.com/signup](https://resend.com/signup) usando como login o próprio endereço que será o remetente.

#### ➡️ Validar o domínio

🔘 No Resend, acesse **Domains** e clique em **+ Add Domain**.

🔘 Informe o domínio do e-mail e valide o DNS. Em provedores como a Cloudflare a validação é automática; nos demais, os registros são configurados um a um.

#### ➡️ Criar a chave de API

🔘 No Resend, acesse **Api Key** e clique em **+ Create Api Key**.

🔘 Dê um nome à chave — por exemplo, `Recuperar Senha Chat Master Veloz`.

🔘 Copie a chave: ela vai no campo **API RESEND** desta seção.

### Os campos, na ordem da tela

Por onde o usuário recebe o código (e-mail, WhatsApp ou os dois) se escolhe no **Modo de Recuperação de Senha**, no menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Segurança**.

🔘 **API RESEND:** a chave de API gerada na Resend. Vale para a instância inteira.

🔘 **Remetente de E-Mail:** o endereço que aparece como remetente. Precisa ser de um domínio verificado na Resend; de outro domínio, o envio é recusado.

⚠️ Sem esta seção preenchida, a recuperação de senha por e-mail não funciona. Empresa que usa **Somente WhatsApp** em **Modo de Recuperação de Senha** não depende dela.

⚠️ Dois envios do **Dashboard** de cada empresa também usam o e-mail desta seção: o **Resumo automático**, que a empresa programa para receber os números do atendimento, e o **Aviso dos alertas**, que avisa quando um alerta do painel abre. Sem a seção preenchida, nenhum dos dois é enviado por e-mail — os outros canais, como o WhatsApp, seguem —, e a janela do resumo mostra o motivo: *o e-mail da plataforma não está configurado (Configurações da Plataforma)*.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preenchi a seção WABA e o botão de adicionar WhatsApp Oficial não aparece nas conexões.** As chaves sozinhas não bastam. A empresa precisa ter **WABA WL** no plano, no menu **Configurações  ›  Planos**, e as conexões podem precisar de reinício.
>
> **Habilito COEX ou não?** Com coexistência, o cliente mantém o número no aplicativo do celular. Sem ela, o número passa a existir só na plataforma. É uma decisão comercial sua, e vale para as conexões novas a partir da mudança.
>
> **Preciso preencher a Versão Forçada da Baileys para conectar um número?** Não. Somente em casos de emergência.
>
> **Preenchi a Versão Forçada da Baileys e as conexões caíram.** Reinicie as conexões da instância.
>
> **O usuário não recebe o e-mail de recuperação.** Confira, nesta ordem: a **API RESEND** está preenchida; o **Remetente de E-Mail** é de um domínio verificado na Resend; o e-mail do usuário está certo no cadastro dele.
>
> **As empresas não recebem o Resumo automático ou o Aviso dos alertas do Dashboard por e-mail.** Confira a seção **SMTP API (RESEND)**: os dois usam o mesmo envio de e-mail da plataforma. Sem a **API RESEND** e o **Remetente de E-Mail**, a janela do resumo, no Dashboard da empresa, mostra *o e-mail da plataforma não está configurado (Configurações da Plataforma)*.
>
> **Posso usar outro provedor de e-mail?** A plataforma envia pela API da Resend. Não há campo para servidor SMTP genérico nesta tela.
>
> **Como sei se o e-mail enviado pela SMTP API (RESEND) foi entregue?** Acompanhe pelo menu **Logs** dentro do painel do Resend. Ele mostra se a mensagem foi entregue ou rejeitada.
