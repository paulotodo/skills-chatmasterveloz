# Botões

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/bloco-botoes
- **Categoria:** Recursos
- **Menu:** FlowBuilder › Blocos › Botões

---

🧩 O bloco **Botões** envia uma mensagem com botões que o cliente toca em vez de digitar: abrir um site, ligar para a empresa, copiar um código ou responder com uma opção pronta.

O mesmo bloco funciona em todos os canais. O que muda é quantos botões cabem e quais tipos cada canal aceita. Onde o canal não tem botão, as opções chegam numeradas em texto e o cliente responde com o número.

**🏷️ Categoria: Mensagem**

Ideal para:

☑️ **Link para o site:** leva o cliente a uma página com um toque.

☑️ **Cupom ou código PIX:** entrega um código que o cliente copia sem erro de digitação.

☑️ **Resposta rápida:** oferece opções prontas, como *Sim* e *Não*, para o cliente responder com um toque.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **FlowBuilder Nativo** e abra o fluxo no editor.
>
> ➡️ Clique no **+** e escolha **Botões**.
>
> ➡️ Escreva o **Corpo da Mensagem**, configure cada botão e clique em **Adicionar**.

## Como configurar o bloco Botões

Acesse o menu **FlowBuilder Nativo  ›  editar fluxo  ›  +  ›  Botões**

🔘 **Título (Header):** texto opcional acima da mensagem, até 60 caracteres.

🔘 **Corpo da Mensagem (Body):** o texto principal, obrigatório, até 1024 caracteres.

🔘 **Rodapé (Footer):** texto opcional abaixo da mensagem, até 60 caracteres.

Cada botão tem o **Tipo de Botão** e o **Texto do Botão / Título**, com até 20 caracteres, e mais um campo conforme o tipo:

◽ **Botão URL:** o campo **URL**, a página que abre ao tocar.

◽ **Botão Ligação:** o campo **Telefone**, o número que o celular do cliente vai discar.

◽ **Botão Copiar e Colar:** o campo **Valor a Copiar**, o texto que vai para a área de transferência, como um cupom ou um código PIX.

◽ **Botão Quick Reply:** o campo **Valor da Resposta Rápida**, que identifica a resposta quando o cliente toca no botão.

🔘 **Adicionar Novo Botão:** inclui o próximo botão. A janela mostra quantos já estão configurados.

🔘 **Sem resposta: seguir pela saída depois de (minutos):** com minutos preenchidos, o bloco ganha a saída **Sem resposta**, para quem não responder nesse tempo. Vazio ou 0 desliga.

🔲 Para finalizar, clique em **Adicionar**.

No desenho, o bloco mostra cada botão com o texto, o valor e o tipo, e tem **uma saída**: o fluxo segue por ela depois que o cliente responde.

## Quantos botões cabem em cada canal                                    

| Canal | Botões | Tipos aceitos |
|---|---|---|
| WhatsApp Oficial | até 3 | URL, Copiar e Colar, Quick Reply |
| WhatsApp QRCode | sem limite da plataforma | URL, Ligação, Copiar e Colar, Quick Reply |
| Instagram e Facebook | até 13 | Quick Reply |
| Telegram | sem limite da plataforma | URL, Quick Reply |
| Canais do HUB | sem botões | as opções chegam numeradas em texto |

⚠️ **No WhatsApp Oficial, o primeiro botão manda na mensagem inteira.** Se ele for de URL, só ele é enviado. Se for de Copiar e Colar, a mensagem vira texto com o código. Ponha primeiro o botão que não pode faltar.

⚠️ **No Instagram e no Facebook, um botão de URL transforma os botões num cartão**, e cabem só 3. O que passar disso entra escrito na mensagem, sem se perder.

⚠️ No **WhatsApp QRCode**, os botões precisam do recurso de botões liberado no plano.

No **WebChat**, os botões de **Quick Reply** chegam clicáveis no chat do site, e o fluxo segue na hora em que o visitante toca. Só a última mensagem com opções aceita o toque: os botões das mensagens anteriores ficam desativados, e o toque num deles é recusado.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Quero um caminho diferente para cada botão. Uso o bloco Botões?** O bloco **Botões** tem uma saída só. Para um caminho por opção, use o bloco **Menu** no tipo **Menu em Botões**, que leva cada escolha para um lado.
>
> **Por que o cliente recebeu as opções numeradas em vez de botões?** O canal da conversa não tem botões, como os canais do HUB. Nesses casos as opções chegam em texto e o cliente responde com o número.
>
> **Configurei quatro botões e o cliente recebeu só um no WhatsApp Oficial.** O primeiro botão era de URL, e nesse canal ele manda na mensagem inteira. Coloque o botão de URL depois dos outros, e lembre que o canal aceita até 3.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Texto do botão longo demais:** o campo **Texto do Botão / Título** não aceita mais de 20 caracteres, e o texto planejado não cabe. **Solução:** use textos curtos, como *Ver site* ou *Copiar cupom*.
>
> **Botão de Ligação no canal errado:** Ligação não existe no WhatsApp Oficial, no Instagram, no Facebook nem no Telegram. **Solução:** confira o quadro de canais antes de escolher o tipo.
