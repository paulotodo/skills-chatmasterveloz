# Pergunta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-pergunta
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Pergunta

---

🧩 **O Bloco de Pergunta** é o momento de escuta do seu fluxo. Ele serve para **interromper a automação** e ficar aguardando o cliente digitar alguma coisa. Enquanto o cliente não responder (ou alguma inatividade acionar), o fluxo não avança para o próximo passo.

**🏷️ Categoria: Mensagem**

☑️ **Captura de Dados:** Ideal para perguntar Nome, E-mail, CPF ou Cidade.

☑️ **Engajamento:** Transforma a conversa em um diálogo real.

☑️ **Controle de Fluxo:** Garante que o cliente só receba a próxima mensagem após interagir.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Pergunta**.
>
> ➡️ Preencha sua **mensagem** e clique no botão **Adicionar**.

## Vídeo Tutorial

[Vídeo Voomly — id BlfAVhKMhwYRgNvXXME77t3e00LYEDu6wjvpRtxeXk7BN68Ad, tipo v]  

## Como adicionar o bloco "Pergunta" no FlowBuilder Nativo

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Pergunta**

![FlowBuilder Formulário Bloco de Pergunta](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ada37999f80b.png)

A janela **Adicionar bloco: Pergunta** tem os campos abaixo.

🔘 **Pergunta:** digite o texto de sua pergunta.

🔘 **Mover de setor por inatividade:** ligado, o contato que parar nesta pergunta e não responder entra na regra de inatividade da Conexão — a mesma **Após / Mover** da aba **Setores & Tempos**, que leva para outro Setor, depois do tempo definido, o cliente parado no fluxo ou sem Setor. Desligue quando a resposta puder demorar de propósito: o atendimento fica parado nesta pergunta até o cliente voltar, ou até o prazo do campo **Sem resposta**, quando preenchido.

🔘 **Sem resposta: seguir pela saída depois de (minutos):** o prazo para o cliente responder. Com minutos preenchidos, o bloco ganha a saída **Sem resposta**: ligue-a ao passo de quem não responder nesse tempo — uma mensagem de lembrete ou a transferência para um atendente, por exemplo. Vazio ou **0** desliga.

🔲 Para finalizar, clique em **Adicionar**.

## Como salvar a Resposta após o bloco de "Pergunta"?

Utilize o bloco de **Variável**, logo após o bloco de **Pergunta.**

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O robô valida a resposta?** O bloco de Pergunta básico geralmente aceita qualquer texto. Se você precisa validar se é um CPF ou E-mail válido por exemplo, utilize os blocos de **Variável**, **Execução de Código JS** ou **Condição** conforme necessidade.
>
> **Como salvar a resposta do cliente?** Utilize um bloco de **Variável** logo na sequência.
>
> **O cliente parou na pergunta e sumiu. O atendimento fica preso ali para sempre?** Depende de dois campos, que fazem coisas diferentes: **Mover de setor por inatividade** ou **Sem resposta**.
