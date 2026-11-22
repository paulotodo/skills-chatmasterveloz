# Enviar figurinha

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-enviar-figurinha
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Enviar figurinha

---

🧩 O bloco **Enviar Figurinha** manda ao cliente uma figurinha da biblioteca da empresa, no meio do fluxo. É o toque leve numa conversa automática: um *obrigado* animado depois do pedido, um *bom dia* com a cara da marca.

As figurinhas vêm do menu **Figurinhas**, onde ficam organizadas em pastas.

**🏷️ Categoria: Mensagem**

Ideal para:

☑️ **Tom da marca:** reforça a identidade da empresa com figurinhas próprias.

☑️ **Agradecimento:** fecha uma etapa do fluxo de um jeito mais humano.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Cadastre as figurinhas no menu **Figurinhas**.
>
> ➡️ No menu **FlowBuilder Nativo**, abra o fluxo, clique no **+** e escolha **Enviar Figurinha**.
>
> ➡️ Escolha a figurinha e clique em **Adicionar**.

## Como configurar o bloco Enviar Figurinha

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Enviar Figurinha**

A janela **Adicionar bloco: Enviar Figurinha** mostra as figurinhas da biblioteca da empresa. Escolha uma e clique em **Adicionar**.

Sem nenhuma figurinha cadastrada, a janela avisa *Nenhuma figurinha cadastrada. Peça a um administrador para criar as pastas em Figurinhas.*

## Em quais conexões a figurinha é enviada

O bloco **Enviar Figurinha** envia a figurinha nas conexões **WhatsApp QRCode** e **WhatsApp Oficial**.

⚠️ Nos outros canais, o bloco é pulado: o fluxo segue para o próximo passo, sem enviar nada ao cliente, e registra um aviso no log do fluxo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente não recebeu a figurinha do bloco Enviar Figurinha. Por quê?** A conversa estava num canal que não recebe figurinha pelo fluxo. O bloco só envia nas conexões **WhatsApp QRCode** e **WhatsApp Oficial**; nos outros, ele é pulado e o fluxo continua.
>
> **A janela do bloco Enviar Figurinha está vazia.** A empresa ainda não tem figurinhas. Um administrador precisa criar as pastas e as figurinhas no menu **Figurinhas**.
>
> **O fluxo para quando a figurinha não pode ser enviada?** Não. O bloco é pulado e o fluxo segue para o próximo passo.
