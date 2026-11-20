# Modelos de E-mail: Blocos e HTML

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/modelos-de-e-mail-blocos-e-html
- **Categoria:** Recursos
- **Menu:** Mail Marketing › Modelos de E-mail: Blocos e HTML

---

🧩 O modelo é o e-mail pronto para as campanhas do **Mail Marketing**: assunto, textos, imagens, botões e o nome de cada pessoa no lugar certo. Ele é montado uma vez e usado em quantas campanhas a empresa quiser, de dois jeitos: com **blocos**, sem escrever código, ou colando o **HTML** de um e-mail já pronto.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Mail Marketing** e abra a aba **Modelos**.
>
> ➡️ Clique em **Novo modelo** e preencha o **Nome do modelo**, o **Assunto** e o **Pré-cabeçalho**.
>
> ➡️ Escolha **Blocos** ou **HTML** e monte o e-mail, conferindo na **Prévia**.
>
> ➡️ Clique em **Salvar**.
>
> ➡️ Em **Enviar um teste**, digite o seu e-mail e clique em **Enviar teste** para ver o e-mail na caixa de entrada.

## A aba Modelos

A aba **Modelos** lista cada modelo do **Mail Marketing** com o **Nome do modelo**, o **Assunto**, o **Tipo** (**Blocos** ou **HTML**) e a data em **Alterado em**, e os botões **Editar**, **Duplicar** e **Remover**.

## Os campos do modelo

Acesse o menu **Mail Marketing  ›  Modelos  ›  Novo modelo**

🔘 **Nome do modelo:** o nome que aparece na escolha do modelo da campanha. Sem ele, o **Salvar** fica desativado.

🔘 **Blocos** e **HTML:** o alternador do topo escolhe como o e-mail é montado.

🔘 **Assunto:** o assunto do e-mail. A campanha usa este assunto quando o assunto dela fica em branco.

🔘 **Pré-cabeçalho:** nas palavras da tela, *"O texto curto que aparece ao lado do assunto na caixa de entrada."*

## As variáveis do modelo

As variáveis trocam um texto pelo dado de cada pessoa no momento do envio. O editor mostra as variáveis em botões:                          

| Variável | No e-mail enviado |
|---|---|
| `{{nome}}` | o nome da pessoa, como está na lista |
| `{{primeiro_nome}}` | a primeira palavra do nome |
| `{{email}}` | o endereço de e-mail da pessoa |
| `{{descadastro}}` | o link para a pessoa não receber mais |

Clicar numa variável copia o texto dela, e a tela confirma, por exemplo, *"{{primeiro_nome}} copiado. Cole no texto."* A variável funciona no assunto e nos textos do e-mail.

As colunas a mais das planilhas das listas também viram variáveis, com o nome da coluna entre chaves duplas, como `{{cidade}}` ou `{{plano}}`. Quem não tem a informação na lista recebe o e-mail com o espaço em branco.

O `{{descadastro}}` é opcional. Nas palavras da tela, *"se o modelo não tiver, ele entra sozinho no rodapé."*

## O estilo do e-mail

🔘 **Fundo**, **Conteúdo**, **Texto** e **Destaque:** as cores do fundo do e-mail, da área do conteúdo, do texto e de destaque.

🔘 **Fonte:** Arial, Georgia, Trebuchet MS, Verdana ou Courier New.

🔘 **Endereço da logo (opcional):** o endereço público da imagem com a logo da empresa.

## Os blocos

O e-mail em blocos é montado de cima para baixo, com o botão **Adicionar bloco**. O modelo novo já abre com blocos de exemplo, como um **Título**, um **Texto** e um **Botão**, para trocar pelo conteúdo da empresa.                                          

| Bloco | O que se preenche |
|---|---|
| **Título** | o texto, o **Tamanho** (Grande, Médio ou Pequeno) e o **Alinhamento** |
| **Texto** | o texto, em várias linhas, e o **Alinhamento**; aceita `**negrito**`, `_itálico_` e `[texto do link](https://...)` |
| **Imagem** | o **Endereço da imagem**, o **Link**, a **Descrição da imagem** e a **Largura (%)**, de 10 a 100 |
| **Botão** | o texto, o **Link**, o **Alinhamento** e a **Cor do botão** |
| **Colunas** | duas ou três colunas lado a lado, cada uma com imagem, título, texto e link |
| **Divisor** | uma linha que separa as partes do e-mail, sem campos |
| **Espaço** | um respiro em branco, com a **Altura (px)** de 4 a 120 |
| **HTML livre** | um trecho de HTML no meio dos blocos |

🔘 **Imagem:** a imagem entra pelo endereço público dela, começando com `https://`. O bloco não recebe arquivo do computador.

🔘 **Colunas:** o bloco começa com duas colunas; **Mais uma coluna** acrescenta a terceira e **Uma coluna a menos** tira uma.

🔘 Cada bloco tem, no canto, os botões de subir, descer, duplicar e remover. O primeiro bloco não sobe e o último não desce.

## O modo HTML

Com **HTML** no alternador, o **Estilo** e os **Blocos** dão lugar a um campo só, o **HTML**. Nas palavras da tela: *"Cole o HTML do e-mail. Os links são rastreados e o rodapé de descadastro entra sozinho se faltar."* Voltar para **Blocos** traz de volta os blocos que estavam montados.

No modelo em HTML do **Mail Marketing**, o rodapé com o link de descadastro é somado ao fim do HTML colado.

## A prévia do modelo

A **Prévia**, à direita, mostra o desenho do e-mail com o rodapé e o texto do link de descadastro das configurações do **Mail Marketing**, e se atualiza a cada mudança. Os botões de computador e de celular, acima dela, trocam a largura da prévia.

A prévia não troca as variáveis: `{{primeiro_nome}}` aparece escrito como está. Para ver o e-mail com um nome no lugar, use o teste.

## Salvar e enviar um teste

Ao salvar, a tela confirma com *"Modelo salvo."*, o título passa a **Editar modelo** e aparece o quadro **Enviar um teste**:

🔘 **Enviar o teste para:** o endereço que recebe o teste. Sem ele, o botão **Enviar teste** fica desativado.

🔘 **Conta de e-mail que envia:** a conta de e-mail da empresa que envia o teste.

🔘 **Enviar teste:** salva o modelo e envia o teste; a tela confirma com *"Teste enviado para"* e o endereço.

O e-mail de teste chega com **[Teste]** na frente do assunto e com um exemplo no lugar das variáveis: **Maria** no `{{primeiro_nome}}`, **Maria Silva** no `{{nome}}` e o próprio endereço do teste no `{{email}}`. As colunas das planilhas ficam em branco. Os links do teste levam direto ao endereço de destino, e o link de descadastro não funciona no teste.

## Duplicar e remover o modelo

🔘 **Duplicar:** cria uma cópia do modelo com *"(cópia)"* no fim do nome.

🔘 **Remover:** pede confirmação, e a tela avisa: *"As campanhas que já foram agendadas guardam a cópia delas e não mudam."*

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A prévia do modelo do Mail Marketing mostra {{primeiro_nome}} em vez do nome.** É o esperado: a prévia não troca as variáveis. Salve o modelo e use **Enviar um teste**: o teste chega com um nome de exemplo no lugar delas, e a campanha, com o nome de cada pessoa.
>
> **Posso enviar uma imagem do computador para o modelo do Mail Marketing?** Não. O bloco **Imagem** usa o endereço público da imagem, que começa com `https://`. Publique a imagem num site e cole o endereço no campo **Endereço da imagem**.
>
> **Tenho um e-mail pronto em HTML. Dá para usar no Mail Marketing?** Dá. No modelo, escolha **HTML** no alternador e cole o código no campo **HTML**. Nas palavras da tela, os links são rastreados e o rodapé de descadastro entra sozinho se faltar.
>
> **O e-mail de teste do Mail Marketing chegou com [Teste] no assunto.** É o esperado: o teste chega marcado e com um nome de exemplo no lugar das variáveis. O e-mail da campanha é enviado sem a marca, com os dados de cada pessoa.
>
> **Remover um modelo do Mail Marketing muda a campanha que já foi agendada?** Não. Nas palavras da tela, *"As campanhas que já foram agendadas guardam a cópia delas e não mudam."*
