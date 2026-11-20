# Gatilho via Conexão

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/gatilho-via-conexao
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Pontos de Entrada (Gatilho) › Gatilho via Conexão

---

🧩 **Gatilho via Conexão** é o principal ponto de entrada para iniciar um fluxo em um atendimento. Funciona como a "Porta Principal" de um Atendimento.

☑️ **Fluxo Inicial:** ao retomar uma conversa com status **'Encerrado'**, o sistema gera automaticamente um novo protocolo. O atendimento vai para o **Setor** definido na Conexão, disparando o Fluxo Inicial.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Conexões**.
>
> ➡️ Ao editar uma conexão, na aba **Setores & Tempos**, defina um Setor no campo **Setores**.
>
> ➡️ No menu **Setores & Chatbot**, edite esse Setor e vincule o fluxo desejado no campo **Fluxos de Automação**.

## Como configurar o Gatilho de Fluxo em uma Conexão

#### ⚡ Passo 01 - O Fluxo

Acesse o menu → FlowBuilder e desenvolva seu fluxo.

#### ⚡ Passo 02 - O Setor

Acesse o menu **Setores & Chatbot** para criar ou editar um **Setor**. No campo **Fluxos de Automação**, selecione o fluxo desejado.

#### ⚡ Passo 03 - A Conexão

Acesse o menu **Conexões**, edite a conexão desejada e, na aba **Setores & Tempos**, selecione no campo **Setores** o Setor que tem o fluxo que será iniciado na abertura de um atendimento.

> **[DUVIDAS]**
>
> ### Dúvidas Comuns
>
> **Posso ter Setores diferentes para horários diferentes?** Na conexão, você deve definir um único Setor. Porém, dentro do seu **Fluxo**, você pode usar um bloco de "Horário de Expediente" ou "Condição" para decidir onde direcionar o atendimento.
>
> **Posso iniciar fluxos diferentes conforme palavra-chave enviada pelo cliente?** Sim, inicie seu fluxo com o bloco "Condição" de texto, roteando o atendimento conforme o texto digitado pelo cliente.
