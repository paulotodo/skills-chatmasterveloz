# Retornar último atendimento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-retornar-ultimo-atendimento
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Retornar último atendimento

---

🧩 O bloco **Retornar último atendimento** devolve o cliente para onde ele estava no atendimento anterior: o mesmo **Setor**, o mesmo atendente e a mesma situação. É o atalho para quem volta a falar pouco depois de encerrar e não precisa passar de novo pelo menu.

**🏷️ Categoria: Atendimento - Finalização**

Ideal para:

☑️ **Cliente que voltou logo:** junto com a condição **Protocolo fechado**, leva quem voltou há pouco direto para quem já estava atendendo.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo, clique no **+** e escolha **Retornar último atendimento**.
>
> ➡️ O bloco entra direto no desenho — não há janela para preencher.
>
> ➡️ Ligue a saída **Sem atendimento anterior** ao caminho de quem não tem atendimento anterior.

## Como usar o bloco Retornar último atendimento

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Retornar último atendimento**

🔘 **Sem campos:** o bloco não abre janela. O clique na paleta já o coloca no desenho.

🔘 **Sem atendimento anterior:** a saída do bloco, para o contato que não tem um atendimento anterior para onde voltar.

◽ Com atendimento anterior, o cliente volta ao Setor, ao atendente e à situação daquele atendimento.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O bloco Retornar último atendimento tem configuração?** Não. Ele não abre janela: o que ele faz depende só do último atendimento do contato.
>
> **E se o cliente nunca foi atendido?** O fluxo segue pela saída **Sem atendimento anterior**. Ligue essa saída ao caminho de sempre — o menu, por exemplo.
>
> **Como saber se o cliente voltou há pouco tempo?** Antes deste bloco, use a condição **Protocolo fechado**, com **há menos de** e o tempo que faz sentido para você.
