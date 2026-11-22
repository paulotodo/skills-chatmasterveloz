# Gatilho via Webhooks Trigger

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gatilho-via-webhooks-trigger
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Pontos de Entrada (Gatilho) › Gatilho via Webhooks Trigger

---

🧩 **Gatilho via Webhook Trigger** é o método que cria um endereço de internet exclusivo (URL) para o seu fluxo. Quando qualquer sistema externo acessa esse link enviando os dados de um contato, o robô inicia imediatamente para aquela pessoa.

Diferente do Gatilho via API , o Webhook Trigger é capaz de receber **Variáveis Personalizadas** específicas para aquela conversa.

☑️ **Formulários de Site:** o cliente preenche "Nome" e "Interesse" no seu site. O site envia esses dados para o Webhook, e o robô já chama o cliente no WhatsApp dizendo: *"Olá [Nome], vi que gosta de [Interesse]!"*.

☑️ **Integrações com Ferramentas (Zapier/n8n/Make):** conectar seu CRM ou planilhas ao WhatsApp sem precisar programar uma integração de API complexa.

☑️ **Anúncios de Lead (Facebook Lead Ads):** assim que o lead preenche o cadastro no Facebook, a automação dispara o Webhook e o atendimento começa em segundos.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Webhooks | Triggers** e, na configuração do Webhook, selecione o **Setor** que tem o fluxo desejado vinculado.
>
> ➡️ Inicie uma requisição HTTP para o endpoint do Webhook

## Como configurar o Gatilho de Fluxo via Webhook

#### ⚡ Passo 01 - O Fluxo

Acesse o menu → FlowBuilder e desenvolva seu fluxo.

#### ⚡ Passo 02 – O Setor

Acesse o menu **Setores & Chatbot** para criar ou editar um **Setor**. No campo **Fluxos de Automação**, selecione o fluxo desejado.

#### ⚡ Passo 03 - O Webhook

Acesse o menu **Webhooks | Triggers** e crie um Webhook em **Novo Webhook | Trigger** — a criação pede só o **Nome**. No card do Webhook, clique no ícone de **ferramenta** para abrir a configuração:

🔘 **URL do Webhook:** o endereço que o sistema externo vai chamar.

🔘 **Selecione o FLUXO que será disparado:** a lista mostra os **Setores** que têm um fluxo vinculado. Escolha o Setor do fluxo desejado.

🔘 **Selecione a CONEXÃO de disparo:** por qual Conexão a mensagem vai para o cliente.

🔘 **Configuração dos Campos:** indique qual campo da requisição corresponde a **{celular}**, **{nome}**, **{email}** e **{extra1}** a **{extra4}**. Em **Campos Adicionais**, acrescente outros.

Para finalizar, clique em **Salvar Configuração**.

📌 Atenção: ao chamar essa API, o atendimento passa para **Aguardando**.

#### ⚡ Passo 04 - Requisição Webhook

Realize uma requisição HTTP POST para a URL do Webhook enviando os dados necessários para o funcionamento do seu fluxo. Obrigatório envio do número celular destinatário.

> **[DUVIDAS]**
>
> ### Dúvidas Comuns
>
> **Qual a diferença entre Gatilho via API e via Webhook?** Com o Webhook Trigger é possível iniciar um **Fluxo Específico** e passar variáveis exclusivas para aquela execução.
>
> **É seguro? Qualquer um pode disparar?** A URL do Webhook é pública, mas é um código longo e difícil de adivinhar. Cuidado em divulgar essa URL pois qualquer um que tenha acesso a ela poderá iniciar esse fluxo em seu sistema.
>
> **O que acontece se não enviar o telefone?** O fluxo falha. O sistema precisa saber o número do destinatário para funcionar o contato.
>
> **O cliente precisa ter o contato salvo?** Não. O Webhook consegue disparar mensagens para números que nunca interagiram antes. Porém, cuidado com as políticas de bloqueio do WhatsApp ao abordar contatos frios massivamente.
