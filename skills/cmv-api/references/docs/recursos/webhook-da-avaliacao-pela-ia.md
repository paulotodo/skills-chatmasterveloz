# Webhook da Avaliação pela IA

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/webhook-da-avaliacao-pela-ia
- **Categoria:** Recursos
- **Menu:** Avaliação pela IA › Webhook da Avaliação pela IA

---

🧩 O **Webhook da avaliação** é o endereço de outro sistema da empresa que recebe os eventos da **Avaliação pela IA**: o atendimento avaliado, a aula gerada, o alerta à gestão e os outros que a tela lista. Serve para outro sistema saber o que aconteceu na avaliação sem ninguém copiar à mão.

O **Webhook da avaliação** não fica no bloco da **Avaliação pela IA**, na aba **Automação**: ele fica na aba **Integrações e segurança** das Opções, com o próprio **Salvar**.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Webhooks e integrações**.
>
> ➡️ Em **Webhook da avaliação**, informe o endereço que vai receber os eventos e clique em **Salvar**.

## Como configurar o Webhook da avaliação

Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**. Na seção **Webhooks e integrações**, o campo **Webhook da avaliação** recebe o endereço do sistema que vai receber os eventos da **Avaliação pela IA**, e o **Salvar** ao lado grava o endereço.

⚠️ O endereço do **Webhook da avaliação** precisa começar com `http://` ou `https://`, sem espaços, e não pode apontar para a rede interna.

## Os eventos do Webhook da avaliação

A tela lista seis eventos da **Avaliação pela IA**:

🔘 `atendimento-avaliado`

🔘 `avaliacao-falhou`

🔘 `aula-gerada`

🔘 `alerta-da-avaliacao`

🔘 `contato-fora-da-avaliacao`

🔘 `contato-de-volta-na-avaliacao`

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Onde fica o Webhook da avaliação da Avaliação pela IA?** No menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Webhooks e integrações**, e não no bloco da **Avaliação pela IA**, na aba **Automação**.
>
> **O aviso dos Alertas à gestão também vai para o Webhook da avaliação?** Vai. Nas palavras da tela dos **Alertas à gestão**: *"O aviso também vai para o webhook da avaliação."*
