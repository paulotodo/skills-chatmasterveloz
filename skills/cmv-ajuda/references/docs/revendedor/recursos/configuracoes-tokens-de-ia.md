# Tokens de IA em Configurações

- **Fonte:** https://revendedor.chatmasterveloz.com/docs/configuracoes-tokens-de-ia
- **Categoria:** Recursos
- **Menu:** Configurações › Tokens de IA em Configurações

---

🧩 Você liberou a **sugestão de resposta com IA** para um cliente e agora quer controlar o quanto ele usa. É isso que o card **Tokens de IA** faz: dá a cada empresa um saldo de créditos que vai baixando conforme o uso.

☑️ **Cobrança por uso:** venda a sugestão de IA como pacote de créditos, do tamanho que quiser.

☑️ **Cliente sem surpresa:** quem esgota o saldo recebe um aviso claro na tela, e o recurso para até você recarregar.

☑️ **Ilimitado sob controle:** marque uma empresa como ilimitada quando ela for cortesia ou plano alto.

#### 💡 O crédito é seu controle, não o custo da IA

Este é o ponto que muda como você vende: **o crédito não paga a IA**. O consumo real é cobrado pelo provedor de IA na conta dona da chave da OpenAI que a empresa usa, e essa chave é escolhida empresa por empresa, no menu **Configurações  ›  Empresas**: card da empresa, aba **Integrações**, seção **Chave da OpenAI**.

🔘 **Chave própria do cliente:** a chave que ele cadastra no menu **Integrações**, no card **OPEN.AI**. O consumo é cobrado na conta dele.

🔘 **Chave da plataforma (subsidiada):** a empresa usa a chave colada no campo **Chave da plataforma para esta empresa**, e o consumo é cobrado na conta da OpenAI dona dessa chave. Nas palavras da tela, *a chave da plataforma nunca aparece para a empresa*.

O token desta tela é **outra coisa**: é uma moeda sua, que existe só dentro da plataforma, para você medir e limitar o uso do recurso. Por isso você define quanto vale cada ação — e por isso o saldo não tem relação com o preço que a OpenAI cobra.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Acesse o menu **Configurações  ›  Tokens de IA**.
>
> ➡️ Ajuste **Custo sugestão** e **Custo melhoria** da empresa, se quiser um valor diferente de 1.
>
> ➡️ Clique no **+** da linha para recarregar, ou ligue **Ilimitado** para tirar a trava.

## Os indicadores do topo

🔘 **Empresas com o recurso:** quantas têm **Sugestão de resposta IA** no plano.

🔘 **Sem saldo:** quantas estão em zero. É o número para olhar antes de o cliente reclamar.

🔘 **Ilimitadas:** quantas estão sem trava.

🔘 **Tokens em circulação:** a soma dos saldos ainda não usados.

## A tabela

Acima da tabela, **Buscar por empresa ou plano** filtra as linhas e **Atualizar** recarrega. Por padrão a lista mostra só quem tem o recurso no plano. Desligue **Só quem tem o recurso no plano** para ver todas as empresas — as demais aparecem com a etiqueta **fora do plano** na coluna **Plano**, e servem para você deixar o saldo pronto antes de vender.

🔘 **Empresa** e **Plano.**

🔘 **Saldo de tokens:** o que a empresa ainda tem para gastar. Nas empresas ilimitadas aparece um travessão, porque não há contagem.

🔘 **Ilimitado:** o interruptor da linha, que grava ao clicar. Ligado, a empresa usa sem descontar nada, o uso não entra no extrato e os dois custos da linha ficam desabilitados.

🔘 **Custo sugestão** e **Custo melhoria:** quantos créditos cada ação consome. Vêm em **1** e são editáveis por empresa — é aqui que você cobra mais caro pela sugestão do que pela melhoria, ou o contrário. Aceitam de **0** a **1000** e gravam ao sair do campo, sem botão de salvar. Nas palavras da tela, *"Zero libera sem descontar do saldo; o provedor de IA cobra à parte."*

🔘 **Recarregar tokens (+):** abre a janela **Recarregar tokens**, com o nome da empresa, o campo **Tokens** e uma **Observação**. **CREDITAR** soma os tokens ao saldo e confirma com o aviso *"Tokens creditados"*; **CANCELAR** fecha sem creditar. Nas palavras da tela: *o crédito entra no saldo da empresa selecionada e vira linha no extrato* — a linha **Crédito**, com a observação.

## Como o cliente vê o saldo

No atendimento, o balão do **Copiloto de mensagens** mostra o saldo restante ao lado do título. Cada uso que deu certo desconta o **Custo sugestão** ou o **Custo melhoria** da linha, com a **Chave própria do cliente** ou com a **Chave da plataforma (subsidiada)**. O **Concatenador de Mensagens** no modo **Com IA** também desconta do mesmo saldo, como **Melhoria de texto**. O pedido que falha devolve o que custou, numa linha **Estorno** do extrato.

Quando o saldo não cobre o custo, o pedido é recusado e o cliente recebe um aviso na tela para contratar mais créditos.

Com **Ilimitado** ligado, o menu **Sugestão de resposta IA** da empresa mostra **Ilimitado** no lugar do saldo.

O extrato pode ser visto no menu **Sugestão de resposta IA**: uma linha por movimento, com data e hora, o tipo — **Sugestão**, **Melhoria de texto**, **Crédito** ou **Estorno** —, o valor e o saldo que sobrou. O uso de empresa **Ilimitada** não entra no extrato.

⚠️ **O crédito não se renova sozinho.** Não há ciclo mensal: o que você credita vale até acabar. Quem vende pacote recorrente precisa recarregar a cada período, na mão ou combinando com o cliente.

⚠️ **O saldo trava só o Copiloto de mensagens e o Concatenador de Mensagens no modo Com IA.** A transcrição de áudio, o resumo do atendimento e a análise de atendimento (**GPT Análises**) não descontam crédito dos **Tokens de IA**, e o consumo deles é cobrado na conta da OpenAI dona da chave que a empresa usa: com a **Chave da plataforma (subsidiada)**, a chave da plataforma.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **Recarreguei e o cliente continua sem usar.** Confira se o plano dele tem **Sugestão de resposta IA** — o saldo sozinho não liga o recurso. E, se a empresa usa a **Chave própria do cliente**, confira se a chave da OpenAI está preenchida no menu **Integrações** dele. Confira também se o saldo cobre o **Custo sugestão** e o **Custo melhoria** da linha: abaixo do custo, o pedido é recusado. E confira se o atendente tem a permissão **Pode usar sugestão de IA**, no cadastro dele no menu **Equipe**: sem ela, o **Copiloto de mensagens** some da conversa.
>
> **Coloco crédito, mas quem paga a OpenAI?** A conta da OpenAI dona da chave que a empresa usa: a do cliente, com a **Chave própria do cliente**; a dona da chave da plataforma, com a **Chave da plataforma (subsidiada)**. O crédito daqui é a sua trava de uso, não o repasse do custo.
>
> **Com a Chave da plataforma (subsidiada), o saldo de Tokens de IA ainda desconta?** Sim. O Copiloto de mensagens desconta o custo da linha a cada uso que deu certo, com qualquer das duas chaves. A transcrição de áudio, o resumo do atendimento e a análise de atendimento não descontam, com nenhuma delas.
>
> **O cliente diz que gastou mais do que usou.** Peça para ele abrir o **Extrato de tokens** no fim do menu **Sugestão de resposta IA**: cada linha traz a hora e o tipo do uso.
>
> **Posso deixar a sugestão mais cara que a melhoria?** Pode. Os dois custos são por empresa e independentes.

> **[ERROS]**
>
> #### Erros Comuns
>
> **Vender o recurso e esquecer o saldo:** o plano libera, o cliente usa e trava em zero. **Solução:** ao habilitar **Sugestão de resposta IA** no plano, credite o pacote na mesma hora, ou ligue **Ilimitado**.
>
> **Achar que o crédito renova no mês:** ele não renova. **Solução:** acompanhe o indicador **Sem saldo** e recarregue.
