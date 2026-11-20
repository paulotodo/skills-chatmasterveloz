# Pixel Meta em Tags

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/pixel-meta-em-tags
- **Categoria:** Recursos
- **Menu:** Tags › Pixel Meta em Tags

---

🧩 A integração com **Pixel META em Tags** permite que o **Chat Master Veloz** envie eventos automáticos para o Facebook Ads sempre que uma tag específica for marcada. Isso funciona via API de Conversões (CAPI).

O **Pixel da Meta** é um pequeno código de **monitoramento** que deve ser inserido em algum local (website, nossa plataforma, etc), com o objetivo de enviar informações para a Meta sempre que um **evento** acontece, mapeando ações que ajudam a otimizar sua campanhas de publicidade (anúncios).

Com o Pixel Meta você consegue:

☑️ **Otimização de Anúncios:** informe ao Facebook exatamente quando um lead virou "Cliente" ou "Agendou Visita", ajudando o algoritmo a encontrar mais pessoas com esse perfil.

☑️ **Remarketing Preciso:** crie públicos personalizados de pessoas que chegaram até determinada etapa do funil (ex: tag "Interesse Enviado") para mostrar anúncios específicos para elas.

☑️ **Mensuração de ROI:** rastreie vendas e conversões que aconteceram dentro do atendimento no WhatsApp, cruzando os dados com suas campanhas de anúncios.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Tags**.
>
> ➡️ Ao adicionar ou editar uma tag, abra a aba **Pixel META** e escolha o **Formato do evento**.
>
> ➡️ No formato **Site**, preencha **Pixel ID, Access Token, Nome do Evento, Custom Data (se houver) e Source**.
>
> ➡️ No formato **Mensagens do WhatsApp**, escolha apenas o **Evento** — o resto vem da conexão.
>
> ➡️ Salve. A partir daí, quando a tag for marcada, a plataforma envia o evento à Meta.

## Os dois formatos de evento

O campo **Formato do evento** decide quem envia o evento, e é a primeira escolha da aba:

🔘 **Site (o Pixel de sempre):** você informa o seu **Pixel ID** e o seu **Access Token**, e o evento vai com o nome e os dados que você escrever. É o formato para quem já usa o Pixel no site e quer os mesmos eventos vindo do atendimento.

🔘 **Mensagens do WhatsApp:** quem envia é a **conexão do atendimento** — o token e a conta (WABA) são os dela, e você não informa nada disso na tag. Em troca, o evento vai **amarrado ao clique no anúncio** que abriu a conversa, que é como a Meta sabe qual anúncio trouxe aquele cliente.

⚠️ **Ao salvar no formato Mensagens, o Access Token, o Pixel ID, o Custom Data e o Source daquela tag são apagados.** Se você mantém as duas estratégias, use tags diferentes para cada formato.

## Quando o formato Mensagens envia, e quando não envia

No formato **Mensagens do WhatsApp** o evento só é enviado quando as três condições valem ao mesmo tempo:

▫️ o atendimento **começou por um clique em anúncio** de WhatsApp;

▫️ a conexão dele é da **API Oficial**, com a conta (WABA) e o token preenchidos;

▫️ aquele clique **ainda não recebeu** esse evento.

Os eventos disponíveis são três: **Lead (LeadSubmitted)**, **Lead qualificado (QualifiedLead)** e **Venda (Purchase)**.

O resultado de cada tentativa aparece no **Registro do atendimento** e no menu **Logs Pixel (META)**, com a situação — **Na fila**, **Enviando**, **Enviado**, **Não enviado** ou **Falhou** — e o motivo quando o evento não foi enviado.

## Como testar antes de valer

No cadastro da conexão existe o campo **Código de teste da Meta (Test Events)**. Com ele preenchido, os eventos no formato Mensagens **daquela conexão** são enviados como teste e aparecem no Gerenciador de Eventos da Meta sem contar nas campanhas.

⚠️ **Apague o código depois do teste.** Enquanto ele estiver lá, nenhum evento daquela conexão conta de verdade.

## Como funciona o Pixel da Meta em Tags

Em nossa plataforma, o **Pixel da Meta** pode ser inserido em uma tag, que vai funcionar como um **Gatilho de Evento de Conversão**. Quando essa tag for marcada, o **Chat Master Veloz** imediatamente envia um sinal (o Evento) à Meta.

### ⚡ Exemplo Prático

![Linha do tempo do Pixel em Tags: o anúncio traz o cliente, a tag é marcada na conversa e o evento é enviado à Meta](https://clihelper.chatmasterveloz.com/docs-imagem/22044-pixel-meta-exemplo-1024x309.jpg)1️⃣ Seu anúncio chama atenção de um potencial cliente (lead), que clica e inicia uma conversa com sua empresa.

2️⃣ A sua automação (ou um atendente) marca uma tag para essa conversa.

3️⃣ A atribuição da tag integrada com o Pixel Meta funciona como um gatilho que envia um evento avisando a Meta.

Essa informação é utilizada para melhorias de campanhas e estratégias.

## Como configurar o Pixel da Meta em uma Tag

Acesse o menu **Tags  ›  adicionar ou editar Tag  ›  aba Pixel META**

![Formulário de Integração Pixel Meta em Tags](https://clihelper.chatmasterveloz.com/docs-imagem/22044-tags-pixel-meta-integracao-1024x711.jpg)⚡ Na aba **PIXEL META**, preencha os campos com os dados fornecidos pelo Facebook Business Manager:

**"Configuração Pixel META"**

🔘 **Formato do evento:** **Site (o Pixel de sempre)** ou **Mensagens do WhatsApp**. Os campos abaixo mudam conforme a escolha.

🔘 **Access Token:** cole o token de acesso da API de Conversões. Só no formato Site.

🔘 **Pixel ID:** insira o ID (identificador) do seu pixel. Só no formato Site.

🔘 **Nome do Evento:** deve ser digitado exatamente igual a documentação da Meta: **Leads**, **CompleteRegistration**, **AddToWishlist**, **AddToCart**, **Purchase**, por exemplo. (documentação completa em [https://developers.facebook.com/docs/meta-pixel/reference](https://developers.facebook.com/docs/meta-pixel/reference))

🔘 **Evento:** no formato Mensagens, no lugar de digitar o nome você escolhe entre **Lead**, **Lead qualificado** e **Venda**.

🔘 **Custom Data:** consulte a documentação para saber os campos opcionais e obrigatórios. Só no formato Site.

No evento Purchase é obrigatório "currency" e "value". Veja um exemplo:

```json
{
    "value": 115.00,
    "currency": "BRL"
}
```

🔘 **Source:** indica o local em que o evento está sendo enviado. Website, server, crm ou, neste caso, o nome da nossa plataforma Chat Master Veloz. Só no formato Site.

🔲 Para finalizar, clique em **Salvar**.

🎯 A partir de agora, sempre que essa tag for vinculada (manual ou automaticamente), o evento será enviado para o Facebook.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O evento é disparado se já havia a tag antes?** Não. O disparo ocorre no momento da "ação" de adicionar a tag ao contato ou ticket. Clientes que já possuíam a tag antes da configuração não enviam o evento retroativamente.
>
> **Preciso configurar em todas as tags?** Recomendamos configurar apenas em tags estratégicas que representam uma mudança de etapa importante no funil (ex: "Venda Realizada", "Lead Qualificado").
>
> **Onde pego o Access Token?** No Gerenciador de Eventos do Facebook. No formato **Mensagens do WhatsApp** você não precisa dele: o token vem da conexão.
>
> **Qual formato devo escolher?** Se o atendimento vem de anúncio de WhatsApp e você quer que a Meta ligue a conversão ao anúncio certo, use **Mensagens do WhatsApp**. Se você já tem o Pixel do site e quer repetir aqueles eventos, use **Site**.
>
> **Marquei a tag e o evento não foi enviado.** Abra o menu **Logs Pixel (META)**: a linha daquele atendimento traz o motivo. Os mais comuns no formato Mensagens são o atendimento não ter vindo de anúncio e a conexão não ser da API Oficial.

> **[ERROS]**
>
> #### Erros Comuns
>
> **O atendimento não começou por um clique em anúncio de WhatsApp:** o formato Mensagens só existe para amarrar a conversão ao anúncio. **Solução:** para atendimento que entrou por outro caminho, use o formato **Site**.
>
> **A conexão do atendimento não é da API oficial, ou está sem a conta (WABA) e o token:** quem envia é a conexão, então ela precisa ser oficial e estar completa. **Solução:** confira a conexão no menu **Conexões**.
>
> **O evento já tinha sido enviado para este mesmo clique no anúncio:** cada clique recebe cada evento uma vez. **Solução:** nenhuma — é proteção contra duplicidade.
>
> **A Meta recusou o evento:** a resposta dela aparece logo abaixo do motivo, no log. **Solução:** leia a mensagem da Meta; costuma ser dado faltando ou permissão do app.
>
> **A Meta não liberou o conjunto de dados da conta:** falta permissão de eventos no app da Meta. **Solução:** ajuste a permissão no Gerenciador de Eventos e tente de novo.
>
> **O evento passou de 7 dias sem conseguir sair:** depois desse prazo a plataforma para de tentar. **Solução:** resolva a causa no log e trate o evento como perdido — ele não é reenviado.
