# Avaliação do Atendimento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-avaliacao-do-atendimento
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Avaliação do Atendimento

---

🧩 O bloco **Avaliação do Atendimento** envia ao cliente uma pesquisa de satisfação no meio do fluxo, sem precisar encerrar o atendimento. Ele usa as pesquisas já cadastradas no menu **Avaliações**, com as mesmas opções de nota.

Depois que o cliente responde, o fluxo continua pela saída do bloco. Para encerrar o atendimento em seguida, ligue a saída a um bloco **Encerrar**.

**🏷️ Categoria: Mensagem**

Ideal para:

☑️ **Pesquisa depois do autoatendimento:** mede a satisfação de quem resolveu tudo com o fluxo, sem passar por uma pessoa.

☑️ **Nota antes de transferir:** colhe a avaliação de uma etapa antes de seguir para outra.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Cadastre a pesquisa no menu **Avaliações**, se ainda não existir.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo, clique no **+** e escolha **Avaliação do Atendimento**.
>
> ➡️ Escolha a **Pesquisa de satisfação** e clique em **Adicionar**.
>
> ➡️ Ligue a saída do bloco ao próximo passo, como um bloco **Encerrar**.

## Como configurar o bloco Avaliação do Atendimento

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Avaliação do Atendimento**

🔘 **Pesquisa de satisfação:** a pesquisa enviada ao cliente, entre as cadastradas no menu **Avaliações**.

🔘 **Mensagem (opcional):** o texto que vai antes das opções. Em branco, o bloco usa a mensagem cadastrada na própria pesquisa. As opções de nota são acrescentadas automaticamente.

🔘 **Sem resposta: seguir pela saída depois de (minutos):** com minutos preenchidos, o bloco ganha a saída **Sem resposta**, para quem não responder nesse tempo. Vazio ou 0 desliga.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco mostra o nome da pesquisa e tem uma saída para o próximo passo. Com **Sem resposta** preenchido, aparece a segunda saída, com o tempo escolhido.

⚠️ **O bloco Avaliação do Atendimento não encerra o atendimento.** Sem nada ligado na saída, o fluxo para depois da nota e o atendimento continua aberto.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O bloco Avaliação do Atendimento encerra o atendimento depois da nota?** Não. O fluxo segue pela saída do bloco. Para encerrar, ligue a saída a um bloco **Encerrar**.
>
> **A pesquisa que quero usar não aparece no bloco Avaliação do Atendimento.** O bloco lista as pesquisas cadastradas no menu **Avaliações**. Cadastre a pesquisa lá e abra o bloco de novo.
>
> **Preciso escrever as opções de nota na mensagem do bloco?** Não. As opções vêm da pesquisa e são acrescentadas automaticamente; a mensagem é só o texto que vai antes delas.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Saída sem ligação:** o cliente responde a avaliação e o fluxo para, com o atendimento aberto. **Solução:** ligue a saída do bloco a um **Encerrar** ou ao próximo passo do fluxo.
>
> **Esquecer quem não responde:** o fluxo fica parado esperando a nota. **Solução:** preencha **Sem resposta** com alguns minutos e ligue essa saída também.
