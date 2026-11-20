# Gatilho via API

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gatilho-via-api
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Pontos de Entrada (Gatilho) › Gatilho via API

---

🧩 **Gatilho via API** é o método que permite que softwares externos (seu site, ERP, n8n, RD Station, entre outros) "forcem" o início de um fluxo através de código.

Diferente do gatilho de conexão (onde o cliente chama a empresa), aqui é a **empresa que chama o cliente** ativamente baseada em um evento externo.

Ideal para:

☑️ **Mensagens Transacionais:** enviar um "Seu pedido foi aprovado!" assim que a compra ocorre no site.

☑️ **Leads de Site:** quando alguém preenche um formulário na Landing Page, o sistema cria o contato e já dispara o robô de qualificação imediatamente.

☑️ **Reativação de Base:** sistemas de CRM externos que enviam ofertas para contatos antigos.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No seu sistema externo faça uma chamada API para nosso endpoint **Mensagem para FlowBuilder**
>
> ```
> .../api/messages/flowbuilderStart
> ```

## Como configurar o Gatilho de Fluxo via API

#### ⚡ Passo 01 - O Fluxo

Acesse o menu → FlowBuilder e desenvolva seu fluxo.

#### ⚡ Passo 02 – O Setor

Acesse o menu **Setores & Chatbot** para criar ou editar um **Setor**. No campo **Fluxos de Automação**, selecione o fluxo desejado.

#### ⚡ Passo 03 - A API

Faça uma chamada API:

##### Endpoint

```
https://api2.chatmasterveloz.com/api/messages/flowbuilderStart
```

##### Método

```
POST
```

##### Autenticação

```
Bearer {seutokenaqui}
```

##### Payload

```json
{
    "number": "5511955892164",
    "queueId": "3"
  }
```

➡️ **“number”:** telefone do destinatário no formato ddi ddd numero (somente números).

➡️ **“queueId”:** ID do Setor que está vinculado ao fluxo desejado.

#### 📌 Atenção: ao chamar essa API, o atendimento passa para **Aguardando**.

> **[DUVIDAS]**
>
> ### Dúvidas Comuns
>
> **O cliente precisa ter o contato salvo?** Não. A API consegue disparar mensagens para números que nunca interagiram antes. Porém, cuidado com as políticas de bloqueio do WhatsApp ao abordar contatos frios massivamente.
>
> **Posso enviar variáveis (como Nome do Cliente) pela API FlowBuilder Start?** Você pode utilizar "Mustaches" (que são as variáveis internas do nosso sistema), mas enviar variáveis vindo do seu sistema externo não. Para isso utilize o Webhook Triggers.
