# Token da Empresa em Configurações

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/token-da-empresa-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Token da Empresa em Configurações

---

🧩 O **Token da Empresa** é uma credencial única, válida para a empresa inteira, que funciona em todas as APIs que aceitam o token da Conexão — e algumas chamadas só aceitam ele. Com ele você guarda um token só no seu sistema, em vez de um para cada Conexão — e, em troca, passa a dizer na chamada por qual Conexão ela deve sair.

Ideal para:

☑️ **Integração que fala por várias Conexões:** um token só no seu código, em vez de um por Conexão.

☑️ **Trocar a Conexão sem mexer na credencial:** a Conexão vira um dado da chamada, não a chave de acesso.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Token da Empresa**.
>
> ➡️ Clique em **GERAR UM NOVO** e depois em **COPIAR**.
>
> ➡️ Use o token no cabeçalho `Authorization: Bearer <token>` e informe a Conexão em toda chamada, menos nas que só aceitam o Token da Empresa e na que lista as Conexões da empresa.

## Como gerar, copiar e revogar

Acesse o menu **Configurações  ›  Token da Empresa**

🔘 **GERAR UM NOVO:** cria o token da empresa. **O token anterior para de funcionar na hora.**

🔘 **COPIAR:** copia o token exibido no campo.

🔘 **REVOGAR:** invalida o token atual, que **para de funcionar na hora**. **Revogar não mexe em nenhuma Conexão** — os tokens de Conexão seguem funcionando como antes.

⚠️ **Este token vale por toda a empresa.** Quem o tiver pode falar por qualquer Conexão dela. Guarde-o como guarda uma senha, e revogue na hora se desconfiar que vazou.

⚠️ **Existe um token de cada vez.** Tanto gerar quanto revogar derrubam o token anterior imediatamente.

## Como informar a Conexão na chamada

Com o Token da Empresa, **informar a Conexão é obrigatório em toda chamada — menos nas que só aceitam este token**, que não passam por Conexão nenhuma e vão sem ela.

➡️ Informe **`whatsappId`**, **`connectionId`** ou **`whatsappName`** — na query string (ex.: `?connectionId=67`) ou no corpo da requisição (ex.: `"connectionId": "67"`).

➡️ Para indicar a Conexão pelo **nome** em vez do id, use `whatsappName`. Na query string, o espaço do nome precisa ir escrito como `%20` — por exemplo, `?whatsappName=Ag%20Oficial`.

➡️ Em envio com arquivo, use a query string.

◽ Sem esse dado a chamada é recusada com **400**, e a resposta diz o que está faltando.

◽ **A chamada que lista as Conexões da empresa também vai sem Conexão.** Com o Token da Empresa, o `POST /api/whatsapp-status` traz todas as Conexões da empresa, com o id de cada uma — é por ela que a sua integração descobre os ids que vai usar nas outras chamadas. Se você informar uma Conexão nessa chamada, ela precisa ser desta empresa.

A tela do **Token da Empresa** traz a lista **Conexões desta empresa**, com o **ID**, o **Nome** e a **Situação** de cada uma. São esses os valores a usar na chamada.

## Token da Empresa e Token da Conexão convivem

➡️ **Nada muda para quem usa o token da Conexão.**

◽ A exceção são as chamadas que só aceitam o Token da Empresa — o artigo de cada uma avisa logo no início.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Gerar um novo token invalida o anterior?** Sim. Gerar e revogar derrubam o token antigo na hora — existe um de cada vez.
>
> **Revogar o Token da Empresa derruba as minhas integrações?** Só as que usam esse token. Nenhuma Conexão é alterada, e o que usa token de Conexão segue funcionando.
>
> **Posso usar os dois ao mesmo tempo?** Pode. São credenciais independentes, e numa chamada em que as duas apareçam vale a Conexão.
>
> **Onde eu acho o ID da Conexão?** Na tela do **Token da Empresa**, na lista **Conexões desta empresa**. Pela API, o `POST /api/whatsapp-status` com o Token da Empresa traz todas as Conexões com o id de cada uma, sem precisar informar Conexão nenhuma.

> **[ERROS]**
>
> #### Erros Comuns
>
> **A chamada volta com erro 400 pedindo a Conexão:** você autenticou com o Token da Empresa e não informou `whatsappId`, `connectionId` ou `whatsappName`. Acrescente o parâmetro na query string ou no corpo da requisição.
>
> **A lista de Conexões volta com 400 "Conexão não encontrada nesta empresa":** a chamada que lista as Conexões (`/api/whatsapp-status`) recebeu o id de uma Conexão que foi apagada ou é de outra empresa. Com o Token da Empresa essa chamada não precisa de Conexão: tire o parâmetro.
>
> **A chamada volta com 401 "Acesso não permitido" mesmo com o token certo de uma Conexão:** ela é das que só aceitam o Token da Empresa — o artigo dela avisa logo no início. Use o Token da Empresa, sem informar a Conexão.
>
> **As integrações pararam logo depois de você mexer no Token da Empresa:** gerar um novo token ou revogar derruba o anterior imediatamente. Cole o token novo no seu sistema para elas voltarem.
