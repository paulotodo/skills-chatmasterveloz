# Token da Conexão

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/token-da-conexao
- **Categoria:** Recursos
- **Menu:** Integrações › Token da Conexão

---

🔑 O **token da conexão** funciona como uma **chave exclusiva**, permitindo que você acesse e gerencie uma conexão do nosso sistema (como WhatsApp) de fora da plataforma, por meio de nossas APIs, mesmo sem estar logado no sistema.  
1. Você cadastra um **token único** por conexão.
2. Esse token serve como sua **chave de acesso** para acionar a sua conexão via APIs.
3. Com o token, você pode criar integrações personalizadas, como:  
  - Enviar mensagens, arquivos, imagens
  - Realizar ações como adicionar contatos, atribuir tags, atualizar tickets, etc
  - Integrar com ferramentas externas (como bots, CRMs ou notificações automáticas).
  


## Como adicionar um Token em uma conexão

Acesse o menu **Conexões  ›  editar a Conexão  ›  campo Token**

Na janela aberta da Conexão, procure pelo campo Token, e digite um token qualquer para essa conexão.

Pode ser como desejar, mas como sugestão, utilize algo que ajude a lembrar a conexão do token.

Por exemplo:

API.NOMEDACONEXAO.4f1c2ab8d12345678

> **[ATENCAO]**
>
> #### Importante
>
> O Token deve ser único para cada conexão. **Não** utilize o mesmo token para mais de uma conexão!

#### 📌 Existe também o Token da Empresa

Um token só, válido para a empresa inteira, que funciona nas mesmas APIs — e algumas chamadas só aceitam ele: o artigo de cada uma avisa logo no início. A diferença está no que ele carrega: o token da conexão já diz por qual conexão a mensagem é enviada, e o da empresa não — com ele, é obrigatório informar a conexão em cada chamada, menos nas que só aceitam o Token da Empresa, e na que lista as conexões da empresa, que vão sem ela. Fica no menu **Configurações  ›  Token da Empresa**.
