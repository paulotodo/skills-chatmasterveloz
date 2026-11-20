# Enviar Localização

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-enviar-localizacao
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Enviar Localização

---

🧩 O bloco **Enviar Localização** compartilha um endereço como mapa, em vez de texto. Ao tocar, o aplicativo de mapas do cliente abre e traça a rota até o ponto, sem copiar e colar endereço no GPS.

**🏷️ Categoria: Mensagem**

Ideal para:

☑️ **Loja física e consultório:** facilitar a chegada do cliente até a porta.

☑️ **Evento:** compartilhar o local exato de uma festa ou conferência.

☑️ **Retirada e entrega:** indicar o ponto exato de coleta.

![Flowbuilder - bloco Enviar Localização](https://clihelper.chatmasterveloz.com/docs-imagem/27580-bloco-enviar-localizacao.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Enviar Localização**.
>
> ➡️ Digite o endereço, confira o ponto no mapa e clique em **Adicionar**.

## Como o mapa aparece para o cliente

O cliente recebe um mapa com o pino vermelho no local. Tocando nele, o mapa abre para navegação. A **legenda**, se configurada, aparece junto.

![FlowBuilder Bloco Enviar Localização - visão do cliente](https://clihelper.chatmasterveloz.com/docs-imagem/27580-bloco-enviar-localizaca-visao-cliente.jpg)

## Como configurar o bloco Enviar Localização

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Enviar Localização**

![FlowBuilder Formulário Bloco Localização](https://clihelper.chatmasterveloz.com/docs-imagem/27580-bloco-enviar-localizacao-formulario.jpg)

🔘 **Endereço Completo:** rua, número e cidade, obrigatório. Digite e aguarde 2 segundos: a busca é automática. Complemento, como o apartamento, fica mantido no texto.

🔘 **Buscar localização:** faz a busca na hora, sem esperar.

🔘 **Usar minha localização atual:** pega o ponto em que você está.

🔘 **Latitude** e **Longitude:** as coordenadas do ponto, obrigatórias. A busca preenche sozinha; para precisão total, cole as coordenadas do Google Maps.

🔘 **Abrir no Google Maps:** confere o ponto no mapa antes de salvar.

🔘 **Legenda (opcional):** um texto curto que acompanha o mapa, como *Nossa loja física*.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco mostra o endereço e as coordenadas, e tem uma saída para o próximo passo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente precisa ter o Google Maps para abrir a localização?** Não. O WhatsApp abre o mapa dele e oferece abrir no Google Maps, no Waze e em outros.
>
> **O bloco Enviar Localização envia localização em tempo real?** Não. Ele envia um ponto fixo, que não acompanha movimento.
>
> **O endereço não aparece na busca do bloco Enviar Localização. E agora?** Use as coordenadas. No Google Maps, clique com o botão direito no local exato, copie os números e cole em **Latitude** e **Longitude**.
