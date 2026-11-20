# Conteúdo

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-conteudo
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Conteúdo

---

🧩 O bloco **Conteúdo** envia ao cliente mensagens de texto, imagens, áudios, vídeos e arquivos.

Um mesmo bloco pode ter vários itens, enviados um depois do outro, com pausas entre eles se você quiser.

**🏷️ Categoria: Mensagem**

Ideal para:

☑️ **Mensagens de texto:** dar boas-vindas, explicar um serviço, tirar uma dúvida frequente.

☑️ **Mídia:** enviar a foto de um produto, o PDF de uma proposta, um vídeo ou um áudio gravado.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Conteúdo**.
>
> ➡️ Adicione os itens, na ordem em que devem chegar, e clique em **Adicionar**.

## Vídeo Tutorial

[Vídeo Voomly — id x0cdGaKeSFiLVqwjksG4K2MWfQAqnIwiS0JxIBIwcJbianHJd, tipo v]  

## Como configurar o bloco Conteúdo

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Conteúdo**

![FlowBuilder Formulário Bloco de Conteúdo](https://clihelper.chatmasterveloz.com/docs-imagem/ed-6ad9fb8e017fd.png)

A janela **Adicionar bloco: Conteúdo** tem um botão para cada tipo de item. Cada clique acrescenta um item ao bloco, e eles são enviados na ordem em que aparecem.

🔘 **Texto:** uma mensagem escrita. Aceita formatação do WhatsApp, como `*negrito*`, `_itálico_` e `~tachado~`, e os dados do contato, como em `olá {{firstName}}, tudo bem?`.

🔘 **Intervalo:** uma pausa, em segundos, antes do item seguinte. Serve para a mensagem seguinte não chegar colada na anterior.

🔘 **Imagem:** uma imagem em PNG ou JPG, com **Legenda (Caption)** opcional.

🔘 **Áudio:** um arquivo OGG, MP3 ou OPUS. A opção **Enviar como áudio gravado na hora** faz o áudio chegar como se tivesse sido gravado no momento.

🔘 **Vídeo:** um vídeo em MP4, com **Legenda (Caption)** opcional.

🔘 **Arquivo:** um documento, com **Legenda (Caption)** opcional. Aceita PDF, Word, Excel, PowerPoint, TXT e CSV.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco mostra o começo do conteúdo e tem uma saída para o próximo passo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso colocar vários textos no mesmo bloco Conteúdo?** Pode. Cada **Texto** vira uma mensagem, enviada uma depois da outra. Use um **Intervalo** entre elas para dar tempo de leitura.
>
> **Posso enviar um link no bloco Conteúdo?** Pode. Basta colar o endereço, começando com *https://*, no **Texto**.
>
> **Que tipos de arquivo o item Arquivo aceita?** PDF, Word, Excel, PowerPoint, TXT e CSV.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Errar o nome do dado do contato:** escrever `{{nome}}` quando o esperado é `{{firstName}}`, ou esquecer de fechar as chaves. O cliente recebe o código escrito, em vez do nome. **Solução:** confira o nome exato e as duas chaves dos dois lados.
>
> **Mídia pesada demais:** vídeos e PDFs acima de 5 MB podem falhar no envio ou não abrir no celular do cliente, que muitas vezes está no 4G. **Solução:** prefira arquivos compactados e leves.
