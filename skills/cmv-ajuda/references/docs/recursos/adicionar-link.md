# Adicionar Link

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/adicionar-link
- **Categoria:** Recursos
- **Menu:** Gestão de Links › Adicionar Link

---

🧩 **Adicionar um Link** permite que você gere rapidamente URLs curtas e inteligentes para o seu WhatsApp.

☑️ **Gatilhos de Automação:** Transforme a mensagem pré-definida em um gatilho. No FlowBuilder, use um bloco de Condição para identificar essa frase exata e disparar um robô exclusivo para quem clicou naquele link.

☑️ **Experiência do Cliente:** O cliente não precisa adicionar o seu número na agenda. O link já abre o WhatsApp dele com a mensagem pronta para enviar.

☑️ **Rastreamento:** Cada link novo gerado tem o seu próprio Analytics para monitorar a quantidade e a origem dos cliques.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Gestão de Links**.
>
> ➡️ No canto superior direito, clique em **+ NOVO LINK**.
>
> ➡️ Preencha o nome de identificação, o número do seu WhatsApp (com DDI e DDD) e a mensagem.
>
> ➡️ Clique em **Criar Link** e copie a URL gerada.

## Como adicionar um Link

Acesse o menu → Gestão de Links > + Novo Link

![Formulário exemplo de como Adicionar Link](https://clihelper.chatmasterveloz.com/docs-imagem/28896-gestao-de-links-adicionar-formulario.jpg)**🔘 Nome do Link:** digite o nome do link (somente você enxerga esse nome, seu cliente não).

🔘 **Número do WhatsApp:** o número do whatsapp que receberá o contato. Siga o padrão internacional (somente números DDI DDD Número)

**🔘 Mensagem:** (opcional) defina uma mensagem inicial que virá digitada no celular do cliente. **Dica**: essa mensagem pode ser usada para iniciar um gatilho de fluxo.

⚡ **Integração com Pixel da Meta (Opcional)**

🔘 **Pixel ID:** insira o ID (identificador) do seu pixel. (**tutorial aqui**)

🔘 **Access Token:** cole o token de acesso da API de Conversões. (**tutorial aqui**)

🔘 **Link Ativo:** marque ou desmarca o status do Link.

🔲 Para finalizar, clique em **Criar Link**.

> **[DUVIDAS]**
>
> ### Dúvidas Comuns
>
> **Posso alterar o número de destino depois do link criado?** Sim! E essa é a grande mágica. Se o seu número for banido ou alterado, basta vir nesta tela de Configurações, editar o campo "Número do WhatsApp" e salvar. Sua URL curta que já está divulgada continuará a mesma, redirecionando perfeitamente para o número novo.
>
> **O cliente percebe que o link é rastreado?** O redirecionamento é quase instantâneo. O cliente clica no link curto e, em frações de segundo, já cai na tela verde do WhatsApp, proporcionando uma experiência invisível e fluida.
>
> **O link curto expira?** Não, a menos que você exclua o link ou desative a chave "Link Ativo" nas configurações.

> **[ERROS]**
>
> ## Erros Comuns
>
> **Esquecer o DDI (Código do País):** Digitar apenas o DDD e o número (ex: 11999999999). O link vai gerar um erro ao ser clicado. Lembre-se sempre de colocar o 55 na frente (se for Brasil).
>
> **Digitar traços e parênteses:** O usuário tenta formatar o número para ficar bonito (ex: 55 (11) 99999-9999). A API do WhatsApp não lê formatação, e o link irá falhar. Use **apenas números**.
>
> **Não usar a mensagem pré-definida como Gatilho:** Deixar o campo "Mensagem" em branco. Isso faz com que o cliente chegue no seu WhatsApp enviando apenas um "Oi", dificultando saber de qual campanha ele veio e impedindo que o FlowBuilder inicie uma automação específica para aquele anúncio.
