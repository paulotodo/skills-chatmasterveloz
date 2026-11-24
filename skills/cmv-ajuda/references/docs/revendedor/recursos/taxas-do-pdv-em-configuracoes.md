# Taxas do PDV em Configurações

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/taxas-do-pdv-em-configuracoes
- **Categoria:** Recursos
- **Menu:** Configurações › Taxas do PDV em Configurações

---

🧩 O card **Taxas do PDV** abre a tela onde a plataforma fica com uma parte das vendas do PDV: cada empresa pode ter uma taxa, em percentual ou valor fixo, sobre as cobranças que faz pelo Mercado Pago ou pelo Asaas, e a empresa recebe o restante. É também onde ficam a aplicação do Mercado Pago, que as empresas autorizam ao conectar a conta, e a carteira da plataforma no Asaas.

**Taxas do PDV** vale para a instância inteira, e a taxa é combinada empresa por empresa.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Taxas do PDV**.
>
> ➡️ Em **Aplicação do Mercado Pago**, preencha **Client ID** e **Client Secret**, cadastre o **Endereço de retorno** como Redirect URL na aplicação e clique em **Salvar**.
>
> ➡️ Em **Carteira da plataforma no Asaas**, preencha o **Wallet ID** e clique em **Salvar**.
>
> ➡️ Em **Taxa da plataforma no PDV**, escolha o **Tipo** e o **Valor** de cada empresa e clique em **Salvar** na linha dela.

## Aplicação do Mercado Pago

🔘 **Client ID** e **Client Secret:** as credenciais de produção da aplicação de Marketplace da plataforma no Mercado Pago (no painel do Mercado Pago, em Suas integrações, na aplicação de Marketplace, em Credenciais de produção). É essa aplicação que cada empresa autoriza ao conectar a conta dela, e é por ela que a taxa de cada venda chega à plataforma.

🔘 **Endereço de retorno (cadastre como Redirect URL na aplicação):** a plataforma já preenche este campo. Copie o endereço e cadastre como Redirect URL na mesma aplicação do Mercado Pago.

⚠️ Enquanto a aplicação não está salva, nas palavras da tela, *"Sem aplicação: as empresas ainda não conseguem conectar a conta."*

## Carteira da plataforma no Asaas

🔘 **Wallet ID:** a carteira da conta da plataforma no Asaas (no painel do Asaas, em Integrações, Chave de API, Wallet ID). É para essa carteira que vai a taxa de cada cobrança que as empresas fazem pelo Asaas, no próprio checkout do cliente.

⚠️ Sem a carteira, nas palavras da tela, *"Sem carteira: as empresas com taxa não conseguem cobrar pelo Asaas."*

## Taxa da plataforma no PDV

A tabela tem uma linha por empresa da instância, com as colunas **Empresa**, **Tipo** e **Valor**, e o botão **Salvar** de cada linha. Acima dela, **Buscar empresa** filtra as linhas.

🔘 **Tipo:** **Sem taxa**, **Percentual** (uma parte do valor de cada cobrança) ou **Valor fixo** (o mesmo valor em cada cobrança).

🔘 **Valor:** o percentual ou o valor que a plataforma fica de cada cobrança da empresa.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Defini a taxa no card Taxas do PDV. A empresa precisa fazer alguma coisa?** Para cobrar pelo Mercado Pago, cada empresa conecta a conta dela, e isso só fica possível depois que a **Aplicação do Mercado Pago** está salva em **Taxas do PDV**.
>
> **A taxa do card Taxas do PDV vale igual para todas as empresas?** Não. Cada empresa tem a sua linha na tabela, com o tipo e o valor combinados com ela, e pode ficar **Sem taxa**.
