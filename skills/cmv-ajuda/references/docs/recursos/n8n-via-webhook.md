# n8n via Webhook

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/n8n-via-webhook
- **Categoria:** Recursos
- **Menu:** Integrações › n8n via Webhook

---

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/22182-n8n.jpg)

## Integração n8n via Webhook

A integração com o N8N via Webhook pode acontecer através da Conexão, do Setor ou do Webhook Eventos

🧩 **Conectar o n8n ao **Chat Master Veloz** (Via Webhook)** permite que você dispare automações complexas no n8n a partir de eventos que ocorrem em nosso sistema (ex: uma nova mensagem é recebida, um atendimento é encerrado, ou uma tag é adicionada).

**Funciona assim:** ao conectar um fluxo do n8n em nossa plataforma - via **Conexão**, **Setor** ou **Webhook Eventos** - toda vez que nosso sistema enviar um webhook (evento) esse fluxo do n8n será **iniciado**, assim como sua automação programada.

☑️ **Automação de Eventos:** enviar dados para outras ferramentas (CRM, planilhas, email marketing) no momento exato em que um evento acontece.

☑️ **Inteligência Artificial:** desenvolver uma IA conversacional capaz de receber e enviar mensagens.

☑️ **Integração em Tempo Real:** garantir que as informações da nossa plataforma para os seus fluxos externos, sem atrasos.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Crie um **Workflow** no n8n.
>
> ➡️ Nesse workflow adicione um node de **Webhook Trigger** definindo HTTP Method POST. ➡️ Copie a **URL** desse node dentro do campo “webhook” em uma **Conexão**, um **Setor** ou um **Webhook Eventos** em nossa plataforma.

## Como integrar o n8n com nosso sistema

### ⚡ Passo 01 - Configurar um fluxo no n8n

Dentro do N8N, crie um Workflow e adicione o node **Webhook Trigger,** para definir uma URL que será ativado quando nossa plataforma enviar um webhook.

**➡️** Utilize o HTTP Method **Post**

**➡️ Em Path:** defina uma URL personalizada e única.

**➡️ Authentication:** opcional, mas o padrão é None.

![Formulário Webhook Trigger do n8n para configurar a integração](https://clihelper.chatmasterveloz.com/docs-imagem/22182-n8n-webhook-trigger.jpg)

### ⚡ Passo 02 - Conectar o fluxo do n8n em nossa plataforma

Ainda no node do **Webhook Trigger (n8n)**, clique na aba **Production URL** e em seguida no link logo abaixo para Copiar a URL.

Conecte esse fluxo em uma **Conexão**, um **Setor** ou um **Webhook Eventos** dentro de nossa plataforma, colando a URL nos campos específicos.

◽ Para conectar o fluxo em uma **Conexão**, acesse → Conexões > editar > Integrações > Webhook Principal ou Secundário

◽ Para conectar o fluxo em um **Setor**, acesse o menu **Setores & Chatbot  ›  editar  ›  URL do Webhook**

◽ Para conectar o fluxo em um **Webhook Eventos**, acesse → Configurações > seção Webhook | Eventos > escolha o evento

### ⚡ Passo 03 - Responder via API (opcional)

Em seu fluxo n8n você pode opcionalmente utilizar nossas APIs para enviar comandos para nossa plataforma como responder um lead, alterar dados do atendimento, do contato, entre outras funcionalidades.

Para isso, utilize o node **HTTP Request do n8n**, usando os "Endpoints" de nossa biblioteca de API e o "Token da Conexão" desejada.
