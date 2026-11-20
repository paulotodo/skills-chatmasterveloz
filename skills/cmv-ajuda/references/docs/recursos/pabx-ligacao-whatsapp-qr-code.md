# PABX -> WhatsApp (QR Code)

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pabx-ligacao-whatsapp-qr-code
- **Categoria:** Recursos
- **Menu:** Ligações › PABX -> WhatsApp (QR Code)

---

🧩 **A Integração WhatsApp + PABX** permite que o seu número de WhatsApp conectado via QR Code receba e realize chamadas através do Chat Master Veloz .

☑️ Isso significa que, se um cliente fizer uma **chamada de voz ou áudio** pelo WhatsApp, ela tocará também na plataforma.

☑️ E o atendente também poderá usar o sistema para ligar de volta para o cliente pela plataforma, sem precisar de aparelhos físicos.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ **Fase 1 (PABX):** Acesse a opção “WhatsApp QR Code”, adicione um novo e copie a senha gerada.
>
> ➡️ **Fase 2 (Plataforma):** No menu **Conexões**, clique no ícone de telefone verde. Preencha o “Servidor SIP (Saída)” com a senha gerada no PABX e copie os dados gerados no “Listener SIP”.
>
> ➡️ **Fase 3 (PABX):** Crie um **Tronco** usando as credenciais do Listener.
>
> ➡️ **(PABX):** Crie a **Rota de Saída** para permitir que o ramal ligue para fora usando o WhatsApp.

> **[PREREQUISITO]**
>
> #### Pré-requisito
>
> É recomendável que você já tenha previamente configurado os ****Ramais**** de sua equipe em seu PABX e na plataforma.

## **Integrando WhatsApp QR Code no PABX**

### ⚡ 1**. ADICIONANDO O WHATSAPP (para receber chamadas)**

Em seu **PABX** acesse o menu **WhatsApp (QR Code)** para adicionar um novo WhatsApp.

🔘 Defina um **Nome** e uma descrição qualquer.

🔘 Defina o **Tipo de Destino** para definir a **Rota de Entrada** desse WhatsApp.

🔘 **Codecs:** Digite **opus,ulaw,alaw**

Após **salvar**, o sistema irá gerar as:

◽ **Credenciais SIP:** um **Username** e uma **Senha**.

***✍️ Ação:* Copie essas informações, para colar na plataforma.**

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/28964-pabx-whatsapp-qrcode.jpg)

### ⚡ **2. CRIANDO A PONTE (PABX <-> **Chat Master Veloz**)**

Em nossa plataforma, acesse o menu → Conexões e localize **ícone de Telefone (Verde)** no rodapé da conexão para abrir a "Configuração SIP - Pro" de seu WhatsApp QR Code.

🔘 **Status SIP:** Ative a chave para habilitar o SIP nesta conexão.

**SERVIDOR SIP (Saída)**

🔘 **Servidor SIP:** pabx.ligacaonozap.com:5060

🔘 **Usuário e Senha SIP: 🎯 cole o username e senha copiados do WhatsApp criado no PABX no passo 1.**

🔲 Clique em **Salvar**

**LISTENER SIP (Entrada)**

🔲 Clique novamente no **ícone de Telefone (Verde)** no rodapé da conexão.

O sistema gerou automaticamente as credenciais que o seu PABX precisa para se conectar.

◽ **Host (IP)** e **Porta, Usuário** e **Secret do Listener**.

***✍️ Ação:* Copie essas informações, para colar no Tronco do PABX.**

![PABX Integração - Configurações SIP](https://clihelper.chatmasterveloz.com/docs-imagem/28964-pabx-config-sip.jpg)

### ⚡ **3. CRIANDO O TRONCO (A Conexão com o WhatsApp)**

Novamente em seu **PABX** acesse a área de **Troncos** e adicione um novo.

🔘 **Nome:** Ex: "Tronco WhatsApp QR Code".

🔘 **Provedor:** Digite whatsapp.

🔘 **Credenciais (O Segredo):** 🎯 Preencha os campos Host, Porta, Usuário e Senha **exatamente com os dados que você copiou do Listener SIP** da conexão WhatsApp da nossa plataforma no Passo 2.

🔘 **Tipo:** Selecione **PJSIP**.

🔘 **Direção:** Selecione **Ambos**.

🔘 **Codecs:** Digite **opus,ulaw,alaw**

🔘 **Transporte:** Selecione **UDP (padrão)**.

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/28964-pabx-tronco-wppqrcode.jpg)

### ⚡ **4. ROTA DE SAÍDA (para realizar chamadas)**

Em seu **PABX** acesse a área de **Rotas de Saída**.

🔘 **Pattern (Padrão):** Defina o prefixo de discagem desse número. (ex: _2.)

🔘 **Prefix:** Determina a quantidade de dígito inicial que será suprimida do número discado. Digite 1 se o seu **Pattern** for de _1. a _9. Digite 2 se o seu seu **Pattern** for de _10. a _99. Digite 3 se o seu seu **Pattern** for de _100. a _999. ... e assim sucessivamente.

🔘 **Formato do Número:** Escolha a regra de formatação: **Nenhum (enviar como discado)**.

🔘 **Tronco Principal:** Selecione o "Tronco WhatsApp".

Em nossa plataforma, acesse o menu → Conexões > Editar > Integrações e no campo **Prefixo Voip** digite o número definido em Pattern da Rota de Saída do PABX (em nosso exemplo: 2)

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Por que preciso de duas senhas (Saída e Listener)?** Como o VoIP exige segurança máxima, criamos uma via de duas mãos: uma senha serve para o PABX ter permissão de acessar a plataforma, e a outra serve para a plataforma ter permissão de mandar a chamada para o PABX.
>
> **O cliente precisa ter internet boa para me ligar no WhatsApp?** Sim. Como a chamada é via dados (WhatsApp), a qualidade do áudio na ponta do cliente depende do 4G ou Wi-Fi dele. Já na sua ponta (PABX), garantimos a estabilidade do servidor.
>
> **Posso atender a ligação de voz pelo celular físico?** Se o PABX "puxar" a ligação para o sistema e o Ramal WebRTC atender, a chamada será tratada no computador do seu atendente.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Inverter as senhas:** Colar a senha do Listener dentro das configurações do Servidor de Saída. Lembre-se: "Saída" usa a senha gerada no PABX; "Entrada" (Listener) gera a senha que vai pro Tronco.
