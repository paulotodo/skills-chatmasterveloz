# Cores em Configurações

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/configuracoes-cores
- **Categoria:** Recursos
- **Menu:** Configurações › Cores em Configurações

---

🧩 O card **Cores** cuida da aparência da instância inteira: a cor principal, as barras, as imagens de fundo — e, para quem precisa ir além, CSS e JS personalizados, separados entre o que carrega antes do login e o que só carrega depois.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Cores**.
>
> ➡️ Escolha as cores e as imagens nos dois primeiros blocos.
>
> ➡️ Nos blocos de CSS e JS, cada campo tem o próprio botão **Salvar**.

## Cores Principais

🔘 **Cor Principal**, **Barra de Rolagem** e **Barra Superior:** cada uma com o código da cor e um seletor.

## Imagens de Background

🔘 **Background / Loading** e **Imagem de Background / Login:** o endereço de cada imagem. Aqui é por URL; o envio de arquivo fica no card **Logotipos / Ícones**.

## CSS Personalizado

🔘 **CSS pré-login — público:** injetado no fim do `<head>` em todo o frontend, antes e depois do login; é o que pinta a tela de entrada. Para vencer estilos do tema, use `!important`. **Salvar CSS pré-login** grava, e a página recarrega.

🔘 **CSS pós-login — só para quem entrou:** vale dentro da plataforma. Nas palavras da tela, *"Entra depois do CSS pré-login e antes do CSS da empresa — em empate de especificidade, quem vence é o da empresa."* A opção **Usar a customização geral (CSS e JS)** do cadastro da empresa vale para os dois campos de CSS. **Salvar CSS pós-login** grava, e a página recarrega.

Nas palavras da tela: *são dois campos porque o momento de carregar muda quem consegue ler. O de cima precisa ser público para pintar a tela de entrada; o de baixo só é entregue a quem já está autenticado.*

O link **Ver todas as classes e como usá-las**, no bloco de CSS, abre a lista das classes da plataforma.

## Cores do tema claro e escuro por CSS

As cores do tema claro e do tema escuro são variáveis de CSS. Trocar o valor de uma variável muda de uma vez todos os elementos que a usam, sem precisar achar a classe de cada um.

➡️ **Áreas:** `--mui-background` (o fundo da tela), `--mui-paper` (os cards), `--mui-paper-2`, `--mui-paper-3`, `--mui-divider` e `--mui-dashboard-card`.

➡️ **Cor principal:** `--mui-primary`, `--mui-primary-dark`, `--mui-primary-contrast`, `--mui-button-primary`, `--mui-button-primary-hover` e `--mui-button-primary-contrast`.

➡️ **Cor secundária:** `--mui-secondary`, `--mui-secondary-dark` e `--mui-secondary-contrast`. No tema escuro, ela pinta o botão **Enviar Template** da faixa da janela de 24 horas, os outros botões na cor secundária, os chips e selos, os interruptores, as caixas de marcar, os rádios, as abas e as barras de progresso.

O lugar onde a variável é escrita muda conforme o tema. No **tema claro**, as variáveis de área vão em `body[data-theme="light"]`: escritas no `:root`, elas não mudam o tema claro. No **tema escuro**, as variáveis vão em `:root`; por exemplo, `--mui-primary` no `:root` muda o indicador da aba selecionada.

```
body[data-theme="light"] {
  --mui-background: #f4f6f8;
  --mui-paper: #ffffff;
}

:root {
  --mui-paper: #1c2430;
  --mui-primary: #90caf9;
}
```

Cole o CSS no **CSS pós-login**, que vale dentro da plataforma, ou, para uma empresa só, no **CSS desta empresa**, no card da empresa, no menu **Configurações  ›  Empresas**.

## Menu lateral, Quadro e celular por CSS

O CSS também personaliza partes da plataforma pelo nome de cada uma:

➡️ **Menu lateral:** cada seção do menu tem nome próprio, e um fundo nela destaca a seção inteira, com o título junto. A variável `--menu-ordem` muda a ordem das seções, dos submenus e dos itens.

➡️ **Quadro de atendimentos:** a hora de cada card muda de cor por faixa de tempo — em dia, atenção e atrasado. As variáveis `--quadro-tempo-em-dia`, `--quadro-tempo-atencao` e `--quadro-tempo-atrasado`, no `:root`, trocam essas cores nos dois temas, sem `!important`.

➡️ **Celular:** a foto e o nome do contato no cabeçalho do atendimento, as etiquetas e a faixa **Ticket / Atendimentos** têm nome próprio, para esconder o que não se usa e ganhar espaço para a conversa.

Os nomes de cada parte estão no link **Ver todas as classes e como usá-las**, no bloco de CSS.

## JS Personalizado

🔘 **JS pré-login — público:** injetado no fim do `<body>` em todo o frontend, inclusive na tela de login. A sintaxe é validada ao salvar, e código quebrado é recusado. Erros na execução aparecem no console como `[custom-js]`. **Salvar JS** grava, e a página recarrega.

🔘 **JS pós-login — só para quem entrou:** roda dentro da plataforma, uma vez por carregamento, depois do login e antes do JS da empresa. **Salvar JS pós-login** grava, e a página recarrega.

⚠️ Também nas palavras da tela: *mesma divisão do CSS, e aqui ela pesa mais: no JS não vaza aparência, vaza lógica de operação. Regra de bloqueio de função, limite de SLA, nome de chave de armazenamento — tudo isso fica legível para quem só abriu a URL, se estiver no campo de cima.* Regra de negócio vai no campo de baixo.

## Prévia do link compartilhado

Nas palavras da tela: *"Quando alguém compartilha o endereço do painel no WhatsApp, Facebook, LinkedIn ou Telegram, a prévia mostra estes dados. O que ficar em branco não aparece."*

🔘 **Nome do site**, **Título da prévia** e **Descrição:** os textos da prévia.

🔘 **Endereço da imagem:** uma imagem pública de 1200 × 630 pixels, em JPG ou PNG.

🔘 **Texto alternativo da imagem:** a descrição da imagem.

🔘 **SALVAR PRÉVIA:** grava o bloco.

⚠️ O WhatsApp guarda a prévia de cada link por um tempo. Para ver a nova na hora, compartilhe o link com `?v=2` no final.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Uma empresa quer cores diferentes das outras.** O que é geral fica aqui. Por empresa, use **CSS desta empresa** no card dela, no menu **Configurações  ›  Empresas**, e desligue **Usar a customização geral (CSS e JS)** lá.
>
> **Mudei `--mui-paper` no `:root` e o tema claro não mudou.** No tema claro, as variáveis de área (`--mui-background`, `--mui-paper`, `--mui-paper-2` e `--mui-paper-3`) vão em `body[data-theme="light"]`; o `:root` muda o tema escuro.
>
> **Coloquei CSS e a tela de login não mudou.** Foi no campo pós-login. A tela de entrada só lê o campo **pré-login — público**.
