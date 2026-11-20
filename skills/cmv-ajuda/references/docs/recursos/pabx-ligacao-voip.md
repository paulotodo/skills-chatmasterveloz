# PABX -> Ligação VoIP

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pabx-ligacao-voip
- **Categoria:** Recursos
- **Menu:** Ligações › PABX -> Ligação VoIP

---

🧩 **A Integração de um Tronco VoIP** permite que a sua empresa receba e faça ligações telefônicas normais (para telefones fixos e celulares comuns) utilizando a internet, através de uma operadora SIP (como BRDID, Vono, Locaweb, etc.). Ao configurar este tronco, os seus atendentes poderão ligar para qualquer número no Brasil diretamente pela tela da nossa plataforma.

☑️ **Telefonia Convencional:** Faça e receba chamadas de e para telefones fixos ou celulares em qualquer lugar do mundo.

☑️ **Gestão Integrada:** toda chamada passa pelo PABX e pode ser atendido pelo painel WebRTC da nossa plataforma.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ **(PABX):** Crie um novo **Tronco** e insira as credenciais fornecidas pela sua Operadora VoIP.
>
> ➡️ **(PABX):** Crie uma **Rota de Entrada** para definir onde vai tocar quando um cliente ligar para o seu número.
>
> ➡️ **(PABX):** Crie uma **Rota de Saída** para permitir que seus ramais liguem para clientes usando essa operadora.

> **[PREREQUISITO]**
>
> #### Pré-requisito
>
> É recomendável que você já tenha previamente configurado os ****Ramais**** de sua equipe em seu PABX e na plataforma.

### ⚡ 1. **CRIANDO O TRONCO (A Conexão com a Operadora)**

Em seu **PABX** acesse a área de **Troncos** e adicione um novo.

🔘 **Nome:** Ex: "Tronco Voip".

🔘 **Provedor:** nome da sua operadora (ex: "BRDID").

🔘 **Credenciais (O Segredo):** 🎯 Preencha os campos Host, Porta, Usuário e Senha **exatamente com os dados que você copiou do Provedor SIP**. (Porta geralmente 5060).

🔘 **Tipo:** Selecione **PJSIP**.

🔘 **Direção:** Selecione **Ambos.**

🔘 **Codecs:** Digite **opus,ulaw,alaw**

🔘 **Transporte:** Selecione **UDP (padrão)**.

![imagem](https://clihelper.chatmasterveloz.com/docs-imagem/29081-pabx-tronco-voip-operadora.jpg)

### ⚡ **2. ROTA DE ENTRADA (para receber chamadas)**

Em seu **PABX** acesse a área de **Rotas de Entrada** para dizer ao sistema o que fazer quando o número tocar.

🔘 **Nome:** Ex: "Rota de Entrada VoIP".

🔘 **Número DID:** Insira o número DID da operadora. ***Dica**: Se digitar **s**, essa rota servirá como rota padrão para capturar qualquer chamada que chegar nesse tronco*.

🔘 **Tronco:** Selecione o "Tronco VoIP" que você acabou de criar.

🔘 **Tipo Destino:** Escolha para onde a chamada vai. Pode ser Ramal, URA, etc.

### ⚡ 3. **ROTA DE SAÍDA (para realizar chamadas)**

Em seu **PABX** acesse a área de **Rotas de Saída**.

🔘 **Nome:** Ex: "Rota de Saída VoIP".

🔘 **Pattern (Padrão):** Defina o prefixo de discagem desse número. (ex: _1.)

🔘 **Prefix:** Determina a quantidade de dígito inicial que será suprimida do número discado. No caso do VOIP temos que tirar o DDD (no caso do Brasil são 2 dígitos) e também o(s) dígito(s) do Pattern. Então: Digite 3 se o seu **Pattern** for de _1. a _9. Digite 4 se o seu seu **Pattern** for de _10. a _99. Digite 5 se o seu seu **Pattern** for de _100. a _999. ... e assim sucessivamente.

🔘 **Formato do Número:** Escolha a regra de formatação: **DDD + 9º digito (garante 9 em celular, sem cod. país)**.

🔘 **Tronco Principal:** Selecione o "Tronco Voip".

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Posso ter mais de um Tronco VoIP?** Sim! Você pode ter um tronco da Operadora A para ligar para fixo (mais barato) e um da Operadora B para ligar para celular. Para isso, basta criar duas Rotas de Saída com Patterns diferentes (ex: _2. para a primeira e _3. para a segunda).
>
> **Preciso colocar "Ambos" na direção do tronco?** Geralmente sim, se for um número principal. Mas se você contratou um pacote de telefonia na operadora apenas para disparar ligações (sem receber), você pode configurar a direção como "Saída".

> **[ERROS]**
>
> #### Erros Comuns
>
> **Errar o Host ou a Senha:** É o motivo mais comum para o tronco não ficar "Online" no Status SIP. Copie e cole os dados fornecidos pela sua operadora SIP com cuidado, garantindo que não há espaços em branco sobrando no início ou no final.
>
> **Formato de Número Inválido:** Algumas operadoras exigem que o número seja enviado com o código do país (55), outras exigem apenas o DDD (ex: 11).
