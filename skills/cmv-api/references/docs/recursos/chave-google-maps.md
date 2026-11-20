# Chave Google Maps

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/chave-google-maps
- **Categoria:** Recursos
- **Menu:** Integrações › Chave Google Maps

---

🧩 A **Chave da API do Google** troca o mapa do rastreio da entrega pelo **Google Maps**. É o mapa que o cliente vê ao acompanhar a entrega e que a loja vê no **Mapa dos entregadores**, se o PDV estiver disponível no seu plano.

A chave é opcional: com o **OpenStreetMap (grátis)**, o rastreio funciona sem chave nenhuma. A Chave da API do Google só é necessária para usar o Google Maps.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ No Google Cloud, crie um projeto, ative o faturamento e as APIs do Maps.
>
> ➡️ Crie a **Chave de API** e restrinja ao endereço do seu painel.
>
> ➡️ Na plataforma, acesse o menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**, escolha **Google Maps** em **Mapa do rastreio da entrega**, cole a chave em **Chave da API do Google** e clique em **Salvar**.

## Como criar a chave no Google Cloud

➡️ Entre em [https://console.cloud.google.com](https://console.cloud.google.com) com a conta Google da empresa.

➡️ Crie um projeto novo ou escolha um que já exista.

➡️ Ative o faturamento do projeto: o Google pede uma forma de pagamento para liberar as APIs do Maps.

➡️ Em **APIs e serviços → Biblioteca**, ative as APIs **Maps JavaScript**, **Geocoding** e **Distance Matrix**.

➡️ Em **APIs e serviços → Credenciais**, clique em **Criar credenciais → Chave de API** e copie a chave.

⚠️ O Google marcou a **Distance Matrix API** como legada em março de 2025, e em projeto novo ela pode não aparecer para ativar.

## Restrinja a chave

⚠️ A chave aparece para o cliente no rastreio da entrega. Sem restrição, qualquer pessoa que copiar a chave usa a sua cota do Google.

🔘 **Restrições de aplicativos:** escolha **Sites** e inclua o endereço do seu painel, o mesmo que você usa para entrar na plataforma.

🔘 **Restrições de API:** escolha as três APIs ativadas acima.

## Como integrar o Google Maps à nossa plataforma

Acesse o menu **Configurações  ›  Opções  ›  Vendas**, seção **PDV**. No índice do topo da aba, **Mapa do rastreio da entrega** leva direto ao bloco.

🔘 **Mapa do rastreio da entrega:** escolha **Google Maps**.

🔘 **Chave da API do Google:** cole a chave e clique em **Salvar**.

⚠️ Só o administrador da empresa muda essa opção.

## Custo

O Google cobra pelo uso das APIs do Maps, com uma cota gratuita por mês em cada API. O valor e a cota estão no próprio Google Cloud, e a cobrança é feita na conta Google dona da chave. Para não ter custo nenhum, use o **OpenStreetMap (grátis)**.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Preciso da Chave da API do Google para o rastreio da entrega funcionar?** Não. Com o **OpenStreetMap (grátis)** em **Mapa do rastreio da entrega**, o rastreio funciona sem chave.
>
> **Escolhi o Google Maps e o mapa do rastreio não aparece. O que conferir?** No Google Cloud, confira se o faturamento do projeto está ativo, se as APIs estão ativadas e se a restrição de **Sites** inclui o endereço do seu painel.
>
> **Quem paga o uso do Google Maps?** A conta Google dona da chave, dentro do projeto em que a chave foi criada.
