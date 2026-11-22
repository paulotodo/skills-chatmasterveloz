# Pixel Meta

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-pixel-meta
- **Categoria:** Recursos
- **Menu:** FlowBuilder Nativo › Blocos › Pixel Meta

---

🧩 O bloco **Pixel META** envia um evento para a Meta quando o cliente passa por aquele ponto do fluxo: um cadastro feito, uma compra, um lead qualificado. Com esses eventos, a Meta otimiza os anúncios, entende o público que converte e encontra pessoas parecidas.

O bloco trabalha em dois formatos: o **Site**, que é o Pixel de sempre, e as **Mensagens do WhatsApp**, para conversas que vieram de anúncio.

**🏷️ Categoria: Dados - Integração**

![Bloco Pixel META no construtor de fluxos](https://clihelper.chatmasterveloz.com/docs-imagem/24093-bloco-pixelMeta.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Pixel META**.
>
> ➡️ Escolha o **Formato do evento**, preencha os campos e clique em **Adicionar**.

## Formato Site (o Pixel de sempre)

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Pixel META**

![Campos de configuração do bloco Pixel META: Access Token, Pixel ID, Nome do Evento, Custom Data e Source](https://clihelper.chatmasterveloz.com/docs-imagem/24093-bloco-pixelMeta-config.jpg)

🔘 **Access Token:** o token da Meta.

🔘 **Pixel ID:** o identificador do pixel.

🔘 **Nome do Evento:** escrito exatamente como na documentação da Meta, como **Lead**, **CompleteRegistration**, **AddToWishlist**, **AddToCart** ou **Purchase**. A lista completa fica em [https://developers.facebook.com/docs/meta-pixel/reference](https://developers.facebook.com/docs/meta-pixel/reference).

🔘 **Custom Data:** o JSON com as propriedades do evento. No **Purchase**, `currency` e `value` são obrigatórios:

```json
{
    "value": 115.00,
    "currency": "BRL"
}
```

🔘 **Source:** de onde o evento é enviado: website, server, crm ou o nome da plataforma, Chat Master Veloz.

No desenho, o bloco no formato **Site** tem **uma saída**: o fluxo segue para o próximo passo.

## Formato Mensagens do WhatsApp

Para conversas que chegaram por um anúncio de clique para o WhatsApp, escolha **Mensagens do WhatsApp** em **Formato do evento**.

🔘 **Evento:** **Lead (LeadSubmitted)** ou **Lead qualificado (QualifiedLead)**.

Neste formato o bloco tem **duas saídas**, e o fluxo decide na hora:

🔘 **Elegível:** o evento entrou na fila de envio à Meta.

🔘 **Não elegível:** o evento não pode ser enviado. Acontece quando o atendimento não veio de anúncio, quando a conexão não é **WhatsApp Oficial**, ou quando aquele evento já tinha sido enviado para o mesmo clique.

⚠️ **O fluxo não espera a resposta da Meta.** Passar por **Elegível** quer dizer que o evento foi aceito para envio, não que a Meta já o recebeu. O desfecho de cada tentativa fica no **Registro do atendimento** e no menu **Logs Pixel (META)**.

➡️ Use a saída **Não elegível** para o plano B: seguir o fluxo sem a conversão, avisar uma equipe, marcar uma tag de controle. Sem ela ligada, o fluxo para ali para quem não veio de anúncio.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Qual formato do Pixel META eu uso?** **Site** para o Pixel tradicional, com token e ID do pixel. **Mensagens do WhatsApp** para marcar como lead ou lead qualificado quem chegou por um anúncio de clique para o WhatsApp.
>
> **O que significa a saída Não elegível do Pixel META?** Que aquele evento não podia ser enviado: o atendimento não veio de um clique em anúncio, a conexão não é **WhatsApp Oficial**, ou o evento já tinha sido enviado para o mesmo clique. O motivo exato fica no Registro do atendimento. Essa saída só existe no formato **Mensagens do WhatsApp**.
>
> **O fluxo trava esperando a Meta responder?** Não. O bloco entrega o evento para a fila de envio e o fluxo segue na mesma hora.
>
> **O bloco Pixel META faz a mesma coisa que o Pixel na tag?** O gatilho é que muda: na tag, o evento é enviado quando a etiqueta é marcada; no bloco, quando o contato passa por aquele ponto do fluxo. O destino na Meta é o mesmo.
