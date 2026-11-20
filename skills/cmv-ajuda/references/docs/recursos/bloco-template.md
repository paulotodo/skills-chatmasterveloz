# Template

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-template
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Template

---

🧩 O bloco **Template** dispara uma mensagem modelo, aprovada antes pela Meta, de dentro de um fluxo automático.

É o único jeito de o fluxo falar com um cliente que não escreveu nas últimas 24 horas: fora dessa janela, mensagem livre não é entregue, e o template é o que passa. Também mantém a mensagem padronizada, porque o texto foi aprovado uma vez e chega igual em todos os envios, com apenas as variáveis mudando.

**🏷️ Categoria: Mensagem**

☑️ **Aviso fora da janela:** alcança quem parou de responder, quando a mensagem livre já não seria entregue.

☑️ **Padronização:** o texto aprovado chega igual em todos os disparos, sem depender de quem montou o fluxo.

☑️ **Personalização controlada:** as variáveis trocam nome, número do pedido ou data sem alterar o corpo aprovado.

![Bloco Enviar Template no editor do FlowBuilder](https://clihelper.chatmasterveloz.com/docs-imagem/27582-bloco-enviar-template.jpg)

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Template**.
>
> ➡️ Escolha a **Conexão WhatsApp** e o template, preencha as **variáveis** e clique em **Adicionar**.

## Como configurar o bloco Template

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Template**

![Formulário do bloco Enviar Template](https://clihelper.chatmasterveloz.com/docs-imagem/27582-bloco-enviar-template-formulario.jpg)

🔘 **Conexão WhatsApp Oficial:** a conexão por onde o disparo é enviado. A lista mostra apenas conexões do WhatsApp Oficial; sem nenhuma, a janela avisa *Nenhuma conexão WhatsApp Oficial disponível!*

🔘 **Template:** a mensagem modelo. A lista traz o nome técnico, o idioma, como `pt_BR`, e a categoria, como `UTILITY`, `MARKETING` ou `AUTHENTICATION`. Só aparecem templates aprovados pela Meta.

⚡ **Variáveis do Template:** o sistema lista os campos variáveis do modelo, como `{{1}}` e `{{2}}`, e você preenche cada um. Além de texto fixo, a variável aceita os dados do contato: `{nome}`, `{email}` e `{extra1}`, os campos que chegam pelo webhook, ou `%variavel%`, as variáveis do próprio fluxo. É o que diz a dica no rodapé da janela: *"Use {nome}, {email}, {extra1} (os campos do webhook) ou %variavel% (as do fluxo) para preencher com os dados do contato"*.

⚡ **Pré-visualização do Template:** mostra como a mensagem vai chegar, com o texto preenchido, para conferir antes de salvar.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco mostra o template e as primeiras variáveis preenchidas, e tem uma saída para o próximo passo.

⚠️ **Todo template enviado é cobrado pela Meta**, conforme a categoria dele, inclusive o de utilidade com a janela de 24 horas aberta. Em fluxos que disparam template em volume, o número de envios é decisão de custo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso mudar o texto fixo do template no bloco Template?** Não. O texto aprovado pela Meta não pode ser alterado; você só preenche as variáveis.
>
> **O bloco Template gera cobrança?** Sim. O template é cobrado pela Meta conforme a categoria dele: marketing, utilidade ou autenticação.
>
> **Posso pôr o nome do contato numa variável do bloco Template?** Sim. Escreva `{nome}` na variável, ou outro campo que chega pelo webhook, como `{email}` e `{extra1}`, ou uma variável do fluxo entre sinais de porcentagem, como `%variavel%`.
>
> **Por que aparece uma variável de cabeçalho no bloco Template?** Porque o template tem imagem ou vídeo no cabeçalho. Nesse caso aparece um campo a mais para o endereço da mídia.
>
> **O template não aparece na lista do bloco Template. Por quê?** Ou ele ainda não foi aprovado pela Meta, ou não foi sincronizado. Abra o menu **Conexões  ›  Gestão de Templates** e sincronize. A janela avisa *Nenhum template aprovado disponível para esta conexão!* quando não há nenhum.
>
> **Posso usar o bloco Template numa conexão por QR Code?** Não. A lista de conexões mostra apenas o WhatsApp Oficial, porque template é recurso do canal oficial.
