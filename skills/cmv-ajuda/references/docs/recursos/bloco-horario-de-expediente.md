# Horário de Expediente

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-horario-de-expediente
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Horário de Expediente

---

🧩 O bloco **Horário de Expediente** divide o fluxo em dois caminhos: um para quem escreve dentro do horário de atendimento de um Setor, outro para quem escreve fora dele. É o *"estamos fechados, voltamos amanhã às 8h"* feito pelo fluxo, sem ninguém ligar e desligar mensagem.

O horário não fica no bloco: ele vem do cadastro do **Setor** escolhido.

**🏷️ Categoria: Roteador**

Ideal para:

☑️ **Aviso fora do horário:** informa quando a equipe volta e o que o cliente pode fazer até lá.

☑️ **Atendimento humano só no expediente:** leva para a equipe quem chega no horário e para o autoatendimento quem chega fora.

![FlowBuilder Bloco Horário de Expediente](https://clihelper.chatmasterveloz.com/docs-imagem/14340-bloco-horario-escolhido-768x545.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Ligue o **Gerenciamento de Expediente** no menu **Configurações  ›  Opções  ›  Geral** e cadastre os horários do Setor.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo, clique no **+** e escolha **Horário de Expediente**.
>
> ➡️ Escolha o Setor, ou **Setor vinculado ao fluxo**, e clique em **Adicionar**.
>
> ➡️ Ligue as saídas **Dentro do Horário** e **Fora do Horário**.

## Como configurar o bloco Horário de Expediente

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Horário de Expediente**

🔘 **Setor:** de qual Setor vem o horário. A lista começa por **Setor vinculado ao fluxo**, que faz o bloco seguir o Setor ligado ao fluxo em vez de um Setor fixo, e depois traz os Setores da empresa.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco mostra o Setor escolhido (ou *Setor vinculado ao fluxo*) e tem **duas saídas**: **Dentro do Horário** e **Fora do Horário**.

## De onde vem o horário

O horário de cada Setor é cadastrado no menu **Setores & Chatbot  ›  editar o Setor  ›  aba Horários**.

⚠️ A aba **Horários** do Setor só aparece com o **Gerenciamento de Expediente** ligado, no menu **Configurações  ›  Opções  ›  Geral**. Sem ele, não há horário para o bloco conferir.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Onde mudo o horário que o bloco Horário de Expediente usa?** No cadastro do Setor, aba **Horários**. O bloco só lê o horário de lá.
>
> **O que é a opção Setor vinculado ao fluxo no bloco Horário de Expediente?** É a escolha que faz o bloco seguir o Setor ligado ao fluxo, em vez de um Setor fixo da lista. Ela aparece em primeiro lugar na lista **Setor** da janela do bloco.
>
> **Qual a diferença entre o Horário de Expediente e a Condição com o tipo Horário?** O **Horário de Expediente** usa a agenda da semana cadastrada no Setor. A **Condição** compara a hora com um valor digitado no próprio bloco, como antes ou depois das 18h.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Setor sem horário cadastrado:** o bloco não tem agenda para conferir. **Solução:** ligue o **Gerenciamento de Expediente** e preencha a aba **Horários** do Setor.
>
> **Uma saída sem ligação:** quem cai naquele caminho fica sem resposta. **Solução:** ligue as duas saídas, mesmo que **Fora do Horário** seja só um aviso.
