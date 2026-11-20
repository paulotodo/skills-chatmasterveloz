# Aba VoIP / Chamadas em Equipe

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/aba-voip-chamadas-em-equipe
- **Categoria:** Recursos
- **Menu:** Equipe › Aba VoIP / Chamadas em Equipe

---

🧩 A aba **VoIP / Chamadas** liga a pessoa à telefonia: se ela pode fazer e receber ligações pela plataforma, por qual telefone e com quais dados do ramal.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Equipe**, edite a pessoa e abra a aba **VoIP / Chamadas**.
>
> ➡️ Em **Chamadas**, libere o que a pessoa pode fazer. Em **Tipo de webphone**, escolha o telefone.
>
> ➡️ Preencha os dados do ramal dela — a **Configuração SIP** no telefone nativo, ou o bloco **Webphone Widget (PBX)** no telefone da sua central. Salve.

## Os campos, na ordem da tela

🔘 **Chamadas:** o que a pessoa pode fazer com ligações. Três níveis: **Não Pode Realizar ou Receber Chamadas**, o valor de quem não usa telefonia; **Somente Receber Chamadas**, para quem atende mas não disca; e **Realizar e Receber Chamadas**, o acesso completo.

🔘 **Tipo de webphone:** **Nativo (discador da plataforma)**, o telefone embutido, ou **Widget (PBX externo)**, o telefone da sua central. Nas palavras da tela: *no modo Widget o discador nativo some do topo e do ticket — dois softphones disputariam o microfone*.

### Com o telefone nativo

🔘 **Configuração SIP:** **SIP URI**, **SIP PASS** e **Servidor SIP WSS**, os dados do ramal desta pessoa na central telefônica.

🔘 **Vídeo nas chamadas:** nas palavras da tela, *este operador liga com câmera e vê o vídeo que a central entrega. Desmarcado, as chamadas dele continuam somente de áudio — e o navegador nem pede permissão de câmera*.

### Com o widget da central

Ao escolher **Widget (PBX externo)**, a **Configuração SIP** e o **Vídeo nas chamadas** saem da tela e entra o bloco **Webphone Widget (PBX)**.

🔘 **Tenant**, **Ramal** e **Segredo (WebRTC):** os dados do ramal desta pessoa na sua central.

🔘 **Ao clicar em ligar:** **Preencher o número no discador**, que espera a pessoa clicar para ligar, ou **Discar imediatamente**, que liga assim que o botão é clicado.

🔘 **Conectar automaticamente:** nas palavras da tela, *o widget já entra registrado no PBX ao abrir o painel — e o operador começa a receber chamadas sem precisar clicar em conectar*.

🔘 **Posição na tela:** o canto em que o widget aparece, como **Inferior direito**.

⚠️ Os dados do ramal são por pessoa: cada ramal é um cadastro. Trocar a pessoa de ramal é trocar aqui, não na central.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O botão de ligar não aparece para a pessoa.** Confira, nesta ordem: **Chamadas** não está em **Não Pode Realizar ou Receber Chamadas**; os dados do ramal estão preenchidos.
>
> **Quero que a pessoa atenda ligações, mas não faça.** **Chamadas** em **Somente Receber Chamadas**.
>
> **Escolhi o widget e o discador sumiu do topo.** É o esperado. Com o widget, o discador nativo sai de cena para os dois não disputarem o microfone.
>
> **A pessoa não quer ligar com câmera.** Desmarque **Vídeo nas chamadas**, no telefone nativo. As chamadas dela ficam só de áudio.
