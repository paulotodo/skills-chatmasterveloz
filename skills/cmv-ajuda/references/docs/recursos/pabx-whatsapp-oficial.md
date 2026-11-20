# PABX -> WhatsApp Oficial

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pabx-whatsapp-oficial
- **Categoria:** Recursos
- **Menu:** Ligações › PABX -> WhatsApp Oficial

---

🧩 **A Integração WhatsApp Oficial + PABX** permite que o seu número de WhatsApp Oficial **Cloud** receba e realize chamadas através do Chat Master Veloz .

☑️ Isso significa que, se um cliente fizer uma **chamada de voz ou áudio** pelo WhatsApp, ela tocará também na plataforma.

☑️ E o atendente também poderá usar o sistema para ligar de volta para o cliente pela plataforma, sem precisar de aparelhos físicos.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ **(Plataforma):** No menu **Conexões**, clique no ícone de telefone verde. Ative o SIP e copie a senha gerada.
>
> ➡️ **(PABX):** Crie um novo **Tronco** e insira as credenciais fornecidas pela Meta.
>
> ➡️ **(PABX):** Crie um WhatsApp Cloud para configurar a **Rota de Entrada**.
>
> ➡️ **(PABX):** Crie a **Rota de Saída** para permitir que o ramal ligue para fora usando o WhatsApp Oficial.

> **[PREREQUISITO]**
>
> #### Pré-requisito
>
> É recomendável que você já tenha previamente configurado os ****Ramais**** de sua equipe em seu PABX e na plataforma.

## **Integrando WhatsApp Oficial no PABX**

### ⚡ 1. **CRIANDO A PONTE (PABX <-> **Chat Master Veloz**)**

Em nossa plataforma, acesse o menu → Conexões e localize **ícone de Telefone (Verde)** no rodapé da conexão para abrir a "Gerenciador SIP" de seu WhatsApp Cloud.

🔘 **Configuração do Servidor SIP:** clique em Configurar.

🔘 **Hostname do Servidor SIP:** Digite pabx.ligacaonozap.com

🔘 **Porta SIP:** 5061

🔘 Marque a opção **Habilitar chamadas de saída**

🔲 Clique em **Ativar SIP

***✍️ Ação:* Copie o Password (senha) para usar nos próximos passos.**

### ⚡ 2. **CRIANDO O TRONCO (A Conexão com a API Oficial)**

Em seu **PABX** acesse a área de **Troncos** e adicione um novo.

🔘 **Nome:** Ex: "Tronco API Oficial".

🔘 **Provedor:** Digite Meta (WhatsApp Cloud)

🔘 **Credenciais (O Segredo):** **Host**: wa.meta.vc **Porta**: 5061 **Usuário SIP**: número do whatsapp (somente número, sem + ou outro caractere especial). **Senha SIP**: gerada pela API da Meta no passo 1.

🔘 **Tipo:** Selecione **PJSIP**.

🔘 **Direção:** Selecione **Ambos**.

🔘 **Codecs:** Digite **opus**

🔘 **Transporte:** Selecione **TLS (seguro)**.

🔘 **Criptografia Mídia:** Selecione **SDES (SRTP)**.

🔘 **Habilite a opção Sem REGISTER.**

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/29852-pabx-tronco-wppoficial.jpg)

### ⚡ 3**. ADICIONANDO O WHATSAPP (para receber chamadas)**

Em seu **PABX** acesse o menu **WhatsApp (Cloud)** para adicionar um novo WhatsApp.

🔘 Digite o **Número do WhatsApp** (somente número, sem + ou outro caractere especial).

🔘 Digite a **Senha SIP Meta** gerada no passo 1.

🔘 Defina o **Tipo de Destino** para definir a **Rota de Entrada** desse WhatsApp.

### ⚡ 4. **ROTA DE SAÍDA (para realizar chamadas)**

Em seu **PABX** acesse a área de **Rotas de Saída**.

🔘 **Nome:** Ex: "Rota de Saída API Oficial".

🔘 **Pattern (Padrão):** Defina o prefixo de discagem desse número. (ex: _3.)

🔘 **Prefix:** Determina a quantidade de dígito inicial que será suprimida do número discado. Digite 1 se o seu **Pattern** for de _1. a _9. Digite 2 se o seu seu **Pattern** for de _10. a _99. Digite 3 se o seu seu **Pattern** for de _100. a _999. ... e assim sucessivamente.

🔘 **Formato do Número:** Escolha a regra de formatação: **Nenhum (enviar como discado)**.

🔘 **Tronco Principal:** Selecione o "Tronco API Oficial".

Em nossa plataforma, acesse o menu → Conexões > Editar > Integrações e no campo **Prefixo Voip** digite o número definido em Pattern da Rota de Saída do PABX (em nosso exemplo: 3)

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O cliente tem algum custo para me ligar por esse número Oficial? Não! Para o cliente final, o comportamento é exatamente igual ao de fazer uma chamada de voz tradicional pelo aplicativo do WhatsApp usando o Wi-Fi ou o 4G/5G dele.
>
> **Posso usar o mesmo prefixo de discagem (Pattern) que já uso na minha operadora VoIP? Não. Cada "Rota de Saída" precisa de um prefixo único para o PABX não se confundir. Se você já configurou o Padrão _2. para fazer ligações via operadora SIP, defina _3. ou _4. para as ligações via WhatsApp Oficial Cloud

> **[ERROS]**
>
> #### Erros Comuns
>
> **Digitar o número do WhatsApp com símbolos e espaços: Preencher o campo de "Usuário SIP" ou o cadastro do WhatsApp no PABX no formato +55 (11) 90000-0000. A Meta rejeitará a autenticação imediatamente. Você deve digitar **apenas os números** (Código do país + DDD + Número), por exemplo: 5511900000000.
>
> **Não marcar a caixa "Sem REGISTER": Diferente de uma operadora VoIP tradicional, a arquitetura em nuvem da Meta não utiliza o protocolo de "registro constante". Se você esquecer de habilitar a caixinha **Sem REGISTER** lá no final da configuração do Tronco (Passo 2), o seu PABX ficará tentando forçar um registro na Meta, e o tronco constará como falho ou "Offline".
>
> **Errar a matemática do Prefixo (Strip): Configurar o Pattern como _3. mas esquecer de colocar o número 1 na regra de exclusão do Prefix. Se você não mandar o sistema cortar o 1º dígito, ele enviará o número do cliente para a Meta com o número 3 na frente (ex: 355119999...), invalidando o destino e derrubando a sua chamada de saída.
