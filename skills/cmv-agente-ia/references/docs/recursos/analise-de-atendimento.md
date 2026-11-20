# Análise de Atendimento

- **Fonte:** https://clihelper.chatmasterveloz.com/docs/analise-de-atendimento
- **Categoria:** Recursos
- **Menu:** Inteligência Artificial › Análise de Atendimento

---

🧩 Precisa entender rápido como foi um atendimento, ou ler numa olhada o que aconteceu nas conversas de um contato? Na própria conversa, a IA faz duas leituras: a **análise do atendimento**, que avalia como ele foi conduzido, e o **resumo do período**, que conta o que aconteceu nas mensagens de um intervalo de datas.

A análise e o resumo chegam na conversa como **nota interna**, só para a equipe. O cliente não recebe nada.

Ideal para:

☑️ **Retorno ao atendente:** aponta as objeções do cliente e os pontos de melhoria no atendimento.

☑️ **Passagem de bastão:** quem assume a conversa lê o resumo em vez de rolar o histórico.

> **[RESUMO]**
>
> #### Resumo Prático
>
> ➡️ Abra a conversa pelo menu **Chats**, com o atendimento aberto.
>
> ➡️ No topo da conversa, clique em **Analisar Atendimento com IA** ou em **Resumo do período**. Com as ações do topo agrupadas, os dois ficam no botão **Mais**.
>
> ➡️ Leia o resultado na nota interna que chega na conversa.
>
> ➡️ Para mudar o que a análise escreve, acesse o menu **GPT Análises**.

## Como analisar o atendimento com IA

Acesse o menu **Chats** e abra a conversa.

🔘 **Analisar Atendimento com IA:** um dos ícones do topo da conversa. O botão aparece com o atendimento aberto; com a conversa em **Aguardando**, aceite o atendimento antes.

⚠️ Com a opção **Ações do topo do ticket** em **Agrupadas**, o **Analisar Atendimento com IA** e o **Resumo do período** ficam no botão **Mais**, no grupo **IA e resumos**. A opção fica no menu **Configurações  ›  Opções  ›  Atendimento**, seção **Conversa**.

![Ícone Analisar Atendimento com IA destacado entre os botões do topo da conversa](https://clihelper.chatmasterveloz.com/docs-imagem/20693-analise-atendimento-botao.jpg)

Ao clicar, a conversa recebe a nota interna *"Iniciando análise do atendimento... aguarde!"* e, em poucos segundos, a análise, em outra nota interna. O atendimento continua aberto depois da análise. O conteúdo da análise segue o **Prompt de Análise** configurado no menu **GPT Análises**.

![Exemplo de análise do atendimento pela IA: objeções do cliente; pontos de melhoria no atendimento, como personalização, clareza, empatia, respostas a perguntas específicas, confirmação de informações e agilidade; sentimento geral; e KPIs de tempo de resposta, FCR, CSAT estimado e necessidade de escalonamento](https://clihelper.chatmasterveloz.com/docs-imagem/20693-analise-atendimento-754x1024.jpg)

## Como gerar o resumo do período

🔘 **Resumo do período:** o ícone do topo da conversa abre as opções **Resumo do dia (últimas 24h)**, **Resumo da semana (7 dias)**, **Resumo do mês (30 dias)** e **Período personalizado...**.

Com a opção **Ações do topo do ticket** em **Agrupadas**, o **Resumo do período** fica no botão **Mais**, no grupo **IA e resumos**.

🔘 **Período personalizado...:** abre a janela **Resumo de período personalizado**, com os campos **De** e **Até**. Nas palavras da tela: *"Escolha o intervalo de datas. O resumo será gerado a partir das mensagens deste contato dentro do período."* Clique em **GERAR RESUMO**.

O resumo do período também chega como nota interna: primeiro um aviso, como *"Gerando o resumo (último dia)... aguarde!"*, e depois o resumo, com quantas mensagens ele leu e as seções — visão geral, linha do tempo, pedidos, pendências e próximos passos, entre outras.

Quando a IA não consegue gerar o **resumo do período**, a nota interna diz por quê e onde corrigir, como *"Não foi possível gerar o resumo (último dia). Preencha a Chave de API do provedor em Integrações → Provedor de IA (o campo está vazio)."* Os outros motivos são a chave recusada pelo provedor e o campo **Modelo** vazio.

## Como configurar a análise no GPT Análises

Acesse o menu **GPT Análises**. A tela **GPT Analyzer - Configurações** define o modelo e a instrução que o **Analisar Atendimento com IA** usa.

🔘 **Modelo:** a lista dos modelos da conta OpenAI da empresa. A tela mostra quantos modelos foram carregados, e o ícone **Recarregar modelos OpenAI** busca a lista de novo. Quando a lista não vem da conta, a tela avisa *"Lista fallback — verifique o token OpenAI."*

🔘 **Modelo Personalizado:** nas palavras da tela, *"Ou insira manualmente um ID de modelo"* — para usar um modelo que não está na lista. Escreva o ID exatamente como a OpenAI o chama.

🔘 **Prompt de Análise:** a instrução que a IA segue para analisar o atendimento. Nas palavras da tela, *"O conteúdo da conversa será enviado automaticamente após este prompt"*: você escreve só o que quer que a análise traga.

🔘 **RESTAURAR PADRÃO:** põe no campo o prompt padrão, que pede as objeções do cliente, os pontos de melhoria no atendimento, o sentimento geral e os KPIs — tempo de resposta, FCR (resolução no primeiro contato), CSAT estimado (satisfação do cliente) e necessidade de escalonamento.

🔘 **DESCARTAR ALTERAÇÕES:** volta ao que estava salvo. Enquanto há mudança sem salvar, a tela mostra *Alterações não salvas*.

🔘 **SALVAR CONFIGURAÇÕES:** grava o modelo e o prompt. A tela confirma *"Configurações do GPT Analyzer salvas com sucesso!"*

⚠️ O **RESTAURAR PADRÃO** só põe o texto no campo. Para valer, clique em **SALVAR CONFIGURAÇÕES**.

⚠️ A análise e o resumo usam a IA configurada pela empresa no menu **Integrações**. Quando o card avisa que a conta usa a chave da plataforma, não é preciso cadastrar uma chave ali.

> **[DUVIDAS]**
>
> #### Dúvidas Comuns
>
> **O botão Analisar Atendimento com IA não aparece na conversa.** O botão aparece com o atendimento aberto. Com a conversa em **Aguardando**, aceite o atendimento primeiro. Com a opção **Ações do topo do ticket** em **Agrupadas**, o botão fica no **Mais**, no grupo **IA e resumos**.
>
> **Analisar Atendimento com IA encerra o atendimento?** Não. A análise chega como nota interna e o atendimento continua aberto, com a equipe.
>
> **O cliente vê a análise ou o resumo do atendimento?** Não. A análise e o resumo entram na conversa como nota interna, só para a equipe.
>
> **Como mudo o que a Análise de Atendimento escreve?** No menu **GPT Análises**, reescreva o **Prompt de Análise** e clique em **SALVAR CONFIGURAÇÕES**. A mudança vale para as próximas análises.
>
> **Qual a diferença entre Analisar Atendimento com IA e Resumo do período?** A análise avalia o atendimento pelo **Prompt de Análise**: objeções, pontos de melhoria, sentimento. O resumo do período conta o que aconteceu nas mensagens do contato no intervalo escolhido: pedidos, pendências e próximos passos.
>
> **Quem pode usar a Análise de Atendimento?** O administrador, o supervisor e o atendente, na conversa com o atendimento aberto. O menu **GPT Análises**, que configura a análise, aparece para o administrador.

> **[ERROS]**
>
> #### Erros Comuns
>
> **O resumo do período chega como "Não foi possível gerar o resumo":** a nota interna diz o que falta na IA da empresa. **Solução:** o administrador corrige o que a nota aponta no menu **Integrações**, no card **Provedor de IA**: a chave vazia, a chave recusada ou o **Modelo** vazio.
>
> **Clicar em Restaurar Padrão e sair da tela:** o prompt padrão não fica gravado. **Solução:** depois do **RESTAURAR PADRÃO**, clique em **SALVAR CONFIGURAÇÕES**.
