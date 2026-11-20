# Link na Bio

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/link-na-bio
- **Categoria:** Recursos
- **Menu:** Link na Bio

---

🧩 Você divulga o WhatsApp num lugar, o site em outro e a loja em outro, e não sabe por onde o cliente chegou? Cada link a mais espalhado pelas redes é um lugar a mais para manter e uma informação a menos sobre o que funcionou.

O **Link na Bio** é a página da empresa na internet, com um endereço só: foto, título, descrição e um botão para cada destino. Não é um link curto que leva a um lugar só: é uma página, e a plataforma conta quantas pessoas tocaram em cada botão e quantas viraram conversa.

Ideal para:

☑️ **Bio das redes sociais:** Reúne os destinos da empresa num endereço só.

☑️ **Medição da divulgação:** Mostra os toques de cada botão e quantos viraram conversa.

☑️ **Integração com outros sistemas:** Avisa por webhook cada toque num botão e cada vez que a página é salva.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Link na Bio**. Só o administrador tem esse menu.
>
> ➡️ Preencha **Endereço da página**, **Título**, **Descrição** e **Foto (endereço da imagem)**.
>
> ➡️ Em **Botões**, adicione um botão para cada destino e escreva o **Texto do botão**.
>
> ➡️ Ligue **Página no ar** e clique em **Salvar**.
>
> ➡️ Clique em **Abrir a página** para conferir e divulgue o endereço.

## Como montar a página do Link na Bio

Acesse o menu **Link na Bio**:

🔘 **Página no ar:** deixa a página aberta ao público. Desligada, quem abre o endereço vê *"Esta página não está no ar."*, e os toques já contados ficam guardados.

🔘 **Endereço da página:** a parte final do link, de 3 a 60 letras minúsculas, números e hífen. O link completo aparece logo abaixo e muda enquanto você digita.

🔘 **Título:** até 80 caracteres.

🔘 **Descrição:** até 300 caracteres.

🔘 **Foto (endereço da imagem):** o endereço de uma imagem que já está na internet, começando com `http://` ou `https://`.

🔘 **Abrir a página:** aparece depois que a página é salva e está no ar.

⚠️ Trocar o **Endereço da página** tira o endereço antigo do ar na hora. Atualize o link nas redes e nos materiais de divulgação no mesmo momento. Os toques continuam nos botões.

## Os botões do Link na Bio

A página aceita até **30 botões**, mostrados um por linha, na mesma ordem da tela. Cada botão do **Link na Bio** tem:

🔘 **Tipo:** o destino do botão, escolhido em **+ WhatsApp**, **+ Cardápio Digital**, **+ Link** ou **+ WebChat**.

🔘 **Texto do botão:** o que aparece na página, com até 60 caracteres. Todo botão precisa de um texto.

🔘 **Ativo:** desligado, o botão some da página pública, e o endereço dele deixa de abrir.

🔘 **Subir**, **Descer** e **Remover:** mudam a ordem do botão ou o tiram da página.

Cada tipo de botão leva a um destino:

➡️ **WhatsApp:** abre a conversa pela **Conexão** escolhida, com a **Mensagem que já vem escrita**, de até 500 caracteres. Um código de rastreio vai no fim da mensagem: é por ele que a conversa fica ligada ao toque.

➡️ **Cardápio Digital:** leva ao Cardápio Digital da empresa, em outra aba. O botão só aparece com a loja no ar.

➡️ **Link:** leva ao **Endereço do link**, em outra aba. O endereço precisa começar com `http://` ou `https://`.

➡️ **WebChat:** abre o chat do site ali mesmo, na página, pela **Conexão de WebChat** escolhida. O contato chega com a origem do botão.

## Como saber que a conversa veio do Link na Bio

Quando a conversa começa por um botão do **Link na Bio**, o painel do contato mostra o card **Veio do Link na Bio**, com o botão tocado, a data do toque e as marcações de campanha, quando houver.

Na conversa aberta pelo botão **WebChat**, a **nota interna** do atendimento também registra a origem e a página de onde o contato veio.

## Os toques do Link na Bio

No fim da tela, **Toques nos últimos 30 dias** mostra o total e uma tabela por botão:

🔘 **Texto do botão:** o nome do botão.

🔘 **Toques:** quantas vezes o botão foi tocado.

🔘 **Viraram conversa:** quantos toques daquele botão viraram conversa.

Enquanto ninguém tocar em nada, a tela mostra *"Nenhum toque ainda."*

## Aparência do Link na Bio

O bloco **Aparência (CSS e JavaScript)** personaliza a página. O código roda isolado na página pública, e cada campo aceita até **200 KB**.

🔘 **CSS:** muda o visual da página. As classes da página são `.bio`, `.bio-foto`, `.bio-titulo`, `.bio-descricao`, `.bio-botoes` e `.bio-botao`, e cada botão traz o tipo em `data-tipo`:

```
body { background: #ffe9c9 !important; }
.bio-botao[data-tipo="link"] { border-radius: 24px; }
```

🔘 **JavaScript:** roda na página pública. Os dados da página ficam em `window.__LINK_NA_BIO__`: `titulo`, `descricao`, `fotoUrl`, `link` e `botoes`, cada botão com `id`, `tipo`, `rotulo` e `href`.

## Webhook do Link na Bio

O campo **Webhook do Link na Bio** recebe o endereço de outro sistema, começando com `http://` ou `https://`. Esse sistema recebe dois eventos: cada toque num botão e cada vez que a página é salva.

O evento `link-na-bio-clique` é enviado a cada toque:

```json
{
  "acao": "link-na-bio-clique",
  "companyId": 2,
  "clique": {
    "id": 13,
    "botaoId": "bbb11f11",
    "tipo": "webchat",
    "rotulo": "Chat do site",
    "codigo": "bio_FEFCP4PP",
    "referer": null,
    "utmSource": null,
    "utmMedium": null,
    "utmCampaign": null,
    "em": "2026-11-06T09:36:30.984Z"
  },
  "origem": "publico",
  "enviadoEm": "2026-11-06T09:36:30.992Z",
  "backendURL": "https://api.exemplo.com.br"
}
```  
- `clique.botaoId`, `clique.tipo` e `clique.rotulo` — o botão tocado: o identificador, o tipo e o texto.
- `clique.codigo` — o código de rastreio daquele toque.
- `clique.referer`, `clique.utmSource`, `clique.utmMedium` e `clique.utmCampaign` — de onde veio o toque e as marcações de campanha, quando houver. Sem elas, os campos vêm nulos.
- `clique.em` — a data e a hora do toque.
- `origem` — `publico`, porque o toque veio da página.

O evento `link-na-bio-atualizado` é enviado a cada **Salvar**:

```json
{
  "acao": "link-na-bio-atualizado",
  "companyId": 2,
  "linkNaBio": {
    "slug": "minha-empresa",
    "ativo": true,
    "titulo": "Minha Empresa",
    "link": "https://app.exemplo.com.br/bio/minha-empresa",
    "botoes": [
      { "id": "33cf5f5e", "tipo": "link", "rotulo": "Nosso site", "ativo": true, "url": "https://exemplo.com.br" }
    ]
  },
  "origem": "painel",
  "enviadoEm": "2026-11-06T09:31:46.615Z",
  "backendURL": "https://api.exemplo.com.br"
}
```  
- `linkNaBio.slug` e `linkNaBio.link` — o endereço da página.
- `linkNaBio.ativo` — se a página está no ar.
- `linkNaBio.titulo` — o título da página.
- `linkNaBio.botoes` — a lista de botões, cada um com `id`, `tipo`, `rotulo` e `ativo`.
- `origem` — `painel`, porque o evento veio de quem salvou a página.

Os dois eventos trazem também `companyId`, o número da empresa, `enviadoEm`, a data e a hora do envio, e `backendURL`, o endereço do servidor da plataforma.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Quem pode montar o Link na Bio?** Só o administrador. O menu **Link na Bio** não aparece para supervisor e atendente.
>
> **Quem abre a página do Link na Bio precisa de login?** Não. A página é pública e abre no celular e no computador.
>
> **Troquei o Endereço da página do Link na Bio. O endereço antigo continua abrindo?** Não. O endereço antigo sai do ar na hora, e os toques continuam nos botões.
>
> **Tirar o Link na Bio do ar apaga os toques?** Não. Quando **Página no ar** é ligada de novo, a página volta com os mesmos toques.

> **[ERROS]**
>
> #### Erros Comuns
>
> **A tela mostra "Endereço inválido: use de 3 a 60 letras minúsculas, números e hífen.":** o **Endereço da página** tem espaço, é curto ou longo demais. **Solução:** use só letras minúsculas, números e hífen, de 3 a 60 caracteres.
>
> **A tela mostra "Este endereço já é de outra empresa.":** outra empresa já usa o **Endereço da página**. **Solução:** escolha outro endereço.
>
> **A tela mostra "Todo botão precisa de um texto.":** há um botão com o **Texto do botão** em branco. **Solução:** preencha o texto ou remova o botão.
>
> **O botão não aparece na página do Link na Bio:** o botão está com **Ativo** desligado, ou é um botão **Cardápio Digital** com a loja fora do ar. **Solução:** ligue **Ativo** e clique em **Salvar**, ou coloque a loja no ar.
>
> **A tela mostra "O webhook precisa ser um endereço http:// ou https:// de fora do servidor.":** o endereço do campo **Webhook do Link na Bio** não vale. **Solução:** informe o endereço público do outro sistema, começando com `http://` ou `https://`.
