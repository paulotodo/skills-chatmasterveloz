# Pixel da Meta e Google Analytics nas Páginas Externas

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pixel-da-meta-e-google-analytics-nas-paginas-externas
- **Categoria:** Recursos
- **Menu:** Configurações › Integrações e segurança em Configurações › Pixel da Meta e Google Analytics nas Páginas Externas

---

🧩 Você anuncia no Facebook, no Instagram ou no Google e não sabe quantas pessoas chegaram às páginas da empresa, nem o que fizeram lá? Sem medição, a campanha que trouxe clientes e a que só gastou ficam iguais no relatório do anúncio.

As seções **Pixel da Meta** e **Google Analytics nas páginas externas** ligam as páginas externas da empresa — as páginas públicas que o cliente abre sem login — ao pixel da Meta e ao Google Analytics 4. Um **ID do pixel** e um **ID de métricas** valem para todas as páginas externas da empresa, e cada página pode ficar de fora da medição.

Ideal para:

☑️ **Medição das campanhas:** Leva ao Gerenciador de Eventos da Meta e ao Google Analytics as visitas das páginas externas e o que o cliente fez nelas.

☑️ **Medição por página:** Tira da conta só a página que não deve ser medida, sem mexer nas outras.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**.
>
> ➡️ Na seção **Pixel da Meta**, preencha o **ID do pixel**, desmarque em **Páginas que rastreiam** a página que não deve ser medida e clique em **Salvar pixel**.
>
> ➡️ Na seção **Google Analytics nas páginas externas**, preencha o **ID de métricas (G-XXXXXXXXXX)**, desmarque em **Páginas que medem** a página que não deve ser medida e clique em **Salvar Google Analytics**.

## Pixel da Meta

Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Pixel da Meta**. O pixel serve ao Facebook e ao Instagram Ads, e um **ID do pixel** vale para todas as páginas externas da empresa.

🔘 **ID do pixel:** só números, de 5 a 20. Nas palavras da tela, o ID *"Fica no Gerenciador de Eventos da Meta."* O campo apaga sozinho o que não é número.

🔘 **Token da API de Conversões (opcional):** o token da API de Conversões, copiado do Gerenciador de Eventos da Meta. Depois de salvo, o token não aparece mais: o campo fica vazio, com *Token guardado* escrito no fundo, e a ajuda passa a dizer *"Já existe um token guardado. Preencha só para trocar."* O botão **Apagar token** tira o token guardado.

🔘 **Código de teste (opcional):** só letras e números. Nas palavras da tela: *"O código da aba Testar eventos, para conferir no Gerenciador. Apague depois de testar."*

🔘 **Páginas que rastreiam:** uma caixa para cada página externa — *Cardápio digital*, *Loja digital*, *Link na Bio*, *Reservas*, *Link de agendamento* e *Rastreio do pedido*. A página desmarcada não carrega o pixel.

🔘 **Salvar pixel:** grava a seção, com o aviso *"Pixel da Meta salvo."*

## Google Analytics nas páginas externas

Acesse o menu **Configurações  ›  Opções  ›  Integrações e segurança**, seção **Google Analytics nas páginas externas**. A medição vai para o Google Analytics 4, e um **ID de métricas** vale para todas as páginas externas da empresa.

🔘 **ID de métricas (G-XXXXXXXXXX):** o ID que começa com **G-**. Nas palavras da tela, ele *"Fica no Google Analytics em Administrador → Fluxos de dados → o seu site."* O campo passa as letras para maiúsculas e apaga o que não é letra, número ou hífen.

🔘 **Páginas que medem:** as mesmas páginas da lista do pixel, cada uma com a sua caixa. A página desmarcada não carrega o Google Analytics.

🔘 **Salvar Google Analytics:** grava a seção, com o aviso *"Google Analytics salvo."*

As duas listas são independentes: uma página pode ficar fora do pixel e continuar medida no Google Analytics, ou o contrário.

## O que cada página externa mede

Com o **ID do pixel** e o **ID de métricas** preenchidos, cada página marcada envia:

➡️ **Em todas as páginas:** cada visita conta no pixel como *PageView* e no Google Analytics como *page_view*.

➡️ **Cardápio digital** e **Loja digital:** conforme o cliente abre um produto, põe na sacola e abre a sacola, o pixel recebe *ViewContent*, *AddToCart* e *InitiateCheckout*, e o Google Analytics, *view_item*, *add_to_cart* e *begin_checkout*.

➡️ **Link na Bio:** cada toque num botão conta como contato — *Lead* no pixel e *generate_lead* no Google Analytics, com o texto do botão.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preciso de um pixel da Meta para cada página externa?** Não. Um **ID do pixel** vale para todas as páginas externas da empresa. Para tirar uma página da medição, desmarque-a em **Páginas que rastreiam** e clique em **Salvar pixel**.
>
> **Desmarquei uma página em Páginas que rastreiam. Ela fica fora do Google Analytics também?** Não. As listas **Páginas que rastreiam** e **Páginas que medem** são independentes: cada uma vale só para a sua seção.
>
> **O Token da API de Conversões aparece de novo depois de salvo?** Não. O campo fica vazio, com *Token guardado* no fundo. Para trocar, preencha o token novo e salve; para tirar, clique em **Apagar token**.
>
> **Dá para usar um ID do Google Analytics que começa com UA-?** Não. O **ID de métricas** é o do Google Analytics 4 e começa com **G-**, como *G-AB12CD34EF*.
>
> **Como paro de medir as páginas externas?** Apague o **ID do pixel** e clique em **Salvar pixel**; apague o **ID de métricas** e clique em **Salvar Google Analytics**. Sem os IDs, as páginas deixam de carregar o pixel e o Google Analytics.
>
> **Onde fica o Pixel da Meta nas Configurações?** Na aba **Integrações e segurança**, logo depois de **Webhooks e integrações**, e o **Google Analytics nas páginas externas** vem em seguida. A busca das Configurações também leva até lá: *pixel*, *API de Conversões* ou *Google Analytics* mostram o caminho *Integrações e segurança › Pixel da Meta*.

> **[ERROS]**
>
> #### Erros Comuns
>
> **A tela mostra "O ID do pixel tem só números (de 5 a 20).":** o **ID do pixel** está curto ou longo demais. **Solução:** copie o ID de novo no Gerenciador de Eventos da Meta.
>
> **A tela mostra "O token da API de Conversões não parece válido. Copie de novo no Gerenciador de Eventos.":** o texto colado no **Token da API de Conversões** não foi aceito. **Solução:** copie o token de novo no Gerenciador de Eventos da Meta.
>
> **A tela mostra "O código de teste tem só letras e números.":** o **Código de teste** tem hífen, espaço ou outro sinal. **Solução:** copie o código da aba *Testar eventos* do Gerenciador de Eventos, só com as letras e os números.
>
> **A tela mostra "O ID de métricas começa com G- (por exemplo, G-AB12CD34EF).":** o ID é de outro formato, como um antigo *UA-*, ou está incompleto. **Solução:** copie o ID de métricas no Google Analytics 4, em *Administrador → Fluxos de dados → o seu site*.
