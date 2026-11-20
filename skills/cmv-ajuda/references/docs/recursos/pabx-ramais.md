# PABX -> Ramais

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pabx-ramais
- **Categoria:** Recursos
- **Menu:** Ligações › PABX -> Ramais

---

🧩 **O Ramal** é a linha telefônica individual de cada membro da sua equipe. Para que o seu atendente consiga fazer e receber ligações diretamente pela tela do computador (usando o fone de ouvido), precisamos criar essa "conta" no PABX e depois vinculá-la ao perfil dele dentro da nossa plataforma.

☑️ **Atendimento Integrado:** O atendente usa a nossa plataforma para fazer ligação por voz.

☑️ **Organização:** Cada atendente tem seu próprio número interno (ramal), permitindo transferências de chamadas entre a equipe.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ **(PABX):** crie um **Ramal** com o Transport WSS – WebRTC.
>
> ➡️ **(Plataforma):** Acesse o menu Equipe para configurar cada atendente a um ramal.

## Configurando a Estrutura do PABX

### ⚡ **CRIANDO O RAMAL (Quem vai atender)**

Em seu → PABX acesse a área de **Ramais** e adicione um Novo Ramal. (Crie um ramal para cada atendente.)

🔘 **Número e Nome:** Defina o número (ex: 260001) e o Nome (ex: Recepção).

🔘 **Senha SIP:** Crie uma senha forte, mas sem usar caracteres especiais.

🔘 **Transport:** Como o atendente vai usar a nossa plataforma, selecione **WSS - WebRTC (Navegador)**.

🔘 **Codecs:** opus,ulaw,alaw

![PABX Ramais](https://clihelper.chatmasterveloz.com/docs-imagem/29053-pabx-ramal-novo.jpg)

### ⚡ **CONFIGURE O RAMAL NA PLATAFORMA**

Em nossa plataforma, acesse o menu → Equipe e configure os ramais desejados para cada atendente.

🔘 **Chamadas:** Realizar e Receber Chamadas.

🔘 **SIP URI:** sip:260001@pabx.ligacaonozap.com (substitua o 260001 pelo ramal desejado e configurado no PABX)

🔘 **SIP PASS:** Cole a senha definida no ramal do PABX em questão.

🔘 **Servido SIP WSS:** wss://pabx.ligacaonozap.com:8089/ws

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Dois atendentes podem usar o mesmo ramal?** Não. Cada usuário na plataforma precisa de um ramal exclusivo (ex: João usa o 260001, Maria usa o 260002).
>
> **O que é o "Transport WSS - WebRTC"?** É a tecnologia que permite ao navegador de internet (Google Chrome, etc.) usar o microfone e o fone de ouvido para fazer chamadas sem precisar instalar nenhum programa adicional no computador.
>
> **Posso usar um aparelho de telefone físico (Telefone IP) na mesa?** Pode, mas a configuração muda. Se for usar um aparelho físico, o "Transport" no PABX geralmente será UDP, e você configurará a SIP URI e Senha diretamente no aparelho (via IP), não no menu Equipe da plataforma.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Não usar WebRTC no Ramal:** Configurar o ramal do atendente como UDP no PABX. Se a equipe vai usar o painel da plataforma no navegador para falar, o ramal obrigatoriamente precisa estar configurado como **WSS - WebRTC**.
>
> **Senha com caracteres especiais:** É o erro campeão que impede o telefone de registrar. O usuário coloca uma senha como Ramal@123! no PABX. O padrão WebRTC é sensível a esses símbolos e bloqueia o login do atendente na plataforma. Use apenas letras e números.
>
> **Errar a digitação da SIP URI:** Esquecer de colocar o prefixo sip: antes do número, ou errar o domínio após o @. Se a URI não estiver perfeita (sip:ramal@dominio), a plataforma não consegue encontrar a central telefônica.
