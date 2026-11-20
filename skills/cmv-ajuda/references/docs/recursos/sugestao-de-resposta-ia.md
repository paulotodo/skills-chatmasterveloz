# Sugestão de resposta IA

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/sugestao-de-resposta-ia
- **Categoria:** Recursos
- **Menu:** Inteligência Artificial › Sugestão de resposta IA

---

🧩 Aqui você ensina a IA a falar como a sua empresa fala. É a tela que governa o **Copiloto de mensagens** — o botão de IA ao lado do campo de mensagem — e ela define duas coisas separadas: como a IA escreve uma resposta do zero, e como ela corrige o texto que o atendente digitou.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Sugestão de resposta IA**.
>
> ➡️ Ajuste as instruções das duas funções ao seu negócio.
>
> ➡️ Escolha o **Modelo** e quantas **Mensagens de contexto** a IA lê. Clique em **SALVAR**.
>
> ➡️ Acompanhe o consumo no **Extrato de tokens**, no fim da página.

## Saldo de tokens

No topo, quanto a sua empresa ainda tem para usar a IA. Junto do saldo, a tela mostra quanto cada uso desconta, por exemplo *Custo sugestão: 1 · Custo melhoria: 1*: o primeiro número vale para cada **Sugerir resposta com IA**, o segundo para cada **Melhorar texto**. O saldo aparece em um de dois estados:

🔘 **Com saldo contado:** aparece o número, que cai a cada uso que deu certo, no valor do custo daquele uso. Quando o saldo não cobre o custo de um uso, ainda que não esteja zerado, o pedido é recusado com um aviso para contratar mais créditos. Para recarregar, fale com o suporte.

🔘 **Ilimitado:** no lugar do número, o **Saldo de tokens** mostra **Ilimitado**, com o texto *"Esta empresa usa a credencial de IA dela: o uso não desconta do saldo da plataforma. Os tokens continuam sendo consumidos e cobrados direto pelo provedor de IA."* Não há trava de uso, e o uso não entra no **Extrato de tokens**.

## Instruções para sugerir a resposta

O texto que manda na função **Sugerir resposta com IA**. Nas palavras da tela: *diga à IA como ela deve responder: tom, limites e o que nunca inventar*.

O padrão já vem com as regras que evitam o erro mais caro — inventar preço, prazo, endereço ou política. Vale adaptar ao seu negócio, mas mantenha esse limite: é ele que impede a IA de prometer o que você não cumpre.

## Instruções para melhorar o texto

O texto que manda na função **Melhorar texto**. Nas palavras da tela: *como a IA deve reescrever o que o atendente digitou*.

O padrão manda corrigir ortografia e tom **sem** acrescentar informação nova, promessa, preço ou prazo que não estivesse no texto. É o que garante que a melhoria não mude o que foi combinado com o cliente.

## Modelo e contexto

🔘 **Modelo:** qual inteligência responde. As opções são **GPT-4o Mini**, **GPT-4o**, **GPT-4 Turbo**, **GPT-4** e **GPT-3.5 Turbo**. O Mini é o mais barato e rápido; os maiores escrevem melhor e custam mais na conta da OpenAI dona da chave que a sua empresa usa.

🔘 **Mensagens de contexto:** quantas mensagens da conversa a IA lê antes de responder, de **1 a 50**. Poucas deixam a resposta genérica; muitas encarecem cada uso e podem trazer assunto velho.

## Extrato de tokens

No fim da página, o histórico de consumo, do mais recente para o mais antigo, com quatro colunas:

🔘 **Quando:** data e hora do uso.

🔘 **Tipo:** o que mexeu no saldo — **Sugestão**, **Melhoria de texto**, **Crédito** ou **Estorno**.

🔘 **tokens:** quanto aquela linha mexeu no saldo: negativo no uso, positivo no crédito e no estorno.

🔘 **Saldo depois:** o que sobrou naquele momento. É a coluna que mostra a queda até zero.

Os quatro tipos do **Extrato de tokens**:

➡️ **Sugestão:** cada resposta sugerida pela IA.

➡️ **Melhoria de texto:** cada texto que a IA reescreveu.

➡️ **Crédito:** a recarga que entrou no saldo.

➡️ **Estorno:** o token devolvido quando um uso falha. O pedido que não deu certo não custa nada.

⚠️ A OpenAI cobra o uso na conta dona da chave que a sua empresa usa: com a credencial cadastrada por você no menu **Integrações**, é a **sua** conta na OpenAI. Se a sua conta usa a chave da plataforma, o card **OPEN.AI** do menu **Integrações** avisa *"A inteligência artificial desta conta usa a chave da plataforma. Não é preciso cadastrar uma chave aqui."* Nesse caso, a sugestão e a melhoria usam a chave da plataforma, e o saldo desconta do mesmo jeito. Trocar para um modelo maior ou aumentar as mensagens de contexto aumenta o consumo.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **A sugestão vem sem jeito da minha empresa.** Reescreva as **Instruções para sugerir a resposta** com o seu tom, o que você vende e o que a IA nunca deve afirmar.
>
> **A IA está inventando prazo.** Reforce a regra de não inventar nas instruções, e reduza as mensagens de contexto se ela estiver puxando assunto de conversas antigas.
>
> **Mudei as instruções e nada mudou.** Faltou **SALVAR**. A mudança vale para as próximas sugestões, não para a que já está na tela.
>
> **Quem está gastando os créditos?** Veja o **Extrato de tokens**: cada linha traz a hora e o tipo do uso.
>
> **A sugestão foi recusada por falta de créditos, mas o saldo não está zerado.** O saldo não cobre o custo de um uso, que aparece junto dele como **Custo sugestão** e **Custo melhoria**. Para recarregar, fale com o suporte.
>
> **Um uso da IA falhou. Perdi o token?** Não. O token volta para o saldo, e o **Extrato de tokens** mostra a linha **Estorno**.
>
> **Qual modelo escolher?** Comece no **GPT-4o Mini**. Só suba se as respostas estiverem fracas para o seu tipo de atendimento.
